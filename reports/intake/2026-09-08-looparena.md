# LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering

- **arXiv**: [2608.28281](https://arxiv.org/abs/2608.28281)
- **版本**: v1
- **提交日期**: 2026-08-28（12:44:54 UTC）
- **最后更新**: 2026-08-28（目前仅 v1）
- **作者**: Yi Wang；Haopeng Zhang；Chengxiang Huang；Rui Dai；Kaikui Liu；Piotr Koniusz；Xiangxiang Chu
- **主要机构**: DreamX Team, Alibaba Group；Beijing University of Posts and Telecommunications；UNSW Sydney；Data61, CSIRO。机构按论文 HTML 首页列示，逐作者机构映射未从该页可靠解析。
- **建议模块**: `Others`
- **辅助标签**: `loop-engineering`、`controller-evaluation`、`coding-agents`、`long-horizon`、`benchmark`
- **阅读状态**: 手动提交全文精读；已读 arXiv HTML 正文 §1–8、附录 §9–17，并交叉核对官方协议、发布结果与相关源码。
- **收录状态**: **待确认收录**
- **拟写入路径**: `others/looparena.md`
- **原文许可**: CC BY 4.0；代码与文档为 Apache-2.0，上游任务材料保留各自许可。

元数据依据：[arXiv 摘要与版本历史](https://arxiv.org/abs/2608.28281)、[论文 HTML 首页](https://arxiv.org/html/2608.28281v1)、[官方仓库许可说明](https://github.com/AMAP-ML/LoopArena)。

## 手动收录记录

- **收到日期**: 2026-09-08（Asia/Shanghai）
- **入口**: Dukou 导入的 nxc 联系人聊天记录；本次 ZIP 仅含一条文本链接记录。
- **聊天记录时间**: 2026-09-07 14:07（导出文本中的时间，未另行转换时区）。
- **发现来源**: 微信公众号「智猩猩 AI」，依据用户提供的微信分享卡片截图；导出 TXT 本身只有 nxc、时间、标题与 URL，没有公众号署名。
- **推送标题**: 阿里开源LoopArena，比拼五大模型Loop Engineering能力！海外博主直呼「太需要了」
- **完整推送 URL**: [微信原始分享链接](https://mp.weixin.qq.com/s?__biz=MjM5ODExNDA2MA==&mid=2450014664&idx=1&sn=48760fa1113d634cadb3f3e5a1090554&chksm=b058749d14a4a7d80003970f1f2bf82e0c7d35384808297f31dfec08a13d1d7487ac202a3da1&mpshare=1&scene=1&srcid=0907QfpQwTD9Rp9WLER12gI5&sharer_shareinfo=08c61788afdb258bfd35925ec6fbe3b6&sharer_shareinfo_first=08c61788afdb258bfd35925ec6fbe3b6#rd)
- **原始资源 URL**: [论文](https://arxiv.org/abs/2608.28281)、[作者官方代码与基准](https://github.com/AMAP-ML/LoopArena)、[项目页](https://amap-ml.github.io/LoopArena/)。论文与配套代码合并为同一条目。
- **用户备注**: 无额外备注。
- **去重结果**: 本库正式论文、Others、README 与既有报告未发现相同 arXiv ID、标题或官方仓库 URL；此次为新草稿，不自动成为 Seed。
- **出处与证据的区分**: 公众号链接保留作发现出处；本次未依赖其正文或宣传性表述判断论文结果。精读依据为可读的论文全文和第一方材料。

## 一句话结论

LoopArena 把“模型能否指导另一个固定编码 agent 做完任务”拆成单步决策、任务切片和完整任务三层评测；完整任务的最高观测成功率为 24.69%，但切片排序接近完整任务这一结论强烈依赖主表采用的 Core 评分口径，不能直接推广到其他验收规则。[论文 §2、§5.2、附录表 13](https://arxiv.org/html/2608.28281v1)

## 要解决的问题

一次端到端编码任务失败，可能是执行模型写不出代码，也可能是外层控制者选错下一步、误信过时进度、漏掉验证或过早停止。把整套 agent 的最终分数放在一起，难以分辨这两种能力。

LoopArena 固定 Worker、工具、预算、起始状态、运行环境和终局 evaluator，只替换负责指导 Worker 的 Controller。它评测的是这个固定执行条件下的运行时控制能力，没有训练新的 Controller，也没有提出持续改写 harness 的自我改进算法。[论文 §1、§2；官方协议](https://github.com/AMAP-ML/LoopArena/blob/main/docs/protocol.md)

## 先用大白话说

让同一个程序员分别接受五位项目负责人的指导。程序员完成一段工作后，记录员整理“做了什么、哪些检查真跑过、还缺什么”；负责人据此决定继续实现、补查证据，还是结束。这样可以较清楚地比较谁更会安排任务，而不会把不同程序员的水平一起混进分数。

这里的困难是长任务会不断改变状态：上一轮正确的计划，下一轮可能已经过时；“一个小任务完成”也不等于“整个目标完成”。Controller 只能看到经过整理的证据，必须在不直接动代码、不查看隐藏评分的条件下作决定。[论文 §2.2、§11.1、§17.4](https://arxiv.org/html/2608.28281v1)

## 一个具体例子

论文附录 §9.2 的真实 Type I 样例来自 Django 支持矩阵更新任务。当前证据显示版本矩阵基本改完，但留下了已无用途的 Django REST Framework 3.9 依赖 `drf39`。四个候选指令中，两个会误删仍被当前配置使用的依赖，一个保留孤立依赖并重复检查，正确选项是删除 `drf39` 且保留活跃配置。模型必须结合当前证据选择下一步；它在答题时不运行代码，标签来自预先执行候选方案后的结果。[论文附录 §9.2、表 3](https://arxiv.org/html/2608.28281v1)

另一个记录在案的 Type II 交接发生在 SCBench 的 watch mode 与 secondary configuration store 任务。Reporter 明确报告第一段仅完成定位、尚未实现功能，Controller 才派发包含 CLI 参数、seed lookup 和验证条件的实现任务。这个例子展示了交接机制；论文未在该例子的短摘录中给出完整任务最终胜负，不能把它当作新增成功率证据。[论文附录 §11.2](https://arxiv.org/html/2608.28281v1)

## 方法拆解

### 三个角色与两种结构化材料

| 组成 | 可读取的信息 | 可执行的行为与边界 |
|---|---|---|
| Worker | 原始公开任务、持续保留的自身对话、当前指令、工具结果 | 唯一能修改仓库、执行命令和运行检查的角色 |
| Reporter | 复制出的 Worker 对话、公开任务、静态只读工作区 | 整理事实和不确定性、引用 Worker 回合；不能执行代码或测试，报告过程不写回 Worker 对话 |
| Controller | 报告、被引用的完整 Worker 回合、预算、自己的历史报告与决策 | 输出下一步指令或停止；不能直接查看仓库、使用编码工具或读取私有 evaluator |
| Evidence Packet | 四段报告、引用证据与预算 | harness 确定性整理，不另调用模型“再总结” |
| Loop Contract | 决策、理由、Worker 任务与验收条件 | 经校验后转成 Worker 的下一条消息；`stop` 触发终局评测 |

Reporter 的四个字段分别覆盖任务约束、工作历史与当前状态、验证证据、未解决问题与不确定性。Controller 的 `advance` 用于推进实现，`verify` 用于补证据，`stop` 用于结束；继续执行时还要给出目标、上下文、必要结果、禁止动作、交回条件、应保持的不变量和验证验收条件。[论文 §11.1；官方协议 Information boundary / Decisions](https://github.com/AMAP-ML/LoopArena/blob/main/docs/protocol.md)

官方 `packet_compiler.py` 根据引用标签选择 Worker 原始回合，并把报告与剩余预算装入 Packet；`controller.py` 将模型输出校验、规范化为执行合约。这个设计使“摘要说了什么”和“原始工具证据是什么”可以对照，但不能保证 Reporter 永不漏报或误解。[Packet 编译源码](https://github.com/AMAP-ML/LoopArena/blob/main/src/looparena/harness/packet_compiler.py)、[Controller 源码](https://github.com/AMAP-ML/LoopArena/blob/main/src/looparena/harness/controller.py)

### 三层评测

| 设置 | 数据量 | 起点与执行范围 | 得分 |
|---|---:|---|---|
| Type I | 90 道；40 SCBench / 50 BeyondSWE | 冻结控制点与四个完整候选；新模型评测时不执行 Worker | Contract Accuracy、Invalid Rate |
| Type II | 27 个切片；11 SCBench / 16 BeyondSWE | 从准备好的中间工作区完成一个选定阶段，并检查截至该阶段的累积要求 | Strict Success Rate |
| Type III | 同一组 27 个完整任务 | 从原始任务状态执行；SCBench 按原生顺序完成所有 checkpoint，BeyondSWE 完成整个任务 | Strict Success Rate |

Type II 不是抽掉验证的快捷版：切片起点必须至少不满足一个新阶段要求，而官方完成状态必须通过截至该阶段的要求。Type II 与 Type III 一一配对，便于比较成本和模型排序。SCBench 的多 checkpoint 任务在统计中仍只算一个完整任务，不能把历史 case alias 当额外样本。[论文 §3、表 1、附录 §9.1；Type II 数据说明](https://github.com/AMAP-ML/LoopArena/blob/main/benchmarks/type2/README.md)

Type I 的正确答案由执行确定：先选父轨迹、再选可恢复的非 bootstrap 控制点，保留当时真实 Contract 并生成三个完整替代项；四项与顺序在观察结果前冻结。每项从同一状态运行两套匹配回放，先比任务是否成功，再以较少后续控制轮数、较少 Worker 回合打破成功项的并列。只有两套回放得到同一个唯一赢家才保留；全失败、无法分出唯一赢家或两套不一致均丢弃，事后不改选项修题。标签因此是这个固定 Worker 与回放协议下的优选项，不能理解为脱离执行条件的唯一正确管理策略。[论文 §3.3、附录 §10.1](https://arxiv.org/html/2608.28281v1)

## 实验与证据

所有 Type II/III Controller 模型都使用 **Qwen3.7-Plus** 作为共享 Worker，Reporter 也使用相同配置。五个 Controller 的实际接口标识分别为 `qwen3.7-plus`、`deepseek-v4-flash-0731`、`glm-5.2`、`gpt-5.5-0424-global`、`claude-opus-4-8`。Qwen、DeepSeek、GLM 使用温度 0；GPT、Claude 使用 provider-default thinking，不传温度或 seed 参数。这些是论文记录的接口配置，不表示各家推理预算完全等价。[论文 §5.1、附录 §12.1、表 5](https://arxiv.org/html/2608.28281v1)

每个 Controller、每条参考策略、每个 Type II/III 任务各运行 3 次，因此每方法每设置为 81 次。两种设置共 1,134 条规范化结果（2 × 7 × 27 × 3），不是 1,134 个独立任务。主 Worker 每 episode 上限 600 ReAct 回合或 7,200 秒，先到者结束并记失败；模型控制最多 128 次交接、累计 86,400 秒，Reporter 每次上限 50 回合。Controller 单请求最多输出 20,480 tokens，Worker/Reporter 为 8,192。多 checkpoint SCBench 保留工作区，但在原生 checkpoint 边界重启 Worker 与控制对话。[论文附录 §11.3、§12.2；发布结果说明](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/README.md)

成功同时要求 evaluator 通过和控制协议有效。SCBench 主结果要求全部 Core 检查通过；BeyondSWE 要求原生 Harbor evaluator 的 reward 为 1。无效合约、模型导致的协议违规或预算耗尽算失败；provider、容器、runner、evaluator 的基础设施故障单独记录。模型访问在终局评分前结束，私有评测结果不反馈给下一轮 Controller。[论文 §4.2、§11.5；官方协议 Evaluation](https://github.com/AMAP-ML/LoopArena/blob/main/docs/protocol.md)

## 实验结果总结

- **训练/评测模型**：无训练实验；评测上述五个 Controller，Worker/Reporter 固定为 Qwen3.7-Plus。
- **Benchmark / 数据**：90 道 Type I 选择题；27 对 Type II 切片与 Type III 完整任务，来自 11 个 SCBench、16 个 BeyondSWE 任务。
- **对比基线**：No control 让 Worker 一次接收完整任务后自主执行；Fixed control 在每次交接重述固定目标，直到 Worker 显式声明完成，没有根据报告调整指导的模型 Controller。它们提供参考，不进入五模型排序。Type I 另有随机、位置、动作、长度、词汇重叠等确定性捷径分析。
- **指标**：Type I Contract Accuracy / Invalid Rate；Type II/III Strict Success Rate（SSR）；无缓存估计推理成本；Worker 回合与控制轮数；Type II–III 的 Spearman 排名相关性；重复运行稳定性和来源子集分解。
- **主要结果**：GPT-5.5 在三个主指标上取得最高观测值；Type III 为 20/81 = 24.69%，Qwen 为 19/81 = 23.46%。Type II 相对 Type III 的平均配对成本降低 64.4%，Core 口径的五 Controller 排名相关性为 0.9747。[论文表 2、表 7；官方发布汇总](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/summary.json)

| 方法 | Type I 正确数 / 准确率 | Type II 成功数 / SSR | Type II 美元/次 | Type III 成功数 / SSR | Type III 美元/次 |
|---|---:|---:|---:|---:|---:|
| No control（参考） | — | 32/81 · 39.51% | 1.04 | 15/81 · 18.52% | 2.01 |
| Fixed control（参考） | — | 38/81 · 46.91% | 1.08 | 15/81 · 18.52% | 5.58 |
| Qwen3.7-Plus | 65/90 · 72.22% | 39/81 · 48.15% | 4.30 | 19/81 · 23.46% | 6.89 |
| DeepSeek-V4-Flash-0731 | 70/90 · 77.78% | 37/81 · 45.68% | 2.10 | 16/81 · 19.75% | 10.24 |
| GLM 5.2 | 67/90 · 74.44% | 30/81 · 37.04% | 1.63 | 13/81 · 16.05% | 4.86 |
| GPT-5.5 | 79/90 · 87.78% | 42/81 · 51.85% | 5.00 | 20/81 · 24.69% | 18.84 |
| Claude Opus 4.8 | 69/90 · 76.67% | 39/81 · 48.15% | 5.87 | 17/81 · 20.99% | 16.82 |

全部 Type I 回答均可解析，Invalid Rate 为 0。整套 90 题的新增评测成本依上表五模型顺序为 $0.70、$0.31、$3.02、$9.43、$13.68；它不包括构造题目时预先执行候选的成本。上述金额使用论文冻结的无缓存估价口径。[论文附录表 7、表 9、表 10](https://arxiv.org/html/2608.28281v1)

| Type I 捷径 | 准确率 |
|---|---:|
| 均匀随机选择 | 25.00% |
| 总选最常见答案位置 | 31.11% |
| 只看 advance / verify 动作 | 25.00% |
| 选择序列化后最短的候选 | 23.33% |
| Packet 与候选词汇重叠 | 18.89% |

每道 Type I 题的四个候选动作相同，动作类型本身不能区分答案。这些捷径都低于最弱 Controller 的 72.22%，支持题目需要结合证据与指令；它没有证明不存在其他未测试的捷径。[论文附录 §14.3、表 11](https://arxiv.org/html/2608.28281v1)

### 结果应如何理解

**切片排序接近完整任务，仅在指定评分口径成立。** Core 口径中，五模型共有十对，两两严格排序的九对没有反转，另一对含并列，Spearman 使用并列平均名次。更换 SCBench 验收集合后，相关性会明显改变；BeyondSWE 的评分保持不变。[论文 §5.2、附录 §13.2、表 13](https://arxiv.org/html/2608.28281v1)

| SCBench 评分规则 | Type II SSR 范围 | Type III SSR 范围 | Type II–III Spearman ρ |
|---|---:|---:|---:|
| 全部检查 | 28.40%–33.33% | 16.05%–17.28% | 0.1481 |
| 全部 non-error 检查 | 30.86%–35.80% | 16.05%–17.28% | -0.2962 |
| Core 检查（主结果） | 37.04%–51.85% | 16.05%–24.69% | 0.9747 |

**最高观测分数不等于显著领先。** GPT-5.5 比 Qwen 多成功一次，发布结果给出的 Type III 95% bootstrap 区间分别为 9.88%–40.74% 和 9.88%–38.27%。区间广且重叠，本笔记不据此宣称两模型存在显著差异。发布协议在来源内部重采样父任务、再重采样三个重复，进行 10,000 次抽样；27 个任务和五个 Controller 的结果不宜外推成稳定的通用排行榜。[官方 summary.json 的 ci95 / uncertainty](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/summary.json)、[bootstrap 说明](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/README.md)

**固定目标提示的收益随执行范围变化。** Fixed control 在 Type II 从 39.51% 提升到 46.91%，但 Type III 与 No control 同为 18.52%，估计成本却从 $2.01 增至 $5.58。这说明在本组任务和协议中，反复提醒继续并没有带来完整任务成功率收益；它不是“所有任务都必须用独立 Controller”的因果证明。[论文表 2、附录 §11.4](https://arxiv.org/html/2608.28281v1)

**64.4% 是按模型配对的推理估价降幅。** 先对每个 Controller 算 `1 - Type II平均成本 / Type III平均成本`，再对五模型取平均；不是把所有花费汇总后计算的比例。模型控制成本包含 Worker、Reporter、Controller，参考策略包含实际需要的 Worker 调用；无缓存估价采用 2026-08-16 冻结价格，不含仓库执行、终局 evaluator、存储等基础设施费用，也不等于当前价格或真实账单。旧 fixed-control 运行中生成但未被使用的 Reporter 调用在规范化费用中扣除。[论文附录 §11.4、§13.2、表 9–10；发布结果说明](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/README.md)

**来源与协议失败会影响解读。** 例如 GLM 5.2 在 Type III 的 SCBench Core 成功数为 0/33，BeyondSWE 为 13/48，不能只凭总分推断所有软件任务同样困难。论文还将输出触顶与非法 Contract 计为模型协议失败；附录表 12 的 DeepSeek/GLM 诊断集合中，162/1,614 次 Controller 调用触及 20,480-token 上限。该诊断集合共 167 evaluations，不能直接替换主榜每方法每设置 81 次的分母来估算总体失败率。[论文附录 §14.3、表 12、表 15](https://arxiv.org/html/2608.28281v1)

## 与 Seed 的关系

建议归入 **Others**。本库 `Harness RSI` 要求训练或执行经验触发对 prompt、tools、skills、workflow、retrieval 或 scaffold 的验证后更新。LoopArena 固定执行 harness 与 Worker，只比较 Controller 在任务中的下一步决策；没有展示持久的 harness 更新、训练或晋升闭环。因此，运行时自适应指导本身不足以满足该 Track 的收录边界。[本库术语定义](../../CONTEXT.md)

以下为本笔记的关联推断，不是声称原论文引用了这些 Seed：

- 与 [EvoTrainer](../../papers/harness-rsi/2606.03108.md) 的联系在于都关注执行证据；EvoTrainer 用证据修改诊断、干预和可复用 skill，LoopArena 可作为评价“新的控制策略是否更有效”的思路参照。
- 与 [EvoHarness-RL](../../papers/harness-rsi/2608.05446.md) 的联系在于运行时状态与控制策略；后者学习读、写和整合策略，LoopArena 当前主要贡献是固定 Worker 下的评测分离。
- 它对多模态 Deep Research 的可迁移价值是控制层评测设计；原实验是仓库编码任务，没有证明同样的排序、成本降幅或成功率适用于图文研究任务。

## 可迁移启示

1. **把执行能力和控制能力分开测。** 若研究自动精读流程的调度策略，先固定搜索、读取、写作工具与执行模型，再比较何时追查原文、何时核验、何时停止。
2. **报告必须带可回溯证据。** 保存“已核实、未核实、仍有冲突”的结构化状态，并能回到原始工具结果；Controller 的旧决定不能被当成工作已经完成的证据。
3. **廉价切片需要完整任务校准。** 小切片可以加快迭代，但在本项目的真实验收规则下重新检查排序一致性，不能直接套用论文的 0.9747。
4. **先建强且便宜的参考策略。** 同时测不加控制、固定目标提醒与自适应控制，并统计全部模型调用成本；复杂架构并不自动更划算。

以上是从论文方法作出的迁移建议，尚未在本仓库执行实验。

## 局限与待核对

- **覆盖有限**：仅仓库级编码、单 Worker 家族与结构化交接；多 Worker、其他执行模型、其他领域及多模态 Deep Research 均需再验证。Type II 从准备好的中间状态出发，可能避开完整任务最困难的早期路径依赖。[论文 §7](https://arxiv.org/html/2608.28281v1)
- **Controller 分数仍依赖整个信息通道**：固定 Worker 有利于比较，但 Reporter 的摘要与证据选择、提示词、工具及上下文策略都界定了评测条件；不能将结果解释为与这些条件无关的纯管理能力。
- **小样本与评分敏感性**：27 个任务、每任务三次、五个 Controller；Core 下的高相关性在另外两套评分中不保持。未据此声称 Type II 可全面替代 Type III。
- **Type I 的范围**：它测冻结状态下四选一，不能独立证明模型会生成好 Contract、长期跟踪任务或正确选择停止；两套回放一致也只控制了有限的随机性。
- **发布材料边界**：公开 `outcomes.jsonl` 可复核 SSR、来源分解与重复结果，费用仍是冻结发布元数据，完整 provider usage 与原始轨迹未包含在这份公开结果包中。本次未运行上游代码或模型 API，属于全文与发布数据核对，并非独立实验复现。[结果包说明](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/README.md)
- **Type I 输入边界**：官方数据说明将 `input`（模型消息）与 `ideal`（答案）列为不同字段；复用时只应发送 `input`。公开数据有答案字段，不宜概括为“公开文件完全不含答案”。[Type I 数据说明](https://github.com/AMAP-ML/LoopArena/blob/main/benchmarks/type1/README.md)
- **复现待核对**：论文 v1 的 `stop` 示例只有 `action`、`rationale`；2026-09-08 查阅的 `main` 中，`rendering.py` 的系统提示与 `controller.py` 校验使用带空辅助字段的五字段形态，而末尾 reminder 仍写两字段。实际复现需固定提交并核对协议版本；该源码观察不能倒推已发表分数受到影响。[提示词源码](https://github.com/AMAP-ML/LoopArena/blob/main/src/looparena/harness/rendering.py)、[校验源码](https://github.com/AMAP-ML/LoopArena/blob/main/src/looparena/harness/controller.py)
- **元数据待核对**：HTML 的作者上标渲染不完整，暂不逐一归属机构；主要机构列表和七位作者顺序已有原文依据，不将任职关系补猜出来。

## 相关链接

- Paper HTML: [arXiv v1 全文](https://arxiv.org/html/2608.28281v1)
- Code: [AMAP-ML/LoopArena](https://github.com/AMAP-ML/LoopArena)
- Dataset / Project: [项目主页](https://amap-ml.github.io/LoopArena/)、[Benchmark 数据目录](https://github.com/AMAP-ML/LoopArena/tree/main/benchmarks)
- Protocol: [docs/protocol.md](https://github.com/AMAP-ML/LoopArena/blob/main/docs/protocol.md)
- Results: [v0.1.0 发布说明](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/README.md)、[summary.json](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/summary.json)、[manifest.json](https://github.com/AMAP-ML/LoopArena/blob/main/results/0.1.0/manifest.json)

本文件为草稿。用户明确确认 LoopArena 后，才整理至 `others/looparena.md` 并更新正式索引。
