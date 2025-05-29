---
title: Lindy platform for building AI agents
videoId: _qr7ogLpTJs
---

From: [[gregisenberg]] <br/> 

Lindy.AI is an [[building_ai_agent_platforms_with_crewai | AI agent platform]] that enables users to build their own [[ai_agents_and_their_applications | AI agents]] without needing to code <a class="yt-timestamp" data-t="01:38:29">[01:38:29]</a>. Flo, the CEO of Lindy.AI, describes it as "the Zapier of AI" <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>. The platform allows users to automate a significant portion of their business operations quickly, with the potential to automate half a business in half a day and create a first agent in just 10 minutes <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>.

## Core Concepts and Features

### AI Agents vs. Workflows
Unlike traditional workflow automation platforms like Zapier, where steps are isolated, Lindy's agents maintain coherence across a sequence of steps <a class="yt-timestamp" data-t="04:09:47">[04:09:47]</a>. This means an [[ai_agents_and_their_applications | AI agent]] can learn and adapt throughout a process, even recovering from mistakes <a class="yt-timestamp" data-t="04:29:41">[04:29:41]</a>. Users can interact with each step using natural language prompts, allowing the agent to understand and format content without needing separate AI-specific steps <a class="yt-timestamp" data-t="03:42:04">[03:42:04]</a>.

### Agent Swarms
A significant feature of Lindy is the ability to deploy [[building_ai_agent_platforms_with_crewAI | agent swarms]] <a class="yt-timestamp" data-t="10:20:25">[10:20:25]</a>. An [[building_ai_agent_platforms_with_crewAI | agent swarm]] allows a list of tasks to be sent to an [[ai_agents_and_their_applications | AI agent]], which then duplicates itself (like "Agent Smith" from The Matrix) to handle each task reliably, quickly, and in parallel <a class="yt-timestamp" data-t="11:13:30">[11:13:30]</a>. This overcomes the limitation of single [[ai_agents_and_their_applications | AI agents]] that can lose coherence over long-term tasks <a class="yt-timestamp" data-t="10:42:57">[10:42:57]</a>. This capability makes tasks like personalized outreach to hundreds of leads efficient and cost-effective <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.

### Integrations and Control
Lindy boasts thousands of integrations and scrapers, positioning it as a top [[ai_agents_and_their_applications | AI agent platform]] in terms of integration numbers <a class="yt-timestamp" data-t="04:55:04">[04:55:04]</a>. This includes the ability to scrape YouTube comments <a class="yt-timestamp" data-t="02:01:21">[02:01:21]</a>. Users can choose the underlying LLM (e.g., Claude 3.5, Gemini, O1) for their agents, with Claude 3.5 recommended as a default, and more expensive models like O1 for research tasks <a class="yt-timestamp" data-t="21:42:52">[21:42:52]</a>.

### Human-in-the-Loop and Learning
Lindy allows users to insert a human in the loop for confirmation at any step <a class="yt-timestamp" data-t="17:49:03">[17:49:03]</a>. This is particularly useful for tasks where an [[ai_agents_and_their_applications | AI agent]] could potentially cause embarrassment <a class="yt-timestamp" data-t="18:02:40">[18:02:40]</a>. A feature in development will enable agents to learn from user feedback and corrections <a class="yt-timestamp" data-t="18:27:03">[18:27:03]</a>.

## Key Use Cases

### Meeting Management
*   **Meeting Recording and Note-taking**: Lindy can record meetings triggered by calendar events and summarize them <a class="yt-timestamp" data-t="02:15:37">[02:15:37]</a>. It can also add notes to existing Google Docs, recalling past interactions with specific contacts <a class="yt-timestamp" data-t="02:54:19">[02:54:19]</a>. Users can ask the agent specific questions about past meetings, effectively serving as an "exocortex" or external brain <a class="yt-timestamp" data-t="07:22:25">[07:22:25]</a>.
*   **Meeting Scheduling**: Lindy can act as a meeting scheduler, handling email correspondence to find available times and send calendar invites, including office addresses for in-person meetings <a class="yt-timestamp" data-t="13:36:19">[13:36:19]</a>.
*   **Meeting Preparation (Swarm of Swarms)**: A complex Lindy setup can check daily meetings, deploy an [[building_ai_agent_platforms_with_crewAI | agent swarm]] for each meeting, and then another swarm for each attendee <a class="yt-timestamp" data-t="11:31:37">[11:31:37]</a>. This swarm searches for meeting notes, emails, and LinkedIn profiles to compile a daily digest email for the user <a class="yt-timestamp" data-t="11:47:39">[11:47:39]</a>.

