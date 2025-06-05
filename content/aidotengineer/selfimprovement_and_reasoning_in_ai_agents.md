---
title: Selfimprovement and reasoning in AI agents
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

AI agents are a significant area of progress in artificial intelligence, with figures like Bill Gates calling them the "biggest revolution in computing" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a> and Sam Altman predicting 2025 as the "year of agent" <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. While some skepticism exists regarding their capabilities, particularly in planning beyond simple Large Language Model (LLM) wrappers <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, recent advancements show promising developments in their self-improvement and reasoning abilities <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## What Are AI Agents?
At their core, AI agents are systems that interact with an environment through actuations of actions <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Their conceptual basis is not new but has been significantly amplified by the power of large language models <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

The process of an AI agent typically involves four main steps:
1.  **Perception**: The agent understands its environment by sensing information from various modalities like text, image, audio, video, or touch <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
2.  **Reasoning**: After perceiving information, the agent processes it to understand how to complete tasks, break them down into individual steps, and decide on appropriate tools or actions <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This "inner plan process" is often referred to as [[chain_of_thought_reasoning_in_ai | Chain of Thought reasoning]], powered by LLMs <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Reflection (Meta-reasoning)**: Agents can perform meta-reasoning steps, asking themselves if previous actions were correct and if they need to adjust their approach <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Actions**: The agent performs actions, which can range from talking to a human to moving physically or executing digital commands <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Levels of Autonomy in AI Agents
The deployment of AI agents can be understood through an analogy with levels of autonomy in self-driving cars <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:

*   **Level 1 (Chatbot)**: Simple information retrieval, like a chatbot from 2017 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2 (Agent Assist)**: LLMs generate suggested responses for human agents (e.g., customer service), requiring human approval before sending <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3 (Agent as a Service)**: LLMs automate AI workflows for specific tasks like meeting bookings or writing job descriptions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4 (Autonomous Agents)**: An AI can delegate and perform multiple, interconnected tasks, sharing knowledge and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5 (Jarvis-like Agents)**: Full trust in the agent, delegating all security measures (e.g., keys) to perform actions on behalf of the user <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

While self-driving cars are high-risk agents, AI agents can be deployed for low-risk tasks (e.g., filing reimbursements with human supervision) and gradually move towards high-risk, customer-facing tasks as trust is built <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## [[Developing and optimizing AI agents | Improving Reasoning and Reflection in AI Agents]]

### Self-Refinement with Large Language Models
[[Using reasoning models and tool calls in AI | Improving the reasoning abilities of LLMs]] can be approached in two main ways for mathematical reasoning tasks:
1.  **Few-shot prompting**: Providing examples of similar problems and their answers as context <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
2.  **[[Chain of Thought reasoning in AI | Chain of Thought reasoning]]**: Instructing the model to "think step by step" to reach an answer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

A more recent method combines these approaches by incorporating self-reflection or self-improvement <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The model generates an initial answer, then prompts itself to generate feedback on its own answer (e.g., "the part blah blah is incorrect") <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This feedback, combined with the original question and answer, is used to prompt the model again to update its answer and internal processes <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This "self-refined" process can be iterated multiple times until the correct answer is reached <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

#### Challenges with Smaller LLMs
While effective with larger LLMs, this self-improvement process can be problematic with smaller models (e.g., Llama 7 billion) <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Noise Propagation**: Feedback generated by smaller models can contain "noise" that propagates to correction steps, leading to worse results <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Incompatibility**: Internal logics and demonstrations from larger LLMs may not be compatible with smaller models, making the feedback useless <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

#### Proposed Solution: Distillation from Larger Models
To enable self-improvement in smaller models, a method called "Wiass" proposes:
1.  Using a smaller model to generate an initial answer and self-feedback <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
2.  Employing a larger LLM or external tools (like Python scripts for math tasks) to **edit** the smaller model's feedback, tailoring it to the smaller model's internal logic <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
3.  Using this corrected feedback to update the answer iteratively until the problem is solved <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

This process generates "traces" of trial and error, which can be filtered and used to train existing smaller models to perform self-improvement with guidance <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. On-policy supervised training (generating feedback in real-time as the model changes) showed significant improvement (up to 48% after three iterations) compared to simple supervised fine-tuning <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

> [!NOTE] Takeaway
> Models' reflection and self-learning abilities can be improved using synthetic data generation policies, reducing the reliance on explicit human supervision <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. However, the quality of improvement is capped by the ceiling effect of the larger models or verifiers used for editing <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

## Eliciting Stronger Model Behavior Through Test-Time Scaling

Beyond pre-training, test-time scaling offers a way to elicit better performance from existing pre-trained LLMs by giving them more steps or computational budget during inference <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This includes methods like "think step by step" or applying reflection <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Sequential Decision-Making in Dialogue Tasks
Dialogue tasks, like a donation persuasion scenario, involve sequential decision-making where an agent must strategize and plan its conversational moves ahead of time <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. This is analogous to games like chess, where players plan moves by simulating opponent responses <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

