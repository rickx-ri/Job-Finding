"""Curated research records from individually reviewed official pages, 2026-09-29."""
import json
from pathlib import Path
DATE='2026-09-29'
jobs=[]
def add(company,title,rid,direction,location,url,summary,required,plus,fit,gap,**kw):
 d=dict(id=f'J{len(jobs)+1:03}',company=company,title=title,req_id=rid,direction=direction,location=location,country='美国',season='2027暑期',duration='未公布；约3个月可行性待确认',status='开放：官网JD及申请入口',deadline=None,deadline_type='未公布',deadline_note='未公布截止，不等于长期有效',degree='BS/MS/PhD或相关专业在读',phd='非必需',graduation='未指定毕业年份',return_school='未单独写明',summary=summary,required=required,preferred=plus,fit=fit,gap=gap,priority='P1',category='A 学位与暑期匹配',kind='具体岗位',authorization='正文未明确；不推断个人资格',source=url,discovery='人工检索公司官网',verification='官方正文',checked=DATE,resume=direction.split('/')[0])
 d.update(kw);jobs.append(d);return d

W='https://careers.withwaymo.com/jobs/'
waymo=[
('Machine Learning, Simulator Evaluation','5408','D5','Mountain View, CA','2027-summer-intern-ms-phd-machine-learning-simulator-evaluation-mountain-view-california-united-states','仿真器评测指标与数据分析、模型质量评估','Python、SQL、ML评测','机器人/自动驾驶、后端系统','Unitree 8任务24场景评测；真机日志','SQL及大规模评测后端证据不足','MS/PhD'),
('Software Engineering, Behavior Test','5361','D5','San Francisco, CA','2027-summer-intern-ms-software-engineering-behavior-test-san-francisco-california-united-states','异常/故障与远程辅助行为验证，指标和分析工具','Python、SQL、统计数据分析','测试工具、数据管道','真机闭环评测、ROS2测试平台','故障注入和SQL需补作品证据','MS'),
('Perception Machine Learning','5456','D3','Mountain View, CA','2027-summer-intern-ms-phd-perception-machine-learning-mountain-view-california-united-states','多传感器3D检测、跟踪、占用及基础模型','PhD，或具有强发表记录的MS；Python与深度学习','多模态感知、论文','视觉KV、分割和VLM研究','MS强发表记录为额外门槛；投稿不等于发表','PhD或强发表记录MS'),
('Road Understanding ML Engineer','5452','D4','Mountain View, CA','2027-summer-intern-ms-phd-road-understanding-ml-engineer-mountain-view-california-united-states','道路几何/拓扑建模及感知训练评测','Python、PyTorch、3D几何、Transformer','DETR/GNN/BEV、HD地图、分布式训练','ASV感知、机器人空间标定','缺道路建图/BEV项目证据','MS/PhD'),
('Multiverse SWE','5433','D5','Mountain View, CA','2027-summer-intern-ms-phd-software-engineer-multiverse-mountain-view-california-united-states','日志聚类及不良驾驶行为检测、自动分析管道','C++、Python、SQL','ML训练评测、分布式系统、agent原型','rollout日志与跨平台基础设施','SQL/分布式规模未证明','MS/PhD'),
('Embedded Software Engineer','5438','D5','Mountain View, CA','2027-summer-intern-bs-ms-embedded-software-engineer-mountain-view-california-united-states','固件与software-in-the-loop测试、嵌入式集成','C/C++、Linux、Git、数据结构','RTOS、gtest、板级调试','嵌入式课程、传感器和控制接口','RTOS/固件深度缺证据','BS/MS'),
('Maneuvering Tech','5411','D4','San Francisco, CA','2027-summer-intern-bs-ms-software-engineer-maneuvering-tech-san-francisco-california-united-states','场站驾驶行为、失败日志及感知评估','C++、软件工程','图搜索、优化规划、Python/SQL','多机器人探索与规划、实船控制','自动驾驶场景及生产C++需补','BS/MS'),
('Pipeline Test Health','5365','D5','San Francisco, CA','2027-summer-intern-bs-ms-software-engineer-pipeline-test-health-san-francisco-california-united-states','关键仿真测试自动化及测试健康度','Python/C++、复杂系统调试','SRE/SLO、SQL','Unity/AirSim、ROS2及复现流程','缺服务可靠性/SLO经验','BS/MS'),
('Scenes','5422','D1','Mountain View, CA','2027-summer-intern-bs-ms-software-engineer-scenes-mountain-view-california-united-states','大型ML模型上车集成与实时行为系统','Python/C++、数据结构','ML/CV/规划','Unitree模型部署、策略与控制接口','汽车软件栈和生产质量要求','BS/MS'),
('Conflict Behavior','5421','D2','Mountain View, CA','2027-summer-intern-ms-phd-software-engineer-conflict-behavior-mountain-view-california-united-states','可达性与安全裕度指标，真实/仿真长尾事件评价','Python/C++、统计分析','SQL、物理建模','Lie-MPC、进行中的CBF安全研究','CBF研究尚无已验证结果；道路经验待补','MS/PhD'),
('ML Engineer','5446','D3','San Francisco, CA','2027-summer-intern-ms-phd-machine-learning-engineer-san-francisco-california-united-states','驾驶日志Transformer微调、校准与严格模型评测','ML训练、Python、数据与损失调试','JAX/Flax、TPU、论文、分布式','视觉KV预算匹配实验、PyTorch','JAX/TPU与PR-AUC校准经验未确认','MS/PhD'),
('Simulator Realism Evaluation','5432','D3','San Francisco, CA','2027-summer-intern-ms-phd-machine-learning-engineer-simulator-realism-evaluation-san-francisco-california-united-states','用ML判别器和统计实验评估仿真真实性','C++、Python、ML、统计','分布式加速系统','仿真平台、真机评测与对照实验','缺仿真真实性判别器成果','MS/PhD'),
('Software Engineer, Onboard Behavior','5453','D4','Mountain View, CA','2027-summer-intern-ms-phd-software-engineer-mountain-view-california-united-states-5fee6bf6-c4ad-4bfa-ad0b-7a335c8f649d','交通规则行为软件及大规模仿真安全/平顺性验证','C++、算法与数据结构','实时、容错系统','ROS2、多机器人与闭环控制','交通法规行为模块/生产容错未证明','MS/PhD'),
('Simulation Evaluation ML Model','5441','D3','Mountain View, CA','2027-summer-intern-ms-phd-software-engineer-simulation-evaluation-ml-model-mountain-view-california-united-states','仿真日志语义图与多模态检索评测','Python/C++、Linux、PyTorch','图/GNN、RAG、分布式','VLM压缩、视频研究、仿真日志','RAG/GNN非已证明技能','MS/PhD')]
# Resolve canonical URLs from saved primary-page snapshots where available.
cache=[json.loads(p.read_text()) for p in Path('sources/public').glob('*.json')]
for title,rid,d,loc,slug,s,req,pref,fit,gap,deg in waymo:
 url=W+slug
 for c in cache:
  if 'careers.withwaymo.com' in c['url'] and (f'Job ID: {rid}' in c['text'] or f'Job ID\n{rid}' in c['text'] or rid in c['text']):
   url=c['url'];break
 row=add('Waymo',f'2027 Summer Intern — {title}',rid,d,loc,url,s,req,pref,fit,gap,degree=deg,deadline_type='滚动',deadline_note='官方写明岗位填满为止；每人建议最多申请3个岗位')
 if rid=='5456':row.update(category='B 额外资格待核',priority='P2',phd='PhD或MS强发表记录')
 if rid in ['5441','5446']:row['return_school']='结束后至少一学期/返校'

