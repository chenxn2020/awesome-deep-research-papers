# Awesome Deep Research Papers

面向 Deep Research，尤其是多模态 Deep Research 的高相关、偏精读论文库。

## 研究方向

- [Data Synthesis](papers/data-synthesis/)：附件输入、证据链和图文交错报告的数据与评测构造。
- [Rubric RL](papers/rubric-rl/)：Rubric 的自演进、优化，以及 criterion-level 信号在 RL 中的保留。
- [Harness RSI](papers/harness-rsi/)：Harness/skill 从训练和执行经验中持续演进。

## 当前 Seed

Seed 清单见 [`seed_papers.md`](seed_papers.md)。首批精读页面已经按 arXiv ID 建立在 `papers/` 下；日期和主要机构均记录在每篇页面的元数据中。

### Seed 精读索引

#### Rubric RL

| 论文 | 日期 | 主要机构 |
| --- | --- | --- |
| [Open Rubric System](papers/rubric-rl/2602.14069.md) | 2026-02-15 | Alibaba；中国科学院计算技术研究所；北京邮电大学 |
| [Rubric Dropout](papers/rubric-rl/2608.11669.md) | 2026-08-12 | Scale AI；University of Arizona；UT Dallas |
| [GDPO](papers/rubric-rl/2601.05242.md) | 2026-01-08 | NVIDIA；HKUST |
| [CriPO](papers/rubric-rl/2607.18082.md) | 2026-07-20 | Zhejiang University；ByteDance |

#### Data Synthesis

| 论文 | 日期 | 主要机构 |
| --- | --- | --- |
| [TVIR](papers/data-synthesis/2606.02320.md) | 2026-06-01 | Nanjing University；Alibaba Group |
| [MMDeepResearch-Bench](papers/data-synthesis/2601.12346.md) | 2026-01-18 | Ohio State University；Amazon；多所高校 |
| [MiroEval](papers/data-synthesis/2603.28407.md) | 2026-03-30 | MiroMind AI |
| [HiEviDR-Bench](papers/data-synthesis/2607.25151.md) | 2026-07-27 | Tsinghua University；中科院；Northeastern University；Shanghai Jiao Tong University |
| [FinanceHarness](papers/data-synthesis/2607.27853.md) | 2026-07-30 | Google Cloud AI Research；UCLA |
| [FrontierScience](papers/data-synthesis/2601.21165.md) | 2026-01-29 | OpenAI |

#### Harness RSI

| 论文 | 日期 | 主要机构 |
| --- | --- | --- |
| [EvoTrainer](papers/harness-rsi/2606.03108.md) | 2026-06-02 | Alibaba Group；中科院；SUAT |
| [Recuris](papers/harness-rsi/2608.24876.md) | 2026-08-25 | NUS；Princeton；Stanford；Oxford |
| [EvoHarness-RL](papers/harness-rsi/2608.05446.md) | 2026-08-05 | Meta AI；UIUC |

## 收录标准

论文必须能直接帮助理解上述方向之一，并通过 Seed 相似性、相关工作、引用链或 Hugging Face Daily Papers 发现。候选先进入 Draft PR；用户合并后才算正式收录。

每次 Review Run 最多审核 30 篇摘要、精读 5 篇全文，最终收录 0–5 篇。没有合格论文时不创建 PR。仓库只保存 Markdown 和外部论文链接，不保存 PDF。

## 自动运行

按 [`AUTOMATION.md`](AUTOMATION.md) 在 Codex 桌面端创建每周一、周四 09:00（Asia/Shanghai）的 Scheduled Task。任务使用独立 Git worktree，先本地检查，再创建 Draft PR；用户负责最终合并。

## 目录

```text
papers/<track>/<arxiv-id>.md  精读页面
seed_papers.md                用户维护的 Seed
PROCESS.md                    审核与写作协议
AUTOMATION.md                 Scheduled Task 提示词与运行说明
paper-template.md             新论文模板
scripts/check_repo.py         本地元数据与链接格式检查
```

## 许可与来源

论文版权归原作者和发布平台所有。本仓库仅保存短摘要、分析笔记、元数据和原文链接；引用时以 arXiv、项目主页和官方代码仓库为准。
