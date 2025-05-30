---
title: Creating workflows and intents in Voice Flow
videoId: 0c05ijEmk2g
---

From: [[colemedin]] <br/> 

The [[voice_flow_platform_for_ai_agents | Voice Flow platform for AI agents]] is a no-code tool designed to make it easy to build production-ready [[agentic_workflows_and_ai_technology | AI agents]] while maintaining control over details like the RAG pipeline, conversation handling, integrations, and custom code [00:00:00](<a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, [00:00:29](<a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, [00:00:36](<a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>). Its mission is to serve as the "brain" connecting a frontend (e.g., a React app) and backend services (e.g., Slack, Google Drive, other [[agentic_workflows_and_ai_technology | AI agents]]) [00:01:44](<a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, [00:02:08](<a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, [00:02:15](<a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>).

## Getting Started

Users can start for free by creating an account on the Voiceflow homepage [00:03:30](<a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>). This leads to a dashboard where new agents can be created [00:03:37](<a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, [00:03:51](<a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>). For in-depth learning, Voiceflow provides extensive documentation and videos, including robust use cases [00:02:51](<a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, [00:03:01](<a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>).

## Key Components

### Knowledge Base (RAG Pipeline)

Voiceflow prioritizes the knowledge base, which is crucial for any [[agentic_workflows_and_ai_technology | AI agent]] to have an internal RAG (Retrieval Augmented Generation) pipeline [00:04:37](<a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, [00:04:43](<a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>). When creating a new agent, a web page (e.g., voiceflow.com) can be imported to kickstart the knowledge base by parsing the page, creating vectors, and training the agent [00:04:01](<a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, [00:04:15](<a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>).

Data sources for the knowledge base are robust and include:
*   URLs (individual pages or a whole sitemap) [00:04:54](<a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, [00:04:57](<a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>)
*   File uploads [00:05:02](<a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>)
*   Plain text insertion [00:05:02](<a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>)
*   Integration with Zendesk [00:05:03](<a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>)

### Workflows

Workflows are where the operations for the agent are defined, dictating how conversations flow [00:05:09](<a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>, [00:05:14](<a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>). Voiceflow uses a drag-and-drop workflow builder similar to other [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | no-code and low-code tools like n8n and Voiceflow]] or Flowise [00:05:28](<a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, [00:05:31](<a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>).

Workflow actions include:
*   Getting responses from the AI [00:05:37](<a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>)
*   Sending raw messages [00:05:40](<a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>)
*   Listening for user responses (e.g., button selections, capturing specific input for variables) [00:06:01](<a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>, [00:06:06](<a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>)
*   Logic nodes [00:06:26](<a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>)
*   Development nodes (e.g., custom JavaScript functions, API endpoints, knowledge base search, custom actions) [00:06:28](<a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>, [00:06:35](<a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>)

Additional features within workflows:
*   **Components**: Reusable workflows that can be nested, promoting efficient system building [00:06:59](<a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>, [00:07:08](<a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>).
*   **Variables**: Used to store information throughout a conversation (e.g., clarifying questions) and reference it later in prompts or API calls [00:07:12](<a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, [00:07:24](<a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>).
*   **Custom Functions**: Allow users to write JavaScript to create custom logic nodes [00:07:37](<a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>).

### Intents and Entities

Intents define the "tools" for the agent and specify when the agent should invoke them [00:07:51](<a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, [00:07:56](<a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>).

When creating an intent:
*   **Name**: A simple identifier (e.g., "send a slack message") [00:08:54](<a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>).
*   **Description**: Tells the agent *when* to use the tool (e.g., "trigger this intent when the user wants support or to send a slack message") [00:08:58](<a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>).
*   **Utterances**: Examples of what a user might say to trigger this intent (e.g., "I need support," "I need to send a slack message"). AI can generate more examples [00:09:08](<a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, [00:09:24](<a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>).

Entities are essentially input variables required by a tool [00:09:54](<a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>, [00:09:56](<a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>). Before invoking a tool, the AI agent needs to have values for all required entities [00:10:14](<a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>). The agent will intelligently converse with the user to gather these values [00:10:19](<a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>, [00:10:37](<a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>).

## [[examples_of_ai_agents_and_workflows | Example: Sending a Slack Message via n8n]]

This [[examples_of_ai_agents_and_workflows | example]] demonstrates integrating Voiceflow with an [[creating_custom_ai_workflows_with_n8n | n8n workflow]] to send messages in Slack [00:01:16](<a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, [00:01:21](<a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>).

### 1. Create the Intent

1.  **Name**: "send a slack message" [00:08:54](<a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>).
2.  **Description**: "Trigger this intent when the user wants support or to send a slack message" [00:09:00](<a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>).
3.  **Utterances**: "I need support," "I need to send a slack message" [00:09:16](<a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>, [00:09:21](<a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>).
4.  **Required Entity**: A `slack message` entity (custom data type for a string) is added, ensuring the AI agent obtains the message text before calling the tool [00:09:35](<a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>, [00:09:57](<a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>).

### 2. Create the Workflow

1.  **New Workflow**: Named "send a slack message tool" [00:12:00](<a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, [00:12:05](<a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>).
2.  **Trigger**: The workflow is triggered by the "send a slack message" intent [00:12:18](<a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>, [00:12:24](<a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>). At this point, the `slack message` variable is assumed to be filled [00:12:31](<a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>).
3.  **API Call**: An API (Dev) node is used to make a POST request to an n8n webhook URL [00:12:41](<a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>, [00:12:47](<a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>).
    *   **Headers**: An Authorization Bearer token is included for authentication with the n8n workflow [00:13:08](<a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>, [00:13:10](<a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>).
    *   **Body**: The `slack message` entity's value is passed as the `message` attribute in the JSON body, using curly brackets for variable referencing [00:13:43](<a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>, [00:13:55](<a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>).
4.  **Handling Success/Failure**:
    *   If the API call succeeds, the agent sends a confirmation message like "Your message was sent in slack" [00:14:38](<a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>, [00:14:40](<a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>).
    *   If it fails, a message like "Your message failed to send in slack" is sent [00:15:15](<a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>, [00:15:17](<a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>).
    *   After either outcome, the agent listens for the next user message/trigger [00:15:51](<a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>).

## Testing and Debugging

Voiceflow offers a debug view in the "Run" tab, which shows all intents, decisions, and variable sets behind the scenes. This allows users to ensure the agent is making the correct decisions [00:15:35](<a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>, [00:15:40](<a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>).

## [[deploying_ai_agents_using_voice_flow | Deploying AI Agents using Voice Flow]]

Voiceflow agents can be [[deploying_ai_agents_using_voice_flow | deployed]] easily as an embeddable chat widget on a website or as an API endpoint [00:00:52](<a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, [00:00:55](<a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>). The "Publish" tab allows publishing a version of the agent, and the "Integration" tab provides the embed code or API key [00:16:51](<a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>, [00:16:56](<a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>). For instance, the embed code can be used in a basic HTML/JavaScript application created with tools like Autodev (a Bolt.new fork) [00:17:08](<a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>, [00:17:11](<a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>, [00:17:20](<a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>).

## Comparison to Other Tools

Voiceflow offers advantages over other tools like [[creating_custom_ai_workflows_with_n8n | n8n]] or [[using_flowise_and_n8n_for_local_ai_automation | Flowise]] for building [[agentic_workflows_and_ai_technology | AI agents]]:
*   **Ease of Setup**: Setting up the RAG pipeline and knowledge base is simpler in Voiceflow compared to n8n [00:03:26](<a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, [00:03:31](<a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>).
*   **Pricing**: Voiceflow is generally more competitive in pricing than hosted Flowise, unless Flowise is self-hosted locally [00:03:35](<a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, [00:03:40](<a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>).
*   **Control**: Voiceflow provides a high level of control, even without custom coding, allowing customization of the AI model and prompts for tool selection [00:11:41](<a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>, [00:11:50](<a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>, [00:11:54](<a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>).

The platform's focus on intents and the customization capabilities around them make it powerful for helping agents understand when to use specific tools [00:10:52](<a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, [00:10:56](<a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>).