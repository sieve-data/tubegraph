---
title: Reinforcement Learning and Q Learning in AI
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

Q* (Q-star) is a rumored method, technique, or algorithm that OpenAI allegedly used to achieve a significant step-function improvement in the current state of AI <a class="yt-timestamp" data-t="03:00:04">[03:00:04]</a>. The name itself hints at [[reinforcement_learning_in_ai | reinforcement learning]] concepts, with "Q" likely standing for the "Q function," a core concept in [[reinforcement_learning_in_ai | reinforcement learning]] <a class="yt-timestamp" data-t="03:00:04">[03:00:04]</a>. The "star" in Q* could refer to the optimal Q function (Q*) <a class="yt-timestamp" data-t="03:59:10">[03:59:10]</a>, or even potentially the A* search algorithm, suggesting a combination of Q-learning with A*-like search <a class="yt-timestamp" data-t="03:59:10">[03:59:10]</a>.

Yann LeCun states that Q* is likely OpenAI's attempt at planning, a concept that has been explored in [[reinforcement_learning_in_ai | reinforcement learning]] for decades <a class="yt-timestamp" data-t="04:04:47">[04:04:47]</a>. He notes that nearly every top AI lab, including Facebook AI Research (Meta), DeepMind (Google), and OpenAI (Microsoft), is working on similar ideas and some have already published results <a class="yt-timestamp" data-t="03:50:52">[03:50:52]</a>.

## Reinforcement Learning Fundamentals

[[reinforcement_learning_in_ai | Reinforcement learning]] (RL) is a paradigm where an agent learns to maximize a cumulative reward by taking actions in an environment <a class="yt-timestamp" data-t="24:56:00">[24:56:00]</a>. Key concepts in RL include:
*   **Markov Decision Process (MDP):** The cornerstone of RL, describing a system where an agent transitions between states by taking actions, receiving rewards based on state-action pairs <a class="yt-timestamp" data-t="24:11:00">[24:11:00]</a>. A language model (LLM) can be thought of as a policy executing an MDP <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>.
*   **Policy (π):** A function that dictates which action to take given a certain state <a class="yt-timestamp" data-t="23:48:00">[23:48:00]</a>. In LLMs, the policy determines the next token based on previous tokens <a class="yt-timestamp" data-t="23:54:00">[23:54:00]</a>.
*   **Value Function (V):** Estimates the expected cumulative reward from a given state <a class="yt-timestamp" data-t="27:57:00">[27:57:00]</a>.
*   **Q-function (Q):** Estimates the expected cumulative reward for taking a specific action in a specific state <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>.
*   **Reward (R):** A signal indicating the desirability of an action or state <a class="yt-timestamp" data-t="24:21:00">[24:21:00]</a>. RL aims to maximize the expected discounted future rewards, where future rewards are slightly less important <a class="yt-timestamp" data-t="50:42:00">[50:42:00]</a>.
*   **Credit Assignment Problem:** Determining which actions in a sequence contributed most to a final reward <a class="yt-timestamp" data-t="01:33:14">[01:33:14]</a>.

## Monte Carlo Tree Search (MCTS)

[[reinforcement_learning_and_selfplay_in_ai_development | MCTS]] is a sampling-based search algorithm that has enabled models to achieve superhuman performance in complex tasks like the game of Go (AlphaGo) <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>. [[reinforcement_learning_and_selfplay_in_ai_development | MCTS]] works in four phases <a class="yt-timestamp" data-t="26:02:00">[26:02:00]</a>:
1.  **Selection:** Recursively selecting child nodes from the root <a class="yt-timestamp" data-t="26:07:00">[26:07:00]</a>.
2.  **Expansion:** Adding new nodes to the tree based on possible actions <a class="yt-timestamp" data-t="26:39:00">[26:39:00]</a>.
3.  **Evaluation (Simulation):** Estimating the value of newly expanded nodes using a fast rollout policy <a class="yt-timestamp" data-t="26:54:00">[26:54:00]</a>.
4.  **Backpropagation:** Updating the estimated values of ancestor nodes based on the evaluation <a class="yt-timestamp" data-t="28:38:00">[28:38:00]</a>.

AlphaGo achieved superhuman performance by using [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning on self-play]] <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>. This allows the model to explore novel tactics beyond human expert data <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.

## Challenges in Applying [[Reinforcement Learning to LLMs]]

Applying [[reinforcement_learning_in_ai | reinforcement learning]] directly to LLMs presents unique [[challenges_and_techniques_in_reinforcement_learning | challenges and techniques in reinforcement learning]]:
*   **Vast Search Space:** LLMs operate on a vocabulary of around 30,000 possible tokens at each step, making the "action space" enormous compared to games like Go <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **Subjective Feedback:** Unlike games with clear win/loss conditions, evaluating natural language responses for a "win" or "loss" is fuzzy and subjective, making it difficult to derive unambiguous reward signals <a class="yt-timestamp" data-t="16:56:00">[16:56:00]</a>.
*   **Data Scarcity:** High-quality, expert-annotated data for training reward models can be scarce <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.

## AlphaLLM: A Self-Improvement Framework for LLMs

A paper titled "Toward Self-Improvement of LLMs via Imagination Searching and Criticizing" (Tencent AI Lab, April 18, 2024) proposes AlphaLLM, which adapts AlphaGo's self-learning loop for LLMs <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.

