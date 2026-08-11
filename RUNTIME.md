# Trade Judgment Runtime Harness 使用说明

这个 Runtime 把原来的纯指令 Skill 变成一个可恢复、可验证、可审计的本地执行系统。

它负责：

- 为每个客户项目保存结构化状态
- 先路由项目阶段和 Mode，再加载对应 Policy
- 强制模型返回 JSON Schema
- 在 Schema 之后继续执行外贸领域不变量校验
- 对工具执行实施 `allow / manual / approval / deny` 权限
- 每一步保存 checkpoint；进程中断后可继续
- 对写入操作使用 call id / idempotency key 防止重复副作用
- 保存不含原始业务正文的哈希链审计日志

核心 Runtime 默认**不会发送邮件、写 CRM 或替你作正式承诺**。`send_external_message` 在代码层默认为 `deny`。

## 1. 环境要求

- Python 3.9 或更高版本
- 一个支持 JSON 输出的模型接口

Runtime 本身只使用 Python 标准库，没有第三方 Python 依赖。

## 2. 初始化

在仓库根目录运行：

```bash
python3 -m trade_judgment_harness init
```

命令会创建两个不会被 Git 提交的本地文件：

- `harness.config.local.json`
- `company-context.local.md`

并创建私有状态目录：

```text
.trade-harness/
├── projects/     # 长期项目状态
├── runs/         # 每次运行 checkpoint
├── notes/        # 经批准写入的本地记录
├── audit/        # 哈希链审计事件
└── locks/        # 并发锁
```

先填写 `company-context.local.md`。不知道的字段保留 `Unknown`，不要补猜。

## 3. 配置模型

### OpenAI-compatible API

默认配置使用兼容 `/chat/completions` 和 `json_schema` 的接口。

在终端设置密钥和模型名：

```bash
export OPENAI_API_KEY="你的密钥"
export TRADE_HARNESS_MODEL="你的模型名称"
```

密钥只放在环境变量里，不要写入仓库或配置文件。

如果使用其他兼容服务，修改私有的 `harness.config.local.json`：

```json
{
  "provider": {
    "type": "openai_compatible",
    "base_url": "https://your-provider.example/v1",
    "endpoint": "/chat/completions",
    "model": "your-model",
    "api_key_env": "YOUR_PROVIDER_API_KEY",
    "strict_json_schema": true
  }
}
```

运行检查：

```bash
python3 -m trade_judgment_harness doctor --check-provider
```

### Claude、Gemini、本地模型或自定义网关

将 provider 改成 `command`：

```json
{
  "provider": {
    "type": "command",
    "command": ["你的模型包装程序", "--json"],
    "timeout_seconds": 120
  }
}
```

包装程序从 stdin 接收：

```json
{
  "purpose": "route 或 decide",
  "system_prompt": "...",
  "payload": {},
  "schema_name": "...",
  "schema": {}
}
```

并向 stdout 只输出符合传入 Schema 的 JSON。这样模型可以替换，Harness 的状态、权限、验证和审计层保持不变。

## 4. 开始一个真实项目

把询盘、聊天或项目材料保存为 UTF-8 文本，例如 `inquiry.txt`：

```bash
python3 -m trade_judgment_harness run \
  --project nordcommute-001 \
  --title "NordCommute recycled puffer" \
  --customer "NordCommute" \
  --input inquiry.txt
```

`--project` 是长期稳定的项目 ID，只能使用字母、数字、点、下划线和连字符。同一客户的同一项目后续继续使用这个 ID。

如果你明确要求生成客户回复草稿，再加：

```bash
--customer-reply
```

没有这个参数，Validator 会拒绝模型擅自生成客户回复。即使生成了草稿，也会强制标记为“发送前需要人工批准”。

也可以从 stdin 输入：

```bash
python3 -m trade_judgment_harness run --project demo-001 --input -
```

输入完成后按 `Ctrl-D`。

## 5. Runtime 暂停时怎么处理

### 等待公开研究、内部确认、供应商或测试结果

状态会显示类似：

```text
Status: waiting_tool_result
Pending:
- research_1: public_research (manual_result)
```

