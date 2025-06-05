---
title: Designing and optimizing agent environments
videoId: D7_ipDqhtwk
---

From: [[aidotengineer]] <br/> 
Barry, a speaker and co-author of the blog post "[[building_effective_agents | Building Effective Agents]]", discusses three core ideas for [[building_effective_agents | building effective agents]]: not building agents for everything, keeping them simple, and thinking like the agents themselves <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. These principles are crucial for [[developing_ai_agents_and_agentic_workflows | developing AI agents and agentic workflows]], especially when considering the design and optimization of the environments in which they operate.

## Understanding Agentic Systems and Environments
The evolution of AI applications has moved from simple features like summarization and classification to more sophisticated workflows that orchestrate multiple model calls <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. These workflows are seen as the beginning of agentic systems <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. Unlike predefined workflows, agents can determine their own trajectory and act almost autonomously based on feedback from their environment <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. As these systems are given more agency, they become more useful and capable, but also incur higher costs, latency, and consequences for errors <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

## Components of an Agent and Its Environment
Agents are fundamentally conceptualized as models using tools in a loop <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. Three critical components define an agent:
1.  **The Environment**: This is the system in which the agent operates <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>. Its design largely depends on the specific use case <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.
2.  **Tools**: These offer an interface for the agent to perform actions and receive feedback within the environment <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.
3.  **System Prompt**: This defines the agent's goals, constraints, and ideal behavior within the given environment <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

Keeping these core components simple is crucial for rapid iteration and achieving a high return on investment (ROI) <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. Optimizations, such as trajectory caching to reduce cost or parallelizing tool calls to reduce latency, should be considered only after the basic behaviors of the agent are established <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.

## Thinking Like Your Agent for Better Environment Design
A common pitfall in [[developing_ai_agents_for_productivity | developing AI agents]] is designing them from a human perspective, leading to confusion when agents make unexpected mistakes <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. To overcome this, it's recommended to "put yourself in the agent's context window" <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

Agents, despite sophisticated behavior, operate by running inference on a very limited context (typically 10 to 20k tokens) <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. Everything the agent knows about the current state of the world is within this context <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>. It's vital to ensure this context is sufficient and coherent <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.

### Practical Application: Computer Use Agents
Consider a computer use agent that receives a static screenshot and a poorly written description. When it attempts an action, it's akin to closing one's eyes for a few seconds—it doesn't "see" what's happening during the tool execution and inference phase <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>. This "blind execution" is a significant challenge in the agent's interaction with its environment <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

By experiencing a task from the agent's perspective, developers can identify crucial environmental information that is missing. For a computer use agent, this might include:
*   Screen resolution to enable accurate clicks <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
*   Recommended actions and limitations to provide guardrails and avoid unnecessary exploration <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.

This exercise helps determine the precise context an agent needs to perform its task effectively within its environment <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.

### Using AI to Optimize Agent Environments
One method to optimize environment context is to use a model like Cloud to evaluate the agent's understanding:
*   Ask if instructions in the system prompt are ambiguous or make sense <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>.
*   Check if the agent knows how to use provided tool descriptions, and if it needs more or fewer parameters <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
*   Provide the agent's entire trajectory to the model and ask why a certain decision was made, or how to help it make better decisions <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.

This helps bridge the gap between human understanding and how the agent perceives its world, leading to more effective environmental design <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.

## Future Considerations for Agent Environments
Looking ahead, several [[future_of_ai_agent_ecosystems | future considerations]] will impact the design and optimization of agent environments:
*   **Budget Awareness**: Agents need to become more budget-aware regarding cost and latency, which is essential for deploying them in production <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>. Defining and enforcing budgets (time, money, tokens) within the environment will be critical <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.
*   **Self-Evolving Tools**: The concept of agents designing and improving their own tools and ergonomics will generalize, enabling agents to adapt tools for each use case, making them more general-purpose <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. This implies environments that can facilitate tool creation and refinement.
*   **Multi-Agent Collaboration**: The future will likely see more multi-agent collaborations in production, with agents having distinct roles and protecting each other's context windows <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>. A key open question is how these agents will communicate with each other beyond rigid, synchronous user-assistant interactions, potentially moving towards asynchronous communication and enabling more diverse roles <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>. This will require new paradigms for designing shared or interconnected environments.

These areas represent [[challenges_in_ai_agent_development | challenges in AI agent development]] and require collective effort from AI engineers to address.