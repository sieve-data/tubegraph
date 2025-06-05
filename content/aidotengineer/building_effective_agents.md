---
title: Building effective agents
videoId: D7_ipDqhtwk
---

From: [[aidotengineer]] <br/> 

Barry introduces the topic of [[building_effective_ai_agents | building effective agents]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Approximately two months prior, he and Eric co-authored a blog post titled "[[building_effective_ai_agents | Building Effective Agents]]" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This post shared opinions on what an agent is and isn't, alongside practical insights gained during their work <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The discussion expands on three core ideas from that blog post <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>:

1.  Don't build agents for everything <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Keep it simple <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
3.  Think like your agents <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Evolution of AI Systems

The journey to [[ai_agents_and_agentic_workflows | agentic systems]] began with simple features like summarization, classification, and extraction, which were considered "magic" a few years ago but are now commonplace <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. As products matured, developers became more creative, often requiring multiple model calls <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This led to orchestrating these calls in predefined control flows, known as workflows <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Workflows allowed a trade-off between cost and latency for improved performance, marking the beginning of [[ai_agents_and_agentic_workflows | agentic systems]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

Currently, models are more capable, leading to the emergence of domain-specific agents in production <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Unlike workflows, agents can determine their own trajectory and operate nearly independently based on environmental feedback <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

The future of [[ai_agents_and_agentic_workflows | agentic systems]] might involve single agents becoming more general-purpose or the development of multi-agent collaborations with delegation <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. As systems are given more agency, they become more useful and capable, but also incur higher costs, increased latency, and greater consequences for errors <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## When to Build Agents: A Checklist

[[building_effective_ai_agents | Agents]] are ideal for scaling complex and valuable tasks, not as a universal upgrade for every use case <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Workflows remain a valuable and concrete method for delivering value today <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

[!INFO] Checklist for [[building_effective_ai_agents | Building Agents]]
*   **Complexity of Task**: Agents excel in ambiguous problem spaces <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. If a decision tree can be easily mapped, explicitly building and optimizing it is more cost-effective and provides greater control <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Value of Task**: The exploration involved in agentic tasks consumes many tokens, so the task's value must justify the cost <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For high-volume, low-budget tasks (e.g., customer support), a workflow for common scenarios might capture most of the value <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Derisk Critical Capabilities**: Ensure there are no significant bottlenecks in the agent's trajectory <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. For a coding agent, this means ensuring it can write good code, debug, and recover from errors <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Bottlenecks multiply cost and latency, suggesting a need to reduce scope and simplify the task <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Cost of Error and Error Discovery**: If errors are high-stakes and difficult to discover, it becomes challenging to trust the agent with autonomy <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Mitigation strategies include limiting scope (e.g., read-only access) or incorporating more human-in-the-loop interaction, though this also limits scalability <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Coding as an Agent Use Case

Coding is an excellent use case for [[building_effective_ai_agents | agents]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>:
*   The process from design document to pull request is ambiguous and complex <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   Good code holds significant value <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   Models like Claude are proficient in many parts of the coding workflow <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   Coding output is easily verifiable through unit tests and Continuous Integration (CI) <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This verifiability is a key reason for the proliferation of creative and successful coding agents <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Keep It Simple

Once a suitable use case for [[building_effective_ai_agents | agents]] is identified, the second core idea is to maintain simplicity <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Agents are fundamentally models utilizing tools in a loop <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

The three defining components of an agent are <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:
1.  **Environment**: The system in which the agent operates <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **Tools**: An interface that allows the agent to take action and receive feedback <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
3.  **System Prompt**: Defines the agent's goals, constraints, and ideal behavior within the environment <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

The model is then called in a loop <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. It is crucial to keep this structure simple, as complexity upfront significantly hinders iteration speed <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Iterating on these three basic components yields the highest return on investment (ROI), with optimizations to follow later <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

Different agent use cases may appear distinct in product surface, scope, and capability, but often share nearly identical backbones and code <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. The environment depends on the use case, leaving the choice of tools and system prompt as the primary design decisions <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

Once these basic components are established, various optimizations can be applied <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>:
*   Caching trajectories for coding and computer use to reduce cost <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   Parallelizing tool calls for search-heavy agents to reduce latency <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   Presenting agent progress clearly to build user trust <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

The advice remains: keep it as simple as possible during iteration, focusing on these three core components first, and then optimize once desired behaviors are achieved <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Think Like Your Agents

A common mistake in [[developing_ai_agents_and_agentic_workflows | developing agents]] is to approach them from a human perspective, leading to confusion when agents make unexpected errors <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The recommendation is to place oneself in the agent's context window <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

While agents can exhibit sophisticated and complex behaviors, at each step, the model is merely running inference on a highly limited set of contexts <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Everything the model knows about the current state of the world is contained within 10-20k tokens <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Limiting one's own understanding to this context helps determine if it's sufficient and coherent, offering a better grasp of how agents perceive the world <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

### An Agent's Perspective: Computer Use Case

Imagine being a computer use agent <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>:
*   Input is a static screenshot and a brief, often poorly written, description (e.g., "You are a computer use agent. You have a set of tools and you have a task.") <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   Despite internal reasoning, only actions taken through tools affect the environment <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   During inference and tool execution, it's akin to "closing eyes" for 3-5 seconds and operating in the dark <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   Opening "eyes" reveals a new screenshot, but the outcome of the previous action (success or failure) is unknown <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This "lethal phase" perpetuates the cycle <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

Performing a full task from an agent's perspective reveals crucial contextual needs, such as screen resolution for accurate clicks or recommended actions and limitations to guide exploration and prevent unnecessary steps <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

Fortunately, since systems speak our language, one can directly query the model (e.g., Claude) <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>:
*   Ask if system prompt instructions are ambiguous or make sense <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Inquire if the agent understands how to use a tool, or if it needs more/fewer parameters <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   Feed the entire agent's trajectory back to the model and ask why a decision was made, or how to facilitate better future decisions <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

This process, while not replacing human understanding, helps bridge the gap between human and agent perceptions, aiding in [[best_practices_for_building_ai_agents | building AI agents]] more effectively <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## Personal Musings and Open Questions

Barry shares personal reflections on the evolution of [[ai_agents_and_agentic_workflows | AI agents]] and open questions for [[building_effective_ai_agents | AI engineers]] <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>:

*   **Budget-Aware Agents**: Unlike workflows, controlling cost and latency for agents is challenging <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Defining and enforcing budgets (time, money, tokens) is crucial for deploying agents in production and enabling more use cases <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. This relates to [[challenges_in_creating_effective_ai_agents | challenges in creating effective AI agents]].
*   **Self-Evolving Tools**: Models are already assisting in iterating on tool descriptions <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This concept could generalize into a meta-tool allowing agents to design and improve their own tool ergonomics <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This would make agents more general-purpose by enabling them to adapt tools for each use case, impacting [[designing_and_optimizing_agent_environments | designing and optimizing agent environments]] and [[building_ai_agents_using_primitives | building AI agents using primitives]].
*   **Multi-Agent Collaborations**: There is a strong conviction that multi-agent collaborations will be widespread in production by the end of the year <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. These systems offer benefits like parallelism, separation of concerns, and protection of main agent context windows via sub-agents <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. A key open question is how these agents will communicate beyond rigid synchronous user-assistant turns, exploring asynchronous communication and enabling more diverse roles for agent interaction <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. This is critical for [[developing_ai_agents_for_productivity | developing AI agents for productivity]] and [[ai_agents_and_agentic_workflows | agentic workflows]].

## Key Takeaways

The three core takeaways for [[building_effective_ai_agents | building effective agents]] are <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>:
1.  Don't build agents for everything <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
2.  If you find a good use case, keep the agent as simple as possible for as long as possible <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
3.  As you iterate, think like your agent, gain their perspective, and help them do their job <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.