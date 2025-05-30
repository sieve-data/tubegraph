---
title: AI agent frameworks and platforms
videoId: 8N2_iXC16uo
---

From: [[customaistudio]] <br/> 

This article explores the evolution of [[developing_ai_agents_and_their_market_potential | AI agents]] over the past 18 months, focusing on the frameworks and platforms used for their development, their core functionalities, and the lessons learned from [[ai_agent_projects_and_learnings | building AI agents]]. The speaker, a non-coder, emphasizes the transformative potential of AI for business leverage and cost reduction <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## What are AI Agents?
[[developing_ai_agents_and_their_market_potential | AI agents]] are essentially Large Language Models (LLMs) like ChatGPT that have the ability to take actions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Unlike ChatGPT, which primarily handles input/output tasks (e.g., writing an email response), an AI agent can perform the action itself (e.g., sending the email) <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This capability to reason and make decisions, and then act upon them, is considered a significant breakthrough for AI <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

The industry is rapidly moving towards [[current_trends_in_ai_agent_platforms | AI agents]], with many new frameworks and [[current_trends_in_ai_agent_platforms | nocode AI platforms]] being launched regularly <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Even traditional chatbot builders are integrating AI agent capabilities <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## AI Agent Frameworks (Coding Required)
These frameworks are powerful but require coding knowledge, presenting a significant learning curve <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

*   **CrewAI**: Gaining significant traction, it allows multiple AIs (called "crews") to work together <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Autogen**: Created by Microsoft, it works well and is constantly improving for intuitiveness. However, it can be fragile and prone to breaking <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **LangChain**: A highly regarded open-source framework for [[building and deploying AI agents | building agents]], underlying many AI tools <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## [[current_trends_in_ai_agent_platforms | Nocode AI Platforms]] for Building Agents
These platforms aim to simplify [[building and deploying AI agents | agent development]] for users without coding expertise <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

*   **Zapier Central**: Zapier's platform for building "assistants" (AI agents). The speaker finds its approach to building agents unintuitive, suggesting it treats agents more like automations with AI decision-makers rather than virtual assistants <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Voiceflow / Stack AI**: Traditionally chatbot builders, these platforms are now incorporating actions and tools to enable AI agent functionality <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Relevance AI**: A popular platform, possibly from Australia, known for its intuitive interface for building agents <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. Downsides include frequent breakage and occasional difficulty in understanding workflow construction <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Mind Studio**: One of the first no-code platforms explored, known for its simple way to build powerful AI applications and now focusing on AI agents/assistants <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

## Preferred Platform: n8n
The speaker's team has found [[tools_and_resources_for_building_ai_agents | n8n]] to be the most effective platform for [[building and deploying AI agents | building AI agents]] <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Why n8n?
*   **Ease of Use**: It's similar to Zapier or Make but offers a more intuitive visual interface for building agents <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **AI Features**: Provides advanced AI features like OpenAI modules, basic LLM chains, Q&A chains, and summarization chains, often backed by LangChain <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **No-Code**: It allows for powerful no-code agent construction <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Cost-Effective**: Super cheap to operate <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Data Security**: Allows self-hosting on personal servers, offering strong data security <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **Custom Tools**: Enables building complex custom workflows within n8n and using them as tools for agents <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. This allows for comprehensive tools that handle various actions within a single platform (e.g., an "email actions tool" for all inbox interactions) <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.

## Key Learnings for Building Effective Agents
Based on 18 months of [[ai_agent_projects_and_learnings | building AI agents]], several critical components have emerged for effective [[building and deploying_ai_agents | agent development]]:

### Data is King
The effectiveness of [[developing_ai_agents_and_their_market_potential | AI agents]] is directly proportional to the quality and timeliness of the data they receive <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Just as a human employee needs to be onboarded and trained with current business context, so too do agents require up-to-date information <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