add('Google','Student Researcher, BS/MS, Winter/Summer 2027','131518356678156998','D3','美国多地','https://www.google.com/about/careers/applications/jobs/results/131518356678156998-student-researcher-bsms-wintersummer-2027','研究项目匹配，覆盖ML/CV/机器人等；并非专属机器人组','BS/MS在读、相关研究与编程','研究论文、具体领域专长','MSR+VLM/机器人研究','大多数项目优先PhD；需团队匹配与毕业月份',degree='BS/MS',season='2027冬/夏',kind='项目匹配池',category='T 人才/项目池',priority='P2',deadline='2027-07-16',deadline_type='预计申请窗口',deadline_note='预计接受至2027-07-16，可提前结束；滚动审阅')
NV='https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/'
add('NVIDIA','2027 Internships: Autonomous Vehicles and Robotics','JR2023496','D1','Santa Clara及美国多地',NV+'US-CA-Santa-Clara/NVIDIA-2027-Internships--Autonomous-Vehicles-and-Robotics_JR2023496','自动驾驶和机器人多个技术团队匹配','BS/MS/PhD在读、相关编程研究能力','深度学习、机器人/自动驾驶','Unitree部署、仿真与控制组合','通用池，不保证具体组；要求毕业月/年',duration='至少12周',kind='通用实习池',category='T 人才/项目池',season='2027，具体季节按团队确认',return_school='持续在读；毕业月份需提供',status='官方职位页可读；团队名额另定')
add('NVIDIA','AI Developer Technology Intern, Robotics — 2027','JR2024054','D1','上海/中国',NV+'China-Shanghai/AI-Developer-Technology-Intern--Robotics---2027_JR2024054-1','机器人基础模型训练/推理、VLA与世界模型技术优化','MS/PhD；Python/PyTorch、机器人/AI','CUDA、分布式FSDP/NeMo等','GR00T/OpenPI部署与VLM研究','CUDA/大规模训练未确认；暑期与3个月需确认',country='中国',degree='MS/PhD',season='2027，季节未写明',category='B 时间待确认',status='官方JD索引可读；动态入口待确认')
add('NVIDIA','Research Intern, Robotics — Summer 2027','JR2025647','D1','Seattle, WA',NV+'US-WA-Seattle/Research-Intern--Robotics---Summer-2027_JR2025647','机器人学习研究','必须PhD在读、机器人ML研究','高水平论文','研究内容相近','当前MSR学籍不满足PhD硬门槛',degree='PhD在读',phd='必需',category='C 硬条件不符',priority='排除',deadline_type='最早接受日期',deadline_note='至少接受申请至2026-09-25，不是关闭日期',discovery='Indeed发现；公司官网核验',status='官方JD可读；仅作要求对照')
add('NVIDIA','Research Intern, Physical AI Foundation Models — 2027','JR2025103','D1','美国',NV+'US-CA-Santa-Clara/Research-Intern--Physical-AI-Foundation-Models---2027_JR2025103','GEAR/Physical AI基础模型研究','PhD在读、深度学习研究','VLA/世界模型、论文','Unitree+VLM方向相邻','PhD硬门槛',degree='PhD在读',phd='必需',category='C 硬条件不符',priority='排除',season='2027，季节待确认',deadline_type='最早接受日期',deadline_note='至少接受申请至2026-09-21；不作为截止',status='官方JD索引可读；动态入口待确认')
for title,rid,d,s,req,fit,gap,duration in [
('Software Development Engineer Intern/Co-Op, ROBOTICS','10529525','D5','机器人软件、分布式服务、生产测试与维护','本科以上STEM在读；编程、数据结构与算法','ROS2、跨平台部署与日志评测','AWS/数据库/生产服务经验不足','未公布；夏季或春秋Co-op'),
('Hardware Development Engineer Intern/Co-Op, ROBOTICS','10535282','D5','硬件原型、测试、可靠性与工程文档','BS/MS以上；CAD、硬件设计开发与测试','ASV传感器集成、CAD和真机测试','硬件可靠性/量产经验不足','3-6+个月；可选约3个月但不保证'),
('Industrial Development Engineer Intern/Co-Op, ROBOTICS','10536817','D5','制造流程、布局与机器人设施优化','工程本科以上；美国校区在读；CAD','机械/电气背景与CAD','工业流程方向，距机器人学习研究较远','未公布')]:
 slug=title.lower().replace('/','-').replace(',','').replace(' ','-')+'-2027'
 add('Amazon',title+' — 2027',rid,d,'North Reading/Westborough, MA及其他美国地点','https://www.amazon.jobs/en/jobs/'+rid+'/'+slug,s,req,'既有实习、机器人相关项目',fit,gap,duration=duration,season='2027夏实习或春/秋Co-op',degree='BS/MS或以上',return_school='至少一学期（SDE/HDE）；工业岗美国在读',kind='多团队招聘轨道',category='T 多团队招聘轨道',priority='P1' if rid=='10529525' else 'P2')
