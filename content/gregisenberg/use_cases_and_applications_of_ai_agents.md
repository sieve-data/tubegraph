---
title: Use cases and applications of AI agents
videoId: RHXb92PAIa0
---

From: [[gregisenberg]] <br/> 
[[practical_use_cases_for_ai_agents_in_business | Use Cases and Applications of AI Agents]]

AI agents are described as a platform for creating AI employees, enabling users to build startups with thousands of agents running simultaneously <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The core premise is that these agents can be "a thousand times better than a human" in certain tasks <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, making businesses more efficient and fostering faster growth <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Advantages of AI Agents
AI agents offer several significant advantages:
*   **Efficiency and Growth:** They make businesses more efficient and enable faster growth <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Ease of Deployment:** They are easy to spin up <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **No Management Overhead:** Unlike human employees, they don't require management <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Infinite Scalability:** They scale infinitely and elastically, meaning they can scale up with demand and down when not in use <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Continuous Improvement:** Agents continuously improve their performance <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **LLM Capabilities:** Large Language Models (LLMs) like GPT-4 and Claude can perform work beyond just generating text or copy <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Distinguishing AI Agents from Automations
A key distinction is made between traditional automations (like Zapier) and AI agents:
*   **Intelligence:** AI agents possess intelligence, unlike simple automations <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **AI Throughout:** AI can be used at any point in an agent's workflow, allowing for natural language instructions and dynamic data extraction <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Contextual Awareness:** An agent is aware of the entire context of its actions, understanding everything it has done previously <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. In contrast, each step in traditional automation is isolated <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This allows for more robust and less brittle workflows <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **Long-Term Task Management:** While automations are "once and done," an AI agent manages long-term tasks and time horizons, enabling ongoing conversations and dynamic responses <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## [[ai_agents_and_their_applications | Applications and Use Cases]]
The platform Lindy is showcased to demonstrate various [[ai_agents_and_their_applications | practical use cases for AI agents in business]]:

### Meeting Recorder and Coach
An AI agent can join and record meetings automatically when a calendar event begins <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   It creates Google Docs with meeting notes <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Sends notes and coaching feedback (e.g., "was I too confrontational?") via Slack <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   Can disseminate notes to relevant Slack channels <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   It maintains context, allowing users to reply to coaching emails with follow-up questions, which the agent understands within the full meeting context <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Financial Data Extraction
An agent can process incoming emails, such as reservation confirmations from platforms like Airbnb, and extract specific data points like the date and total amount of a reservation <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This extracted information can then be appended to a Google Sheet <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The agent understands natural language prompts for extraction, even if the email format changes <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Sales Call Summarization and Coaching
An AI agent can join sales calls, post a summary of the call in a designated Slack channel, and then allow users to ask follow-up questions within the thread, receiving immediate, context-aware replies <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This facilitates real-time coaching for teammates based on call interactions <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

### Time-Sensitive Email Notifier and Responder
An agent can monitor incoming emails and, using an LLM, determine if an email is "urgent and time sensitive" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. If it is, the agent can send a direct message on Slack with context about the email <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. Furthermore, it can be equipped with "skills" like replying to emails and creating calendar events, allowing users to instruct the agent to perform actions via natural language commands in Slack <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. The agent understands complex instructions like "tell him I'll call him right away and create a 15-minute calendar invite for 3 p.m." <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

### Proposal Generation
AI agents can communicate and delegate tasks to each other, a concept similar to object-oriented programming for agents <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. One agent can summon another, specialized "proposal writer Lindy" to create Google Docs with proposals based on given instructions <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. The proposal writer can name the document, write content with multiple sections (e.g., pricing, terms) <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>, and then report back to the summoning agent with the link to the created proposal <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. This streamlines the proposal process, especially for service businesses <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.

### Meeting Scheduler
An AI agent can act as a meeting scheduler, understanding email conversations to look at a user's calendar, find available times, suggest them, and then send a calendar invite once a time is agreed upon <a class="yt-timestamp" data-t="00:28:17">[00:28:17]</a>. The agent can handle complex scenarios like rescheduling, deleting previous events, and finding new times for future weeks <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.

### Designer/Recruiter (Lead Generation and Outreach)
An agent can be configured to find designers based on various inputs like Twitter links, websites, or just a name <a class="yt-timestamp" data-t="00:29:58">[00:29:58]</a>.
*   It performs "site quests" to find email addresses by browsing portfolios and performing Google searches <a class="yt-timestamp" data-t="00:30:24">[00:30:24]</a>.
*   The agent is given a "high-level goal" and browses for a bit, looking for portfolios and giving up after a set number of attempts to avoid getting stuck in loops <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>.
*   It can extract emails even if they are obfuscated (e.g., "my name at gmail") <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.
*   Once an email is found, it can check if the user has reached out before and, if not, send an initial email and programmed reminders <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>.
*   This can be scaled to build a business, like a recruiting company, by having an army of AI recruiters <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>.
*   A "lead generator Lindy" can find specific professionals (e.g., product designers at Zapier), add their information to Google Sheets, and then delegate to the "designer recruiter" Lindy to perform outreach, even finding personal emails <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.

### Customer Support Agent
For e-commerce businesses, an AI agent can serve as a customer support agent <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a>. During peak times like Black Friday, where customer support tickets can surge, an AI agent can handle an influx of thousands of tickets simultaneously, scaling infinitely to meet demand without requiring additional human staff <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>. This ensures consistent service levels and efficiency even during high-volume periods <a class="yt-timestamp" data-t="00:42:13">[00:42:13]</a>.

## The Autonomous Company
The vision presented is to [[building_apps_using_ai_tools | build an autonomous company]] using AI agents <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>. By having various Lindies work together, a user can effectively create an entire team of AI employees that handles diverse tasks <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This allows for businesses to scale infinitely with compute rather than human capital <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.

## Getting Started
For those new to [[designing_and_optimizing_ai_tasks_and_agents | designing and optimizing AI tasks and agents]], it's recommended to start with simpler, individual AI agents before moving to more advanced scenarios involving agents communicating with each other <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. A useful approach is to first identify "jobs to be done" – repeatable tasks within a business – and then create agents to automate those tasks <a class="yt-timestamp" data-t="00:42:48">[00:42:48]</a>.