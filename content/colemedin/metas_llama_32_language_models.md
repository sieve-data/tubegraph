---
title: Metas Llama 32 language models
videoId: E3jO8YLc_CI
---

From: [[colemedin]] <br/> 

Meta recently released their latest suite of large language models, [[using_llama_for_llms | Llama 3.2]], which includes 1 billion, 3 billion, 11 billion, and 90 billion parameter versions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These models are designed to run on a wide range of hardware and support a variety of generative AI use cases <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Benchmarks for [[using_llama_for_llms | Llama 3.2]] are impressive, with the 90 billion parameter version nearing or even exceeding the performance of [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] in some areas <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. A significant advantage is that these models can be downloaded and run locally <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>, marking promising progress for [[working_with_local_large_language_models | local LLMs]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This is particularly beneficial for use cases that require [[benefits_of_hosting_your_own_large_language_models | local LLMs]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Llama 3.2 as an AI Agent

Traditionally, [[working_with_local_large_language_models | local LLMs]] have struggled as AI agents due to their limited ability with function calling (also known as tool calling) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This capability is crucial for LLMs to perform actions beyond generating text, such as sending emails, interacting with Slack, or querying knowledge bases <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The development of a [[working_with_local_large_language_models | local LLM]] that can reliably perform function calls would be a "GameChanger" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Testing and Comparison

A custom-coded AI agent, built with LangChain and LangGraph, was used to test and compare [[using_llama_for_llms | Llama 3.2]]'s (specifically the 90B version) performance as an AI agent against [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The testing process involved starting with simple tool call requests and gradually moving to more complex scenarios <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

> [!WARNING]
> The 1 billion, 3 billion, and 11 billion parameter versions of [[using_llama_for_llms | Llama 3.2]] were found to be unusable for function calling, as they would not invoke tools <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Therefore, only the 90 billion parameter version was used for comparison, as it is the most comparable to [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

#### Test Cases

*   **Asana Integration (Simple Tool Calls):**
    *   Both [[using_llama_for_llms | Llama 3.2]] 90B and [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] successfully listed projects in Asana <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
    *   Both models were able to create tasks in Asana with specified parameters (e.g., project, due date) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>, <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Google Drive Integration (Complex Tool Calls):**
    *   When asked to download a specific file from Google Drive, [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] successfully searched for and downloaded the file, correctly handling the specific search formatting required by the Google Drive API <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    *   [[using_llama_for_llms | Llama 3.2]] 90B, however, failed in this task. It generated an incorrect search query for Google Drive, demonstrating a struggle with complex tool call formatting <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. It requested more information from the user, which should not have been necessary given the prompt <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Retrieval Augmented Generation (RAG) with Local Knowledge Base:**
    *   Both models were tested on their ability to perform RAG tasks using a local Chroma instance <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] could download a document from Google Drive, add it to the knowledge base, and then answer questions based on the document's content all within a single multi-step request <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Although it sometimes downloaded the same file multiple times <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, it ultimately provided the correct answer.
    *   Since [[using_llama_for_llms | Llama 3.2]] 90B failed to download the file from Google Drive, the file path was directly provided <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. [[using_llama_for_llms | Llama 3.2]] 90B successfully added the document to the knowledge base and answered RAG-based questions correctly once the document was in the knowledge base <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

### Conclusion on AI Agent Performance

While [[using_llama_for_llms | Llama 3.2]] marks a significant step forward for [[working_with_local_large_language_models | local LLMs]] in function calling compared to its predecessor, [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | Llama 3.1]] (which was largely unusable for function calling, even the 70B version) <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>, it doesn't quite reach the level of [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT-4o mini]] as a general AI agent at a base level <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>, <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

> [!NOTE]
> Fine-tuning and improving docstrings for tools can significantly enhance an LLM's understanding and performance in function calling, potentially bridging some of the observed gaps <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.