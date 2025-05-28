---
title: Language Models as Q functions
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

The concept of [[quantization in large language models | Qstar]] and its implications in the AI world has led to a deeper understanding of how Large Language Models (LLMs) might secretly function as Q functions <a class="yt-timestamp" data-t="01:10:02">[01:10:02]</a>. This connection bridges the fields of language modeling and reinforcement learning (RL), suggesting that LLMs can be viewed through the lens of optimal decision-making processes.

## The Q function in Reinforcement Learning

In reinforcement learning, a Q function (or quality function) estimates the value of taking a particular action in a given state <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>. The goal of RL algorithms is to find an optimal Q function (often denoted as Q*) that guides a policy (the decision-making agent) to maximize expected future rewards <a class="yt-timestamp" data-t="01:10:46">[01:10:46]</a>. The optimal Q function represents the maximum possible cumulative discounted reward that can be obtained from a given state-action pair <a class="yt-timestamp" data-t="01:10:49">[01:10:49]</a>.

## Language Models as Markov Processes

LLMs operate in an autoregressive manner, generating tokens one at a time, relying solely on the context provided by previously generated tokens <a class="yt-timestamp" data-t="02:30:1">[02:30:1]</a>. This process inherently constitutes a Markov decision process (MDP) <a class="yt-timestamp" data-t="02:40:9">[02:40:9]</a>. In this view:
*   **States:** A sequence of input tokens or previously generated tokens <a class="yt-timestamp" data-t="02:23:4">[02:23:4]</a>.
*   **Actions:** The selection of the next token from a predefined vocabulary <a class="yt-timestamp" data-t="02:39:42">[02:39:42]</a>.
*   **Policy:** The LLM itself, which picks the best token for a particular context <a class="yt-timestamp" data-t="02:44:5">[02:44:5]</a>.

While the terminology differs (input/output sequences in LLMs vs. states/actions/trajectories in RL), the underlying concepts are fundamentally the same <a class="yt-timestamp" data-t="02:52:53">[02:52:53]</a>.

## Direct Preference Optimization (DPO) and Q-Learning

The paper "From R to Qstar: Your Language Model is Secretly a Q Function" from Stanford University (featuring Chelsea Finn) theoretically demonstrates that Direct Preference Optimization (DPO) and token-level MDPs (Markov Decision Processes) in LLMs are effectively equivalent to the Q-learning algorithm and satisfy the Bellman equation <a class="yt-timestamp" data-t="01:20:12">[01:20:12]</a>, <a class="yt-timestamp" data-t="01:21:18">[01:21:18]</a>. This implies that DPO can be used to learn the optimal policy for any per-token reward function <a class="yt-timestamp" data-t="01:28:47">[01:28:47]</a>.

### Key Insights:
*   **LLM as Optimal Soft Q Function:** An LLM can be considered the optimal soft Q function for some reward function within a token-level MDP <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>.
*   **Discrete Action Space:** Natural language is a discrete space (limited set of tokens), which is advantageous because these theoretical interpretations do not generally hold in continuous spaces <a class="yt-timestamp" data-t="01:30:40">[01:30:40]</a>. This also opens possibilities for robotic control by discretizing actions <a class="yt-timestamp" data-t="01:31:10">[01:31:10]</a>.
*   **Explaining DPO Phenomena:** This framework explains observed phenomena in DPO training, such as the likelihood of chosen responses sometimes decreasing over time, by linking it to concepts in maximum entropy reinforcement learning <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>.

## Implications and Future Directions

The realization that LLMs are secretly Q functions has significant implications for [[performance_and_implications_of_quantized_language_models | LLM self-improvement]] and the broader field of AI:

### Self-Improvement Loops
Inspired by AlphaGo's success through self-play <a class="yt-timestamp" data-t="01:35:54">[01:35:54]</a>, researchers are exploring similar self-improvement loops for LLMs. This involves:
1.  **Data Generation:** LLMs synthesize their own data by exploring possible "trajectories" (sequences of tokens) through search algorithms like Monte Carlo Tree Search (MCTS) <a class="yt-timestamp" data-t="02:54:47">[02:54:47]</a>.
2.  **Critic/Value Function:** Another language model, often initialized from the policy model itself, acts as a "critic" or value function to estimate the quality or reward of these generated trajectories <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>, <a class="yt-timestamp" data-t="03:07:4">[03:07:4]</a>. These critics can evaluate entire responses (Outcome Reward Model - ORM) or individual steps (Process Reward Model - PRM) <a class="yt-timestamp" data-t="01:48:47">[01:48:47]</a>.
3.  **Policy Fine-tuning:** The LLM (policy) is then fine-tuned on the high-quality synthetic data generated and evaluated by the critics <a class="yt-timestamp" data-t="02:58:47">[02:58:47]</a>. This allows the model to learn from its own "experience" and improve <a class="yt-timestamp" data-t="02:55:21">[02:55:21]</a>.

This self-play loop has shown drastic improvements in tasks like mathematical reasoning and coding, where a clear "correct" or "wrong" answer provides an objective reward signal <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>, <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

### Guided Decoding
Simply using search algorithms like MCTS or beam search during inference time dramatically improves LLM performance, even if the underlying model weights aren't necessarily "smarter" <a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>, <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>. This suggests that future LLM products will likely incorporate such "guided decoding" techniques in the background <a class="yt-timestamp" data-t="01:58:52">[01:58:52]</a>.

### [[integration_of_large_language_models_in_interactive_agents | Robotics and Embodied AGI]]
The ability to define clear reward signals in robotics (e.g., did the robot successfully grasp an object?) means that LLM-based policies outputting action tokens for robots could utilize these self-play loops to achieve superhuman performance <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>, <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>. This potential has led prominent researchers in RL and robotics to leave established companies to found their own humanoid robotics startups <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>, <a class="yt-timestamp" data-t="01:16:15">[01:16:15]</a>.

### Credit Assignment
The ability of LLMs to act as Q functions also enables "credit assignment," meaning they can identify which specific tokens or actions within a long trajectory were most responsible for a successful outcome <a class="yt-timestamp" data-t="01:33:36">[01:33:36]</a>. This is crucial for learning from offline data, where experience might not have been collected by the current policy <a class="yt-timestamp" data-t="01:35:12">[01:35:12]</a>.

## Limitations

While promising, current self-improvement methods for LLMs still face challenges:
*   **Limited Iterations:** Papers demonstrating self-improvement often only run for a few iterations, suggesting a "wall" beyond which performance doesn't continue to improve or even degrades <a class="yt-timestamp" data-t="01:04:49">[01:04:49]</a>. This could be due to issues with training dynamics, such as the critic models remaining static (not receiving gradients) <a class="yt-timestamp" data-t="01:07:08">[01:07:08]</a>.
*   **Domain Specificity:** The most significant improvements are currently seen in domains like math and coding, where objective evaluation is straightforward <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>. Extending this to general natural language reasoning, where "correctness" is more fuzzy, remains an open problem <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.