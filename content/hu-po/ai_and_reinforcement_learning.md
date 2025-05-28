---
title: AI and Reinforcement Learning
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

[[AI and Reinforcement Learning | Q*]] (Q-star) is rumored to be a specific method or algorithm used by OpenAI that led to a significant step-function improvement in the current state of [[discussion_on_reinforcement_learning_and_ai | AI]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. While shrouded in mystery and hype, the core concept of [[AI and Reinforcement Learning | Q*]] is understood by many in the field <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.

## Understanding Q*

According to Yann LeCun, a prominent AI researcher, virtually every top lab—including Facebook AI Research (Meta), DeepMind (Google), and OpenAI (Microsoft)—is working on similar ideas, with some having already published results <a class="yt-timestamp" data-t="00:3:49">[00:3:49]</a>. LeCun suggests that [[AI and Reinforcement Learning | Q*]] is likely OpenAI's attempt at planning within [[discussion_on_reinforcement_learning_and_ai | AI]] systems <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This involves concepts that have been explored in [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] and planning for decades <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### The "Cherry on Top" Analogy
Yann LeCun previously used a "cake analogy" to describe the composition of [[discussion_on_reinforcement_learning_and_ai | AGI]] (Artificial General Intelligence) <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. In this analogy, the majority of the "cake" (by volume) would be composed of self-supervised learning, with the [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] or planning component—the "[[AI and Reinforcement Learning | Q*]] component"—being merely a "little cherry on top" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This suggests that [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] is a critical, albeit smaller, part of achieving [[discussion_on_reinforcement_learning_and_ai | AGI]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

However, LeCun later contradicted this by tweeting that "agency and planning can't be a wart on top of auto-regressive LLMs, it must be an intrinsic property of the architecture" <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Auto-regressive LLMs are trained in a self-supervised way, primarily through next-token prediction on large internet text datasets <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### The Q-Function Connection
The "Q" in [[AI and Reinforcement Learning | Q*]] unmistakably refers to the Q-function in [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] <a class="yt-timestamp" data-t="01:10:14">[01:10:14]</a>. The "star" in Q* is often interpreted as signifying an "optimal Q-function," representing a theoretical God-level Q-function that a system aims to achieve <a class="yt-timestamp" data-t="01:10:46">[01:10:46]</a>. Alternatively, it could refer to A* (A-star), a popular search algorithm <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>.

## Applying Reinforcement Learning to LLMs

Recent research demonstrates how [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] and planning can be applied to Large Language Models (LLMs) for self-improvement.

### Toward Self-Improvement of LLMs via Imagination Searching and Criticizing (Tencent AI Lab)
Published April 18, 2024, this paper introduces "AlphaLLM," which applies the principles of AlphaGo to language models <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>. AlphaLLM aims to refine LLM outputs and learn from self-assessed rewards, leading to self-improvement <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

The methodology involves:
*   **Monte Carlo Tree Search (MCTS):** AlphaLLM leverages MCTS to explore potential language responses <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. MCTS is a sampling-based search algorithm with four phases: selection, expansion, evaluation, and back-propagation <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
*   **Self-Play:** Similar to AlphaGo, AlphaLLM employs [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] on self-play to generate novel tactics that surpass human capabilities <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. This allows the LLM to synthesize its own data, which is then used to push gradients back into the LLM, improving its performance <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.
*   **Critics (Reward Models):** To guide the search, AlphaLLM uses three types of critics:
    *   **Process Reward Model (PRM):** Provides feedback for each step in a Chain of Thought <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>.
    *   **Outcome Reward Model (OMM):** Provides feedback only for the final result of the Chain of Thought <a class="yt-timestamp" data-t="00:48:53">[00:48:53]</a>.
    *   **Value Function:** A neural network, often initialized from the policy (the LLM itself), that estimates the discounted sum of future rewards for a given state and action <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>.
*   **Option-Level MCTS:** To mitigate the vast search space of language (where each token is an action, resulting in ~30,000 possible tokens), AlphaLLM introduces "option-level" search <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. This allows actions to be variable-length sequences of tokens, determined by a "termination function" <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. This approach makes the search more efficient, though it increases the complexity of the action space <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

#### Results and Limitations
AlphaLLM, starting from a Llama 2 70B model, demonstrated significant performance improvements, from 57% to 92% on GSM8K and 20% to 51% on MATH benchmarks <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. This performance is comparable to GPT-4 *specifically on math problems* <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a>.

However, the improvements are primarily seen when using MCTS during inference, not in the base model's greedy decoding capabilities <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. The paper also only shows results for two iterations of self-improvement, suggesting potential challenges or limitations in scaling the virtuous cycle of [[reinforcement_learning_and_selfplay_in_ai_development | self-play]] <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. The critics (reward models) in this framework remain static, meaning their underlying LLM weights are effectively frozen during training, which could limit overall training dynamics <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>.

### From R to Q*: Your Language Model is Secretly a Q Function (Stanford University)
Also published on April 18, 2024, this theoretical paper argues that a language model is inherently a Q-function <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>. It draws connections between Direct Preference Optimization (DPO) and token-level Markov Decision Processes (MDPs) in [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>.

Key points include:
*   **LLMs as Policies:** A language model can be thought of as a policy executing a Markov Decision Process, where states are sequences of input tokens, and actions are the next tokens to be generated <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>.
*   **DPO and Q-Learning:** The paper theoretically shows that DPO, a method for training reward models, is effectively the Q-learning algorithm and satisfies the Bellman equation, allowing for "credit assignment" at the token level <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>.
*   **Search Algorithms Improve Performance:** Simple beam search, a type of graph search algorithm similar to MCTS, yields meaningful improvement over base DPO policies <a class="yt-timestamp" data-t="01:20:33">[01:20:33]</a>. This corroborates the findings from the Tencent paper regarding the benefits of guided decoding.
*   **Credit Assignment:** The ability of LLMs to identify erroneous statements and perform "credit assignment" (determining which tokens in a trajectory contribute to a positive or negative outcome) is a promising sign for combinatorial generalization from offline data <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>.

### Challenges and Advancements in AI Research
The primary challenge in applying [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] to language models is the vastness of the action space (e.g., 30,000 possible tokens at each step) and the subjective nature of feedback <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. Unlike games like Go, where the outcome (win/loss) provides clear and unambiguous feedback, natural language tasks lack such a distinct reward signal <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

However, for domains like mathematics and coding, where answers can be definitively correct or wrong, self-play loops can be effectively implemented <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>. The big question remains: can this self-play loop be extended to general natural language and logical reasoning, where "correctness" is more nuanced <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>?

[[Stateoftheart in Reinforcement Learning | Ilia Sutskever]] (co-founder of OpenAI) is speculated by some to have potentially found a way to use a pre-trained language model as a Q-function in a more generic set of tasks beyond just math and programming, which would explain the hype around [[AI and Reinforcement Learning | Q*]] <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>.

## Implications for Embodied AI and Robotics
The concepts discussed, particularly the use of LLMs for policies and value functions, are directly applicable to [[applications_in_machine_learning_and_reinforcement_learning | robotics]] and [[selfimproving_ai_through_reinforcement_learning_and_reasoning | embodied AI]] <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a>. In robotics, a clear win/loss signal (e.g., whether an object was grasped successfully) provides high-quality reward signals <a class="yt-timestamp" data-t="01:15:24">[01:15:24]</a>. This enables the creation of [[selfimproving_ai_through_reinforcement_learning_and_reasoning | self-play]] loops with robot policies that output action tokens, potentially leading to human-level and [[selfimproving_ai_through_reinforcement_learning_and_reasoning | superhuman performance]] in embodied [[discussion_on_reinforcement_learning_and_ai | AGI]] <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>.

The fact that prominent researchers from Google's robotics division, like Chelsea Finn and Sergey Levine, are leaving to start humanoid robot companies, suggests a strong belief in the near-term potential of these [[applications_in_machine_learning_and_reinforcement_learning | applications in machine learning and reinforcement learning]] <a class="yt-timestamp" data-t="01:15:52">[01:15:52]</a>.

## Conclusion

The synergy between [[reinforcement_learning_and_selfplay_in_ai_development | reinforcement learning]] and LLMs is rapidly advancing. The core idea is that pre-trained language models can serve as both policies (generating responses) and critics (evaluating responses or actions). By combining these with search algorithms like MCTS and [[reinforcement_learning_and_selfplay_in_ai_development | self-play]] loops, LLMs can undergo self-improvement, especially in domains with objective feedback like math and coding <a class="yt-timestamp" data-t="01:57:10">[01:57:10]</a>. This approach enables LLMs to generate higher-quality data than human expert data, potentially leading to [[selfimproving_ai_through_reinforcement_learning_and_reasoning | superhuman performance]] <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>. While [[AI and Reinforcement Learning | Q*]] remains speculative, it likely represents an attempt to harness these principles for a new leap in [[discussion_on_reinforcement_learning_and_ai | AI]] capabilities <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. It is anticipated that future LLM products will incorporate such [[taskspecific_agent_loops_and_reinforcement_learning | task-specific agent loops and reinforcement learning]] techniques during inference to achieve superior performance <a class="yt-timestamp" data-t="01:58:52">[01:58:52]</a>.