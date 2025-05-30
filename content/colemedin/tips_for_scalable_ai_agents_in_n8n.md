---
title: Tips for scalable AI agents in n8n
videoId: Nsu9BzQv5C4
---

From: [[colemedin]] <br/> 

[[N8N in creating AI agents | n8n]] is a no-code AI automation tool designed for [[Building AI Agents with n8n | building AI agents]] and integrating them with over 500 applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide provides key tips for leveraging [[N8N in creating AI agents | n8n]] effectively, especially for [[Prototyping AI agents using n8n | prototyping]] and deploying scalable AI agents.

## Memory Management for Scalable AI Agents

When [[Prototyping AI agents using n8n | prototyping AI agents using n8n]], it's crucial to select scalable memory solutions for production environments <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

*   **Avoid Non-Scalable Options**: For production AI agents, it is highly recommended to avoid `windowed buffer memory` for chat history and the `in-memory vector store` for RAG (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. These options run in the memory of your [[N8N in creating AI agents | n8n]] instance and do not scale well once users are on the platform <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.
*   **Recommended Scalable Solution: Superbase**: Superbase is an excellent and easy-to-set-up alternative for scalable AI agent memory <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
    *   **Postgres for Chat Memory**: Utilize the PostgreSQL database within Superbase for robust and scalable chat memory <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
    *   **PG Vector for RAG Embeddings**: Superbase includes a `PG Vector` extension, which allows for storing embeddings for RAG purposes within the Superbase vector store <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. This ensures a production-ready and highly scalable solution on a single platform <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

## Choosing Large Language Models (LLMs) and Embedding Models

The choice of LLM depends largely on the specific use case <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>, but general recommendations can help in [[Prototyping AI agents using n8n | building workflows]] quickly <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.

*   **Best Overall LLM**: For the absolute best performance, consider Anthropic's Claude 3.5 Sonnet <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   **Fastest LLM**: If speed is the priority and extreme power isn't required, Groq's Llama model is a good choice <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   **Affordable and Strong LLM**: For a balance of affordability and strength, OpenAI's GPT-4o mini is recommended <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   **Embedding Model**: For embedding models, OpenAI's `text-embedding-3-small` is highly recommended <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. The same model chosen for the chat model should also be used for processing chunks from RAG <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

## Working with [[Creating RAG AI agents using n8n | RAG AI Agents]]

[[Creating RAG AI agents using n8n | RAG AI agents]] require specific considerations, particularly regarding file processing and data handling <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

### Handling File Types for Text Extraction

Extracting text from different file types requires separate nodes in [[N8N in creating AI agents | n8n]] <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. For instance, extracting text from a PDF document requires a different node than extracting from a plain text or Excel document <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.
You must include all necessary "extract from file" nodes in your workflow based on the file types you plan to ingest into your vector database <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.

### Working with Previous Node Outputs

When [[Creating powerful AI workflows with n8n | creating powerful AI workflows with n8n]], referencing previous node outputs is fundamental.

*   **Test Execution**: To access the output of a node for use in a subsequent node, you must first run a test execution of the preceding node by clicking "Test Step" <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This populates the output panel on the left, allowing you to drag and drop values to create expressions <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.
*   **Referencing Immediate Previous Node**: The `json.` prefix (e.g., `{{$json.fileId}}`) only works to reference values from the node immediately preceding the current one <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Referencing Older Nodes**: To reference values from nodes further back in the workflow, you must explicitly use the node's name (e.g., `{{$node["Set File ID"].json.fileId}}`) <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

### Setting Up API Endpoints and In-Platform Testing

For [[Integrating AI Agents in n8n using Open Web UI | integrating AI agents in n8n using Open Web UI]] or custom code, setting them up as API endpoints is essential <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

*   **Webhook Node**: Use a "Hook" node as the entry point for your agent to expose it as an API endpoint <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **In-Platform Chat Testing**: To test your agent directly within the [[N8N in creating AI agents | n8n]] platform using the chat widget, add a "When Chat Message Received" trigger <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   **Combining Inputs**: You can combine both the webhook and chat trigger inputs into a single "Edit Fields" node using JavaScript syntax to intelligently grab the defined value from either input, ensuring the agent functions regardless of the trigger <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

### Proper Looping and Handling Multiple Items

When nodes output multiple items, [[N8N in creating AI agents | n8n]] automatically handles looping, processing each item sequentially for the next node <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>. However, careful consideration is needed for how these multiple items are handled.
For example, if a Google Drive trigger outputs two files simultaneously, the workflow must be designed to process both <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. A "Summarized" node at the end can concatenate outputs from multiple files into a single parameter before sending it to an LLM <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. Always think through how your workflow will manage multiple items in a single output <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

## Advanced [[Creating powerful AI workflows with n8n | n8n Workflows]] Tips

Beyond basic setup, several features enhance development speed and production readiness.

### Data Pinning

Data pinning is an underutilized feature that significantly speeds up development <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>. Normally, when you refresh [[N8N in creating AI agents | n8n]], test event outputs are lost, requiring re-execution <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.
By clicking the "Pin Data" button in a trigger node's top right, its specific output will persist even after a hard reload, eliminating the need to re-execute test events <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

### Error Workflows

[[Creating powerful AI workflows with n8n | Error workflows]] are crucial for making [[N8N in creating AI agents | n8n]] workflows production-ready by handling issues gracefully <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **Create an Error Workflow**: Design a dedicated workflow starting with an "Error" trigger node <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. This workflow can send notifications, such as a Slack message with error details, alerting you to problems <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.
*   **Hook into Main Workflow**: In any workflow you want to monitor, click the three dots in the top right, go to "Settings," and select your created error workflow under "Error Workflow" <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. If an error occurs in the main workflow, it will trigger the error workflow, providing production monitoring <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### Schedule Trigger

The "Schedule" trigger is valuable for workflows that need to run at specific intervals rather than being event-based <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
This is ideal for tasks like generating daily reports (e.g., fetching overdue tasks from Asana and sending Slack alerts) which cannot be triggered by an event within an application <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>. The schedule trigger ensures consistent execution at set times <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.

### [[N8N in creating AI agents | n8n]] Workflow Library

The [[N8N in creating AI agents | n8n]] workflow library is an extensive resource with over a thousand workflow templates <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.
You can search by application, keywords, or specific nodes (e.g., "Superbase Vector Store" to find relevant examples) <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>. These templates can serve as excellent starting points for [[Prototyping AI agents using Flowise and n8n | building your own workflows]] <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.