### Executive Assistant Functions
Lindy can replace approximately 70% of typical executive assistant tasks <a class="yt-timestamp" data-t="08:17:34">[08:17:34]</a>. This includes note-taking, scheduling, meeting preparation, and making reservations <a class="yt-timestamp" data-t="08:23:44">[08:23:44]</a>. Lindy can even make phone calls, as demonstrated by an [[voicedriven_ai_applications | AI agent]] successfully making a dinner reservation at a popular restaurant, even interacting with another [[voicedriven_ai_applications | AI agent]] on the receiving end <a class="yt-timestamp" data-t="08:28:50">[08:28:50]</a>. Lindy has also been used to cancel flights via phone call <a class="yt-timestamp" data-t="10:02:14">[10:02:14]</a>.

### Recruitment and Sales Prospecting
*   **Recruitment**: Users can create a Lindy recruiter by providing criteria for desired candidates. The agent can search for people, present a list for selection, and then use an [[building_ai_agent_platforms_with_crewAI | agent swarm]] to research selected individuals (e.g., on Perplexity) and send personalized outreach emails <a class="yt-timestamp" data-t="16:04:19">[16:04:19]</a>. This process can be scaled to hundreds of leads and can be set up to send reminders <a class="yt-timestamp" data-t="18:53:14">[18:53:14]</a>.
*   **Sales Prospecting**: Lindy can be used for sales prospecting by uploading CSVs of leads and initiating personalized outreach campaigns <a class="yt-timestamp" data-t="20:50:06">[20:50:06]</a>. It can customize messages based on detailed information about the recipient <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>.

### Other Applications
*   **Customer Support**: With over 1,600 integrations, Lindy can automate customer support across various platforms like Telegram, Slack, WhatsApp, Zendesk, and Intercom <a class="yt-timestamp" data-t="26:20:25">[26:20:25]</a>.
*   **Focus Groups and User Research**: Lindy can simulate user personas based on training data, allowing companies to conduct virtual focus groups for feedback on products and ideas at a fraction of the cost <a class="yt-timestamp" data-t="26:48:29">[26:48:29]</a>. This can be used to iterate on an app MVP with feedback from thousands of virtual users <a class="yt-timestamp" data-t="28:32:00">[28:32:00]</a>.
*   **Virtual Stand-ups ("Elon Lindy")**: This [[voicedriven_ai_applications | AI agent]] makes phone calls to team members weekly for virtual stand-ups, asking about their accomplishments, and then compiles a summary report for leadership <a class="yt-timestamp" data-t="28:50:00">[28:50:00]</a>. It's being used by companies with over a thousand employees, potentially replacing parts of middle management <a class="yt-timestamp" data-t="29:36:20">[29:36:20]</a>.
*   **Competitive Analysis**: A "competitive tracker" Lindy can wake up monthly, pull a list of competitors from a spreadsheet, and deploy an [[building_ai_agent_platforms_with_crewAI | agent swarm]] for each competitor <a class="yt-timestamp" data-t="30:37:37">[30:37:37]</a>. It gathers information such as employee count, traffic estimates, news, funding, and hiring data <a class="yt-timestamp" data-t="30:47:00">[30:47:00]</a>. The agent then logs this data into a spreadsheet and provides reports on competitor trends <a class="yt-timestamp" data-t="31:01:22">[31:01:22]</a>.
*   **CRM/Network Management**: A Lindy can help manage a professional network by adding new contacts to a spreadsheet and providing lists of contacts based on criteria (e.g., location, profession) <a class="yt-timestamp" data-t="33:04:14">[33:04:14]</a>. It can also observe a user's inbox for flight confirmations and then suggest contacts in the destination city from their CRM <a class="yt-timestamp" data-t="33:53:00">[33:53:00]</a>.
*   **Influencer Outreach**: Lindy is used by brands to find influencers on platforms like TikTok, Instagram, and YouTube, find their contact information, and offer partnerships <a class="yt-timestamp" data-t="25:34:00">[25:34:00]</a>. It also helps manage incoming partnership requests for high-volume creators <a class="yt-timestamp" data-t="25:18:00">[25:18:00]</a>.

## Getting Started

Flo recommends starting with personal assistant-type [[ai_agents_and_their_applications | AI agents]] like meeting schedulers, meeting prep, and meeting recorders due to their ease of setup <a class="yt-timestamp" data-t="15:07:07">[15:07:07]</a>. Lindy offers hundreds of templates, including a "personal assistant starter pack" <a class="yt-timestamp" data-t="15:26:00">[15:26:00]</a>.

> "There is a huge gap right now between what is possible and what people are actually doing. There's there's a huge arbitrage and you can see it because the companies that are actually exploiting this arbitrage are blowing up." <a class="yt-timestamp" data-t="23:32:00">[23:32:00]</a>

The rapid pace of innovation in [[building_apps_with_ai_tools | building apps with AI tools]] and [[ai_agents_and_their_applications | AI agents]] presents a significant opportunity for those who adopt these technologies early <a class="yt-timestamp" data-t="35:48:00">[35:48:00]</a>. Lindy.AI offers a custom sign-up link for a 50% discount and a longer free trial at lindy.ai/greg <a class="yt-timestamp" data-t="35:23:00">[35:23:00]</a>.