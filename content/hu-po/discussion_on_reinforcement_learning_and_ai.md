---
title: Discussion on reinforcement learning and AI
videoId: oQqOiwUhJkA
---

From: [[hu-po]] <br/> 

The release of OpenAI's O1 model has sparked significant discussion within the [[challenges_and_advancements_in_ai_research | AI research]] community, largely due to its performance on benchmarks and the underlying techniques believed to be in use. While some critics argue O1 is merely a "glorified Chain of Thought," others consider it a highly surprising research result and a potential "new scaling paradigm" <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.

## The O1 Model and the Chain of Thought Debate

O1, or "Strawberry" as it was informally referred to, is OpenAI's latest model that has been observed breaking various benchmarks <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. However, it has been met with skepticism from some [[current_state_of_ai_agents_and_their_limitations | AI YouTubers]] who contend it's simply a "glorified Chain of Thought" <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. This criticism stems from a previous incident where an [[current_state_of_ai_agents_and_their_limitations | AI Twitter personality]] achieved high benchmark scores with "Reflection 70B" by primarily using prompt engineering and Chain of Thought with Anthropic's Sonnet 3.5 model <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

### Test Time Computation and Chain of Thought

The concept of "test time computation" refers to the compute used during the evaluation or inference phase of a model <a class="yt-timestamp" data-t="14:21:00">[14:21:21]</a>. Traditionally, models were evaluated based on their immediate, "zero-shot" output <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>. However, allocating a budget of compute for each question at test time can significantly improve performance <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.

Chain of Thought prompting, a technique described in a January 2023 paper, enables large language models to elicit complex, multi-step reasoning by generating step-by-step answers, achieving [[stateoftheart_in_reinforcement_learning | state-of-the-art performances]] <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>. This technique, while effective, is not new, which contributes to the contention around OpenAI's claims <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. OpenAI's API documentation indicates that for O1 models, "total tokens generated can exceed the number of visible tokens due to the internal reasoning tokens" <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>. These "internal reasoning tokens" might include special tokens for actions like "use a calculator" or "think step-by-step," or they might simply be standard text tokens used for internal deliberation <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>.

A significant point of contention is OpenAI's decision to not show the raw Chain of Thought to users, citing security and safety arguments <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. This secrecy is also theorized to be an anti-competitive measure, preventing others from fine-tuning open-source models like LLaMA on OpenAI's internal reasoning traces <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.

## The Role of [[Reinforcement learning and selfplay in AI development | Reinforcement Learning and Self-Play]]

The core innovation believed to be behind O1's performance, beyond just Chain of Thought, is the integration of [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning and self-play]].

### Process-Based Reward Models and Search Methods

At the heart of this approach are "process-based reward models" (PRM), which evaluate not just the final answer but the entire Chain of Thought or process that led to it <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>. This addresses the "credit assignment problem" in [[ai_and_reinforcement_learning | reinforcement learning]] by determining the utility of each step taken in a reasoning process <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.

Different search methods employ PRMs to explore possible reasoning paths:
*   **Best of N**: The simplest, where an LLM generates N answers, and a reward model picks the best one <a class="yt-timestamp" data-t="18:30:00">[18:30:00]</a>.
*   **Beam Search & Look Ahead Search**: More complex methods that run the verifier (reward model) on intermediate steps of the process, picking optimal paths <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.
*   **Monte Carlo Tree Search (MCTS)**: A technique, commonly used in games like Tic-Tac-Toe or Go, where the model builds a tree of possible actions and states, simulates "rollouts" (paths through the tree), and uses a value function to guide its search for the best move <a class="yt-timestamp" data-t="20:20:00">[20:20:00]</a>. This process of searching and simulating incurs "test time computation" costs <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a>.

For [[ai_and_reinforcement_learning | AI and Reinforcement Learning]] applications, the environment needs to be representable as a Markov Decision Process (MDP), requiring discrete states and actions <a class="yt-timestamp" data-t="22:22:00">[22:22:00]</a>. Text, with its limited vocabulary and token-based nature, fits this requirement, allowing for tree-based search methods <a class="yt-timestamp" data-t="22:09:00">[22:09:00]</a>.

### The "New Green Bar": RL Training Beyond RHF

Traditional LLM development involves a massive "pre-training" phase, followed by "post-training" which often boils down to Reinforcement Learning from Human Feedback (RLHF) or instruction tuning <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>. RLHF relies on human labelers comparing outputs and indicating preferences, leading to a reward model that imitates human "vibe checks" <a class="yt-timestamp" data-t="47:02:00">[47:02:00]</a>. However, RLHF is criticized for often making models "stupider" by focusing on human preferences rather than objective problem-solving <a class="yt-timestamp" data-t="47:50:00">[47:50:00]</a>.

