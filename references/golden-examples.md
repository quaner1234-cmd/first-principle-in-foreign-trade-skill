# Golden Examples（完整输出样例）

> 用途：给 Skill 看的"填好的输出长什么样"。比十条规则更能稳定输出质量。
> 所有示例为**脱敏构造数据**（非真实项目），用于演示格式与粒度。
> 示例假设用户已填写虚构的 `company-context.local.md`（功能服装工厂 OEM；常规 MOQ 300；样品约 25 天；持有 GRS 范围证书——均为演示用假设，非任何真实公司资料）。

---

## Example 1 — 询盘分析（含阶段识别 + 自动背调）

### 输入（客户原文）

> Hi team, this is Maya from NordCommute (nordcommute.example). We are a small outdoor brand in Northern Europe. We want to launch a line of insulated winter jackets for urban commuting — recycled polyester shell, puffer style. We are looking for a factory that can handle development and production. MOQ would be around 200-300 pcs per color, 2 colors. Could you share your price for FOB? We need samples within 6 weeks to hit our launch.

### 输出（Action Mode 主输出）

## 当前判断

**先澄清，不报价。** 外部痕迹支持「小型户外品牌」叙述，需求也具体（品类+数量级+时间），但面料规格/是否要 GRS 未定——现在报价不可信。

**项目阶段**：Qualified Inquiry（首次联系，但已有品类方向 + 数量级 + 上市时间；不是需求尚粗的 New Lead）

## 外部背调事实

**档位**：Quick Check（身份证据不足，首次补齐）
**Buyer Identity Evidence**：补查后趋于充分（仍缺注册号等，不影响当前推进）

### 身份
- Company: NordCommute（公开页面使用该品牌名）
- Country: 北欧（官网 About 写 Sweden；未单独核验注册实体）
- Website: nordcommute.example（可访问）
- Buyer: Maya（官网 Team 页有同名联系人）
- Email domain: （本例邮件未给出；若后续有 @nordcommute.example 再核域名一致性）

### 业务
- 主营：urban outdoor / commuting 外套与配件
- 商业角色：品牌方（DTC 官网 + 少量零售合作表述）
- 目标市场：北欧
- 与本次询盘的关联：官网已有 autumn/winter jacket 类目；询盘为加厚 puffer + recycled shell，与现有方向相关

### 公开经营痕迹
- 官网可访问，有产品页与购买路径
- LinkedIn company page 存在（约 10–50 人表述）
- 未发现与询盘明显冲突的第二身份

### 最近活动
- 官网 Journal 最近一篇标注为近 3 个月内
- Instagram 近 60 天内有发帖（公开时间戳）

### 发现的矛盾 / Risk Facts
- 无显著矛盾（当前 Quick Check 范围）

### 未找到
- 未发现公开证据：完整公司注册号、财务报表、大货采购记录

### 来源
- Source 1: nordcommute.example（About / Products / Team）
- Source 2: LinkedIn company page 摘要
- Source 3: Instagram 公开时间戳

## 事实 / 推断 / 未知

**事实**
- 客户要 puffer 冬季夹克、再生涤纶面料、开发+生产一体 [客户原文]
- 数量级 200-300 件/色 × 2 色 [客户原文]
- 需要 6 周内出样品 [客户原文]
- 公开品牌痕迹与「小型北欧 outdoor brand」叙述基本吻合；官网已有冬季外套方向 [外部背调]
- 我司工厂有 GRS 范围证书，可覆盖再生涤纶产品 [公司上下文]

**推断**
- 主体与项目方向匹配度尚可，值得标准开发沟通；但 200–300 件级仍应按小单控制投入深度 [依据：背调痕迹 + MOQ 原文]
- 客户有具体上市时间计划（"to hit our launch"），时间窗口表述真实 [依据：原文]——但 6 周样品 vs 我司常规约 25 天（收样品费后），能否对齐取决于面料复杂度，属推断

