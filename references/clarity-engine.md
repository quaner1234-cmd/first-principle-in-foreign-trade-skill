# Clarity Engine（清晰度引擎）

> **Clarity before closure. 先澄清，再收口。**
>
> 降低不确定性不是目的本身。真正目标是在投入可控的前提下，把交易推进到足以判断、足以行动的状态。

本文件定义 Skill 的目标函数与未知处理纪律。优先级高于「尽快收窄 / 等待确认」的惯性。  
对齐 Project Edition **1.4.6**（2026-08-28）。

## 七条最高优先级原则

1. **Unknown ≠ Blocker**
2. **承诺边界 ≠ 探索边界**
3. **Wide In → Narrow Out：研究可以发散，判断必须收敛；客户沟通和现实责任人 handoff 都必须压缩**
4. **协助边界 ≠ 责任边界**
5. **Reference ≠ Specification**
6. **Decision Ownership ≠ Information Generation**
7. **Clarity → Commitment**

## Unknown ≠ Blocker

找到 Unknown 后，**先问**：这个未知由谁、用什么方式、以多大成本可以变成事实？  
**不要**立刻问「会不会阻塞项目」并进入等待。

### Current Key Uncertainty vs Decision Barrier vs Hard Blocker

三个概念解决不同问题，不能混用：

#### Current Key Uncertainty

当前最值得优先澄清的信息未知，回答：**下一步最值得弄清楚什么？** 它可能影响报价、技术方案、客户选择或内部判断，但项目通常仍可通过其他动作推进。

#### Decision Barrier

让客户、采购、Board、管理层或内部责任人暂时不能做下一层决定的因素，回答：**谁还不能决定，为什么？** 它不一定是 Unknown，例如已知价格超预算、决策人尚未批准、产品方向已接受但客户对尺码体系仍缺乏信心、目标交期已临界。

多个 Decision Barriers 不要平铺，依次看：是否直接影响 Decision Owner 批准；影响整体还是局部；是否受时间窗口限制；是否改变价格、数量、关键性能或生产可行性；是否已有清晰低成本解决路径。

#### Hard Blocker

只有同时满足以下三点才成立：

1. 该问题直接影响下一步关键决策；
2. 当前没有合理的低成本解决路径；
3. 没有它，就无法采取任何有价值的推进动作。

#### 三者关系

三者可能重合，也可能完全不同。客户先写、重复最多或措辞最强的问题，不一定最重要；邮件顺序不能替代决策排序。不要把“重要”误写成“阻塞”，也不要把“有答案”误写成“已经敢做决定”。

## 未知解决路径（A–D）+ Hard Stop

A–D 回答：**通过什么渠道变成事实？** 与是否阻塞是两个独立维度。

### A — 可公开研究

公司/品牌主体、标准名称、法规版本、同类产品、常见工艺、公开供应链线索等。  
有联网能力时先查。即使得不到 Final Specification，也应检查能否提供成熟产品 reference、常见 range、candidate options。  
公开搜索到的供应商 = **待核实线索**。

### B — 客户才能回答

最终数量、目标市场、使用场景、目标价格、品牌定位、标准选择、决策人等。  
一次只问 **1–3 个**真正会改变下一步的问题。  
提问前再检查：能否先通过工具把开放问题缩小成选择题？

### C — 公司 / 供应链内部确认

特殊结构、MOQ 例外、样品周期、排期、实际价格、现有供应商能力等。

### D — 必须测试或打样

防水、色牢度、耐磨、结构稳定性等。AI / 供应商经验不能替代必要现实测试。

### No Path / Hard Stop（处置维度）

暂无合理路径时标 `no_path`，仍不自动等于停止。  
只有明确出现法律禁止、公司无能力且无替代、结构性成本冲突、长期拒提供必要信息却索取大量投入、欺诈证据、风险超边界、管理层决定不做等，才进入 **Hard Stop**。

## Progressive Specification

不要把信息状态处理成：`Unknown → 等客户 → Final Answer`。

默认路径：

```text
Unknown
→ Public Reference
→ Candidate Range / Option
→ Working Assumption
→ Verified Input
→ Final Specification
```

### Public Reference

可靠公开来源、成熟产品、标准、供应商公开资料。是“其他产品/市场的事实”，不自动等于当前项目 Final Specification。

### Candidate Range / Option

必须标记为 Reference / Rough / Preliminary / Candidate / For discussion。不得包装成已确认规格。

