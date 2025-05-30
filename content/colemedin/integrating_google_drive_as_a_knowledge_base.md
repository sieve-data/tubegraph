---
title: Integrating Google Drive as a knowledge base
videoId: ieLdMih5_V0
---

From: [[colemedin]] <br/> 

Developing AI agents can range from complex, custom-coded solutions to simpler needs requiring quick proof-of-concepts. For the latter, platforms exist that streamline the process, allowing for the creation of powerful AI agents in minutes <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. This article demonstrates how to build a Retrieval-Augmented Generation (RAG) AI agent by [[using_google_drive_as_a_knowledge_base_for_ai_agents | integrating Google Drive]] as its knowledge base, using the platform VectorShift <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.

## Introducing VectorShift

VectorShift is a drag-and-drop component workflow builder, similar to [[using_n8n_to_build_an_ai_knowledge_base | n8n]], but with a strong focus on AI <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>. It simplifies the process of building robust and simple AI agents <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. Many users have endorsed VectorShift for its power and ease of use, making it suitable for both proof-of-concepts and extensive agent development <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

To begin, visit VectorShift.com and click "get started." A free tier is available to create your first knowledge base for RAG and your initial workflow <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. The convenience and speed offered by such platforms for [[integrating_knowledge_bases_with_ai | developing agents]] are significant <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

Upon signing in, the dashboard presents several features, with three main components being key for this task:
*   **Chatbots**: Used for integrating the agent into a website <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Knowledge**: Where the connection to [[using_google_drive_as_a_knowledge_base_for_ai_agents | Google Drive]] is set up to ingest Google Docs as the knowledge base for RAG <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
*   **Pipelines**: For creating workflows, which can include AI elements for the chatbot <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Setting Up Google Drive as a Knowledge Base

1.  **Navigate to Knowledge**: Go to the "Knowledge" section <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
2.  **Create New Knowledge Base**: Click "new" and name it (e.g., "test KB") <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. Default settings for chunk size and embedding model are typically sufficient <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
3.  **Add Integration**: Select "add an integration" to connect your [[integrating_google_drive_with_n8n_for_document_management | Google Drive]] <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. After authenticating, choose "Google Docs" and then select the specific folder (e.g., a "meeting notes" folder) <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
4.  **Ingestion**: VectorShift quickly adds all documents from the selected folder as vectors into the knowledge base within seconds <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. The [[integrating_google_drive_with_n8n_for_document_management | Google Drive]] integration also constantly syncs with the files in that folder, reflecting any deletions, creations, or updates <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>.

## Building the RAG Agent Pipeline

1.  **Start a New Pipeline**: Go to "Pipelines" and create a new pipeline from scratch <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.
2.  **Input Component**: Add an "Input" component, typically the start of any workflow in VectorShift. Name the field (e.g., "input") and set its type to "text" <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.
3.  **LLM Component**: Add an LLM component (e.g., Anthropic's Claude 3.5 Sonnet) <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
    *   Drag the "input" to the LLM's prompt.
    *   Customize the prompt to include variables for both `input` (the user's query) and `context` (from the knowledge base), e.g., "answer the question using this context to help..." <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
    *   Set a system prompt (e.g., "You are a helpful assistant who answers questions to the best of your ability") <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
    *   Note that while the free tier offers some credits, you may need your own API key for continued use <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.
4.  **Knowledge Base Reader**: Drag in a "Knowledge Base" component from the top-left tab <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
    *   Select the previously created "test KB" <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
    *   Connect the initial "input" component to this knowledge base component as the query <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.
    *   Feed the results from the knowledge base (the retrieved context) into the LLM's `context` variable <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
5.  **Output Component**: Drag the LLM's response to an "Output" component, naming it "output" and setting its type to "text" <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

This completes the RAG AI agent, built in under five minutes <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>.

## Testing the AI Agent

To test, click "deploy changes" in the top right, then "run pipeline" <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>. Input a query that requires access to the [[using_google_drive_as_a_knowledge_base_for_ai_agents | Google Drive documents]], such as "what are the action items from the 8/23 meeting" <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>. The responses are fast, providing the answer based on the retrieved context, demonstrating that the agent is working perfectly <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.

## Deploying the AI Agent

Once validated, the AI agent can be deployed using the "publish" option <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.
1.  **Export Pipeline**: Go to "export pipeline" in the top right <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>.
2.  **Choose Export Type**: Options include automation, chatbot, search, or form <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.
3.  **Chatbot Deployment**: Selecting "chatbot" allows you to name it (e.g., "test chatbot") and create it <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>. The chatbot can be customized and then exported as a URL, an API, or even [[integrating_ai_agents_with_services_like_slack_and_google_drive | connected to Slack]] for a personal assistant <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.

## Templates and Conclusion

VectorShift also offers numerous pre-built templates for pipelines, allowing users to get started quickly without building workflows from scratch <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. These templates can be loaded, customized with credentials, and adapted for various agents, such as a blog article generator that uses multiple LLMs working together <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

Platforms like VectorShift provide significant convenience and speed for [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | developing AI agents]], especially when the goal is a quick proof-of-concept or a simple use case <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>. They prevent the need to "reinvent the wheel" by coding everything from scratch, while still offering the robustness to extend agents further <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. This approach makes [[setting_up_and_running_a_local_knowledge_base | building and deploying AI agents]] with external knowledge bases like [[using_google_drive_as_a_knowledge_base_for_ai_agents | Google Drive]] accessible and efficient.