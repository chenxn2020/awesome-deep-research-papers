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
完成全文审核，并通过合并 Draft PR 正式进入仓库的论文。
_Avoid_: 候选论文、自动入选论文

**Review Run**:
一次定时或手动触发的候选发现、筛选和精读周期。
_Avoid_: 同步、全量爬取

**Track**:
一个由 Seed Paper 定义的研究方向。本仓库首版包含 Data Synthesis、Rubric RL 和 Harness RSI 三个主方向；论文可以有多个标签，但只保留一个主方向。
_Avoid_: 互斥分类、重复收录

**Harness RSI**:
Harness 的 recursive self-improvement：训练或执行经验触发对 prompt、tools、skills、workflow、retrieval 或 agent scaffold 的验证后更新。
_Avoid_: 静态工具框架、只增加工具数量
