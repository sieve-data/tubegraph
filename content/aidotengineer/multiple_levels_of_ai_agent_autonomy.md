---
title: Multiple levels of AI agent autonomy
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

The concept of AI agents is not new, but large language models have significantly enhanced their capabilities <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Bill Gates is bullish on agents, calling them the "biggest revolution in computing," and Andrew Ng considers them a "massive AI progress" <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>. Sam Altman from OpenAI predicts 2025 as the "year of agent" <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

AI agents generally operate through a process involving perception, reasoning, reflection, and actions <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. Like humans, agents perceive their environment through sensory information (text, image, audio, video, touch) <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. This information then goes through a reasoning process to understand tasks, break them down into steps, and identify appropriate tools or actions <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. This inner planning process is often referred to as "chain of thoughts reasoning," powered by large language models <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. Agents can also perform "meta reasoning" or "reflection," evaluating whether an action was correct and deciding to backtrack if not <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. Finally, actions are any operations performed by the agent, such as talking to humans or moving physically <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Agents interact with their environment through these actuations of actions <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

To understand the ease of deploying agents, an analogy with the different levels of autonomy in self-driving cars can be used <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

## Levels of AI Agent Autonomy

### Level 1: Chatbot (2017)
At this foundational level, AI agents primarily retrieve information <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

### Level 2: [[evaluating_ai_agents_and_assistance | Agent Assist]]
In this stage, agents, such as customer service AI, use large language models to generate suggested responses <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. However, a human still needs to approve the final message before it's sent <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

### Level 3: [[developing_ai_agents_for_productivity | Agent as a Service]]
This current level involves using large language models to automate AI workflows, functioning as a service <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. Examples include automated meeting bookings or writing job descriptions <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

### Level 4: [[building_effective_ai_agents | Autonomous Agents]]
At this level, an AI agent can delegate and perform multiple tasks simultaneously <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. These tasks often have interconnections, sharing components, knowledge, and resources <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

### Level 5: Jarvis / Iron Man
This is the highest level of autonomy, where users trust agents 100% and delegate all security measures, such as keys, for the agents to perform actions on their behalf <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

### Risk Levels in AI Agent Tasks
While a self-driving car is an example of an agent performing perception, reasoning, planning, and executing driving actions, it's considered a very high-risk application where errors could be life-threatening <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.

AI agent tasks can be separated into:
*   **Low-risk tasks** <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>: These include back-office tasks like filing reimbursements, where human supervision can be maintained initially and trust can be built over time for full automation <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
*   **High-risk tasks** <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>: Customer-facing tasks are typically considered higher-risk <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>. The progression is often from automating back-office tasks to front-office tasks over time <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

## Improving AI Agent Performance
Research aims to improve large language models for better reasoning and reflection, elicit better behaviors for AI agent tasks, and learn from past examples to optimize models for agent tasks <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.

One method for self-improvement involves prompting models to generate feedback and then iteratively refining their answers, a process called self-refinement or self-improvement <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>. This can involve using a larger language model to edit the feedback generated by a smaller model, making it more tailored to the smaller model's internal logic <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.

Another approach focuses on "test time scaling," where existing pre-trained models are given more steps or budget during inference to achieve better results <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>. This involves more complex tree search processes like Monte Carlo Tree Search (MCTS), which can significantly improve performance <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>. For example, in dialogue tasks, MCTS can simulate possible conversational strategies to drive real-world decision-making <a class="yt-timestamp" data-t="25:50:00">[25:50:00]</a>.

New algorithms like R-MCTS incorporate contrastive reflection and [[multiagent_systems_in_ai | multi-agent]] debate to improve decision-making <a class="yt-timestamp" data-t="28:48:00">[28:48:00]</a>. By equipping the system with a memory module, it can learn from past interactions and dynamically improve search efficiency across different tasks <a class="yt-timestamp" data-t="29:39:00">[29:39:00]</a>. This method has shown significant improvements in benchmarks like Visual Web Arena and OS World <a class="yt-timestamp" data-t="32:18:00">[32:18:00]</a>.

Furthermore, "exploratory learning" can teach models how to explore, backtrack, and evaluate during a search process, leading to improved decision-making <a class="yt-timestamp" data-t="33:55:00">[33:55:00]</a>.

## [[challenges_in_ai_agent_development | Future Directions]] and [[best_practices_for_building_ai_agents | Best Practices for Building AI Agents]]
Ongoing work focuses on improving control abilities and autonomous exploration for the [[multiagent_orchestration_in_ai_copilot_systems | agent orchestration layer]] <a class="yt-timestamp" data-t="36:27:00">[36:27:00]</a>. This involves integrating machine learning expertise with systems, HCI, and security expertise for more practical advancements <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>.

Current benchmarks often focus on single agents performing single tasks <a class="yt-timestamp" data-t="37:25:00">[37:25:00]</a>. Future challenges include [[scaffolding_ai_agents_for_scalability | scaling]] to scenarios where a single human wants a model to perform multiple tasks on the same computer, leading to system-level problems like scheduling, database interaction, security, and human handover points <a class="yt-timestamp" data-t="37:37:00">[37:37:00]</a>. Even more complex are multi-user, [[multiagent_systems_in_ai | multi-agent]] planning scenarios <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>. Establishing realistic benchmarks that consider system integrations, efficiencies, and securities, beyond just task completion, is a key area of focus <a class="yt-timestamp" data-t="38:25:00">[38:25:00]</a>.