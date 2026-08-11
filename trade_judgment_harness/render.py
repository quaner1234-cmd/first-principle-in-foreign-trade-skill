STAGE_LABELS = {
    "new_lead": "New Lead",
    "qualified_inquiry": "Qualified Inquiry",
    "active_project": "Active Project",
    "re_engagement": "Re-engagement",
    "unknown": "Unknown",
}

MOMENTUM_LABELS = {
    "positive": "Positive",
    "weak": "Weak",
    "negative": "Negative",
    "unknown": "Unknown",
}

PATH_LABELS = {
    "public_research": "公开研究",
    "customer": "客户回答",
    "internal": "内部确认",
    "testing": "现实测试",
    "no_path": "暂无合理路径",
}

BLOCKER_LABELS = {
    "non_blocking": "非阻塞",
    "soft_blocking": "软阻塞",
    "hard_blocking": "Hard Blocker",
}


def render_decision(decision, run_id=None):
    lines = []
    if run_id:
        lines.extend(["运行：`{}`".format(run_id), ""])
    lines.extend(
        [
            "## 当前判断",
            "",
            decision["summary"],
            "",
            "- 项目阶段：{}（{}）".format(
                STAGE_LABELS.get(decision["project_stage"], decision["project_stage"]),
                decision["stage_basis"],
            ),
            "- 对话动量：{}（{}）".format(
                MOMENTUM_LABELS.get(decision["momentum"], decision["momentum"]),
                decision["momentum_basis"],
            ),
            "- Mode：{}".format(decision["primary_mode"]),
            "- 处置：{}".format(decision["disposition"]),
            "",
            "## 事实",
            "",
        ]
    )
    lines.extend(_bullets(["{} [{}]".format(item["claim"], item["source_ref"]) for item in decision["facts"]]))
    lines.extend(["", "## 推断", ""])
    lines.extend(
        _bullets(
            [
                "{}（依据：{}；{}）".format(
                    item["claim"], ", ".join(item["basis_source_refs"]), item["verification_status"]
                )
                for item in decision["inferences"]
            ]
        )
    )
    lines.extend(["", "## 当前关键未知", ""])
    if decision["unknowns"]:
        lines.extend(
            [
                "| 未知 | 解决路径 | 状态 | 谁负责 | 解决后改变什么 |",
                "|---|---|---|---|---|",
            ]
        )
        for item in decision["unknowns"]:
            lines.append(
                "| {} | {} | {} | {} | {} |".format(
                    _cell(item["description"]),
                    PATH_LABELS.get(item["resolution_path"], item["resolution_path"]),
                    BLOCKER_LABELS.get(item["blocker_status"], item["blocker_status"]),
                    _cell(item["owner"]),
                    _cell(item["decision_impact"]),
                )
            )
    else:
        lines.append("- 当前没有结构化关键未知。")
    lines.extend(["", "## 现在可以主动澄清什么", ""])
    lines.extend(_bullets(decision["proactive_clarifications"]))
    lines.extend(["", "## 下一步最小有效推进", ""])
    lines.extend(_numbered_actions(decision["next_actions"]))
    if decision["parallel_actions"]:
        lines.extend(["", "## 并行推进项", ""])
        lines.extend(_bullets([_action_text(item) for item in decision["parallel_actions"]]))
    lines.extend(["", "## 承诺边界", "", "### 现在可以说", ""])
    lines.extend(_bullets(["{} [{}]".format(item["claim"], ", ".join(item["source_refs"])) for item in decision["can_say"]]))
    lines.extend(["", "### 暂时不能承诺", ""])
    lines.extend(_bullets(decision["cannot_promise"]))
    lines.extend(["", "## 停止条件", ""])
    lines.extend(_bullets(decision["stop_conditions"]))
    if decision.get("customer_reply"):
        reply = decision["customer_reply"]
        lines.extend(
            [
                "",
                "## 客户回复草稿（发送前必须人工批准）",
                "",
                reply["body"],
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_run_status(run):
    lines = [
        "Run: {}".format(run["run_id"]),
        "Project: {}".format(run["project_id"]),
        "Status: {}".format(run["status"]),
        "Phase: {}".format(run["phase"]),
        "Turns: {}/{}".format(run["turn_count"], run["max_turns"]),
    ]
    if run["pending_tool_calls"]:
        lines.append("Pending:")
        for item in run["pending_tool_calls"]:
            lines.append("- {}: {} ({})".format(item["call_id"], item["tool_name"], item["wait_type"]))
    if run.get("error"):
        lines.append("Error: {}".format(run["error"].get("message", "unknown")))
    return "\n".join(lines) + "\n"


def _bullets(items):
    return ["- {}".format(item) for item in items] if items else ["- 无"]


def _numbered_actions(actions):
    return ["{}. {}".format(index, _action_text(item)) for index, item in enumerate(actions, 1)]


def _action_text(item):
    approval = "；需人工批准" if item["approval_required"] else ""
    return "{}（负责人：{}；风险：{}{}）".format(item["description"], item["owner"], item["risk"], approval)


def _cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")
