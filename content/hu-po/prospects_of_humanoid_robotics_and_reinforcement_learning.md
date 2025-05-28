---
title: Prospects of Humanoid Robotics and Reinforcement Learning
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

The intersection of large language models (LLMs) and reinforcement learning (RL) is currently a significant area of research, with direct implications for the [[robotics_and_automation_advancements | field of robotics]], particularly in the development of humanoid robots <a class="yt-timestamp" data-t="01:14:04">[01:14:04]</a>. Experts suggest that the world is only a few years away from the widespread presence of humanoid robots in homes <a class="yt-timestamp" data-t="01:13:40">[01:13:40]</a>.

## Reinforcement Learning Foundations
[[reinforcement_learning_in_ai | Reinforcement learning]] aims to maximize an expected cumulative reward based on interactions within an environment <a class="yt-timestamp" data-t="02:00:58">[02:00:58]</a>. Key concepts include:
*   **States and Actions**: Agents transition between states by taking actions <a class="yt-timestamp" data-t="02:24:15">[02:24:15]</a>.
*   **Reward Function**: A function that assigns a value to a state-action pair, indicating how good a particular action is in a given state <a class="yt-timestamp" data-t="02:24:21">[02:24:21]</a>.
*   **Policy**: A function that chooses the best action for a given state, aiming to maximize future rewards <a class="yt-timestamp" data-t="02:24:33">[02:24:33]</a>.
*   **Discount Factor**: Future rewards are discounted, making immediate rewards more important <a class="yt-timestamp" data-t="02:51:16">[02:51:16]</a>.

### AlphaGo and Self-Play
A pinnacle of [[reinforcement_learning_in_ai | reinforcement learning]] success is AlphaGo, which achieved superhuman performance in the game of Go <a class="yt-timestamp" data-t="02:00:41">[02:00:41]</a>. AlphaGo's success stemmed from its ability to use self-play to generate vast amounts of experience data <a class="yt-timestamp" data-t="01:54:48">[01:54:48]</a>. This self-play approach allowed the system to explore novel tactics that surpassed human capabilities <a class="yt-timestamp" data-t="01:38:43">[01:38:43]</a>. The key insight is that the policy itself creates higher-quality data than human expert demonstrations, leading to superhuman performance <a class="yt-timestamp" data-t="01:56:07">[01:56:07]</a>.

## LLMs as Reinforcement Learning Components
Recent research suggests that LLMs can be directly thought of as components within an [[reinforcement_learning_in_ai | RL]] framework <a class="yt-timestamp" data-t="02:24:45">[02:24:45]</a>.
*   **Function Approximators**: LLMs are deep neural networks approximating a conditional probability distribution of tokens <a class="yt-timestamp" data-t="02:30:12">[02:30:12]</a>.
*   **Auto-regressive Manner**: LLMs operate in an auto-regressive manner, generating tokens one at a time based on previous tokens <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This sequential generation can be framed as a Markov decision process (MDP) <a class="yt-timestamp" data-t="02:52:09">[02:52:09]</a>.

A paper titled "From R to Q-star: Your language model is secretly a Q function" theoretically demonstrates that LLMs can be interpreted as optimal Q-functions for certain reward functions in a token-level MDP <a class="yt-timestamp" data-t="01:37:38">[01:37:38]</a>. This implies that the principles of Q-learning are directly applicable to how LLMs operate <a class="yt-timestamp" data-t="01:43:08">[01:43:08]</a>.

### Alpha-LLM: Self-Improvement for LLMs
The "Toward Self-Improvement of LLMs via Imagination Searching and Criticizing" paper (Alpha-LLM) applies AlphaGo's self-learning loop to language models <a class="yt-timestamp" data-t="01:54:19">[01:54:19]</a>.
*   **Components**: Alpha-LLM uses an "imagination" component and an "efficient search" component <a class="yt-timestamp" data-t="02:59:10">[02:59:10]</a>.
*   **Monte Carlo Tree Search (MCTS)**: This search algorithm explores potential sequences of tokens (trajectories) <a class="yt-timestamp" data-t="02:59:07">[02:59:07]</a>.
    *   Unlike Go, where actions are discrete board moves, language models have a vast action space of 30,000 possible tokens at each step <a class="yt-timestamp" data-t="01:55:28">[01:55:28]</a>.
    *   **Option-Level MCTS**: To mitigate the vast search space, Alpha-LLM uses an "option level" search where actions are sequences of tokens rather than individual tokens, with a termination function determining the length of the sequence <a class="yt-timestamp" data-t="02:55:39">[02:55:39]</a>.
*   **Critics/Value Functions**: These are LLMs that estimate the value of a given trajectory <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>. They can be trained using:
    *   **Process Reward Model (PRM)**: Provides feedback for each step in a chain of thought <a class="yt-timestamp" data-t="01:49:54">[01:49:54]</a>.
    *   **Outcome Reward Model (ORM)**: Provides feedback only on the final result of a trajectory <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>.
