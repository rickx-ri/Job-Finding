# 自动求职工具评估

评估日期：2026-09-29。结论：现在不需要新增自动求职工具。现有邮箱、浏览器、官方JD与本地表格已覆盖本轮任务。以后若做持续跟踪，优先考虑JobHuntBot的“只找线索+本地看板”部分；JobSpy和Simplify目录可作为补充发现渠道。当前不建议启用带自动投递、消息或邮箱整理的完整代理工作流。

本轮只读公开仓库元数据、README、关键技能文件和少量代码，没有安装、执行或用这些项目生成岗位清单。作者成功率、运行稳定性、实际费用和访问兼容性均未做运行验证。下述“静态可确认”仅指查到相应代码/规则，不是端到端有效性证明。

| 工具 | 现在结论 | 主要价值 | 核心限制 |
|---|---|---|---|
| 人工核验+本地XLSX | 现在需要 | 官网来源、学历/季节审查、事实可追溯 | 更新需重复核验，不能保证所有动态页面覆盖 |
| JobSpy | 以后可选 | 多招聘网站公开职位聚合 | 无本轮中美/学历/季节专用校验；平台访问限制 |
| JobHuntBot | 以后可选，优先 | 线索/材料/阻塞项与本地看板 | 是代理工作流，不自带新的求职账号权限 |
| SimplifyJobs目录 | 以后可选 | 美国实习入口和更新线索 | 不是代理；高级学位标识不区分硕士与博士硬要求 |
| job-search-skill | 当前不建议 | 浏览器找岗、填表与跟踪 | 技能文件提交规则相互矛盾；许可证未确认 |
| ai-job-agent | 当前不建议整套采用 | ATS填表、求职管理 | 涉及简历、账号、表单及外联等更大范围 |
| job-seeker | 当前不建议整套采用 | LinkedIn+Postgres全流程 | 外部数据库和浏览器状态；自动投递/消息/日常流程范围过大 |

## JobSpy

仓库最后推送 / 许可：2026-02-18 / MIT。最后推送只反映活动，不代表质量。

作者定位是公开招聘信息抓取库。静态读取 jobspy/__init__.py 和 model.py，确认多站点适配、岗位URL/direct URL及描述字段；所查接口没有学历和招聘截止语义解析器。美国覆盖较广；未看到Handshake、BOSS或牛客原生适配。跨板去重和日期有效性仍需岗位ID/官网人工复核。

输入是关键词/地点等查询；请求发往目标招聘网站，可配置代理。库本身不需要把简历交给LLM，也不负责投递。MIT代码使用无单独授权费，代理、模型及维护成本视实际配置；未做费用或成功率测试。未来只在平台允许的范围试用公开搜索；不采用规避封禁的功能。

