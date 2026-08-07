# Foreign Trade Decision Skill

An AI-assisted decision workflow for foreign trade sales.

Book explains the thinking.  
Skill runs the workflow.  
You make the final judgment.

---

这是《让客户敢下单》配套的 **可执行工作工具**，不是书的全文电子版。

把真实询盘、客户邮件、报价问题、技术包、样品反馈或供应商问题丢进来，Skill 会按统一判断框架告诉你：**现在最值得做什么、找谁验证、什么可以承诺。**

Skill 内部名称：`trade-judgment`  
仓库名称：`first-principle-in-foreign-trade-skill`

---

## What it does

- 新询盘分析
- 客户背调
- 报价准备
- 技术包检查
- 样品反馈
- 客户跟进与沉默判断
- 供应商可靠性
- 谈判和拒绝
- 战略客户内部升级
- 项目复盘归档

默认是 **Action Mode**（告诉你现在做什么），不是读书模式。

---

## Core workflow

```text
Raw input
↓
Fact / Inference / Unknown
↓
Company Context
↓
Biggest blocker
↓
Next smallest effective action
↓
Reality verification
↓
Commitment boundary
↓
Customer reply if requested
```

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

Biggest blocker:
Product specification is not sufficient for reliable costing.

Next action:
Ask only the 2 variables that will materially change price.

Reality verification:
Customer + material supplier

Do not promise yet:
Final FOB price and delivery time
```

更多完整样例见 `examples/` 与 `references/golden-examples.md`。

---

## Installation / Use

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
```

---

## Contributing

欢迎提交 bug、幻觉案例、新场景、跨行业适配与文档改进。见 [CONTRIBUTING.md](CONTRIBUTING.md)。

提交真实业务案例前，请先脱敏。

---

## License

本仓库采用 [Apache License 2.0](LICENSE)。

Copyright 2026 Alex

该许可仅覆盖本仓库内的 Skill 文件、规则与脱敏示例。  
《让客户敢下单》书籍全文及未公开书稿**不在**本许可范围内，版权仍由权利人保留。

---

## Disclaimer

本工具协助降低信息处理的不确定性，不替代业务员、管理层或法务的最终责任。对外报价、交期、认证与合规承诺，必须以你们公司核实后的事实为准。
