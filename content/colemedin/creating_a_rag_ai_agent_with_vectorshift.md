---
title: Creating a RAG AI agent with VectorShift
videoId: ieLdMih5_V0
---

From: [[colemedin]] <br/> 

Developing AI agents exists on a spectrum: from coding complex, highly specific agents from scratch, which requires significant time investment <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, to simple use cases or rapid proof-of-concept development <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. For the latter, platforms can save considerable time compared to "reinventing the wheel" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. [[vectorshift_platform_for_building_ai_agents | VectorShift]] is one such platform that allows users to build powerful, yet simple, RAG (Retrieval Augmented Generation) AI agents in minutes <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## What is VectorShift?
[[vectorshift_platform_for_building_ai_agents | VectorShift]] is a drag-and-drop component workflow builder, similar in concept to n8n, but with a strong focus on AI <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. It facilitates the creation of robust and simple AI agents <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The platform offers extensive power, enabling users to extend simple proofs of concept into more complex solutions <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Getting Started with VectorShift
To begin, navigate to `VectorShift.com` and select "get started" <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. A free tier is available, allowing users to create their first knowledge base and workflow <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This convenience and speed in [[rag_ai_agent_development | developing agents]] highlights the value of such platforms <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

Upon signing in, the dashboard presents several features, but the key components for building an AI agent are:
*   **Chatbots**: Used for integrating the agent into a website <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Knowledge**: For setting up data sources, such as Google Drive, to ingest documents for the RAG knowledge base <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Pipelines**: Where workflows are created, which can include AI functionalities for chatbots <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Building a [[building_a_nocode_rag_ai_agent | RAG AI Agent]]

### Setting up the Knowledge Base
1.  Navigate to the "Knowledge" section <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
2.  Click "New" in the top right corner <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
3.  Name the knowledge base (e.g., "test KB") <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Default settings for chunk size and embedding model are generally suitable <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
4.  Choose "add an integration" to add documents <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
5.  Select "Google Docs" if Google Drive is already authenticated <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
6.  Select the desired Google Drive folder (e.g., a "meeting notes" folder) <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
7.  The documents are quickly added as vectors to the knowledge base <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. This Google Drive integration constantly syncs with files that are deleted, created, or updated in the folder, ensuring a robust and up-to-date knowledge base <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

### Creating the Pipeline (Workflow)
1.  Go to "Pipelines" and create a new pipeline from scratch <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
2.  **Add the Input Component**: This is typically the starting point of any [[vectorshift_platform_for_building_ai_agents | VectorShift]] workflow <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   Name the field "input" and set its type to "text" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Add the LLM Component**:
    *   Drag the output of the "Input" component into the input of an LLM component <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
    *   Select an LLM (e.g., Anthropic's Claude 3.5 Sonnet) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   Set the prompt to include two variables: `input` (from the user query) and `context` (from the RAG knowledge base). For example: "Answer the question using this context to help." <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   Add a system prompt (e.g., "You are a helpful assistant who answers questions to the best of your ability.") <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   Note: While a free tier offers some credits, using your own API key for LLMs might be necessary for extended use <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
4.  **Add the Knowledge Base Component**:
    *   Drag the "Knowledge Base" component into the pipeline <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   Select the previously created knowledge base (e.g., "test KB") <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   Connect the "input" from the initial Input component to the Knowledge Base component; this will be the query for the knowledge base <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Connect the results from the Knowledge Base component (the retrieved context) to the `context` variable in the LLM prompt <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
5.  **Add the Output Component**:
    *   Connect the response from the LLM component to the final "Output" component <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   Name the output "output" and set its type to "text" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

This completes the creation of a [[rag_ai_agent_development | RAG AI agent]] in under five minutes <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

## Testing the AI Agent
After creating the pipeline, it's crucial to test it:
1.  Click "Deploy changes" in the top right <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
2.  Click "Run pipeline" <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
3.  Input a question that the LLM could only answer if it accesses the documents in the knowledge base (e.g., "What are the action items from the 8/23 meeting?") <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
4.  [[improving_rag_ai_agent_accuracy | VectorShift]] provides very fast responses and shows the time taken for each node <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
5.  Verify that the agent correctly retrieves and uses the context to answer the question, confirming its functionality <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

## Deploying the AI Agent
Once validated, the AI agent can be deployed using the "publish" option:
1.  Go to "Export pipeline" in the top right <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
2.  Export options include automation, chatbot, search, or form <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
3.  For a chatbot, select "chatbot," name it (e.g., "test chatbot"), and create it <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
4.  The chatbot can then be exported as a URL, an API for custom frontends, or even connected to Slack for a personal assistant experience <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. [[using_vector_shift_for_voice_bots | Vector Shift]] also offers multimodal capabilities for outputs beyond text <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Further Capabilities and Templates
[[vectorshift_platform_for_building_ai_agents | VectorShift]] simplifies [[rag_ai_agent_development | AI agent development]] by providing numerous templates <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. When creating a new pipeline, examples like a "Blog article generator" are available, allowing users to load them directly, customize credentials, and adapt them <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. These templates often showcase robust workflows, sometimes involving multiple LLMs working together <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

Platforms like [[vectorshift_platform_for_building_ai_agents | VectorShift]] provide immense convenience and speed for [[building_a_nocode_rag_ai_agent | building AI agents]], offering a powerful alternative to coding from scratch when time and simplicity are priorities <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.