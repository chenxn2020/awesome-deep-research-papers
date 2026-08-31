# Review Process

## 1. Discover

每次运行先读取 `seed_papers.md`，提取三个 Track 的 Seed、关键词和研究缺口，然后检查：

1. arXiv 最近 30 天的相关提交；
2. Hugging Face Daily Papers；
3. Seed 的 related work、references 和 citing papers；
4. 候选论文的项目主页、代码仓库和数据集页面。

保留唯一 arXiv ID，排除已收录论文和明显重复版本。候选清单最多 30 篇。

## 2. Screen

对每篇候选记录：主 Track、辅助标签、与 Seed 的具体连接、是否处理 Deep Research、多模态相关性、是否有可验证实验、主要机构和提交日期。

优先级：

- 直接研究 Deep Research 数据、Rubric RL 或 Harness RSI；
- 方法能迁移到附件输入或图文交错输出；
- 明确暴露 criterion-level、evidence-chain 或 harness-evolution 机制；
- 有公开实验、代码、数据或可复现实验设置。

排除普通 VQA、通用图文增强、静态 Agent 工具框架、只在标题中提及 agent 但没有方法贡献的论文。

## 3. Read

最多选择 5 篇全文。每篇页面必须包含：

- 标题、arXiv ID、版本、提交/更新日期、作者、主要机构；
- 一句话结论；
- 问题定义和方法拆解；
- 实验设置、关键结果和证据强度；
- 与 Seed 的关系、可迁移启示、局限与待核对项；
- 原文、代码、数据集和项目主页链接（如有）。

笔记使用中文；论文原标题和技术术语保留英文。不要把摘要中的推断写成论文明确结论；无法从原文确认的内容标为“待核对”。

## 4. Publish

新页面写入 `papers/<主方向>/<arxiv-id>.md`。README 只列一次；多方向论文用辅助标签表示。运行结束后执行本地 Markdown/链接检查，只有存在合格新论文时才创建 Draft PR。
