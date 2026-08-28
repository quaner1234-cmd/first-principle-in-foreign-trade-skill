# Output Contract（输出契约）

Action Mode 必须可扫读。不要求每次机械展示全部标题；按复杂度压缩，但内部逻辑应保持。  
对齐 Project Edition **1.4.5**。

## 模板

```markdown
## 当前判断

一句话：现在应 **探索澄清 / 并行推进 / 短时等待 / 收敛确认 / 内部核实 / 升级 / 降低投入 / 补前序 / 停止（仅 Hard Stop）**
核心理由一句。必要时注明项目阶段。

## 对话 / 项目动量

- 动量：Positive / Weak / Negative（一句证据）
- 策略取向：继续探索 / 可等待但仍可并行 / 降低投入（尚未等于关闭）

## 外部背调事实

（身份证据不足时必出；充分可「沿用」；格式见 auto-due-diligence.md）

## 客户国家 / 地区（New Lead / Qualified Inquiry 必出）

`客户国家 / 地区：X（Fact / Inference / Unknown）`。非 Fact 时简述依据或缺口；与目标销售市场分开。先做低成本公开核实，仍无法确认就写 Unknown。

## 事实 / 推断 / 未知

### 事实
带来源标签。

### 推断
每条有依据；禁止精确成交概率。

### 未知
列出关键未知即可（详细分类见下节）。

## 当前关键未知

对每个关键未知（通常 1–3 个）：

| 未知 | 解决路径 A–D / No Path | 能否先 Reference？ | 当前要 Reference 还是 Verified Input？ | 谁最终确认 | 解决后改变什么 | Blocker 状态 |
|---|---|---|---|---|---|---|
| … | 公开/客户/内部/测试/暂无路径 | 是/否 | Reference / Verified | … | … | 非阻塞/软阻塞/Hard Blocker |

规则：Unknown ≠ Blocker。解决路径与 Blocker 状态必须分开填写。

## Decision Barriers（有明确下一层决定时）

- 下一层决定与 Decision Owner
- 1–3 个按决策影响排序的 Barrier
- 不把所有 Unknown 改写成 Barrier，也不因客户问题顺序决定优先级

## 现在可以主动澄清什么

- Web / 公开资料 / 成熟产品 Reference：…
- 内部 / 供应商 / 版师 / 测试：…
- 不依赖客户回复也能推进：…

（有联网且存在 A 类未知时，分析过程中应先查再写结论。）

## 下一步最小有效推进

最多 3 项。标准：低成本 × 高信息增量 × 保持动量。  
若 Reference 已够支持低风险下一步，优先用 Reference 推进。

## 可直接提供的资料 / 证据

仅列现成、相关、低成本且不扩大承诺边界的资产；没有或不确定时不虚构。邮件回复的完整检查见 `customer-reply.md`。

## 并行推进项

短列表。

## Order Conversion Check

当项目刚完成有意义的样品、测试、报价、评审或技术收敛节点时，必要时补充：

- 下一层决定与 Decision Owner；
- 按决策影响排序的 Decision Barriers；
- 哪些是真正 Order Blockers；
- 哪些可以后置到 PP / production preparation；
- 当前合理的 Next Customer Commitment；
- 哪些最后验证与商业准备可以并行；
- 时间窗口是否已经需要立即锁定。

如果项目明显还没到商业收敛阶段，不要为了完整性强行加入。

## 承诺边界

### 现在可以说
### 暂时不能承诺
（探索中的市场/供应商线索不得写入供应承诺。）

## 责任边界（复杂项目必要时）

**内部写清即可；不要默认整段贴进客户话术。**

- 我方直接执行（Can Do）
- 我方协助 / 协调（Can Assist / Coordinate）
- 外部 / 客户责任主体
- 当前不能承诺（Cannot Commit Yet）

## 投入阶段检查（高额开发/测试/认证时）

- 当前阶段是否已需要这项投入？
- 客户是否提供了匹配的投入证据？
- 是否应先做更低成本的 feasibility / prototype？

## Execution Friction 检查（涉及付款/PI/多节点时）

- 是否有可安全合并的动作？
- 拆开是否增加手续费/等待？
- 合并是否会提前承诺未确认金额/条件？
- 能否先补一个低成本确认再一次完成？

## 停止条件

只有真正存在 Hard Stop 风险时才写。  
不要为了“完整”每次硬加停止条件。
```

## 客户回复（仅用户要求时追加）

见 `references/customer-reply.md`。

摘要：

- Reply Gate：未明确要求则不生成话术  
- Natural Customer Communication：内部严谨，对外自然  
- 用措辞强度表达不确定性（as a reference / please confirm…），不默认免责声明堆叠  
- Boundary by Design：流程与确认节点管理边界  
- 商业条件：内部拆清，对外压缩  
- Reply the Delta：不复述无异议的已知信息；结构服从决策逻辑
- Reply Asset Check：邮件正文后另给业务员发送前资料检查

## 反模式（输出禁止）

- ❌ 把「客户还没给某信息」直接写成最大阻塞并只建议等待  
- ❌ 把承诺边界当成探索边界  
- ❌ Positive Momentum 下主动寻找结案理由  
- ❌ 首轮产品开发询盘直接全面收敛（无 Hard Stop 时）  
- ❌ 对客户倾倒研究报告；跨项目机械复制答案  
- ❌ 把 Reference 写成 Final Specification  
- ❌ 因安全/法律变量而拒绝提供任何前期 Reference  
- ❌ 普通回复堆叠法律式免责声明；把内部责任模型整段外显  
- ❌ 为减节点而虚构费用；或把旧工作假设当成不可推翻  
- ❌ 样品已原则认可，却因可后置细节完全不谈数量 / 交期 / 正式报价  
- ❌ 把 Order Conversion 做成催单（`When will you place the order?`）  
- ❌ 为拿 PO 把安全 / 性能 / 交期 / 量产可行性错误降级  
- ❌ 按客户问题顺序代替 Decision Barrier 排序；把下一件样机械视为 development sample
- ❌ 客户回复逐条复述无异议背景，或虚构已有附件 / 公司资料
