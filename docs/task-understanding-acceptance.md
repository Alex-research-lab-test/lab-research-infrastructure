# 通用科研任务 Skill 实际验收（2026-11-03）

## 基线与改动

中央 main `9aabeb8964b01e87f421ecc89bbe762f0bd28caa` 已包含分级审核。
试点 PR #3、#4 未合并，本次试点基于 PR #4 的
`0972cf9797afc50992b195fbbd4c50ed706cb5ed`，不覆盖 PR #2。

沿用 `research-reproduction` 名称、发现路径、原生角色 TOML 与调度机制。
增加 Task Understanding、必要澄清、中途冲突处理和四条科研路线，更新任务
模板、接入说明及项目指令。失败分析由证据选择路线，不自动重跑官方 Demo。
信息齐全与执行授权分别判断；不开发 Agent 平台。

## 方法与真实结果

CLI 0.166.0 的独立任务会话实际加载 canonical Skill。任务提示不给预期审核
等级或指定 Reviewer；主 Agent 根据目标、完整 diff 和风险决定。所有 fixture
均为合成材料，官方场景只附固定上游 README/任务配置摘录和未访问的论文定位符。
测试仅做只读规划、限定 CPU 验证和真实原生审核，不运行科研训练或硬件。

| 场景 | 实际结果 |
| --- | --- |
| 明确官方 Push-T | READY，直接制定官方复现方案；无多余澄清，未核查指标保留证据缺口 |
| 仅说训练自有数据 | NEEDS_USER_INPUT，3 个关键问题；不默认 Push-T，继续安全核查 |
| 完整数据说明/目标/评价 | READY，读取已有契约直接设计方案；无重复问题 |
| 中途 Action/评价冲突 | NEEDS_USER_INPUT，暂停受影响操作，保留 3 个问题与安全后续 |
| 算法开发 | C 路线，L2 双原生角色完成；限定 CPU 检查通过 |
| 数值分析 | D 路线，L2 双原生角色完成；限定 CPU 与解析验证通过 |
| 纯文档 | L0，零 Reviewer，格式/范围检查完成 |
| 协作配置 | L1，仅原生 code_reviewer 完成 |
| 实验失败分析 | 区分观察与根因假设，不重跑训练；3 个待答问题，L2 双角色报告审核完成 |

后续实验的计划审核与当前已完成审核分别记录；规划场景未冒充科学验收。
数值 fixture 为标量中心化方法，未在 Diffusion Policy 核心算法中改代码。

## 原生调用与实施审核

[详细证据](task-understanding-evidence.json) 保存每个原始任务提示、实际返回、
固定 base/head、fixture 内容哈希及独立角色的真实最终回复。原生调用依据为
实际 `agent_type`、`fork_turns=none`、不同线程 UUID、运行时 agent_role 与加载
的角色 developer_instructions；不是 task_name 或主代理模拟审核。
L2 两次派发在首次收集前完成；没有向对方传递审核结论。

Reviewer 子接口只返回 canonical task ID；宿主另从原生 rollout 补核 UUID
和角色 metadata。加密任务正文未解密或发布，保留选择器/哈希/时序及实际结果，
不把无法读取的密文当作已独立检查过的明文。未公开完整会话上下文或认证材料。

本次 Skill/协作规范变更为 L1。中央实施提交
`1d99e54f26dc02df1ad46540f396bb760f5b09a6` 与试点实施提交
`7764503aa7bd8d750bf19269f6fd848c81b7bc02` 各由独立原生 code_reviewer 完成
静态审核，无可操作发现。审核不冒充独立验证了场景运行。

原有 Automatic review decision / Native dispatch 段落与基线逐字节相同；
角色 TOML、工作流、规则集文件、论文映射及实验模板均未改。
中央 pre-commit、6 项现有 unittest、actionlint 通过；试点治理范围 pre-commit、
metadata、actionlint 通过。没有执行旧项目 tests 全目录。

最终证据附录仅增加本页和 JSON，不在上述实施审核 tip 内；通过差异确认
Skill、配置和其他实施内容与审核 SHA 完全一致，不将旧审核移称新 tip 审核。

## 对照、纠正与边界

旧 Skill 已能识别冲突并暂停依赖操作；有效对照中缺少要求的显式
NEEDS_USER_INPUT 状态，不能声称旧版本总会使用错误数据。首个 sparse 夹具
误含删除历史，完整数据夹具误带另一场景的冲突材料，另有提示 SHA 构造错误；
这些尝试不计相应验收，原始记录保留，修正夹具后按同一 Skill 重新运行通过。

本记录证明所观察场景的工作流行为，不保证所有未来模型运行。无人值守测试
实际返回并保留问题，未测试交互界面的提问提交。没有训练、真实性能、论文
复现或真实数据/硬件结果。CI 与 AI 是辅助证据，保留已有 GitHub 门禁。

用户已明确要求本次独立分支与 PR；远程 CI、PR 地址和未合并状态由发布后的
真实记录补充，本页不预先宣称远程通过。
