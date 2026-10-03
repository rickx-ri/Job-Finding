import json,re,html
from pathlib import Path
from collections import Counter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'sources/research_data.json').read_text());jobs=data['jobs'];byid={x['id']:x for x in jobs}
R=ROOT/'reports';R.mkdir(exist_ok=True)
pdfout=ROOT/'output/pdf';pdfout.mkdir(parents=True,exist_ok=True)
counts=Counter(j['category'][0] for j in jobs)
def jd(k,label=None):
 j=byid[k];return f'[{label or (j["company"]+" / "+j["req_id"])}]({j["source"]})'

access='''# 渠道访问清单

核验日：2026-09-29。权限来自用户本次授权与已登录会话，仅用于查找和本地材料准备。公开网页可读不代表有账号权限；会话状态也不等于长期授权已配置。

| 渠道 | 账号/会话 | 实测能力 | 当前限制 |
|---|---|---|---|
| CMU Gmail | rickx@andrew.cmu.edu | Gmail连接器与浏览器；搜索及完整招聘正文可读 | 连接器绑定CMU账号；未发送、归档或改标签 |
| UMich Gmail | ziyuxu@umich.edu | 浏览器搜索与邮件正文可读；已看到Midea Summer 2027 Co-op线索 | 当前未获得独立UM邮箱连接器；附件未全面检查 |
| CMU Handshake | 早前CMU登录；当前独立会话未登录 | 曾进入CMU学校首页；本次独立浏览器重新检查 | 独立会话停在CMU Sign In；需恢复登录；不能认定可持续读取CMU职位 |
| UMich Handshake | 当前Chrome共享会话为UMich | 登录首页和职位列表可读 | CMU和UM域名共享会话会切换学校；UM单岗详情读取未单独覆盖 |
| LinkedIn | Ziyu (Rick) Xu；主邮箱ziyuxu@umich.edu | 登录身份、职位搜索与JD读取已验证 | 语义搜索有误匹配；不等同官网正在招；无投递/外联授权 |
| Indeed | 公开页面 | 搜索和NVIDIA机器人实习JD可读 | 不主张已登录；博士门槛用官网再核验 |
| 牛客 | 公开实习栏目 | 实习目录页面可读 | 未验证登录与所有岗位详情；非最终岗位状态依据 |
| BOSS直聘 | 公开首页 | 首页可读 | 未核验登录账号与完整JD权限 |
| 公司招聘官网/ATS | 公开页面 | 搜索索引、直接正文及部分浏览器实时入口 | 动态网页、403/202、下架旧索引分别标记；HTTP 200不单独证明在招 |
| GitHub私人简历仓库 | 用户已登录Chrome | 读取CMU_Ziyu.tex与仓库约束 | 未推送；浏览器页面读取快照保存在本地 |

## 发现渠道与最终核验

CMU Handshake邮件提供J&J Controls和Bedrock V&V线索；UM邮件提供Midea线索；Indeed发现NVIDIA研究实习。最终岗位清单以公司官网/ATS正文为依据，跨渠道同一岗位编号合并。Midea尚未定位到同一官方JD，因此只进入公司观察。

CMU独立会话实际地址：[CMU Handshake登录页](https://cmu.joinhandshake.com/login)。UM当前入口：[UMich Handshake](https://umich.joinhandshake.com/home)。后续恢复CMU会话需用户登录，本次不继续提问。

LinkedIn限制自动抓取/自动化访问；本轮没有安装或运行任何发现的求职工具。参见[LinkedIn官方说明](https://www.linkedin.com/help/linkedin/answer/a1341387)。本地报告不包含会话Cookie、口令或访问令牌。
'''

tool_intro='''# 自动求职工具评估

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
'''

