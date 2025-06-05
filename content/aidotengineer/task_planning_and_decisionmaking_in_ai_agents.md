---
title: Task planning and decisionmaking in AI agents
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

## Introduction to AI Agents

The concept of [[role_of_ai_agents_in_planning_and_executing_tasks | AI agents]] has gained significant traction, with figures like Bill Gates hailing it as a major revolution in computing and Andrew Ng noting it as a massive [[role_of_ai_agents_in_planning_and_executing_tasks | AI progress]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Sam Altman of OpenAI even projected 2025 as the "year of agent" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. While some critics argue that these are merely "thin wrappers" around Large Language Models (LLMs) with limited planning capabilities, the core idea of [[components_of_ai_agents | AI agents]] is not new, but has been significantly empowered by LLMs <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Components of AI Agents

[[components_of_ai_agents | AI agents]], like humans, operate through several key steps:
*   **Perception:** Understanding the environment by sensing information such as text, image, audio, video, or touch <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Reasoning:** Processing information to understand tasks, break them into individual steps, and identify appropriate tools or actions. This often involves an "inner plan" or "chain of thoughts" process, powered by LLMs <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Reflection (Meta-reasoning):** A step where the agent evaluates its executed actions and decides whether to adjust or go back if a choice was incorrect <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Actions:** Any performance by the agent, such as talking to humans, moving between points, or utilizing tools <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

Generally, [[role_of_ai_agents_in_planning_and_executing_tasks | agents]] interact with their environment through the actuation of actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Levels of Autonomy

The deployment of [[role_of_ai_agents_in_planning_and_executing_tasks | AI agents]] can be understood through an analogy to the levels of autonomy in self-driving cars <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:
*   **Level 1 (Chatbot):** Basic information retrieval, akin to early chatbots from 2017 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2 (Agent Assist):** LLMs generate suggested responses, but human approval is still required, like a customer service agent <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3 (Agent as a Service):** LLMs automate specific workflows, acting as a service (e.g., meeting bookings, writing job descriptions) <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4 (Autonomous Agents):** The [[role_of_ai_agents_in_planning_and_executing_tasks | AI agent]] can delegate and perform multiple, inter-connected tasks, sharing knowledge and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5 (Jarvis/Iron Man):** Full trust in the agent, delegating all security measures like keys, allowing the agent to perform fully on its behalf <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

While self-driving cars represent a high-risk application of [[role_of_ai_agents_in_planning_and_executing_tasks | agents]] (due to potential for loss of life), [[role_of_ai_agents_in_planning_and_executing_tasks | AI agents]] can be separated into low-risk and high-risk tasks <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Low-risk tasks, such as back-office operations like filing reimbursements, can benefit from human supervision initially and gain trust over time for full automation <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. Customer-facing tasks are generally considered higher risk <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## Improving LLM Reasoning and Reflection for AI Agents

To enhance [[role_of_ai_agents_in_planning_and_executing_tasks | AI agents]], research focuses on improving LLMs' reasoning and reflection capabilities <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Self-Refinement through Prompting

Mathematical reasoning tasks often employ two main prompting methods <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>:
1.  **Few-shot prompting:** Providing examples of similar problems and their answers as context to the LLM <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
2.  **Chain of Thought (CoT):** Instructing the model to "think step by step," allowing it to reason over tokens to reach a correct answer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

More recent methods combine these, providing the LLM with a question and its initial answer, then prompting it to generate feedback (reflection) on its own answer <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This feedback, combined with the original question and answer, is used to re-prompt the model, allowing it to update its answer and internal processes. This iterative process is called **self-refinement** or **self-improvement** <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### [[Challenges in Developing AI Agents | Challenges with Smaller LLMs]]

While effective, self-improvement processes can face [[challenges_in_developing_ai_agents | problems]] with smaller LLMs (e.g., Llama 7 billion). Their generated feedback may contain "noise," which can propagate through correction steps, leading to worse results ("the blind leading the blind") <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Additionally, the internal logic or "demonstrations" of larger LLMs (e.g., GPT-4) may be incompatible with smaller models, rendering their feedback useless <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Distillation for Smaller Models

To address these [[challenges_in_developing_ai_agents | challenges]] and enable smaller LLMs to self-improve, a method involves:
*   **Reformulating the problem:** Retraining the model with its attempt as input, then generating feedback and updates <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Using larger LLMs as editors/verifiers:** Instead of having smaller models generate their own feedback, a larger LLM or external tools (like Python scripts for math tasks) can edit the smaller model's feedback, tailoring it to the smaller model's internal logic <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This corrected feedback guides the smaller model's updated answer <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Iterative Correction:** This correction process can be iterated until the problem is solved correctly, especially for mathematical problems with ground truth <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   **On-policy training:** Generating these feedback traces and filtering successful trajectories to fine-tune the smaller models. This on-policy self-supervision proves more useful than simply fine-tuning on gold answers <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

This approach demonstrates that models' reflection and self-learning abilities can be improved using synthetic data policies, reducing the reliance on explicit human supervision <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

## Eliciting Stronger Model Behavior through Test-Time Scaling

Beyond pre-training, which is resource-intensive, a new direction called **test-time scaling** allows eliciting better behaviors from existing pre-trained LLMs <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. This involves providing the model with more steps or computational budget during inference, such as instructing it to "think step by step" or perform reflection <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

### [[Dynamic planning for complex tasks in AI | Tree Search for Sequential Decision-Making]]

Sequential decision-making tasks, such as dialogue or persuasion, benefit significantly from look-ahead [[dynamic_planning_for_complex_tasks_in_ai | planning]] <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. The analogy to chess is strong: thinking multiple moves ahead and simulating opponent responses to determine the best strategy <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

Algorithms like **Monte Carlo Tree Search (MCTS)**, popularized by AlphaGo, apply this principle <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. The MCTS process involves:
1.  **Proposing a move/action:** Selecting a promising action <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
2.  **Simulating outcomes:** Projecting the changes and values after taking the action <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
3.  **Evaluating action quality:** Assessing the outcomes of the action after interacting with the environment <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
4.  **Updating quality:** Iteratively refining the action quality over time <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

In conversational settings, MCTS can be applied without specific training data (Zero-training approach) by prompting LLMs to act as different components of the search <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. An LLM can be prompted to propose actions (policy), simulate action outcomes, and evaluate action quality <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. For self-play, another LLM can simulate the opponent's behavior <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

For tasks with human responses, which introduce variance, an **Open-Loop MCTS** is used. This stochastically samples different possible simulated paths, allowing the agent to anticipate and strategize against varied human reactions <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
Evaluations for conversational tasks like donation persuasion have shown that models utilizing MCTS produce more convincing, natural, and coherent interactions, leading to better outcomes <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. These models can even self-discover effective strategies, such as avoiding early donation asks and diversifying persuasion tactics <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

## Transferring Policy and Improving Base Models for Broader AI Agent Tasks

While Monte Carlo Tree Search is effective for specific tasks like dialogue, the goal is to extend it to larger [[role_of_ai_agents_in_planning_and_executing_tasks | AI agent]] spaces that involve tool use and manipulation <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

### Adapting Visual Language Models for Action-Based Tasks

Traditional Visual Language Models (VLMs) are often trained for Visual Question Answering (VQA), e.g., "What is he doing?" <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>. However, [[role_of_ai_agents_in_planning_and_executing_tasks | AI agent]] tasks require action-based understanding, such as interpreting a computer screenshot and performing actions like "clear my shopping cart" by clicking buttons <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>. There is a significant gap between VQA and agentic tasks in terms of environmental interaction data and training <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.

### RL-MCTS for Test-Time Compute

To address this gap without retraining large models like GPT-4, a new algorithm called **Reflective Monte Carlo Tree Search (RL-MCTS)** was introduced <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>. RL-MCTS is a search algorithm that:
*   **Explores vast action spaces** and improves decision-making by incrementally constructing a search tree <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
*   Incorporates **contrastive reflection**, allowing agents to learn from past interactions and dynamically improve search efficiency <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.
*   Utilizes a **memory module** (vector database) to cache learned experiences (successes and errors) from completed tasks, which are then retrieved for future tasks to enhance decision-making <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.
*   Employs **multi-agent debate** for more robust and reliable state evaluation, counteracting biases from a single model's prompt <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>.

Through these modifications, RL-MCTS (a test-time compute scaling method) significantly improves performance on popular [[evaluating_and_optimizing_ai_agents_and_workflows | AI agent]] benchmarks like Visual Web Arena (browsing tasks) and OS World (Linux computer tasks) without additional human supervision <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. It outperforms other search algorithms and non-search methods <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.

### [[Developing and optimizing AI agents | Exploratory Learning]] for Base Model Improvement

The knowledge obtained through search algorithms like RL-MCTS can also be transferred to the training process of base LLMs <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. Instead of simple imitation learning (direct transfer of the best action found), **exploratory learning** treats the tree search process as a single trajectory <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. The model learns how to linearize the search tree traversal, motivating it to learn how to explore, backtrack, and evaluate its actions <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>. This approach enables the model to improve its decision processes autonomously <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

## Future Directions and [[Design challenges for AI agents | Challenges]]

The reflective MCTS models relying on test-time compute scaling can significantly enhance [[role_of_ai_agents_in_planning_and_executing_tasks | AI agent]] performance <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>. Future work includes:
*   **Reducing reliance on search trees:** [[developing_and_optimizing_ai_agents | Developing better methods]] that don't depend entirely on extensive search <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.
*   **Model Predictive Control:** Minimizing expensive environment setup and interaction costs <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>.
*   **Improving Control and Autonomous Exploration:** Integrating these capabilities within an agent orchestration layer <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

Addressing these advancements requires combining expertise from machine learning, systems, human-computer interaction (HCI), and security <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. Current benchmarks primarily focus on single agents performing single tasks <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. Future [[design_challenges_for_ai_agents | challenges]] and research directions include:
*   **System-level problems:** Handling multiple tasks concurrently on the same computer, scheduling, database interactions, and security measures (e.g., human handover, supervision requests) <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
*   **Multi-user, Multi-agent planning:** Managing scenarios where multiple humans interact with multiple agents and assign different tasks, leading to complex, diverse settings <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.

Establishing more realistic benchmarks with system integrations and algorithms that consider not only task completion but also efficiency and security will form the foundation for future [[implementing_function_calling_and_agents_in_ai | AI agent applications]] <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.