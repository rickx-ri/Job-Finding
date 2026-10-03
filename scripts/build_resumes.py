import re,json,subprocess,difflib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ORIG=ROOT/'resumes/original/CMU_Ziyu_original.tex'
src=ORIG.read_text(); pre,body=src.split('\\begin{document}',1)
parts=re.split(r'\\section\*\{([^}]+)\}\s*',body)
header=parts[0]; sections={parts[i]:parts[i+1] for i in range(1,len(parts),2)}
def clean_section(s):return s.split('%====================')[0].replace('\\end{document}','').strip()
sections={k:clean_section(v) for k,v in sections.items()}
research=[s.strip() for s in re.split(r'(?=\\resumeSubheading\s*\n)',sections['Research Experiences and Internships']) if s.strip()]
assert len(research)==5
keys=['unitree','shanghai','asv','autonomy','surgical'];oldblocks=dict(zip(keys,research))
heads={k:v.split('\\begin{itemize}')[0].strip() for k,v in oldblocks.items()}
def bullets(items):return '\\begin{itemize}[leftmargin=2.4em, itemsep=0.5pt, topsep=0pt]\n\\small\n'+'\n'.join('\\resumeItem{'+x+'}' for x in items)+'\n\\end{itemize}\n'
cmuhead=r'''\resumeSubheading
{Intelligent Control Lab, Carnegie Mellon University}
{Aug. 2026 -- Present}
{\hspace*{1.4em}Graduate Student Researcher, advised by Prof. Changliu Liu}
{Pittsburgh, PA}'''
cmu=[r'\textbf{Whole-Body and Safe Locomotion Research (ongoing):} Investigating whole-body control, safety with control barrier functions (CBFs), and world-model-based locomotion.',r'\textbf{Dexmate Bimanual Manipulation Demo, IROS 2026:} Contributed to a bimanual block-stacking demonstration combining agent planning with policy execution. Implemented the agent component, prepared the on-site environment, adapted the system to different grippers, and performed system calibration.']
updated_edu=sections['Education'].replace('{Aug. 2026}','{Aug. 2026 -- Expected 2028}',1)
master=pre+'\\begin{document}\n'+header+'\\section*{Education}\n'+updated_edu+'\n\\section*{Research Experiences and Internships}\n'+cmuhead+'\n'+bullets(cmu)+'\n'+sections['Research Experiences and Internships']+'\n'
for name in ['Publications and Manuscripts','Awards','Skills']:master+='\\section*{'+name+'}\n'+sections[name]+'\n'
master=master.replace(r'\resumeItem{\textbf{\textit{Field Perception',r'\newpage'+'\n'+r'\resumeItem{\textbf{\textit{Field Perception',1)
master+='\\end{document}\n'
MASTER=ROOT/'resumes/master/Ziyu_Xu_master.tex';MASTER.write_text(master)

