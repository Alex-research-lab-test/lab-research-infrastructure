# Codex 科研工作流

## 项目本地发现

项目 `AGENTS.md` 提供操作规则；`.agents/skills/research-reproduction/SKILL.md`
提供按需科研复现流程；`.codex/agents/*.toml` 定义专业 reviewer。
从项目 Git 根目录启动新的 Codex 会话，并按客户端要求信任该项目。

自定义 agent 使用 `name`、`description` 和 `developer_instructions`。
本模板不固定模型或推理级别，继承父会话设置。
`code_reviewer` 与 `scientific_reviewer` 的只读要求是行为指令；
父会话控制实际沙箱。需要技术层面的只读限制时，在父会话选择只读权限。
自定义文件内的 `sandbox_mode` 不会覆盖父会话设置。

### 实际 Git 根目录的信任

角色定义有效不等于已被客户端加载。CLI 0.166.0 实测会忽略未信任项目中的
角色；需要信任实际 Git 根目录，不能只信任父目录或旧部署目录。
从项目根启动一个新会话，按客户端提示完成信任确认。不要把信任设置放在
项目 `.codex/config.toml` 里让项目自行授信。

如需不覆盖现有用户配置的只读隔离审核，可复制
`templates/user/lab-review.config.toml` 为 `~/.codex/lab-review.config.toml`，
将其中的路径替换为实际项目 Git 根目录，再显式启用：

```bash
codex --profile lab-review --cd /absolute/path/to/project
```

profile 不含模型覆盖，继承用户模型设置；只在选择时生效。不要提交本机路径、
认证材料或用户 profile。仅用 `-c projects.*.trust_level` 的测试没有使项目层
通过信任检查，不能以此声称已经在受信任项目中完成验证。

### 是否需要显式 config_file 注册

本轮单变量对照确认：CLI 0.166.0 在受信任目录能直接发现两个 standalone TOML，
移走显式注册文件后 `agent_type` 和两个角色仍存在。因此本项目不需要为修复
发现问题而强加 `.codex/config.toml`。

官方配置参考仍支持 `[agents.<name>]` 的 `description` / `config_file`。
这是一条可用的显式注册路径，不是本客户端自动发现的必需条件。若使用它，
`config_file` 相对声明配置文件所在目录解析，且不应覆盖已有项目配置。

## 验证实际加载

1. 在新会话的 Skill 列表核实 `research-reproduction` 可见。
2. 核实实际原生工具的 `agent_type` 可选角色列出这两个名字。名字只出现在
   AGENTS 文本里，或给普通 Agent 起同名 task_name，均不算原生发现。
3. 明确请求使用 `scientific_reviewer` 和 `code_reviewer`，给出 base/head SHA、
   允许读取的材料、禁止编辑/实验/发布及等待两者返回的要求。
4. 两次调用均使用 `fork_turns="none"`，先独立调度再等待，不能共享审核结论。
   核对不同线程 ID、各自 native `agent_role`、实际角色指令和 reviewed SHA。
5. 保存两个实际结果和限制；TOML 解析、普通 Agent 或父模型模拟不能替代这些证据。

示例请求：

```text
请使用项目自定义 scientific_reviewer 和 code_reviewer 分别评审当前分支相对
main 的变化。只读，不运行训练或硬件，不发布到 GitHub，等待两者返回。
请各自报告所审阅的 head SHA、可定位的发现和证据缺口。
```

## GitHub Code Review

1. 经授权连接 Codex GitHub App，只开放本次两个测试仓库所需范围。
2. 在 Codex 的仓库设置启用 Code Review；核对账号资格、配额和自动触发条件。
3. 使用已授权的自动触发，或在获准后发布 `@codex review` 评论。
4. 读取实际 bot review/评论并核对当前 head SHA；reaction 只表示开始处理。
5. 修复后确认最新提交已重新审阅，不能复用旧提交上的完成结果。

本地自定义 reviewer 不会自动作为 GitHub bot 运行。Codex 原生 GitHub review
采用其自身流程和仓库 `AGENTS.md`；不能声称它已经执行了两个本地角色。
如果原生集成没有可依赖的状态检查，AI 审核保持额外审核，硬门禁由 CI
与适用的人工批准承担，不伪造 `ai-review: success`。

## 本轮本地测试结果

2026-11-03 在同一 CLI 0.166.0 中，仅纠正实际项目根目录的信任加载即可发现
两个角色。显式注册也是可用方案，但通过单变量对照排除了“缺少显式注册
必然导致失败”的推断。没有升级客户端，也没有修改原角色 TOML。

两个真实原生角色线程已完成独立审核；详细调用证据、审核 SHA 与限制见
[原生验收记录](native-reviewer-acceptance.md)。此前未通过的记录只代表当时
未加载项目层的状态，不能推广为该版本缺少原生角色能力。

## 官方依据

- [Skills 发现位置](https://learn.chatgpt.com/docs/build-skills)
- [Subagents 文件和权限继承](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [GitHub Code Review 设置与触发](https://learn.chatgpt.com/docs/third-party/github)

配置依据于 2026-11-02 查看；客户端升级后需复查实际支持情况。