tool_details=[
('JobSpy','speedyapply/JobSpy','2026-02-18 / MIT',
'作者定位是公开招聘信息抓取库。静态读取 jobspy/__init__.py 和 model.py，确认多站点适配、岗位URL/direct URL及描述字段；所查接口没有学历和招聘截止语义解析器。美国覆盖较广；未看到Handshake、BOSS或牛客原生适配。跨板去重和日期有效性仍需岗位ID/官网人工复核。',
'输入是关键词/地点等查询；请求发往目标招聘网站，可配置代理。库本身不需要把简历交给LLM，也不负责投递。MIT代码使用无单独授权费，代理、模型及维护成本视实际配置；未做费用或成功率测试。未来只在平台允许的范围试用公开搜索；不采用规避封禁的功能。',
'jobspy/__init__.py'),
('job-search-skill','Julien-ser/job-search-skill','2026-06-24 / 未确认许可证',
'README宣称支持LinkedIn、Indeed、Glassdoor和外部ATS，靠Playwright和代理理解JD；没有可确认的中美学历/2027届专用规则。跟踪Markdown可避免部分重复，但“只看最近一小时”默认规则可能漏掉仍开放的重要岗位。',
'静态SKILL.md前段要求用户最终提交，后面仍出现auto-submit和Submit步骤，形成直接冲突；不能把“不会自动提交”视为可靠默认。工作流会读取简历并填表/上传，代理模型与网站会接触相应数据。许可证和运行费用未确认，本轮不建议采用。',
'SKILL.md'),
('ai-job-agent','AkbarDevop/ai-job-agent','2026-04-26 / MIT',
'作者报告跨5个ATS完成大量申请，这属于作者案例，不是本次验证结果。读取skills/job-apply/SKILL.md，看到默认dry-run与--submit开关；技能仍会填入真实表单，URL触发范围较广。学历、季节、去重与来源追溯依赖配置/代理，未见可靠的本轮领域专用评测。',
'整套项目还包含邮箱、联系招聘者等流程。简历与个人资料可能进入模型、浏览器和ATS；dry-run不保证没有信息传入表单。MIT不等于模型/API免费，实际费用未测试。以后只考虑抽出受限的辅助模块，不以整套默认流程执行本次研究。',
'skills/job-apply/SKILL.md'),
('JobHuntBot','DanielPan12/JobHuntBot','2026-09-17 / MIT',
'静态SKILL.md明确要求区分届别、年份、当前入口以及旧/模糊线索，并默认首次试验只发现线索；最终提交需明确确认。dashboard/server.js是本地Node服务，监听127.0.0.1，配CSV表。适合复用本轮方向分流和待确认队列。',
'中美覆盖仍来自外部搜索/浏览器，未实测Handshake或国内ATS。看板可本地运行，但代理读到的简历仍受所用模型的数据流约束，“本地看板”不等于全部数据从不离机。Node服务代码无第三方运行依赖；代理成本和维护时间未量化。推荐以后仅复用lead-finding/dashboard部分。',
'SKILL.md'),
('job-seeker','galiprandi/job-seeker','2026-09-10 / MIT',
'静态apply技能包含Easy Apply搜索、--dry-run以及apply_batch_size=0停止自动投递的配置；默认其他流程仍覆盖提交、外联和日常邮箱处理。scripts/db.js确认通过Postgres访问候选人资料，README建议Neon。学历/日期判断仍依赖代理，缺少本轮专项验证。',
'资料、申请历史与消息可能存到外部Postgres，并被模型/浏览器处理；源码不入Git不等于数据不出本机。需要数据库、浏览器和模型环境，成本未测。README残留模板链接，文档完成度有限。当前范围仅研究，整套系统带来的配置和权限成本没有证实收益。',
'.agents/skills/apply/SKILL.md'),
('SimplifyJobs Summer2027目录','SimplifyJobs/Summer2027-Internships','2026-09-29 / API未标明许可证',
'它是社区职位目录和更新程序，不是自动求职代理。读取CONTRIBUTING.md及list_updater/listings.py，确认URL/ID去重、活动状态及高级学位标记流程；高级学位标记合并Master/MBA/PhD，不能自动判定MS是否合格。新近更新不保证每个职位仍开放。',
'本次README API正文未完整返回；以贡献规则和更新代码限定评估结论。美国技术实习为主要用途，中国机器人岗位覆盖未验证。单纯阅读目录无需上传简历；点击外部申请或使用Simplify产品是另一数据流。以后可作线索源，仍须复核官网；本轮没有用目录给岗位表供数。',
'CONTRIBUTING.md')]
tools_md=tool_intro
for name,repo,meta,cap,risk,codefile in tool_details:
 branch='master' if repo.startswith('Julien') else ('dev' if repo.startswith('Simplify') else 'main')
 tools_md+=f'\n## {name}\n\n仓库最后推送 / 许可：{meta}。最后推送只反映活动，不代表质量。\n\n{cap}\n\n{risk}\n\n依据：[{name}仓库](https://github.com/{repo})；[本次检查的文件](https://github.com/{repo}/blob/{branch}/{codefile})。\n'
tools_md+='''
## 能否替代本轮人工核验

没有证据表明这些工具能稳定完成“MSR/2028毕业/约三个月/2027暑期”的全部筛选。重点反例：博士必需与博士优先不同；国内2027届常指毕业年份；“至少接受至某日”不是截止；人才池不是已分配岗位；官方索引可能残留下架职位。工具收集速度不能替代这些判断。

以后如选择试验，建议仅用10条公开JD做只读对照：人工标注学位、季节、时长、活动状态与官方ID；比较遗漏、误纳、字段正确率和人工复核时间。所有硬条件有原文依据，零误标为已投递，且减少净人工时间后再决定是否继续。该试验本次未执行，也未建立任何持续自动化。
'''

