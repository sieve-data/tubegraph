---
title: Qwen 25 Coder 32B local AI model
videoId: y6Wh4SpRoao
---

From: [[colemedin]] <br/> 

Qwen 2.5 Coder 32B is an open-source large language model (LLM) that runs entirely locally, distinguishing it as a significant development in the field of AI [00:00:29]. Released on November 11th, 2024, it was described as marking "one of the biggest days for AI this entire year" [00:00:09]. Initial testing of the model yielded "insane" results, sparking significant excitement within the AI space [00:01:02].

## Key Features & Capabilities

Qwen 2.5 Coder 32B offers powerful performance comparable to larger, closed-source models while allowing users to run it for free on their local machines [00:01:32]. It excels in coding tasks and complex [[custom_function_calling_in_local_ai_models | AI agent]] interactions.

## How to Access and Run

The recommended method for using [[working_with_local_large_language_models | local large language models]] like Qwen 2.5 Coder 32B is through Ollama [00:02:00]. Users can download Ollama from ollama.com [00:02:03], then use a specific command from Ollama's Qwen 2.5 Coder page to pull and run the model [00:02:13].

### Model Variations and Hardware Considerations

Beyond the 32 billion parameter (32B) version, Ollama also provides other variations, including a 7 billion parameter (7B) model and a recently released 14 billion parameter (14B) option [00:02:24]. The 14B version is a good alternative for machines that may not meet the higher requirements of the 32B model [00:02:38].

For optimal performance with the 32B model, a minimum of an Nvidia 3090 graphics card is highly recommended [00:02:47]. The model can run on a single 3090 card [00:03:08].

#### Quantization

For systems with less robust hardware, a concept called "quantizing" can be applied to [[working_with_local_large_language_models | local large language models]] [00:03:36]. Quantizing significantly reduces the model's size (e.g., a Q2 quantized 32B model is 12GB instead of 20GB) while only slightly affecting performance [00:03:51]. Quantized options are also available for the 14B parameter models [00:04:03].

## Performance Demonstrations

### [[using_ai_coding_assistance | AI Coding Assistance]] with AutodDev

Qwen 2.5 Coder 32B, when loaded with Ollama and AutodDev (a fork called bolt.new), demonstrated exceptional [[ai_coding_assistants | AI coding assistance]] capabilities [00:04:33].

*   **Simple Task:** The model successfully created a React chat interface with Tailwind CSS, allowing users to send messages and receive sample replies [00:04:45]. It "knock[ed] this out of the park" [00:04:54].
*   **Complex Task:** When prompted with more detailed UI/UX requirements, including an AI agent responding with a sample message after a two-second delay with a loading indicator, Qwen 2.5 Coder 32B handled it proficiently [00:05:12]. This level of task complexity is where other [[working_with_local_large_language_models | local large language models]] often "totally botch" the execution [00:05:32].
*   **[[comparison_between_local_and_large_ai_models | Comparison with Code Llama 34B]]:** In contrast, Code Llama 34B (a larger model) failed to complete even a basic task, specifically failing to install necessary dependencies like Vite, which Qwen 2.5 Coder 32B and other large models like Sonnet consistently handle [00:07:04]. This highlights the superior performance of Qwen 2.5 Coder 32B in coding tasks [00:07:32].

### [[extending_local_ai_infrastructure | AI Agent]] with LangChain and LangGraph

Qwen 2.5 Coder 32B was also tested with a complex [[extending_local_ai_infrastructure | AI agent]] built using LangChain and LangGraph, designed to push the limits of LLMs [00:09:47]. This agent integrates with various tools for task management (Asana), file management (Google Drive for downloading/uploading and searching), and Retrieval Augmented Generation (RAG) using Chroma for a local vector database [00:10:24].

*   **Asana Integration:**
    *   Successfully queried and listed projects in Asana, accurately identifying projects like "YouTube," "Fitness," "Business," "Personal," and "Coding" [00:11:37].
    *   Correctly created a task in the "Coding" project with a specific due date (the 18th), requiring it to reason about the project ID, due date, and task name [00:12:05].
*   **Google Drive & RAG Integration:**
    *   Initial search for "meeting notes from 823" in Google Drive was too specific, leading to a "file not found" result [00:12:48].
    *   When given a more general prompt ("search for meaning notes"), the model correctly identified and downloaded "823 meeting notes" [00:13:09].
    *   Successfully added the downloaded file to its knowledge base (Chroma vector database) [00:13:41].
    *   Answered a question about "action items from the 823 meeting notes" by performing RAG on the vector database (the only way to access the file), accurately extracting the relevant action items [00:13:52].
*   **[[comparison_between_local_and_large_ai_models | Comparison with Llama 3.1 70B]]:** The speaker noted that Llama 3.1 70B from Groq would have "broken a long long time ago" when attempting these complex multi-tool interactions, further emphasizing Qwen 2.5 Coder 32B's advanced capabilities [00:14:41].

## Conclusion

Qwen 2.5 Coder 32B is considered a major reason for the excitement in the world of [[working_with_local_large_language_models | local]] and open-source AI [00:15:14]. Its power allows for the constant running of [[extending_local_ai_infrastructure | AI agents]] without the cost of proprietary API models like Claude 3.5 Sonnet [00:15:27]. The model demonstrates the rapidly diminishing gap between massive closed-source models and [[working_with_local_local_large_language_models | local LLMs]] that can be run for free [00:15:48].