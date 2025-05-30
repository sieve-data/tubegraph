---
title: Deploying and testing AI agents quickly
videoId: ieLdMih5_V0
---

From: [[colemedin]] <br/> 

When [[creating_a_robust_ai_agent_development_environment | developing AI agents]], there's a spectrum ranging from complex needs requiring custom code to simple use cases or fast proof-of-concepts <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For simpler scenarios or quick validations, it's more efficient to use platforms that save significant time rather than coding from scratch <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Vector Shift: A Platform for Rapid AI Agent Development

Vector Shift is a platform designed to simplify the process of [[building_ai_agents | building]] and [[deploying_and_monitoring_ai_agents | deploying AI agents]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. It functions as a drag-and-drop component workflow builder, focusing heavily on AI <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It enables the creation of powerful, robust, and simple AI agents rapidly <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This platform is ideal for quick proof-of-concepts due to its convenience and speed <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a><a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

To get started with Vector Shift, users can visit their website and utilize the free tier, which allows for the creation of a knowledge base and a workflow <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The platform's dashboard features three main components crucial for rapid development:
*   **Chatbots** Used for integrating the AI agent into a website <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Knowledge** Manages the knowledge base, allowing connections to sources like Google Drive to ingest documents for Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Pipelines** Where workflows are created, including those for AI agents <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Building a RAG AI Agent in Minutes

A RAG AI agent can be [[building_ai_agents | built]] in minutes using Vector Shift:

1.  **Set up Knowledge Base**:
    *   Navigate to the "Knowledge" section <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   Add a new knowledge base, for example, "test KB" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Integrate a document source, such as a Google Drive folder containing Google Docs <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Documents are rapidly added as vectors to the knowledge base <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. The Google Drive integration ensures constant syncing with created, updated, or deleted files in the folder <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
2.  **Create a Pipeline Workflow**:
    *   Go to "Pipelines" and create a new pipeline from scratch <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   **Input Component**: Add an "Input" component (e.g., named "input," type text) <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   **LLM Component**: Drag in an LLM component (e.g., Anthropic's Claude 3.5 Sonnet) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    *   **Prompt Configuration**: Configure the LLM prompt to include variables for both user input and context from the RAG system <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. A system prompt can also be set (e.g., "You are a helpful assistant...") <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   **Knowledge Base Reader**: Add a "Knowledge Base" component, selecting the previously created knowledge base (e.g., "test KB") <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   **Connect Components**:
        *   Connect the "input" to the LLM's prompt and the knowledge base reader's query <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a><a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
        *   Feed the results from the knowledge base reader as "context" to the LLM <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
    *   **Output Component**: Add an "Output" component (e.g., named "output," type text) and connect the LLM's response to it <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

This completes the [[building_ai_agents | building]] of a RAG AI agent in under five minutes <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### Quick Testing and Validation

Before [[deploying_and_monitoring_ai_agents | deploying]] the AI agent, it can be easily tested within Vector Shift:
1.  **Deploy Changes**: Click "Deploy Changes" in the top right <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
2.  **Run Pipeline**: Click "Run Pipeline" <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
3.  **Input Query**: Enter a query that requires access to the knowledge base documents to be answered correctly (e.g., "What are the action items from the 8/23 meeting?") <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
4.  **Review Output**: The agent's response, including retrieval details, is provided quickly <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The runtime for each node is also displayed <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

This process allows for quick validation of the agent's functionality <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Rapid Deployment Options

Once validated, the AI agent can be [[deploying_and_monitoring_ai_agents | deployed]] using Vector Shift's "Publish" option:
1.  **Export Pipeline**: Go to "Export Pipeline" in the top right <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
2.  **Choose Export Type**: Options include:
    *   **Automation** <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>
    *   **Chatbot**: Allows naming the chatbot (e.g., "test chatbot") and creating an assistant that can be messaged and customized <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
    *   **Search** <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
    *   **Form** <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
3.  **Deployment Formats**: The exported chatbot can be made available as:
    *   A direct **URL** <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>
    *   An **API** for integration into custom frontends <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>
    *   Connected to **Slack** for use as a personal assistant <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>

Vector Shift also provides various templates, such as a blog article generator, to help users get started quickly with pre-built workflows <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. These templates can be loaded directly, customized with credentials, and adapted <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. The platform's robustness allows for complex workflows, even using multiple LLMs in a single pipeline <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

Using platforms like Vector Shift is valuable for avoiding "reinventing the wheel" when [[building_ai_agents | building]] and [[deploying_and_monitoring_ai_agents | deploying AI agents]], especially for rapid prototyping or less complex applications <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.