for title,rid,d,slug,s,req,pref,fit,gap in [
('Robotics Controls & Autonomy Intern','R-099654','D2','robotics-controls-autonomy-intern-robotics-rd','运动学、控制/自主算法及实时软件验证','相关BS/研究生在读；GPA≥3.0、C++/控制','机器人、优化、系统集成','Lie-MPC实船20%改善、CMU安全研究','医疗器械实时标准；JD授权条件须单独核对'),
('Systems & Simulation Engineering Intern','R-100027','D5','systems-simulation-engineering-intern-robotics-rd','系统建模、仿真、需求追溯、实验相关性验证','BS高年级或研究生；GPA≥3.0、工程分析','MATLAB/Simulink/ANSYS等、Python/C++、MBSE','Unity/AirSim、机器人仿真与硬件闭环','SysML/JAMA/DOORS等未证明'),
('Software Engineering Intern','R-099919','D5','software-engineering-intern-robotics-rd','机器人手术软件、测试与可靠性开发','BS/研究生/PhD在读；GPA≥3.0；相关工程专业','跨学科开发、质量与网络安全','ROS2、跨平台策略软件、手术视觉','医疗软件合规工程经验未证明')]:
 r=add('Johnson & Johnson',title+' — Robotics R&D',rid,d,'Santa Clara, CA（Hybrid）','https://www.careers.jnj.com/en/jobs/'+rid.lower()+'/'+slug+'/',s,req,pref,fit,gap,duration='2027-06-01至08-20，或06-21至09-10；40h/周',degree='本科/硕士/博士',return_school='实习结束后返校',deadline='2026-10-17',deadline_type='预计关闭日期',deadline_note='预计2026-10-17；公司明确可能延长',discovery='CMU Handshake邮件（Controls）/官网',authorization='入职及任职期间需美国工作授权')
 if rid=='R-099654':r['authorization']='JD明确永久美国工作授权且不提供现在/未来担保；不推断个人状态'
for title,rid,d,loc,slug,s,req,pref,fit,gap in [
('Vision System Intern','77396','D3','Painted Post, NY','Painted-Post-Vision-System-Intern-Summer-2027-NY-14870/1425508200/','2D/3D视觉、相机标定、检测/分割与工业机器人','BS/MS/PhD；2027年12月或以后毕业；Python/C#、视觉基础','OpenCV/PyTorch/Halcon','ASV感知、标定、SAM评测','工业视觉/Halcon经验未确认'),
('Intern, Advanced Process Controls','78170','D2','Painted Post, NY','Painted-Post-Intern,-Advanced-Process-Controls-Summer-2027-NY-14870/1432275700/','模型控制、系统辨识、优化、故障监测','BS/MS/PhD；控制/动态系统/统计基础；Python或MATLAB','MPC/PID、数值优化','Lie-MPC、在线扰动学习、凸优化课程','制造过程知识需学习'),
('Intern, Controls Engineering','77402','D5','Painted Post, NY','Painted-Post-Intern,-Controls-Engineering-Summer-2027-NY-14870/1425734500/','Digital Factory Lab机器人/传感器/视觉系统搭建与演示','机器人/电气相关学位在读；编程与机电基础','CAD、控制、机器人项目','系统集成、Dexmate演示、CAD','PLC和工业网络未证明'),
('Controls Engineer Intern','77365','D2','Canton, NY','Canton-Controls-Engineer-Intern-Summer-2027-NY-13617/1425733700/','PLC/HMI/SCADA开发与现场控制调试','BS/MS；控制和工业自动化基础','Ladder/Structured Text、CAD','机械+ECE背景与闭环控制','PLC技能缺口；工业控制非学习研究')]:
 r=add('Corning',title+' — Summer 2027',rid,d,loc,'https://corningjobs.corning.com/job/'+slug,s,req,pref,fit,gap,degree='BS/MS/PhD' if rid in ['77396','78170'] else ('BS/MS' if rid=='77365' else '相关学位在读，未限学位层级'),priority='P1' if rid in ['77396','78170'] else 'P2',authorization='JD写明不支持移民担保' if rid!='77402' else '正文未明确；不推断个人资格')
 if rid=='77396':r.update(duration='10周',graduation='2027-12或以后')