base={
'unitree':[
r'\textbf{Real-Robot Policy Infrastructure:} Built and validated a closed-loop stack on Unitree H2/G1 humanoids integrating teleoperation, VLA/WAM and whole-body policy adapters, rollout logging, evaluation, controller interfaces, and policy fine-tuning; enabled one-command launches across platforms.',
r'\textbf{VLA Adaptation and Post-Training:} Deployed and fine-tuned Isaac GR00T/OpenPI policies with SONIC whole-body control using real-robot rollout traces. Developing phase-aware adaptation across embodiments by aligning semantic task progress and execution timing.',
r'\textbf{Reproducible Evaluation:} Implemented an 8-task, 24-scene manipulation benchmark with background variation. Built PICO-based scene digitization and AR-guided reconstruction with reusable layouts, achieving 2.5 cm median placement error.'],
'shanghai':[r'\textbf{Iterative Visual KV Compression:} Studied errors from reusing retained visual KV entries after neighboring tokens are removed in multi-turn and streaming inference. Developed context-aware re-encoding at original positions and compared with inheritance and restoration under matched memory and runtime budgets.'],
'asv':[
r'\textbf{Learning-Augmented Lie-MPC:} Developed and field-tested an autonomous surface vehicle controller that estimates residual wind/current disturbances online and corrects the dynamics used by MPC. Achieved a 20\% improvement in trajectory-tracking performance over baseline MPC in real-ASV experiments.',
r'\textbf{Field Perception:} Built DINO/SAM2 segmentation and fine-tuned Grounded-DINO/YOLO for submerged vegetation detection in autonomy experiments.',
r'\textbf{Sensor Integration:} Designed mounts and integrated, aligned, and calibrated GPS, lidar, IMU, and cameras for field data collection and closed-loop control.'],
'autonomy':[
r'\textbf{Multi-Robot Simulation and ROS2:} Rebuilt a Unity + AirSim multi-drone testbed with revised dynamics and sensing; migrated SlideSLAM communication from ROS1 to ROS2 for bandwidth-limited active-SLAM evaluation.',
r'\textbf{Communication-Aware Exploration:} Developed distributed EXP3-style algorithms using submodular objectives and bandit feedback to balance map coverage and communication cost in simulation.'],
'surgical':[r'\textbf{Surgical Video Segmentation:} Evaluated Segment Anything Model variants on surgical frames, examining domain shift and temporal mask stability around instruments, tissues, and interaction regions.']}
interests={
'D1':'Robot Foundation Models, VLA Adaptation, and Real-Robot Learning',
'D2':'Learning-Augmented Control, Whole-Body Control, and Safe Locomotion',
'D3':'Vision-Language Models, Streaming Video, and Efficient Inference',
'D4':'Autonomous Systems, Planning and Control, and Multi-Robot SLAM',
'D5':'Robotics Software, Simulation, and Reproducible Evaluation'}
configs={
'D1':('D1_embodied',['unitree','cmu','shanghai','asv','autonomy'],{'unitree':[0,1,2],'asv':[0],'autonomy':[0]},[0,1,2]),
'D2':('D2_control',['cmu','asv','unitree','autonomy','shanghai'],{'asv':[0,2],'unitree':[0,1],'autonomy':[0,1]},[2,0]),
'D3':('D3_vlm',['shanghai','unitree','surgical','cmu','asv','autonomy'],{'unitree':[1,2],'asv':[1],'autonomy':[0]},[0,1,3]),
'D4':('D4_autonomy',['autonomy','asv','unitree','cmu','shanghai'],{'asv':[0,1,2],'unitree':[0]},[2,0,1]),
'D5':('D5_systems',['unitree','autonomy','asv','cmu','shanghai'],{'asv':[2,0],'unitree':[0,2],'autonomy':[0]},[2,0,1])}
skillrows={
'D1':[r'\textbf{Robot Learning:} VLA post-training, real-robot deployment, whole-body policy integration, RL, teleoperation, rollout evaluation',r'\textbf{ML and Systems:} PyTorch, Python/C++, ROS/ROS2, Linux, Docker, Git, OpenCV, visual KV compression'],
'D2':[r'\textbf{Control and Autonomy:} MPC, learning-augmented control, RL, whole-body policy integration, real-robot experiments, sensor calibration',r'\textbf{Tools:} Python/C++, ROS/ROS2, PyTorch, Unity + AirSim, Linux, Git, CAD, sensor integration'],
'D3':[r'\textbf{Multimodal ML:} PyTorch, visual KV compression, streaming/multi-turn inference evaluation, LLM fine-tuning, SAM2, Grounded-DINO, YOLO, OpenCV',r'\textbf{Systems:} Python/C++, Linux, Git, Docker, ROS/ROS2, real-robot policy deployment'],
'D4':[r'\textbf{Autonomy:} Active-SLAM simulation, communication-aware exploration, MPC, RL, perception, sensor integration and calibration',r'\textbf{Tools:} Python/C++, ROS/ROS2, Unity + AirSim, PyTorch, OpenCV, Linux, Docker, Git, CAD'],
'D5':[r'\textbf{Robotics Systems:} ROS/ROS2, Python/C++, Unity + AirSim, Linux, Docker, Git, sensor integration, teleoperation and policy interfaces',r'\textbf{Evaluation and ML:} Real-robot benchmarks, rollout logging, PyTorch, OpenCV, scene reconstruction, model evaluation under matched budgets']}
pubsection=sections['Publications and Manuscripts']
pubitems=re.split(r'\n\s*\\item ',pubsection)[1:]
pubitems=[x.split('\\end{itemize}')[0].strip() for x in pubitems]
assert len(pubitems)==4
def selectedpub(indices):
 # Preserve complete author lists, titles, and publication status; shorten line spacing only.
 return '\\begin{itemize}[leftmargin=1.4em,itemsep=3pt,topsep=2pt]\n\\small\n'+'\n'.join('\\item '+pubitems[i].replace('\\\\\n',' ').replace('\\\n',' ') for i in indices)+'\n\\end{itemize}\n'
def plain(s):
 s=re.sub(r'(?<!\\)%[^\n]*','',s)
 s=s.replace('\\&','&').replace('\\%','%').replace('\\ldots','...').replace('~',' ')
 s=re.sub(r'\\hspace\*?\{[^}]*\}','',s)
 s=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?','',s)
 s=re.sub(r'\\[A-Za-z]+\*?(?:\[[^]]*\])?','',s)
 return re.sub(r'\s+',' ',s.replace('{','').replace('}','').replace('\\','')).strip()
