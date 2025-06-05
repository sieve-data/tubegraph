---
title: Multitagent collaborations and communication
videoId: D7_ipDqhtwk
---

From: [[aidotengineer]] <br/> 

The evolution of AI has seen a progression from simple features to complex, autonomous systems. Initially, building AI involved creating very simple features like summarization, classification, and extraction, which felt like magic just a few years ago but are now considered basic capabilities <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. As products matured, the approach became more sophisticated, leading to the orchestration of multiple model calls in predefined control flows, termed "workflows" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. These workflows allowed for trading off cost and latency for better performance <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## The Rise of Agentic Systems

Workflows are seen as the beginning of [[AI agents and agentic workflows | agentic systems]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Modern models are increasingly capable, leading to the emergence of domain-specific agents in production <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Unlike workflows, agents can determine their own trajectory and operate almost independently based on environmental feedback <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

The future of [[AI agents and agentic workflows | agentic systems]] in production is still unfolding <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Single agents could become more general-purpose and capable, or we might see [[Multiagent systems in AI | collaboration and delegation in multi-agent settings]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. A key trend is that as these systems are given more agency, they become more useful and capable, though this also increases the cost, latency, and consequences of errors <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### When to Build an Agent

It's crucial not to build agents for every task <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Agents are best suited for scaling complex and valuable tasks, not as a drop-in upgrade for every use case <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Workflows remain a practical way to deliver value for simpler, more defined tasks <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Consider the following checklist for building an agent:
*   **Complexity of Task**: Agents excel in ambiguous problem spaces <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. If a decision tree can be easily mapped, building it explicitly is more cost-effective and offers greater control <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Value of Task**: Agent exploration can consume many tokens, so the task must justify the cost <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. High-volume, low-budget tasks are often better served by workflows <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Critical Capabilities**: Ensure there are no significant bottlenecks in the agent's trajectory <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Bottlenecks can multiply cost and latency, suggesting a need to reduce scope or simplify the task <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Cost of Error and Discovery**: High-stakes or hard-to-discover errors make it difficult to trust agents with autonomy <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Mitigation through limited scope or human-in-the-loop involvement can also limit scalability <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

Coding is cited as a prime use case for agents due to its complexity, high value, compatibility with existing tools, and verifiable output through unit tests and CI <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Components of an Agent

Agents are fundamentally models using tools in a loop <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The three core components defining an agent are:
1.  **Environment**: The system in which the agent operates <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **Tools**: Provide an interface for the agent to take action and receive feedback <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
3.  **System Prompt**: Defines the agent's goals, constraints, and ideal behavior within the environment <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

Keeping these components simple is crucial for iteration speed, as complexity upfront can hinder development <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Optimizations should come after the basic behaviors are established <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

## Thinking Like an Agent

To effectively [[Developing AI agents and agentic workflows | develop AI agents and agentic workflows]], it's vital to "think like your agents" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Agents operate based on a very limited set of context, typically 10 to 20k tokens <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. Understanding their world view within this constrained context helps bridge the gap between human and agent understanding <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

For instance, a computer-use agent only receives a static screenshot and a brief description <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. While the agent's inference and tool execution occur, it's akin to operating a computer blind for several seconds, without immediate feedback <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This perspective highlights the need for crucial context, such as screen resolution, recommended actions, and limitations, to guide exploration and avoid unnecessary steps <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

AI models can also help in understanding agent behavior. Developers can ask a model like "Cloud" to:
*   Assess if system prompt instructions are ambiguous or make sense <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Determine if the agent knows how to use a tool based on its description, and if it needs more or fewer parameters <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   Explain its decision-making process by providing its entire trajectory and asking for suggestions for better decisions <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

## Future Musings and Open Questions

Several key areas and open questions remain for the future of [[AI agents and agentic workflows | AI agents]] and [[Multiagent systems in AI | multiagent systems in AI]]:

*   **Budget Awareness**: Agents need to become more budget-aware regarding cost and latency, unlike workflows where control is clearer <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Defining and enforcing budgets for time, money, and tokens is a crucial open question <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

*   **Self-Evolving Tools**: The concept of agents designing and improving their own tool ergonomics is emerging <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This meta-tool capability would make [[AI agents beyond chatbots | agents more general-purpose]] as they could adapt tools for specific use cases <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

*   **Multi-Agent Collaborations and Communication**: A strong conviction exists that more [[Multiagent orchestration in AI copilot systems | multi-agent collaborations]] will be seen in production by the end of the year <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. These systems offer benefits like parallelization, clear separation of concerns, and sub-agents protecting the main agent's context window <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

    A significant open question is [[MultiAgent Systems and APIBased Communication | how these agents will communicate with each other]] <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. Current systems often operate within a rigid frame of synchronous user-assistant interactions <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Expanding to asynchronous communication and enabling more roles for agents to communicate and recognize each other is vital for the future of [[Multiagent systems in AI | multi-agent systems]] <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.