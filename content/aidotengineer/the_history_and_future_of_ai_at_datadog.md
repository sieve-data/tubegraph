---
title: The history and future of AI at Datadog
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

Datadog's approach to artificial intelligence integrates decades of experience in the field, moving from embedded AI features to advanced, autonomous AI agents for operations and development <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The company aims to provide an "AI assistant" to help with devops problems <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Speaker Background
The presenter, Diamond, has spent approximately 15 years in [[evolution_and_history_of_ai_technology | AI]] attempting to create more [[the_impact_and_future_potential_of_ai_and_agents | AI friends and co-workers]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This career spans roles at Microsoft Cortana <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, Amazon Alexa <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, Meta (working on PyTorch) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, and his own [[the_impact_and_future_potential_of_ai_and_agents | AI]] startup focused on a devops assistant <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Datadog Overview
Datadog is an observability and security platform designed for cloud applications <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Its core function is to allow users to observe system behavior and take action, making it easier to understand and build safer, more devops-friendly systems <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## History of AI at Datadog
Datadog has been incorporating [[evolution_and_history_of_ai_technology | AI]] into its products since around 2015 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. While not always overtly branded as "AI product," features like proactive alerting, root cause analysis, impact analysis, and change tracking have utilized [[role_of_ai_in_research_and_data_analytics | AI]] capabilities <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

The current landscape represents a "clear era shift," akin to the advent of the microprocessor or the shift to SaaS <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This shift is characterized by:
*   Bigger, smarter models <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>
*   Reasoning capabilities <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>
*   Multimodal [[evolution_of_ai_models_and_their_application | AI]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
*   "Foundation model Wars" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   Intelligence becoming "too cheap to meter" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

This has led to a rise in user expectations for [[the_impact_and_future_potential_of_ai_and_agents | AI]] <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Datadog is responding by moving "up the stack" to leverage these advancements and provide [[the_impact_and_future_potential_of_ai_and_agents | AI agents]] that use the platform on behalf of customers <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Bits AI: Datadog's AI Agents
Datadog is developing "Bits AI" as an [[the_impact_and_future_potential_of_ai_and_agents | AI assistant]] for devops problems <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This requires work in agent development, evaluation (eval), and new types of observability <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Currently, two agents are in private beta <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:

### AI On-Call Engineer
This agent is designed to save engineers from 2 AM alerts <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Proactive Operation**: Kicks off automatically when an alert occurs <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Situational Awareness**: Reads runbooks, gathers alert context, and analyzes logs, metrics, and traces <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Investigation and Summarization**: Automatically runs investigations, finds summaries, and pulls information before a human even gets to their computer <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Hypothesis and Tooling**: Formulates hypotheses, reasons over them, and uses tools to test ideas by running queries against data <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Remediation and Post-Mortems**: If a root cause is found, it can suggest remediations (e.g., paging another team, scaling infrastructure) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. It can also write post-mortems after an issue is remediated, summarizing what occurred and the actions taken by both humans and the agent <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Human-AI Collaboration**: A new page facilitates collaboration, allowing humans to verify what the agent did, learn from its actions, and ask follow-up questions <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### AI Software Engineer
This agent acts as a proactive developer or devops/software engineering agent <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Error Tracking Assistant**: Observes and acts on incoming errors <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Analysis and Solutions**: Automatically analyzes errors, identifies causes, and proposes solutions <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Code Generation**: Solutions can include generating code fixes and creating tests (e.g., a recursion test for a recursion issue) <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Integration**: Offers options to create a Pull Request in GitHub or open a diff in VS Code for editing <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This significantly reduces the time engineers spend manually writing and testing code <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Incident Reduction**: Aims to reduce the number of on-call incidents in the first place by proactively addressing issues <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

## Learnings from Building AI Agents
Datadog has identified several key learnings in the process of building these [[the_impact_and_future_potential_of_ai_and_agents | AI agents]] <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>:

### Scoping Tasks for Evaluation
It's easier to build demos than to properly scope and evaluate what's occurring <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Define "Jobs to Be Done"**: Clearly understand step-by-step what needs to be accomplished, thinking from a human perspective first <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Vertical, Task-Specific Agents**: Build specific agents rather than generalized ones <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Measurable and Verifiable**: Tasks should be measurable and verifiable at each step, which is a significant challenge for [[challenges_and_solutions_in_ai_driven_data_processing | AI agents]] <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Domain Experts as Verifiers**: Use domain experts as design partners or task verifiers, not for writing rules or code, as stochastic models work differently than human experts <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Prioritize Eval**: Deeply consider evaluation from the start, using offline, online, and "living" evaluations with end-to-end measurements and proper instrumentation <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Building the Right Team
The right team is crucial for moving fast and dealing with ambiguity <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **ML Experts and Optimistic Generalists**: Teams should be seeded with one or two ML experts, complemented by optimistic generalists who are good at writing code and willing to quickly try things <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **UX Importance**: User experience (UX) and front-end development are more important than often perceived, especially for collaboration with agents <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **AI-Augmented Teammates**: Team members should be excited to be [[the_impact_and_future_potential_of_ai_and_agents | AI]] augmented themselves, possessing an explorer mindset willing to learn in a rapidly changing field <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

### Evolving User Experience (UX)
The UX of [[the_impact_and_future_potential_of_ai_and_agents | AI agents]] is still an early space, and old UX patterns are changing <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. Datadog favors agents that act more like human teammates rather than requiring a multitude of new pages or buttons <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

### Observability Matters
Even with [[the_impact_and_future_potential_of_ai_and_agents | AI agents]], observability is critical and should not be an afterthought <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   **Complex Workflows**: [[the_impact_and_future_potential_of_ai_and_agents | AI agent]] workflows are complex, often involving hundreds of multi-step calls, decisions about tools, and looping <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **Situational Awareness**: Debugging requires situational awareness, which is provided by tools like Datadog's "LM observability" view <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. This ties together interactions and calls to various [[evolution_of_ai_models_and_their_application | AI models]] (hosted, running, or via API) into a single view <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Agent Graph**: Datadog developed an "agent graph" to visualize and debug agent workflows in a human-readable format, making it easier to identify errors <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### The "Agent or Application Layer Bitter Lesson"
General methods that can leverage new, off-the-shelf [[evolution_of_ai_models_and_their_application | AI models]] are ultimately the most effective <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. It's important to be able to easily try out different models and not get stuck on a particular one, as the field is rapidly advancing with new models solving complex reasoning tasks quickly <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

## Future of AI at Datadog and Beyond
Datadog anticipates a future where [[the_impact_and_future_potential_of_ai_and_agents | AI agents]] are pervasive and become key users themselves.

### AI Agents as Users
It is estimated that [[the_impact_and_future_potential_of_ai_and_agents | AI agents]] could surpass humans as users of platforms like Datadog and other SaaS products within the next five years <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This means companies should consider designing their products not just for humans or their own agents, but also for third-party agents (e.g., Claude) that might use their platform directly <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>, providing context and API information tailored for [[the_impact_and_future_potential_of_ai_and_agents | agent]] consumption <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

### DevSecOps Agents For Hire
Datadog expects to soon offer a "team of DevSecOps agents for hire," where their agents will directly handle on-call responsibilities and integrations for customers <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### Empowering Small Companies
The speaker believes that in the future, small companies will be built by individuals who can use automated developers (like Cursor or Devin) to bring ideas to life <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>, and then rely on agents like Datadog's to manage operations and security. This will enable an order of magnitude more ideas to reach the real world <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

Datadog is actively hiring [[the_evolution and_current_state_of_ai_engineering | AI engineers]] and enthusiasts to work in this evolving space <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.