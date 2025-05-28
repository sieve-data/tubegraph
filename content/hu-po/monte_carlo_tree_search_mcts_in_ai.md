---
title: Monte Carlo Tree Search MCTS in AI
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

Monte Carlo Tree Search (MCTS) is a search algorithm that has enabled AI models to achieve human parity or even surpass human performance in complex tasks, such as the game of Go <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>, and is now being applied to [[Foundation models in AI | large language models]] (LLMs) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. It is a sampling-based search algorithm <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a> that navigates vast action spaces to find optimal strategies <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.

## Core Concepts and Phases

MCTS operates through four main phases <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>:
1.  **Selection**: Recursively selecting child nodes from the root <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>. This involves choosing the most promising path in the tree built so far.
2.  **Expansion**: Adding new nodes to the tree by simulating future trajectories <a class="yt-timestamp" data-t="00:37:11">[00:37:11]</a>. A "fast rollout policy" (often a smaller, specialized language model) can be used for rapid simulation during this phase to avoid computational demands <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a>.
3.  **Evaluation**: Estimating the value of each newly expanded node using a "value function" <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>. This function provides a numerical score indicating how good a specific state or trajectory is <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.
4.  **Backpropagation**: Updating the average value of the newly generated node and all its ancestor nodes using the scaled reward from the evaluation steps <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. This pushes gradients back into the policy to improve its action selection <a class="yt-timestamp" data-t="00:37:47">[00:37:47]</a>.

## Applications and Benefits

### AlphaGo and Self-Play
MCTS, combined with [[AI and Reinforcement Learning | reinforcement learning]] on self-play, was the key to [[Motion modeling in AI | AlphaGo]]'s success in mastering the game of Go <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Self-play fosters the emergence of novel tactics that surpass human capabilities because the model generates data that is of higher quality than expert human games <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. In games like Go, the direct and accurate feedback of a win or a loss offers a clear and unequivocal learning signal for the model <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

### MCTS in Language Models
Recent research, such as the "AlphaLLM" paper "Toward Self-Improvement of LLMs via Imagination, Searching and Criticizing" <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, explores applying MCTS to LLMs for self-improvement. By adding MCTS as a "cherry on top" to [[Foundation models in AI | self-supervised pre-trained LLMs]] like Llama 2 70B, they achieved performance comparable to GPT-4 on math problems (GSM8K and Math datasets) <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a>. This self-improvement loop allows LLMs to refine their outputs and learn from self-assessed rewards <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Challenges and Adaptations for Language Models

Applying MCTS to natural language presents unique challenges compared to games like Go <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>:

*   **Vast Search Space**: In language models, each token prediction can involve a vocabulary of 30,000 possible tokens, leading to an exponentially expanding search space <a class="yt-timestamp" data-t="00:32:22">[00:32:22]</a>.
*   **Subjective Feedback**: Unlike games with clear win/loss conditions, evaluating the quality of natural language responses is fuzzy and lacks an unambiguous reward signal <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
*   **Data Scarcity**: There isn't an abundance of "expert games" for language tasks as there are for Go <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.

To mitigate these challenges, AlphaLLM introduces several adaptations:

*   **Option-Level MCTS**: Instead of token-level search (which is too slow), they propose a sentence-level or "option-level" search, where actions consist of sequences of tokens rather than individual ones <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. A "termination function" decides the variable length of these token sequences <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.
*   **Hierarchical Search**: Allocating a larger "child budget" to nodes of higher importance <a class="yt-timestamp" data-t="00:39:58">[00:39:58]</a>.
*   **Similarity Filtering**: Using a heuristic function to measure the similarity between generated options and filter out redundant sub-trees, ensuring efficient exploration of the search space <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
*   **Pre-trained Models as Critics**: The value function (critic) is often initialized from a pre-trained language model, leveraging its general knowledge <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. These critics guide the search by predicting the value or "goodness" of specific trajectories <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
    *   **Process Reward Models (PRM)**: Provide feedback for each step in a Chain of Thought <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>.
    *   **Outcome Reward Models (OMM)**: Provide feedback only on the final result of a Chain of Thought <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>.

## MCTS and Q-Learning

The paper "From R to Q\* Your Language Model is Secretly a Q Function" <a class="yt-timestamp" data-t="01:09:53">[01:09:53]</a> argues that standard reinforcement learning techniques like DPO (Direct Preference Optimization) are inherently Q-learning algorithms. This implies that an LLM can be interpreted as an optimal soft Q-function for some reward function in a token-level Markov Decision Process (MDP) <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>. The *Q*\* (Q-star) in the paper title refers to the optimal Q function <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>, suggesting that LLMs, when framed correctly, can naturally estimate optimal values for actions in specific states.

This theoretical connection allows for the direct application of search algorithms like MCTS, as their effectiveness (e.g., beam search yielding meaningful improvements) aligns with the idea that LLMs are implicitly Q-functions <a class="yt-timestamp" data-t="01:20:37">[01:20:37]</a>. This connection is particularly strong in discrete action spaces like natural language or discretized robotic control <a class="yt-timestamp" data-t="01:31:06">[01:31:06]</a>.

## Limitations and Future Potential

While MCTS demonstrates significant improvements, particularly when combined with inference-time search, the language model itself isn't necessarily "smarter" in greedy decoding <a class="yt-timestamp" data-t="01:03:20">[01:03:20]</a>. This suggests that the gains come from the search process augmenting the model's output rather than a fundamental change in the model's core intelligence <a class="yt-timestamp" data-t="01:06:27">[01:06:27]</a>.

Furthermore, self-improvement loops have shown limited iterations (e.g., only two iterations in AlphaLLM) <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. This might indicate that the training dynamics run into walls, possibly due to static critic models or challenges in continually generating higher-quality data beyond certain tasks like math or coding, where a clear reward signal exists <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>.

However, the ability of DPO to learn "credit assignment" – knowing which specific parts of a long sequence contributed to a successful outcome – is a promising sign for future [[AI and Reinforcement Learning | reinforcement learning]] applications, especially for [[AI and Reinforcement Learning | offline reinforcement learning]] and [[applications_in_machine_learning_and_reinforcement_learning | robotics]] <a class="yt-timestamp" data-t="01:33:59">[01:33:59]</a>. If LLMs can learn optimal exploration behavior in tasks like web navigation or embodied control, this combination of [[Foundation models in AI | LLMs]] with MCTS and [[AI and Reinforcement Learning | Q-learning]] could lead to superhuman [[AI and Reinforcement Learning | AGI]] <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>. This concept aligns with the idea of [[Reinforcement learning and selfplay in AI development | self-play]] leading to increasingly capable AI systems <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>.