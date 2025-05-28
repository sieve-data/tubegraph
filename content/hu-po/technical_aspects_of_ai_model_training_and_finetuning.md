---
title: Technical aspects of AI model training and finetuning
videoId: oQqOiwUhJkA
---

From: [[hu-po]] <br/> 

OpenAI's latest release, internally referred to as `strawberry` (or O1), has sparked considerable debate within the AI community due to its performance on benchmarks <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. While some criticize it as "glorified Chain of Thought," others hail it as a "new scaling paradigm" <a class="yt-timestamp" data-t="02:59:52">[02:59:52]</a>. The core of this discussion revolves around advanced [[training_and_finetuning_processes_for_ai_models | training and finetuning processes for AI models]] and their implications for model capabilities.

## Chain of Thought and Test-Time Compute

Chain of Thought (CoT) prompting is a technique that elicits complex multi-step reasoning by having a model generate step-by-step answers <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>, <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>, <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. It has been documented in research literature for years, with papers from January 2023 already showing its effectiveness <a class="yt-timestamp" data-t="01:06:22">[01:06:22]</a>, <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>.

CoT falls under the umbrella of **test-time computation**, which refers to compute used during the evaluation or inference phase of a model <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>, <a class="yt-timestamp" data-t="01:23:26">[01:23:26]</a>, <a class="yt-timestamp" data-t="01:41:14">[01:41:14]</a>. Instead of simply generating the next token in a single pass (zero-shot), test-time compute allows the model a budget to internally "think" or perform multiple inferences to arrive at a better answer <a class="yt-timestamp" data-t="01:41:14">[01:41:14]</a>.

> [!NOTE] Internal Reasoning Tokens
> OpenAI's O1 series can generate total tokens that exceed the number visible to the user due to "internal reasoning tokens" <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. These tokens represent the model's internal thought process, which is hidden from the user <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. This allows the model to perform a more complex thought process without exposing the intermediate steps <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.

Special tokens (e.g., `[start_tool_use]`, `[end_tool_use]`) could potentially be used to represent abstract actions within this internal reasoning, reducing context length and allowing for more reasoning within the context window <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

## Reward Models and Monte Carlo Tree Search (MCTS)

A key component in leveraging test-time compute is the **process-based reward model (PRM)** <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>. Unlike traditional reward models that evaluate a single outcome, a PRM evaluates the entire Chain of Thought, or "process," to assign credit to each step leading to a final answer <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

This process is often combined with search methods like **Monte Carlo Tree Search (MCTS)** <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. MCTS involves building a tree of possible actions and their outcomes, running simulations (rollouts) to explore different paths, and then using a reward model to evaluate the best paths <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
*   **Best of N**: The simplest form, where the LLM produces N answers, and the reward model picks the best one <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
*   **Beam Search / Look Ahead Search**: More complex methods that involve running the verifier on intermediate parts of the process, picking paths, and continuing to search <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>, <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

These search methods significantly increase the computational cost at inference time, as each circle or purple square in a search tree represents an inference <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. However, research indicates that a small model with test-time compute can outperform a 14x larger model that does not use it <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

## The Shift from RLF to "Real RL" in Training

Historically, the "post-training" phase for large language models (LLMs) primarily involved Reinforcement Learning from Human Feedback (RLHF) or instruction tuning <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. RLHF relies on human labelers to compare and prefer different model outputs, training a reward model to imitate this human "vibe check" <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>, <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. While useful for alignment, this approach doesn't inherently make models better at complex reasoning <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>, <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

The emerging paradigm for [[finetuning_and_training_curriculums_in_ai_models | finetuning and training curriculums in AI models]] involves "real RL," akin to how AlphaGo Zero was trained <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. AlphaGo Zero played millions of simulated games against itself, assigning rewards based on winning outcomes, and then used those rewards to push gradients back into the model, improving its policy <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>, <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>, <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

> [!INFO] AlphaGo Zero's Cost
> AlphaGo Zero cost approximately $35 million in computing power, largely spent on running millions of simulated games <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

