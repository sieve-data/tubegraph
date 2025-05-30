---
title: Voice Flow platform for AI agents
videoId: 0c05ijEmk2g
---

From: [[colemedin]] <br/> 

[[Building AI Agents | Building AI Agents]] often requires granular control over details to ensure the AI agent fits specific needs and is production-ready <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Voice Flow is highlighted as a no-code platform that simplifies the [[Building AI Agents | building of AI agents]] while providing the necessary control <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Core Mission and Capabilities

Voice Flow's mission is to act as the "brain" connecting a front-end (e.g., a React application) and various back-end services (e.g., Slack, Google Drive, other AI agents) <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. It provides an AI agent that understands different tools and can direct conversations for users <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

### Key Features

Voice Flow offers extensive control, including:
*   Managing the Retrieval-Augmented Generation (RAG) pipeline <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   Handling different conversation flows <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Integrating with various tools <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   Adding custom code if desired <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   Features for debugging, monitoring, and analyzing agents in production <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
*   Designed to be an enterprise-level platform <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.
*   Considered more competitive in pricing compared to platforms like [[Prototyping AI agents using Flowise and n8n | Flowise]], especially if not self-hosting <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. It simplifies setting up a RAG pipeline or knowledge base compared to [[Prototyping AI agents using Flowise and n8n | n8n]] <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

### Deployment Options

[[Deploying AI agents using Voice Flow | Voice Flow agents]] can be deployed as:
*   An embeddable chat widget on a website <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.
*   An API endpoint <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.
Deployment is noted for its ease and customizability <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

## Getting Started with Voice Flow

Users can begin for free by creating an account on the Voice Flow homepage <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. The dashboard allows for the creation of new agents <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. Extensive documentation and video courses are available to help users get started with robust use cases <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

## Building an AI Agent: An Example with n8n

A simple [[Building AI Agents | AI agent]] can be constructed using Voice Flow and integrated with an [[Prototyping AI agents using Flowise and n8n | n8n]] workflow to send messages in Slack <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

### Knowledge Base

Voice Flow emphasizes the knowledge base as a "forefront" feature of the agent dashboard <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. This is crucial for the RAG pipeline, providing an internal knowledge base (e.g., for e-commerce products) <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.

Data sources that can be ingested include:
*   URLs <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>, including an entire site map <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   Uploaded files <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   Plain text <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
*   Integration with ZenDesk <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

### Workflows

Workflows define the operations for the agent and how conversation flow occurs <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. The platform uses a drag-and-drop workflow builder similar to [[Prototyping AI agents using Flowise and n8n | n8n]], [[Using Vector Shift for Voice Bots | Vector Shift]], or [[Prototyping AI agents using Flowise and n8n | Flowise]] <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.

Workflow actions can include:
*   Getting a response from the AI <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.
*   Sending a raw message <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
*   Listening for a trigger <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
*   Capturing specific input to store in variables <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   Logic nodes and development nodes <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   Creating custom functions with JavaScript <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.
*   API endpoints <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>, enabling integration with any service <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.

### Content Management

The content tab offers features like:
*   **Components**: Reusable workflows that can be added within other workflows <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.
*   **Variables**: For storing context throughout a conversation, such as clarifying questions or user input, which can be referenced later in AI prompts or external API calls <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
*   **Custom Functions**: Allowing JavaScript to create custom logic that can be used as nodes in workflows <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

### Intents and Entities

[[Creating workflows and intents in Voice Flow | Intents and entities]] are crucial for defining tools and instructing the agent on when to invoke them <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

*   **Intents**: Provide instructions to the [[AI voice systems and integration | AI agent]] on when to use a tool <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>. This includes a description and example "utterances" (what a user might say) <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>. AI can also generate additional utterances <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. Voice Flow allows customization of the [[Voice AI advancements and applications | AI model]] and prompt that determines tool usage, offering a high level of control <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>.

*   **Entities**: Represent input variables required for a tool to function <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>. For example, to send a Slack message, the "slack message" itself would be an entity <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>. The [[Voice AI Agents | AI agent]] will intelligently interact with the user to collect all required entity values before calling the tool <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. This ensures the agent has all necessary information (e.g., meeting name, time, guests for an appointment booking tool) <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

### Debugging and Testing

Voice Flow provides a debug version of the agent that shows all intents, decisions made, and variables set behind the scenes, allowing verification of correct agent behavior <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.

### Integration Example: n8n and Slack

In a practical example, an [[AI voice systems and integration | AI agent]] in Voice Flow is configured to send Slack messages via an [[Prototyping AI agents using Flowise and n8n | n8n]] workflow.
1.  An intent named "send a slack message" is created, with example utterances like "I need support" or "I need to send a slack message" <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>.
2.  A required entity, "slack message," is defined to capture the text the user wants to send <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.
3.  A workflow named "send a slack message tool" is created, triggered by the "send a slack message" intent <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
4.  This workflow makes a POST request to an [[Prototyping AI agents using Flowise and n8n | n8n]] webhook URL, passing the "slack message" entity as part of the request body <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
5.  Success or failure messages are then displayed to the user based on the API call's outcome <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>.

## Deployment

After [[Deploying AI agents using Voice Flow | building an agent]], it can be published and integrated. The platform provides code for an embeddable chat widget or an API key for API endpoint usage <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>. An example deployment involved embedding the Voice Flow chat widget code into a simple HTML/JavaScript application created with AutodDev (a bolt.new fork) <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.

Voice Flow is described as making it "so easy these days to [[Building AI Agents | build any AI agent]] that you want without code and still have all the control that you need" <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>. This flexibility allows for integration with any [[AI voice systems and integration | services]] needed to build a desired agent <a class="yt-timestamp" data-t="19:00:00">[19:00:00]</a>.