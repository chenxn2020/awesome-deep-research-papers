# Review Process

## 1. Discover

每次运行先读取 `seed_papers.md`，提取各论文 Track 的 Seed、关键词和研究缺口，然后检查：

1. arXiv 最近 30 天的相关提交；
2. Hugging Face Daily Papers；
3. Seed 的 related work、references 和 citing papers；
4. 候选论文的项目主页、代码仓库和数据集页面。
5. Anthropic、OpenAI 等前沿公司的官方博客；博客只接受官方域名原文。

保留唯一 arXiv ID，排除已收录论文和明显重复版本。候选清单最多 30 篇。

## 2. Screen

对每篇候选记录：主 Track、辅助标签、与 Seed 的具体连接、是否处理 Deep Research、多模态相关性、是否有可验证实验、主要机构和提交日期。

优先级：

- 直接研究 Deep Research 数据、Rubric RL、Credit Assignment 或 Harness RSI；
- 方法能迁移到附件输入或图文交错输出；
- 明确暴露 criterion-level、evidence-chain 或 harness-evolution 机制；
- 有公开实验、代码、数据或可复现实验设置。

排除普通 VQA、通用图文增强、视频/音频/纯文本 Deep Research 数据集、静态 Agent 工具框架、只在标题中提及 agent 但没有方法贡献的论文，以及非官方博客转载。

## 3. Read

每个论文 Track 每次最多新增 3 篇，允许为 0 篇。官方博客没有合格的 Anthropic、OpenAI 等官方原文时允许不更新。每篇论文页面必须包含：

- 标题、arXiv ID、版本、提交/更新日期、作者、主要机构；
- 一句话结论；
- 问题定义和方法拆解；
- 实验设置、关键结果和证据强度；
- 与 Seed 的关系、可迁移启示、局限与待核对项；
- 原文、代码、数据集和项目主页链接（如有）。

每篇必须补充“实验结果总结”，明确训练/评测模型、Benchmark/数据、对比基线、指标和主要结果；正文没有给出精确数字时标为“待核对”。不添加架构图章节。

笔记使用中文；论文原标题和技术术语保留英文。不要把摘要中的推断写成论文明确结论；无法从原文确认的内容标为“待核对”。

## 4. Publish

新页面写入 `papers/<主方向>/<arxiv-id>.md`，博客写入 `blogs/`。README 只列一次；多方向论文用辅助标签表示。运行结束后执行本地 Markdown/链接检查，只有存在合格新内容时才直接提交 `main`，并在 GitHub Issue 中记录本次运行结果；不创建 PR。
