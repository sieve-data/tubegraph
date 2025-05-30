---
title: Tools and resources for building AI agents
videoId: fcTtO57zH0s
---

From: [[customaistudio]] <br/> 

[[Building and deploying AI agents|Building and deploying AI agents]] is accessible to anyone, even without programming or AI engineering experience, through the use of [[nocode_ai_platforms_for_building_agents|nocode AI platforms]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These platforms allow for rapid agent development, with some agents capable of being built in an afternoon to fulfill specific workflows <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Core Platforms and Technologies

*   **Nocode Platforms:** These platforms serve as a "one-stop shop" for [[building_and_deploying_ai_agents|building and deploying AI agents]] and their associated tools <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.
    *   **N8n:** Primarily used for building agents and their tools <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>, offering a streamlined environment for [[creating_customizable_tools_for_ai_agents|creating customizable tools for AI agents]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Large Language Models (LLMs):**
    *   **OpenAI API:** Utilized to access models like GPT-4o, providing the core AI intelligence for agents <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, enabling them to understand requests and make decisions <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. [[utilizing_openai_api_for_ai_agent_development|Utilizing OpenAI API for AI agent development]]
*   **Vector Databases:**
    *   **Pinecone:** Used as a vector database to create the knowledge base for agents, providing contextual understanding and awareness necessary for accurate task completion <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Common Agent Tools and Functionalities

Many AI agents share a common set of tools, reflecting the typical tech stack of businesses <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. These tools enable agents to interact with various systems and data sources.

*   **Email Actions:** Allow agents to send, retrieve, and reply to emails <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Calendar Actions:** Enable agents to update, create, and delete calendar events <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Google Drive Integration:** Permits agents to pull and access documents from Google Drive <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **CRM (Customer Relationship Management) Integration:** Essential for managing lead information and client data <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Project Management Tools:** Integration with platforms like Trello or Asana allows agents to interact with and update project statuses <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **Knowledge Base / Vector Store:** Agents leverage these to retrieve contact information and other relevant data <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. This gives them the contextual understanding needed for tasks <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Memory/Context Management:**
    *   **Window Buffer Memory:** Gives agents context of past conversations, typically storing a set number of previous messages to maintain continuity <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Specialized Agent Tools

Beyond the common tools, specific agents utilize unique functionalities tailored to their objectives.

*   **For Personal Agents:**
    *   **Telegram Integration:** Used as an access point to trigger the agent by sending messages <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   **Calculator and Wikipedia:** Basic utility tools provided for general information retrieval and computation <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   **Update Database Tool:** Allows manual addition of information to the vector store/knowledge base, useful for capturing new contacts from networking <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **For Lead Nurturing Agents:**
    *   **Autofixing Output Parser:** Ensures the agent's output is in a specific JSON package format, enabling seamless integration with email sending nodes <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
*   **For Lead Enrichment Agents:** These agents gather information about leads to make sales engagements more compelling <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
    *   **Google Search (Ser API):** Used to perform general web searches about individuals or companies for additional context <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.
    *   **Website Scraper:** Gathers information from a lead's website, summarizes it, and saves it to the CRM <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
    *   **LinkedIn Scraper:** Collects publicly available information from LinkedIn profiles <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.
    *   **Google Sheets (as CRM):** A simple CRM solution where enriched lead data is stored <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
    *   **Find LinkedIn Profiles (Tool):** A specialized tool that can search for LinkedIn profiles based on parameters like location and industry, then compile them into a sheet <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. This serves as a quick prospecting tool <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>.
*   **For Inbox Management Agents:**
    *   **Gmail Integration:** Triggers the agent upon receiving any new email <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.
    *   **Categorization Tools:** Handle specific rules for categorizing emails (e.g., promo, lead, sales), preventing the agent from needing to manage complex rule sets directly <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
    *   **Notify Tool:** Alerts the user when a high-priority or urgent email requires a human response <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>.

> [!NOTE] Building unique tools based on specific business workflows, offers, and ideal customer profiles (ICPs) provides immense flexibility and opportunity <a class="yt-timestamp" data-t="00:32:28">[00:32:28]</a>.
>
> [!TIP] The speaker emphasizes that the agent's main job is to identify and reason about what needs to be done with an email, while the specific details and actions are handled by specialized tools <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>. This approach keeps the agent's core function clear and prevents "tool overload" <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>.