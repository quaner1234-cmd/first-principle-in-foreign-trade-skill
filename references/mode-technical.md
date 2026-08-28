# Mode 5 — Technical / Tech Pack（技术包与技术描述）

**触发**：技术包、规格、供应商或客户的模糊技术描述。

## 分析重点

- 矛盾（规格前后不一致）
- 缺失（关键尺寸、材料、性能、用量、工艺条件等）
- 产品 / 技术方案本身是否合理
- 技术假设
- 能否验证
- 哪个是当前关键未知；它是否真的构成 Hard Blocker

## Product Reality Check / Domain Expert Lens

当 Tech Pack / 产品方案较复杂、客户对方案本身不确定、多个功能可能冲突或过度设计，或某个选择会显著影响成本、MOQ、性能、耐久性、量产稳定性或客户决策时，**不要默认接受客户原始 frame**。

只选择当前 Decision Barrier 真正需要的少数专业视角，例如：

- 产品 / 结构工程、版型 / fit（适用时）
- 材料 / 配方 / component specialist
- 制造 / 表面处理 / 印刷 / 装配等工艺 specialist
- 测试 / 质量 / 可靠性 specialist
- 法规 / 标准 / 包装 / 物流 specialist（仅在当前决策相关时）

优先检查：

1. **Intent / Use Case ↔ Product Architecture / Fit**
2. **Material / Component System ↔ Required Performance**
3. **Construction / Process ↔ Material Compatibility**
4. **Manufacturability ↔ Cost / MOQ / Durability / Repeatability**

如果成熟行业实践可能明显改变方案，再按 Tool-before-Question / Progressive Specification 做 targeted **Reality Benchmark**。优先看：

1. 成熟同类产品或公开工程案例；
2. 材料、零部件、工艺、设备供应商的技术资料；
3. 标准、测试方法、官方或高可信行业资料；
4. 社区 / 论坛 / 用户经验仅作使用反馈补充，不作为工程规格依据。

输出默认收敛为：

- **Preferred Candidate**：一个明确首选；
- **Main Trade-off**：当前最重要的代价 / 风险；
- **Reality Verification**：当前项目还需谁确认、做什么测试或拿什么证据。

只有当前决策确实需要比较不同 trade-off 时，才给 2–3 个 options，并明确首选。公开 Benchmark 只能形成 Reference / Candidate Recommendation，不能替代当前项目的 Verified Input，也不能自动升级成使用者公司的既有能力或供应承诺。

## Technical Hypothesis 机制

当用户给出模糊技术描述时（例："这种蓝色尼龙晒牢度就是做不上去"），**AI 的任务不是直接宣布技术原因**，而是输出：

```markdown
### Original Observation
供应商、客户、样品或测试报告实际描述了什么。

### Candidate Explanation
AI 根据已有知识提出一个或多个可能机制（明确标注为假设，不是结论）。

### Evidence Needed
哪些证据能够验证或否定这个解释。

### Real-world Verification
应该问材料/零部件供应商？实验室？工程/技术人员？客户？查标准？做实际测试？
```

原则：

> AI 的重要价值不是把模糊描述直接变成"事实"，而是把模糊问题转化成更精确、可验证的假设。

即：模糊事实 → AI 组织和解释 → 可验证假设 → 现实验证 → 新事实

## 技术结论边界

- "供应商说做不到"是说法，测试、工程验证或其他可靠现实证据才决定当前项目能否成立
- 模型知识中的技术解释默认只能作为 Candidate Explanation，除非有现实证据或可靠来源验证
- 优先验证“这个项目条件下能不能做”，不要轻易扩展成“全行业都这样”
- Final Specification 暂时不可得时，先检查能否从标准、成熟产品、公开资料或供应商型号得到 Reference / Range
- 客户自己也不知道开放技术问题时，不要要求客户从零回答；先把问题缩小成可选项
- 安全 / 法律 / 认证相关变量：Reference 仍可用于研究与供应商筛选，但不能直接作为执行规格、测试依据或性能宣称
- Development prototype 可基于可逆 Working Assumption 推进；正式验证样 / PP / production-intent 需要更高 Verified Input
- 技术边界不清时，给客户的是“待验证方案”，不是已确认承诺

## Wide In → Narrow Out（技术 Handoff）

如果最终仍需工程、采购、供应商、实验室或其他现实责任人确认，不把整份研究报告交给对方。默认压缩成：

1. **推荐方向**：一句话；
2. **必要依据**：1–3 条；
3. **待确认问题**：1–3 个，且答案会改变下一步。

只有对方确实需要时，再补完整研究、来源和备选方案。

## Progressive Specification（技术场景）

```text
Unknown → Public Reference → Candidate Range → Working Assumption → Verified Input → Final Specification
```

见 `references/clarity-engine.md`。

关键测试通过或技术可行性基本确认后，运行 **Order Conversion Check**（见 `mode-order-conversion.md`）。

## 供应链执行检查点

按独立状态跟踪：

`询价 → 合同 → 审批 → 付款 → 提货 / 备料 → 投产 → 到货`

- 合同 ≠ 付款；准备请款 ≠ 已付款；安排投产 ≠ 已完成；盖章 ≠ 已锁定库存
- 不要靠联想推进事实状态

## 知识层

需要时加载：与当前产品相关的章节、`references/clarity-engine.md`；不要为完整性加载无关行业资料。
