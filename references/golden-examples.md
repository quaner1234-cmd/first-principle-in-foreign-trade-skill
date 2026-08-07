# Golden Examples（完整输出样例）

> 用途：给 Skill 看的"填好的输出长什么样"。比十条规则更能稳定输出质量。
> 所有示例为**脱敏构造数据**（非真实项目），用于演示格式与粒度。
> 示例假设用户已填写虚构的 `company-context.local.md`（功能服装工厂 OEM；常规 MOQ 300；样品约 25 天；持有 GRS 范围证书——均为演示用假设，非任何真实公司资料）。

---

## Example 1 — 新询盘（Mode 1）

### 输入（客户原文）

> Hi team, we are a small outdoor brand in Northern Europe. We want to launch a line of insulated winter jackets for urban commuting — recycled polyester shell, puffer style. We are looking for a factory that can handle development and production. MOQ would be around 200-300 pcs per color, 2 colors. Could you share your price for FOB? We need samples within 6 weeks to hit our launch.

### 输出（Action Mode 主输出）

## 当前判断

**先澄清，不报价。** 客户是真实开发意图（具体品类+数量级+时间计划），但关键变量未齐：面料规格、单耗、是否要求 GRS 再生涤纶认证——这些直接决定价格结构，现在报的价不可信。

## 事实 / 推断 / 未知

**事实**
- 客户要 puffer 冬季夹克、再生涤纶面料、开发+生产一体 [客户原文]
- 数量级 200-300 件/色 × 2 色 [客户原文]
- 需要 6 周内出样品 [客户原文]
- 我司工厂有 GRS 范围证书，可覆盖再生涤纶产品 [公司上下文]

**推断**
- 客户有具体上市时间计划（"to hit our launch"），时间窗口真实 [依据：原文表述]——但 6 周样品 vs 我司常规样品周期约 25 天（收到样品费后），紧张但理论上可谈，属推断，需确认面料与工艺复杂度
- 客户是小品牌，300 件级 MOQ 说明是初创/小众定位 [依据：MOQ 表述 + 自述 small brand]——不判定"没实力"，数量级只是事实

**未知**
- 面料规格（克重、成分比例、是否必须 GRS 认证纱线）→ 决定单耗与价格
- 开发费用、样品费是否接受 → 决定投入节奏
- 品牌方是否已有 tech pack / 是否要我司参与设计开发（OEM vs ODM）

## 当前最大阻塞

1. **面料方向未定**（含是否要 GRS）——不确认无法核价、无法承诺 6 周
2. 样品费与样品周期的确认——承诺 6 周的前提

## 下一步最小有效动作

1. 回复：确认能做，报常规流程（开发流程、样品费政策、周期约 25 天收到样品费后）；同时问 3 个问题：①面料规格或方向 ②是否需要 GRS 认证再生涤纶 ③有无 tech pack
2. 不问价格、不核价——数量级已知道，但面料未定，核价是浪费
3. 内部确认：当前产能下 6 周样品是否可承诺（找生产计划）

## 现实验证

| 未知 | 谁验证 |
|---|---|
| 面料规格/是否 GRS | Customer（回复时问） |
| 6 周样品是否可承诺 | Internal（生产计划） |
| 再生涤纶面料 MOQ 与价格 | Supplier |

## 承诺边界

**现在可以说**：工厂有 GRS 范围证书，再生涤纶产品可做；常规样品周期约 25 天（收到样品费后）；OEM/ODM 均可；正常 MOQ 300 件，客户 200-300 件量级接近可谈。

**暂时不能承诺**：FOB 单价（面料未定）；6 周样品交期（需内部确认产能）；GRS 产品认证（需确认纱线来源与 TC 流程）；样品费金额（需按开发复杂度核定）。

### 客户回复（用户要求时才追加，直接可发）