The emerging "new green bar" represents a significant investment in a more "real" or "classic" [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning and selfplay in AI development]] approach, akin to AlphaGo Zero <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. AlphaGo Zero famously cost $35 million in computing power, primarily for simulating millions of games against itself and using the outcomes to assign credit to intermediate moves <a class="yt-timestamp" data-t="35:49:00">[35:49:00]</a>. This self-play approach pushes gradients into the model itself, making it fundamentally better at reasoning, rather than just adding a Chain of Thought abstraction on top <a class="yt-timestamp" data-t="36:44:00">[36:44:00]</a>.

This integration is seen as the "first merging" of the LLM world (next-token prediction at massive scale) and the DeepMind-style [[Reinforcement learning and selfplay in AI development | self-play and reinforcement learning]], a combination that Google's Gemini project also aims to achieve <a class="yt-timestamp" data-t="39:16:00">[39:16:00]</a>. This new phase of [[applications_in_machine_learning_and_reinforcement_learning | machine learning and reinforcement learning]] involves generating high-quality training data through self-play simulations and reflection, and then fine-tuning models on this synthetic data <a class="yt-timestamp" data-t="38:12:00">[38:12:00]</a>.

## Implications for [[Selfimproving AI through reinforcement learning and reasoning | Self-Improving AI through Reinforcement Learning and Reasoning]]

This shift paves the way for [[selfimproving_ai_through_reinforcement_learning_and_reasoning | self-improving AI through reinforcement learning and reasoning]].

### Path to Superhuman Reasoning

The ability to use [[ai_and_reinforcement_learning | reinforcement learning]] for reasoning tasks, particularly in domains with objective correctness like math or coding, offers a clear path to "superhuman reasoning" <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>. While subjective tasks like writing or philosophy might not yield a clear reward signal for direct RL, evidence suggests that excelling in one domain (e.g., coding) can transfer to others (e.g., poetry) <a class="yt-timestamp" data-t="51:47:00">[51:47:00]</a>. This implies that even if real RL is only possible for certain tasks, the resulting improvement in general reasoning could uplift performance across the board <a class="yt-timestamp" data-t="52:09:00">[52:09:00]</a>.

### Challenges and Costs

This approach introduces new [[challenges_and_costs_in_reinforcement_learning_implementation | challenges and costs in reinforcement learning implementation]]. The compute required for the "green bar" of RL post-training is expected to rival or even exceed the cost of pre-training <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>. This necessitates specialized data centers and hardware optimized for different workloads: strong CPUs for simulations (experience collection) and GPUs for gradient pushing (policy training) <a class="yt-timestamp" data-t="30:51:00">[30:51:00]</a>.

OpenAI's O1 model is also believed to be a "small model" <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. The motivation for using a smaller model for internal reasoning is financial: reducing the cost of "test time compute" <a class="yt-timestamp" data-t="55:51:00">[55:51:00]</a>. The goal is an "extremely small model that has superhuman reasoning" <a class="yt-timestamp" data-t="56:03:00">[56:03:00]</a>.

### The Bitter Lesson and Future Outlook

The "bitter lesson," proposed by Rich Sutton, suggests that simple, massively scaled computational methods often outperform more complex, human-engineered [[challenges_and_methodologies_in_ai_training | AI training methodologies]] over time <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>. While current [[ai_and_reinforcement_learning | AI and Reinforcement Learning]] systems like O1 might involve complex "over-engineered ways of creating these superhuman systems" <a class="yt-timestamp" data-t="01:19:27">[01:19:27]</a>, the long-term trend could see the simpler, massive scaling of pre-training alone eventually achieving similar results <a class="yt-timestamp" data-t="01:18:52">[01:18:52]</a>.

Nonetheless, the emergence of O1 represents a significant milestone: "production-grade actual [[Reinforcement learning and selfplay in AI development | Reinforcement Learning and Self-Play]] on an LLM that has been convincingly achieved and demonstrated" <a class="yt-timestamp" data-t="01:24:22">[01:24:22]</a>. This combination of pre-training and [[reinforcement_learning_and_selfplay_in_ai_development | self-play RL]] can be scaled indefinitely, as the model generates its own training data by playing against itself <a class="yt-timestamp" data-t="01:51:51">[01:51:51]</a>. This continuous self-improvement process has the potential to lead not just to Artificial General Intelligence (AGI), but to Artificial Superintelligence (ASI) <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>.