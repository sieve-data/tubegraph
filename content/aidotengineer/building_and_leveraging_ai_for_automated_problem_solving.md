---
title: Building and leveraging AI for automated problem solving
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

Diamond, from DataDog, shared insights into the development and application of AI agents designed to automate problem-solving in DevOps environments. DataDog's initiative, "Bits AI," aims to create an AI assistant that helps users manage their DevOps challenges <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## DataDog's Evolution with AI
DataDog, an observability and security platform for cloud applications, has been incorporating AI since around 2015 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. While not always overtly presented as "AI products," these capabilities include proactive alerting, root cause analysis, impact analysis, and change tracking <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

The current landscape represents a clear era shift, comparable to the advent of microprocessors or the transition to SaaS, with the emergence of larger, smarter, reasoning, and multimodal models <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This shift signifies a future where intelligence becomes "too cheap to meter" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. DataDog is actively working to [[enhancing_existing_systems_with_ai_capabilities | leverage these advancements]] by moving up the stack and enabling AI agents to use their platform directly for customers <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Key AI Agents at DataDog
DataDog is currently developing several AI agents in private beta, with a focus on [[ai_in_workflow_automation | automating workflows]] and problem-solving <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### AI On-Call Engineer
This agent is designed to help engineers avoid being paged in the middle of the night <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. When an alert occurs, the AI On-Call Engineer proactively initiates an investigation <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. It performs several key actions:
*   **Situational Orientation**: Reads run books and gathers alert context <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Data Analysis**: Examines logs, metrics, and traces <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Hypothesis Testing**: Formulates hypotheses about the issue, tests them using tools, and validates or invalidates each <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Remediation Suggestion**: If a root cause is found, it can suggest remediations, such as paging another team or scaling infrastructure <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Workflow Integration**: Can tie into existing DataDog workflows for remediation <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Postmortem Generation**: After an incident is resolved, the agent can write a postmortem documenting what occurred and the actions taken by both humans and the agent <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

This agent also facilitates human-AI collaboration, allowing users to verify its actions and understand its reasoning, which helps [[building_trust_in_ai_systems | build trust]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a> <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### AI Software Engineer
This agent acts as a proactive developer, observing and acting on errors <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. It automatically analyzes errors, identifies causes, and proposes solutions, including generating code fixes and creating tests to prevent recurrence <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This significantly reduces the time engineers spend manually writing and testing code <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## Lessons Learned in [[building_effective_ai_agents | Building Effective AI Agents]]
Developing these agents has provided DataDog with several key learnings <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Scoping Tasks for Evaluation
It is easy to build quick demos, but much harder to properly scope and evaluate what is occurring <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Define "Jobs to Be Done"**: Clearly understand tasks step-by-step from a human perspective <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Vertical, Task-Specific Agents**: Build agents for specific tasks rather than generalized agents <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Measurable and Verifiable**: Ensure tasks are measurable and verifiable at each step, as this is a significant challenge <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Domain Experts as Design Partners**: Utilize domain experts for evaluation and verification, rather than for writing code or rules <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Deeply Consider Evaluation**: Start by thinking deeply about evaluation, including offline, online, and living evaluations with end-to-end measurements <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### [[building_and_recruiting_ai_teams | Building the Right Team]]
A successful team doesn't require a large number of ML experts, which are scarce <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Instead, it should be seeded with one or two ML experts and augmented with optimistic generalists who are skilled at coding and willing to iterate quickly <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. UX and front-end expertise are also critically important for effective collaboration with agents <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Team members should be excited to be AI-augmented themselves, as the field is rapidly changing <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

### Adapting User Experience (UX)
The traditional UX patterns are changing, and developers must be comfortable with this evolution <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. In this early space, UX is crucial for collaboration <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. DataDog favors agents that function more like human teammates rather than requiring new pages or buttons <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

### The Importance of Observability
Observability is critical and should not be an afterthought, especially with complex AI agent workflows <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. Situational awareness is necessary to debug problems <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. DataDog has introduced "LLM Observability" within its product to provide a single pane of glass for monitoring various model interactions, whether hosted, run, or used via API <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

Agent workflows can become very complex, involving hundreds of multi-step calls and tool-use decisions <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. To address this, DataDog provides an "agent graph" view, which makes complex workflows human-readable, highlighting errors within the process <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### The "Bitter Lesson" of Application Layer
General methods that can [[building_and_scaling_ai_use_cases_with_openai | leverage new, off-the-shelf models]] are ultimately the most effective <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. While fine-tuning for specific tasks might seem beneficial, new foundational models often solve much of the reasoning quickly <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. It's crucial to be able to easily try out any new models and not be tied to a particular one <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. This aligns with the "rising tide lifts all boats" concept <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

## Future Outlook for AI in Problem Solving
Diamond anticipates that AI agents will surpass humans as users of SaaS products within the next five years <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This means companies should consider building for agents as users, providing context and API information that agents would utilize more than humans <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

DataDog plans to offer a team of DevSecOps agents for hire, capable of handling on-call duties and platform integrations directly for customers <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. They also envision AI agents themselves becoming customers, using platforms like DataDog just as humans would <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

The future of small companies may involve leveraging automated developers like Cursor or Devin to bring ideas to life, with agents like DataDog's handling operations and security, enabling a significantly greater number of ideas to reach the real world <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

DataDog is actively hiring AI engineers and individuals passionate about this evolving space <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.