B='https://jobs.ashbyhq.com/bedrock-robotics/'
for title,rid,d,s,req,pref,fit,gap in [
('Behavior ML Engineer, World Models','c51d682e-58ee-44de-886f-4cfacb56d2e1','D1','真实车队世界模型训练、消融与控制连接','BS/MS/PhD或同等；Python、PyTorch、复现论文与实验判断','视频预测/世界模型、RL/IL、大规模训练','Unitree数据与策略适配；CMU在研世界模型','世界模型研究进行中；不得声称已完成成果'),
('Onboard Infrastructure Engineer, ML Inference','0331551e-c18e-428a-8e91-e6cb25c9c2e8','D3','LLM/VLA边端集成、确定性延迟与推理优化','BS/MS/PhD；Rust/C++、PyTorch/JAX、GPU/CUDA或并行','TensorRT/ONNX、KV管理、量化','VLM KV压缩+机器人部署','CUDA/Rust/推理kernel性能证据不足'),
('Validation & Verification Test Engineer','c396dedc-06ec-4a23-8408-0194e360f30e','D2','执行器响应/时延/死区等系统验证、分析sim/real差异','控制或系统辨识、Python、传感器/DAQ、现场测试','ROS、机器人仿真、液压','实船控制、传感器校准、实机评测','液压与重型机械经验未知'),
('Evaluation Engineer, Metric Prototyping','07b55743-d5c4-4347-bfac-000821317b13','D5','原型指标、现场真值验证、回归评估与分析工具','BS/MS/PhD或同等；Python、统计、定义可解释指标','机器人评测、点云/测绘','8任务24场景benchmark、预算匹配评测','施工域指标/现场真值需学习'),
('Sensor Systems Engineer','d7da851b-55c2-45d4-bf8b-aa879282f25c','D4','传感器视场/位置/遮挡权衡与现场验证','BS/MS/PhD或同等；3D变换、Python、CAD','传感器覆盖仿真、自动驾驶suite','GPS/lidar/IMU/camera集成与标定','传感器物理/覆盖模拟经验待补'),
('Hardware Engineer, Machine Integration & Test','c9c08251-6a42-4f9c-be4d-2621995cc8f9','D5','机载硬件接口、支架/线束、台架测试','BS/MS或同等；CAD、动手制造、基础电气','线束设计、机加工/3D打印','机械和电气学位、传感器安装','重型工程车经验未知；偏硬件'),
('Software Engineer, Fleet Platform','8927dd7e-a48d-49a2-92eb-09ec059432f4','D5','机器人生命周期内部工具、数据后端和界面','BS/MS或同等；全栈应用、Python/Rust/C++/TS等','遥测、数据可视化、云/CI/CD','部署工具和日志基础设施','全栈前端/云部署证据不足')]:
 r=add('Bedrock Robotics','2027 Internship — '+title,rid,d,'New York, NY' if 'Fleet' in title else 'San Francisco, CA',B+rid,s,req,pref,fit,gap,season='2027；暑期未明确',category='B 时间待确认',status='官方JD可读；实时入口待复核',verification='官方索引正文',degree='BS/MS/PhD或同等经验' if 'BS/MS/PhD' in req else ('BS/MS或同等' if 'BS/MS' in req else '所读正文未限定'),discovery='CMU招聘邮件（V&V）/官网人工检索')
 if 'World Models' in title:r.update(status='开放：浏览器官网及申请入口',verification='浏览器现场正文')
 if 'Fleet' in title:r.update(season='2027暑期（正文明确summer）',category='B 入口待确认')

