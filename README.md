# Foreign Trade Decision Skill

An AI-assisted decision workflow for foreign trade sales.

Book explains the thinking.  
Skill runs the workflow.  
You make the final judgment.

---

这是《让客户敢下单》配套的 **可执行工作工具**，不是书的全文电子版。

把真实询盘、客户邮件、报价问题、技术包、样品反馈或供应商问题丢进来，Skill 会按统一判断框架告诉你：**现在最值得做什么来推进清晰度、找谁验证、什么可以承诺、何时才该停止。**

Skill 内部名称：`trade-judgment`  
仓库名称：`first-principle-in-foreign-trade-skill`

当前 Skill 对齐 ChatGPT Project Edition **1.4.6（2026-08-28）**。1.4.6 不新增 Mode 或 Gate，重点补充 **Product Reality Check / Domain Expert Lens** 和 **Wide In → Narrow Out**：复杂产品/技术任务先检查客户原始 frame 是否合理，必要时用成熟行业实践做 targeted Reality Benchmark；研究可以宽，但给客户、同事、供应商或管理层的输出必须压缩成当前决定真正需要的推荐、依据和少量确认问题。此前 1.4.5 的 Decision Barrier、Sample Purpose、Reply the Delta、询盘国家/地区输出、Hard Constraint 与暂估变量分离等规则继续保留。

仓库另含 Runtime Harness：原 Skill 作为领域决策 Policy，Python Runtime 负责状态、Schema、工具权限、审批、恢复、审计与回归测试。1.4.6 未新增机器状态或审批节点，因此 Runtime schema 保持不变。完整说明见 [`RUNTIME.md`](RUNTIME.md)。

---

## What it does

- Clarity before closure：把不确定转化为可行动清晰度（不是尽快关单）
- Clarity → Commitment：产品越清晰，越要检查下一层合理的客户承诺
- Current Key Uncertainty ≠ Decision Barrier：先识别谁还不能做下一层决定、为什么，再按决策影响排序
- Product Reality Check：必要时先挑战客户原始产品 / 技术 frame，而不是直接照单执行
- Targeted Reality Benchmark：成熟同类产品、供应商技术资料、标准 / 测试方法可形成 Reference / Candidate Recommendation，但不能替代当前项目 Verified Input
- Wide In → Narrow Out：研究可以宽；给客户和现实责任人的 handoff 默认压缩成一个推荐 + 1–3 条依据 + 1–3 个高价值问题
- Progressive Specification：Unknown → Reference → Working Assumption → Verified Input → Final Spec
- Reference ≠ Specification；Tool-before-Question；Decision Ownership ≠ Information Generation
- 项目阶段自动识别 + 对话动量 + 未知解决路径 + 独立 Blocker 状态
- Order Conversion：样品/测试/报价节点后区分 Order Blocker 与 Remaining Detail；Validation + Conversion 可并行
- 责任边界（Can Do / Assist / Coordinate）内部严谨、对外自然（不默认免责声明堆叠）
- Reply Gate：仅在用户明确要求时生成客户话术
- Reply the Delta：覆盖必要事项，不复述无异议背景；邮件正文后提供内部发送前资料检查
- Sample Purpose Check：按探索 / 验证 / PP 目的判断下一件样，不按样品次数判断
- Hard Constraint ≠ Provisional Commercial Variable；Available Asset Before Ask
- Execution Friction：减少不必要交易节点，但不提前承诺未知
- 客户身份证据不足时的公开背调（只建事实，不打分）
- 询盘澄清、报价、技术包、样品、跟进、供应商、谈判、升级、复盘、大货推进

默认是 **Action Mode**（告诉你现在做什么），不是读书模式。

---

## Core workflow

```text
Raw input
↓
Identify customer / project + existing context
↓
Project stage + conversation momentum
↓
Buyer identity evidence / Company Context
↓
Fact / Inference / Unknown
↓
Current key uncertainty + decision owner / decision barriers
↓
Product Reality Check when the product/technical frame itself may affect the decision
↓
Targeted Reality Benchmark (only when mature practice could materially change the solution)
↓
Tool-before-Question → Progressive Specification
↓
Smallest effective advance + parallel tracks
↓
Wide In → Narrow Out handoff to customer / internal owner / supplier / lab / management
↓
Commitment + responsibility + execution-friction checks
↓
Order Conversion Check after a meaningful sample / quote / test / review node
↓
Customer reply only if requested (Reply Gate)
```

Skill 会自动判断项目阶段，**不要**让用户先选「新询盘还是老询盘」。  
**Unknown ≠ Blocker.** **Reference ≠ Specification.** **Wide In → Narrow Out.** 内部严谨，对外自然。

---

## Example

输入：

```text
Customer wants 500 jackets.
They sent reference photos but no fabric specification.
They want FOB price.
```

输出（核心结构）：

