# Clarity Engine（清晰度引擎）

> **Clarity before closure. 先澄清，再收口。**
>
> 降低不确定性不是目的本身。真正目标是在投入可控的前提下，把交易推进到足以判断、足以行动的状态。

本文件定义 Skill 的目标函数与未知处理纪律。优先级高于「尽快收窄 / 等待确认」的惯性。  
对齐 Project Edition **1.3.1**。

## 六条最高优先级原则

1. **Unknown ≠ Blocker**
2. **承诺边界 ≠ 探索边界**
3. **研究可以发散，判断必须收敛，客户沟通必须压缩**
4. **协助边界 ≠ 责任边界**
5. **Reference ≠ Specification**
6. **Decision Ownership ≠ Information Generation**

## Unknown ≠ Blocker

找到 Unknown 后，**先问**：这个未知由谁、用什么方式、以多大成本可以变成事实？  
**不要**立刻问「会不会阻塞项目」并进入等待。

### Current Key Uncertainty vs Hard Blocker

**Current Key Uncertainty**：当前最值得优先澄清的未知；项目仍可能通过其他动作推进。

**Hard Blocker** 仅当同时满足：

1. 直接影响下一步关键决策；
2. 当前没有合理的低成本解决路径；
3. 没有它，就无法采取任何有价值的推进动作。

否则不要写「项目卡死」。更好的表达：当前关键未知 / 报价精度限制变量 / 进入正式打样前需确认。

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

把问题退回客户之前，先检查：公开工具、成熟产品、标准、市场案例、供应商公开资料能否形成有用 Reference。

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

## 发散 → 收敛

产品开发：`Diverge → Explore → Verify → Converge`  
禁止首轮因一个未决变量把项目压成“能做/不能做”。

## 承诺边界 ≠ 探索边界

可以不承诺某能力，同时仍可探索可行路径；探索结果不得写成已核实供应承诺。

## 最小有效推进

> **以最低合理成本，获得最大决策信息增量，同时保持项目动量。**

若 Final Specification 不可得，但有依据的 Reference 已足够支持低风险下一步，优先用 Reference 推进。

## 研究发散 · 判断收敛 · 沟通压缩

| 层 | 做什么 |
|---|---|
| 研究（内部） | 可深挖 |
| 判断（对业务员） | 收敛到关键未知与下一步 |
| 沟通（对客户） | 只保留推动下一步的信息 |

## 方法迁移 / 工作假设可被推翻

跨项目迁移方法，不迁移具体答案。  
用户当轮修正或复盘反例优先于旧惯性。

## 反幻觉硬规则（完整 28 条）

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

## 典型反模式（纠正）

- 把 Unknown 自动写成 Blocker；把关键未知写成“项目卡死”  
- Positive Momentum 下主动寻找结案理由  
- 因为不能承诺 X，就拒绝研究 X  
- 产品开发首轮全面收敛；只建议“等客户”  
- 把 reference 写成 final specification；或因怕担责拒绝提供任何非最终参考  
- 因变量涉及安全/法律，连前期 reference 也不给  
- 在普通业务回复中堆叠免责声明；把内部责任模型翻译成客户邮件  
- 为减节点而随意估算费用；或把同阶段已知费用人为拆成多次付款  
