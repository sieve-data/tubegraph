---
title: Comparing Llama 32 to GPT 40 mini
videoId: E3jO8YLc_CI
---

From: [[colemedin]] <br/> 

Meta recently released their new suite of large language models, [[metas_llama_32_language_models | Llama 3.2]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These models, available in 1 billion, 3 billion, 11 billion, and 90 billion parameter versions, can run on a wide range of hardware for various generative AI use cases <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The [[benchmark_performance_of_LLMs | benchmarks for Llama 3.2]] are impressive, with the 90 billion parameter version nearing or even surpassing [[utilizing_gpt_models_for_task_automation | GPT-4o mini's performance]] in some areas <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This advancement is particularly significant for local LLMs, especially when use cases require them to run on-premise <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

Historically, local LLMs have not performed well as AI agents because they struggle with function calling, also known as tool calling <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Function calling enables LLMs to perform actions beyond text generation, such as sending emails, interacting with Slack, or querying a knowledge base <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The ability of a local LLM to reliably perform function calling would be a "game-changer" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This article compares [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | Llama 3.2 90B]] against [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] as AI agents, testing their function calling capabilities <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## AI Agent Setup

A custom-coded AI agent was developed using LangChain and LangGraph for robust testing across different LLMs <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The agent features a Streamlit UI for interaction and uses a `model_mapping` to easily swap between various models by setting an environment variable, without requiring code changes <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

The agent's "brain" is set up with LangGraph, managing conversation messages and routing actions between calling the LLM and invoking tools <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This setup allows for continuous loops, enabling the agent to invoke multiple tools sequentially until a user's request is fulfilled <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Available Tools
The AI agent is equipped with several tools, grouped by service <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>:
*   **Asana:** For task management, including creating tasks, creating projects, and getting tasks within a project <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Google Drive:** For file management, such as searching for, creating, and downloading files <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Vector Database (Chroma):** For Retrieval Augmented Generation (RAG) capabilities, allowing the agent to search for, query, add, and clear documents from a local knowledge base <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## [[utilizing_gpt_models_for_task_automation | GPT-4o mini]] Performance
The [[integrating_large_language_models_like_gpt_with_custom_tools | GPT-4o mini]] model was tested first, starting with simpler tool call requests and progressing to more complex scenarios <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Asana Tool Calls
*   **Listing Projects:** Successfully listed all projects in Asana (Coding, Personal, Business, YouTube, Fitness) <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Creating a Task:** Successfully created a task with defined parameters (e.g., "end world hunger with code by Monday" in the "coding" project), including setting the due date and providing a link <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Google Drive Tool Calls
*   **Searching and Downloading Files:** Successfully searched for and downloaded a specific file ("823 meeting notes") from Google Drive, providing the local file path <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. The model correctly formatted the search query for the Google Drive API and used the file ID from the search to initiate the download <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### RAG Tool Calls
*   **Adding Document to Knowledge Base:** Successfully added the downloaded "823 meeting notes" document to the knowledge base <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **Querying Knowledge Base:** Correctly answered questions based on the newly added document's content, such as "What are the action items from the 823 meeting?" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Complex Multi-step Tasks
*   **Download, Add, Query (Implicit):** When asked about "action items from the 825 meeting" without the file being in the knowledge base or downloaded, GPT-4o mini initially stated it only had access to the "823 meeting notes" <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Download, Add, Query (Explicit Prompt):** When prompted with "get it from the drive and do what you need to do to answer my question," GPT-4o mini intelligently performed the necessary steps: downloading the file, adding it to the knowledge base, and then querying it to provide the correct answer <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. The only minor issue observed was the model inexplicably downloading the file multiple times <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

> [!success] GPT-4o mini Summary
> GPT-4o mini demonstrated impressive capabilities as an AI agent, successfully handling simple, complex, and multi-step tool calls across different services. Its ability to implicitly understand and execute a sequence of actions for a single request is particularly noteworthy <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## [[using_llama_for_llms | Llama 3.2]] Performance

Only the [[metas_llama_32_language_models | Llama 3.2 90B]] model was used for testing, as the 1B, 3B, and 11B versions were found to be unusable for function calling <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Asana Tool Calls
*   **Listing Projects:** Successfully listed all Asana projects, matching GPT-4o mini's performance <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Creating a Task:** Successfully created a task with specified parameters (e.g., "create an AI pet startup by Tuesday" in the "coding" project) <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

### Google Drive Tool Calls
*   **Searching and Downloading Files:** Llama 3.2 90B **failed** to properly search for and download the "823 meeting notes" file <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. The model generated an incorrect search query (e.g., `name contains` with no search term), indicating an inability to correctly format the tool's parameters <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. It subsequently requested more information about the file name, despite the prompt being clear <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

### RAG Tool Calls
*   **Clearing Knowledge Base:** Successfully cleared the knowledge base <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.
*   **Adding Document to Knowledge Base (Manual Path):** Since it couldn't download the file, the file path was provided directly. Llama 3.2 90B successfully added the document to the knowledge base <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Querying Knowledge Base:** Correctly answered questions based on the manually added document's content, such as "What are the action items from the 823 meeting?" <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

> [!failure] Llama 3.2 90B Summary
> While Llama 3.2 90B performed well with Asana tasks and RAG queries (when the file path was provided), it demonstrated a significant weakness in handling Google Drive tool calls, specifically failing to format search queries correctly <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. This indicates that it does not yet match GPT-4o mini's proficiency in more complex tool interaction scenarios <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

## Conclusion

[[speed_and_performance_comparison_with_other_llms | In terms of AI agent capabilities]], specifically function calling, [[utilizing_gpt_models_for_task_automation | GPT-4o mini]] still surpasses [[metas_llama_32_language_models | Llama 3.2 90B]] <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. Although [[using_llama_for_llms | Llama 3.2]] is a significant improvement over its predecessor, [[building_a_powerful_chatbot_using_llama_3_1_405b | Llama 3.1]] (where even the 70B version was unusable for function calling) <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>, it still requires more refinement to consistently handle complex tool interactions.

Despite this, the progress in local LLMs like Llama 3.2 for AI agent use cases is promising <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. Further improvements through better docstrings for tools and fine-tuning could potentially bridge the performance gap <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.