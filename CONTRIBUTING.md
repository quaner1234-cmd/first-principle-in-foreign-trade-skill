# Contributing

感谢你愿意改进这个 Skill。

目标很简单：让外贸业务员在真实项目里更快做出可靠判断，而不是生成更长的分析报告。

## 欢迎提交

- Bug：输出结构坏了、模式路由错了、承诺边界失效
- Hallucination cases：虚构能力、法规、价格、客户背景等
- Real cases（必须脱敏）：新场景输入→期望判断
- Feature：新 Mode、更清晰的规则、跨行业适配
- Documentation：README、示例、术语表

建议 Issue 标签：

```text
bug
hallucination
case
feature
documentation
cross-industry
```

## 提交前请脱敏

**不要**在 Issue / PR 里贴：

- 真实客户姓名、邮箱、电话、WhatsApp、地址
- 真实公司名、品牌名、未公开价格、成本
- 私有供应商信息、内部政策、NDA 内容
- API key / token / 任何密钥

可以用虚构名称，例如 `Customer A`、`Brand X`、`Supplier Y`。

## PR 建议

1. 先开 Issue 说明问题或场景
2. 改动尽量小、可验证
3. 若改输出格式，同步更新 `references/output-contract.md` 或 `references/golden-examples.md`
4. 不要把 `company-context.local.md` 或任何私有资料带进来

## 设计原则（请保持）

- Action Mode 默认；Learning Mode 仅在用户追问时展开
- 事实 / 推断 / 未知必须分开
- 给判断建议，但不替用户承担最终判断
- Unknown 优于编造
- 不要求 API key