依据：[JobSpy仓库](https://github.com/speedyapply/JobSpy)；[本次检查的文件](https://github.com/speedyapply/JobSpy/blob/main/jobspy/__init__.py)。

## job-search-skill

仓库最后推送 / 许可：2026-06-24 / 未确认许可证。最后推送只反映活动，不代表质量。

README宣称支持LinkedIn、Indeed、Glassdoor和外部ATS，靠Playwright和代理理解JD；没有可确认的中美学历/2027届专用规则。跟踪Markdown可避免部分重复，但“只看最近一小时”默认规则可能漏掉仍开放的重要岗位。

静态SKILL.md前段要求用户最终提交，后面仍出现auto-submit和Submit步骤，形成直接冲突；不能把“不会自动提交”视为可靠默认。工作流会读取简历并填表/上传，代理模型与网站会接触相应数据。许可证和运行费用未确认，本轮不建议采用。

依据：[job-search-skill仓库](https://github.com/Julien-ser/job-search-skill)；[本次检查的文件](https://github.com/Julien-ser/job-search-skill/blob/master/SKILL.md)。

## ai-job-agent

仓库最后推送 / 许可：2026-04-26 / MIT。最后推送只反映活动，不代表质量。

作者报告跨5个ATS完成大量申请，这属于作者案例，不是本次验证结果。读取skills/job-apply/SKILL.md，看到默认dry-run与--submit开关；技能仍会填入真实表单，URL触发范围较广。学历、季节、去重与来源追溯依赖配置/代理，未见可靠的本轮领域专用评测。

整套项目还包含邮箱、联系招聘者等流程。简历与个人资料可能进入模型、浏览器和ATS；dry-run不保证没有信息传入表单。MIT不等于模型/API免费，实际费用未测试。以后只考虑抽出受限的辅助模块，不以整套默认流程执行本次研究。

依据：[ai-job-agent仓库](https://github.com/AkbarDevop/ai-job-agent)；[本次检查的文件](https://github.com/AkbarDevop/ai-job-agent/blob/main/skills/job-apply/SKILL.md)。

## JobHuntBot

仓库最后推送 / 许可：2026-09-17 / MIT。最后推送只反映活动，不代表质量。

静态SKILL.md明确要求区分届别、年份、当前入口以及旧/模糊线索，并默认首次试验只发现线索；最终提交需明确确认。dashboard/server.js是本地Node服务，监听127.0.0.1，配CSV表。适合复用本轮方向分流和待确认队列。

中美覆盖仍来自外部搜索/浏览器，未实测Handshake或国内ATS。看板可本地运行，但代理读到的简历仍受所用模型的数据流约束，“本地看板”不等于全部数据从不离机。Node服务代码无第三方运行依赖；代理成本和维护时间未量化。推荐以后仅复用lead-finding/dashboard部分。

依据：[JobHuntBot仓库](https://github.com/DanielPan12/JobHuntBot)；[本次检查的文件](https://github.com/DanielPan12/JobHuntBot/blob/main/SKILL.md)。

## job-seeker

仓库最后推送 / 许可：2026-09-10 / MIT。最后推送只反映活动，不代表质量。

静态apply技能包含Easy Apply搜索、--dry-run以及apply_batch_size=0停止自动投递的配置；默认其他流程仍覆盖提交、外联和日常邮箱处理。scripts/db.js确认通过Postgres访问候选人资料，README建议Neon。学历/日期判断仍依赖代理，缺少本轮专项验证。

资料、申请历史与消息可能存到外部Postgres，并被模型/浏览器处理；源码不入Git不等于数据不出本机。需要数据库、浏览器和模型环境，成本未测。README残留模板链接，文档完成度有限。当前范围仅研究，整套系统带来的配置和权限成本没有证实收益。

依据：[job-seeker仓库](https://github.com/galiprandi/job-seeker)；[本次检查的文件](https://github.com/galiprandi/job-seeker/blob/main/.agents/skills/apply/SKILL.md)。

## SimplifyJobs Summer2027目录

仓库最后推送 / 许可：2026-09-29 / API未标明许可证。最后推送只反映活动，不代表质量。

它是社区职位目录和更新程序，不是自动求职代理。读取CONTRIBUTING.md及list_updater/listings.py，确认URL/ID去重、活动状态及高级学位标记流程；高级学位标记合并Master/MBA/PhD，不能自动判定MS是否合格。新近更新不保证每个职位仍开放。

本次README API正文未完整返回；以贡献规则和更新代码限定评估结论。美国技术实习为主要用途，中国机器人岗位覆盖未验证。单纯阅读目录无需上传简历；点击外部申请或使用Simplify产品是另一数据流。以后可作线索源，仍须复核官网；本轮没有用目录给岗位表供数。

依据：[SimplifyJobs Summer2027目录仓库](https://github.com/SimplifyJobs/Summer2027-Internships)；[本次检查的文件](https://github.com/SimplifyJobs/Summer2027-Internships/blob/dev/CONTRIBUTING.md)。

## 能否替代本轮人工核验

没有证据表明这些工具能稳定完成“MSR/2028毕业/约三个月/2027暑期”的全部筛选。重点反例：博士必需与博士优先不同；国内2027届常指毕业年份；“至少接受至某日”不是截止；人才池不是已分配岗位；官方索引可能残留下架职位。工具收集速度不能替代这些判断。

以后如选择试验，建议仅用10条公开JD做只读对照：人工标注学位、季节、时长、活动状态与官方ID；比较遗漏、误纳、字段正确率和人工复核时间。所有硬条件有原文依据，零误标为已投递，且减少净人工时间后再决定是否继续。该试验本次未执行，也未建立任何持续自动化。
