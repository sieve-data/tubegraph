---
title: AI agents in DevOps
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

DataDog is an observability and security platform for cloud applications, focused on helping users observe and take action on system events [00:01:24]. DataDog has been integrating AI since around 2015, offering features like proactive alerting, root cause analysis, impact analysis, and change tracking [00:01:48].

## The Era Shift Towards AI Agents
There is a significant era shift occurring in AI, comparable to the advent of the microprocessor or the transition to SaaS [00:02:09]. This shift is characterized by bigger, smarter models, enhanced reasoning, and multimodal capabilities, leading to "intelligence becoming too cheap to meter" [00:02:17]. This means users expect more from AI daily [00:02:35]. DataDog is responding to this by moving up the stack and leveraging advancements to provide [[ai_agents_beyond_chatbots | AI agents]] that can use the platform on behalf of customers [00:02:53].

## DataDog's AI Agents
DataDog is currently developing [[ai_agents_beyond_chatbots | AI agents]] in private beta [00:03:22].

### Bits AI
Bits AI is DataDog's [[ai_agents_beyond_chatbots | AI assistant]] designed to help users with their DevOps problems [00:01:04].

### AI Software Engineer
The AI Software Engineer is a proactive developer or DevOps agent that observes and acts on errors [00:06:55]. It automatically analyzes errors, identifies causes, and proposes solutions [00:07:07]. These solutions can include generating code fixes and working to reduce on-call incidents [00:07:12]. For instance, it can catch recursion issues, propose fixes, and create new recursion tests, streamlining the engineer's workflow by reducing manual coding and testing [00:07:22].

### AI On-Call Engineer
This agent is designed to assist with 2 AM alerts, aiming to reduce the frequency of human pages [00:03:46].
When an alert occurs, the AI On-Call Engineer proactively initiates an investigation [00:04:04]:
*   It situationally orients itself by reading runbooks and gathering alert context [00:04:05].
*   It then proceeds to analyze logs, metrics, and traces in a loop to understand the situation [00:04:16].
*   The agent can automatically run investigations and provide summaries or insights before a human even reaches their computer [00:04:26].
*   It operates by forming hypotheses about what might be happening, reasoning over them, and using tools to test ideas and run queries against data [00:05:30].
*   If a root cause is identified, the agent can suggest remediations, such as paging another team or scaling infrastructure [00:05:51].
*   It can integrate with existing DataDog workflows for remediation [00:06:16].
*   After an incident is resolved, the agent can write a postmortem by reviewing what occurred and what actions both AI and humans took [00:06:26].

A new page has been added to facilitate human-AI collaboration, allowing users to verify the agent's actions, learn from its processes, and build trust [00:04:47]. Users can see the reasoning behind hypotheses and the steps taken by the agent, similar to a junior engineer's work, and ask follow-up questions [00:05:05].

## Learnings from Developing AI Agents
Building these [[ai_agents_and_agentic_workflows | AI agents]] has provided several key lessons for DataDog:

### Scoping Tasks for Evaluation
It is crucial to define "jobs to be done" clearly and understand them step-by-step from a human perspective [00:08:33]. DataDog focuses on building vertical, task-specific [[ai_agents_beyond_chatbots | agents]] rather than generalized ones [00:08:48]. A significant challenge is ensuring that each step is measurable and verifiable, as demos are easy to build but verifying long-term improvement is difficult [00:08:52]. Domain experts should be used as design partners or task verifiers, not for writing code or rules, due to the stochastic nature of models [00:09:10].

It is essential to start by thinking deeply about evaluation, including offline, online, and "living" evaluations [00:09:35]. This involves having end-to-end task measurements and appropriate instrumentation to get human feedback [00:09:57].

### Building the Right Team
A team doesn't need many ML experts; one or two can seed the team, supplemented by optimistic generalists who are proficient at writing code and willing to iterate quickly [00:10:14]. UX and frontend development are more critical for [[ai_agents_using_humanlike_interfaces_and_workflows | human-AI collaboration]] than initially perceived [00:10:28]. Team members should be excited about being AI-augmented themselves, exhibiting a day-to-day use of AI and an explorer's mindset, as the field is rapidly changing [00:10:38].

### User Experience (UX)
UX is paramount in this early stage of work, especially for [[ai_agents_using_humanlike_interfaces_and_workflows | collaboration]] [00:11:18]. Old UX patterns are changing, and it's important to be comfortable with this [00:11:24]. DataDog prefers agents that behave more like human teammates rather than requiring new pages or buttons [00:11:28].

### Observability
Observability is critical and should not be an afterthought when developing [[ai_agents_and_agentic_workflows | complex AI agent workflows]] [00:11:38]. Situational awareness is necessary to debug problems [00:11:44]. DataDog utilizes its full observability stack, including GPU and LLM monitoring, to tie together diverse interactions and calls to models for debugging [00:11:51].

Agent workflows can become very complex, involving hundreds of multi-step calls, loops, and tool decisions [00:12:26]. To address this, DataDog developed an "agent graph" view within its observability tools, which provides a human-readable representation of the agent's workflow, highlighting errors [00:12:46].

### The "Agent Bitter Lesson"
A general principle observed is that methods leveraging new, off-the-shelf models are ultimately the most effective [00:13:16]. While fine-tuning for specific tasks requires significant effort, new foundation models often quickly solve much of the reasoning, making it crucial to be able to easily switch between models [00:13:26].

## Future of AI Agents
The future will be "weird" and "fun," with AI acceleration happening daily [00:14:50]. DataDog anticipates offering a team of DevSecOps [[ai_agents_beyond_chatbots | agents]] for hire, which will handle operations and security without users needing to directly integrate with the DataDog platform [00:14:56].

There's a high probability that [[ai_agents_beyond_chatbots | agents]] will surpass humans as users of SaaS products like DataDog within the next five years [00:14:07]. Therefore, companies should not only build for humans or their own agents but also consider how third-party [[ai_agents_beyond_chatbots | agents]] (like Claude) might use their products [00:14:21]. This means providing context and API information optimized for [[ai_agents_beyond_chatbots | agents]] [00:14:38].

Small companies will increasingly be built by individuals using "auto-developers" (like Cursor or Devin) to bring ideas to life, and then using [[ai_agents_beyond_chatbots | agents]] like DataDog's to manage operations and security, enabling an order of magnitude more ideas to reach the real world [00:15:25].