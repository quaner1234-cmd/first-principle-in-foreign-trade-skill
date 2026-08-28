# Decision Engine（统一判断内核）

所有场景都必须先运行同一个判断内核。对齐 Project Edition **1.4.6**。

## 流程

```text
RAW INPUT
↓
1. 识别客户 / 项目；读取已有对话与项目上下文
   - 持续项目 → 沿用已有事实，禁止当成全新 New Lead 重跑
↓
2. 判断项目阶段（四档 + Active Project 中的 Order Conversion / Pre-Bulk）+ 对话动量（Positive / Weak / Negative）
   - project-stage.md / clarity-engine.md
   - 不确定且会改变下一步 → 只问一个前序问题
↓
3. 选择主 Mode（复合输入只选一个主 Mode，其余作辅助）
↓
4. Buyer Identity Evidence 是否充分？
   - 不足 → 公开背调（只建事实层）；充分 → 不重复；新风险 → 增量
↓
5. 读取 Company Context（承诺边界；≠ 探索边界）
↓
6. 合并证据 → 事实 / 推断 / 未知
↓
7. Unknown 解决路径（A 公开 / B 客户 / C 内部 / D 测试 / No Path）
↓
8. Current Key Uncertainty
   - 类型、谁最终确认、是否 Hard Blocker
↓
9. 若当前存在明确的客户 / 内部下一层决定：识别 Decision Owner 与 Decision Barriers
   - 回答“谁还不能决定、为什么”，并按决策影响排序；不要把所有 Unknown 都改写成 Barrier
↓
10. Product Reality Check（仅在产品 / 技术 frame 本身可能影响当前决定时触发）
    - 选择少数相关 Domain Expert Lens；检查 use case、产品架构、材料/组件、工艺、量产、成本/MOQ/耐久性的逻辑是否一致
    - 若成熟行业实践可能明显改变方案，再做 targeted Reality Benchmark
↓
11. Tool-before-Question + Progressive Specification
    - 先查公开工具 / 成熟产品 / 标准 / 供应商技术资料
    - 若 Reference 足以支持当前推进 → Public Reference / Candidate Range / Working Assumption
    - 再判断何时必须获得 Verified Input / Final Specification
↓
12. 对仍需客户决策的 B 类未知：只问 1–3 个高信息价值问题
↓
13. Smallest Effective Advance + 并行推进项
    - Available Asset Before Ask：检查是否有现成、相关、低成本且不扩大承诺的资料 / 证据可在本轮直接提供
↓
14. 承诺边界
    + Responsibility Boundary（内部：Can Do / Assist / Coordinate / Cannot Commit Yet）
    + Staged Commitment（投入是否与阶段和客户投入证据匹配）
    + Execution Friction / Transaction Node Check
↓
15. Wide In → Narrow Out
    - 研究可以宽；给客户 / 内部责任人 / 供应商 / 管理层的 handoff 必须窄
    - 默认：一个推荐 + 1–3 条必要依据 + 1–3 个会改变下一步的问题
    - 只有决策确实需要比较 trade-off 时才给少量 options，并明确首选
↓
16. Order Conversion Check（刚完成有意义的报价 / 样品 / 测试 / 评审 / 技术收敛节点时）
    - 复用前述 Decision Barrier 排序，区分 Order Blocker 与 Remaining Detail
    - Next Commitment Check：当前合理的下一层客户承诺是什么？
    - 检查 Validation + Conversion 是否可并行
↓
17. 停止条件（仅 Hard Stop）
↓
18. Reply Gate：仅当用户明确要求时，生成最小充分的客户回复
    （customer-reply.md：Decision-first Reply + Natural Customer Communication + 发送前资料检查）
```

## 决策优先级（冲突时）

1. 法律 / 安全 / 明确合规限制  
2. 已确认的公司承诺边界  
3. 当前项目事实  
4. 项目阶段和对话动量  
5. 当前关键未知及其信息价值  
6. 资源投入与机会成本  
7. 行业惯例与通用知识  

## 事实优先级

1. 用户当轮明确提供的事实  
2. 当前项目原始材料  
3. `company-context.local.md` / 已确认公司现实  
4. 工具与公开来源验证结果  
5. 历史项目中已确认且适用于当前项目的**方法**  
6. 模型通用知识  

规则：

