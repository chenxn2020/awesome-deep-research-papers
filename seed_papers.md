### Rubric-RL
主要想解决两个问题：
+ 将多维reward压成scalar reward，会损失criterion-level信息
+ rubric随着训练演进需要更新或者根据group内行为设定合适的rubric
1. [open rubric system scaling reinforcement learning with pairwise adaptive rubric](https://arxiv.org/abs/2602.14069):建立一套rubric合成框架，同时使用了pair-wise和point-wise
2. [Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL](https://arxiv.org/abs/2608.11669):借助dropout思想，防止policy只优化rubric 中的某项criterion
3. [GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://arxiv.org/abs/2601.05242):multi-reward设置，解决了多reward下不同reward gap会被GRPO映射成为完全相同的adv
4. [CriPO: Enhancing Rubric-based RL via Self-Distillation](https://arxiv.org/abs/2607.18082): 使用OPSD来解决unexplored criteria和suppressed criteria
### Data Synthesis
只关注多模态（图文）deepresearch的数据合成或者benchmarks
1. [TVIR: Building Deep Research Agents Towards Text-Visual Interleaved Report Generation
](https://arxiv.org/abs/2606.02320)
2. [MMDeepResearch-Bench: A Benchmark for Multimodal Deep Research Agents
](https://arxiv.org/abs/2601.12346)
3. [MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome](https://arxiv.org/abs/2603.28407)
4. [HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research](https://arxiv.org/abs/2607.25151)
5. [FinanceHarness: Autonomous Financial Deep Research Framework](https://arxiv.org/abs/2607.27853)
### OpenAI-bench
1. [FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks
](https://arxiv.org/abs/2601.21165)
### Some Blogs
1. [The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)
### Credit Assignment
1. [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://arxiv.org/abs/2510.14967)

### Official Lab Blogs
仅收录 Anthropic、OpenAI 等前沿 AI 大厂官方博客中，直接解释 Deep Research、Agent RL、Rubric、Harness 或相关评测的文章。
### Harness RSI
1. [EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03108)
2. [Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses](https://arxiv.org/html/2608.24876v1)
3. [EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents](https://arxiv.org/html/2608.05446v1)
