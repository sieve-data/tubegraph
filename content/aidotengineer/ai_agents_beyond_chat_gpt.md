---
title: AI agents beyond chat GPT
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

AI agents are a significant area of discussion, with figures like Bill Gates, Andrew Ng, and Sam Altman highlighting their transformative potential in computing and AI progress <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. While some critics view them as mere wrappers for large language models (LLMs) or question their practical solution capabilities, understanding their definition and components is key <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## What Are AI Agents?
AI agents are not a new concept, but the advent of large language models has significantly enhanced their capabilities <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The core components of an AI agent are:
*   **Perception** Like humans, agents must understand their environment by sensing information from text, images, audio, video, and touch <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Reasoning** After perceiving information, agents process it to understand how to complete tasks, break them into individual steps, and decide which tools or actions to take <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This inner planning often involves "Chain of Thoughts" reasoning, typically powered by LLMs <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Reflection (Meta-Reasoning)** Agents can perform meta-reasoning steps, reflecting on executed actions to evaluate if the correct choice was made and adjust if necessary <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Actions** Any performance an agent undertakes, such as talking to a human or moving from point A to point B, constitutes an action <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

In essence, [[Components of AI agents | AI agents]] interact with their environment through the actuation of actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Levels of Autonomy for AI Agents
The deployment of AI agents can be understood through an analogy to the levels of autonomy in self-driving cars <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:
*   **Level 1: Chatbot** (e.g., pre-2017 chatbots) Simply retrieves information <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2: Agent Assist** A human customer service agent uses an LLM to generate suggested responses but must approve sending messages <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3: Agent as a Service** LLMs automate AI workflows, offering services like booking meetings or writing job descriptions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4: Autonomous Agents** A single agent can delegate and perform multiple, interconnected tasks that share components, knowledge, and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5: JARVIS (Iron Man Analogy)** Full trust in agents, delegating all security measures and keys for agents to perform on behalf of the user <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

While self-driving cars represent a high-risk agent application, AI agents can be applied to both low-risk (e.g., filing reimbursements with human supervision) and high-risk tasks (e.g., customer-facing interactions) <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Over time, the goal is to transition from back-office to front-office deployments <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

## [[Building and Improving AI Agents | Improving AI Agents]]
Strategies to improve LLMs for better reasoning and reflection in AI agent tasks include:

### Self-Improvement Through Reflection
Self-improvement processes involve LLMs generating feedback on their own answers and then using that feedback to refine their responses <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This "self-refined" or "self-improvement" process can be iterated multiple times until a correct answer is reached <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

However, smaller LLMs (e.g., Llama 7B) can generate "noise" in their feedback, leading to degraded results ("the blind is leading the blind") <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
Additionally, internal logic and demonstrations from larger models may be incompatible with smaller models, making their feedback unhelpful <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

To address this, a method called WiGlass proposes:
1.  Using a smaller model to generate an initial answer and self-feedback <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
2.  Employing a larger language model or external tool (like Python scripts for math tasks) to *edit* the smaller model's feedback, making it more tailored to the smaller model's internal logic <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
3.  Using this corrected feedback to update the answer, iterating until the problem is solved correctly <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

This process generates "traces" of trial and error that can be filtered and used to train smaller models for self-improvement, guided by larger models or tools <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This "on-policy self-supervision" has shown significant performance improvements in mathematical reasoning tasks (e.g., 48% accuracy after three iterations) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

### Test-Time Scaling for Stronger Model Behavior
While pre-training LLMs is compute-intensive and often beyond smaller organizations' budgets, "test-time scaling" offers an alternative <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. This approach involves taking an existing model and providing it with more steps or budget during inference to elicit better results <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

One method for this is **Tree Search**, specifically Monte Carlo Tree Search (MCTS), applied to LLMs.
*   **Conversational Agents:** In tasks like donation persuasion, MCTS allows an agent to simulate potential moves and opponent responses (e.g., "what's my opponent going to do") multiple steps ahead, similar to a chess game <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. This "self-play" involves prompting one LLM to act as the policy (propose actions) and another to simulate user responses and evaluate action quality <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
    *   This approach, termed GPD-Zero (based on AlphaGo's zero-training principle), does not require explicit training data and uses simulation to achieve competitive results <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Human studies showed models using this planning algorithm achieved higher donation rates and were perceived as more convincing and natural <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. Agents self-discovered strategies like delaying the "big ask" and diversifying persuasion tactics <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

*   **Visual Web Agents:** Expanding beyond conversational tasks, [[building_singlepurpose_ai_agents | AI agents]] need to perceive visual information and perform actions like clicking buttons based on screenshots <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. Traditional visual language models (VLMs) trained on Visual Question Answering (VQA) are insufficient for action-based tasks <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. For instance, humans achieve 88% success on tasks like "clear my shopping carts" on Visual Web Arena, while a basic GPT-4V gets only 16% <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

    *   **RL MCTS:** An algorithm called RL MCTS (Reinforcement Learning Monte Carlo Tree Search) was introduced to improve decision-making in these environments <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. It extends simple MCTS by incorporating:
        *   **Contrastive Reflection:** Allows agents to learn from past interactions and dynamically improve search efficiency <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. This involves a memory module that caches learned knowledge from previous tasks, allowing retrieval of similar reflections for future tasks <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.
        *   **Multi-Agent Debate:** Uses a debate format to get more robust state evaluations, asking models to argue for why an action is good or bad to counteract biases from single-model prompting <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.
    *   RL MCTS outperformed existing search algorithms and non-search methods on benchmarks like Visual Web Arena (browser tasks) and OS World (Linux computer tasks) <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>. This demonstrated that augmenting VLMs with search algorithms can improve performance without additional human supervision <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.

### Exploratory Learning
Beyond test-time compute, the knowledge obtained through search processes can be transferred into the training process of the base LLM <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>.
*   Unlike *imitation learning* (direct transfer of best actions), *exploratory learning* treats the tree search process as a single trajectory <a class="yt-timestamp" data-t="00:33:45">[00:33:45]</a>.
*   The model learns to linearize the search tree traversal, motivating it to learn how to explore, backtrack, and evaluate its own decisions <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>. This teaches the model the decision-making process itself, rather than just providing the final correct answer <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>.

## Future Directions for AI Agents
Current benchmarks often focus on a single agent performing a single task <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. Future work needs to address more complex scenarios:
*   **Multi-Tasking:** How a single human can have a model perform multiple tasks on the same computer <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **System-Level Problems:** Scheduling, database interactions (to avoid side effects), and improved security, including human handover and supervision requests <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
*   **Multi-User, Multi-Agent Planning:** When multiple humans interact with various agents, assigning different tasks, leading to more complicated planning scenarios <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.

Establishing more realistic benchmarks that integrate system considerations alongside algorithms will be crucial for developing applications that prioritize task completion, efficiency, and security <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

For those interested in exploring these advancements, the ARCollex AI open-source agent framework offers features like continuous learning and task decomposition for developers <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.