### AlphaLLM's Approach
AlphaLLM aims to allow LLMs to refine their outputs and learn from self-assessed rewards, leading to self-improvement <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
*   **Self-play Loop:** Starts with a pre-trained LLM (e.g., Llama 2 70B) and iteratively improves it by generating data and fine-tuning on it <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>.
*   **MCTS Decoding:** Uses MCTS during inference to explore possible token sequences and find the best path <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>.
*   **Option-Level MCTS:** To mitigate the vast token-level search space, AlphaLLM introduces "option-level" MCTS, where actions can be variable-length sequences of tokens (e.g., sentences), determined by a "termination function" <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a>.
*   **Efficient Search Tricks:**
    *   **Importance-based branching:** Allocating more search budget to more important nodes <a class="yt-timestamp" data-t="39:58:00">[39:58:00]</a>.
    *   **Similarity filtering:** Using a heuristic function to avoid exploring redundant sub-trees (similar to RAG embeddings) <a class="yt-timestamp" data-t="40:20:00">[40:20:20]</a>.
    *   **Fast Rollout Policy:** Employing a smaller, faster LLM to project future trajectories for quicker simulation during MCTS <a class="yt-timestamp" data-t="41:34:00">[41:34:00]</a>.
*   **Critics:** AlphaLLM uses three types of critics, initialized from a pre-trained LLM, to provide guidance <a class="yt-timestamp" data-t="48:06:00">[48:06:00]</a>:
    *   **Value Function (V):** An LLM with a small multi-layer perceptron (MLP) head that outputs a single scalar value estimating the discounted sum of future rewards <a class="yt-timestamp" data-t="52:54:00">[52:54:00]</a>.
    *   **Process Reward Model (PRM):** Provides feedback for each step in a "Chain of Thought" <a class="yt-timestamp" data-t="48:59:00">[48:59:00]</a>.
    *   **Outcome Reward Model (OMM):** Provides feedback on the complete trajectory or final answer <a class="yt-timestamp" data-t="48:53:00">[48:53:00]</a>.
*   **Policy Fine-tuning:** Data generated by MCTS (selected trajectories with highest critic scores) is used to fine-tune the LLM policy, pushing gradients to improve its ability to pick high-reward trajectories <a class="yt-timestamp" data-t="54:47:00">[54:47:00]</a>.

### Results and Limitations
AlphaLLM demonstrated significant improvements on mathematical reasoning problems (GSM8K and MATH benchmarks), achieving performance comparable to GPT-4 <a class="yt-timestamp" data-t="01:02:47">[01:02:47]</a>. However, this performance is largely due to the use of MCTS during *inference*, not solely from the LLM itself being "smarter" <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

A key limitation is that the results are only demonstrated for tasks where a clear, unambiguous reward signal exists (e.g., correct/incorrect math answers, valid code) <a class="yt-timestamp" data-t="01:05:54">[01:05:54]</a>. The critics also remain static, meaning their underlying LLM weights are frozen during training <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>. The paper only shows results for two iterations of self-improvement, suggesting that continued improvement might hit a wall, possibly due to training dynamics or overfitting <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>.

## Language Models as Q-Functions

Another paper, "From R to Q*: Your Language Model is Secretly a Q Function" (Stanford University, Chelsea Finn, April 18, 2024), provides theoretical justification for treating LLMs as Q-functions <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>.

*   **DPO and Q-Learning:** This paper argues that [[reinforcement_learning_with_human_feedback_rlhf | Reinforcement Learning with Human Feedback (RLHF)]] methods like Direct Preference Optimization (DPO) are effectively Q-learning algorithms <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>. DPO treats the entire model response as a single "arm" in a contextual bandit problem <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>.
*   **LLMs as Optimal Soft Q Functions:** The paper theoretically demonstrates that an LLM is always the optimal soft Q function for some reward function in a token-level MDP <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>. This means the concepts and mathematics of [[reinforcement_learning_in_ai | reinforcement learning]] can be directly applied to LLMs <a class="yt-timestamp" data-t="01:25:53">[01:25:53]</a>.
*   **Credit Assignment:** DPO is shown to be capable of learning credit assignment, identifying which specific tokens in a sequence contribute to a positive or negative outcome <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>. This is crucial for improving models with sparse rewards or offline data <a class="yt-timestamp" data-t="01:35:12">[01:35:12]</a>.
*   **Discrete vs. Continuous Spaces:** Natural language is a discrete space (limited vocabulary of tokens), which is generally more tractable for RL than continuous action spaces <a class="yt-timestamp" data-t="01:30:43">[01:30:43]</a>. Even continuous domains like robotics can be discretized into "action tokens" <a class="yt-timestamp" data-t="01:31:09">[01:31:09]</a>.
*   **Implications for Robotics and Agent Frameworks:** The ability to use LLMs as Q-functions, perform credit assignment, and leverage offline data has strong implications for [[the_role_of_reinforcement_learning_in_developing_agent_frameworks | developing agent frameworks]] and embodied AI (robotics) <a class="yt-timestamp" data-t="01:13:38">[01:13:38]</a>. If a robot's actions are discretized into tokens, a self-play loop could enable superhuman robotic control, as success/failure is easily verifiable <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>.

## Conclusion

The current state of research suggests that Q* likely refers to the integration of [[agent_loops_and_reinforcement_learning_in_ai | agent loops and reinforcement learning in AI]] and planning algorithms like MCTS with pre-trained large language models <a class="yt-timestamp" data-t="03:00:04">[03:00:04]</a>. While significant progress has been made in domains with clear reward signals (like math and coding), the true "holy grail" for AGI would be applying these [[reinforcement_learning_and_stateoftheart_models | reinforcement learning and state-of-the-art models]] to general natural language reasoning, where reward signals are less obvious <a class="yt-timestamp" data-t="01:43:50">[01:43:50]</a>. The use of search algorithms like MCTS during inference can drastically improve LLM performance, and it is anticipated that future LLM products will incorporate such [[incontext_learning_versus_finetuning_in_ai_development | in-context learning versus fine-tuning in AI development]] techniques in the background <a class="yt-timestamp" data-t="01:58:49">[01:58:49]</a>.