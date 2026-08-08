# Project Stage（项目阶段识别）

> 真正影响下一步的，是客户已经走到哪一步——不是「新询盘 / 老询盘」二元标签。
>
> **Never ask the user to label the inquiry stage if the stage can be inferred from the supplied evidence.**
>
> **If the stage is unclear, ask only when that uncertainty would materially change the next action.**
>
> 中文：**能从材料里判断，就不要问用户「这是新询盘还是老询盘」。只有阶段不清会改变下一步时，才问一个问题。**

本文件是决策引擎**前置层**：先识别客户/项目与阶段，再决定 Mode、背调策略与提问。用户无需先选手动模式。

## 四档阶段（主路由）

| 阶段 | 典型状态 | 背调侧重 |
|---|---|---|
| **New Lead** | 第一次接触，需求尚粗 | 默认 Quick Check（几乎不了解对方） |
| **Qualified Inquiry** | 已有较明确产品、数量、规格，开始澄清/报价 | 若身份事实不足则补背调；重点转向项目真实性、需求匹配、投入程度 |
| **Active Project** | 报价、打样、修改、付款、生产等已发生 | 通常不重复全量背调；检查**新的未知**（账期、换抬头、换收货主体、高额投入等） |
| **Re-engagement** | 以前沟通过，中断一段时间后重新出现 | 确认公司是否仍活跃、联系人是否仍在、项目背景有无变化 |

可与更细的产品推进粒度并用（概念探索 / 供应商初筛 / 产品定义 / 样品 / 大货），但**对外输出与路由以四档为主**。

## 识别顺序（自动，不问用户）

```
输入材料
↓
1. 识别客户 / 项目（同一对话上下文、公司名、买家昵称、邮件线程）
↓
2. 读取已有上下文（本轮对话已有分析、邮件、报价、样品记录 → 持续项目，沿用已有事实，不重跑「全新 New Lead 流程」）
↓
3. 判断项目阶段（四档）
↓
4. 检查 Buyer Identity Evidence 是否充分（与「是不是新询盘」解耦）
↓
5. 不足 → 背调；充分 → 不重复背调
↓
6. 继续事实 / 推断 / 未知…
```

### 第一层：对话上下文

同一客户/项目已在本次对话出现过，且已有分析、邮件、报价、样品记录 → 判定为**持续项目**（多为 Active Project 或 Qualified Inquiry），**沿用已有事实**，禁止当成全新 New Lead 重跑全套。

### 第二层：材料形态信号（非新询盘强信号）

出现下列信号，基本可确认不是 New Lead：

- `Re:`、`Fwd:`、引用邮件链、多个时间戳
- `As discussed` / `As mentioned` / `Following up`
- `Thanks for your quotation`
- `We received the sample`
- `Let me check`（出现在已有往返对话中）
- `Please revise the price`
- `We have paid`
- 已有 sample / quotation / PI / tech pack revision / PO / tracking / feedback 等

### 第三层：商业动作成熟度（不是措辞）

例：客户**第一次**发给你的只有一句  
`Please see attached tech pack and quote 500 pcs.`  
→ 对你是首次联系，但项目成熟度不是最早期。  
应识别为：**新客户 + Qualified Inquiry（已有明确项目）**，不是「普通 New Lead」。

### 第四层：不确定时不要猜

例：用户只贴 `Hi Alex, yes, please make two samples.`  
Skill 知道这不是第一封，但不知道前序做到哪一步。

输出：

> **当前判断：这是持续沟通，但前序信息缺失。**

然后**只问一个问题**：

> **把前面的聊天/邮件一起发我，或者简单告诉我此前已经做到哪一步。**

禁止连环问：哪个公司？多少数量？报过价吗？做过样吗？……

仅当阶段不清**会实质改变下一步**时才问；能从材料推断则不问用户贴标签。

## 阶段 → Mode 提示（仍自动选主 Mode）

| 阶段 | 常见主 Mode |
|---|---|
| New Lead | Mode 1（询盘分析）+ 默认背调 |
| Qualified Inquiry | Mode 1 或 Mode 4/5（视材料：报价/技术包） |
| Active Project | 按最新材料选 Mode 4/5/6/8…；不重开 New Lead 全流程 |
| Re-engagement | Mode 1/2 成分 + Recency 向背调；先确认是否仍同一项目 |

复合输入仍：选一个主 Mode，其余作次要引用。

## 输出要求

在 `## 当前判断` 中或紧接其后标明：

```markdown
**项目阶段**：New Lead / Qualified Inquiry / Active Project / Re-engagement
（一句依据；若前序缺失写「持续沟通，前序信息缺失」）
```

不要让用户在输入时选择阶段。