direction_md='# 方向分析与岗位筛选\n\n核验日：2026-09-29。以CMU MSR、预计2028毕业、约三个月、美国优先为筛选基线。主方向建议是D1具身/VLA、D2学习控制、D3多模态；同时保留D4自主系统和D5机器人系统工程以扩大有效机会。这个排序来自既有证据与本轮JD要求，不代表录用概率。\n'
examples={'D1':['J030','J017'],'D2':['J023','J027'],'D3':['J012','J031'],'D4':['J004','J049'],'D5':['J002','J024']}
explain={
'D1':'VLA把视觉/语言观测映射为动作；世界模型预测动作或状态变化后的环境。简历中最强证据是把模型接入真实机器人并建立数据与评测链路。CMU世界模型课题仍是ongoing；不要把它写成已训练完成的算法贡献。',
'D2':'CBF是用于表达安全集合约束的控制方法；用户未提供完成的CBF系统或保证，因此仅写研究方向。Lie-MPC的真实ASV实验提供更成熟的控制证据。安全岗位可能要求形式化证明，与CBF并不是同一技能。',
'D3':'视觉KV压缩与流式视频工作支持多模态研究和推理效率方向。论文仍为ICLR投稿；它不能自动满足“强发表记录”门槛。边端推理岗位常额外要求CUDA/Rust/GPU体系结构，这些未写入简历已有技能。',
'D4':'把多机器人探索、主动SLAM与实船感知控制作为整体自主系统证据。机器人仿真迁移和传感器标定与地图/定位岗位相连，但不等于已经做过道路BEV、神经建图或量产自动驾驶。',
'D5':'这一方向强调系统能否复现、测试、排查问题并稳定运行。跨平台launch、真实rollout、场景复现和现场演示都是直接证据。云后端、SQL、CI/CD与全栈界面要求要逐岗看，不能由“会Python”推定全部满足。'}
for d in data['directions']:
 did=d['id'];direction_md+=f'\n## {did} {d["name"]}\n\n{explain[did]}\n\n简历证据：{d["evidence"].replace("8×24","8任务/24场景")}。对应版本：{did}。\n'
 for k in examples[did]:
  j=byid[k];direction_md+=f'\n代表JD：{jd(k)}。{j["summary"]}。学位/时间：{j["degree"]}；{j["season"]}。主要差距：{j["gap"]}。\n'

pending='''# 待确认事项

这些缺项集中保留，不在本轮逐项追问。已用保守文字完成可继续的本地材料。

| 事项 | 当前处理 | 以后在哪一步需要 |
|---|---|---|
| CMU毕业月份 | 只写Expected 2028 | Google/NVIDIA等要求MM/YYYY的正式表单前 |
| 2027实际可用起止日期 | 筛选约3个月；不承诺某个cohort | 对照J&J两档日期、10/12周岗位和国内最短时长 |
| CMU正式岗位头衔 | Graduate Student Researcher作为中性描述 | 获得实验室正式称谓后再替换；不写Senior/Lead |
| CMU课题具体边界 | WBC、CBF安全、world-model locomotion标ongoing | 明确本人实现模块、数据/训练、实验后再增加成果 |
| Dexmate可公开链接和结果 | 写已在IROS2026展示及本人四项贡献 | 公开作品集/投递附件前确认分享范围；不编造成功率或试验次数 |
| Demo中的policy来源/训练职责 | 只写agent planning与policy execution结合 | 若补技术细节，确认本人是否训练/改policy、夹爪适配范围及标定类型 |
| Unitree与Shanghai AI Lab的Present | 沿用原文 | 核对是否仍在职/远程并行，或需准确结束月份 |
| 论文状态与作者顺序 | 沿用原投稿/修订审稿/接收状态 | 正式使用前复核当前状态、日期、可公开链接；没有把投稿升级为录用 |
| 既有20%/2.5cm指标定义 | 保留原简历指标与措辞 | 备面试时补指标口径、基线、次数及误差统计；8任务/24场景不推定192组合 |
| CMU Handshake会话 | 独立会话停在登录页 | 用户登录后才能继续读取当前CMU账号下JD |
| BOSS/牛客登录及动态JD | 公开访问与账号能力分别记录 | 有需读取的具体JD时再恢复对应账号；本次不推断权限 |
| 国内日常实习时长/未来档期 | 未把日常岗标为2027暑期 | 具体团队确认能否约3个月、2027暑期开始 |
| 部分动态官网内容 | 分别标出入口/索引/实时正文层级 | 列表发现的Meituan、LimX等先补完整JD，不算确认岗位 |

个人工作授权不作推断，也不作为本轮追加问题。表格只记录JD明确给出的条件。
'''