### Data Collection and RAG (Retrieval Augmented Generation)
Maintaining an up-to-date knowledge base is crucial. This is achieved by building and continuously updating a vector database <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Vector Databases**: These store information that the agent can retrieve. The speaker's team uses Pinecone, noting its ease of setup, reliability, and low cost <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. Superbase also offers vector embeddings but is more complex to set up <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
*   **Automated Data Collection**: To keep the database current, automations are built to collect real-time information from business operations (e.g., emails sent, calendar events, new leads) and save it directly to the database <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

### Automated Prompt Engineering
Effective prompts are vital for agent performance. Without a structured approach, agents can flounder or work inconsistently <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. A strong prompt template includes:
1.  **Objective**: A clear, broad overview of the agent's role <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
2.  **Context**: Specific details about the environment and the agent's responsibilities, including categories, priority levels, and available tools <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
3.  **Instructions**: Detailed steps on how the agent should perform its job, similar to Standard Operating Procedures (SOPs) for human employees <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
4.  **Output Requirements**: Specifies the format or type of output expected from the agent after completing a task <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
5.  **Examples**: Crucial for agent success, examples demonstrate how the agent should react to different scenarios, significantly increasing reliability <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

### Tools
Tools are what grant an AI agency, allowing it to perform actions <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. The agent analyzes incoming messages, determines which tools are needed, and executes the task <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>. As demonstrated with n8n, custom complex workflows can be built and then provided to the agent as tools <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>.

### Integrations
When considering integrations, it's beneficial to think of the agent as a human employee. What platforms or systems would a human performing this role need access to? <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>. This means providing agents with broad access to necessary APIs (e.g., Google, Microsoft, Slack) and ensuring they can perform all relevant actions within those platforms <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>. Integrations also involve ensuring the agent receives all necessary data streams to trigger its tasks <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.

### [[ai_agent_architecture_and_scalability | Architecture]]
The architecture of [[building and deploying_ai_agents | AI agent teams]] is a significant learning. The optimal approach is to organize agents by "job functions," with each job function comprising various "workflows," and each workflow breaking down into "tasks" <a class="yt-timestamp" data-t="00:30:56">[00:30:56]</a>.

Unlike rigid automations that break with edge cases, agents excel at handling various tasks within a workflow using reasoning <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a>. For example, a "Lead Generation AI Agent Team" might consist of specialized agents:
*   **Inbox Management Agent**: Handles incoming emails, kicks interested leads to the qualification agent <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>.
*   **Lead Qualification Agent**: Responds to queries, qualifies leads, and schedules appointments <a class="yt-timestamp" data-t="00:35:14">[00:35:14]</a>.
*   **Lead Enrichment Agent**: Searches online (Google, LinkedIn) for lead information, scrapes data, summarizes it, assigns a quality score, and saves to the CRM <a class="yt-timestamp" data-t="00:35:49">[00:35:49]</a>.
*   **Lead Nurturing Agent**: Periodically checks the CRM for leads needing follow-up, drafts emails, finds relevant content, and sends it <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

This decentralized [[ai_agent_architecture_and_scalability | architecture]], where agents are triggered by specific events to complete a single workflow, is more effective than trying to create complex group chats or centralized commanders <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>.

## The Future: Leverage through AI Agents
The speaker firmly believes that [[developing_ai_agents_and_their_market_potential | AI agents]] represent the next major step in technological innovation, offering immense leverage for businesses <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>. Instead of focusing on hiring more human employees to scale or maintain operations, businesses will increasingly ask: "Can we build an [[developing_ai_agents_and_their_market_potential | AI agent]] or a team of [[developing_ai_agents_and_their_market_potential | AI agents]] to fulfill this job?" <a class="yt-timestamp" data-t="00:39:54">[00:39:54]</a>. This shift will drastically decrease the cost of scaling, increase profit margins, and free up resources to hire high-value human employees who can drive exponential business growth <a class="yt-timestamp" data-t="00:41:19">[00:41:19]</a>.