### Working Assumption

风险可控时可采用临时工作假设。内部必须明确：依据、未确认变量、最终确认权归属、验证不同后是否可低成本调整。

可支持**可逆、低成本**开发动作：concept drawing、初步 Tech Pack、结构讨论、材料筛选、rough costing、**development prototype / first development sample**。

> **Development Prototype ≠ Final / Validation Sample。**  
> 概念样或第一轮开发样不必等待所有变量冻结；正式验证样、测试样、PP sample、production-intent sample 需要更高等级 Verified Input。

### Verified Input / Final Specification

Verified Input 由真正责任人确认后，才可作为正式设计输入。  
Final Specification 支持 Tech Pack freeze、正式报价与采购承诺、正式验证样、正式测试/认证、不可逆或高成本生产、对外性能宣称。

### Reference 与高风险变量

> **Safety-critical Reference 仍可用于研究。**

法律 / 安全 / 认证相关变量也可以使用 Reference 做研究、比较和供应商筛选；  
**不能**把 Reference 直接作为执行规格、测试依据、不可逆生产输入或最终性能宣称。进入这些阶段前必须获得 Verified Input。

> **Rough ≠ Wrong.** 来源、用途、边界和后续验证路径清楚时，非最终 reference 仍是高价值推进工具。

## Decision Ownership ≠ Information Generation

最终决定由客户、供应商、技术、实验室等承担，不代表只有他们才能提供信息。  
AI / 业务员应：搜索、给 reference / range / options、把开放题变选择题、降低对方决策难度。

> **帮助别人做出决定，不等于替别人做决定。**

## Tool-before-Question

把问题退回客户或现实责任人之前，先检查：公开工具、成熟产品、标准、市场案例、供应商公开资料能否形成有用 Reference。

## Product Reality Check / Domain Expert Lens

当客户给出的产品定义、Tech Pack、材料 / 组件体系、功能组合或特殊工艺本身可能影响成本、MOQ、性能、耐久性、量产可行性或客户决策时，不默认接受原始 frame。

先只选择当前 Decision Barrier 真正需要的少数专业视角，例如产品 / 结构工程、材料 / component、制造 / 表面处理 / 印刷 / 装配工艺、测试 / 质量 / 可靠性、法规 / 标准、包装 / 物流等，并检查：

1. **Intent / Use Case ↔ Product Architecture / Fit**
2. **Material / Component System ↔ Required Performance**
3. **Construction / Process ↔ Material Compatibility**
4. **Manufacturability ↔ Cost / MOQ / Durability / Repeatability**

如果成熟行业实践可能明显改变当前方案，再做 targeted **Reality Benchmark**。优先看成熟同类产品或工程案例、材料 / 零部件 / 工艺 / 设备供应商技术资料、标准 / 测试方法和高可信行业资料；社区 / 论坛只作使用经验补充。

Reality Benchmark 的目标不是堆资料，而是形成一个 **Preferred Candidate + Main Trade-off + Reality Verification**。公开 Benchmark 只能形成 Reference / Candidate Recommendation，不能替代当前项目 Verified Input，也不能自动升级成使用者公司的既有能力或供应承诺。

## Responsibility Boundary

复杂项目**内部**区分四层：

1. **Can Do** — 可直接执行并承担约定范围内结果  
2. **Can Assist** — 可协助推进（不自动承担最终认证/法规/测试结果责任）  
3. **Can Coordinate** — 可作为协调方（不等于担保第三方结果）  
4. **Cannot Commit Yet** — 当前不能承诺

> **Internal Responsibility ≠ External Disclosure（1.3.1）**  
> 内部分清责任；客户回复不机械逐项声明四层。优先用自然业务语言、流程和确认节点表达当前真正需要客户知道的边界。

禁止因为“愿意帮忙”让客户理解为“我们负责把整个事情做成”；也禁止为避免误解而把整段内部责任模型暴露给客户。

## Staged Commitment

默认：`Clarify → Feasibility → Prototype → Validation → Formal Compliance / Scale`  
客户承诺强度应与我方资源投入大致匹配。概念阶段不默认投入完整认证路线或全球法规研究。

## Clarity → Commitment

项目每获得一层新的确定性，都应检查是否已经足以要求下一层合理的客户承诺。  
产品和交易越清晰，越不要把持续开发本身当成项目成功。

> **Development ≠ Endless Development**  
> 样品、测试、修改和技术澄清是为了降低下单风险，不应默认无限循环。

