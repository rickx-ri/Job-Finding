# D2 简历修改说明

对照 J&J Controls R-099654 与 Corning 78170：优先控制建模、系统辨识、闭环实验与安全研究。

基线：resumes/original/CMU_Ziyu_original.tex。以下列出各语义块的完整旧文/新文；红线PDF另覆盖全部可提取文字变化。调整经历顺序只表示相关性，不改变时间。

## 共同新增与日期

原文：CMU Aug. 2026；未包含CMU实验室经历。

改文：CMU Aug. 2026 – Expected 2028；新增 Graduate Student Researcher (Aug. 2026 – Present)。

Intelligent Control Lab, Carnegie Mellon University Aug. 2026 -- Present Graduate Student Researcher, advised by Prof. Changliu Liu Pittsburgh, PA Whole-Body and Safe Locomotion Research (ongoing): Investigating whole-body control, safety with control barrier functions (CBFs), and world-model-based locomotion. Dexmate Bimanual Manipulation Demo, IROS 2026: Contributed to a bimanual block-stacking demonstration combining agent planning with policy execution. Implemented the agent component, prepared the on-site environment, adapted the system to different grippers, and performed system calibration.

原因：用户提供事实；中性头衔；ongoing不冒充完成；IROS demo只写确认过的个人贡献。

## 研究兴趣

原文：Robot Foundation Models, Real-World Policy Adaptation, and Learning-Augmented Control

改文：Learning-Augmented Control, Whole-Body Control, and Safe Locomotion

原因：对照 J&J Controls R-099654 与 Corning 78170：优先控制建模、系统辨识、闭环实验与安全研究。

## unitree

原文：Unitree Robotics, R&D Department, Embodied AI Team May 2026 -- Present Research Intern, Humanoid Robot Foundation Models Hangzhou, China Closed-Loop Real-Robot Infrastructure for Humanoid Foundation-Model Policies: Built and validated an end-to-end policy infrastructure on Unitree H2/G1 humanoids, integrating teleoperation data collection, VLA/WAM and whole-body policy adapters, rollout logging and evaluation, controller interfaces, and policy fine-tuning. Enabled launch with one command and closed-loop rollouts across platforms, allowing policies and controllers to be integrated without modifying platform-specific launch workflows. Embodiment VLA Adaptation & Post-Training: Conducted a structured survey of representative robot VLA, WAM, and physical-AI policies, especially work from NVIDIA GEAR Lab. Deployed and fine-tuned Isaac GR00T/OpenPI VLA policies with SONIC whole-body control on Unitree humanoids using real-robot rollout traces. Currently developing a phase-aware adaptation method that aligns semantic task progress and execution timing across embodiments for policy transfer and rollout-driven post-training. Reproducible Real-World VLA Benchmark for Humanoid Manipulation: Implemented an 8-task, 24-scene benchmark with green-screen background replacement to evaluate foundation models under varied visual conditions. Built a PICO-based scene-digitization and AR-guided reconstruction pipeline that captured shelf-object layouts as reusable digital scene templates, and registered target placements back into the physical workspace, achieving 2.5 cm median placement error.

改文：Unitree Robotics, R&D Department, Embodied AI Team May 2026 -- Present Research Intern, Humanoid Robot Foundation Models Hangzhou, China Real-Robot Policy Infrastructure: Built and validated a closed-loop stack on Unitree H2/G1 humanoids integrating teleoperation, VLA/WAM and whole-body policy adapters, rollout logging, evaluation, controller interfaces, and policy fine-tuning; enabled one-command launches across platforms. VLA Adaptation and Post-Training: Deployed and fine-tuned Isaac GR00T/OpenPI policies with SONIC whole-body control using real-robot rollout traces. Developing phase-aware adaptation across embodiments by aligning semantic task progress and execution timing.

原因：压缩冗长描述并按目标JD突出已存在的事实；不增加技能、数字或领导职责。

## shanghai

原文：Shanghai Artificial Intelligence Lab & IRMV, SJTU Apr. 2026 -- Present Research Assistant, Directed by Prof. Junchi Yan and Prof. Hesheng Wang Shanghai, China Context-Aware Re-encoding for Iterative Visual KV Compression: Identified representation errors caused by reusing retained visual KV entries after their spatial neighbors are removed, and showed that these errors compound across repeated compression in multi-turn and streaming inference. Developed a re-encoding method that recomputes each retained set in its new context at the original positions, and benchmarked it against inheritance and restoration methods under matched memory and runtime budgets.

