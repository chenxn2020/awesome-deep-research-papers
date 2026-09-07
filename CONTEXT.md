# Deep Research Paper Curation

本文档定义论文发现、筛选和精读时使用的核心术语。实现细节不在此记录。

## Language

**Deep Research**:
一种需要搜集外部证据并综合生成答案的开放式研究任务；本项目特别关注接受附件输入或要求图文交错输出的多模态场景。
_Avoid_: 开放域问答（Open-domain Question Answering）、通用问答

**Seed Paper**:
由用户选定的正向样例，用于界定某一研究方向的主题边界，并作为相关性判断的依据。
_Avoid_: 候选论文、推荐论文

**Candidate Paper**:
从外部来源发现、但尚未完成全文审核和入库确认的论文。
_Avoid_: 已收录论文、推荐论文

**Curated Paper**:
完成全文审核，并通过用户确认后正式进入仓库的论文。
_Avoid_: 候选论文、自动入选论文

**Review Run**:
一次定时或手动触发的候选发现、筛选和精读周期。
_Avoid_: 同步、全量爬取

**Track**:
一个由 Seed Paper 定义的研究方向。本仓库包含 Data Synthesis、Rubric RL、Credit Assignment 和 Harness RSI 四个论文方向；论文可以有多个标签，但只保留一个主方向。
_Avoid_: 互斥分类、重复收录

**Harness RSI**:
Harness 的 recursive self-improvement：训练或执行经验触发对 prompt、tools、skills、workflow、retrieval 或 agent scaffold 的验证后更新。
_Avoid_: 静态工具框架、只增加工具数量

**Credit Assignment**:
Agent RL 中把最终任务结果分解、归因到步骤、工具调用、token 或子目标的训练信号设计；重点关注多轮搜索/研究任务中的稀疏奖励和错误定位。
_Avoid_: 只有通用 RL 理论、没有 agent 轨迹或任务级归因机制的工作

**Official Lab Blog**:
Anthropic、OpenAI 等前沿 AI 公司的官方博客文章，且内容直接解释 Deep Research、Agent RL、Rubric、Harness 或相关评测。
_Avoid_: 个人博客、媒体转载、无原始出处的二手解读

**Multimodal Deep Research Dataset**:
服务于图文输入、图文证据检索或图文交错研究报告生成的数据集/Benchmark。
_Avoid_: 视频、音频、纯文本 Deep Research 数据集，以及普通 VQA 或通用图文数据集