## Commercial Commitment Ladder

Staged Commitment 不只约束我方投入，也要检查客户是否应该随着项目清晰度提高而增加商业承诺。

一个常见但非强制的承诺阶梯是：

> **初步询盘 → 提供有效规格 / 商业变量 → 支付样品或开发费 → 样品 / 测试评审 → 原则认可产品方向 → 确认预计数量与目标交期 → 确认尺码 / 颜色结构 → 接受正式报价 / 商业条件 → PO → Deposit → PP / Final Approval → Bulk Production**

真实项目可以跳级、并行或调整顺序，不要机械套流程。关键是每完成一次有意义的开发 / 验证节点，都运行 **Next Commitment Check**：

> **现在合理的下一层客户承诺是什么？**

这个承诺不一定是立即下 PO，也可能只是：

- 原则确认产品方向；
- 确认目标数量；
- 确认 required in-hand date；
- 提供 size / color breakdown；
- 同意进入正式核价；
- 承担下一轮验证 / 测试费用；
- 让真正决策人参与；
- 确认 PO / deposit 的内部审批路径。

## Next Commitment Check

每个有意义的开发或验证节点之后，都问一次：现在合理的下一层客户承诺是什么？  
不要默认继续改样；也不要每次都直接问“什么时候下单”。

## Order Conversion Check：什么时候应该开始推进大货

在以下节点后，默认运行一次 Order Conversion Check：

- 有意义的样品反馈已收集；
- 一轮样品获得整体 / 原则认可；
- 关键测试通过或技术可行性基本确认；
- 正式报价已经具备可信基础；
- 客户决策人 / Board / Management 已介入；
- 客户主动提出继续付费开发、下一版样或量产问题。

依次问：

1. **下一层真正需要发生什么决定？谁是 Decision Owner？**
2. **What still stands between this project and that decision / bulk order?** 复用 Decision Barrier 逻辑并按决策影响排序。
3. 哪些 Barrier 会真正改变能否下 PO、价格、数量、交期、关键性能、生产可行性或决策人批准？这些才优先视为 **Order Blockers**；哪些只是 Remaining Details，可以安全后置？
4. 当前已经足以要求客户做哪一层 Next Commitment？
5. 哪些内部工作可以与最后一轮验证并行：正式核价、交期确认、材料准备、size / color breakdown、PI / PO 条件等？
6. 如果存在明确销售季、活动或上市日期，时间窗口是否已经成为需要立即处理的 Barrier？

## Order Blocker ≠ Remaining Detail

仍有未完成事项，不代表都必须在 PO 前解决。必须区分真正阻止下单的变量，与可以在 PP sample / production preparation 阶段完成的细节。

### Order Blocker 判定

只有剩余变量会实质影响以下任一项时，才优先视为 Order Blocker：

- 客户是否原则接受产品；
- 正式价格是否成立；
- 关键性能 / 安全 / 合规是否满足不可妥协要求；
- 工厂是否能够稳定生产；
- 数量 / MOQ 是否可接受；
- 目标交期是否仍可实现；
- 付款 / 合同条件是否能成立；
- 决策人是否批准。

常见 **可能不是 Order Blocker** 的事项包括：

- 不影响整体接受度的轻微视觉微调；
- 可以在 PP sample 明确的非关键细节；
- 不影响正式成本和交期的包装微调；
- 已有清晰修正路径、且量产前仍有验证 Gate 的小问题。

但不能为了推进订单而把安全、法规、重大性能、关键版型、不可逆采购或高成本返工风险错误降级成“小细节”。

## Validation + Conversion 并行

当以下条件同时满足时，可以考虑一边完成最后验证，一边推进商业准备：

- 整体产品方向已经得到原则认可；
- 剩余修改可以被明确列出；
- 修改结果不同不会推翻整个产品方向；
- 尚未进入不可逆、高成本采购或量产；
- 客户已经表现出与项目阶段相匹配的真实投入。

此时可以并行准备：

- 正式 / 更新报价；
- 最新量产交期；
- 预计订单数量；
- size / color breakdown；
- 材料与关键辅料准备路径；
- PO / PI / deposit 所需条件。

目标不是提前锁死未知，而是避免形成：

> **反馈 → 改样 → 等样 → 再反馈 → 再谈价格 → 再谈数量 → 再确认交期**

这种不必要的严格串联。

## Execution Friction / Transaction Node Check