This "real RL" approach involves:
1.  **Generating high-quality training data**: Using MCTS and reward models to generate synthetic data through self-play simulations and reflection <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>, <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. This is distinct from RLHF's contextual bandit approach <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
2.  **[[finetuning_machine_learning_models | Finetuning machine learning models]] on this data**: Pushing gradients from these self-generated, high-value reasoning traces directly into the model <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>, <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.

This process allows the model to become inherently better at producing effective Chains of Thought, rather than merely performing them at inference time <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>, <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

## Implications for AI Model Scaling and Convergence

This new approach signifies a merging of two major AI research branches:
1.  **Massive-scale next-token prediction**: The traditional LLM [[pretraining_and_finetuning_in_ai_models | pretraining and finetuning in AI models]] on vast datasets (the "gray bar" of compute) <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>, <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.
2.  **Reinforcement Learning and self-play**: The DeepMind approach of training agents through self-improvement in defined environments (the "green bar" of compute) <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>, <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

The O1 model is considered the first production-grade implementation of this combination <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

> [!CAUTION] The "Bitter Lesson" vs. Complexity
> While the "bitter lesson" suggests that simpler models with more compute eventually win out over overly complicated systems, day-to-day incentives often lead to accumulating complexity <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>. This new paradigm with RL-enhanced reasoning introduces additional complexity but currently yields significant performance gains <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

### Superhuman Reasoning and Transfer Learning

The ability to use "real RL" in language models, particularly for tasks where a definitive reward signal is available (like coding or mathematics), offers a path to [[selfimprovement_in_ai_models | selfImprovement in AI Models]] and superhuman reasoning <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>, <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. For example, a model trained to be superhuman at math and coding might see transfer effects, improving its performance in seemingly unrelated fields like poetry or general writing <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. This highlights the [[implications_of_ai_model_scaling_and_convergence | implications of AI model scaling and convergence]].

### Model Size and Cost

A key advantage of this approach is the potential to achieve high performance with smaller models <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. A small model with sophisticated internal reasoning can outperform a much larger model <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. This is crucial for financial viability, as running large models for extensive internal reasoning would be prohibitively expensive <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

The total cost of these models will increase significantly due to the massive investment in the RL phase, potentially rivaling the cost of initial pre-training <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This could also lead to specialization in hardware and data centers, with different types of compute optimized for pre-training versus RL-based experience collection <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

### Secrecy and Competition

OpenAI's decision to hide the internal Chain of Thought from users is contentious <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. One theory is that this prevents others from easily [[finetuning_language_models_for_specific_tasks | finetuning language models for specific tasks]] by distilling OpenAI's proprietary Chain of Thought data <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>, <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. Without access to these internal steps, it's harder for competitors to replicate the model's reasoning capabilities <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

Another reason for hiding the Chain of Thought might be to allow the internal model to remain "un-lobotomized" or less aligned with human preferences, while a post-processing filter ensures the final output is safe and palatable <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. This contrasts with traditional RLHF, which can make models "stupider" by aligning them too strictly <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

## Challenges and Future Outlook

While powerful, this RL-driven approach has limitations:
*   **Reward Signal Availability**: It works best in environments where a clear, automated reward signal is available, such as competitive games, mathematics, or code execution (where correctness can be objectively verified) <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>, <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>. It's less applicable to subjective domains like philosophy, literature, or general writing <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
*   **Cost of Compute**: Even with smaller models, the hundreds of millions of dollars required for this type of compute present [[challenges_and_methodologies_in_ai_training | challenges and methodologies in AI training]] for smaller companies <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **Interpretability**: Hiding the internal reasoning limits interpretability and control for users <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

Despite these challenges, the ability to train models for superhuman reasoning through self-play marks a significant step towards Artificial Superintelligence (ASI) <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. The game has been "totally redefined" by this combination of pre-training scale and sophisticated RL-based post-training <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>, showcasing the evolving [[the_role_of_data_quality_and_training_scale_in_ai_models | role of data quality and training scale in AI models]].