add('Neuralink','Software Engineer Intern, Robotics','5469305003','D4','Austin, TX / South San Francisco, CA','https://job-boards.greenhouse.io/neuralink/jobs/5469305003','机器人系统可靠性、视觉/运动学与规划软件','C/C++或Rust，关键系统软件基础','机器人、视觉、运动规划','控制、ROS2和真机系统','未公布学位/2027暑期/3个月安排',season='未注明2027或暑期',degree='未指定',category='B 时间与学位待确认',status='官网实习JD可读')
add('Toyota Research Institute','Robotics Research Intern — Post-Training (Spring 2027)','186808f9-464c-4f22-9d7d-4372ef272ff0','D1','Los Altos, CA','https://jobs.lever.co/tri/186808f9-464c-4f22-9d7d-4372ef272ff0','机器人后训练、RL/IL和生成世界模型','PhD在读、PyTorch与机器人学习','DAgger、在线/离线RL','VLA后训练相关','PhD硬门槛且为春季',season='2027春季',duration='12周',degree='PhD在读',phd='必需',category='C 硬条件不符',priority='排除')
add('Zoox','Contract Student Worker — Data Mining with VLM','7206fd97-14e4-43a0-b903-ba65dfeee53e','D3','Foster City, CA','https://jobs.lever.co/zoox/7206fd97-14e4-43a0-b903-ba65dfeee53e','VLM/RAG检索、数据挖掘与生产数据管道','BS/MS；Python、PySpark/SQL','VLM数据评估','多模态研究与数据评测','官方明确不是实习；供应商雇佣；SQL/PySpark未证明',season='未注明2027',duration='至少3个月，40h/周现场',degree='BS/MS',category='C 非实习形式',kind='Contract Student Worker，非internship',priority='对照')
add('Physical Intelligence','Research Internships','f020ff1a-4b4c-4415-8434-2da5010a7076','D1','San Francisco, CA（现场）','https://jobs.ashbyhq.com/physicalintelligence/f020ff1a-4b4c-4415-8434-2da5010a7076','官网仅显示Research Internships与AI & Robotics Research部门；无具体职责','未公开','未公开','VLA/机器人研究方向相邻，仅方向判断','学位、团队、季节、时长及职责均需确认',season='未公布',degree='未公布',category='B JD信息不足',status='开放：浏览器显示实习页及申请入口',verification='浏览器现场正文',priority='P2')
add('Apptronik','IROS 2026 — Robotics & AI Talent Pool','6206626004','D1','Austin, TX / Sunnyvale, CA','https://job-boards.greenhouse.io/apptronik/jobs/6206626004','IROS人才池包含Summer 2027 internship及其他级别机会','MS/PhD及多级别人才；需后续匹配','人形机器人、学习与控制','Unitree/Dexmate/CMU组合','人才池不是已分配团队岗位',degree='MS/PhD',kind='会议人才池',category='T 人才/项目池',priority='P2')
add('Figure','Special Projects Intern — Fall 2026','4694889006','D5','San Jose, CA','https://job-boards.greenhouse.io/figureai/jobs/4694889006','机器人演示与行为序列、现场调试和跨团队系统集成','研究生MS/PhD；Python、Linux、机器人系统','实际AI/机器人演示','Dexmate现场演示高度相关','季节为Fall 2026，不能作为Summer 2027',season='2026秋季',duration='至少10周，偏好1-2学期',degree='MS/PhD',category='C 季节不符',priority='观察')
add('AMD','PhD ML Systems Research Intern — Summer 2027','90993','D3','美国','https://careers.amd.com/students/jobs/90993?lang=en-us','分布式训练、RL评估与推理系统研究','PhD在读；Python/PyTorch与ML系统','大规模训练/推理','预算匹配KV研究相邻','PhD硬门槛',duration='05-24至08-13或06-21至09-10',degree='PhD在读',phd='必需',category='C 硬条件不符',priority='排除',authorization='JD写明不支持担保',status='官方JD索引可读；动态入口待确认')
add('Alibaba','日常实习生—数据智多星—具身智能仿真方向','199904300004','D1','杭州','https://campus-talent.alibaba.com/campus/position/199904300004','3D资产生成、动作条件世界模型、VLA数据闭环评测','MS/PhD；3D生成或视频世界模型相关经验','顶会论文、物理仿真','Unitree场景复现与CMU世界模型在研','尚无已完成世界模型结果；暑期与时长待确认',country='中国',season='日常实习，非已确认2027暑期',degree='MS/PhD',graduation='2026-11-01至2030-01-01毕业',category='B 时间待确认',status='官方JD索引可读；动态入口待确认')
for title,rid,uid,d,s,req,gap,duration in [
('大模型/多模态算法实习生','J99230','f8a467f0-2a4a-4238-a21c-412408f85c2e','D3','大模型、多模态算法与训练优化','Python、PyTorch/Paddle、Transformers','最少4个月，与约3个月不符','至少4个月'),
('研究院大模型算法实习生','J95515','f4f00de1-f5a6-494d-b8e1-943ce9d94905','D3','多模态融合、大模型微调研究','编码/数据结构、机器学习','学位和实习档期/时长未明确','未公布'),
('大模型算法工程师实习生（Agent/RL）','J100640','09a5cef9-73c6-4462-995b-fe74a8450d10','D3','RL reward/环境服务及大模型工程','本科以上；PyTorch/Linux；Python/Go/Java/C++','研究内容偏LM；具体团队与暑期需核实','未公布')]:
 add('Baidu',title,rid,d,'北京/深圳（以岗位页为准）','https://talent.baidu.com/jobs/detail/INTERN/'+uid,s,req,'论文、相关研究','视觉KV、视频与agent经验；Agent/RL为相邻方向',gap,country='中国',season='日常实习；未注明2027',duration=duration,degree='本科以上' if rid=='J100640' else '所读正文未明确学位层级',category='C 时长不符' if rid=='J99230' else 'B 时间与学位待确认',priority='排除' if rid=='J99230' else 'P2',status='官网实习正文可读')
add('ByteDance Seed','Seed 2027基础模型研究实习项目','Seed-2027-program','D1','中国多地','https://seed.bytedance.com/zh/blog/bytedance-seed-2027-foundation-model-campus-recruitment-is-now-open-internships-included','基础模型研究项目，覆盖具身/视觉/ML系统；非具体组JD','实习面向2027-09及以后毕业学生','相关领域研究','2028毕业满足项目年份窗口；机器人+VLM','项目池非具体职位；不能套用ByteIntern 2027届规则',country='中国',season='2027项目/日常实习；夏季未定',degree='项目公告未逐岗限定',graduation='实习：2027-09及以后毕业',kind='研究项目池',category='T 人才/项目池',priority='P2',status='官方项目公告可读')

