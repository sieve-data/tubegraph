---
title: SelfImprovement in AI Models
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

The concept of [[selfimproving_ai_through_reinforcement_learning_and_reasoning | self-improving AI models]] has gained significant attention, particularly with rumors surrounding Open AI's supposed "Q\* (Q-Star)" algorithm <a class="yt-timestamp" data-t="03:00:04">[03:00:04]</a>. Q\* is rumored to be a method that led to a "step function improvement" in the current state of AI <a class="yt-timestamp" data-t="03:00:04">[03:00:04]</a>.

## What is Q\*?
Q\* is a rumored algorithm from Open AI, shrouded in mystery <a class="yt-timestamp" data-t="03:28:29">[03:28:29]</a>. While the exact nature is unknown, the consensus among experts like Yann LeCun is that it involves reinforcement learning and planning, concepts that have existed for decades <a class="yt-timestamp" data-t="04:07:07">[04:07:07]</a> <a class="yt-timestamp" data-t="04:14:15">[04:14:15]</a>. The "Q" in Q\* most likely refers to the Q-function, a core concept in Q-learning in reinforcement learning <a class="yt-timestamp" data-t="01:10:16">[01:10:16]</a> <a class="yt-timestamp" data-t="01:10:46">[01:10:46]</a>. The "star" (Q\*) potentially signifies an *optimal* Q-function <a class="yt-timestamp" data-t="01:10:46">[01:10:46]</a>, or perhaps a reference to the A\* search algorithm <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>.

### Yann LeCun's "Cake Analogy"
Yann LeCun previously described [[future_directions_and_potential_breakthroughs_in_ai_models | Artificial General Intelligence (AGI)]] as a "cake," where the majority (volume) is composed of self-supervised learning, and [[selfimproving_ai_through_reinforcement_learning_and_reasoning | reinforcement learning or planning]] (the Q\* component) is merely a "little cherry on top" <a class="yt-timestamp" data-t="05:14:18">[05:14:18]</a> <a class="yt-timestamp" data-t="05:27:07">[05:27:07]</a>. This contrasts with a more recent tweet where he stated that "agency and planning can't be a wart on top of auto-regressive LLMs, it must be an intrinsic property of the architecture" <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

## Self-Improvement Mechanisms
Current large language models (LLMs) are often improved using advanced prompting techniques and [[finetuning_and_training_curriculums_in_ai_models | fine-tuning with high-quality data]] <a class="yt-timestamp" data-t="09:16:05">[09:16:05]</a>. However, these methods are limited by data availability and quality <a class="yt-timestamp" data-t="09:56:06">[09:56:06]</a>. [[selfimproving_ai_through_reinforcement_learning_and_reasoning | Self-improvement]] aims to allow LLMs to refine their outputs and learn from self-assessed rewards <a class="yt-timestamp" data-t="10:07:07">[10:07:07]</a>.

### AlphaLLM: Imagination, Searching, and Criticizing
The paper "Toward Self-Improvement of LLMs via Imagination Searching and Criticizing" by Tencent AI Lab, released April 18, 2024, proposes a strategy that enables LLMs to improve themselves <a class="yt-timestamp" data-t="06:37:07">[06:37:07]</a>. This approach, named AlphaLLM, applies principles from AlphaGo to language models <a class="yt-timestamp" data-t="10:27:07">[10:27:07]</a>.

#### Inspiration from AlphaGo
AlphaGo achieved superhuman performance in the game of Go by combining imitation learning on expert data with [[selfimproving_ai_through_reinforcement_learning_and_reasoning | reinforcement learning]] on self-play <a class="yt-timestamp" data-t="12:56:06">[12:56:06]</a>. Self-play generates novel tactics by exploring potential moves through statistical sampling of a large search space <a class="yt-timestamp" data-t="13:52:02">[13:52:02]</a>.

#### Challenges in Applying to LLMs
Applying this to LLMs presents unique [[challenges_and_improvements_in_animated_ai_models | challenges]]:
*   **Vast Search Space:** Unlike discrete board games like Tic-Tac-Toe or Go, language models have a massive action space (e.g., 30,000 possible tokens at each step), making tree search incredibly complex <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a> <a class="yt-timestamp" data-t="22:28:00">[22:28:00]</a>.
*   **Data Scarcity:** Lack of expert-level language data comparable to millions of Go games <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.
*   **Subjective Feedback:** Unlike a clear win/loss in games, evaluating language outputs is often fuzzy and lacks unequivocal learning signals <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.

#### AlphaLLM's Solutions and Components
AlphaLLM features two main components:
1.  **Imagination Component:** Synthesizes its own data for improvement, which is then used to push gradients back into the LLM <a class="yt-timestamp" data-t="31:05:00">[31:05:00]</a>.
2.  **Efficient Search Component (Option-Level MCTS):**
    *   **Monte Carlo Tree Search (MCTS):** A sampling-based search algorithm that explores a tree of possible actions and states through selection, expansion, evaluation, and backpropagation <a class="yt-timestamp" data-t="25:58:00">[25:58:00]</a> <a class="yt-timestamp" data-t="26:02:00">[26:02:00]</a>.
    *   **Option-Level Search:** Instead of token-level or sentence-level search, AlphaLLM introduces "option-level" search, where actions consist of variable-length sequences of tokens, determined by a "termination function" <a class="yt-timestamp" data-t="34:08:00">[34:08:00]</a> <a class="yt-timestamp" data-t="34:40:00">[34:40:00]</a>. This mitigates the huge search space of token-level MCTS <a class="yt-timestamp" data-t="33:11:00">[33:11:00]</a>.
    *   **Filtering:** Employs heuristics to filter out similar options, preventing redundant sub-trees in the search space <a class="yt-timestamp" data-t="40:26:00">[40:26:00]</a>.
    *   **Fast Rollout Policy:** Uses a smaller, specialized language model for rapid simulation of future trajectories within the MCTS tree, improving efficiency <a class="yt-timestamp" data-t="41:51:00">[41:51:00]</a>.

