# Codex Scheduled Task

本文件是桌面 Codex Scheduled Task 的持久化提示词。Codex 桌面任务可以在本地项目或独立 worktree 中运行；运行时 Mac 需开机且 ChatGPT/Codex App 保持运行。

## 建议配置

- 频率：每周一、周四 09:00
- 时区：`Asia/Shanghai`
- 项目：本仓库
- 工作区：独立 Git worktree
- 模型：使用 Codex 默认模型和现有额度
- 首次运行：Seed 补齐后手动 Run now

## 任务提示词

```text
你在本地 Git worktree 中维护 awesome-deep-research-papers。先读取 README.md、CONTEXT.md、PROCESS.md 和 seed_papers.md。

目标：收录与三个 Seed Track 高度相关、值得精读的论文：Data Synthesis、Rubric RL、Harness RSI。不要把 OpenQA 当作传统开放域问答。

本次 Review Run：
1. 从 arXiv 最近 30 天、Hugging Face Daily Papers、每个 Seed 的 related work/references/citing papers 中发现候选；必要时查看论文项目页、代码和数据集页。
2. 去重后最多保留 30 篇摘要候选。按 Seed 相似性和 PROCESS.md 的标准筛选，最多精读 5 篇全文。
3. 每篇精读页面记录标题、arXiv ID、版本、提交/更新日期、作者、主要机构、主 Track、辅助标签、中文精读笔记、证据强度、局限和所有外部链接。不要下载或提交 PDF。
4. 将新论文写入 papers/<track>/<arxiv-id>.md；README 只列一次。论文可多标签，但只能有一个主 Track。
5. 运行本地检查：Markdown 文件存在、arXiv ID 唯一、日期和主要机构非空、链接可解析。没有合格新论文时不创建 PR。
6. 有合格新论文时提交清晰的 commit，并创建 Draft PR；不要自动合并。PR 描述列出候选数、全文数、收录数、每篇主 Track 和排除原因摘要。

停止条件：超过 30 篇摘要、5 篇全文或 5 篇收录候选时立即停止；缺少某个 Track 的 Seed 时暂停该 Track，但继续处理有 Seed 的 Track。遇到无法确认的机构、日期、实验数字或引用关系，标记“待核对”，不要猜测。
``` 

## 手动运行前检查

1. 先在普通 Codex 对话中测试上面的提示词。
2. 检查生成页面是否包含“主要机构”和“日期”。
3. 检查 Draft PR，不满意就关闭 PR 并修改提示词或 Seed。
