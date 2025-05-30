---
title: No code AI agent builders
videoId: 0c05ijEmk2g
---

From: [[colemedin]] <br/> 

Developing [[developing_ai_agents_without_coding | AI agents without coding]] can be challenging when seeking platforms that offer significant control over details necessary for a production-ready solution <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Often, custom coding is resorted to, leading to time loss <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. However, platforms like Voiceflow provide an alternative, allowing users to [[building_ai_agents_with_nocode_tools | build AI agents with no-code tools]] while maintaining crucial control <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Voiceflow: A No-Code Solution for AI Agents

Voiceflow aims to be the "brain" connecting a front-end to a back-end <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. It provides an [[understanding_ai_agents | AI agent]] that comprehends various tools and can guide user conversations <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Key Capabilities and Control
Voiceflow offers extensive control over various aspects of an AI agent:
*   **RAG Pipeline Management** Control over the Retrieval Augmented Generation (RAG) pipeline <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Conversation Handling** How the [[building_ai_agents | AI agent]] manages different conversations <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Integrations** Connections with various external tools <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Custom Code** Option to add custom code if needed <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Deployment** Agents can be converted into embeddable chat widgets for websites or API endpoints, making deployment easy and customizable <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Production Features** Includes features for debugging, monitoring, and analyzing agents in production, demonstrating an enterprise-level focus <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. These capabilities are crucial for [[building_productiongrade_ai_agents | building production-grade AI agents]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

### Getting Started with Voiceflow
Users can start for free by creating an account and their first agent <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Voiceflow also provides comprehensive documentation and video courses for advanced use cases <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### [[benefits_of_no_code_platforms_for_ai_agents | Benefits of No-Code Platforms for AI Agents]]
Compared to other tools like n8n or Flowise, Voiceflow offers advantages:
*   **Ease of Setup** Setting up components like a RAG pipeline and knowledge base is easier than in n8n <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Competitive Pricing** Pricing is more competitive than Flowise, especially when not self-hosting <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Retained Control** Despite being no-code, it maintains the necessary control over agent functionalities <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Core Components for Building AI Agents in Voiceflow

### Knowledge Base
Voiceflow emphasizes the knowledge base as a "forefront" feature, crucial for any [[understanding_ai_agents | AI agent]]'s RAG pipeline <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Data sources can be ingested from:
*   URLs (single page or full sitemaps) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
*   Uploaded files <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
*   Plain text <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>
*   Integrations like Zendesk <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
An initial knowledge base can be kicked off by importing a web page, which Voiceflow parses to create vectors and train the agent <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Workflows
Workflows define the operations and conversation flow for the agent <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. They utilize a drag-and-drop builder, similar to n8n or Flowise, with various actions:
*   Getting AI responses <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>
*   Sending raw messages <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
*   Listening for triggers <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>
*   Capturing specific user input for variables <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
*   Logic and development nodes, including custom JavaScript functions <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>
*   API endpoints <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
*   Knowledge base searches <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>

### Components and Variables
*   **Components** Reusable workflows that can be embedded within other workflows <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   **Variables** Allow storage of information throughout a conversation, such as clarifying questions or user input, providing context for AI prompts and tool calls <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Intents and Entities
These are critical for defining and invoking tools within the agent <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>:
*   **Intents** Instructions that tell the [[understanding_ai_agents | AI agent]] when to use a specific tool, defined with examples of user utterances (phrases) <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. AI can also generate additional utterances for training <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Users can define the AI model for intent recognition and even customize the prompt, though it's not recommended <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
*   **Entities** Essential input variables for tools. The [[understanding_ai_agents | AI agent]] intelligently interacts with the user to gather values for all required entities before invoking a tool <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

## Building a Basic AI Agent with Voiceflow

A practical example involves [[building_a_nocode_rag_ai_agent | building a no-code RAG AI agent]] in Voiceflow to send messages via an n8n workflow and Slack <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

1.  **Create an Intent:** Define an intent (e.g., "send a slack message") with a description and sample utterances to guide the AI <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
2.  **Add a Required Entity:** For sending a Slack message, a "slack message" entity (a string) is required, ensuring the agent obtains the message content from the user before proceeding <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
3.  **Create a Workflow:** Design a workflow that triggers based on the intent <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
4.  **Make an API Call:** Within the workflow, configure an API block (e.g., a POST request) to the n8n webhook endpoint <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Include necessary headers (e.g., authorization token) and a JSON body referencing the `slack message` entity as the message content <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
5.  **Handle Responses:** Add subsequent message blocks to inform the user about the success or failure of the API call, then listen for the next user message to continue the conversation <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

### Testing and Deployment
Voiceflow offers a debug view to test the agent, showing intent recognition, decisions, and variable assignments <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. Once satisfied, the agent can be published <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. Deployment options include:
*   **Embeddable Chat Widget:** Copy-pasting code into a website (e.g., a simple HTML/JavaScript app created with AutodDev) <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **API Endpoint:** Using an API key to integrate the agent into other applications <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.

This demonstrates how [[no_code_ai_app_builders | no-code AI app builders]] enable integrating AI agents with virtually any service via API endpoints, allowing for the creation of customized agents <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.