scope=f'''# 2027暑期实习调研交付说明

本次覆盖{len(data['companies'])}家公司入口与岗位检索，收录{len(jobs)}条去重的岗位/项目记录。记录总量比70条少{70-len(jobs)}条；其中仅{counts['A']}条明确满足学位范围与2027暑期两个条件，按此口径距70岗仍差{70-counts['A']}岗。未达到70个符合条件岗位的目标。

| 分类 | 条数 | 含义 |
|---|---|---|
| A | {counts['A']} | 官网明确包含2027暑期，学位范围可覆盖MS；仅学位与季节层面匹配 |
| B | {counts['B']} | 季节、学位、专业、技能或JD信息仍待确认 |
| C | {counts['C']} | 博士/季节/时长不符、非实习形式或已撤下；用于对照，排除在适合数量之外 |
| T | {counts['T']} | 人才池、项目匹配池或多团队招聘轨道；另列，不计具体团队岗位 |

A也不表示所有条件已通过：许多岗位未公布最短时长，技能和JD授权条件仍需逐项判断。C类与T类不用于补足合格岗位数量。当前记录明显集中于Waymo和Bedrock；公司检索深度不同，低可访问页面只记录观察结论。本报告不是整个市场无遗漏的清单。

## 建议先看的短名单

Waymo先从Behavior Test、Conflict Behavior和Simulator Realism三条比较，结合希望偏工程、控制还是研究作选择；官网建议每人最多选择3岗。其他方向优先看J&J Systems/Simulation、Corning Advanced Process Controls，以及待确认暑期的Bedrock World Models/SLAM。NVIDIA DevTech Robotics可作为中国方向候选。这里是材料优先级建议，本轮未投递。

| 岗位 | 主要匹配 | 关键限制 |
|---|---|---|
| {jd('J002')} | 真机评测/测试基础设施，D5 | SQL、故障场景经验要补证据 |
| {jd('J010')} | 控制与安全指标，D2 | 实习时长未公布；CBF为进行中研究 |
| {jd('J012')} | ML+仿真评估，D3 | 统计与仿真真实性研究深度 |
| {jd('J024')} | 仿真/系统/硬件闭环，D5 | 预计2026-10-17关闭，可延长；固定cohort |
| {jd('J027')} | Lie-MPC、优化与系统辨识，D2 | 制造域知识；JD写明不支持移民担保 |
| {jd('J030')} | 世界模型/真机数据，D1 | 仅2027，未写暑期；世界模型课题ongoing |
| {jd('J049')} | SLAM+SAM/DINO+传感器，D4 | 未写暑期；学习型建图经验需补 |
| {jd('J017')} | VLA与部署研究，D1 | 中国岗位季节/3个月可行性待确认 |

## 本轮改变筛选结论的证据

{jd('J033','Bedrock旧Metric Prototyping链接')}仍出现在官方搜索索引，但浏览器实时页面已显示Job not found，已标为撤下。{jd('J051','Bedrock安全实习')}要求Lean/mathlib；CBF研究相关性不能替代这个技能门槛。

{jd('J023','J&J Controls')}的JD明确要求永久美国工作授权且不需要现在或未来担保。仅记录原条件，不推断个人资格。{jd('J018','NVIDIA Robotics Research')}和TRI Post-Training明确要求PhD，未计入MS匹配数量。NVIDIA的“至少接受至某日”不是明确截止；Google项目预计申请窗口也不是保证开放到该日。

## 简历处理

保存原始LaTeX快照，更新完整总简历，再生成D1-D5五套英文简历。加入Expected 2028、CMU Intelligent Control Lab、Prof. Changliu Liu、Aug.2026-Present与IROS2026 Dexmate贡献。未新增毕业月份、领导头衔、实验数字、正式论文录用或未证明的JD技能。

每套提供LaTeX、干净PDF、相对原版的红线LaTeX/PDF及changes.md。删除为红色删除线，新增为蓝色下划线；移动段落可同时出现删除和新增。红线对比覆盖PDF可提取文字，并验证可精确重构原版与新版词序列；版式差异另在changes.md说明。

## 文件使用

先在XLSX“岗位清单”按筛选结论、国家、方向和优先级过滤。A只表示学位/季节匹配；B/C/T保留不同用途。“公司观察”列出46家检索范围与访问限制，“方向与简历对应”连接到5个版本。岗位截止/窗口日期与核验日期使用Excel日期值，可按时间排序；未公布日期留空并在相邻说明列解释。

所有产物均在当前工作区。未投递、发送消息、上传简历、推送GitHub、安装/运行评估的求职工具或建立持续自动化。
'''