companies=[
('Waymo','美国',W+'search','多项2027暑期MS岗位','D3/D4/D5','已有逐岗记录；每人最多3岗建议'),
('NVIDIA','美国/中国','https://www.nvidia.com/en-us/about-nvidia/careers/','通用2027实习池、中国DevTech及PhD岗位','D1/D3','严格区分人才池与PhD研究岗'),
('Google','美国','https://www.google.com/about/careers/applications/jobs/results/131518356678156998-student-researcher-bsms-wintersummer-2027','BS/MS Winter/Summer2027项目池','D3','项目匹配，不保证机器人组'),
('Amazon','美国','https://www.amazon.jobs/en/teams/amazon-robotics','2027 Robotics多团队轨道','D4/D5','具体团队和3个月安排offer时确定'),
('Bedrock Robotics','美国','https://bedrockrobotics.com/careers','7个相关2027岗位录入','D1/D2/D3/D5','多数未写summer；世界模型实时页面已复核'),
('Johnson & Johnson','美国','https://www.careers.jnj.com/en/early-career-programs/internships/','3项2027暑期Robotics R&D','D2/D5','预计2026-10-17关闭，可延长'),
('Corning','美国','https://corningjobs.corning.com/go/Internships/7688500/','4项2027暑期视觉/控制岗位','D2/D3/D5','工业应用方向，需看PLC/赞助条件'),
('Neuralink','美国','https://job-boards.greenhouse.io/neuralink/jobs/5469305003','机器人SWE实习，季节未注明','D4/D5','需核对Summer2027和时长'),
('Toyota Research Institute','美国','https://jobs.lever.co/tri','机器人后训练Spring2027 PhD岗','D1','未找到匹配MS+Summer2027的具体研究岗'),
('Zoox','美国','https://jobs.lever.co/zoox','VLM Contract Student Worker','D3','明确不是结构化internship'),
('Apptronik','美国','https://job-boards.greenhouse.io/apptronik/jobs/6206626004','IROS人才池含Summer2027 MS/PhD','D1/D2','人才池，不计具体岗位'),
('Physical Intelligence','美国','https://jobs.ashbyhq.com/physicalintelligence/f020ff1a-4b4c-4415-8434-2da5010a7076','Research Internships入口开放，JD极简','D1','浏览器核验；未公开学位季节职责'),
('Boston Dynamics','美国','https://bostondynamics.com/careers/','有10-12周实习制度；未核到2027具体JD','D2/D5','官方招募时段说明不保证2027开放日'),
('Figure','美国','https://job-boards.greenhouse.io/figureai','Fall2026 Special Projects Intern','D1/D5','保留为未来Summer同类岗位观察'),
('Agility Robotics','美国','https://www.agilityrobotics.com/careers','未核到2027暑期MS具体岗位','D1/D2','官网检索范围有限；不等于没有岗位'),
('Intrinsic','美国','https://www.intrinsic.ai/careers','实习项目说明；未核到2027 JD','D1/D5','继续关注年初学生岗位'),
('1X','美国','https://www.1x.tech/careers','AI Residency及其他职位；未确认2027实习','D1','Residency不可直接视为三个月暑期实习'),
('Skild AI','美国','https://www.skild.ai/career','动态招聘页；未确认2027实习JD','D1','页面获取受限，保留观察'),
('Tesla','美国','https://www.tesla.com/careers/search/?query=bot','Optimus Winter/Spring2027岗位','D1/D2','不是已确认Summer2027'),
('Apple','美国','https://jobs.apple.com/en-us/search?team=Internships-STDNT-INTRN','学生招聘入口；相关2027机器人研究岗未确认','D3','检索未覆盖全部动态职位'),
('Meta','美国','https://www.metacareers.com/jobs','未核到合适2027暑期MS研究JD','D3','访问/索引有限；不宣称未开放'),
('Microsoft','美国','https://careers.microsoft.com/v2/global/en/phdinternship','PhD项目说明；未确认对应MS2027岗','D3','不要把PhD项目套用MS'),
('Qualcomm','美国','https://careers.qualcomm.com/','Summer2027 PhD兴趣池发现','D3','博士池不计MS岗位'),
('AMD','美国','https://careers.amd.com/students/jobs/90993?lang=en-us','Summer2027 PhD ML Systems Research','D3','已记录为PhD硬门槛对照'),
('Intel','美国','https://jobs.intel.com/','未核到对应2027暑期MS具体JD','D3/D5','动态入口限制；不等于无岗位'),
('Adobe','美国','https://careers.adobe.com/us/en/student','学生入口；检索见2027全职研究岗位','D3','全职毕业窗口不能当2027暑期'),
('Bosch','美国','https://www.bosch.com/careers/','机器人/VLA研究方向存在；未确认2027 JD','D1/D4','研究团队页面不是在招证明'),
('ByteDance Seed','中国','https://seed.bytedance.com/zh/seedearlycareer','2027研究实习项目；2028毕业可进入公告窗口','D1/D3','ByteIntern2027届与Seed日常实习应分开'),
('Alibaba','中国','https://campus-talent.alibaba.com/','具身仿真日常实习具体JD','D1','2028毕业在窗口内；时长/档期待核'),
('Baidu','中国','https://talent.baidu.com/','多项日常算法实习','D3','常见4/6月要求与约3个月冲突'),
('Tencent','中国','https://careers.tencent.com/zh-cn/search.html?pcid=40005','实习筛选入口可见，未核到对应2027具体岗','D1/D3','旧Robotics X报道不作为当前岗位'),
('Huawei','中国','https://career.huawei.com/cn/campus-recruitment','2027届全职校招页面','D3','2028毕业与2027届不同；实习需单独核实'),
('Meituan','中国','https://hr.meituan.com/web/campus?hiringType=4_6','日常实习列表出现具身/无人机传感器方向','D1/D4','列表发现，具体JD/最短时长未完成核验'),
('Xiaomi','中国','https://hr.xiaomi.com/website/opportunities.html','实习筛选入口；未确认具体2027岗','D1','动态列表限制'),
('JD.com','中国','https://zhaopin.jd.com/','校招入口；未确认相关2027暑期JD','D1/D5','动态/访问限制，保留观察'),
('Unitree','中国','https://www.unitree.com/position/','机器人/VLA/控制技术招聘列表','D1/D2','未把全职岗位当实习；现有经历Present需更新'),
('Agibot','中国','https://www.agibot.com/recruitment/%2A.htm','招聘入口，未确认2027具体实习JD','D1/D2','需具体团队/实习条件'),
('Galbot','中国','https://galbot.com/about/','公司/联系入口；未取得可核验实习JD','D1','公司网页不等于在招'),
('LimX Dynamics','中国','https://career.limxdynamics.com/index/m/position/7687534113214318884/detail','遥操作软件算法实习线索','D1/D2','动态JD未取得完整条件；未计岗位清单'),
('Pony.ai','中国','https://campus.pony.ai/','2027届全职及实习分流说明','D4','2027年8月后毕业学生走实习；具体组待核'),
('WeRide','中国','https://www.weride.ai/zh/careers','2027秋招公告及职位入口','D4','秋招不能等同Summer2027'),
('DeepRoute.ai','中国','https://deeproute.ai/','公司入口动态；未确认实习JD','D4','访问受限，不判定未开放'),
('DJI','中国','https://we.dji.com/zh-CN/','校园招聘入口；未核到2027暑期具体岗','D4','历史2026招聘不混入'),
('XPeng','中国','https://www.xiaopeng.com/join.html','社招/校招入口','D1/D4','未确认三个月2027暑期JD'),
('Li Auto','中国','https://www.lixiang.com/','仅取得公司入口；具体实习未核验','D1/D4','低验证深度，列观察不计岗位'),
('Midea','美国/中国','https://careers.midea.com/','UM邮箱发现Summer2027 Co-op；官网未定位同一JD','D2/D5','邮件为发现线索；具体岗位/时长仍待核')]

