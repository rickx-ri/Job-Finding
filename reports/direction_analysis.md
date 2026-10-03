# 方向分析与岗位筛选

核验日：2026-09-29。以CMU MSR、预计2028毕业、约三个月、美国优先为筛选基线。主方向建议是D1具身/VLA、D2学习控制、D3多模态；同时保留D4自主系统和D5机器人系统工程以扩大有效机会。这个排序来自既有证据与本轮JD要求，不代表录用概率。

## D1 具身智能/VLA/机器人基础模型

VLA把视觉/语言观测映射为动作；世界模型预测动作或状态变化后的环境。简历中最强证据是把模型接入真实机器人并建立数据与评测链路。CMU世界模型课题仍是ongoing；不要把它写成已训练完成的算法贡献。

简历证据：Unitree H2/G1、GR00T/OpenPI+SONIC、8任务/24场景评测、Dexmate IROS demo。对应版本：D1。

代表JD：[Bedrock Robotics / c51d682e-58ee-44de-886f-4cfacb56d2e1](https://jobs.ashbyhq.com/bedrock-robotics/c51d682e-58ee-44de-886f-4cfacb56d2e1)。真实车队世界模型训练、消融与控制连接。学位/时间：BS/MS/PhD或同等经验；2027；暑期未明确。主要差距：世界模型研究进行中；不得声称已完成成果。

代表JD：[NVIDIA / JR2024054](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/China-Shanghai/AI-Developer-Technology-Intern--Robotics---2027_JR2024054-1)。机器人基础模型训练/推理、VLA与世界模型技术优化。学位/时间：MS/PhD；2027，季节未写明。主要差距：CUDA/大规模训练未确认；暑期与3个月需确认。

## D2 全身控制/locomotion/安全控制

CBF是用于表达安全集合约束的控制方法；用户未提供完成的CBF系统或保证，因此仅写研究方向。Lie-MPC的真实ASV实验提供更成熟的控制证据。安全岗位可能要求形式化证明，与CBF并不是同一技能。

简历证据：Lie-MPC实船20%改善；CMU WBC/CBF/world model在研。对应版本：D2。

代表JD：[Johnson & Johnson / R-099654](https://www.careers.jnj.com/ja-jp/jobs/r-099654/robotics-controls-autonomy-intern-robotics-rd/)。运动学、控制/自主算法及实时软件验证。学位/时间：本科/硕士/博士；2027暑期。主要差距：医疗器械实时标准；JD授权条件须单独核对。

代表JD：[Corning / 78170](https://corningjobs.corning.com/job/Painted-Post-Intern,-Advanced-Process-Controls-Summer-2027-NY-14870/1432275700/)。模型控制、系统辨识、优化、故障监测。学位/时间：BS/MS/PhD；2027暑期。主要差距：制造过程知识需学习。

## D3 VLM/视频理解/推理效率

视觉KV压缩与流式视频工作支持多模态研究和推理效率方向。论文仍为ICLR投稿；它不能自动满足“强发表记录”门槛。边端推理岗位常额外要求CUDA/Rust/GPU体系结构，这些未写入简历已有技能。

简历证据：ICLR2027投稿两篇、SAM手术视觉、PyTorch。对应版本：D3。

代表JD：[Waymo / 5432](https://careers.withwaymo.com/jobs/2027-summer-intern-ms-phd-machine-learning-engineer-simulator-realism-evaluation-san-francisco-california-united-states)。用ML判别器和统计实验评估仿真真实性。学位/时间：MS/PhD；2027暑期。主要差距：缺仿真真实性判别器成果。

代表JD：[Bedrock Robotics / 0331551e-c18e-428a-8e91-e6cb25c9c2e8](https://jobs.ashbyhq.com/bedrock-robotics/0331551e-c18e-428a-8e91-e6cb25c9c2e8)。LLM/VLA边端集成、确定性延迟与推理优化。学位/时间：BS/MS/PhD或同等经验；2027；暑期未明确。主要差距：CUDA/Rust/推理kernel性能证据不足。

## D4 自主系统/规划控制/SLAM

把多机器人探索、主动SLAM与实船感知控制作为整体自主系统证据。机器人仿真迁移和传感器标定与地图/定位岗位相连，但不等于已经做过道路BEV、神经建图或量产自动驾驶。

简历证据：Unity/AirSim、ROS1到ROS2、EXP3与实船感知。对应版本：D4。

代表JD：[Waymo / 5452](https://careers.withwaymo.com/jobs/2027-summer-intern-ms-phd-road-understanding-ml-engineer-mountain-view-california-united-states)。道路几何/拓扑建模及感知训练评测。学位/时间：MS/PhD；2027暑期。主要差距：缺道路建图/BEV项目证据。

代表JD：[Bedrock Robotics / 8c7bad61-50e3-4702-be36-72e9b72a9760](https://jobs.ashbyhq.com/bedrock-robotics/8c7bad61-50e3-4702-be36-72e9b72a9760)。学习型SLAM、3D语义地图、真实数据与经典基线比较。学位/时间：BS/MS/PhD或同等；2027；暑期未明确。主要差距：学习型建图/3D神经表示成果未确认。

## D5 机器人软件/仿真/数据与评测系统

这一方向强调系统能否复现、测试、排查问题并稳定运行。跨平台launch、真实rollout、场景复现和现场演示都是直接证据。云后端、SQL、CI/CD与全栈界面要求要逐岗看，不能由“会Python”推定全部满足。

简历证据：跨平台策略基础设施、PICO 2.5cm、传感器集成和现场demo。对应版本：D5。

代表JD：[Waymo / 5361](https://careers.withwaymo.com/jobs/2027-summer-intern-ms-software-engineering-behavior-test-san-francisco-california-united-states)。异常/故障与远程辅助行为验证，指标和分析工具。学位/时间：MS；2027暑期。主要差距：故障注入和SQL需补作品证据。

代表JD：[Johnson & Johnson / R-100027](https://www.careers.jnj.com/es-la/jobs/r-100027/systems-simulation-engineering-intern-robotics-rd/)。系统建模、仿真、需求追溯、实验相关性验证。学位/时间：本科/硕士/博士；2027暑期。主要差距：SysML/JAMA/DOORS等未证明。
