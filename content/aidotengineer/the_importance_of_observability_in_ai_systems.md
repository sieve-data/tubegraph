---
title: The importance of observability in AI systems
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

Observability is crucial for understanding and managing complex systems, and its significance is amplified in the context of artificial intelligence (AI) systems and agents <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. DataDog, as an [[AI security and observability | observability]] and security platform for cloud applications, focuses on making it easier to observe what's happening in a system and take action <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Why Observability Matters in the AI Era

In the current era of AI advancement, where intelligence is becoming "too cheap to meter" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, the need for robust observability is paramount <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. As AI agents become more sophisticated and take on critical tasks, understanding their internal workings and potential issues becomes vital.

Key reasons for the importance of observability include:
*   **Debugging Complex Workflows** Modern AI agents, like those developed by DataDog, involve complex, multi-step calls that can number in the hundreds and include continuous looping and tool decisions <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Without proper observability, it's impossible to understand what's occurring <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Situational Awareness** Observability provides the necessary situational awareness to debug problems effectively and saves time <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
*   **Preventing Afterthoughts** Observability should be an integral part of AI system development, not an afterthought, given the inherent complexity of AI workflows <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

## Observability in Practice at DataDog

DataDog has been incorporating AI since around 2015 for features like proactive alerting, root cause analysis, impact analysis, and change tracking <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. With the current "era shift" in AI, they are developing "AI agents" that leverage their platform <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This requires building out new types of [[AI security and observability | observability]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### LM Observability

DataDog has introduced a new view called "LM observability" within its product, which has proven very helpful <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. This feature ties into DataDog's existing full [[AI security and observability | observability]] stack, which can monitor GPUs, LLMs, and entire systems end-to-end <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. It's particularly beneficial for AI systems because it can group a wide variety of interactions and calls to different models (hosted, running, or via API) into a single "pane of glass" for easier debugging <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Agent Graph for Workflow Visualization

To address the complexity of observing AI agents, DataDog has developed an "agent graph" view within its [[AI security and observability | observability]] tools <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. This graph allows users to visualize and understand the complex workflows of an agent, much like the agent itself perceives them <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. For example, if an error occurs within a complex workflow, it can be highlighted as a bright red node on the graph, making it human-readable and significantly easier to identify and debug issues <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

## Broader Implications

The speaker emphasizes that beyond building internal agents, companies should anticipate a future where AI agents become significant users of SaaS products like DataDog <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. This means thinking about providing context and API information optimized for agent consumption <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. Strong [[AI security and observability | observability]] will be critical not just for monitoring human-driven systems but also for overseeing these autonomous agent interactions.

## Lessons Learned in Building AI Agents

DataDog's experience in building AI agents has yielded several insights, including:
*   **Scoping Tasks for [[evaluating_ai_systems_at_scale | Evaluation]]** It's easy to build quick demos, but much harder to clearly define "jobs to be done" and scope work for [[evaluating_ai_systems_at_scale | evaluation]] <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Tasks should be measurable and verifiable at each step, a significant pain point for many working with agents <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **[[importance_of_evaluations_in_ai_projects | Importance of Evaluations]]** Deeply considering [[importance_of_evaluations_in_ai_projects | evaluation]] from the start is crucial, as everything in the "fuzzy stochastic world" of AI requires good [[importance_of_evaluations_in_ai_projects | evaluation]]—from small initial tests to living, breathing test sets <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Building the Right Team** Teams should be seeded with a few ML experts but primarily consist of optimistic generalists who can move fast and embrace ambiguity <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Evolving UX** Traditional user experience (UX) patterns are changing, and developers should be comfortable with agents acting more like human teammates <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.