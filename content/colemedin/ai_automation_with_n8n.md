---
title: AI automation with n8n
videoId: Nsu9BzQv5C4
---

From: [[colemedin]] <br/> 

[[workflow_automation_with_n8n|n8n]] is a powerful no-code AI automation tool that allows users to [[building_ai_agents_with_n8n|build any AI agent]] and integrate with over 500 different applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article focuses on underutilized and trickier aspects of the platform to enhance proficiency in [[creating_powerful_ai_workflows_with_n8n|creating powerful AI workflows with n8n]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Key Recommendations for AI Agents

### 1. Scalable Memory for AI Agents
Many n8n tutorials for [[building_ai_agents_with_n8n|AI agents]] often suggest using `windowed buffer memory` for chat history and `in-memory vector store` for RAG (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. However, these are not recommended for production environments as they do not scale well, running directly in the memory of the n8n instance <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

A highly scalable alternative is **Superbase** <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   It includes a SQL database with PostgreSQL, suitable for PostgreSQL chat memory <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   The `PG Vector` extension allows for embeddings for RAG, leveraging the Superbase vector store <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   Superbase provides a production-ready and highly scalable solution within a single platform <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### 2. Choosing Large Language Models (LLMs) and Embedding Models
The choice of Large Language Models (LLMs) within n8n workflows depends on the specific use case <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Absolute Best:** Anthropic's Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Fastest:** Groq's Llama model <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Affordable and Strong:** OpenAI's GPT-4o mini <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

For embedding models, OpenAI's `text-embedding-3-small` is highly recommended <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The same model chosen for the chat model should also be used to process chunks from RAG <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Working with n8n Workflows

### 3. Extracting Text from Different File Types
When building [[using_n8n_to_build_an_ai_knowledge_base|AI knowledge bases]] or RAG agents, different file types require specific n8n nodes for text extraction <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. For example, extracting text from a PDF document requires a different node than extracting from a plain text document or an Excel spreadsheet <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Users must include all necessary extraction nodes in the workflow based on the file types that will be ingested into the vector database <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### 4. Referencing Previous Node Outputs
To reference outputs from previous nodes in a current node, users can run a test execution to generate the output on the left-hand side of the n8n interface <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Values can then be dynamically referenced by dragging them into the desired field, creating an expression <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

**Important Distinction:**
*   `json.file ID` (or `json.value`) can only reference values from the *immediately preceding* node <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   To reference a value from a node further back in the workflow (e.g., two nodes back), the full name of that specific node must be used in the expression (e.g., `set file ID` for a node named "set file ID") <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### 5. API Endpoints and In-Platform Testing for AI Agents
When [[creating_custom_ai_workflows_with_n8n|building AI agents]] in n8n, it's often desirable for them to function as API endpoints for [[integration_capabilities_of_n8n_with_ai_libraries|integration]] with other platforms like Open Web UI or custom Python code <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This is achieved using a **Hook node** as an entry point <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

To facilitate testing the agent directly within the n8n platform via the chat widget, an additional **"When Chat Message Received" trigger** can be added <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. These two triggers can be combined using specific JavaScript syntax in an "Edit Fields" node, allowing the workflow to correctly grab the input value regardless of whether it comes from the chat widget or the web hook <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This setup is valuable for [[prototyping_ai_agents_using_n8n|prototyping AI agents]] and ensuring robust [[using_n8n_for_api_workflows_in_ai_agents|API workflows in AI Agents]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### 6. Handling Loops and Multiple Items in Output
n8n automatically handles looping by processing multiple items from a single node output one at a time for subsequent nodes <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. However, users must carefully consider how to handle scenarios where multiple items are generated simultaneously, such as two files created at the same time triggering a workflow <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

For instance, if two files are processed, the workflow might concatenate their extracted text into a single parameter at a later stage, such as a "summarize" node, before passing it to a large language model <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. The key is to design workflows that explicitly manage multiple items in a single output to avoid unexpected behavior <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### 7. Data Pinning for Faster Development
**Data pinning** is an underutilized feature that significantly speeds up development <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. Normally, a test execution is required to generate the output on the right-hand side, which serves as the input for the next node, allowing for dynamic value referencing <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. This output is lost upon refreshing n8n or closing and reopening the instance <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

By clicking the "Pin Data" button in the top right of a trigger node, its specific output will persist even after a hard reload <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This eliminates the need to repeatedly execute test events, streamlining the development process <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### 8. Error Workflows for Production Readiness
**Error workflows** are crucial for making n8n workflows production-ready by handling unexpected issues <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   To create an error workflow, add an **Error Trigger** node to a new workflow <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   Within this error workflow, actions can be defined, such as sending a Slack message with error details to alert users to problems <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   To link an error workflow to another workflow, go to the settings (three dots in the top right) of the main workflow and select the error workflow to be triggered <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
This setup provides valuable production monitoring <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### 9. Schedule Trigger for Interval-Based Workflows
The **Schedule Trigger** is an underutilized feature that enables workflows to trigger on a defined interval (e.g., daily, hourly, or at custom times) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. This is essential for tasks that cannot be event-based but need to run consistently at set times <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Examples include:
*   Generating reports <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   Fetching overdue tasks from a project management tool like Asana and sending a Slack alert <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

### 10. n8n Workflow Library for Templates and Inspiration
The **n8n Workflow Library** on the n8n website offers over a thousand workflow templates <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Users can search by applications, keywords, or specific nodes (e.g., "Superbase vector store node") to find examples <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. These templates can be viewed in the n8n workflow viewer widget and serve as excellent starting points for building custom workflows <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This resource is highly valuable for anyone looking to get started or seeking inspiration for [[creating_custom_ai_workflows_with_n8n|creating custom AI workflows with n8n]] <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.