for filename,content in [('channel_access.md',access),('tool_evaluation.md',tools_md),('direction_analysis.md',direction_md),('pending_questions.md',pending),('delivery_summary.md',scope)]: (R/filename).write_text(content)
(ROOT/'resumes/master/changes.md').write_text('''# 总简历修改说明

基线为原始CMU_Ziyu_original.tex。教育日期从Aug.2026改为Aug.2026 -- Expected 2028，不添加毕业月份。

在研究经历首位新增Intelligent Control Lab, Carnegie Mellon University，Aug.2026 -- Present，Graduate Student Researcher，advised by Prof. Changliu Liu。

新增进行中的whole-body control、CBF safety、world-model-based locomotion研究；新增IROS2026 Dexmate双臂搭积木展示，说明agent规划与policy执行，列出agent、现场环境、夹爪适配、标定四项本人贡献。原其他经历、指标、论文状态和奖项完整保留。新增文字均来自本次用户提供的信息；正式头衔和更多demo细节留待确认。
''')

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
styles={
 'h1':ParagraphStyle('h1',fontName='STSong-Light',fontSize=21,leading=29,textColor=colors.HexColor('#173B55'),spaceAfter=14,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='STSong-Light',fontSize=14,leading=21,textColor=colors.HexColor('#173B55'),spaceBefore=14,spaceAfter=7,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='STSong-Light',fontSize=10.5,leading=17,spaceAfter=8,wordWrap='CJK'),
 'cell':ParagraphStyle('cell',fontName='STSong-Light',fontSize=9,leading=14,wordWrap='CJK'),
 'headcell':ParagraphStyle('headcell',fontName='STSong-Light',fontSize=9,leading=14,textColor=colors.white,wordWrap='CJK'),
}
def inline(s):
 # Escape first and selectively convert Markdown links to clickable PDF links.
 s=html.escape(s)
 s=re.sub(r'\[([^]]+)\]\((https?://[^)]+)\)',lambda m:f'<link href="{m.group(2)}" color="#135C8F"><u>{m.group(1)}</u></link>',s)
 return s.replace('—','-').replace('–','-')
def flow(md):
 lines=md.splitlines();items=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('|'):
   tab=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    row=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r'[-: ]+',c) for c in row):tab.append(row)
    i+=1
   n=len(tab[0]); widths=([95,48,355] if n==3 and tab[0][0]=='分类' else ([105,88,150,155] if n==4 else ([120,188,190] if n==3 else [498/n]*n)))
   cells=[[Paragraph(inline(c),styles['headcell' if r==0 else 'cell']) for c in row] for r,row in enumerate(tab)]
   t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#24485E')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#24485E')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#F2F5F8'),colors.white])]))
   items.extend([t,Spacer(1,10)]);continue
  if line.startswith('# '):items.append(Paragraph(inline(line[2:]),styles['h1']))
  elif line.startswith('## '):items.append(Paragraph(inline(line[3:]),styles['h2']))
  else:items.append(Paragraph(inline(line),styles['body']))
  i+=1
 return items
def footer(can,doc):
 can.saveState();can.setStrokeColor(colors.HexColor('#CBD5DF'));can.line(48,38,547,38);can.setFillColor(colors.HexColor('#536778'));can.setFont('Helvetica',8);can.drawString(48,25,'2027 Internship Research | 2026-09-29 | Local research only');can.drawRightString(547,25,str(doc.page));can.restoreState()
def pdf(path,sections):
 doc=SimpleDocTemplate(str(path),pagesize=(595.28,841.89),leftMargin=48,rightMargin=48,topMargin=42,bottomMargin=52,title=path.stem,author='Ziyu Xu - prepared with Codex')
 story=[]
 for index,section in enumerate(sections):
  if index:story.append(PageBreak())
  story+=flow(section)
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
pdf(pdfout/'Tool_Evaluation.pdf',[tools_md])
pdf(pdfout/'Research_Report.pdf',[scope,access,direction_md,pending])
print(json.dumps({'jobs':len(jobs),'companies':len(data['companies']),'counts':counts,'reports':[str(pdfout/'Tool_Evaluation.pdf'),str(pdfout/'Research_Report.pdf')]},ensure_ascii=False))
