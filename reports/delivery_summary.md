# 2027暑期实习调研交付说明

本次覆盖46家公司入口与岗位检索，收录57条去重的岗位/项目记录。记录总量比70条少13条；其中仅22条明确满足学位范围与2027暑期两个条件，按此口径距70岗仍差48岗。未达到70个符合条件岗位的目标。

| 分类 | 条数 | 含义 |
|---|---|---|
| A | 22 | 官网明确包含2027暑期，学位范围可覆盖MS；仅学位与季节层面匹配 |
| B | 18 | 季节、学位、专业、技能或JD信息仍待确认 |
| C | 8 | 博士/季节/时长不符、非实习形式或已撤下；用于对照，排除在适合数量之外 |
| T | 9 | 人才池、项目匹配池或多团队招聘轨道；另列，不计具体团队岗位 |

A也不表示所有条件已通过：许多岗位未公布最短时长，技能和JD授权条件仍需逐项判断。C类与T类不用于补足合格岗位数量。当前记录明显集中于Waymo和Bedrock；公司检索深度不同，低可访问页面只记录观察结论。本报告不是整个市场无遗漏的清单。

## 建议先看的短名单

Waymo先从Behavior Test、Conflict Behavior和Simulator Realism三条比较，结合希望偏工程、控制还是研究作选择；官网建议每人最多选择3岗。其他方向优先看J&J Systems/Simulation、Corning Advanced Process Controls，以及待确认暑期的Bedrock World Models/SLAM。NVIDIA DevTech Robotics可作为中国方向候选。这里是材料优先级建议，本轮未投递。

| 岗位 | 主要匹配 | 关键限制 |
|---|---|---|
| [Waymo / 5361](https://careers.withwaymo.com/jobs/2027-summer-intern-ms-software-engineering-behavior-test-san-francisco-california-united-states) | 真机评测/测试基础设施，D5 | SQL、故障场景经验要补证据 |
| [Waymo / 5421](https://careers.withwaymo.com/jobs/2027-summer-intern-ms-phd-conflict-behavior-mountain-view-california-united-states) | 控制与安全指标，D2 | 实习时长未公布；CBF为进行中研究 |
| [Waymo / 5432](https://careers.withwaymo.com/jobs/2027-summer-intern-ms-phd-machine-learning-engineer-simulator-realism-evaluation-san-francisco-california-united-states) | ML+仿真评估，D3 | 统计与仿真真实性研究深度 |
| [Johnson & Johnson / R-100027](https://www.careers.jnj.com/es-la/jobs/r-100027/systems-simulation-engineering-intern-robotics-rd/) | 仿真/系统/硬件闭环，D5 | 预计2026-10-17关闭，可延长；固定cohort |
| [Corning / 78170](https://corningjobs.corning.com/job/Painted-Post-Intern,-Advanced-Process-Controls-Summer-2027-NY-14870/1432275700/) | Lie-MPC、优化与系统辨识，D2 | 制造域知识；JD写明不支持移民担保 |
| [Bedrock Robotics / c51d682e-58ee-44de-886f-4cfacb56d2e1](https://jobs.ashbyhq.com/bedrock-robotics/c51d682e-58ee-44de-886f-4cfacb56d2e1) | 世界模型/真机数据，D1 | 仅2027，未写暑期；世界模型课题ongoing |
| [Bedrock Robotics / 8c7bad61-50e3-4702-be36-72e9b72a9760](https://jobs.ashbyhq.com/bedrock-robotics/8c7bad61-50e3-4702-be36-72e9b72a9760) | SLAM+SAM/DINO+传感器，D4 | 未写暑期；学习型建图经验需补 |
| [NVIDIA / JR2024054](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/China-Shanghai/AI-Developer-Technology-Intern--Robotics---2027_JR2024054-1) | VLA与部署研究，D1 | 中国岗位季节/3个月可行性待确认 |

## 本轮改变筛选结论的证据

[Bedrock旧Metric Prototyping链接](https://jobs.ashbyhq.com/bedrock-robotics/07b55743-d5c4-4347-bfac-000821317b13)仍出现在官方搜索索引，但浏览器实时页面已显示Job not found，已标为撤下。[Bedrock安全实习](https://jobs.ashbyhq.com/bedrock-robotics/cb06dc4f-3e78-4546-897d-b39ba12a9178)要求Lean/mathlib；CBF研究相关性不能替代这个技能门槛。

[J&J Controls](https://www.careers.jnj.com/ja-jp/jobs/r-099654/robotics-controls-autonomy-intern-robotics-rd/)的JD明确要求永久美国工作授权且不需要现在或未来担保。仅记录原条件，不推断个人资格。[NVIDIA Robotics Research](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-WA-Seattle/Research-Intern--Robotics---Summer-2027_JR2025647)和TRI Post-Training明确要求PhD，未计入MS匹配数量。NVIDIA的“至少接受至某日”不是明确截止；Google项目预计申请窗口也不是保证开放到该日。

## 简历处理

保存原始LaTeX快照，更新完整总简历，再生成D1-D5五套英文简历。加入Expected 2028、CMU Intelligent Control Lab、Prof. Changliu Liu、Aug.2026-Present与IROS2026 Dexmate贡献。未新增毕业月份、领导头衔、实验数字、正式论文录用或未证明的JD技能。

每套提供LaTeX、干净PDF、相对原版的红线LaTeX/PDF及changes.md。删除为红色删除线，新增为蓝色下划线；移动段落可同时出现删除和新增。红线对比覆盖PDF可提取文字，并验证可精确重构原版与新版词序列；版式差异另在changes.md说明。

## 文件使用

先在XLSX“岗位清单”按筛选结论、国家、方向和优先级过滤。A只表示学位/季节匹配；B/C/T保留不同用途。“公司观察”列出46家检索范围与访问限制，“方向与简历对应”连接到5个版本。岗位截止/窗口日期与核验日期使用Excel日期值，可按时间排序；未公布日期留空并在相邻说明列解释。

所有产物均在当前工作区。未投递、发送消息、上传简历、推送GitHub、安装/运行评估的求职工具或建立持续自动化。
