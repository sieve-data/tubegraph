---
title: Development and deployment of observability platforms
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

Datadog serves as an [[cloud_observability_with_opentelemetry | observability]] and security platform tailored for cloud applications <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Its core function is to enable users to observe system behavior and take appropriate actions, simplifying understanding and enhancing system safety and DevOps friendliness <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Historical Context of AI in Observability at Datadog

Datadog has been integrating AI into its offerings since around 2015 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. While not always overtly presented as "AI products," these integrations include features like proactive alerting <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, root cause analysis <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, impact analysis <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, and change tracking <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

The current era marks a significant shift, comparable to the advent of the microprocessor or the transition to SaaS, with larger, smarter models, enhanced reasoning capabilities, and multimodal AI <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This shift leads to "intelligence becoming too cheap to meter," causing products like Cursor to grow rapidly and increasing user expectations for AI <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Datadog is adapting to this by moving up the stack, aiming for AI agents to utilize the platform on behalf of users, rather than users interacting with the platform directly <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## AI Agents and Observability

The development of [[ai_agents_in_devops | AI agents in DevOps]] at Datadog requires focus on several key areas:
*   Developing the agents themselves <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   Conducting evaluations, which are crucial for agent performance <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Building out new types of [[cloud_observability_with_opentelemetry | observability]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

Datadog is developing several [[ai_agents_in_devops | AI agents]], including:
*   **AI Software Engineer**: This agent identifies errors, recommends code, and can generate code fixes to improve systems and reduce on-call incidents <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **AI On-Call Engineer**: Designed to proactively respond to alerts, this agent can situationally orient itself by reading runbooks and gathering context <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. It then investigates issues by analyzing logs, metrics, and traces, similar to a human engineer <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. It can also generate post-mortems after an incident is remediated <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

These agents function by forming hypotheses, testing them with tools, running queries against [[cloud_observability_with_opentelemetry | observability]] data (logs, metrics, traces), and validating or invalidating these hypotheses <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## The Critical Role of Observability

Observability is paramount in developing and deploying complex [[ai_agents_in_devops | AI agents]], as it provides the necessary situational awareness for debugging problems <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. It should not be an afterthought <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

### LLM Observability

Datadog has introduced "LLM observability" as a new view within its product <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. This feature is particularly useful because [[ai_agents_in_devops | AI agents]] involve a wide array of interactions and calls to various models—whether self-hosted, run locally, or accessed via API <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. LLM observability consolidates all these interactions into a single view for debugging <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

However, workflows involving [[ai_agents_in_devops | AI agents]] can become very complex, with multi-step calls and hundreds of decisions about tools and loops <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. To address this complexity, Datadog provides an "agent graph" <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. This human-readable visual representation of the agent's workflow makes it easier to identify issues, such as errors highlighted with a bright red node <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

## Lessons Learned in Developing AI Agents

Developing [[ai_agents_in_devops | AI agents]] has provided several key learnings, especially regarding [[implementation_of_evaluation_platforms_for_ai_agents | evaluation platforms for AI agents]] and the importance of observability:

*   **Scoping Tasks for Evaluation**: It's crucial to define "jobs to be done" clearly and in a step-by-step manner, approaching it from a human perspective first <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. Building vertical, task-specific agents is preferred over generalized ones <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. The work should be measurable and verifiable at each step, which is a significant challenge for agents <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Evaluation is Paramount**: Deeply considering evaluation from the outset is essential <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. While demos are easy to build, verifying and improving performance over time in a "fuzzy, stochastic world" requires robust offline, online, and "living" evaluations, including end-to-end measurements <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Team Building**: A small number of ML experts, supplemented by optimistic generalists who can code quickly and are willing to experiment, form an effective team <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Evolving UX**: The user experience paradigms are changing, and being comfortable with these shifts is important <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. Agents that behave more like human teammates are preferred over creating many new pages or buttons <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Observability is Not an Afterthought**: Observability is critical for managing complex agent workflows and debugging problems effectively <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

A "bitter lesson" in [[agent_frameworks_and_orchestration_layers_in_ai_engineering | AI engineering]] is that general methods leveraging new, off-the-shelf models are ultimately the most effective <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. Teams should be able to easily try out new models and avoid being stuck to a particular one they've been working on <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

## The Future: Agents as Users of Observability Platforms

A significant future trend is the expectation that [[ai_agents_in_devops | AI agents]] will surpass humans as users of SaaS products like Datadog within the next five years <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This means platforms must consider building not just for human users or internal agents, but also for third-party agents (e.g., Claude) that might directly interact with their APIs <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. This involves providing context and API information optimized for agent consumption <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

Datadog anticipates offering "DevSecOps agents for hire," where agents will handle platform integration, on-call duties, and more directly <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. Conversely, SRE, coding, and other types of [[ai_agents_in_devops | AI agents]] built by users should also leverage Datadog's platform and tools just like humans would <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This future envisions small companies being built by automated developers and operations/security agents, enabling an order of magnitude more ideas to reach the market <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.