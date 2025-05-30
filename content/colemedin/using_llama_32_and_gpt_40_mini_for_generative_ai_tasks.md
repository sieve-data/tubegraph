---
title: Using Llama 32 and GPT 40 mini for generative AI tasks
videoId: E3jO8YLc_CI
---

From: [[colemedin]] <br/> 

Recently, Meta released its latest suite of [[metas_llama_32_language_models | Llama 3.2]] large language models, including 1 billion, 3 billion, 11 billion, and 90 billion parameter versions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These models can be run on a wide range of hardware for various generative AI use cases <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Benchmarks for [[metas_llama_32_language_models | Llama 3.2]] are impressive, with the 90 billion parameter version performing comparably to [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]], even surpassing it in some aspects <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This is notable as [[metas_llama_32_language_models | Llama 3.2]] can be downloaded and run locally <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

The progress in [[strategies_for_scaling_ai_with_local_llms | local LLMs]] is promising, particularly for use cases with local requirements <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Historically, [[strategies_for_scaling_ai_with_local_llms | local LLMs]] have struggled as [[utilizing_gpt_models_for_task_automation | AI agents]] due to their performance with function calling (also known as tool calling) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Function calling enables LLMs to perform actions beyond text generation, such as sending emails, interacting with Slack, or using a knowledge base <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The ability for [[strategies_for_scaling_ai_with_local_llms | local LLMs]] to reliably perform function calling would be a "game-changer" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Testing Setup

To assess the function calling capabilities of [[metas_llama_32_language_models | Llama 3.2]] as an [[utilizing_gpt_models_for_task_automation | AI agent]], it was compared against [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. A custom-coded [[utilizing_gpt_models_for_task_automation | AI agent]] was developed using LangChain and LangGraph for this purpose <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This robust implementation allows for easy swapping of different models <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### AI Agent Implementation

The [[utilizing_gpt_models_for_task_automation | AI agent]]'s interface is built with [[developing_ai_tools_with_streamlit_and_gpt | Streamlit]], enabling interaction with the LLM in a browser <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The core logic involves a `Prompt AI` function that interacts with a LangGraph runnable to stream responses from the LLM <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

Key features of the implementation:
*   **Model Mapping**: Dynamically instantiates the correct chat class from LangChain based on an environment variable, supporting OpenAI, Anthropic, and Groq models, with future support for Hugging Face <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This setup allows for switching between services without changing code <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **LangGraph**: Manages conversational messages as state and has two main nodes: one to call the LLM for a response, and another to invoke any tools the LLM requests <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Router**: Determines if tool calls are needed after an LLM response; if so, it routes to the tool node; otherwise, it returns the response <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This router also handles loops, allowing the [[utilizing_gpt_models_for_task_automation | AI agent]] to invoke multiple tools sequentially until a user request is completed <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Integrated Tools

The [[utilizing_gpt_models_for_task_automation | AI agent]] binds several tools into its model to enable various actions <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. These tools are organized by service:
*   **Asana (Task Management)**: Functions include creating tasks, creating projects, and getting tasks within a project <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Google Drive (File Management)**: Supports searching for files, creating files, and downloading files <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Vector Database (RAG)**: Utilizes a local Chroma instance for RAG capabilities, including searching and querying documents (similarity search), adding documents to the knowledge base, and clearing it <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Performance Comparison: GPT-4o mini vs. Llama 3.2 90B

The same set of prompts was used for both [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] and [[metas_llama_32_language_models | Llama 3.2]] 90B to test their capabilities as [[utilizing_gpt_models_for_task_automation | AI agents]].

### GPT-4o mini Performance

[[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] demonstrated impressive performance across various tool-calling tasks:
*   **Simple Tool Call**: Successfully listed all projects in Asana <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Defining Parameters**: Created a task in Asana's "coding" project with a due date, accurately defining necessary parameters <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Multi-Step Tool Calls (Google Drive)**: Successfully searched for a file ("823 meeting notes") in Google Drive, then downloaded it, and provided the local path <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. It correctly formatted the search query for the Google Drive API and used the context from the search to perform the download <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **RAG Integration**:
    *   Added the downloaded document to its knowledge base <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
    *   Successfully answered questions using RAG, extracting "action items" from the meeting notes after they were added to the knowledge base <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Complex Multi-Step Task**: When asked for "action items" from a meeting document not in its knowledge base or downloaded locally, [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] intelligently understood it needed to:
    1.  Search Google Drive for the file.
    2.  Download the file.
    3.  Add the document to its knowledge base.
    4.  Query the knowledge base to answer the question <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    This complex sequence was largely successful, though it did oddly download the file multiple times <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

Overall, [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] performed very well as an [[utilizing_gpt_models_for_task_automation | AI agent]] <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

### Llama 3.2 90B Performance

Other [[building_a_powerful_chatbot_using_llama_3_1_405b | Llama 3.2]] models (1B, 3B, 11B) were found to be unusable for function calling, as they would not invoke tools <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Therefore, only the 90B version was tested for comparison with [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

[[metas_llama_32_language_models | Llama 3.2]] 90B's performance:
*   **Simple Tool Call**: Successfully listed projects in Asana, matching [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]]'s performance <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Defining Parameters**: Created a task in Asana with parameters, also matching [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Google Drive Interaction (Failure)**: Failed to download meeting notes from Google Drive. It generated an incorrect search query, lacking an actual search term within the `name contains` parameter <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. Despite attempts to self-correct, it ultimately failed to perform the task, indicating a significant limitation compared to [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **RAG Integration (Conditional Success)**:
    *   Successfully cleared the knowledge base <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
    *   When given the file path directly (bypassing the Google Drive search issue), [[metas_llama_32_language_models | Llama 3.2]] 90B successfully added the document to the knowledge base <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
    *   It then accurately answered RAG questions based on the added document <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

## Conclusion

[[metas_llama_32_language_models | Llama 3.2]] 90B is a significant step forward for [[strategies_for_scaling_ai_with_local_llms | local LLMs]] as [[utilizing_gpt_models_for_task_automation | AI agents]] <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. While [[building_a_powerful_chatbot_using_llama_3_1_405b | Llama 3.1]] models (even the 70B version) were generally unusable for function calling, [[metas_llama_32_language_models | Llama 3.2]] shows much improved capabilities <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

However, based on these tests, [[comparing_llama_32_to_gpt_40_mini | GPT-4o mini]] still surpasses [[metas_llama_32_language_models | Llama 3.2]] 90B in overall performance as an [[utilizing_gpt_models_for_task_automation | AI agent]], particularly with more complex, multi-step tool interactions like those involving Google Drive <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. For use cases solely involving RAG or simpler tool calls, [[metas_llama_32_language_models | Llama 3.2]] 90B could be a viable option <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. Further improvements could potentially be achieved through fine-tuning and optimizing tool docstrings <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. The ongoing development of [[open_source_ai_code_generators | open-source models]] for [[utilizing_gpt_models_for_task_automation | AI agents]] remains an exciting prospect <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.