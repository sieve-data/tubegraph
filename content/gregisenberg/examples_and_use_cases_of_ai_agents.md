---
title: Examples and use cases of AI agents
videoId: RHXb92PAIa0
---

From: [[gregisenberg]] <br/> 

AI agents are described as being vastly superior to human employees, offering significant benefits such as increased efficiency, faster growth, infinite scalability, and continuous improvement for businesses <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. They leverage Large Language Models (LLMs) not just for generating text, but to perform actual work <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A key differentiator from traditional automations like Zapier is their inherent intelligence and ability to maintain context over long-term tasks <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This allows for AI prompts at any point in a workflow and enables the agent to remember past interactions <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Core Applications and Examples

### Meeting Recorder and Coach
A "Meeting Recorder Lindy" can be set up to:
*   Join and record meetings when a calendar event begins <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   Create Google Docs with meeting notes <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Send notes via Slack <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   Provide coaching notes based on specific prompts (e.g., analyzing if the speaker was too confrontational or not confrontational enough) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   Disseminate notes to relevant Slack channels <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   Manage follow-up conversations via email, understanding the entire context of the meeting and prior feedback <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. For instance, if feedback was "too technical," the agent can understand follow-up questions asking for clarification based on the original meeting context <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Reservation Confirmation Processing
An AI agent can automate the processing of reservation confirmation emails, such as those from a rental platform:
*   Upon receiving a confirmation email, the agent extracts specific data like the reservation date and total amount using natural language prompts <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   This extracted data is then appended to a Google Sheet <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   Unlike traditional automations, it does not require complex data injection or HTML parsing, making it resilient to format changes <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Sales Call Summary and Coaching
AI agents can also enhance sales operations:
*   A Lindy agent can join sales calls <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   After the call, it posts a summary to a designated Slack channel <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   Team members can then ask follow-up questions within the Slack thread, and the agent provides contextual answers <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   This enables in-context coaching of teammates directly within Slack <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

### Time-Sensitive Email Management
An agent can triage and manage urgent emails:
*   It acts as a trigger when an email is received <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   Using natural language processing, it determines if the email is "urgent and time sensitive" <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   If so, it sends a direct message to the user on Slack, providing context from the email <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   The user can then chat back with the agent in Slack, instructing it to reply to the email or create a calendar event based on the conversation <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. The agent understands and executes complex instructions like "tell him I'll call him right away and create a 15-minute calendar invite for 3 p.m." <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

### Meeting Scheduler
An AI agent can act as a meeting scheduler:
*   It looks at the user's calendar to find available times <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.
*   It replies to email threads suggesting multiple availabilities <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.
*   If the recipient changes their mind or requests a different time, the agent can delete existing calendar events, find new times, and send new invites, managing the entire negotiation process <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.

### Designer Recruiter / Lead Generator
This complex use case demonstrates the ability of agents to perform advanced research and outreach:
*   The agent receives various forms of information about designers (Twitter links, portfolios, names) <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>.
*   It identifies the type of input (website, email, LinkedIn) <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.
*   It searches for email addresses by browsing websites, portfolios, and performing Google searches (e.g., combining "designer portfolio" with a name) <a class="yt-timestamp" data-t="00:30:22">[00:30:22]</a>.
*   It can identify email addresses even if they are spelled out or creatively hidden to avoid bots <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.
*   Once an email is found, it checks if prior contact was made <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>.
*   If not, it drafts and sends an initial outreach email, and can be programmed to send multiple reminders <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>.
*   This system can be used to build an autonomous recruiting company <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.
*   A "lead generator Lindy" can be asked to find specific profiles (e.g., "five product designers who work at [[ai_agent_platforms | Zapier]]") and add them to a Google Sheet <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.

### Customer Support Agent
AI agents are adept at handling high volumes of customer inquiries:
*   An e-commerce customer uses Lindy as their customer support agent <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a>.
*   During peak demand, like Black Friday, the system automatically scales to handle thousands of tickets simultaneously <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>.
*   It ensures that key performance indicators, such as average ticket handling time, remain stable even with massive influxes of inquiries <a class="yt-timestamp" data-t="00:42:13">[00:42:13]</a>.
*   The user pays only for the compute used, unlike human support where idle time is still paid <a class="yt-timestamp" data-t="00:42:29">[00:42:29]</a>.

## Advanced Concepts: Agent Collaboration and Autonomous Companies
A significant advanced capability is the ability for multiple AI agents to communicate and work together, akin to "object-oriented programming for agents" <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

### Delegating Tasks Between Agents
*   A primary agent (e.g., the time-sensitive email catcher) can delegate a task, like writing a proposal, to another specialized agent (e.g., a "proposal writer Lindy") <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
*   The "proposal writer Lindy" can then create a Google Doc with a proposal based on instructions, communicate its completion, and provide a link back to the summoning agent <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
*   This delegation allows for complex workflows where agents collaborate on different parts of a larger task <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
*   The primary agent can then send the completed proposal to the client <a class="yt-timestamp" data-t="00:40:11">[00:40:11]</a>.
*   This parallel processing capability allows for many proposals to be generated concurrently <a class="yt-timestamp" data-t="00:41:05">[00:41:05]</a>.

### Building an Autonomous Company
The concept extends to building entire "autonomous companies" where an individual or a small team manages an "army of AI recruiters" or other specialized AI agents that scale infinitely with compute power <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This represents a significant [[using_ai_models_for_practical_applications_and_startups | arbitrage opportunity]] because not everyone is currently leveraging this capability <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>.

## Getting Started with AI Agents
For those new to [[building_ai_agents_for_business_automation | building AI agents]], it's recommended to start with single-agent workflows before graduating to inter-agent communication <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>. Identifying repetitive tasks or "jobs to be done" within a business is a good starting point for designing agents <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. Platforms like Lindy offer an academy and templates to help users get started <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>.