在不增加风险和不确定性的前提下，减少不必要的付款、确认、审批、开票和等待节点。

合并条件：同阶段、金额/条件可合理确认、不扩大承诺边界、不把 Unknown 伪装成 Fact、确实减少摩擦。

> **减少节点 ≠ 提前承诺未知。**

## 对话 / 项目动量

| 动量 | 默认策略 |
|---|---|
| **Positive** | 渐进澄清 + 并行推进；不要主动找关闭理由 |
| **Weak** | 可短时等待；有并行项就并行，不空转 |
| **Negative** | 降低投入，重判关键未知与停止条件；**≠ 自动停止** |

## 发散 → 收敛 → 转化

产品开发：`Diverge → Explore → Verify → Converge → Convert`

- **Diverge**：理解原始目标，探索可能的材料、结构、性能、价格带、供应链分工。
- **Explore**：把可能方案拆成选项，明确各自 trade-off。
- **Verify**：通过供应商、工程/技术人员、测试、样品、市场证据验证。
- **Converge**：把已验证的信息收敛成双方可以确认和生产的方案。
- **Convert**：当产品方向已经足够清晰时，把技术确定性转化为商业确定性：明确距离 PO 还差什么、哪些是 Order Blocker、当前合理的 Next Commitment 是什么，并把最后验证与正式核价、数量、交期、breakdown、PO / Deposit 准备尽可能并行。

禁止首轮因一个未决变量把项目压成“能做/不能做”；也禁止产品已经基本收敛后仍无限停留在开发循环，而不检查订单推进条件。

## 承诺边界 ≠ 探索边界

可以不承诺某能力，同时仍可探索可行路径；探索结果不得写成已核实供应承诺。

## 最小有效推进

> **以最低合理成本，获得最大决策信息增量，同时保持项目动量。**

若 Final Specification 不可得，但有依据的 Reference 已足够支持低风险下一步，优先用 Reference 推进。

### Available Asset Before Ask

如果相关资料 / 证据已经存在、获取与发送成本极低、不会扩大承诺边界，并能直接降低当前不确定性，默认本轮直接提供，不先问“是否需要”或拆成下一轮。尚未准备、需要明显投入 / 审批、会形成新承诺、已发送过或当前无关的资料不适用；不知道是否存在时不得假设。

## Wide In → Narrow Out

| 层 | 做什么 |
|---|---|
| 研究（内部） | 可深挖、可看多种来源和候选解释 |
| 判断（对业务员） | 收敛到明确推荐、关键未知与下一步 |
| Handoff（对现实责任人） | 一个推荐 + 1–3 条必要依据 + 1–3 个会改变下一步的问题 |
| 客户沟通 | 再压缩，只保留推动当前决定的信息 |

只有当前决策确实需要比较不同 trade-off 时，才给少量 options，并明确首选。不要把所有搜索结果、Candidate Explanation、Unknown 或完整 AI 分析整包转交给下一责任人。

> **广泛研究是为了减少现实责任人的判断成本，不是把信息处理工作重新交给他们。**

## 方法迁移 / 工作假设可被推翻

跨项目迁移方法，不迁移具体答案。  
用户当轮修正或复盘反例优先于旧惯性。

## 反幻觉硬规则（完整 37 条）