```text
Current judgment:
Clarify before formal quotation.

Facts:
- Quantity: 500 pcs
- Reference photos provided
- Fabric specification unknown

Current key uncertainty:
The fabric specification affects reliable costing.
Resolution path: customer clarification + material reference. Blocker status: soft blocking, not Hard Stop.

Product reality check (only if needed):
If the reference construction itself appears contradictory or over-specified, first compare mature product architecture and supplier technical guidance, then form a preferred candidate.

Next action:
Ask only the 1–3 variables that will materially change price or construction.

Internal / supplier handoff:
Preferred direction + 1–3 reasons + 1–3 questions that change the next step.

Do not promise yet:
Final FOB price and delivery time
```

更多完整样例见 `examples/` 与 `references/golden-examples.md`。

---

## Installation / Use

### Runtime Harness（推荐用于长期真实项目）

```bash
python3 -m trade_judgment_harness init
python3 -m trade_judgment_harness doctor
python3 -m trade_judgment_harness run --project demo-001 --input inquiry.txt
```

Runtime 需要配置一个 OpenAI-compatible API，或通过 command adapter 接入其他模型。它默认禁止自动发送外部消息。初始化、配置、暂停恢复和审批操作见 [`RUNTIME.md`](RUNTIME.md)。

如果只想在 Claude Code、Codex 或兼容 Agent Skills 的宿主中手动使用判断框架，可继续按下面的纯 Skill 方式安装。

### Download ZIP

1. 打开本仓库 GitHub 页面
2. 点击 **Code → Download ZIP**
3. 解压到本地任意目录
4. 按下方 First-run setup 复制公司上下文模板

适合不熟悉 Git 的业务员。

### Clone

```bash
git clone https://github.com/quaner1234-cmd/first-principle-in-foreign-trade-skill.git
```

### Claude Code / compatible Agent Skills

把整个 skill 目录放到你所用 AI 宿主支持的 skills / agents 目录中即可。

不同产品的安装路径可能不同，请以宿主文档为准。本仓库不绑定某一家私有路径。

核心要求只有：

1. 宿主能读取 `SKILL.md`
2. 能按需打开 `references/`、`chapters/` 等相对路径文件
3. 你本地有一份私有的 `company-context.local.md`（不要提交到公开仓库）

**不需要 API key。** 这是纯指令型 Agent Skill。

---

## First-run setup

复制：

```text
company-context.template.md
```

为：

```text
company-context.local.md
```

然后填写自己公司的最低必要信息。

第一次不用全部填完。**Unknown 比编造更好。**

### Minimum Context

- Company type
- Main products
- Core capabilities
- Capability boundaries
- MOQ / sample / lead-time 基本规则
- 哪些事情不能未经内部确认承诺

> Never commit your private company context, customer information, API keys, pricing data, supplier details, or internal policies to a public repository.

---

## Action Mode vs Learning Mode

**Action Mode（默认）**  
短输出、给判断、给动作。不讲书，不显示“第 X 章”。

**Learning Mode（可选）**  
你主动问“为什么？”“按书里怎么解释？”时，才补充框架与章节依据。

---

## AI boundary

> AI can recommend a judgment, but it does not own the judgment.

> Facts require evidence.  
> Inferences must stay labeled as inferences.  
> Unknowns should remain unknown until verified.

硬规则摘要：

- 不虚构公司能力、价格、库存、认证、交期、客户背景、供应商能力、法规
- 不用精确百分比表达成交概率
- 模型技术解释默认是 Candidate Explanation，必须经过现实验证
- 公开行业 Benchmark / 成熟产品 / 供应商技术资料只能形成 Reference / Candidate Recommendation，不能自动变成当前项目规格或我方能力
- Wide In → Narrow Out 只能压缩表达，不能删掉会改变决定的关键风险或验证要求

---

## Book relationship

This Skill is an executable companion to the book 《让客户敢下单》。

- 书负责解释“为什么这样判断”
- Skill 负责收到真实材料后跑工作流
- 人负责最终判断与对外承诺

本仓库公开的是可执行压缩版框架、决策规则与脱敏案例，**不是**整本书的全文。

---

## Repository layout

```text
SKILL.md                      # orchestrator / decision engine
company-context.template.md   # 公开模板（私有 local 不入库）
references/                   # 判断内核、输出契约、各 Mode
chapters/                     # 按需加载的方法论压缩材料
examples/                     # 脱敏输入→输出案例
patterns.md / cheatsheet.md / glossary.md
trade_judgment_harness/       # durable runtime / policy enforcement
schemas/                      # machine-readable input/output/state contracts
tests/                        # runtime and policy invariant regression tests
```

---

## Contributing

欢迎提交 bug、幻觉案例、新场景、跨行业适配与文档改进。见 [CONTRIBUTING.md](CONTRIBUTING.md)。

提交真实业务案例前，请先脱敏。

---

## License

本仓库采用 [MIT License](LICENSE)。

Copyright 2026 Alex

MIT 许可仅覆盖本仓库内的 Skill 文件、代码、规则与脱敏示例。
《让客户敢下单》书籍全文及未公开书稿**不在**本许可范围内，版权仍由权利人保留。

---

## Disclaimer

本工具协助降低信息处理的不确定性，不替代业务员、管理层、技术人员或法务的最终责任。对外报价、交期、认证、产品性能与合规承诺，必须以你们公司核实后的事实为准。