改文：Shanghai Artificial Intelligence Lab & IRMV, SJTU Apr. 2026 -- Present Research Assistant, Directed by Prof. Junchi Yan and Prof. Hesheng Wang Shanghai, China Iterative Visual KV Compression: Studied errors from reusing retained visual KV entries after neighboring tokens are removed in multi-turn and streaming inference. Developed context-aware re-encoding at original positions and compared with inheritance and restoration under matched memory and runtime budgets.

原因：压缩冗长描述并按目标JD突出已存在的事实；不增加技能、数字或领导职责。

## asv

原文：Computational Autonomy and Robotics Lab, UM Jun. 2025 -- Apr. 2026 Research Assistant, Directed by Prof. Maani Ghaffari Ann Arbor, MI Online Learning Lie-MPC for Robust ASV Control: Developed a Neural-Fly-inspired learning-augmented Lie-MPC framework for an autonomous surface vehicle, estimating residual wind/current disturbances online and injecting learned dynamics corrections into the controller for robust trajectory tracking under hydrodynamic uncertainty. Implemented and evaluated the framework on a real ASV, achieved a 20% improvement in trajectory-tracking performance over the baseline MPC controller during field experiments. Field Perception for Aquatic Vegetation Tracking: Built a water-scene perception pipeline for autonomous surface vehicles, combining DINO/SAM2-based segmentation with Grounded-DINO and YOLO fine-tuning to detect submerged vegetation and provide perception signals for navigation and autonomy experiments. ASV Hardware and Sensor Integration for Closed-Loop Field Autonomy: Designed sensor mounts and integrated GPS, lidar, IMU, and camera systems on an autonomous surface vehicle. Aligned and calibrated sensors to support field data collection and control experiments.

改文：Computational Autonomy and Robotics Lab, UM Jun. 2025 -- Apr. 2026 Research Assistant, Directed by Prof. Maani Ghaffari Ann Arbor, MI Learning-Augmented Lie-MPC: Developed and field-tested an autonomous surface vehicle controller that estimates residual wind/current disturbances online and corrects the dynamics used by MPC. Achieved a 20% improvement in trajectory-tracking performance over baseline MPC in real-ASV experiments. Sensor Integration: Designed mounts and integrated, aligned, and calibrated GPS, lidar, IMU, and cameras for field data collection and closed-loop control.

原因：压缩冗长描述并按目标JD突出已存在的事实；不增加技能、数字或领导职责。

## autonomy

原文：Intelligent Robotics and Autonomy Lab , UM Oct. 2024 -- Apr. 2026 Research Assistant, Directed by Prof. Vasileios Tzoumas Ann Arbor, MI Multi-Robot Active-SLAM Simulation & ROS2 Integration: Rebuilt a Unity + AirSim multi-drone simulation testbed with redesigned vehicle dynamics and sensing modules, then migrated SlideSLAM communication logics from ROS1 to ROS2 by refactoring topic interfaces and workflows for bandwidth-limited active-SLAM evaluation. Resource-Aware Multi-Robot Exploration Algorithms: Developed distributed exploration EXP3-style algorithms for bandwidth-limited robot teams, formulating communication-aware action selection with submodular objectives and bandit feedback in simulation to balance map coverage and communication cost.

改文：Intelligent Robotics and Autonomy Lab , UM Oct. 2024 -- Apr. 2026 Research Assistant, Directed by Prof. Vasileios Tzoumas Ann Arbor, MI Multi-Robot Simulation and ROS2: Rebuilt a Unity + AirSim multi-drone testbed with revised dynamics and sensing; migrated SlideSLAM communication from ROS1 to ROS2 for bandwidth-limited active-SLAM evaluation. Communication-Aware Exploration: Developed distributed EXP3-style algorithms using submodular objectives and bandit feedback to balance map coverage and communication cost in simulation.

原因：压缩冗长描述并按目标JD突出已存在的事实；不增加技能、数字或领导职责。

## surgical

原文：Surgical Computer Vision Detection, SJTU Apr. 2024 -- Dec. 2024 Research Assistant, Directed by Prof. Yutong Ban Shanghai, China Foundation Segmentation Model Evaluation for Surgical Video: Evaluated Segment Anything Model variants on surgical video frames, analyzing domain shift and temporal mask stability around instruments, tissues, and tool-tissue interaction regions.

改文：本定向版删除此经历；总简历保留。

原因：为两页限制和方向相关性让出空间。

## 论文、奖项与技能