# Final live-page audit and additional distinct roles.
for j in jobs:
 if j['company']=='Johnson & Johnson':
  lang={'R-099654':'ja-jp','R-100027':'es-la','R-099919':'fr-ca'}[j['req_id']]
  j['source']=j['source'].replace('/en/jobs/',f'/{lang}/jobs/')
  j['kind']='Robotics R&D职能招聘轨道'
 if j['company']=='Bedrock Robotics':
  j['status']='开放：浏览器实时招聘列表';j['verification']='官方正文+浏览器实时列表';j['location']+='（现场）'
  if 'Fleet' in j['title']:j.update(category='A 学位与暑期匹配',priority='P2')
  if 'Metric Prototyping' in j['title']:
   j.update(status='已撤下：浏览器显示Job not found',category='C 已撤下',priority='排除',verification='官方旧索引+实时Job not found',deadline_note='旧索引仍存在；2026-09-29实时页面已撤下',gap=j['gap']+'；该链接已无岗位')
for title,rid,d,s,req,pref,fit,gap in [
 ('State Estimation, Learned Mapping & Semantic SLAM','8c7bad61-50e3-4702-be36-72e9b72a9760','D4','学习型SLAM、3D语义地图、真实数据与经典基线比较','BS/MS/PhD或同等；Python/PyTorch、3D变换、SLAM/点云','DINO/SAM、lidar融合、NeRF/3DGS、ROS/C++','SlideSLAM/ROS2、DINO/SAM感知、传感器标定','学习型建图/3D神经表示成果未确认'),
 ('Simulation Engineer, Neural Rendering','77759050-75f5-45ed-a3a8-35b665daaadc','D5','NeRF/3DGS真实场景合成、时序/速度及下游自治评估','BS/MS/PhD或同等；Python/PyTorch、3D图形与神经场景表示','Unity/Isaac/Unreal、CUDA、渲染研究','Unity/AirSim、PICO场景复现','NeRF/3DGS经验为实质缺口'),
 ('Safety Engineer, Agentic Safety Case Assessment','cb06dc4f-3e78-4546-897d-b39ba12a9178','D2','Lean形式化安全声明、LLM辅助证明与真实车队证据审计','Lean/mathlib、概率统计、LLM证明评估、安全机器人背景','形式化安全论证、Rust验证工具','安全研究兴趣与实机经历相邻','未证明Lean/mathlib；CBF研究不能替代形式化证明经验'),
 ('Hardware Engineer','949feb1b-c60f-43c5-94de-7dd9cd70ba4a','D5','自主硬件集成、组件验证和传感器测试自动化','所读JD未列学位硬门槛；Python/C++/C/Rust分析测试','相机/lidar/IMU/GNSS、Jetson、通信协议','GPS/lidar/IMU/camera集成与真机实验','板级/协议/Jetson深度未确认'),
 ('Sensor Hardware Test Engineer','1f413f83-b897-4938-a19e-ab91bd326c51','D5','相机/lidar台架测试、工装DAQ、现场传感器评价','动手传感器测试、数据分析及现场工作能力；学位待核','CAD、Git、机器人/控制','ASV硬件传感器与标定','DAQ/测试规范证据待补')]:
 add('Bedrock Robotics','2027 Internship — '+title,rid,d,'San Francisco, CA（现场）',B+rid,s,req,pref,fit,gap,season='2027；暑期未明确',category='B 时间与技能待确认',degree='BS/MS/PhD或同等' if 'BS/MS/PhD' in req else '所读正文未限定',status='开放：浏览器实时招聘列表',verification='浏览器正文' if rid in ['8c7bad61-50e3-4702-be36-72e9b72a9760','77759050-75f5-45ed-a3a8-35b665daaadc','cb06dc4f-3e78-4546-897d-b39ba12a9178'] else '官方正文+浏览器实时列表',priority='P2' if 'Safety Engineer' not in title else 'P3')
