---
title: Criteria for building agents
videoId: D7_ipDqhtwk
---

From: [[aidotengineer]] <br/> 

Barry, a speaker from an AI engineer summit, discusses key insights for [[building_effective_ai_agents | building effective AI agents]], drawing from a blog post titled "[[building_effective_agents | Building Effective Agents]]" co-written with Eric <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The article shares opinionated takes on what an agent is and isn't, along with practical learnings <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This discussion focuses on three core ideas: not building agents for everything, keeping it simple, and thinking like your agents <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## The Evolution to Agentic Systems

The journey of AI development has progressed from simple features like summarization, classification, and extraction, which were once considered magic but are now commonplace <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. As products matured, developers moved to orchestrating multiple model calls in predefined control flows, known as workflows, trading cost and latency for better performance <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This marked the beginning of [[the_emergence_and_significance_of_agent_engineering | agentic systems]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

Today, models are more capable, leading to the rise of domain-specific agents in production <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Unlike workflows, agents can determine their own trajectory and operate almost independently based on environment feedback <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The broad trend is that as these systems gain more agency, they become more useful and capable, but also incur higher costs, latency, and greater consequences for errors <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Core Ideas for Building Agents

### 1. Don't Build Agents for Everything

Agents are best suited for scaling complex and valuable tasks, not as a universal upgrade for every use case <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Workflows are often a more concrete and effective way to deliver value today <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

#### Agent Building Checklist:
*   **Complexity of Your Task** <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>: Agents thrive in ambiguous problem spaces <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. If the decision tree for a task can be easily mapped out, it's more cost-effective and provides more control to build that explicitly rather than using an agent <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Value of Your Task** <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>: The exploration involved in agentic behavior consumes many tokens, so the task must justify the cost <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. For high-volume customer support systems with a budget of around 10 cents per task (30-50,000 tokens), workflows for common scenarios are more practical <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Derisk Critical Capabilities** <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>: Ensure there are no significant bottlenecks in the agent's trajectory <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. For a coding agent, this means ensuring it can write good code, debug, and recover from errors <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Bottlenecks can multiply costs and latency, suggesting a need to reduce scope or simplify the task <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Cost of Error and Error Discovery** <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>: If errors are high-stakes and difficult to discover, it becomes challenging to trust the agent with autonomous actions <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. Mitigation strategies include limiting scope (e.g., read-only access) or incorporating more human-in-the-loop, though these can limit scalability <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

#### Example: Coding as a Great Agent Use Case
Coding is an ideal agent use case because:
*   Going from a design document to a pull request is a complex and ambiguous task <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   Good code has significant value <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   Models like Claude are already proficient at many parts of the coding workflow <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   Coding output is easily verifiable through unit tests and CI <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### 2. Keep it Simple

Once a good use case for agents is found, the second core idea is to keep the design as simple as possible <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Agents are fundamentally models using tools in a loop <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

#### Agent Components:
*   **Environment**: The system in which the agent operates <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **Tools**: Provide an interface for the agent to take action and receive feedback <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **System Prompt**: Defines the agent's goals, constraints, and ideal behavior within the environment <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

Complexity introduced upfront significantly hinders iteration speed <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Iterating on these three basic components offers the highest ROI <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Many different agent [[use_cases_and_applications_for_browser_agents | use cases and applications for browser agents]], such as coding agents, computer use agents, and search agents, share nearly identical backbones and codebases, differing mainly in environment, tools, and prompts <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

Optimizations, such as caching trajectories to reduce cost in coding, parallelizing tool calls in search to reduce latency, or presenting agent progress to build user trust, should come after the basic behaviors are established <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

### 3. Think Like Your Agents

A common pitfall for builders is developing agents from their own human perspectives, leading to confusion when agents make mistakes <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. It is recommended to put oneself in the agent's context window <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

Even though agents can exhibit sophisticated behavior, at each step, the model is performing inference on a very limited set of contexts, typically 10 to 20k tokens, which represents everything it knows about the current state of the world <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Limiting one's own understanding to this context helps determine if it's sufficient and coherent <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

For example, a computer use agent receives only a static screenshot and a poorly written description, then attempts actions without full visual feedback. This "lethal phase" is like closing one's eyes for 3-5 seconds while using a computer <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Experiencing a task from this limited perspective reveals crucial missing information, such as screen resolution for clicking or recommended actions to avoid unnecessary exploration <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

Models like Claude can also assist in [[evaluating the performance of browser agents | evaluating the performance of browser agents]] and improving agents <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>:
*   Asking if system prompt instructions are ambiguous or make sense to the model <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Checking if the agent understands how to use a tool based on its description, or if it needs more/fewer parameters <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   Analyzing the agent's entire trajectory with the model to understand decision-making and identify areas for improvement <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

## Future Considerations in Agent Engineering

Discussions around [[best_practices_for_building_ai_agents | best practices for building AI agents]] and [[strategies for developing and implementing browser agents | strategies for developing and implementing browser agents]] often touch on future challenges:
*   **Budget-Aware Agents**: Making agents more aware of cost and latency is crucial for production deployment <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Defining and enforcing budgets (time, money, tokens) is an open question <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Self-Evolving Tools**: Agents could design and improve their own tool ergonomics, becoming more general-purpose by adopting tools needed for specific use cases <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
*   **Multi-Agent Collaboration**: There is a strong conviction that multi-agent collaborations will become prevalent in production <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. They offer benefits like parallelization, separation of concerns, and protection of the main agent's context window <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. A key open question is how these agents will communicate beyond rigid synchronous user-assistant interactions, enabling asynchronous communication and diverse roles <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

## Summary

To summarize the criteria for [[building_effective_agents | building effective agents]]:
1.  **Don't build agents for everything**: Choose use cases wisely based on complexity, value, critical capabilities, and error costs <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
2.  **Keep it as simple as possible**: Focus on iterating with the core components – environment, tools, and system prompt – before optimizing <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
3.  **Think like your agent**: Gain their perspective by understanding their limited context window to improve their decision-making and job performance <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.