---
title: Improving AI agent task execution
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

The development of [[building_effective_ai_agents | AI agents]] has been a significant topic in computing, with figures like Bill Gates, Andrew Ng, and Sam Altman highlighting their potential impact <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. While some skepticism exists regarding their planning abilities and practical solutions, a fundamental understanding of [[building_effective_ai_agents | AI agents]] is crucial <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The recent advancements in large language models (LLMs) have significantly enhanced the power of [[building_effective_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## What are AI Agents?

At their core, [[building_effective_ai_agents | AI agents]] operate through a cyclical process involving:
*   **Perception**: Like humans, [[building_effective_ai_agents | AI agents]] must understand their environment by sensing information from text, images, audio, video, and touch <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Reasoning**: After gathering information, [[building_effective_ai_agents | AI agents]] process it to understand tasks, break them down into steps, and determine appropriate tools or actions <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This "inner plan process" is often powered by LLMs and is referred to as "chain of thoughts reasoning" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Reflection (Meta-reasoning)**: [[building_effective_ai_agents | AI agents]] can perform meta-reasoning by asking if a chosen action was correct and if they should revisit previous steps <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Actions**: This involves any output or behavior an [[building_effective_ai_agents | AI agent]] performs, such as talking to humans or moving in an environment <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Essentially, [[building_effective_ai_agents | AI agents]] interact with their environment through actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Levels of AI Agent Autonomy

Similar to the levels of autonomy in self-driving cars, [[building_effective_ai_agents | AI agents]] can be categorized by their degree of independence and trust <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:
*   **Level 1 (Chatbot)**: Basic information retrieval, as seen in chatbots from 2017 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2 (Agent Assist)**: LLMs suggest responses for human agents (e.g., customer service), requiring human approval before sending <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3 (Agent as a Service)**: LLMs automate AI workflows for specific tasks like meeting bookings or writing job descriptions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4 (Autonomous Agents)**: [[building_effective_ai_agents | AI agents]] can delegate and perform multiple tasks simultaneously, sharing components, knowledge, and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5 (Jarvis-like AI)**: Full trust is placed in [[building_effective_ai_agents | AI agents]], delegating all security measures and allowing them to act on behalf of the user <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

While self-driving cars are a high-risk example of [[building_effective_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, general [[building_effective_ai_agents | AI agents]] can be applied to both low-risk (e.g., filing reimbursements with human supervision) and high-risk (e.g., customer-facing tasks) operations <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Improving AI Agent Task Execution

Improving [[building_effective_ai_agents | AI agent]] task execution involves enhancing LLMs' reasoning and reflection capabilities, eliciting better behaviors, and learning from past interactions <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### 1. Enhancing Reasoning and Reflection (Self-Improvement)

LLMs can improve their reasoning through various prompting methods <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>:
*   **Few-shot prompting**: Providing examples of problems and their answers as context <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Chain of thoughts (CoT)**: Instructing the model to "think step by step" to reach a correct answer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Self-refinement/Reflection**: A more recent method combines CoT with feedback generation <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The model generates an initial answer, then produces feedback on its own solution, and finally updates the answer based on this reflection <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. This iterative process can be repeated until a correct answer is reached <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

#### Challenges with Smaller LLMs
Smaller LLMs (e.g., LLaMA 7B) struggle with self-improvement because the feedback they generate can contain "noise" that propagates through correction steps, leading to worse results <a class="yt-timestamp" data-t="00:08:58">[00:09:01]</a>. Also, internal logic from larger models (like GPT-4) may be incompatible with smaller models, making feedback unhelpful <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

#### Distillation from Larger Models (Wiass)
To address this, a method called Wiass distills self-improvement capabilities from larger models to smaller ones <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>:
1.  A smaller model attempts to solve a problem and generates initial feedback <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
2.  A larger LLM or external tool (like Python scripts for math) edits this feedback to make it more tailored and useful for the smaller model <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
3.  This corrected feedback is then used to update the smaller model's answer, in an iterative process until the problem is solved <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
4.  The successful "traces" (trial and error trajectories) are filtered and used to fine-tune the smaller models, enabling them to perform self-improvement with guidance <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

This "on-policy self-supervision" approach, using synthetically generated data, has shown significant improvements in mathematical reasoning tasks, even outperforming supervised training data <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. It enables models to learn self-improvement without explicit human supervision <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

### 2. Eliciting Better Behaviors (Planning and Tree Search)

Beyond pre-training, enhancing performance at "test time" by providing more steps or "budgets" during inference can yield better results <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This is achieved through more complex chain-of-thought processing, particularly tree search <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

#### Monte Carlo Tree Search (MCTS) for Dialogues
Inspired by games like chess and AlphaGo, Monte Carlo Tree Search (MCTS) can be applied to sequential decision-making tasks, such as dialogue <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. The process involves:
*   **Proposing a move/action**: An LLM acts as the policy to suggest a promising action <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   **Simulating outcomes**: An LLM simulates what would happen after the action <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.
*   **Evaluating action quality**: An LLM evaluates the outcome of the action after interacting with the environment <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
*   **Updating quality**: Action quality is updated over time, leading to stronger moves through simulation <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.
*   **Opponent simulation**: Another LLM simulates the opponent's (e.g., user's) behavior <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

For conversational tasks, an "open-loop MCTS" is used to account for human response variance, stochastically sampling possible simulated tests <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. This approach, called GDP0, improves persuasion tasks without explicit training data, leading to higher donation rates and more convincing, natural, and coherent interactions <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Models also self-discover effective strategies, like delaying the "big ask" and diversifying persuasion tactics <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

#### R-MCTS for Broader AI Agent Tasks
To extend these planning capabilities to broader [[developing_ai_agents_for_productivity | AI agent]] tasks beyond dialogue, a new algorithm called RL MCTS (R-MCTS) was introduced <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. This algorithm, applied to visual language models (VLMs) for action-based tasks like clearing shopping carts on a computer screenshot <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>, incorporates:
*   **Contrastive Reflection**: Allows [[building_effective_ai_agents | agents]] to learn from past interactions and dynamically improve search efficiency by internalizing successes or errors <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. These experiences are saved in a vector database for future retrieval <a class="yt-timestamp" data-t="00:29:58">[00:29:58]</a>.
*   **Multi-agent Debate**: Improves state evaluation by using multiple [[building_effective_ai_agents | agents]] to debate the quality of an action (why it's good or bad), counterbalancing biases from a single model <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

R-MCTS outperforms other search algorithms on benchmarks like Visual Web Arena (browsing tasks) and OS World (Linux computer tasks like file system navigation or using apps) <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>. It shows that augmenting VLMs with search algorithms can improve performance without additional human supervision <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.

### 3. Learning from Examples and Traces (Exploratory Learning)

The knowledge gained through tree search can be transferred back into the base LLM through a training process <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>.
*   **Exploratory Learning**: Unlike imitation learning (which directly transfers the best action found), exploratory learning treats the entire tree search process as a single trajectory <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. This teaches the model how to linearize the search tree traversal, motivating it to learn how to explore, backtrack, and evaluate <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>. This makes models improve their decision processes inherently <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

Exploratory learning leads to better performance with constrained budgets for test-time computation compared to imitation learning <a class="yt-timestamp" data-t="00:34:32">[00:34:32]</a>.

## Future Directions and Challenges

Current benchmarks often focus on a single [[building_effective_ai_agents | AI agent]] performing a single task <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. Future work aims to address more complex scenarios:
*   **Multi-task, Multi-agent Environments**: How can a single human assign multiple tasks to a model on the same computer, or how do multiple humans interact with multiple [[building_effective_ai_agents | agents]] concurrently <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>?
*   **System-level Problems**: This includes scheduling, database interaction to avoid side effects, and enhanced security measures, such as determining when to handover to a human or request supervision <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
*   **Realistic Benchmarks**: There is a need for more realistic benchmarks that integrate system considerations, focusing not only on task completion but also on efficiency and security <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

The open-source Arcollex AI framework is being developed to integrate these research findings, providing features like continuous learning and task decomposition <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. This involves combining machine learning expertise with systems, HCI, and security knowledge to advance [[building_effective_ai_agents | AI agent]] systems in a deeper and more practical way <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.