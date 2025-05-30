---
title: Run Bear platform for AI integration
videoId: oMwipO6cmPQ
---

From: [[colemedin]] <br/> 

Run Bear is a platform designed to simplify the creation and deployment of AI personal assistants within various chat platforms <a class="yt-timestamp" data-t="01:11:11"></a>. It aims to boost productivity by providing AI tools directly within existing workflows <a class="yt-timestamp" data-t="00:17:09"></a>.

## Overview and Purpose

Many individuals seek to implement AI personal assistants in platforms like Slack to enhance productivity <a class="yt-timestamp" data-t="00:00:00"></a>. This kind of RAG (Retrieval Augmented Generation) implementation, where AI generates answers to frequently asked questions, has become a classic AI use case and remains crucial for businesses <a class="yt-timestamp" data-t="00:41:00"></a>. Run Bear makes it incredibly easy and affordable to create such AI assistants, avoiding the need to "reinvent the wheel" <a class="yt-timestamp" data-t="01:08:08"></a> <a class="yt-timestamp" data-t="01:14:00"></a>.

## Platform Features

### Supported Chat Platforms
Run Bear supports integration with multiple chat platforms, including:
*   Slack <a class="yt-timestamp" data-t="01:23:00"></a>
*   Discord <a class="yt-timestamp" data-t="01:25:00"></a>
*   Teams <a class="yt-timestamp" data-t="01:26:00"></a>

Users can invite their AI assistant to specific channels within a workspace, limiting chat exposure for sensitive information <a class="yt-timestamp" data-t="01:39:00"></a>. Each thread in Slack acts as a separate chat memory, similar to conversations in ChatGPT <a class="yt-timestamp" data-t="08:44:00"></a>.

### Knowledge Base Integration (RAG)
The platform allows for [[integrations_and_collaboration_in_ai_platforms | integrating AI]] assistants with external knowledge sources for RAG functionality <a class="yt-timestamp" data-t="02:59:00"></a> <a class="yt-timestamp" data-t="01:29:00"></a>. Supported knowledge bases include:
*   Confluence <a class="yt-timestamp" data-t="03:14:00"></a>
*   Google Drive <a class="yt-timestamp" data-t="03:15:00"></a>
*   Notion <a class="yt-timestamp" data-t="03:16:00"></a>

Connecting these platforms is straightforward, often involving OAuth flows for Slack or API keys for services like Confluence <a class="yt-timestamp" data-t="03:22:00"></a>.

### AI Capabilities and Actions
Run Bear AI assistants can perform a wide range of actions:
*   **RAG Functionality** <a class="yt-timestamp" data-t="01:29:00"></a>: Using external knowledge bases to answer questions <a class="yt-timestamp" data-t="05:08:00"></a>.
*   **Web Search** <a class="yt-timestamp" data-t="01:31:00"></a>: The ability to search the web for information <a class="yt-timestamp" data-t="06:08:00"></a>.
*   **URL Information Fetching** <a class="yt-timestamp" data-t="06:12:00"></a>: Performing web scraping from a URL <a class="yt-timestamp" data-t="06:13:00"></a>.
*   **Image Interpretation and Generation** <a class="yt-timestamp" data-t="05:56:00"></a>.
*   **Current Date Awareness** <a class="yt-timestamp" data-t="06:00:00"></a>: LLMs often lack current date knowledge, which is important for time-sensitive queries <a class="yt-timestamp" data-t="06:01:00"></a>.
*   **Slack Conversation Search and Summarization** <a class="yt-timestamp" data-t="01:33:00"></a> <a class="yt-timestamp" data-t="06:16:00"></a>: AI can summarize conversations in specific channels <a class="yt-timestamp" data-t="06:18:00"></a>. This is useful for catching up on discussions without reading through many messages <a class="yt-timestamp" data-t="10:58:00"></a>.

An example of its web search capability was demonstrated by asking it to determine the pricing for a text stack including Groq, Pinecone, Olama, and [[superbase_integration_for_ai_projects | Superbase]] <a class="yt-timestamp" data-t="09:11:00"></a> <a class="yt-timestamp" data-t="09:21:00"></a>.

### Custom AI Agents and Functions
Run Bear offers advanced options for customization:
*   **Existing AI Models**: Users can use a base model like OpenAI's GPT <a class="yt-timestamp" data-t="04:03:00"></a>.
*   **Custom AI Agents**: The platform allows connecting custom AI agents built with frameworks like LangChain and LangServe <a class="yt-timestamp" data-t="04:19:00"></a>.
*   **Python SDK**: Users can develop custom AI in Python using Run Bear's SDK and hook it into their assistant <a class="yt-timestamp" data-t="04:26:00"></a>. This provides significant power and flexibility <a class="yt-timestamp" data-t="04:30:00"></a>. This represents an example of [[integrating_ai_agents_with_live_platforms | integrating AI agents with live platforms]].
*   **Custom Functions**: Users can add custom functions using the OpenAI specification for function calling, enabling the assistant to perform virtually any desired action <a class="yt-timestamp" data-t="06:21:00"></a>.

The platform provides a balance between basic usability and powerful extensibility <a class="yt-timestamp" data-t="06:42:00"></a>.

## User Experience and Benefits

Run Bear's dashboard is designed to be simple and user-friendly, with clear tabs for "Assistants" and "Integrations" <a class="yt-timestamp" data-t="02:44:00"></a>.

To set up an assistant:
1.  Users create an account and access a free tier for testing <a class="yt-timestamp" data-t="02:12:00"></a>.
2.  They define the assistant's name and instructions, detailing its behavior and response formatting <a class="yt-timestamp" data-t="04:51:00"></a>.
3.  An external knowledge source is added <a class="yt-timestamp" data-t="05:19:00"></a>.
4.  Actions are selected or custom functions are added <a class="yt-timestamp" data-t="05:47:00"></a>.
5.  Advanced options allow for fine-tuning the assistant's responses <a class="yt-timestamp" data-t="06:50:00"></a>.

The process of [[integrating_ai_with_front_ends | integrating AI]] into a Slack channel is quick, involving a simple invite <a class="yt-timestamp" data-t="08:00:00"></a>. Bots can be triggered by specific keywords, mentions (e.g., @runbear), or emojis, preventing them from responding to every message <a class="yt-timestamp" data-t="07:33:00"></a>.

Run Bear is highlighted as a valuable platform because it significantly reduces the work involved in creating a robust personal assistant with diverse tools and platform connections <a class="yt-timestamp" data-t="12:00:00"></a>.