original_interest='Robot Foundation Models, Real-World Policy Adaptation, and Learning-Augmented Control'
jobs_by_id={j['id']:j for j in json.loads((ROOT/'sources/research_data.json').read_text())['jobs']}
representatives={'D1':['J030','J017'],'D2':['J023','J027'],'D3':['J012','J031'],'D4':['J004','J007'],'D5':['J002','J024']}
manifest=[]
for did,(folder,order,selected,pubs) in configs.items():
 pubs=pubs+[i for i in range(4) if i not in pubs]
 h=header.replace(original_interest,interests[did])
 # Keep the original 11pt Charter face, margins, section rules, and entry macros.
 target=pre+'\\begin{document}\n'+h+'\\section*{Education}\n'+updated_edu+'\n\\section*{Research Experiences and Internships}\n'
 newblocks={}
 for block_index,key in enumerate(order):
  if block_index==3:target+='\\newpage\n{\\small Ziyu (Rick) Xu}\\hfill{\\small Research experience continued}\n\\vspace{4pt}\n'
  if key=='cmu':b=cmuhead+'\n'+bullets(cmu)
  else:b=heads[key]+'\n'+bullets([base[key][i] for i in selected.get(key,range(len(base[key])))])
  newblocks[key]=b;target+=b+'\n'
 target+='\\section*{Publications and Manuscripts}\n'+selectedpub(pubs)
 target+='\\section*{Selected Awards}\n\\small Gold Medal, University Physics Competition (2023); Dean\'s Honor List, University of Michigan (2024, 2025).\n'
 target+='\\section*{Skills}\n'+bullets(skillrows[did])+'\\end{document}\n'
 path=ROOT/'resumes'/folder/f'Ziyu_Xu_{did}.tex';path.write_text(target)
 reasons={
 'D1':'对照 Bedrock World Models 与 NVIDIA DevTech：优先真机模型适配、真实数据与评测。',
 'D2':'对照 J&J Controls R-099654 与 Corning 78170：优先控制建模、系统辨识、闭环实验与安全研究。',
 'D3':'对照 Waymo 5432 与 Bedrock ML Inference：优先VLM研究、预算匹配评测及模型部署。',
 'D4':'对照 Waymo 5452/5411：优先规划/感知/多机器人与C++/ROS2系统证据。',
 'D5':'对照 Waymo 5361 与 J&J R-100027：优先仿真、部署、日志、标定和测试。'}
 changes=[f'# {did} 简历修改说明',reasons[did], '基线：resumes/original/CMU_Ziyu_original.tex。以下列出各语义块的完整旧文/新文；红线PDF另覆盖全部可提取文字变化。调整经历顺序只表示相关性，不改变时间。','## 共同新增与日期','原文：CMU Aug. 2026；未包含CMU实验室经历。','改文：CMU Aug. 2026 – Expected 2028；新增 Graduate Student Researcher (Aug. 2026 – Present)。',plain(newblocks['cmu']),'原因：用户提供事实；中性头衔；ongoing不冒充完成；IROS demo只写确认过的个人贡献。','## 研究兴趣','原文：'+original_interest,'改文：'+interests[did], '原因：'+reasons[did]]
 for key in keys:
  changes+=['## '+key,'原文：'+plain(oldblocks[key]),'改文：'+(plain(newblocks[key]) if key in newblocks else '本定向版删除此经历；总简历保留。'),'原因：'+('压缩冗长描述并按目标JD突出已存在的事实；不增加技能、数字或领导职责。' if key in newblocks else '为两页限制和方向相关性让出空间。')]
 changes+=['## 论文、奖项与技能','原文论文：'+plain(pubsection),'改文论文：'+plain(selectedpub(pubs)),'原因：按相关性调整论文顺序，完整保留作者、标题和投稿/审稿/接收状态。','原文奖项：'+plain(sections['Awards']),'改文奖项：Gold Medal, University Physics Competition (2023); Dean\'s Honor List, University of Michigan (2024, 2025).','原因：压缩次要荣誉，不改变奖项层级；其余留在总简历。','原文技能：'+plain(sections['Skills']),'改文技能：'+plain(bullets(skillrows[did])),'原因：只重排和筛选已有技能，不填入JD出现但简历未证明的SQL/CUDA/Rust/TPU/PLC等。','## 版式','沿用原11pt Charter、0.65英寸边距、章节线与经历格式。前三段研究经历后明确分页，第二页增加续页标识，避免仅少量文字溢出到第二页。论文减少人为换行；红线文档为完整文本审阅版，不受两页限制。']
 changes+=['## 代表JD与适配边界','以下为官网要求摘要；关键词匹配不代表满足所有资格，未证明的能力保留为缺口。']
 for jid in representatives[did]:
  j=jobs_by_id[jid]
  changes+=[f'[{j["company"]} / {j["req_id"]}]({j["source"]})：{j["title"]}。要求：{j["required"]}。现有证据：{j["fit"]}。缺口：{j["gap"]}。']
 (path.parent/'changes.md').write_text('\n\n'.join(changes)+'\n')
 manifest.append(dict(id=did,tex=str(path.relative_to(ROOT)),pdf=str(path.with_suffix('.pdf').relative_to(ROOT))))

