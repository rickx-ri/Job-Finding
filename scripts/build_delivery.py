"""Create linked delivery indexes and a portable archive of final artifacts."""
import json, hashlib, re
from collections import Counter
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'sources/research_data.json').read_text())
qa = json.loads((ROOT/'qa/artifact_validation.json').read_text())
assert qa['native_hyperlinks'] == 103
assert len(qa['pdfs']) == 15
assert not qa['latex_overfull']
assert all(hashlib.sha256((ROOT/p['file']).read_bytes()).hexdigest() == p['sha256'] for p in qa['pdfs'])

qa_text = '''# 交付核验记录

核验日期：2026-09-29。此记录区分程序检查、视觉检查与未验证部分。

## 岗位数据

- 46家公司入口与检索记录；57条岗位/项目记录，A/B/C/T分别为22/18/8/9。
- 公司+官方岗位编号、官方URL均无重复；每条岗位映射至有效的D1-D5简历版本。
- 来源和关键条件逐行整理在表格中。动态页、旧索引、正文访问限制分别标记；未把HTTP 200当作岗位仍开放的充分证据。
- A仅表示学位范围与2027暑期两个条件匹配；没有把博士限定、已撤下及人才池记录计入A。记录总量距70少13条，按A口径距70少48岗；尚未确定满足全部个人条件的数量。
- 这是截至核验日的调研快照，公司检索深度不同，不能证明市场已无其他机会。

## XLSX

- 三个工作表均导出为原生Excel表格，筛选范围与冻结前4行已通过导出文件结构检查；岗位表冻结前3列，另两表冻结首列。
- 记录总数与A类数量公式重算为57和22；公式错误扫描未发现标准错误值。
- 61个岗位日期单元格为可排序的数值日期；未公布的日期保持空白，解释在相邻列。
- 103个官方URL保留可见文本并写入原生超链接关系，逐条核对关系目标。渲染引擎不支持HYPERLINK公式，已改用原生链接，避免缓存显示错误。
- 三张表及岗位表全部字段范围均已渲染检查，日期、长URL和文字可读。
- 未在桌面Excel中实际点击筛选、排序或链接；检查范围是重算、渲染与导出结构，不把它表述为原生应用交互测试。

## 简历与报告

- 原始简历、总简历、D1-D5及六份红线共13份简历PDF，每份2页；综合报告6页，工具评估3页，共15份PDF、35页。
- 所有简历LaTeX编译成功，未出现Overfull提示。每页文字可提取，字符边界检查通过；所有PDF逐页渲染后完成视觉检查。
- 六份红线以原始/新版PDF提取的词序列比较，可精确重构两侧序列；删除为红色删除线，新增为蓝色下划线。移动段落会同时表现为删除和新增；纯分页变化在修改说明中单独解释。
- 红线中的断词差异来自PDF行末断词，可能比语义修改更细；changes.md提供语义块的原文、改文、原因及代表JD。
- 五份changes.md已修复转义百分号导致的截句问题；保留20%及奖项百分比后的完整原文。
- 原始PDF是从保存的原始LaTeX本地重新编译的版本，不是远端PDF副本。原始LaTeX保留不改。

## 尚待确认

毕业月份、具体实习日期、实验室正式头衔、demo可公开证据、仍标Present的经历及CMU Handshake登录恢复，统一见待确认事项。个人工作授权没有推断。

本轮仅查找、静态评估和本地材料准备：没有投递、发送消息、上传简历、推送GitHub，或安装/运行调研的求职工具；没有建立自动化。
'''
(ROOT/'qa/verification_summary.md').write_text(qa_text)

variants = [
    ('完整总简历', 'master', 'Ziyu_Xu_master'),
    ('D1 具身智能 / VLA', 'D1_embodied', 'Ziyu_Xu_D1'),
    ('D2 全身控制 / 安全 / locomotion', 'D2_control', 'Ziyu_Xu_D2'),
    ('D3 VLM / 视频 / 推理效率', 'D3_vlm', 'Ziyu_Xu_D3'),
    ('D4 自主系统 / 规划 / SLAM', 'D4_autonomy', 'Ziyu_Xu_D4'),
    ('D5 机器人软件 / 仿真 / 评测', 'D5_systems', 'Ziyu_Xu_D5'),
]

