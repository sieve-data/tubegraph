---
title: Integration of Slack with external knowledge bases like Confluence and Google Drive
videoId: oMwipO6cmPQ
---

From: [[colemedin]] <br/> 

Many individuals seek to implement AI personal assistants within Slack to boost productivity, especially given the significant amount of time spent on the platform for team collaboration and community engagement <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Historical Context and Modern Relevance
A few years ago, with the rise of ChatGPT, there was curiosity within Slack communities about using AI as an FAQ personal assistant to automatically generate answers to frequently asked questions in Slack channels <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This type of Retrieval Augmented Generation (RAG) implementation has since become a classic AI use case <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Despite its classic nature, having chat platform assistants remains one of the most crucial [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI use cases]] for businesses today <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Runar: A Solution for Slack AI Integration
Platforms like Runar make it easy and affordable to create an [[integrating_ai_agents_with_services_like_slack | AI Slack assistant]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Runar allows for the creation of single or multiple AI assistants and supports various chat platforms beyond Slack, including Discord and Teams <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

The Slack chatbot developed with Runar can feature:
*   RAG functionality <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   The ability to search the web <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Invocation of custom tools <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Summarization of Slack conversations and channels <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

Assistants can be invited to specific channels within a Slack workspace, allowing for control over chat exposure and privacy <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Getting Started with Runar
To begin with Runar, users can visit runbear.ai, create an account, and access a free tier to test the platform <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Dashboard Overview
The Runar dashboard features two primary tabs:
1.  **Integrations**: Used for setting up connections to knowledge bases and chat platforms <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
2.  **Assistants**: Where the AI bots are created and configured <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Integrations for Knowledge Bases and Platforms
Runar supports [[integration_with_various_platforms | integration with various platforms]] for chat and knowledge bases <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Knowledge Base Connections
For knowledge bases, Runar supports:
*   Confluence <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>
*   [[integrating_google_drive_as_a_knowledge_base | Google Drive]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>
*   Notion <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>

Connecting these platforms is straightforward; for Slack, it involves a simple OAuth flow <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, while for Confluence, documentation is provided to guide API key creation <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

An example of a RAG demonstration involved using an [[integrating_knowledge_bases_with_ai | AI-generated research document]] on an AI application tech stack, ingested from Confluence by copying its URL <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Creating an Assistant
When adding an assistant in Runar, users have powerful options:
*   **Base Models**: Utilize a base model for simplicity <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Existing AI/Custom Agents**: Connect existing AI solutions, custom GPTs, or even custom [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] developed with LangChain and LangServe <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Runar offers a Python SDK to hook custom AI into assistants <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Assistant Configuration
Assistants can be configured with:
*   **Name**: A descriptive name for the assistant <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Instructions**: Directives on how the agent should behave, including response formatting, and how to use RAG to answer user questions <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Model Selection**: Choice of available GPT models <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **External Knowledge Source**: Addition of external knowledge sources like Confluence documents by providing a URL, which then ingests the content <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Actions and Tools
Runar offers a wide array of built-in actions and the flexibility for custom functions:
*   **Built-in Actions**:
    *   Image interpretation and generation <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>
    *   Current date retrieval (important for LLMs that may not know the real-time date) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>
    *   Web search functionality <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>
    *   Fetching information from a URL (web scraping) <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>
    *   Searching and summarizing Slack conversations in specific channels <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>
*   **Custom Functions**: Users can add custom functions using the OpenAI specification for function calling, allowing for complex actions like those performed by custom agents querying GPT in Python <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

Advanced options are also available for fine-tuning assistant responses <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## Inviting and Testing in Slack
Once an assistant is configured, it can be connected to a Slack channel <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Users can choose how the bot is triggered, such as by mentioning `@run bear`, rather than responding to every message <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Inviting Runar to a specific Slack channel is done by adding the app via the channel's member/integration settings <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### Demonstration of Capabilities
Once integrated, the assistant can perform various tasks:

#### Retrieval Augmented Generation (RAG)
By asking a question that requires information from the connected knowledge base, such as "What is the text stack that I am researching?", the assistant can process the request and provide a perfect answer based on the Confluence document <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Each thread in Slack acts as a separate chat memory, similar to conversations in ChatGPT <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

#### Web Search
The assistant can search the web for information it doesn't already possess, such as pricing for various services mentioned in the knowledge base, demonstrating its ability to fetch external data <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. The assistant also uses conversation history to understand follow-up questions <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

#### Slack Conversation Summarization
A key capability is the ability to summarize Slack conversations in specific channels <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. By inviting Runar to a channel, it can read the conversation history and provide a concise summary, saving users from reading numerous messages and threads when returning to a conversation <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

These examples highlight the ease of creating a powerful personal assistant in Slack that can significantly save time <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Although creating a robust personal assistant with diverse tools and platform connections requires significant effort, platforms like Runar streamline the process, preventing the need to "reinvent the wheel" <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.