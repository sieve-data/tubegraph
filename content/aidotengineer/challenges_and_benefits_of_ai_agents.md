---
title: Challenges and benefits of AI agents
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

AI agents are generating significant discussion, with experts holding varied opinions on their capabilities and future. While some are highly optimistic about their potential, others voice concerns about their current limitations <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Defining AI Agents

An AI agent is not a new concept <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The recent increase in their power is largely due to the advancement of large language models (LLMs) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. AI agents operate through a cyclical process:
1.  **Perception**: Agents must understand their environment by sensing information from various sources like text, images, audio, video, and touch <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Reasoning**: After perceiving information, agents process it to understand how to complete tasks, break them down into steps, and identify appropriate tools or actions <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This inner planning often involves a "chain of thought" reasoning, typically powered by LLMs <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
3.  **Reflection (Meta-reasoning)**: Agents can perform meta-reasoning steps, asking themselves if a choice was correct after executing an action and, if not, going back to reconsider <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Actions**: These are any performances an agent executes, such as talking to a human or moving from point A to point B <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
In essence, agents interact with their environment through actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Levels of Autonomy

The difficulty in deploying AI agents can be understood through an analogy to the levels of autonomy in self-driving cars <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>:
*   **Level 1 (Chatbot)**: Similar to initial chatbots (around 2017), focused on retrieving information <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2 (Agent Assist)**: An agent assists a human, like a customer service agent using an LLM to suggest responses that still require human approval before sending <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3 (Agent as a Service)**: LLMs automate AI workflows, offering services like booking meetings or writing job descriptions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4 (Autonomous Agents)**: An agent can delegate and perform multiple, interrelated tasks, sharing components, knowledge, and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5 (Jarvis-like)**: Complete trust in agents, delegating all security measures like keys, allowing agents to perform entirely on behalf of the user <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

While self-driving cars are high-risk agents where errors can be fatal, AI agents can be separated into low-risk and high-risk tasks <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Low-risk tasks, such as filing reimbursements, can benefit from human supervision initially and gain trust over time for full automation <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. Customer-facing tasks are typically considered high-risk, but the progression from back-office to front-office deployment is anticipated <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Benefits and Potential of AI Agents
Prominent figures are very bullish on AI agents, viewing them as a massive advancement in AI progress <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Revolution in Computing**: Bill Gates sees agents as the "biggest revolution in computing" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Significant AI Progress**: Andrew Ng describes it as "massive AI progress" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Year of the Agent**: Sam Altman from OpenAI suggested 2025 could be "the year of agent" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Improved Performance**: Methods like reflection and tree search can significantly improve an agent's ability to reason, plan, and perform tasks <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Self-Discovery**: Agents can self-discover task-specific information, like optimal persuasion strategies in dialogue tasks, diversifying their approaches (e.g., emotional vs. logical appeal) <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
*   **Reduced Human Supervision**: Improvements can be achieved without explicit human supervision data, by using synthetic data and on-policy data generation <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Test-Time Scaling**: Existing pre-trained models can achieve better results by being given more steps or "budgets" during inference, allowing for more in-depth reasoning and reflection <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
*   **Broader Application**: The ability to perform complex tasks like web browsing (Visual Web Arena) and operating system tasks (OS World) demonstrates the wide applicability of these agents <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.

## Challenges and Solutions in Building AI Agents

Despite the optimism, there are [[challenges_in_ai_agent_development | challenges in AI agent development]]. Some dismiss current agents as mere "simple wrappers of large language models" that "really can't plan" or solve practical solutions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Technical Challenges

*   **Self-Improvement with Smaller Models**:
    *   **Noise Propagation**: Smaller LLMs (e.g., LLaMA 7B) can generate "noisy" feedback that propagates into correction steps, hindering improvement (the "blind leading the blind" problem) <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
    *   **Incompatibility of Logics**: Feedback generated by larger models or verifiers might not be compatible with the internal logic or demonstration style of smaller models, rendering the feedback useless <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   **Solution: Distillation and Edited Feedback**: One approach is to use a larger LLM to *edit* the smaller model's feedback, tailoring it to the smaller model's internal logic, or use external tools like Python scripts for more accurate feedback <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This process, called "self-refine" or "self-improvement," involves iterating on feedback and corrections <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Scaling Laws and Data Limitations**:
    *   The performance of LLMs is linearly correlated with compute, data size, and parameter size <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.
    *   **Data Scarcity**: There's a "million-dollar question" on how to generate more and better diversified data, as there's effectively "one internet" of data <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
    *   **Parameter Limits**: Increasing parameters without abundant, diversified data makes models harder to improve <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
*   **Eliciting Better Behaviors/Planning**:
    *   Pre-training LLMs is resource-intensive and often only feasible for large organizations like Google or OpenAI <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
    *   **Solution: Test-Time Scaling**: Instead of re-training, significant improvements can be achieved by giving models more steps or "budget" during inference (test time) to perform processes like "think step by step" or "reflection" <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
    *   **Monte Carlo Tree Search (MCTS)**: Applied to sequential decision-making tasks (like dialogue or chess), MCTS allows agents to simulate future actions and outcomes to choose the best move <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
        *   In conversational settings, "Zero-training MCTS" prompts an LLM to act as a policy, simulate action outcomes, and evaluate action quality, while another LLM simulates the user <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
        *   Open-loop MCTS accounts for human response variance, allowing for stochastic sampling of simulated conversations <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
    *   **Reflective MCTS (RMCTS)**: This algorithm extends MCTS by incorporating contrastive reflection, allowing agents to learn from past interactions and dynamically improve search efficiency. It also uses multi-agent debate for more reliable state evaluation instead of single prompts <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
    *   **Memory Module**: RMCTS equips the system with a memory module to improve behavior across different tasks. Experiences (successes or errors) are saved to a vector database, allowing the agent to retrieve similar reflections for future tasks <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.
*   **Learning from Search Processes**:
    *   **Solution: Exploratory Learning**: Instead of simple imitation learning (training on the best action found), exploratory learning treats the tree search process as a single trajectory. The model learns how to linearize the search tree traversal, motivating it to learn how to explore, backtrack, and evaluate its own actions <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. This enables the model to improve its decision processes independently <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

## Future [[development_and_challenges_of_ai_agents | Development and Challenges of AI Agents]]

Ongoing [[technical_challenges_in_ai_agent_development | technical challenges in AI agent development]] include <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>:
*   Developing better reinforcement learning (RL) methods to reduce reliance on the search tree <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.
*   Implementing model predictive control methods to reduce expensive environment setup and interaction <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>.
*   Improving control abilities and autonomous exploration for agent orchestration layers <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

Beyond single-agent, single-task benchmarks, future [[challenges_and_solutions_in_building_ai_agents | challenges and solutions in building AI agents]] will involve system-level problems when a human wants a model to perform multiple tasks on the same computer <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>:
*   Scheduling <a class="yt-timestamp" data-t="00:37:49">[00:37:49]</a>.
*   Interacting with databases to avoid side effects <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
*   Enhanced security measures for human handover and supervision requests <a class="yt-timestamp" data-t="00:37:55">[00:37:55]</a>.
*   **Multi-user, Multi-agent Planning**: This is even more complex, especially in a community setting where multiple humans interact with various agents for different tasks, leading to diverse settings that need quantification <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.

The aim is to establish more realistic benchmarks that integrate system considerations and algorithms that prioritize not only task completion but also efficiency and security, forming the basis for future applications <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.