add('Waymo','2027 Summer Intern, BS/MS, Software Engineer','5392','D4','San Francisco, CA',W+'2027-summer-intern-bs-ms-software-engineer-san-francisco-california-united-states','聚类ML/生产行为差异并将优质ML行为移入生产','BS/MS Software Engineering；C++、数据分析','机器人/ML','真机策略部署与rollout分析','JD学科写Software Engineering，MSR是否认可相关性需确认',degree='BS/MS Software Engineering',category='B 专业范围待确认',priority='P2',deadline_type='滚动',deadline_note='填满为止；建议每人最多3岗')
add('Waymo','2027 Summer Intern, BS/MS, Software Engineering, Commercialization','5401','D5','Mountain View / San Francisco, CA',W+'2027-summer-intern-bs-ms-software-engineering-commercialization-mountain-view-california-united-states-san-francisco','车队工具/后端可靠性、调度预测与优化','BS/MS CS或相关；内部工具与基础设施兴趣','C++、分布式后端','部署基础设施与机器人软件','云/后端规模经验不足；偏商业系统',degree='BS/MS相关专业',priority='P2',deadline_type='滚动',deadline_note='填满为止；建议每人最多3岗')
add('Apple','Applied Data Solutions Program, Internships — Summer 2027','200673612-0836','D3','Cupertino及美国项目地点','https://jobs.apple.com/tr-tr/details/200673612-0836/applied-data-solutions-program-internships-summer-2027?team=STDNT','多团队数据/ML/SWE/生成AI工程，生产数据管道与模型','本科/研究生相关专业；Python等、DS/ML与软件生命周期','SQL/Spark、PyTorch、LLM','PyTorch、VLM研究与数据评测','不是专门机器人组；SQL/Spark和生产数据系统待补',kind='多团队项目',category='T 人才/项目池',degree='本科/研究生',priority='P2',status='官方项目JD可读；团队匹配另定')
add('Apple','Machine Learning and Artificial Intelligence Masters Internships','200664221-3810','D3','美国多地','https://jobs.apple.com/en-il/details/200664221-3810/machine-learning-and-artificial-intelligence-masters-internships?team=STDNT','AIML硕士实习意向入口；官方明确不是具体空缺职位','相关MS在读；实习后返校或实习为最后毕业要求','Python等面向对象编程、PyTorch/TF、数学统计、ML项目','VLM、视频和机器人研究','未注明2027暑期；通用池非具体团队',degree='MS',return_school='返校或实习为最后毕业要求',season='未注明2027/暑期',kind='通用硕士实习意向池',category='T 人才/项目池',priority='P2',status='开放：官方项目正文及持续接收意向',verification='官方正文',deadline_type='持续接收',deadline_note='官方写明ongoing；仅表达未来岗位兴趣')
company_records=[dict(company=x[0],region=x[1],source=x[2],finding=x[3],direction=x[4],next_action=x[5],checked=DATE,verification='官网入口/官方索引；详见结论') for x in companies]
for c in company_records:
 if c['company']=='Bedrock Robotics':c.update(source=B,finding='11项实习在实时列表；另1旧评测JD已撤下',next_action='除Fleet明确summer外，其余暑期/时长需确认；安全岗实质要求Lean')
 if c['company']=='Apple':c.update(finding='ADSP Summer2027项目池及AIML Masters通用入口',next_action='团队/季节分别确认，不把通用MS池当2027具体岗位')
 if c['company']=='LimX Dynamics':c.update(finding='实习历史线索；当前所查URL返回404',next_action='需从官方招聘入口重新定位；未计岗位清单')
 if c['company']=='Meituan':c.update(finding='实时日常实习列表：具身智能数据管线开发、Agent算法等',next_action='列表可读；详情跳转未完成，学位/最短时长未核，未计确认岗位',verification='浏览器实时列表（2026-09-29）')
directions=[
dict(id='D1',name='具身智能/VLA/机器人基础模型',focus='真机模型适配、数据与评测、策略和控制集成',evidence='Unitree H2/G1、GR00T/OpenPI+SONIC、8任务/24场景评测、Dexmate IROS demo',jd='Bedrock World Models；NVIDIA DevTech Robotics China',gap='大规模训练、世界模型已完成成果、PhD门槛',resume='resumes/D1_embodied/Ziyu_Xu_D1.tex',level='主方向：工程研究结合'),
dict(id='D2',name='全身控制/locomotion/安全控制',focus='学习增强控制、真机闭环、安全评估',evidence='Lie-MPC实船20%改善；CMU WBC/CBF/world model在研',jd='J&J Controls R-099654；Corning MPC/Advanced Process 78170',gap='新研究尚在进行；不可暗示CBF保证或locomotion成果',resume='resumes/D2_control/Ziyu_Xu_D2.tex',level='主方向：控制与实机证据扎实'),
dict(id='D3',name='VLM/视频理解/推理效率',focus='KV上下文重编码、预算匹配评估、视频/视觉研究',evidence='ICLR2027投稿两篇、SAM手术视觉、PyTorch',jd='Waymo Simulator Realism 5432；Bedrock ML Inference',gap='ICLR是投稿；CUDA/Rust/TPU等不能补写成既有技能',resume='resumes/D3_vlm/Ziyu_Xu_D3.tex',level='主方向：研究岗位需严查学位'),
dict(id='D4',name='自主系统/规划控制/SLAM',focus='主动SLAM、通信约束探索、传感器与闭环自治',evidence='Unity/AirSim、ROS1到ROS2、EXP3与实船感知',jd='Waymo Road Understanding 5452；Maneuvering Tech 5411',gap='自动驾驶道路/BEV、生产C++深度待证明',resume='resumes/D4_autonomy/Ziyu_Xu_D4.tex',level='相邻强方向'),
dict(id='D5',name='机器人软件/仿真/数据与评测系统',focus='可复现部署、日志、仿真、系统测试与标定',evidence='跨平台策略基础设施、PICO 2.5cm、传感器集成和现场demo',jd='Waymo Behavior Test 5361；J&J Systems/Simulation R-100027',gap='SQL/云/CI与工业质量经验逐岗判断',resume='resumes/D5_systems/Ziyu_Xu_D5.tex',level='覆盖面最广的工程方向')]
out=Path('sources/research_data.json');out.write_text(json.dumps(dict(checked=DATE,jobs=jobs,companies=company_records,directions=directions),ensure_ascii=False,indent=2))
print(json.dumps({'jobs':len(jobs),'companies':len(companies),'categories':{c:sum(j['category']==c for j in jobs) for c in sorted(set(j['category'] for j in jobs))}},ensure_ascii=False))
