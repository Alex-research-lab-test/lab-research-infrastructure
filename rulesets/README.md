# 分支规则参数

在首个真实 CI 成功并读取 check context/App ID 后，生成仓库专用的原生
规则集 JSON，再展示给用户确认。当前目录不提供可误启用的通用 JSON。

| 参数 | 单成员公开测试建议值 |
| --- | --- |
| 目标 | `main` 分支 |
| enforcement | `active`，仅在确认后启用 |
| bypass actors | 空列表 |
| pull request | 必须 |
| required approvals | 0；双人审核另行配置为 1 |
| required status checks | 真实观察的 `lab-ci` context 和来源 App ID |
| strict required checks | true |
| required review thread resolution | true |
| deletion / non-fast-forward | 禁止 |

不要求通过本地 Skill 或普通 AI 评论提供一个不存在的状态检查。
实际创建后读取规则集确认字段和状态，并在真实失败 PR 验证阻断。

规则集与 GitHub 套餐、仓库可见性和管理员权限有关，见
[GitHub 官方说明](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)。