def index(portable=False):
    def link(label, p):
        target = p if portable else str(ROOT/p)
        return f'[{label}](<{target}>)'
    text = '''# 2027暑期实习调研与简历适配

核验日期：2026-09-29。按CMU MSR、预计2028毕业、暑期约三个月、美国优先/中国备选整理。

本轮覆盖46家公司，收录57条去重的岗位/项目记录，其中A类22条、B类18条、C类8条、T类9条。A只确认学位范围与2027暑期匹配，不表示全部技能、实习时长或工作授权条件已满足。C为排除/对照，T为人才池或多团队项目，均不计入具体合格岗位。

未达到70岗目标：记录总量少13条，按A类口径少48岗。岗位集中度和访问限制已明确记录，不能把本轮结果当作市场的完整清单。

## 先看这些

'''
    text += '- '+link('岗位XLSX：岗位清单 / 公司观察 / 方向与简历对应', 'outputs/recruiting_2027/2027_Internship_Research.xlsx')+'\n'
    text += '- '+link('调研综合报告PDF', 'output/pdf/Research_Report.pdf')+'：含交付说明、渠道访问、方向分析与待确认事项。\n'
    text += '- '+link('自动求职工具评估PDF', 'output/pdf/Tool_Evaluation.pdf')+'：当前不需要新增自动求职工具；以后可选JobHuntBot线索/看板部分，JobSpy和Simplify目录作补充。\n'
    text += '- '+link('核验记录与限制', 'qa/verification_summary.md')+'：包含日期、筛选结构、链接、编译、红线完整性和视觉检查。\n'
    if not portable:
        text += '- '+link('全部交付文件ZIP', 'outputs/recruiting_2027/2027_Internship_Package.zip')+'：解压后从README.md进入，文件链接可随目录移动。\n'
    text += '\n## 简历\n\n干净版和红线版均为两页。删除用红色删除线，新增用蓝色下划线；移动内容可能同时出现删除和新增。LaTeX保持可编辑。\n\n'
    text += '| 版本 | 干净PDF | 红线PDF | LaTeX | 修改说明 |\n|---|---|---|---|---|\n'
    for label, folder, stem in variants:
        p = f'resumes/{folder}/'
        text += '| '+label+' | '+link('查看',p+stem+'.pdf')+' | '+link('查看',p+stem+'_redline.pdf')+' | '+link('干净',p+stem+'.tex')+' / '+link('红线',p+stem+'_redline.tex')+' | '+link('原文、改文与原因',p+'changes.md')+' |\n'
    text += '\n原始版本：'+link('原始LaTeX', 'resumes/original/CMU_Ziyu_original.tex')+'；'+link('原始PDF（本地重新编译）','resumes/original/CMU_Ziyu_original.pdf')+'。PDF并非从远端仓库下载的二进制副本。\n'
    text += '\n## 可编辑报告与来源\n\n'
    for label, name in [('交付说明及短名单','delivery_summary'),('渠道访问清单','channel_access'),('自动求职工具评估','tool_evaluation'),('方向分析','direction_analysis'),('待确认事项','pending_questions')]:
        text += '- '+link(label, 'reports/'+name+'.md')+'\n'
    text += '- '+link('结构化岗位与公司数据', 'sources/research_data.json')+'\n'
    text += '- '+link('原始简历来源与核验口径', 'sources/source_manifest.md')+'\n'
    text += '''
## 使用顺序

先按XLSX的筛选结论、国家、方向和优先级缩小范围，再核对季节/时长、必需技能及JD的授权条件。通用人才池和博士限定岗位单独保留。对照官方链接查看当前状态，再选对应D1-D5简历。

需要恢复CMU Handshake独立会话；其余缺项统一留在《待确认事项》。目前不需要逐项回复。

本轮没有投递、发送消息、上传简历、推送GitHub，或安装/运行评估的求职工具；没有建立持续自动化。
'''
    return text

(ROOT/'INDEX.md').write_text(index())
(ROOT/'README.md').write_text(index(portable=True))
paths = [ROOT/'INDEX.md', ROOT/'README.md', ROOT/'qa/verification_summary.md', ROOT/'sources/research_data.json', ROOT/'sources/source_manifest.md', ROOT/'resumes/manifest.json', ROOT/'outputs/recruiting_2027/2027_Internship_Research.xlsx']
paths += list((ROOT/'reports').glob('*.md')) + list((ROOT/'output/pdf').glob('*.pdf'))
paths += [p for p in (ROOT/'resumes').rglob('*') if p.is_file() and p.suffix in {'.tex','.pdf','.md'}]
assert len(paths) == len(set(paths))
zip_path = ROOT/'outputs/recruiting_2027/2027_Internship_Package.zip'
with ZipFile(zip_path, 'w', ZIP_DEFLATED) as z:
    for p in sorted(paths):
        z.write(p, '2027_Internship_Package/'+str(p.relative_to(ROOT)))
with ZipFile(zip_path) as z:
    assert z.testzip() is None
    names = set(z.namelist())
    for target in re.findall(r'\]\(<([^>]+)>\)', (ROOT/'README.md').read_text()):
        assert '2027_Internship_Package/'+target in names, target
    assert sum(n.endswith('.pdf') for n in names) == 15
    assert sum(n.endswith('.xlsx') for n in names) == 1
print(json.dumps({'package':str(zip_path),'files':len(paths),'bytes':zip_path.stat().st_size,'portable_links_valid':True},ensure_ascii=False))
