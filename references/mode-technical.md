# Mode 5 — Technical / Tech Pack（技术包与技术描述）

**触发**：技术包、规格、供应商或客户的模糊技术描述。

## 分析重点

- 矛盾（规格前后不一致）
- 缺失（幅宽？用量？材质？）
- 技术假设
- 能否验证
- 哪个是当前关键未知；它是否真的构成 Hard Blocker

## Technical Hypothesis 机制（本 Skill 与普通 Prompt 的最大区别）

当用户给出模糊技术描述时（例："这种蓝色尼龙晒牢度就是做不上去"），**AI 的任务不是直接宣布技术原因**，而是输出：

```markdown
### Original Observation
供应商的实际描述是什么。

### Candidate Explanation
AI 根据已有知识提出一个或多个可能机制（明确标注为假设，不是结论）。

### Evidence Needed
哪些证据能够验证或否定这个解释。

### Real-world Verification
应该问：面料厂？实验室？版师？工艺人员？客户？查标准？做实际测试？
```

原则：

> AI 的重要价值不是把模糊描述直接变成"事实"，而是把模糊问题转化成更精确、可验证的假设。

即：模糊事实 → AI 组织和解释 → 可验证假设 → 现实验证 → 新事实

## 技术结论边界

- "供应商说做不到"是说法，"第三方实验室证实"才是证据
- 模型知识中的技术解释默认只能作为 Candidate Explanation，除非有现实证据或可靠来源验证
- 优先验证“这个项目条件下能不能做”，不要轻易扩展成“全行业都这样”
- Final Specification 暂时不可得时，先检查能否从标准、成熟产品、公开资料或供应商型号得到 Reference / Range
- 客户自己也不知道开放技术问题时，不要要求客户从零回答；先把问题缩小成可选项
- 安全 / 法律 / 认证相关变量：Reference 仍可用于研究与供应商筛选，但不能直接作为执行规格、测试依据或性能宣称
- Development prototype 可基于可逆 Working Assumption 推进；正式验证样 / PP / production-intent 需要更高 Verified Input
- 技术边界不清时，给客户的是“待验证方案”，不是已确认承诺

## Progressive Specification（技术场景）

```text
Unknown → Public Reference → Candidate Range → Working Assumption → Verified Input → Final Specification
```

见 `references/clarity-engine.md`。

关键测试通过或技术可行性基本确认后，运行 **Order Conversion Check**（见 `mode-order-conversion.md`）。

## 供应链执行检查点

按独立状态跟踪：

`询价 → 合同 → 审批 → 付款 → 提货 → 投产 → 到货`

- 合同 ≠ 付款；准备请款 ≠ 已付款；安排投产 ≠ 已完成；盖章 ≠ 已锁定库存
- 不要靠联想推进事实状态

## 知识层

需要时加载：`chapters/ch07-技术与供应链.md`、`references/clarity-engine.md`
