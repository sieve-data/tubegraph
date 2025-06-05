---
title: Large language models and selfimprovement
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

The field of AI agents, extending beyond simple chatbots like ChatGPT, is poised for significant progress, with figures such as Bill Gates and Andrew Ng highlighting its potential for a computing revolution <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Sam Altman even predicts 2025 will be "the year of agent" <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Despite some skepticism regarding the planning capabilities of [[ai_models_and_training_methods | large language models]] (LLMs) and the practical limitations of early attempts like AutoGPT <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, the core concept of AI agents, enabled by LLMs, is gaining traction.

## What are AI Agents?

AI agents are not a new concept <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. They are defined by a process that involves interacting with an environment through actuations of actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The process typically involves several steps:

1.  **Perception**: Agents must understand their environment by sensing information from various modalities like text, images, audio, video, and touch <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Reasoning/Planning**: After perceiving information, agents process it to understand how to complete tasks, break them down into individual steps, and decide on appropriate tools or actions <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This often involves "chain of thought" reasoning, powered by LLMs <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Reflection (Meta-reasoning)**: Agents can perform [[meta_prompting_with_language_models | meta-reasoning]] steps by reflecting on executed actions, asking if the right choice was made, and adjusting if necessary <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Action**: This involves any performance that interacts with the environment, such as talking to humans or moving objects <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Levels of Autonomy

The deployment of agents can be understood through different levels of autonomy, similar to self-driving cars <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:

*   **Level 1 (Chatbot)**: Simple information retrieval (e.g., 2017 chatbots) <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2 (Agent Assist)**: LLMs generate suggested responses for human approval (e.g., customer service) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3 (Agent as a Service)**: LLMs automate AI workflows for specific services (e.g., meeting bookings, writing job descriptions) <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4 (Autonomous Agents)**: Agents can delegate and perform multiple, inter-connected tasks, sharing knowledge and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5 (Jarvis-like)**: Full trust in agents to perform all tasks, including security measures, on behalf of users <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

While self-driving cars are high-risk agents where errors are critical <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, AI agents can be categorized by risk level. Low-risk tasks like filing reimbursements can start with human supervision and gradually build trust, while customer-facing tasks are typically higher risk <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Improving LLM Reasoning and Reflection

Key areas for improving LLMs for agent tasks include enhancing their reasoning and reflection abilities, eliciting better behaviors from existing models, and learning from past examples to optimize LLMs for agent tasks <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Self-Refinement via Reflection

For mathematical reasoning tasks, two common methods using LLMs are:

*   **Few-shot prompting**: Providing examples of similar problems and their answers as context for the LLM <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Chain of thought**: Instructing the model to "think step by step," allowing it to reason over tokens to reach a correct answer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

A more recent method combines these by providing the model with a problem, asking it to solve it step-by-step, then providing the initial answer and prompting the LLM to generate feedback (reflection) on its correctness <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This process of "self-refined" or "self-improvement" involves combining the feedback with the original question to prompt the model again, allowing it to update its answer and internal processes <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This iterative process can be repeated until a correct answer is reached <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

#### Challenges with Smaller LLMs

While effective for larger models (e.g., >7 billion or 13 billion parameters), this self-improvement process poses [[challenges_and_solutions_in_using_large_language_models | challenges for smaller LLMs]] like LLaMA 7 billion <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. The feedback generated by smaller models often contains "noise," which can propagate and degrade correction steps, leading to worse results ("the blind leading the blind") <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Furthermore, feeding internal logics or demonstrations from larger models (verifiers) to smaller models can lead to incompatibility, rendering the feedback useless <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. The feedback needs to be "dumbed down" to cater to the smaller model's internal logic <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

#### Wiass: Distilling Self-Improvement for Smaller Models

The "Wiass" method addresses these challenges by:

1.  Reformulating the problem to retrain the model with an attempted solution as input, then generating feedback and updates <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
2.  Using a larger LLM to edit the smaller model's feedback, tailoring it to the smaller model <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. External tools like Python scripts can also provide more accurate feedback for specific tasks <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

In this approach, the smaller model generates an answer and self-reflection, which is then edited by a larger model. This corrected feedback is used as input for the smaller model to generate an updated answer <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. This iterative process generates "traces" or "trajectories" of trial and error until the problem is solved correctly <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. These filtered trajectories are then used to train the smaller models to perform self-improvement with the guidance of a larger model or other tools <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

Results show that this "on-policy self-supervision" is effective. After three iterations, the method achieved 48% accuracy on mathematical problems, outperforming supervised training data <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This indicates that fine-tuning with such self-improvement data truly helps models learn self-improvement <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>, with improvements ranging from 7% to 18% across tasks <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

> "We can actually improve these models' reflection or self-learning abilities without explicitly human supervision data. We could use the synthetic ways to generate data policy to help the models to improve." <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>

A limitation remains that the effectiveness of this approach is capped by the ceiling of the larger LLM's (verifier/editor) ability to provide correct feedback <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

## Eliciting Stronger Model Behavior via Test-Time Scaling

Traditional [[ai_models_and_training_methods | LLM training]] relies on compute, data size, and parameter size, following scaling laws <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. However, pre-training is resource-intensive, making it difficult for smaller companies or academia <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

