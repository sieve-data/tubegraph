---
title: Challenges in AI agent development
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

Developing AI agents presents various [[technical_challenges_in_ai_agent_development | technical challenges]], particularly in an era characterized by a clear shift towards bigger, smarter models and the widespread availability of intelligence <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. This evolving landscape creates both opportunities and [[challenges_in_ai_development | challenges]] <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

## Key [[challenges_in_creating_effective_AI_agents | Challenges in Creating Effective AI Agents]]

Building effective AI agents requires dedicated effort in several key areas <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>:

### Scoping Tasks for Evaluation
One of the most significant [[challenges_in_ai_agent_evaluation | challenges]] is accurately scoping tasks for evaluation <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>. While it's easy to quickly build demos, it is much harder to scope and evaluate what is actually occurring <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. Defining clear "jobs to be done" and understanding step-by-step human processes are crucial <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

It is particularly difficult to make an agent's performance measurable and verifiable at each step over time <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>. This is a common pain point where a demo might look functional but is hard to verify and improve continually <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

> "I can't stress this enough... start by thinking deeply about your eval. The number of mistakes we made by not thinking about eval first is frustrating" <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>

This "fuzzy stochastic world" of AI agents necessitates robust evaluation methods, including offline, online, and living evaluations <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. End-to-end measurements and proper instrumentation are vital to gather human feedback and continuously improve the test set <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

### Building the Right Team
Assembling a team ready to move fast and handle ambiguity is essential <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. It's not necessary to have a large number of machine learning experts, as they are scarce <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. Instead, a team can be seeded with one or two ML experts and then filled with optimistic generalists who are skilled at writing code and willing to experiment quickly <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.

Crucially, teammates should be excited about being AI-augmented themselves and possess an explorer mindset, eager to learn in a rapidly changing field <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.

### Adapting User Experience (UX)
The traditional user experience (UX) is changing dramatically with AI agents <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. UX and front-end development are more important than often realized, especially for human-AI collaboration <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>. As AI agents move from experimental to mainstream, new UX patterns are emerging, and developers must be comfortable with this shift <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>. The speaker prefers agents that behave more like human teammates rather than requiring numerous new pages or buttons <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.

### Ensuring Observability
Observability is critical and should not be an afterthought in AI agent development <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. AI agents often involve complex workflows, making situational awareness vital for debugging problems <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.

However, observability can quickly become messy with agents <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. An agent's multi-step calls can be incredibly complex, involving hundreds of decisions, tool usages, and loops <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>. Simply reviewing a list of these interactions makes it nearly impossible to understand what is happening <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>. Visualizing these complex workflows, such as through an agent graph, is essential for human-readable debugging <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>.

### Human-AI Collaboration and Trust
A significant challenge lies in figuring out the expected level of collaboration between humans and AI agents <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. While agents are designed to act like humans, there's a need for humans to verify their actions, oversee their processes, and learn from them <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. This continuous verification helps earn trust over time, allowing users to see the agent's reasoning, findings, and decision-making steps <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

### The "Bitter Lesson" of AI Development
A key insight, akin to the "bitter lesson" in application development, is that general methods leveraging off-the-shelf models are ultimately the most effective <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. Extensive fine-tuning for specific projects or tasks can quickly become outdated as new, more powerful models are released by major AI developers <a class="yt-timestamp" data-t="13:26:00">[13:26:00]</a>. Therefore, it's crucial for development teams to be adaptable and able to easily switch between different models <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.

### Designing for Agent Users
Looking ahead, a significant challenge involves designing products not just for human users but for AI agents themselves <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>. There's a strong possibility that agents will surpass humans as primary users of Software-as-a-Service (SaaS) products within the next five years <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>. This means developers must consider how agents will consume their product, providing appropriate context and API information that agents would utilize more effectively than humans <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.