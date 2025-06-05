---
title: Importance and progress of AI agents
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

AI agents are generating significant excitement in the computing world, with figures like Bill Gates calling them the "biggest revolution in computing" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, Andrew Ng noting "massive AI progress" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, and Sam Altman predicting 2025 will be "the year of agent" <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Despite some negative voices dismissing them as mere wrappers for large language models (LLMs) or criticizing examples like AutoGPT for not solving practical solutions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, the advancements in AI agents are substantial. Agents are not a new concept, but the power of large language models has significantly enhanced their capabilities <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## What Are AI Agents?

At their core, AI agents interact with an environment through actuations of actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This process generally involves four key steps:

*   **Perception**: Agents need to understand their environment by sensing information from various sources like text, images, audio, video, and touch <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Reasoning**: Once information is perceived, agents process it to understand how to complete tasks, break them down into individual steps, and utilize environmental inputs to determine appropriate tools or actions. This inner planning process is often referred to as "chain of thoughts reasoning," frequently powered by large language models <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Reflection (Meta-reasoning)**: Agents can perform meta-reasoning steps, asking themselves if a chosen action was correct and course-correcting if needed <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Actions**: These are the physical or digital performances an agent undertakes, such as talking to humans, moving from one point to another, or manipulating interfaces <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Levels of AI Agent Autonomy

The deployment of AI agents can be understood through an analogy to the levels of autonomy in self-driving cars <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:

*   **Level 1: Chatbot (2017)**: Simple information retrieval <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2: Agent Assist**: An agent uses an LLM to generate suggested responses, but a human must approve the message before sending (e.g., customer service) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3: Agent as a Service**: LLMs automate AI workflows for specific tasks, acting as a service (e.g., meeting bookings, writing job descriptions) <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4: Autonomous Agents**: An agent can delegate and perform multiple tasks that have shared components, knowledge, and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5: Jarvis/Iron Man-level Agents**: Full trust and delegation of security measures, allowing agents to perform on behalf of the user 100% autonomously <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

Self-driving cars are an example of an agent performing perception, reasoning, planning, and execution, but they are high-risk due to potential errors affecting lives <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. AI agents can be separated into low-risk tasks (e.g., filing reimbursements with human supervision) and high-risk customer-facing tasks. Over time, the trend is to move from back-office automation to front-office deployment <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Progress in Improving AI Agents

Recent advancements in AI agents focus on three key areas:
1.  Improving LLMs for better reasoning and reflection <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
2.  Eliciting better behaviors from existing LLMs for AI agent tasks <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
3.  Learning from examples and traces to optimize LLMs for AI agent tasks <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Improving Reasoning and Reflection

Traditional methods for mathematical reasoning with LLMs include:
*   **F-shot prompting**: Providing examples of similar problems and their answers as context <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Chain of thought prompting**: Instructing the model to "think step by step," allowing it to reason over tokens to reach an answer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

More recently, a combined approach uses a "reflection" or "self-improvement" process. The model generates an initial answer, then is prompted to generate feedback on its own answer (e.g., "in step two, blah blah blah is incorrect..."). This feedback is then combined with the original question and answer to prompt the model again, allowing it to update and refine its answer <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This process can be iterated until a correct answer is reached <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

However, challenges arise with smaller LLMs (e.g., Llama 7B) where generated feedback can contain "noise" that propagates to correction steps, leading to worse results ("the blind leading the blind") <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Also, internal logic from larger models may be incompatible with smaller models, making their feedback unhelpful <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

To address this, the **`Wiass` method** was proposed <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>:
*   A smaller model generates an initial answer and self-feedback.
*   A larger LLM (or external tool like Python scripts) edits this feedback to be more tailored for the smaller model's internal logic <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   This corrected feedback is used to update the answer, iterating until the problem is solved <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   The trajectories of these trial-and-error processes are filtered into a balanced set to train smaller models for self-improvement under the guidance of larger models or tools <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

This approach shows improved performance, particularly on mathematical reasoning tasks, demonstrating that on-policy self-provisioning is useful and models can learn self-improvement without explicit human supervision <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. The limitation remains the ceiling effect of the verifiers (larger LLMs); if they cannot edit correctly, smaller models cannot distill information effectively <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

### Eliciting Better Behaviors and Planning

While pre-training large language models is resource-intensive and often limited by compute, data size, and parameter size (scaling laws) <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>, a promising direction is **test-time scaling** <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This involves taking an existing pre-trained model and giving it more steps or budget during inference (e.g., "think step by step," reflection) to achieve better results <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