A new direction, **test-time scaling**, focuses on eliciting better behaviors from existing pre-trained models by providing them with more steps or budgets during inference <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. Techniques like "think step by step" or "do reflection" fall into this category, leading to improved results <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Tree Search for Sequential Decision Making

Complex sequential decision-making tasks, like chess or dialogue, require planning ahead <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. **Monte Carlo Tree Search (MCTS)** is an algorithm that simulates moves and evaluates outcomes multiple times to find stronger actions <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

For conversational settings with a clear goal, like a donation persuasion task <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>, a "zero training" MCTS model can be designed by prompting an LLM (e.g., ChatGPT) to:

1.  **Search potential**: Act as the policy to propose promising actions <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
2.  **Simulate action outcomes**: Predict outcomes if a persuasion strategy is used <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.
3.  **Evaluate action quality**: Assess the quality of actions after interacting with the environment <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
4.  **Simulate opponent behavior**: Use another LLM to simulate user responses, given conversational history <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

Unlike closed-loop MCTS, open-loop MCTS is used for conversational tasks to account for the stochastic nature and variance of human responses <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.

"GD P0," a proposed method, has shown to generate more competitive results without explicit training <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Evaluations by LLMs (e.g., ChatGPT) and human studies (Mechanical Turk) confirm that models using this planning algorithm achieve higher donation rates and are perceived as more convincing, natural, and coherent <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. Analysis also reveals that these models can self-discover task information, like avoiding early "big asks" and diversifying persuasion strategies (emotional vs. logical appeals) <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

## Transferring Policy and Exploratory Learning

The principles of MCTS can be extended to broader AI agent spaces that involve tool use and manipulations beyond just talking <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

### RMCTS: Reinforcement Learning MCTS

To enable [[integration_of_large_language_models_in_development | LLMs to perform various AI agent tasks]], they need to perceive the world, starting with visual language models (VLMs) that can process images and text <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>. Traditional VLMs trained on visual question answering (VQA) tasks are different from the action-based visual language models needed for AI agent tasks, which involve executing actions like clicking buttons on a screenshot <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. Humans achieve 88% success on tasks like "clear my shopping carts" on benchmarks like Visual Web Arena, while a simple GPT-4V achieves only 16% <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>, highlighting the gap in agent environment interaction data and training <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>.

**RMCTS (RL Monte Carlo Tree Search)** is an algorithm that augments VLMs with a search algorithm to improve decision-making during test time <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. It extends simple MCTS by incorporating:

1.  **Contrastive Reflection**: Allows agents to learn from past interactions and dynamically improve search efficiency, saving experiences to a vector database for future retrieval <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. This creates a "memory module" for the system <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.
2.  **Multi-agent Debate**: Improves the robustness of state evaluation by having models debate the quality of actions (e.g., "why is this a good/bad action?"), counterbalancing biases from single prompts <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

RMCTS builds a search tree dynamically and uses multi-agent debate for reliable state estimation <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>. After each task, it performs contrastive self-reflection to improve future execution <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>.

Evaluated on benchmarks like **Visual Web Arena** (browsing tasks) and **OS World** (computer desktop tasks in Linux) <a class="yt-timestamp" data-t="00:31:43">[00:31:43]</a>, RMCTS outperforms other search algorithms and non-search methods <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>. It leads the Visual Web Arena leaderboard and is the best non-trained method in OS World <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>, demonstrating significant performance gains without additional human supervision <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

### Exploratory Learning

The knowledge obtained through these search processes can be transferred into the training of the base LLM <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. Instead of **imitation learning** (directly training on the best action found), **exploratory learning** treats the tree search process as a single trajectory <a class="yt-timestamp" data-t="00:33:48">[00:33:48]</a>. The model learns how to linearize search tree traversal to understand how to explore, backtrack, and evaluate <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>. This teaches the model to improve its decision processes autonomously <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

Exploratory learning outperforms imitation learning, especially with constrained test-time budgets, by enabling the agent to learn from scenarios where an action didn't lead to the desired state, prompting it to backtrack and try other actions <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>.

## Future Directions and Frameworks

Reflective MCTS models and exploratory learning demonstrate that significant improvements in agent performance can be achieved through test-time compute scaling and retraining from refined or backtracked exploratory traces, without relying on human supervised information <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>.

Future work includes developing better RL methods to reduce reliance on the search tree and model predictive control to lessen expensive environment setups <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>. Ongoing efforts focus on improving control abilities and autonomous exploration within agent orchestration layers <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

The **ARCollex AI** open-source agent framework offers features like continuous learning and task decomposition, providing developers flexibility <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. Advancing AI agents requires a multidisciplinary approach, combining expertise from machine learning, systems, human-computer interaction (HCI), and security <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

Current benchmarks typically focus on single agents performing single tasks <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. Future challenges include:

*   **Multi-tasking**: How one human can assign multiple tasks to a model on the same computer, leading to system-level problems like scheduling <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Database interaction**: Avoiding side effects and ensuring better security, including knowing when to trigger human handovers or supervision requests <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
*   **Multi-user, Multi-agent planning**: Complex scenarios involving multiple humans interacting with different agents, requiring realistic benchmarks that consider efficiency and security in addition to task completion <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.