if '--notes-only' in sys.argv:
 print('Regenerated five change notes; PDF content unchanged')
 sys.exit(0)

def compile_tex(path):
 p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(path.parent),str(path)],capture_output=True,text=True)
 if p.returncode:raise RuntimeError(p.stdout[-4500:])
 return p.stdout
paths=[ORIG,MASTER]+[ROOT/x['tex'] for x in manifest]
logs={}
for p in paths:
 logs[str(p.relative_to(ROOT))]=compile_tex(p)
print('Compiled original, master and five tailored resumes')
Path('qa/latex_compile.json').write_text(json.dumps({k:{'overfull':[x for x in v.splitlines() if 'Overfull' in x],'output':[x for x in v.splitlines() if 'Output written' in x]} for k,v in logs.items()},indent=2))
def pdftxt(p):return subprocess.check_output(['pdftotext','-layout',str(p),'−'],text=True) if False else subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True)
oldwords=pdftxt(ORIG.with_suffix('.pdf')).split()
def esc(s):
 table={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','ﬀ':'ff','ﬁ':'fi','ﬂ':'fl','ﬃ':'ffi','ﬄ':'ffl','•':'','–':'--','—':'---','−':'-','’':"'",'“':'``','”':"''"}
 return ''.join(table.get(c,c) for c in s)
audits=[]
for p in [MASTER]+[ROOT/x['tex'] for x in manifest]:
 newwords=pdftxt(p.with_suffix('.pdf')).split();sm=difflib.SequenceMatcher(a=oldwords,b=newwords,autojunk=False);chunks=[];oldback=[];newback=[];added=deleted=0
 for tag,a,b,c,d in sm.get_opcodes():
  if tag=='equal':chunks.append(' '.join(esc(t) for t in oldwords[a:b]));oldback+=oldwords[a:b];newback+=newwords[c:d]
  else:
   if tag in ('replace','delete'):
    chunks.append(' '.join(r'\del{'+esc(t)+'}' for t in oldwords[a:b]));oldback+=oldwords[a:b];deleted+=b-a
   if tag in ('replace','insert'):
    chunks.append(' '.join(r'\add{'+esc(t)+'}' for t in newwords[c:d]));newback+=newwords[c:d];added+=d-c
 assert oldback==oldwords and newback==newwords
 redbody=' '.join(chunks)
 for section_label in ['Education','Research Experiences and Internships','Publications and Manuscripts','Selected Awards','Awards','Skills']:
  redbody=re.sub(r'(?<![A-Za-z{])'+re.escape(section_label)+r'(?![A-Za-z}])',r'\\par\\medskip\\textbf{'+section_label+r'}\\par ',redbody)
 red=r'''\documentclass[10pt,letterpaper]{article}
\usepackage[margin=0.65in]{geometry}
\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage{charter}
\usepackage{xcolor}\usepackage[normalem]{ulem}\usepackage{hyperref}
\newcommand{\del}[1]{{\color{red}\sout{#1}}}
\newcommand{\add}[1]{{\color{blue}\uline{#1}}}
\setlength{\parindent}{0pt}\setlength{\parskip}{6pt}
\emergencystretch=3em
\begin{document}
\textbf{Ziyu Xu -- Full-text redline against original resume}\\
\del{Red strikeout: deleted} \quad \add{Blue underline: added}\\
'''+esc(p.stem)+r'''\par
Original baseline: CMU\_Ziyu\_original.tex. All visible text is compared in PDF reading order; moved content appears as deletion and insertion. Layout-only changes are described in changes.md.
\hrule\medskip
'''+ redbody+r'\end{document}'
 redpath=p.with_name(p.stem+'_redline.tex');redpath.write_text(red);compile_tex(redpath)
 audits.append(dict(file=str(redpath.relative_to(ROOT)),original_tokens=len(oldwords),new_tokens=len(newwords),added_tokens=added,deleted_tokens=deleted,exact_original_and_new_reconstruction=True))
Path('qa/redline_coverage.json').write_text(json.dumps(audits,indent=2))
Path('resumes/manifest.json').write_text(json.dumps(manifest,indent=2))
print('Compiled six complete redlines; reconstructed original/new token streams exactly')