#### [[Using reasoning models and tool calls in AI | Monte Carlo Tree Search (MCTS)]] for Dialogue
[[Using reasoning models and tool calls in AI | Tree search]] algorithms, common in games like AlphaGo, can be applied to conversational settings to improve decision-making <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   **Zero-training MCTS**: A model is prompted to act as a policy, propose actions, simulate outcomes, and evaluate action quality, updating each action's quality over time <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
*   **User Simulation**: Another LLM can be used to simulate user (opponent) behavior, generating diverse responses to proposed strategies <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
*   **Open-Loop MCTS**: Unlike closed-loop MCTS used in deterministic games, human responses introduce variance, necessitating an open-loop MCTS approach that stochastically samples simulated tests <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.

In donation persuasion tasks, this MCTS approach (termed GDP0) improved donation rates and led to more convincing, natural, and coherent conversations <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. The models learned to self-discover effective strategies, such as avoiding early donation asks and diversifying persuasion tactics (emotional, logical appeals) <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

## Expanding to Broader AI Agent Tasks

The principles of MCTS and self-improvement can be extended to broader AI agent tasks involving tool use and manipulations, beyond just conversation <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>. This requires teaching LLMs to perceive the world visually.

### Action-Based Visual Language Models
Traditional visual language models (VLMs) are often trained for Visual Question Answering (VQA) tasks <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. However, AI agent tasks require VLMs to process computer screenshots and perform actions like clicking buttons to clear a shopping cart <a class="yt-timestamp" data-t="00:27:25">[00:27:25]</a>. Standard GPT-4V, without specific planning or agentic training, performs poorly (16% success) on benchmarks like Visual Web Arena <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>, highlighting a lack of agent-environment interaction data.

#### R-MCTS: RL Monte Carlo Tree Search
A new algorithm, R-MCTS, is introduced to elicit better performance through test-time compute <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. It extends MCTS with two key modifications:
1.  **Contrastive Reflection with Memory**: The system includes a memory module where agents learn from past interactions. After completing a task, contrastive reflection helps the model internalize successes or errors, saving this experience to a vector database <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>. For future tasks, relevant reflections are retrieved to enhance decision-making <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
2.  **Multi-Agent Debate for State Evaluation**: Instead of single prompts for evaluating progress, a "debate" format is used. Models are asked to argue why an action is good or bad, leading to more robust and balanced evaluations and counteracting biases <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>.

These modifications allow R-MCTS to build a search tree on the fly, improve decisions, and continuously learn from experience through reflection <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

#### Evaluation and Benchmarks
R-MCTS was evaluated on two popular AI agent benchmarks:
*   **Visual Web Arena**: Evaluates agents on browsing tasks (e.g., Reddit, shopping) <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.
*   **OS World**: Consists of computer tasks like navigating file systems or using apps (V Code, Excel) in a Linux environment <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

R-MCTS consistently outperformed other search algorithms (breadth-first, depth-first, vanilla MCTS) and non-search methods <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>. It achieved top rankings in both the Visual Web Arena leaderboard and as the best non-trained method in OS World <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>, demonstrating significant performance gains without additional human supervision or fine-tuning of original models <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

## Transferring Knowledge through Exploratory Learning

The knowledge gained through these search processes at test time can be transferred to the base LLM itself during training <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.
*   **Exploratory Learning**: Unlike imitation learning (direct training on the best action found in the tree), exploratory learning treats the tree search process as a single trajectory <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. This teaches the model to linearize the search tree traversal, motivating it to learn how to explore, backtrack, and evaluate its actions <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>.
*   This approach helps models improve their decision processes by learning to evaluate and backtrack independently <a class="yt-timestamp" data-t="00:34:23">[00:34:23]</a>.

## Future Directions and Frameworks
[[Continuous improvement in AI systems | Continuous improvement]] in AI agents, especially without reliance on human supervision, is a key area of research <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>. Future work focuses on:
*   **Reducing Reliance on Search Trees**: Developing better methods to minimize the need for computationally expensive search trees <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.
*   **Model Predictive Control**: Implementing methods to reduce the cost of environment setup and interaction <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>.
*   **Improved Control and Autonomous Exploration**: Enhancing the agent's ability to control its actions and explore autonomously within its orchestration layer <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

> [!INFO] ArXlex Open-Source Agent Framework
> The [[building_and_improving_ai_agents | ArXlex open-source agent framework]] integrates these research advancements, offering features like [[continuous_improvement in_ai_systems | continuous learning]] and task decomposition for developers <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.

### Interdisciplinary Challenges
[[Design challenges for AI agents | Designing AI agents]] for practical, real-world deployment requires an interdisciplinary approach, combining machine learning expertise with systems, human-computer interaction (HCI), and security expertise <a class="yt-timestamp" data-t="00:37:11">[00:37:11]</a>.

[[Challenges in creating personal AI agents | Challenges in creating personal AI agents]] include:
*   **Multi-Agent, Multi-User Scenarios**: Current benchmarks often focus on a single agent performing a single task <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>. Real-world applications demand multiple agents interacting with multiple humans and tasks simultaneously <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.
*   **System-Level Problems**: Issues like scheduling, database interaction to avoid side effects, and robust security measures (e.g., human handover points) become critical <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
*   **Realistic Benchmarks**: There is a need to establish more realistic benchmarks that consider not only task completion but also efficiency, security, and potential adversarial settings <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

Addressing these [[challenges_in_ai_agent_evaluation | challenges in AI agent evaluation]] will provide the foundation for future AI agent applications <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>.