> Thanks for your message — this is right in our wheelhouse. We make functional apparel for outdoor and winter categories, and our factory holds a GRS scope certificate, so recycled polyester shells are fully possible.
>
> To give you a reliable price and timeline, could you confirm three things:
> 1. Do you have a tech pack, or should we work from reference samples/sketches?
> 2. Fabric direction — do you have a specific shell fabric in mind (weight, composition), and do you need GRS-certified recycled yarn specifically?
> 3. Sample fee and development cost: we usually charge a sample fee (deductible from bulk), and samples take about 25 days after we receive it. Would that work with your 6-week target?
>
> Once we know the fabric direction, we can get you a proper FOB quote quickly.

---

## Example 2 — 报价（Mode 4）

### 输入（客户邮件原文）

> We confirm the quantity: 800 pcs, one style, two colors. Attached is the tech pack. The shell fabric we want is 20D nylon ripstop with C0 DWR, and for the insulation we are open to your suggestion. Please send us your best FOB price and production lead time.

### 输出（Action Mode 主输出）

## 当前判断

**进入核价，但报价前先闭环三个内部变量。** 数量、款式、面料方向已明确，可以投入核价；但单耗（幅宽未在 tech pack 确认）、填充方案、合规要求仍会改变价格——先内部核价，拿到结果后给"结构报价"，不在核价前口头报估算。

## 事实 / 推断 / 未知

**事实**
- 800 件、1 款 2 色 [客户原文]
- 面料方向：20D 尼龙防撕裂 + C0 DWR [客户原文]
- 填充方案让我方建议 [客户原文]
- tech pack 已提供 [客户原文]（幅宽字段待核，属未知）

**推断**
- 客户进入比价/决策阶段（数量+tech pack+明确面料 = 供应商初筛后期或产品定义期）[依据：行为证据完整度]
- C0 DWR 说明客户重视环保合规（无氟）[依据：选型本身]——但客户目标市场环保法规（如 EU）是否硬性要求，未确认，属推断

**未知**
- 面料幅宽与单耗（tech pack 是否含幅宽，需核）
- 填充方案与克重（我方建议方向：需内部确认哪种填充在 800 件量级最划算）
- 客户是否要求测试/合规报告（如 GRS 纱线、RSL）及其费用归属

## 当前最大阻塞

1. **单耗未知**（缺幅宽）——直接决定面料用量与单价
2. 填充方案未定——占成本比例大

## 下一步最小有效动作

1. 内部核价三步：①版师/工艺确认单耗（或向客户要幅宽）②向面料供应商询 20D 尼龙防撕裂 C0 DWR 价格与 MOQ（800 件用量可能低于面料 MOQ，提前确认）③确认填充方案
2. 价格预期管理：告知客户"已在核价，预计 X 天内给结构报价"，不让客户等空音讯
3. 报价时标注假设：面料价格按当前询价、填充按建议方案、不含测试费——每一行都能回答"为什么"

## 现实验证

| 未知 | 谁验证 |
|---|---|
| 面料幅宽/单耗 | Technical Staff（版师）或 Customer（tech pack 补充） |
| 面料单价/MOQ | Supplier |
| 填充方案成本 | Internal（采购） |
| 测试与合规要求 | Customer（问清是否要报告、费用归属） |

## 承诺边界

**现在可以说**：正在核价；正常大货周期约 90-120 天（收到预付款、样品确认后）；MOQ 300 件，800 件无压力；工厂有 GRS 范围证书（如客户要再生纱线）。

**暂时不能承诺**：FOB 单价（核价中）；填充成本（方案未定）；大货交期具体日期（需样品确认后倒排）；测试费用归属（未与客户确认）。

---

## 两个示例共同遵守的纪律

1. 事实必须带来源标签；推断必须写明依据；未知只列会改变决策的。
2. 不给精确成交概率、不给"诚意 70%"类评分。
3. 动作具体到"问谁、核什么、多久"。
4. 承诺边界永远分两栏：现在可以说 / 暂时不能承诺。
5. 客户回复不重复客户已说的内容，问题不超过 3 个，语言跟随客户。