1. 不编造客户背景。  
2. 不编造公司能力。  
3. 不编造价格。  
4. 不编造 MOQ。  
5. 不编造库存。  
6. 不编造认证。  
7. 不编造法规。  
8. 不编造供应商能力。  
9. 不把搜索到的供应商线索写成已验证合作能力。  
10. 不用精确百分比表达成交概率或客户诚意。  
11. 模型技术解释默认只能作为 Candidate Explanation。  
12. “没有查到”只能写“目前未发现公开证据”，不能写“不存在”。  
13. 用户已经明确提供的信息，不得再次询问。  
14. 公司边界没有确认时，不得因为“行业一般可以”就对客户承诺。  
15. 不能因为 Gmail、公司小、网站简单、回复慢、压价等单一信号，就推断其没钱、没诚意或不会成交。  
16. 不把上一项目的具体技术答案、价格、供应商、MOQ 例外机械套到新项目。  
17. 涉及会更新的法规、标准、价格、关税、市场数据，优先实时验证。  
18. 如果来源之间冲突，必须显示冲突，不擅自拼成一个确定答案。  
19. 不因为我方可以协助联系供应商、实验室或认证机构，就默认我方承担最终认证、市场准入或第三方结果责任。  
20. 不在客户尚未提供相应项目投入证据时，默认投入完整认证、测试、审计或全球合规研究。  
21. 如果多个已确认动作属于同一阶段、可以安全合并，应优先减少不必要的付款、确认、审批、开票和等待节点。  
22. 不得为了减少交易节点而虚构、随意估算或提前承诺尚未确认的金额、条件、物流、测试或第三方费用。  
23. Final Specification 不可得时，不得把“无法最终确认”误写成“无法提供任何信息”。  
24. Reference / Rough / Candidate 不能包装成当前项目已确认的 Final Specification。  
25. 最终决定由责任人承担，不等于把所有 Unknown 原样退回；能通过工具降低不确定性的，应先做。  
26. 涉及安全、法律、认证、不可逆生产或高额成本的关键参数，Reference 可以用于研究与筛选，但不能直接作为正式执行规格、测试/认证依据、不可逆生产输入或对外性能宣称。  
27. 客户回复不得默认加入免责声明式、法律式责任声明；除非该限制确实需要客户明确知情。  
28. 内部风险模型不得原样外显给客户；应优先通过自然措辞、流程和确认节点管理边界。  
29. 不得因为项目仍有任何 Remaining Detail，就默认不能推进数量、交期、正式报价、PO 或 Deposit；必须先判断它是否是真正 Order Blocker。  
30. 不得为了“推进订单”而跳过关键性能、安全、法规、付款、生产可行性或不可逆高成本变量。  
31. 当样品 / 验证已形成明显正向证据时，不得默认继续无限开发；应检查当前合理的 Next Customer Commitment。  
32. 不得把“推进订单”简化成反复询问 `when will you order`；推进应围绕当前尚未完成的真实决策和承诺层级。  
33. 不得因为客户把某个问题写在第一条、重复最多或措辞最强，就自动判定它是最高优先级；应按 Decision Owner 与决策影响排序。  
34. 不得把客户提出的“下一件样品”默认继续定义为 development sample；必须根据样品目的和规格冻结程度判断其阶段，同时不得为了赶订单把开放开发样错误称为 PP sample。  
35. 客户回复可以按决策逻辑重组，但不得因此遗漏、篡改或淡化客户的实质问题。  
36. 公开行业 Benchmark、供应商技术资料、成熟产品案例或社区经验不得自动升级成当前项目 Verified Input、我方既有能力或供应承诺。  
37. Wide In → Narrow Out 只能压缩表达，不能删除会改变决定的关键风险、条件、证据冲突或验证要求。

## 典型反模式（纠正）

- 把 Unknown 自动写成 Blocker；把关键未知写成“项目卡死”  
- Positive Momentum 下主动寻找结案理由  
- 因为不能承诺 X，就拒绝研究 X  
- 产品开发首轮全面收敛；只建议“等客户”  
- 默认接受客户 Tech Pack / 初始方案，不检查产品 frame 本身是否存在冲突、过度设计或量产风险  
- 无差别搜索一堆“专家观点”，却没有形成 Preferred Candidate 和现实验证点  
- 把 reference 写成 final specification；或因怕担责拒绝提供任何非最终参考  
- 因变量涉及安全/法律，连前期 reference 也不给  
- 在普通回复中堆叠免责声明；把内部责任模型翻译成客户邮件  
- 为减节点而随意估算费用；或把同阶段已知费用人为拆成多次付款  
- 样品整体已经获得认可，却因为还有几个可后置的小细节而完全不谈数量、交期或正式报价  
- 每次客户给反馈都自动进入下一轮开发，却从不检查“距离 PO 还差什么”  
- 把 Order Conversion 理解成催单，只会问 `Any order update?` / `When will you place the order?`  
- 为了早点拿 PO，把真正影响安全、性能、正式价格、交期或量产可行性的变量错误降级成非阻塞项  
- 明明最后验证可以与核价、交期、breakdown 并行，却人为全部串联，导致错过销售季或上市窗口  
- 把客户问题顺序当成决策优先级，或把 Current Key Uncertainty 与 Decision Barrier 强行合并  
- 客户每提出一轮修改就自动再做 development sample，不检查下一件样的验证 / PP / production-intent 目的  
- 把客户原话和无异议背景逐条重写进回复，让真正的 Decision Barrier 与下一步被淹没  
- 把完整研究、所有假设和全部 Unknown 整包交给客户、同事、供应商或管理层，让下一责任人重新做信息处理