#### Critics and Value Functions
AlphaLLM utilizes three types of critics (value functions) to guide the search:
*   **Process Reward Model (PRM):** Provides feedback for each step in a Chain of Thought <a class="yt-timestamp" data-t="49:00:00">[49:00:00]</a>.
*   **Outcome Reward Model (OMM):** Provides feedback only on the final result of the model's Chain of Thought <a class="yt-timestamp" data-t="49:51:00">[49:51:00]</a>.
*   **Value Function:** Estimates the expected cumulative reward for a given state, initialized from a [[pretraining_and_finetuning_in_ai_models | pre-trained language model]] with a small Multi-Layer Perceptron (MLP) on top <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a> <a class="yt-timestamp" data-t="53:03:00">[53:03:00]</a>.

#### Policy Self-Improvement Loop
The system continuously generates data using MCTS guided by critics, selects high-quality trajectories, and then [[training_and_finetuning_processes_for_ai_models | fine-tunes the policy]] (the language model) on this collected data <a class="yt-timestamp" data-t="54:47:00">[54:47:00]</a>. This creates a self-play virtuous cycle, where the model generates increasingly higher-quality data over time, potentially leading to superhuman performance <a class="yt-timestamp" data-t="55:47:00">[55:47:00]</a> <a class="yt-timestamp" data-t="56:02:00">[56:02:00]</a>.

#### Results and Limitations
AlphaLLM, starting with a Llama 2 70B model, demonstrated significant improvements on mathematical reasoning benchmarks like GSM8K and MATH, achieving performance comparable to GPT-4 *when MCTS decoding is used during inference* <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a> <a class="yt-timestamp" data-t="01:04:36">[01:04:36]</a>. The model itself, without MCTS decoding, was not significantly smarter <a class="yt-timestamp" data-t="01:03:15">[01:03:15]</a> <a class="yt-timestamp" data-t="01:04:17">[01:04:17]</a>.

A key limitation noted in the paper is that the self-improvement loop was only run for two iterations <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>. This suggests potential issues, such as overfitting or a "wall" in performance, if run for more iterations <a class="yt-timestamp" data-t="01:05:33">[01:05:33]</a>. Another limitation is that the critic models remain static (their base LLM weights are frozen during gradient updates) <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>.

### "From R to Q-Star: Your Language Model is Secretly a Q Function"
This Stanford University paper, also released on April 18, 2024, provides a theoretical framework. It argues that Direct Preference Optimization (DPO) and token-level Markov Decision Processes (MDPs) in LLMs are effectively a form of Q-learning <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>. It demonstrates that a language model can be considered an optimal soft Q-function for certain reward functions in a token MDP <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>.

#### Key Concepts
*   **LLMs as Q-functions:** The paper fundamentally argues that language models are inherently Q-functions, and much of the terminology difference between LLM and RL research is superficial <a class="yt-timestamp" data-t="01:23:12">[01:23:12]</a> <a class="yt-timestamp" data-t="01:37:50">[01:37:50]</a>.
*   **Credit Assignment Problem:** This is the challenge of determining which specific actions or tokens contributed most to a successful outcome in a long sequence <a class="yt-timestamp" data-t="01:33:18">[01:33:18]</a>. The paper shows that DPO can learn to do credit assignment directly from feedback data <a class="yt-timestamp" data-t="01:38:50">[01:38:50]</a>.
*   **Discrete vs. Continuous Spaces:** Natural language is a discrete space (limited set of tokens), which is generally more amenable to these RL techniques than continuous spaces <a class="yt-timestamp" data-t="01:30:43">[01:30:43]</a>.
*   **Offline Reinforcement Learning:** The ability to effectively learn from large amounts of offline data (not collected by the current policy) combined with credit assignment is crucial for scaling [[selfimproving_ai_through_reinforcement_learning_and_reasoning | self-improvement]] <a class="yt-timestamp" data-t="01:35:12">[01:35:12]</a>.

## Implications and Future Directions
The advancements in [[selfimproving_ai_through_reinforcement_learning_and_reasoning | self-improvement]] techniques, particularly those involving MCTS and treating LLMs as Q-functions, have profound implications for the [[future_directions_and_potential_breakthroughs_in_ai_models | future of AI models]]:

*   **Beyond Math and Coding:** While current demonstrations of superhuman performance are in domains with clear, objective feedback (like math, coding, and robotics), the ultimate goal is to extend this to general natural language reasoning <a class="yt-timestamp" data-t="01:44:51">[01:44:51]</a>.
*   **Embodied AI and Robotics:** The principles of [[selfimproving_ai_through_reinforcement_learning_and_reasoning | self-improvement]] and treating LLMs as policies that output action tokens are directly applicable to robotics. In robotics, success or failure (e.g., grasping an object) provides clear reward signals, making these methods highly effective <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a> <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>. This is a significant factor in leading top researchers from places like Google to found humanoid robot companies <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>.
*   **Inference-Time Search:** The dramatic performance improvements seen with MCTS decoding during inference suggest that future LLM products will likely perform complex tree searches in the background to generate higher-quality outputs <a class="yt-timestamp" data-t="01:58:54">[01:58:54]</a>.
*   **Improved Generation:** These methods can also be used to improve text generation or refine prompts for image generation by evaluating trajectories of different prompts <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>.