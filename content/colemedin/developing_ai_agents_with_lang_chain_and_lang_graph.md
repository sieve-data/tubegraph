---
title: Developing AI agents with Lang chain and Lang graph
videoId: E3jO8YLc_CI
---

From: [[colemedin]] <br/> 

This article explores the development and testing of AI agents using the [[setting_up_ai_agents_with_python_and_langchain | LangChain]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] frameworks, focusing on their application in building robust and flexible AI agents capable of interacting with various tools and services. The primary goal of such an agent is to evaluate the function-calling capabilities of different Large Language Models (LLMs), specifically comparing Meta's Llama 3.2 90B with GPT-4o mini <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## AI Agent Architecture

A custom-coded AI agent was developed using [[setting_up_ai_agents_with_python_and_langchain | LangChain]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] to facilitate robust and comprehensive testing of LLMs as AI agents <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### User Interface and Interaction

The agent utilizes a Streamlit UI for browser interaction, allowing users to chat with the LLM <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. When a chat message is received, the `Prompt AI` function is called to get a response, which interacts with the [[building_ai_agent_workflows_with_langgraph | LangGraph]] runnable to stream the LLM's output <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Dynamic Model Switching

A key feature of this AI agent is its "model mapping," which allows for easy swapping of different LLM models <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Based on an `llm_model` environment variable, the appropriate chat class from [[setting_up_ai_agents_with_python_and_langchain | LangChain]] is instantiated for models like OpenAI, Anthropic, or Groq, with future support planned for Hugging Face <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This dynamic setup means no code changes are required to switch between different LLM services <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Environment variables are managed in a `.env` file, which includes necessary API keys for various models <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### LangGraph Setup

The core logic of the AI agent is orchestrated through [[building_ai_agent_workflows_with_langgraph | LangGraph]], providing a structured workflow for handling interactions <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

The [[building_ai_agent_workflows_with_langgraph | LangGraph]] setup includes:
*   **Chat Instance**: A chat instance is set up, and all available tools are bound to it <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **State Management**: The graph manages the conversation messages as its state <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Nodes**: There are two primary nodes:
    *   One to call the LLM and get a response <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   Another to invoke any tools the LLM requests <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Router**: A router determines if tool calls are necessary after receiving a response from the LLM <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. If a tool call is requested, it routes to the tool node; otherwise, it routes to the end of the graph, returning the response to the user <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This routing mechanism also handles loops, allowing the LLM to invoke multiple tools sequentially until the user's request is fully addressed <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Runnable Creation**: The `get_runnable` function creates and compiles the graph, defining all edges and nodes with memory, making it ready for use by the Streamlit UI <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Integrated Tools

The AI agent's capabilities are defined by the tools it can access and invoke <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. These tools are imported from separate files and bound to the LLM model <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The tools are categorized by service:

*   **Asana (Task Management)**: Provides functions to create tasks, create projects, and retrieve tasks within a specific project <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Google Drive (File Management)**: Enables searching for files, creating files, downloading files, and searching through folders <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Vector Database Tools (Retrieval Augmented Generation - RAG)**: Utilizes a local Chroma instance for RAG capabilities <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. These tools allow the agent to search for and query documents (performing similarity searches), add documents to the knowledge base, and clear the knowledge base for new tests <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Testing AI Agent Performance

The agent's performance is tested by setting the `llm_model` environment variable to either GPT-4o mini or Llama 3.2 90B <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The testing progresses from simpler tool call requests to more complex scenarios involving multiple sequential tool invocations <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

GPT-4o mini demonstrated strong performance in creating tasks in Asana <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>, downloading files from Google Drive (including formatting complex search queries and using context from previous calls) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>, and integrating documents into the knowledge base for RAG queries <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. It could even handle complex requests requiring it to download, add to the knowledge base, and then answer a question in a single prompt <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. While generally impressive, GPT-4o mini occasionally exhibited unusual behavior, such as downloading the same file multiple times <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

Llama 3.2 90B was tested similarly, though smaller Llama 3.2 models (1B, 3B, 11B) were found to be unusable for function calling <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Llama 3.2 90B successfully performed basic Asana tasks <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. However, it struggled with more complex Google Drive interactions, particularly with formatting search queries, indicating a limitation in its ability to intelligently formulate tool arguments compared to GPT-4o mini <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Despite this, Llama 3.2 90B performed well with RAG operations once given the file path directly, successfully clearing the knowledge base, adding documents, and answering questions based on the retrieved information <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

In conclusion, while Llama 3.2 shows significant progress in function calling compared to its predecessor (Llama 3.1 was largely unusable for this purpose <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>), it does not yet consistently match the performance of GPT-4o mini as an AI agent <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. The [[setting_up_ai_agents_with_python_and_langchain | LangChain]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] framework proves instrumental in systematically evaluating and developing these AI agent capabilities.