---
title: Selfimprovement and Planning for Large Language Models
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

**Q\***, pronounced "Q-star," is a rumored algorithm or technique that OpenAI purportedly used to achieve a significant improvement in the current state of AI capabilities <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Despite much speculation and mystery surrounding it <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>, many experts, including Yann LeCun, suggest that its core concepts are not entirely new <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

## The Nature of Q\*

Yann LeCun states that nearly every top research lab, including Facebook AI Research (Meta), DeepMind (Google), and OpenAI (Microsoft), is actively working on concepts similar to Q\*, with some having already published related ideas and results <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. He posits that Q\* is likely OpenAI's attempt at "planning" <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>, which broadly falls under the umbrella of reinforcement learning (RL) <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. This means that anyone familiar with reinforcement learning papers from the past decade likely already understands the underlying principles of Q\* <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.

Historically, Yann LeCun used a "cake analogy" to describe the future of Artificial General Intelligence (AGI), suggesting that the majority of the "cake" (intelligence) would come from self-supervised learning, with reinforcement learning being a "little cherry on top" <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. However, he has more recently contradicted this, stating that "agency and planning can't be a wart on top of autoregressive [[large_language_models_llms_and_scaling | LLMs]]; it must be an intrinsic property of the architecture" <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. This recent view contradicts his earlier analogy, where RL was merely a "cherry on top" <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

## Self-Improvement of Large Language Models

Current methods to improve the performance of [[large_language_models_and_optimization | Large Language Models (LLMs)]] primarily involve advanced prompting techniques (like Chain of Thought) and [[finetuning_large_language_models | fine-tuning]] with high-quality supervised data <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. However, these methods are limited by the availability and quality of data <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.

A promising strategy proposes allowing [[large_language_models_and_optimization | LLMs]] to refine their outputs and learn from self-assessed rewards, leading to [[selfimprovement_in_ai_models | self-improvement]] <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. This approach draws inspiration from AlphaGo, a groundbreaking reinforcement learning system <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.

### AlphaLLM: Towards Self-Improvement via Imagination, Searching, and Criticizing

The paper "Toward Self-Improvement of [[large_language_models_llms_and_scaling | LLMs]] via Imagination Searching and Criticizing" (April 18, 2024, by Tencent AI Lab) introduces **AlphaLLM** <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>. AlphaLLM applies AlphaGo's principles to [[large_language_models_and_optimization | language models]] <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.

Key aspects of AlphaLLM include:
*   **Monte Carlo Tree Search (MCTS):** This search algorithm is used to enable models to learn from self-play and achieve or surpass human performance in complex tasks <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. MCTS involves selection, expansion, evaluation, and backpropagation <a class="yt-timestamp" data-t="25:58:00">[25:58:00]</a>.
*   **Challenges with LLMs:**
    *   **Vast Search Spaces:** The action space for [[large_language_models_and_optimization | LLMs]] is enormous due to their large vocabulary (e.g., 30,000 possible tokens for each prediction) <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.
    *   **Lack of Clear Feedback:** Unlike games like Go (where win/loss is clear), natural language tasks lack unambiguous "win or loss" signals for reward <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>.
*   **Option-Level MCTS:** To mitigate the vast search space, AlphaLLM proposes "option-level" MCTS, where actions are not individual tokens but sequences of tokens (like sentences), determined by a "termination function" <a class="yt-timestamp" data-t="33:00:00">[33:00:00]</a>.
*   **Critics:** AlphaLLM utilizes "critics" (value functions) to guide its search, which are also [[large_language_models_and_optimization | language models]] themselves, often initialized from the policy model <a class="yt-timestamp" data-t="30:29:00">[30:29:00]</a>, <a class="yt-timestamp" data-t="35:51:00">[35:51:00]</a>. These include:
    *   **Process Reward Model (PRM):** Provides feedback for each step in a Chain of Thought <a class="yt-timestamp" data-t="48:57:00">[48:57:00]</a>.
    *   **Outcome Reward Model (OMM):** Provides feedback only on the final result of a Chain of Thought <a class="yt-timestamp" data-t="48:53:00">[48:53:00]</a>.
