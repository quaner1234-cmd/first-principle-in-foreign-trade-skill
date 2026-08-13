# Decision Engine（统一判断内核）

所有场景都必须先运行同一个判断内核。对齐 Project Edition **1.4**。

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
   - Tool-before-Question：先查公开工具 / 成熟产品 / 标准 / 供应商公开资料
↓
8. Current Key Uncertainty
   - 类型、能否形成 Reference、谁最终确认、是否 Hard Blocker
↓
9. Progressive Specification
   - 若 Reference 足以支持当前推进 → Public Reference / Candidate Range / Working Assumption
   - 再判断何时必须获得 Verified Input / Final Specification
↓
10. 对仍需客户决策的 B 类未知：只问 1–3 个高信息价值问题
↓
11. Smallest Effective Advance + 并行推进项
↓
12. 承诺边界
    + Responsibility Boundary（内部：Can Do / Assist / Coordinate / Cannot Commit Yet）
    + Staged Commitment（投入是否与阶段和客户投入证据匹配）
    + Execution Friction / Transaction Node Check
↓
13. Order Conversion Check（刚完成有意义的报价 / 样品 / 测试 / 评审 / 技术收敛节点时）
    - 区分 Order Blocker 与 Remaining Detail
    - Next Commitment Check：当前合理的下一层客户承诺是什么？
    - 检查 Validation + Conversion 是否可并行
↓
14. 停止条件（仅 Hard Stop）
↓
15. Reply Gate：仅当用户明确要求时，生成压缩后的客户回复
    （customer-reply.md：Natural Customer Communication）
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

### 来源标签

`[客户原文]` `[当前项目文件]` `[对话上下文]` `[公司上下文]` `[供应商原话]` `[测试报告]` `[外部背调]` `[公开来源]` `[工具验证]`

## 关键未知 vs Hard Blocker

输出优先写 **当前关键未知**，并标明是否 Hard Blocker。  
不得把「客户尚未提供某信息」自动升级为阻塞并进入纯等待。

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

## Execution Friction

设计下一步前检查：

1. 哪些已足够确定，可以现在一起完成？  
2. 拆开是否增加手续费、沟通或等待？  
3. 合并是否会错误提前承诺尚未确认的金额/条件/责任？  
4. 不能准确确认时，最低成本确认方式是什么？  

**减少节点 ≠ 提前承诺未知。**

## Order Conversion Check

刚完成有意义的报价 / 样品 / 测试 / 评审 / 技术收敛节点时，默认运行一次。详见 `clarity-engine.md`。

依次问：距离 Bulk Order 还差什么；哪些是 Order Blocker；哪些是可后置 Remaining Detail；当前合理的 Next Customer Commitment；哪些最后验证可与正式核价 / 交期 / breakdown / PO 条件并行；时间窗口是否必须锁定。

项目明显未到商业收敛阶段时，不要为完整性强行加入。

## 提问限制

- 向客户一次最多 1–3 个高价值问题（B 类）  
- 能公开研究或先给 reference/options 的，不要原样退回客户  
- 向业务员：能推断阶段就不要问新/老；只在影响行动时问一个前序问题  

## 三层输出纪律

- **研究层（内部）**：可发散  
- **判断层（对业务员）**：必须收敛  
- **沟通层（对客户）**：再压缩；内部严谨 ≠ 对外法律化  