For sequential decision-making tasks, like dialogue or games such as chess, agents need to plan ahead and simulate future moves. This concept is analogous to how Grand Masters plan many steps ahead in chess <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. Algorithms like AlphaGo use **Monte Carlo Tree Search (MCTS)**, which proposes moves, simulates outcomes, evaluates their value, and repeats to find stronger moves <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

The `GD P0` (Zero Training MCTS) work adapted these ideas to conversational settings, specifically donation persuasion tasks <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. It uses prompting of large language models for:
*   Searching for potential promising actions <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   Simulating action outcomes <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.
*   Evaluating action quality after interacting with the environment <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
*   Simulating the opponent's (user's) behavior <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

Unlike closed-loop MCTS, this approach uses **open-loop MCTS** to account for the variance in human responses in a stochastic process <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>. Evaluations showed that agents using this planning algorithm achieved better donation rates and were perceived as more convincing, natural, and coherent. The models also self-discovered task information, such as not asking for donations too early and diversifying persuasion strategies (emotional vs. logical appeal) <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

### Transferring Policy to Other Tasks / Visual Agents

The concept of MCTS can be extended to broader [[role_of_ai_agents_in_planning_and_executing_tasks | AI agent]] spaces that involve tool use and manipulations beyond just talking <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>. The `Exact` work focuses on teaching large language models to perceive the world visually, leading to **Visual Language Large Models (VLMs)** that process both images and text <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.

Traditional VLMs are trained for tasks like visual question answering, but [[role_of_ai_agents_in_planning_and_executing_tasks | AI agent]] tasks require action-based interaction (e.g., clearing a shopping cart based on a screenshot) <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>. Standard models like GPT-4V, without specific planning, perform poorly on such tasks compared to humans (16% vs. 88% success on Visual Web Arena) <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.

To improve performance without retraining expensive models, the **`R MCTS` (RL Monte Carlo Tree Search)** algorithm was introduced <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. It extends MCTS by incorporating:
*   **Contrastive reflection**: A memory module allows agents to learn from past interactions, internalize successes or errors, and save experiences to a vector database. This knowledge is then retrieved for future tasks to enhance decision-making <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.
*   **Multi-agent debate**: Instead of single prompts, the progress evaluation is made more robust by having models debate whether an action is good or bad and why, counterbalancing biases <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>.

`R MCTS` builds a search tree on the fly, uses multi-agent debate for reliable state estimates, and performs contrastive self-reflection at the end of each task to improve future execution <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

Evaluations on benchmarks like Visual Web Arena (browsing tasks) and OS World (computer desktop tasks in Linux) show that `R MCTS` outperforms other search algorithms and non-search methods. Augmenting visual large language models with search algorithms significantly improves performance without additional human supervision <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a>. This method ranks #1 on the Visual Web Arena leaderboard and is the best non-trained method in OS World <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>.

### Learning from Generated Data

To transfer the knowledge obtained through search processes into the training of base large language models, **Exploratory Learning** was developed <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>. Unlike imitation learning (direct transfer of best actions), exploratory learning treats the entire tree search process as a single trajectory. Models learn to linearize the search tree traversal, motivating them to learn how to explore, backtrack, and evaluate actions themselves <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. This teaches models to improve their decision processes by themselves <a class="yt-timestamp" data-t="00:34:23">[00:34:23]</a>.

## Future Prospects and Challenges

Many advancements in AI agents, particularly those relying on test-time compute scaling and training on refined exploratory traces, do not require human supervised information, making them accessible in academic or smaller company settings <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>.

Future work focuses on:
*   Reducing reliance on search trees and using model predictive control to cut down expensive environment setup and interaction <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.
*   Improving control abilities and autonomous exploration for agent orchestration layers <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

An open-source agent framework, `ARX`, has been released, offering features like continuous learning and task decomposition to provide developers more flexibility <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.

The development of AI agents requires combining expertise from machine learning, systems, human-computer interaction (HCI), and security <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. Current benchmarks primarily focus on single agents performing single tasks <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. However, future challenges include:
*   **Multi-tasking on a single computer**: Addressing system-level problems like scheduling, database interaction, security, and knowing when to request human supervision or handover <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Multi-user, multi-agent planning**: More complex scenarios where multiple humans interact with various agents, leading to complicated and potentially adversarial settings <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.

The goal is to establish more realistic benchmarks that integrate system considerations and algorithms that account for not only task completion but also efficiency and security <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.