*   **Self-Improvement Loop:** The [[large_language_models_and_optimization | LLM]] synthesizes its own data using MCTS and critics. This data is then used to [[finetuning_large_language_models | fine-tune]] the [[large_language_models_and_optimization | LLM]] (the "policy") through gradient descent, creating a virtuous cycle <a class="yt-timestamp" data-t="54:45:00">[54:45:00]</a>.
*   **Results:** AlphaLLM, starting with a Llama 2 70B model, significantly improved performance on mathematical reasoning benchmarks like GSM8K (from 57% to 92%) and MATH (from 20% to 51%) <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>. This performance, especially with MCTS decoding during inference, becomes comparable to GPT-4 on these tasks <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>, <a class="yt-timestamp" data-t="1:04:14">[1:04:14]</a>.
*   **Limitations:** The improvements are largely due to the MCTS search strategy during inference, rather than making the base model inherently "smarter" in greedy decoding <a class="yt-timestamp" data-t="1:03:15">[1:03:15]</a>. The study only ran for two iterations of self-improvement, raising questions about potential overfitting or hitting performance walls <a class="yt-timestamp" data-t="1:04:47">[1:04:47]</a>.

### From R to Q\*: Your Language Model is Secretly a Q Function

The paper "From R to Q\*: Your Language Model is Secretly a Q Function" (April 18, 2024, by Stanford University, Chelsea Finn et al.) focuses on the theoretical underpinnings, arguing that [[large_language_models_and_optimization | LLMs]] can be understood as Q-functions <a class="yt-timestamp" data-t="1:09:53">[1:09:53]</a>.

Key findings include:
*   **Q-function as Optimal:** In reinforcement learning, Q\* refers to the "optimal Q-function" <a class="yt-timestamp" data-t="1:10:42">[1:10:42]</a>.
*   **DPO and Q-learning:** Direct Preference Optimization (DPO), a method for [[training_and_finetuning_of_language_models_for_code | training and finetuning of language models]] using human feedback, is shown to be equivalent to the Q-learning algorithm when interpreted at the token level <a class="yt-timestamp" data-t="1:20:12">[1:20:12]</a>.
*   **Credit Assignment:** DPO can perform "credit assignment," meaning it can identify which specific tokens within a long response were responsible for a successful outcome, even with sparse (end-of-task) rewards <a class="yt-timestamp" data-t="1:32:59">[1:32:59]</a>. This is crucial for efficient learning.
*   **Discrete vs. Continuous Spaces:** Natural language, being a discrete space (limited set of tokens), allows for effective application of these Q-learning principles, unlike continuous spaces where it's more challenging <a class="yt-timestamp" data-t="1:30:38">[1:30:38]</a>. This also makes it highly applicable to robotic control, where continuous actions can be discretized into tokens <a class="yt-timestamp" data-t="1:31:06">[1:31:06]</a>, <a class="yt-timestamp" data-t="1:41:01">[1:41:01]</a>.
*   **Impact on Robotics/Embodied AI:** The ability to apply these [[advancements_in_language_models | advancements in language models]] to robotics suggests a future where robot policies, trained as [[large_language_models_llms_and_scaling | LLMs]], output "action tokens" and can [[selfimprovement_in_ai_models | self-improve]] in environments where success or failure is clearly observable <a class="yt-timestamp" data-t="1:14:10">[1:14:10]</a>, <a class="yt-timestamp" data-t="1:15:14">[1:15:14]</a>.

## Conclusion

The convergence of reinforcement learning principles, particularly Q-learning and MCTS, with [[llm_large_language_models_development | LLM Large Language Models development]] marks a significant step towards achieving [[selfimprovement_in_ai_models | self-improvement in AI models]] <a class="yt-timestamp" data-t="1:57:07">[1:57:07]</a>. While current demonstrations primarily focus on domains with clear reward signals like math and coding <a class="yt-timestamp" data-t="1:57:14">[1:57:14]</a>, the potential for extending these techniques to more generalized reasoning and natural language tasks is highly anticipated <a class="yt-timestamp" data-t="1:57:31">[1:57:31]</a>. The ability to use LLMs as both policies and value functions, leveraging their pre-trained knowledge, offers a powerful path to creating increasingly capable and autonomous AI <a class="yt-timestamp" data-t="1:56:01">[1:56:01]</a>.