原文论文：Xiaohan Wang*, Ziyu Xu*, Xuyi Yang. ``Re-encoding What You Keep After Every Compression: Retained Visual KV Is Computed in a Context That No Longer Exists'', Submitted to ICLR 2027. *Equal contribution. Xuyi Yang, Xiaohan Wang, Wenhao Zhang, and Ziyu Xu. ``StreamJIT: Continuous Observation and Just-in-Time Deliberation for Proactive Streaming Video Assistants'', Submitted to ICLR 2027. Yinan Dong, Ziyu Xu, Tsimafei Lazouski, Sangli Teng, and Maani Ghaffari. ``Online Learning-Enhanced Lie Algebraic MPC for Robust Autonomous Surface Vehicle Control'', IEEE Robotics and Automation Letters (RA-L), revised manuscript under review, 2025. C. Yuan, J. Jiang, K. Yang, Z. Xu, ..., and Y. Ban. ``Systematic Evaluation and Guidelines for Segment Anything Model in Surgical Video Analysis'', npj Digital Surgery, accepted, 2024.

改文论文：Yinan Dong, Ziyu Xu, Tsimafei Lazouski, Sangli Teng, and Maani Ghaffari. ``Online Learning-Enhanced Lie Algebraic MPC for Robust Autonomous Surface Vehicle Control'', IEEE Robotics and Automation Letters (RA-L), revised manuscript under review, 2025. Xiaohan Wang*, Ziyu Xu*, Xuyi Yang. ``Re-encoding What You Keep After Every Compression: Retained Visual KV Is Computed in a Context That No Longer Exists'', Submitted to ICLR 2027. *Equal contribution. Xuyi Yang, Xiaohan Wang, Wenhao Zhang, and Ziyu Xu. ``StreamJIT: Continuous Observation and Just-in-Time Deliberation for Proactive Streaming Video Assistants'', Submitted to ICLR 2027. C. Yuan, J. Jiang, K. Yang, Z. Xu, ..., and Y. Ban. ``Systematic Evaluation and Guidelines for Segment Anything Model in Surgical Video Analysis'', npj Digital Surgery, accepted, 2024.

原因：按相关性调整论文顺序，完整保留作者、标题和投稿/审稿/接收状态。

原文奖项：Gold Medal in 2023 University Physics Competition, by American Physical Society & American Astronomical Society (top 1%) Third place in 2023 RoboMaster Campus Competition (top 10%) Dean's Honor List, University of Michigan College of Engineering (2024, 2025) M Prize in 2024 Mathematical Contest in Modeling (top 13%)

改文奖项：Gold Medal, University Physics Competition (2023); Dean's Honor List, University of Michigan (2024, 2025).

原因：压缩次要荣誉，不改变奖项层级；其余留在总简历。

原文技能：Robot Learning & Control: VLA post-training, humanoid foundation models, whole-body policy, RL, real-robot policy deployment, teleoperation/data collection, MPC, sim-to-real Perception & Multimodal ML: PyTorch, OpenCV, SAM2, Grounded-DINO, YOLO, DINO features, visual token compression, spatial grounding, LLMs fine-tuning Systems & Tools: ROS/ROS2, Python/C++, Unity + AirSim, Docker, Linux, Git, sensor integration, CAD, FEA, Manufacturing, embedded system

改文技能：Control and Autonomy: MPC, learning-augmented control, RL, whole-body policy integration, real-robot experiments, sensor calibration Tools: Python/C++, ROS/ROS2, PyTorch, Unity + AirSim, Linux, Git, CAD, sensor integration

原因：只重排和筛选已有技能，不填入JD出现但简历未证明的SQL/CUDA/Rust/TPU/PLC等。

## 版式

沿用原11pt Charter、0.65英寸边距、章节线与经历格式。前三段研究经历后明确分页，第二页增加续页标识，避免仅少量文字溢出到第二页。论文减少人为换行；红线文档为完整文本审阅版，不受两页限制。

## 代表JD与适配边界

以下为官网要求摘要；关键词匹配不代表满足所有资格，未证明的能力保留为缺口。

[Johnson & Johnson / R-099654](https://www.careers.jnj.com/ja-jp/jobs/r-099654/robotics-controls-autonomy-intern-robotics-rd/)：Robotics Controls & Autonomy Intern — Robotics R&D。要求：相关BS/研究生在读；GPA≥3.0、C++/控制。现有证据：Lie-MPC实船20%改善、CMU安全研究。缺口：医疗器械实时标准；JD授权条件须单独核对。

[Corning / 78170](https://corningjobs.corning.com/job/Painted-Post-Intern,-Advanced-Process-Controls-Summer-2027-NY-14870/1432275700/)：Intern, Advanced Process Controls — Summer 2027。要求：BS/MS/PhD；控制/动态系统/统计基础；Python或MATLAB。现有证据：Lie-MPC、在线扰动学习、凸优化课程。缺口：制造过程知识需学习。
