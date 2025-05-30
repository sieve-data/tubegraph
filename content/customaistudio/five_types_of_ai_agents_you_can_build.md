---
title: Five types of AI agents you can build
videoId: fcTtO57zH0s
---

From: [[customaistudio]] <br/> 

AI agents are designed to assist businesses by increasing margins, decreasing scaling costs, and potentially eliminating the need to increase headcount for maintaining current operations or handling common tasks [00:00:44]. Instead of hiring for roles that involve repetitive tasks like combing lead lists or following up with clients, [[developing_ai_agents_and_their_market_potential | AI agents]] can handle these, allowing human employees to focus on higher-level, more skilled work [00:01:00]. These agents can be built using [[nocode_ai_platforms_for_building_agents | no code platforms]] like N8N, leveraging OpenAI's GPT-4o model via API, and utilizing Pinecone for a vector database to establish a contextual knowledge base [00:00:04].

## [[building_and_deploying_ai_agents | Building and Deploying AI Agents]]
The process for [[building_and_deploying_ai_agents | building and deploying AI agents]] involves using platforms like N8N, which serves as a "one-stop shop" for both agents and their accompanying [[tools_and_resources_for_building_ai_agents | tools and resources]] [00:02:56]. This setup allows for quick creation of agents and integration of [[creating_customizable_tools_for_ai_agents | customizable tools for AI agents]] needed to fulfill workflows [00:03:00]. Key components often include:
*   **OpenAI Chat Model**: For the agent's core AI capabilities [00:03:40].
*   **Window Buffer Memory**: To retain context from past conversations, typically up to 20 messages [00:03:55].
*   **Pinecone Vector Store**: Acts as the agent's knowledge base, often used for retrieving contact information or other data [00:04:35].
*   **Tools**: Agents are equipped with specific tools to perform tasks, such as email actions, calendar actions, database updates, and Google Drive access [00:04:33]. Common tools across many agents include email, calendar, project management software (like Asana or Trello), and document databases (Google Drive, Notion, OneDrive, Dropbox) [00:14:26].

### 1. Personal Agent
A personal agent is designed to execute actions upon a user's request and is utilized almost daily by its creator [00:02:09].
*   **Objective**: To perform tasks based on explicit user instructions [00:02:12].
*   **Tools**: Email, Calendar, Google Drive, Update Database [00:02:16]. Future additions may include CRM and project management [00:02:21]. It can also be given general tools like a calculator and Wikipedia [00:03:48].
*   **Access**: Primarily accessed via a Telegram channel, where messages trigger the agent's actions [00:03:26].
*   **Functionality**: Can handle multi-step tasks, such as sending an email and scheduling a calendar event simultaneously [00:06:13]. The agent uses its knowledge base to retrieve frequently requested information like contact details [00:04:46]. It also allows for manual updates to the knowledge base (e.g., adding new contacts from networking events) [00:05:17].
*   **Benefit**: Saves time on small, repetitive tasks that, while not individually time-consuming, add up over a day [00:09:11]. This agent acts only when told to, making it easy to manage [00:08:21].

### 2. Lead Nurturing Agent
This agent focuses on engaging warm leads effectively to convert them into customers [00:09:32].
*   **Objective**: To send compelling and relevant sales engagement emails to warm leads [00:09:33].
*   **Tools**: Email, Google Drive, and CRM [00:09:37].
*   **Problem Solved**: Addresses the common pain point for small teams and agency owners who lack the bandwidth to consistently nurture leads [00:09:40]. It helps capture revenue from leads who are not immediately ready to buy high-ticket offers but might be interested in lower or medium-ticket products [00:11:17].
*   **Trigger**: Activated by other agents, specifically the CRM management agent, which identifies leads that haven't been contacted in the last seven days [00:12:43]. This ensures consistent follow-ups [00:12:51].
*   **Output**: Requires a specific JSON package output to correctly populate email fields before sending [00:13:46].
*   **Impact**: Can significantly increase revenue by nurturing "silent fans" in a CRM who are willing to buy but haven't received enough touch points or the right offer [00:11:24].

### 3. Customer Success Agent
Designed to streamline client communication and support [00:15:14].
*   **Objective**: To answer questions, retrieve documents, and schedule meetings for clients [00:15:16].
*   **Tools**: Slack or Email (often both), Calendar, Google Drive, and Trello/Project Management software [00:15:20].
*   **Customization**: Each client receives their own dedicated agent with access only to their specific documents and project management information [00:15:30].
*   **Functionality**: Handles quick, easily answerable queries and document requests, automating approximately 40-50% of client queries [00:16:00]. This frees up human customer success personnel to focus on relationship building and high-level problem-solving [00:16:10].
*   **Benefit**: Reduces client churn by providing quicker answers and necessary documents [00:16:34]. Clients quickly adapt and appreciate the efficiency, finding the agent to be a significant asset [00:16:53]. These agents can also be triggered by a customer success person's personal agent to perform specific tasks, demonstrating how agents can work together [00:18:08].

### 4. Lead Enrichment Agent
Crucial for making lead nurturing efforts personalized and effective [00:19:14].
*   **Objective**: To find and save detailed information about leads into the CRM [00:19:27].
*   **Tools**: Google Search (via SerAPI), Website Scraper, LinkedIn Scraper, and CRM [00:19:34].
*   **Functionality**: Scrapes publicly available information from LinkedIn, websites, and Google searches to gather data like company details, articles, or founder profiles [00:20:13]. This information is then summarized and added to the CRM [00:21:06].
*   **Challenges**: LinkedIn scraping can be restrictive, sometimes leading to account flags or temporary bans [00:20:21].
*   **Benefit**: Provides an "extra edge" by supplying the lead nurturing agent with rich context, leading to more compelling and personalized emails that avoid being generic or ending up in spam [00:19:17]. It also equips sales teams with comprehensive briefs about prospects before calls, leading to more productive interactions [00:21:54].

### 5. Inbox Management Agent
A powerful tool for automating email organization and initial responses [00:23:32].
*   **Objective**: To manage a user's inbox by categorizing emails and responding to messages accordingly [00:23:34].
*   **Tools**: Email actions, CRM, Categorization tools, and the ability to trigger other agents [00:23:38].
*   **Functionality**: This agent is typically the first to see incoming emails, categorizing them (e.g., promotional, lead, sales) and applying appropriate labels or tags [00:23:39]. It primarily focuses on triggering other agents (like a lead qualification agent for interested leads) rather than responding to complex emails itself [00:23:40]. The agent's core job is to identify the email and reason what action needs to be taken, with the specific details of that action handled by specialized tools [00:24:40].
*   **Benefit**: Significantly reduces time spent in the inbox by automating categorization and delegating tasks to other agents [00:23:36]. It can also notify the user of high-priority emails, ensuring urgent matters are addressed promptly [00:28:05].

These examples demonstrate the immense flexibility in building [[ai_agent_frameworks_and_platforms | AI agent frameworks and platforms]] and [[creating_customizable_tools_for_ai_agents | creating customizable tools for AI agents]] tailored to specific business needs, offers, or target customers [00:32:18].