---
title: Agentic systems and workflows
videoId: D7_ipDqhtwk
---

From: [[aidotengineer]] <br/> 

Barry discusses how to build effective [[ai_agents_and_agentic_workflows | agents]] and the evolution of [[ai_agents_and_agentic_workflows | agentic systems]] and [[ai_agents_and_agentic_workflows | workflows]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This presentation builds on a blog post titled "Building Effective [[ai_agents_and_agentic_workflows | Agents]]" co-written with Eric <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Three Core Ideas for Building Effective [[ai_agents_and_agentic_workflows | Agents]]
The presentation focuses on three key ideas:
1.  Don't build [[ai_agents_and_agentic_workflows | agents]] for everything <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Keep it simple <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
3.  Think like your [[ai_agents_and_agentic_workflows | agents]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Evolution of AI Systems
The progression of AI system development can be viewed in phases:
*   **Simple Features** Initially, developers built simple features like summarization, classification, and extraction, which were considered "magic" a few years ago but are now commonplace <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Workflows** As products matured, more sophisticated approaches emerged, involving the orchestration of multiple model calls in predefined control flows <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. These [[ai_agents_and_agentic_workflows | workflows]] allowed for a trade-off between cost and latency for better performance <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This is considered the beginning of [[ai_agents_and_agentic_workflows | agentic systems]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **[[AI agents and agentic workflows | Agents]]** Current models are more capable, leading to the emergence of domain-specific [[ai_agents_and_agentic_workflows | agents]] in production <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Unlike [[ai_agents_and_agentic_workflows | workflows]], [[ai_agents_and_agentic_workflows | agents]] can determine their own trajectory and operate almost independently based on environmental feedback <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Future Phases** Future [[ai_agents_and_agentic_workflows | agentic systems]] may involve single, more general-purpose [[ai_agents_and_agentic_workflows | agents]] or collaboration and delegation in multi-[[ai_agents_and_agentic_workflows | agent]] settings <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The broad trend is that as systems are given more agency, they become more useful and capable, but also increase costs, latency, and the consequences of errors <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## When to Build an [[ai_agents_and_agentic_workflows | Agent]]
[[ai_agents_and_agentic_workflows | Agents]] are best suited for scaling complex and valuable tasks, not every use case <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Workflows remain a great way to deliver value <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Checklist for Building an [[ai_agents_and_agentic_workflows | Agent]]
Before building an [[ai_agents_and_agentic_workflows | agent]], consider the following:
*   **Complexity of the Task** [[ai_agents_and_agentic_workflows | Agents]] excel in ambiguous problem spaces <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. If the decision tree is easily mapped, it's more cost-effective to build it explicitly and optimize each node <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Value of the Task** The exploratory nature of [[ai_agents_and_agentic_workflows | agents]] consumes many tokens, so the task must justify the cost <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For high-volume, low-budget tasks (e.g., customer support), a workflow for common scenarios might be more appropriate <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Critical Capabilities** De-risk essential capabilities to avoid bottlenecks that multiply cost and latency <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. For a coding [[ai_agents_and_agentic_workflows | agent]], this means ensuring it can write, debug, and recover from errors <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. If bottlenecks exist, reduce the scope and simplify the task <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Cost of Error and Error Discovery** High-stakes and hard-to-discover errors make it difficult to trust the [[ai_agents_and_agentic_workflows | agent]] with autonomy <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Mitigations like read-only access or human-in-the-loop involvement limit scalability <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Why Coding is a Great Use Case for [[AI agents and agentic workflows | Agents]]
Coding is an excellent use case for [[ai_agents_and_agentic_workflows | agents]] because <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>:
*   The task of going from a design document to a pull request is highly ambiguous and complex <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   Good code has significant value <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   Models like Claude are proficient in many parts of the coding workflow <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   Code output is easily verifiable through unit tests and Continuous Integration (CI) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Keeping [[AI agents and agentic workflows | Agents]] Simple
[[ai_agents_and_agentic_workflows | Agents]] fundamentally consist of models using tools in a loop <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Core Components of an [[ai_agents_and_agentic_workflows | Agent]]
Three components define an [[ai_agents_and_agentic_workflows | agent]] <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:
1.  **Environment** The system in which the [[ai_agents_and_agentic_workflows | agent]] operates <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **Tools** An interface for the [[ai_agents_and_agentic_workflows | agent]] to take action and receive feedback <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
3.  **System Prompt** Defines the goals, constraints, and ideal behavior for the [[ai_agents_and_agentic_workflows | agent]] within its environment <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

Keeping these components simple is crucial for iteration speed <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Iterating on these three basic components offers the highest ROI, with optimizations coming later <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Many different [[ai_agents_and_agentic_workflows | agent]] use cases share nearly identical backbones and code <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. The primary design decisions are the set of tools provided and the prompt instructing the [[ai_agents_and_agentic_workflows | agent]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Optimizations
Once the basic components are established, various optimizations can be applied <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>:
*   **Cost Reduction** For coding and computer use, caching trajectories can reduce costs <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Latency Reduction** For search, parallelizing tool calls can reduce latency <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **User Trust** Presenting the [[ai_agents_and_agentic_workflows | agent]]'s progress transparently helps gain user trust <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## Thinking Like Your [[AI agents and agentic workflows | Agent]]
It's common for developers to misunderstand [[ai_agents_and_agentic_workflows | agent]] behavior because they develop from their own perspective <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. To bridge this gap, developers should put themselves in the [[ai_agents_and_agentic_workflows | agent]]'s context window <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### [[AI agents and agentic workflows | Agent]]'s Limited Context
Despite sophisticated behavior, an [[ai_agents_and_agentic_workflows | agent]] at each step is only running inference on a very limited set of context, typically 10-20k tokens <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Limiting one's own understanding to this context helps determine if it's sufficient and coherent <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

For example, a computer use [[ai_agents_and_agentic_workflows | agent]] might only receive a static screenshot and a poorly written description, then attempt an action without truly "seeing" the environment <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. During inference or tool execution, the [[ai_agents_and_agentic_workflows | agent]] is effectively "blind," only receiving a new screenshot after the action is complete <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This "blind phase" can be very impactful <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Performing a task from this limited perspective reveals crucial missing context, such as screen resolution, recommended actions, and limitations to avoid unnecessary exploration <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### Using Models to Understand [[AI agents and agentic workflows | Agents]]
Since these systems speak human language, models can be used to gain insights into an [[ai_agents_and_agentic_workflows | agent]]'s perspective <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>:
*   Ask the model if instructions in the system prompt are ambiguous <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Query the model about its understanding and usage of tool descriptions <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   Provide the [[ai_agents_and_agentic_workflows | agent]]'s entire trajectory and ask it to explain its decisions or suggest ways to improve <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
This method helps gain a closer perspective on how the [[ai_agents_and_agentic_workflows | agent]] perceives the world <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Future Considerations for [[Agentic systems and workflows | Agentic Systems]]
Several open questions and evolving trends are at the forefront of [[ai_agents_and_agentic_workflows | AI agent]] development:
*   **Budget-Aware [[AI agents and agentic workflows | Agents]]** Unlike [[ai_agents_and_agentic_workflows | workflows]], there's less control over the cost and latency of [[ai_agents_and_agentic_workflows | agents]] <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Defining and enforcing budgets (time, money, tokens) is necessary for production deployment <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   **Self-Evolving Tools** Models are already used to iterate on tool descriptions, but this could generalize to a meta-tool where [[ai_agents_and_agentic_workflows | agents]] design and improve their own tool ergonomics <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This would make [[ai_agents_and_agentic_workflows | agents]] more general-purpose, as they could adapt tools as needed <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Multi-[[AI agents and agentic workflows | Agent]] Collaborations** It's anticipated that multi-[[ai_agents_and_agentic_workflows | agent]] collaborations will be seen in production soon <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. These setups offer benefits like parallelization, clear separation of concerns, and protection of main [[ai_agents_and_agentic_workflows | agent]] context windows through sub-[[ai_agents_and_agentic_workflows | agents]] <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. A key challenge is how these [[ai_agents_and_agentic_workflows | agents]] will communicate, moving beyond rigid synchronous user-assistant interactions to asynchronous communication and enabling more diverse roles <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

## Key Takeaways
To summarize the approach to [[developing_ai_agents_and_agentic_workflows | developing AI agents and agentic workflows]]:
1.  Don't build [[ai_agents_and_agentic_workflows | agents]] for everything <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
2.  If building an [[ai_agents_and_agentic_workflows | agent]], keep it as simple as possible for as long as possible <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
3.  As you iterate, think like your [[ai_agents_and_agentic_workflows | agent]] to understand its perspective and help it perform its job <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.