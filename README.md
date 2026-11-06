# Lab Research Infrastructure

实验室科研协作与 AI 编程的中央规范仓库，先在
`Alex-research-lab-test` 进行公开、无实验数据的验证。

使用 GitHub Issues、PR、Actions 和分支规则组织协作；使用 Codex 原生
`AGENTS.md`、Skills、Subagents 和 GitHub Code Review 辅助研究实现与审核。
当前仓库提供配置和可执行检查；实际远程部署与验收状态以验证记录为准。

## 单独下载或安装 Skill

在终端执行以下命令。第一行列出仓库中匹配的 Skill，第二行仅安装
`research-reproduction` 到 `~/.agents/skills/research-reproduction/`。
安装后新开 Codex 会话，输入 `$research-reproduction` 即可选择它。

```bash
npx skills@1.7.6 add https://github.com/Alex-research-lab-test/lab-research-infrastructure --skill research-reproduction -a codex --list
npx skills@1.7.6 add https://github.com/Alex-research-lab-test/lab-research-infrastructure --skill research-reproduction -g -a codex --copy
```

先检查已有个人 Skill；第三方安装器可能覆盖原文件，不对含个人修改的目录
盲目重复安装。也可用 Codex 自带 `$skill-installer` 指定本仓库的
`.agents/skills/research-reproduction` 路径和固定 commit。

### 只导出 Skill 文件

如果已经有中央仓库的本地副本（包括从 Git bundle 克隆的副本），可以只导出
完整 Skill 目录。进入该仓库根目录，在所需的版本上运行：

```bash
skill_export="$(mktemp -d)"
git archive HEAD:.agents/skills/research-reproduction | tar -x -C "$skill_export"
printf 'Skill 已导出到 %s\n' "$skill_export"
```

导出的目录包含 `SKILL.md` 及该版本随附的资源。可以将整个目录发给其他成员。

上述命令只安装 Skill。需要两个原生 Reviewer 时，按 [Codex 配置说明](docs/codex-setup.md) 接入并验证。

## 从这里开始

1. 阅读 [协作流程](docs/github-collaboration.md) 和 [贡献约定](CONTRIBUTING.md)。
2. 使用 [接入说明](docs/project-adoption.md) 将固定 commit 的模板复制到项目。
3. 按 [Codex 配置](docs/codex-setup.md) 检查 Skill 和 reviewer 的实际发现情况。
4. 按 [验证流程](docs/verification.md) 执行真实 PR 的失败、修复和门禁验证。

## 内容

| 路径 | 用途 |
| --- | --- |
| `AGENTS.md` | 本仓库操作与审核约束 |
| `.agents/skills/research-reproduction/` | 通用科研任务 Skill 的唯一维护源（沿用原名） |
| `.codex/agents/` | Scientific Reviewer 和 Code Reviewer 的唯一维护源 |
| `templates/project/` | 项目级 AGENTS、CI 和检查配置 |
| `templates/user/lab-review.config.toml` | 用户显式启用的只读审核 profile 示例；替换为实际 Git 根目录 |
| `templates/*.md` | 研究任务、论文实现依据、实验记录 |
| `.github/` | 本仓库 CI、Issue 和 PR 模板 |
| `tools/check_codex.py` | 只解析 Codex 元数据的轻量检查 |
| `rulesets/` | 原生合并规则的参数与启用流程 |

中央仓库文件不会自动对其他项目生效。复制时记录来源 commit，后续更新通过
项目 PR 审阅，不在运行时下载可变 `main` 分支的规范或执行脚本。

## 本地验证

Python 3.11+ 和 Node.js 22 用于协作检查，与项目训练环境分离。

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install pre-commit==4.6.1 PyYAML==6.0.3
pre-commit run --all-files --show-diff-on-failure
python -m unittest discover -s tests -v
```

首次运行 pre-commit 会联网安装固定版本的检查工具。
Actionlint 1.7.12 的版本和归档 SHA-256 在工作流中固定。
CI 的预期 job 名为 `lab-ci`，启用合并规则前必须从真实运行确认其名称和来源 App。

角色原生发现还要求客户端信任实际项目 Git 根目录。配置文件存在或静态检查
通过不等于角色已经加载；已验证的 CLI 0.166.0 用法见
[Codex 配置](docs/codex-setup.md) 和 [原生验收记录](docs/native-reviewer-acceptance.md)。

## 公开测试边界

公开仓库只接收经过审阅的通用配置和非敏感文档。不提交数据、checkpoint、
凭据、受限论文全文、实验室内部网络信息或未发表的自定义算法。
现有项目的本地修改、历史和实验数据应保留在原位置。

本阶段不证明论文复现、训练结果或机器人实验成功。
AI review 的存在也不等于 GitHub 必需检查已经生效。
