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

## 验证实际加载

1. 在新会话的 Skill 列表核实 `research-reproduction` 可见。
2. 明确请求使用 `scientific_reviewer` 和 `code_reviewer`，给出 base/head SHA、
   允许读取的材料、禁止编辑/实验/发布及等待两者返回的要求。
3. 检查客户端实际显示两个角色名称与活动，核对结果中的 reviewed head SHA。
4. 保存实际输出和限制；仅解析 TOML 或手工照读角色指令不能证明原生角色已加载。

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

## 本轮本地测试限制

2026-11-02 在 Codex CLI 0.166.0 的非交互只读会话中，项目 Skill 实际出现在
发现列表；两份 agent 定义存在且通过元数据检查，但会话没有提供自定义角色
选择入口，未实际调用这两个角色。一次临时启用当前 CLI 的新版 multi-agent
功能也未完成自定义角色选择，未持久化任何功能开关。

因此本轮只能记录 Skill 发现成功、Reviewer 配置检查成功，不能记录 Reviewer
原生调用成功。后续需在支持项目自定义角色的交互客户端中按上述步骤验证。
普通独立代码审查已执行，但不能替代这项原生加载验证。

## 官方依据

- [Skills 发现位置](https://learn.chatgpt.com/docs/build-skills)
- [Subagents 文件和权限继承](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [GitHub Code Review 设置与触发](https://learn.chatgpt.com/docs/third-party/github)

配置依据于 2026-11-02 查看；客户端升级后需复查实际支持情况。