把结果保存为符合 `schemas/manual-tool-result.schema.json` 的 JSON，然后提交；纯文本会被当作无事实声明的摘要，不会自动升级成事实：

```bash
python3 -m trade_judgment_harness tool-result \
  --run RUN_ID \
  --call research_1 \
  --file research-result.json \
  --by Alex

python3 -m trade_judgment_harness resume --run RUN_ID
```

公开研究结果建议使用：

```json
{
  "summary": "完成本轮公开检索；以下只记录有直接来源的事实。",
  "facts": [
    {
      "claim": "查到的事实",
      "source_ref": "https://direct-source.example/page",
      "observed_at": "2026-08-09",
      "sensitivity": "public"
    }
  ],
  "not_found": [],
  "attachments": []
}
```

### 等待写入批准

状态会显示 `waiting_approval`。先查看 call 的工具名、参数和原因，再批准或拒绝：

```bash
python3 -m trade_judgment_harness approve-tool \
  --run RUN_ID --call CALL_ID --by Alex --reason "仅写本地项目记录"

python3 -m trade_judgment_harness resume --run RUN_ID
```

拒绝：

```bash
python3 -m trade_judgment_harness reject-tool \
  --run RUN_ID --call CALL_ID --by Alex --reason "不能对外发送"
```

拒绝结果会返回给模型，让它选择更安全的下一步，而不是悄悄绕过审批。

## 6. 查看状态和结果

```bash
python3 -m trade_judgment_harness status --run RUN_ID
python3 -m trade_judgment_harness render --run RUN_ID
python3 -m trade_judgment_harness project --project nordcommute-001
python3 -m trade_judgment_harness audit-verify
```

- `status`：看运行停在哪一步
- `render`：把结构化 Decision 转成人能快速阅读的 Markdown
- `project`：看累计事实、当前未知、承诺和待办
- `audit-verify`：检查审计事件是否被破坏或重排

如果模型/API 暂时失败，状态通常是 `failed_recoverable`，修复网络或配置后执行：

```bash
python3 -m trade_judgment_harness resume --run RUN_ID
```

## 7. 不连接 API 的本地演示

仓库自带确定性 Replay，不需要密钥：

```bash
python3 -m trade_judgment_harness run \
  --project demo-runtime-001 \
  --input examples/runtime/inquiry.txt \
  --replay examples/runtime/replay-basic.json
```

Replay 只用于演示和回归测试，不会进行真实模型推理。

## 8. 默认权限边界

| 工具 | 默认策略 | 含义 |
|---|---|---|
| `read_project_file` | allow | 只读项目根目录内文件 |
| `search_project_files` | allow | 只做字面文本搜索 |
| `write_runtime_note` | approval | 批准后写私有 Runtime 目录 |
| `public_research` | manual | 等人工或外部连接器返回来源 |
| `internal_verification` | manual | 等授权内部人员确认 |
| `supplier_inquiry` | manual | 核心 Runtime 不自动联系供应商 |
| `technical_test` | manual | 等现实测试结果 |
| `send_external_message` | deny | 核心 Runtime 永不自动发送 |

不要为了“更自动”直接把所有工具改成 `allow`。接入 Gmail、CRM 或审批系统时，应为每个写操作增加参数 Schema、权限、幂等键、审计事件和失败恢复测试。

## 9. 数据与安全

- `.trade-harness/`、本地配置和公司上下文已加入 `.gitignore`
- 状态文件默认权限为仅当前用户可读写
- 审计日志只存输入哈希、事件类型和决策哈希，不默认保存原始业务正文
- 项目状态和 Run checkpoint 会在本机保存原始输入，以支持恢复；请把电脑和磁盘权限纳入公司数据管理
- 客户邮件、网页和工具输出始终按“不可信业务数据”传给模型，不能改变 Runtime 权限
- 一次项目复盘只能生成候选规则，不能自动修改正式 Policy

## 10. 回归测试

```bash
python3 -m unittest discover -s tests -v
```

当前测试覆盖：正常完成、人工工具结果恢复、审批写入、幂等重放、禁止外部发送以及 Hard Blocker 结构约束。