**未知**
- 面料规格（克重、成分比例、是否必须 GRS 认证纱线）→ 决定单耗与价格
- 开发费用、样品费是否接受 → 决定投入节奏
- 是否已有 tech pack / OEM vs ODM

## 当前最大阻塞

1. **面料方向未定**（含是否要 GRS）——不确认无法核价、无法承诺 6 周
2. 样品费与样品周期的确认——承诺 6 周的前提

## 下一步最小有效动作

1. 回复：确认能做，报常规流程（样品费政策、周期约 25 天收到样品费后）；问 3 个问题：①面料规格或方向 ②是否需要 GRS 认证再生涤纶 ③有无 tech pack
2. 不问价格、不核价——数量级已知但面料未定
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

## Example 1b — 持续对话链（非全新询盘）+ 身份不足

### 输入要点

用户贴上整段平台聊天：已确认防护等级与夹克样品方向；我方已说明不做某类配件；客户追问配件供应商或尺寸，并说 `Let me check.` 买家仅为平台昵称 `ukbuyer_sc`，无公司名/网站/企业邮箱。

### 应如何判

**项目阶段**：Active Project 或 Qualified Inquiry（已有多轮澄清与能力边界说明；**不要**当成 New Lead 重开）

**背调**：Buyer Identity Evidence 不足 → 仍尝试检索昵称/可得线索；通常输出：

**当前无法完成有效主体背调：现有信息只能确认客户的需求内容，不能确认其商业主体。** 已有线索：平台昵称 ukbuyer_sc；寄样目的地 UK。

然后沿用对话事实，聚焦当前阻塞——**不因「不是新询盘」跳过身份检查，也不把整单重写成首封询盘分析。**

---

## Example 1c — 前序信息缺失（只贴一句）

### 输入

> Hi, yes, please make two samples.

### 输出要点

## 当前判断

**补前序上下文。** 这是持续沟通，但前序信息缺失——不知道此前规格、报价、样品费是否已定，无法负责任地推进打样承诺。

**项目阶段**：持续沟通，前序信息缺失（材料形态已排除 New Lead，但不足以在 Active / Qualified 间定下一步）

## 下一步最小有效动作

1. 请把前面的聊天/邮件一起发我，或简单告诉我此前已经做到哪一步。

（不要问：哪个公司？多少数量？报过价吗？做过样吗？——一次只补前序。）

---

## Example 2 — 报价（Mode 4）

### 输入（客户邮件原文）

> We confirm the quantity: 800 pcs, one style, two colors. Attached is the tech pack. The shell fabric we want is 20D nylon ripstop with C0 DWR, and for the insulation we are open to your suggestion. Please send us your best FOB price and production lead time.

### 输出（Action Mode 主输出）

## 当前判断

**进入核价，但报价前先闭环三个内部变量。** 数量、款式、面料方向已明确，可以投入核价；但单耗（幅宽未在 tech pack 确认）、填充方案、合规要求仍会改变价格——先内部核价，拿到结果后给"结构报价"，不在核价前口头报估算。

**项目阶段**：Active Project（已有 tech pack + 确认数量，进入报价执行）

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
2. 价格预期管理：告知客户"已在核价，预计 X 天内给结构报价"，不让客户等无音讯
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

## 示例共同遵守的纪律

1. 先标 **项目阶段**（四档或「前序缺失」）；能推断就不要问用户「新/老询盘」。
2. 背调看 **Buyer Identity Evidence**，不与「是否新询盘」绑死；不足必查或标明无法背调；充分可沿用。
3. 背调只记事实/Risk Facts/未发现证据，不在搜索块里给客户打分。
4. 事实必须带来源标签；推断必须写明依据且能指向事实；未知只列会改变决策的。
5. 不给精确成交概率、不给"诚意 70%"类评分。
6. 动作具体；前序缺失时只问业务员一个补上下文问题。
7. 承诺边界分两栏；客户回复不把内部背调结论写进邮件。
8. 「未找到」只写「未发现公开证据」，不写「不存在」。
