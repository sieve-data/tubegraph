---
title: Deploying AI agents using Voice Flow
videoId: 0c05ijEmk2g
---

From: [[colemedin]] <br/> 

[[Voice Flow platform for AI agents|Voice Flow]] provides an easy and customizable way to [[Deploying AI agents using Voice Flow|deploy AI agents]] <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Its mission is to serve as the "brain" connecting a frontend (like a React app) and backend services (like [[Prototyping AI agents using Flowise and n8n|n8n]] workflows, Slack, or Google Drive) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This allows for the creation of [[Understanding AI agents|AI agents]] that understand and direct conversations, integrating with various tools <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Deployment Options

[[Voice Flow platform for AI agents|Voice Flow]] [[Voice AI Agents|agents]] can be turned into two main deployment types:
*   **Embeddable Chat Widget** <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>: A widget that can be embedded directly onto a website <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **API Endpoint** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>: The agent can be accessed as an API endpoint, allowing integration into custom applications <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## How to Deploy
To [[Deploying AI agents using Voice Flow|deploy an AI agent]] created with [[Voice Flow platform for AI agents|Voice Flow]]:
1.  **Publish**: Navigate to the "publish" tab within the Voice Flow interface <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.
2.  **Integrate**: Go to the "integration" tab <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. Here, you can copy the embed code for a chat widget or obtain an API key for an API endpoint <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. Extensive documentation is available for detailed integration steps <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

## Example Integration with a Frontend
An example of deploying a [[Voice AI Agents|Voice Flow agent]] as a chat widget involves creating a simple HTML application:
1.  **Frontend Generation**: Use a tool like Auto.dev (a fork of bolt.new) with an open-source coding model (e.g., DeepSeek Coder v2 236B via OpenRouter) to generate a basic vanilla JS and HTML app <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>, <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.
2.  **Embed Code Integration**: Paste the Voice Flow embed code into the generated HTML file <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
3.  **Testing**: Due to potential CORS issues, it may be necessary to test the HTML file in an online editor (e.g., JSFiddle) rather than directly within the generation environment <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. The chat widget will then appear and function as designed within the web page <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

This demonstrates how a basic [[Building AI Agents|AI agent]] can be integrated with external services, even if the initial [[Prototyping AI agents using Flowise and n8n|n8n]] workflow is simple or trivial <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. The core principle allows for extension to any [[Prototyping AI agents using Flowise and n8n|n8n]] workflow or API endpoint <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.

## Advantages of Voice Flow for Deployment
[[Voice Flow platform for AI agents|Voice Flow]] offers several key advantages for [[Deploying AI agents using Voice Flow|deploying and monitoring AI agents]]:
*   **No-Code Development**: Allows [[Building AI Agents|building AI agents]] without writing custom code, while still maintaining detailed control <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.
*   **Control over Details**: Provides control over aspects like RAG pipelines, conversation handling, integrations, and even custom code if needed <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
*   **Easy Deployment**: Simplified process for turning agents into embeddable widgets or API endpoints <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Debugging and Monitoring Tools**: Includes features for [[Deploying and monitoring AI agents|debugging, monitoring, and analyzing agents]] in production <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Enterprise-Level Capabilities**: Designed to support enterprise-level needs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Robust Knowledge Base Management**: Makes the knowledge base a central part of the agent dashboard, offering diverse data sources (URLs, site maps, files, plain text, Zendesk integration) <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Workflow Definition**: Offers a drag-and-drop workflow builder similar to [[Prototyping AI agents using Flowise and n8n|n8n]], with various actions and logic nodes to dictate conversation flow <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Intent and Entity Management**: Allows precise definition of when and how tools are invoked, handling required input variables (entities) intelligently <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Cost-Effectiveness**: Offers competitive pricing compared to other platforms, especially when considering self-hosting alternatives <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.