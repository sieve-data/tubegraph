---
title: Function calling capabilities in AI agents
videoId: E3jO8YLc_CI
---

From: [[colemedin]] <br/> 

Meta recently released their Llama 3.2 suite of large language models, including 1 billion, 3 billion, 11 billion, and 90 billion parameter versions, which can run on a wide range of hardware for various generative AI use cases <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The benchmarks for Llama 3.2 are impressive, with the 90 billion parameter version reportedly achieving performance comparable to, and in some ways exceeding, GPT-4o mini <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This progress for local large language models (LLMs) is particularly promising for use cases requiring local deployment <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## The Importance of Function Calling for AI Agents

Traditionally, local LLMs have not performed well as [[defining_ai_agents | AI agents]] due to their limitations with [[function_calling_in_large_language_models | function calling]], also known as tool calling <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. [[function_calling_in_large_language_models | Function calling]] enables LLMs to perform actions beyond just generating text, such as sending emails, interacting with Slack, or querying a knowledge base <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The ability for local LLMs to reliably perform [[function_calling_in_large_language_models | function calling]] would be a significant game-changer <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This article details a test comparing Llama 3.2 90B's capabilities as an [[defining_ai_agents | AI agent]] against GPT-4o mini, particularly focusing on their [[function_calling_in_large_language_models | function calling]] performance <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Experimental Setup: A Custom AI Agent

A custom-coded [[understanding_ai_agent_frameworks | AI agent]] was developed using LangChain and LangGraph to test various LLMs <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This robust implementation allows for easy swapping of different models <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The agent interacts with the user through a Streamlit UI in the browser <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The core of the agent's functionality lies in its ability to dynamically instantiate the correct chat class from LangChain (e.g., OpenAI, Anthropic, Groq) based on an environment variable, removing the need to change code when switching between services <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

The LangGraph setup is designed to manage conversation messages and includes two main nodes: one to call the LLM for a response and another to invoke any tools the LLM requests <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. A router determines whether a tool call is needed, directing the flow accordingly, and can handle multiple tool invocations in a loop until the user's request is fulfilled <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Implemented Tools

The [[building_ai_agents | AI agent]] integrates several tools categorized by service <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>:
*   **Asana**: For task management, including functions to create tasks, create projects, and retrieve tasks within a project <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Google Drive**: For file management, allowing searching, creating, and downloading files, as well as searching through folders <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Vector Database**: For Retrieval Augmented Generation (RAG), using a local Chroma instance. This includes tools to search for documents, query documents (perform similarity search), add documents to the knowledge base from a file path, and clear the knowledge base <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Performance of GPT-4o mini as an AI Agent

GPT-4o mini was initially tested with a series of progressively complex tool call requests <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

*   **Simple Asana Queries**: It successfully listed all projects in Asana and created a task in a specified project, correctly defining parameters like due date <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Google Drive Interaction**: GPT-4o mini was able to search for a specific meeting notes file, download it, and provide the local file path <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. It intelligently used context from previous tool calls to execute the next action (e.g., using the ID from the search to download the file) <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **RAG Integration**: After downloading, it successfully added the document to its knowledge base and then answered questions about the document's content using RAG <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **Multi-step Complex Request**: When asked a question about a document not yet downloaded or in the knowledge base, GPT-4o mini intelligently recognized it needed to first download the file from Google Drive, then add it to the knowledge base, and finally query it with RAG to answer the question <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. While it exhibited a minor oddity of downloading the same file multiple times, it ultimately provided the correct answer <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

Overall, GPT-4o mini demonstrated very strong performance as an [[defining_ai_agents | AI agent]], especially with complex multi-step tool interactions <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

## Performance of Llama 3.2 90B as an AI Agent

The testing then shifted to Llama 3.2 90B, as other Llama 3.2 models (1B, 3B, 11B) were found to be unusable for [[function_calling_in_large_language_models | function calling]] <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

*   **Simple Asana Queries**: Llama 3.2 90B matched GPT-4o mini's performance in listing Asana projects and creating tasks, indicating its capability for basic tool calls <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Google Drive Interaction**: When asked to download a meeting notes file, Llama 3.2 90B failed to correctly format the search query required by the Google Drive API. It needed more specific information about the file name, which the model should have inferred <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. This highlights a significant weakness compared to GPT-4o mini in handling more complex tool parameters <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **RAG Integration**: Although it struggled with Google Drive, Llama 3.2 90B successfully cleared the knowledge base and then added a document when given the direct file path <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. It then accurately answered questions based on the added document using RAG, demonstrating its capability for retrieval-augmented generation when the input path is provided <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

## Conclusion

Llama 3.2 90B represents a significant step forward for [[function_calling_in_large_language_models | function calling]] in local LLMs compared to Llama 3.1, which was largely unusable for this purpose <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. However, it does not yet reach the level of GPT-4o mini's performance as an [[defining_ai_agents | AI agent]], particularly in handling more complex or nuanced tool interactions like Google Drive searches <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

While GPT-4o mini currently surpasses Llama 3.2 90B at a base level, there is potential for improvement in Llama 3.2 through techniques like refining tool docstrings or fine-tuning the model <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. The progress in [[function_calling_in_large_language_models | function calling]] for local LLMs remains an exciting development <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.