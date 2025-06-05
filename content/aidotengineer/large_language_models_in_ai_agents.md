---
title: Large language models in AI agents
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

## Introduction to AI Agents

AI agents are a significant area of progress in artificial intelligence. Prominent figures like Bill Gates view them as the "biggest revolution in computing," while Andrew Ng considers them "massive AI progress." Sam Altman of OpenAI anticipates 2025 to be "the year of agent" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

Despite this optimism, there are also critical voices, with some arguing that current AI agents are merely "simple wrappers of large language models" that "really can't plan" <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Concerns are also raised about tools like AutoGPT not providing practical solutions <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### What are AI Agents?
AI agents are not a new concept, but the emergence of [[large_language_models | large language models]] (LLMs) has significantly enhanced their capabilities <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. An AI agent generally operates through a cyclical process:

1.  **Perception**: Agents sense information from their environment through various modalities like text, image, audio, video, and touch, much like humans understand the world <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
2.  **Reasoning**: After perceiving information, agents process it to understand how to complete tasks, break them down into individual steps, and identify appropriate tools or actions. This "inner plan" process is often referred to as "chain of thoughts reasoning," powered by [[large_language_models | large language models]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  **Reflection**: Agents can perform meta-reasoning steps, asking themselves if their actions were correct and if adjustments are needed. This self-correction process is known as "reflection" or "self-improvement" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Actions**: The final step involves performing actions, which could range from talking to humans, moving physically, or interacting with a digital environment <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Agents interact with their environment through these actuations of actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Levels of Autonomy

The deployment of AI agents can be understood through an analogy with the levels of autonomy in self-driving cars <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:

*   **Level 1: Chatbot (2017)**: The basic level, where an agent can only retrieve information <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2: Agent Assist**: An LLM generates suggested responses for tasks, but a human must approve the final message, such as in customer service <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3: Agent as a Service**: [[large_language_models | Large language models]] automate AI workflows and are used as a service, for example, for booking meetings or writing job descriptions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4: Autonomous Agents**: An AI can delegate and perform multiple tasks simultaneously, sharing components, knowledge, and resources among them <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5: J.A.R.V.I.S. (Iron Man-like)**: Full trust is placed in the agent, delegating all security measures and allowing it to perform tasks on behalf of the user <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

Tasks for AI agents can be categorized by risk. Low-risk tasks, such as filing reimbursements in a back office, allow for human supervision and can be automated over time as trust is built. High-risk, customer-facing tasks require more caution, with a progression expected from back-office to front-office deployments over time <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Improving Large Language Models for AI Agent Tasks

To advance AI agents, several key areas of improvement for [[large_language_models | large language models]] are being explored <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>:

1.  **Enhancing Reasoning and Reflection**: Focus on making LLMs better at internal thought processes and self-correction <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
2.  **Eliciting Better Behaviors**: Optimizing existing LLMs to perform better on AI agent tasks without extensive retraining <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
3.  **Learning from Traces**: Utilizing generated examples and trajectories to further refine LLMs for specific agent tasks <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Self-Improvement and Reflection

One method involves using a process of "reflection" or "self-improvement" <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. In a mathematical reasoning task, an LLM can generate an initial answer, then generate feedback on its own answer (reflection), and finally use this feedback to refine the answer. This iterative process can be repeated until a correct answer is reached <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

However, smaller LLMs (e.g., Llama 7 billion) can struggle with this, generating "noise" in their feedback that propagates into corrections, leading to worse results <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. The internal logic of larger models may also be incompatible with smaller ones, rendering their feedback useless <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

To address this, a proposed method called "Wiass" involves:
*   Using a smaller model to generate an initial answer and self-feedback <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   Employing a larger LLM or external tools (like Python scripts for math tasks) to *edit* the smaller model's feedback, making it tailored and more accurate <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   Using this corrected feedback to update the answer, iterating until the problem is solved <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

By collecting and filtering these trial-and-error trajectories, smaller models can be trained to perform self-improvement with guidance from larger models or tools <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This approach, known as "on-policy self-supervision," has shown significant improvements in mathematical reasoning tasks <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### Eliciting Stronger Model Behavior

Beyond pre-training, test-time scaling allows LLMs to achieve better results by providing more steps or computational budget during inference <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. This includes methods like "thinking step-by-step" or performing "reflection" <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

#### Tree Search for Dialog Tasks
For sequential decision-making tasks like dialogues, principles from chess (e.g., AlphaGo) can be applied using "tree search" <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. This involves:
*   Proposing a move or action <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
*   Simulating potential outcomes <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
*   Evaluating the quality of the action <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
*   Repeating this process to find the strongest move <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.

In a conversational setting, a "zero-training" Monte Carlo Tree Search (MCTS) model can be designed by prompting LLMs (e.g., ChatGPT) to act as policy, simulate action outcomes, and evaluate action quality <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>. To account for human variability, an "open-loop MCTS" is used, where the model stochastically samples simulated conversational strategies <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

This approach, exemplified by "GDP0," has shown to generate more persuasive, natural, and coherent dialogues without human training data, leading to better donation conversion rates in persuasion tasks <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. It allows models to self-discover task information, such as delaying the "big ask" and diversifying persuasion strategies <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

#### Reflective Monte Carlo Tree Search (RMCTS) for Diverse Agent Tasks
To extend these capabilities to broader [[building_and_improving_ai_agents | AI agent tasks]] beyond dialogue, such as tool use and manipulation, a method called "RL MCTS" (Reflective Monte Carlo Tree Search) was introduced <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. This search algorithm explores vast action spaces and improves decision-making by incrementally building a search tree <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.

Key enhancements of RMCTS include:
*   **Contrastive Reflection**: Agents learn from past interactions (successes and errors) and dynamically improve search efficiency. This experience is saved to a vector database, caching learned knowledge for future tasks <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.
*   **Multi-Agent Debate for State Evaluation**: Instead of a single prompt, two LLMs debate the quality of an action (why it's good or bad) to provide a more robust and holistic evaluation, counterbalancing biases <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

RMCTS has been evaluated on benchmarks like Visual Web Arena (browser-based tasks like shopping or Reddit) and OS World (computer desktop tasks like navigating file systems or using V code) <a class="yt-timestamp" data-t="00:31:43">[00:31:43]</a>. It significantly outperforms other search algorithms and non-search methods, demonstrating that augmenting visual [[large_language_models | large language models]] with search algorithms can improve performance without additional human supervision <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.

### Exploratory Learning
The knowledge obtained through these search processes can be transferred into the training process of the base [[large_language_models | large language model]] through "exploratory learning" <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>. Unlike imitation learning (direct transfer of best actions), exploratory learning treats the tree search process as a single trajectory. The model learns how to linearize the search tree traversal, motivating it to explore, backtrack, and evaluate its actions <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. This approach teaches the model to improve its decision processes autonomously <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>.

For example, given a task like "find the recent coffee maker with a touchscreen, then comment 'grade item'," the agent learns to perform an action, realize it didn't lead to the desired state, then backtrack and try other actions <a class="yt-timestamp" data-t="00:34:56">[00:34:56]</a>.

## Future Directions

Current research focuses on:
*   Improving [[reinforcement_learning_in_large_language_models | RL methods]] to reduce reliance on the search tree <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.
*   Developing model predictive control methods to reduce the cost of environment setup and interaction <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>.
*   Enhancing control abilities and autonomous exploration for agent orchestration layers <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

The open-source ArCollex AI agent framework is being developed to integrate these research advancements, offering features like continuous learning and task decomposition <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. Advancing AI agents requires a multidisciplinary approach, combining machine learning expertise with systems, HCI, and security expertise <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

Future challenges include:
*   **Multi-task, Single-Agent Scenarios**: How one agent can perform multiple tasks on the same computer efficiently, addressing scheduling, database interaction, and human handover <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Multi-User, Multi-Agent Planning**: The complexity of multiple humans interacting with different agents, assigning tasks, and managing potential adversarial settings <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.

Establishing more realistic benchmarks with system integrations and algorithms that consider not just task completion but also efficiency and security will be crucial for future applications <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.