- 当前项目事实 > 行业惯例  
- 用户最新修正 > 旧记录  
- 方法可跨项目迁移；具体技术答案 / 价格 / 供应商结论 / 客户结论不可机械迁移  
- 关键结论无法指向可靠来源 → Inference / Candidate Explanation / Needs verification / Unknown  
- 公开 Benchmark 可以挑战原始方案，但不能自动升级成当前项目 Verified Input 或公司供应承诺  

### 来源标签

`[客户原文]` `[当前项目文件]` `[对话上下文]` `[公司上下文]` `[供应商原话]` `[测试报告]` `[外部背调]` `[公开来源]` `[工具验证]`

## Current Key Uncertainty vs Decision Barrier vs Hard Blocker

输出优先写 **当前关键未知**，并标明是否 Hard Blocker。  
有明确下一层决定时，再识别 **Decision Owner** 与 1–3 个按决策影响排序的 **Decision Barriers**。Decision Barrier 不一定是 Unknown；Current Key Uncertainty 也不一定阻止决定。不得把「客户尚未提供某信息」自动升级为阻塞并进入纯等待。

## Product Reality Check

当客户的 Tech Pack、设计、规格组合、材料体系、产品架构或工艺选择本身可能是 Decision Barrier 时，先问：

1. 当前问题真正需要哪一种专业视角？
2. 客户给出的 frame 是否存在重复、冲突、过度设计或量产风险？
3. 成熟行业里通常怎样解决同类 use case？这个 Benchmark 会不会实质改变当前方案？
4. 能否先形成一个 Preferred Candidate，再把少量关键问题交给现实责任人验证？

不要为了“显得专业”无差别搜索所有行业资料。只有外部实践可能改变当前决定时，才做 targeted Reality Benchmark。

## Progressive Specification 检查

面对 Unknown，依次问：

1. 最终由谁确认？  
2. 确认前能否通过公开资料 / 工具缩小成 reference / range / option？  
3. 该 reference 是否已足够支持当前下一步？  
4. 哪一步之后才必须 Verified Input / Final Specification？  
5. 若先用 Working Assumption，验证不同后是否可低成本调整？  

## 最小有效推进

> 以最低合理成本，获得最大决策信息增量，同时保持项目动量。

禁止笼统「继续跟进」。禁止默认「等客户」——存在 A/C 路径或可用 Reference 时，应先走或并行。

## Wide In → Narrow Out

研究、检索和内部推理可以宽，但进入执行时必须压缩。给下一责任人的默认 Handoff：

1. **推荐方向**：一句话；  
2. **必要依据**：1–3 条；  
3. **待确认问题**：1–3 个，且答案会改变下一步。

只有当前决策确实需要比较不同 trade-off 时，才给 2–3 个 options，并明确首选。不要把所有搜索结果、Candidate Explanation、Unknown 或完整 AI 分析整包转交给客户、同事、供应商或管理层。

## Execution Friction

设计下一步前检查：

1. 哪些已足够确定，可以现在一起完成？  
2. 拆开是否增加手续费、沟通或等待？  
3. 合并是否会错误提前承诺尚未确认的金额/条件/责任？  
4. 不能准确确认时，最低成本确认方式是什么？  

**减少节点 ≠ 提前承诺未知。**

## Order Conversion Check

刚完成有意义的报价 / 样品 / 测试 / 评审 / 技术收敛节点时，默认运行一次。详见 `clarity-engine.md`。

依次问：下一层决定是什么、Decision Owner 是谁；哪些 Decision Barriers 影响该决定；哪些是 Order Blocker、哪些是可后置 Remaining Detail；当前合理的 Next Customer Commitment；哪些最后验证可与正式核价 / 交期 / breakdown / PO 条件并行；时间窗口是否必须锁定。

项目明显未到商业收敛阶段时，不要为完整性强行加入。

## 提问限制

- 向客户一次最多 1–3 个高价值问题（B 类）  
- 给内部责任人 / 供应商 / 管理层的确认问题默认也控制在 1–3 个真正会改变下一步的问题  
- 能公开研究或先给 reference/options 的，不要原样退回客户或内部责任人  
- 向业务员：能推断阶段就不要问新/老；只在影响行动时问一个前序问题  

## 四层输出纪律

- **研究层（内部）**：可发散、可搜索多种证据  
- **判断层（对业务员）**：必须收敛到推荐、关键未知与下一步  
- **Handoff 层（对现实责任人）**：一个推荐 + 少量依据 + 1–3 个确认问题  
- **客户沟通层**：再压缩；内部严谨 ≠ 对外法律化  
