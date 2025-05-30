---
title: VectorShift platform for building AI agents
videoId: ieLdMih5_V0
---

From: [[colemedin]] <br/> 

VectorShift is a drag-and-drop component workflow builder that specializes in AI, making it easier to [[building_ai_agents | build powerful, robust, and simple AI agents]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. It offers a convenient and fast way to develop agents, particularly useful for simple use cases or quick proofs of concept, where coding an AI agent from scratch might be overly time-consuming <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Getting Started with VectorShift
To begin, users can visit VectorShift and utilize its free tier, which allows for the creation of a first knowledge base for RAG (Retrieval Augmented Generation) and a first workflow <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

Upon signing in, users are presented with a dashboard that highlights three main components necessary for [[creating_a_rag_ai_agent_with_vectorshift | building a RAG AI agent]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>:
*   **Chatbots**: Used for integrating the AI agent into a website <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Knowledge**: Manages connections to data sources for the knowledge base, such as Google Drive to ingest Google Docs <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Pipelines**: Where workflows are created, which can include AI functionalities for the chatbot <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Building a RAG AI Agent
An example of [[creating_a_rag_ai_agent_with_vectorshift | building a full RAG AI agent]] involves two primary steps:

### 1. Setting up the Knowledge Base
To create a knowledge base, navigate to the "Knowledge" section and add an integration, such as a Google Drive folder <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Users can name their knowledge base (e.g., "test KB") and customize settings like chunk size or embedding model, though defaults are often sufficient <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Documents from the selected folder are quickly added as vectors into the knowledge base <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. A key feature is the continuous syncing of the Google Drive folder with the knowledge base, automatically reflecting any document deletions, creations, or updates <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### 2. Creating the Pipeline Workflow
Pipelines are built using a drag-and-drop interface:
*   **Input Component**: The starting point of any workflow, typically configured as a text input <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **LLM Integration**: An LLM (Large Language Model) component is added, such as Anthropic's Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The input is mapped to the LLM's prompt, which can include multiple variables like the user's input and context from the RAG system <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. A system prompt can also be defined to guide the LLM's behavior <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Knowledge Base Reader**: This component reads from the configured knowledge base (e.g., "test KB") <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. The user's input query is sent to the knowledge base, and the retrieved results are then fed as "context" to the LLM for informed answering <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Output Component**: The final LLM response is directed to an output component, typically of type text <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

This entire process allows for the creation of a RAG AI agent in minutes <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

## Testing and Deployment
After creating the pipeline, it can be tested by deploying changes and running the pipeline, providing inputs to verify that the LLM correctly uses the knowledge base to answer questions <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

For deployment, VectorShift offers various "publish" options:
*   **Automation** <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>
*   **Chatbot**: Can be exported as a URL, an API for custom frontends, or even connected directly to platforms like Slack for use as a personal assistant <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Search** <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
*   **Form** <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>

## Templates and Advanced Capabilities
VectorShift provides numerous templates to help users get started quickly without building workflows from scratch, such as a "Blog article generator template" that demonstrates [[advanced_architecture_for_ai_agents | multiple agents working together]] <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. While the platform simplifies the development process, it is also robust enough to support more complex agents and workflows <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The ability to handle multimodal inputs and outputs further highlights its versatility <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.