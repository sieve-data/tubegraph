---
title: Implementing AI personal assistants in Slack
videoId: oMwipO6cmPQ
---

From: [[colemedin]] <br/> 

Many individuals seek to implement an [[integrating_ai_agents_with_services_like_slack | AI personal assistant in Slack]] to boost productivity, especially given the significant amount of time spent on the platform for team collaboration and community engagement <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Evolution and Importance of AI in Chat Platforms

A few years ago, with the rise of ChatGPT, the concept of using AI as an FAQ personal assistant to automatically generate answers to common questions in Slack channels emerged <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This "RAG" (Retrieval Augmented Generation) implementation has since become one of the most classic AI use cases <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Even today, [[capabilities_of_ai_in_slack_chat_platforms | chat platform assistance]] remains one of the most crucial AI use cases for businesses <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Streamlining AI Assistant Deployment with RunBear

Rather than reinventing the wheel to implement a Slack AI assistant, platforms like RunBear simplify the process <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. RunBear makes it easy and affordable to create single or multiple AI assistants for Slack, and also supports integration with other platforms like Discord or Microsoft Teams <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Key Capabilities of RunBear Assistants

An AI assistant built with RunBear for Slack can:
*   Have RAG (Retrieval Augmented Generation) functionality <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   Search the web <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   Invoke custom tools <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   Summarize Slack conversations and channels <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   Be invited to specific channels to limit which chats are exposed <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Setting Up Your Assistant in RunBear

To get started with RunBear, users can create an account and access a free tier to experiment with a few messages <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The RunBear dashboard features two main tabs for setup: "Integrations" and "Assistants" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

#### Integrations and Knowledge Bases

The "Integrations" tab allows connection to various channels, including Slack, Discord, and Teams <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. For knowledge bases, supported platforms include [[integrating_ai_agents_with_services_like_slack_and_google_drive | Confluence, Google Drive, or Notion]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Connecting these platforms typically involves simple OAuth flows for Slack and API key setup for knowledge bases <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

#### Assistant Configuration

Under the "Assistants" tab, users can [[building_an_ai_agent_for_task_management | build an AI agent]] by:
*   **Naming the assistant:** For example, "Slack Assistant with Knowledge Base" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Providing instructions:** Defining the agent's behavior and response formatting <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Selecting a model:** Various GPT models are available <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Adding an external knowledge source:** Integrating the chosen knowledge base (e.g., Confluence document URL) for RAG functionality <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

#### Available Actions and Custom Functions

RunBear offers numerous built-in actions:
*   Image interpretation and generation <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   Providing the current date (as LLMs often lack this information) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   Web search capabilities <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   Fetching information from a URL (web scraping) <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   Searching and summarizing Slack conversations in specific channels <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

A powerful feature is the ability to add custom functions using the OpenAI specification for function calling, allowing the assistant to perform almost any desired action <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. RunBear also supports connecting existing AI models, including custom agents developed with LangChain and LangServe using their Python SDK <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Inviting and Triggering the Assistant in Slack

After configuring the assistant in RunBear, it can be easily invited to specific Slack channels <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Users can define how the bot is triggered, preventing it from responding to every message. Common triggers include mentioning the assistant (e.g., `@runbear`), specific keywords, or emojis <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Each thread initiated with the assistant maintains a separate chat memory, similar to conversations in ChatGPT <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Practical Demonstrations

AI assistants in Slack demonstrate their utility through various actions:
*   **RAG Query:** An assistant can accurately answer questions based on ingested knowledge base documents, like details about a text stack <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Web Search:** The assistant can perform follow-up queries that require external information, such as searching the web for pricing details of specific services mentioned in previous responses <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This also showcases its ability to use conversation history <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Conversation Summarization:** An assistant can summarize lengthy Slack conversations from designated channels, saving users significant time when catching up on discussions they missed <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This summary can also be refined for conciseness upon request <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

## Conclusion

Implementing a powerful AI personal assistant in Slack is made significantly easier and more efficient with platforms like RunBear <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. These tools offer robust functionalities, from RAG and web search to custom actions and conversation summarization, proving invaluable for boosting productivity and streamlining communication in chat platforms <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.