*   **Self-Improvement Loop**: The system generates synthetic data through MCTS, evaluates it with critics, and then fine-tunes the policy (LLM) using this high-quality data <a class="yt-timestamp" data-t="01:55:01">[01:55:01]</a>. This process aims to create a virtuous cycle where the model continually improves itself <a class="yt-timestamp" data-t="01:55:47">[01:55:47]</a>.

Alpha-LLM demonstrated significant performance improvements on math reasoning problems (GSM8K and MATH datasets), achieving scores comparable to GPT-4 *when MCTS is used during inference* <a class="yt-timestamp" data-t="01:03:02">[01:03:02]</a>. This indicates that the improvement is primarily due to the sophisticated search strategy rather than a fundamentally "smarter" base model <a class="yt-timestamp" data-t="01:58:25">[01:58:25]</a>.

## Prospects for Humanoid Robotics
The techniques developed for LLMs and their integration with [[reinforcement_learning_in_ai | reinforcement learning]] have direct and profound implications for [[robotics_and_automation_advancements | robotics]], especially humanoid robots <a class="yt-timestamp" data-t="01:14:04">[01:14:04]</a>.

> [!NOTE] Clear Reward Signals
> In games like Go, or problems like math and coding, the final answer (win/loss, correct/incorrect) provides a clear, unambiguous reward signal <a class="yt-timestamp" data-t="01:57:17">[01:57:17]</a>. This is crucial for [[challenges_and_techniques_in_reinforcement_learning | reinforcement learning]] to effectively learn and improve <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>.

[[robotics_and_automation_advancements | Robotics]] often provides similar clear reward signals. If a robot is tasked with grasping an object, it either successfully grasps it or not <a class="yt-timestamp" data-t="01:15:18">[01:15:18]</a>. This allows for the direct application of self-play and value function evaluation strategies to train robot policies <a class="yt-timestamp" data-t="01:15:26">[01:15:26]</a>.

### LLMs as Robot Policies
*   **Action Tokens**: Instead of text tokens, a robot's policy could output "action tokens" <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>. This aligns with research in "Robotics Transformers" (e.g., RT2, RTX) where pre-trained language models are adapted to output robot actions <a class="yt-timestamp" data-t="01:14:39">[01:14:39]</a>.
*   **Discrete Action Space**: While continuous action spaces exist in [[robotics_and_automation_advancements | robotics]], they can be discretized into bins (e.g., 256 bins for joint movements) <a class="yt-timestamp" data-t="01:31:20">[01:31:20]</a>, making them compatible with token-based RL approaches.
*   **Credit Assignment**: Being able to assign credit to specific actions within a long trajectory, even when the reward is sparse (only at the end), is vital for efficient learning <a class="yt-timestamp" data-t="01:32:59">[01:32:59]</a>. This ability, linked to how LLMs process information, can enable learning from offline data collected by different robots <a class="yt-timestamp" data-t="01:35:12">[01:35:12]</a>.

### Industry Implications
The excitement around [[future_of_humanoid_robots_and_llms | humanoid robots]] is palpable, with leading researchers from major tech companies like Google, including prominent figures such as Chelsea Finn and Sergey Levine, leaving to form their own humanoid robotics companies <a class="yt-timestamp" data-t="01:13:56">[01:13:56]</a>. This exodus suggests a strong belief among top talent that these advancements in LLMs and [[reinforcement_learning_in_ai | reinforcement learning]] are paving the way for human-level and superhuman-level embodied AI <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>.

## Challenges and Future Directions
Despite the promising results, [[challenges_in_endtoend_robotic_learning | challenges remain]]:
*   **Generalization Beyond Specific Tasks**: Current demonstrations of LLM self-improvement in RL are primarily limited to domains like math and coding, where objective evaluation is straightforward <a class="yt-timestamp" data-t="01:57:01">[01:57:01]</a>. Extending this to general natural language reasoning, where reward signals are fuzzier, is a significant hurdle <a class="yt-timestamp" data-t="01:57:12">[01:57:12]</a>.
*   **Continual Improvement**: Some self-play papers with LLMs show limited iterations of improvement, suggesting that current methods may hit a wall or even degrade after a few cycles <a class="yt-timestamp" data-t="01:05:33">[01:05:33]</a>. Future work needs to address stable and continual performance gains.
*   **Dynamic Critics**: Allowing the critic models (value functions) to also improve over time, rather than remaining static, could significantly improve training dynamics and lead to more robust [[agent_loops_and_reinforcement_learning_in_ai | agent loops]] <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>.

The ability to train [[reinforcement_learning_with_human_feedback_rlhf | RL]] agents, including humanoid robots, using self-play loops and LLM-based critics promises to unlock unprecedented levels of intelligence and capability in embodied AI <a class="yt-timestamp" data-t="01:59:51">[01:59:51]</a>.