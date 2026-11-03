# 项目接入

## 复制边界

先检查项目现有 AGENTS、CI、Git 状态及数据边界。已有同名文件时人工合并，
禁止用整个模板目录覆盖项目。原工作目录有未提交代码时，优先在独立 clone
准备基础设施变更，保持原 Git 元数据和数据位置不变。

从中央仓库的一个已审阅 commit 取出以下内容：

| 中央来源 | 项目目标 |
| --- | --- |
| `templates/project/AGENTS.md` | `AGENTS.md`，按项目适配 |
| `.agents/skills/research-reproduction/` | 同路径 |
| `.codex/agents/` | 同路径 |
| `templates/project/.github/workflows/lab-ci.yml` | `.github/workflows/lab-ci.yml` |
| `templates/project/.pre-commit-config.yaml` | `.pre-commit-config.yaml` |
| `.markdownlint-cli2.jsonc` | 同路径 |
| `.github/ISSUE_TEMPLATE/research-task.yml` | 同路径 |
| `.github/pull_request_template.md` | 同路径 |
| `tools/check_codex.py` | `tools/lab/check_codex.py` |
| `templates/*.md` | `docs/lab/templates/` |

在项目根目录建立 `lab-infrastructure-version.json`，包含 `schema_version: 1`、
`template_version: "0.1.0"`、`source_repository`、实际 40 位 `source_commit`、
`adopted_on` 和 `local_adaptations` 列表。不得把未核实字符串写成已采用版本。

不生成自动覆盖脚本，不安装全局配置，不增加平台服务。
中央原生 Skill 和 agent 文件是维护源；项目副本通过 PR 更新。

客户端必须信任实际 Git 根目录，才能原生发现项目角色。父目录或旧部署目录
的信任记录不能代替新仓库根目录。首次从项目根启动客户端时完成信任确认；
隔离审核也可由用户选择 `templates/user/lab-review.config.toml` 的 opt-in profile。
它需要复制到用户配置目录并替换路径，不自动安装，也不把本机信任写进项目。

CLI 0.166.0 实测受信任项目可直接发现 standalone TOML，不必为此强加项目
`.codex/config.toml`。显式 `[agents.<name>].config_file` 是另一条可用注册路径，
若采用则合并已有配置，不覆盖用户或项目原配置。详见 [原生加载说明](codex-setup.md)。

## Diffusion Policy 测试接入

官方来源为 [real-stanford/diffusion_policy](https://github.com/real-stanford/diffusion_policy)。
旧本地 HEAD 与本次核实的官方 main 均为
`5ba07ac6661db573af695b419a7947ecb704690f`。实际 Fork 前再次读取远程，
如果上游变化，基于 Fork 当前分支接入，不用强推覆盖它。

独立 clone 只接收已提交历史；现有 Franka 自定义数据集、任务配置、包初始化
文件和 runner 的未提交修改留在原工作目录。本次不搬迁数据、不运行实验，
不在公开仓库记录原部署绝对路径或设备信息。

新 clone 的 `origin` 最终关联组织 Fork；`upstream` 关联官方仓库，设置
不可推送的 push URL；不要改旧工作目录的 remote。推送明确指定组织 remote、
分支和 ref，禁止 `--mirror` 或 `--force`。

## 协作检查的范围

项目 pre-commit 只对协作配置、`docs/lab` 和 `tools/lab` 做检查。
默认不批量格式化历史 Python，不调用整个 `tests/`，不安装训练依赖。
本次没有改算法，所以只验证接入配置与检查工具；以后修改算法时必须另外
为受影响模块增加明确的 CPU/数据/GPU 验证，不能把基础 CI 当作算法测试。

先运行本地检查和 actionlint，再核对暂存清单、来源 commit 和旧仓库基线。
远程创建 Fork、推送和 PR 均遵守用户确认边界。
