---
title: Comparison of local and cloudbased AI models
videoId: y6Wh4SpRoao
---

From: [[colemedin]] <br/> 

November 11th, 2024, marked a significant day for AI with the release of Quen 2.5 Coder 32B, an open-source large language model (LLM) that can be run entirely locally <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This model's performance suggests a rapidly [[local_ai_versus_cloud_ai_benefits | diminishing gap between massive closed-source models and local LLMs]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Running models locally means no API costs, making it a highly attractive option for continuous operations <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

## Running Local Large Language Models

To run local LLMs, Ollama is a recommended tool <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. It simplifies pulling and running models from its library <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. For Quen 2.5 Coder 32B, the model can be downloaded using a simple command provided on the Ollama Quen 2.5 Coder page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Hardware Requirements
For optimal performance of the 32 billion parameter model, a minimum of an NVIDIA 3090 graphics card is recommended <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. A single 3090 GPU is sufficient for running this model <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Model Variations and Quantizing
If a machine doesn't meet the requirements for the 32 billion parameter model, other variations like the 7 billion or 14 billion parameter models are available <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

A concept called "quantizing" allows for significantly reducing the size of local LLMs while only slightly impacting performance <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. For example, a Q2 quantized version of the 32 billion parameter model is 12 GB instead of the default 20 GB <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## [[comparison_between_local_and_large_ai_models | Performance Comparison: Local vs. Other LLMs]]

### AutodDev (AI Coding Assistant)
Quen 2.5 Coder 32B demonstrates strong performance as an AI coding assistant using AutodDev, an open-source AI coding tool <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Simple Task:** It can easily create a React chat interface with Tailwind CSS for sending and receiving sample messages <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Complex Task:** It successfully handles additional requirements like UI/UX enhancements, a loading indicator, and a two-second delay for AI responses <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This level of complexity often causes other local LLMs to fail <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Contrast with Code Llama 34B:** Code Llama 34B, a slightly larger model, failed a very basic task, such as installing necessary dependencies, showing that raw size doesn't guarantee superior performance for local models <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Custom AI Agent
Quen 2.5 Coder 32B was tested with a complex AI agent built using LangChain and LangGraph, designed to push the limits of LLMs <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. This agent integrates with various tools:
*   Asana for task management <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>
*   Google Drive for file operations (downloading, uploading, searching) <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
*   Chroma for a local vector database, enabling Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>, [[incorporating_ai_models_and_databases_in_a_local_setup | incorporating AI models and databases in a local setup]] for knowledge base integration <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>

Other local LLMs, including a larger cloud-based model like Llama 3.1 70B from Groq, have struggled with these complex tasks <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

#### Agent Performance with Quen 2.5 Coder 32B:
*   **Asana Integration:** Successfully retrieves project lists and creates tasks with specific parameters (e.g., due dates, project IDs) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **Google Drive and RAG:**
    *   Searches for files in Google Drive <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
    *   Downloads files and adds them to the Chroma knowledge base <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
    *   Answers questions based on the content of the downloaded file using RAG, demonstrating successful knowledge retrieval <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### Comparison Summary
Quen 2.5 Coder 32B demonstrates a significant leap for local LLMs, performing complex coding and multi-tool agent tasks that even larger models like Code Llama 34B and Llama 3.1 70B (cloud-based) fail to accomplish <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

## Cloud Platforms for AI Deployment (Novita AI)
Cloud platforms like Novita AI offer an "all-encompassing AI Cloud platform" for open-source LLMs, providing an alternative or complement to local deployments <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

Key features of Novita AI:
*   **LLM API:** Provides easy access to various LLMs, including standard and unique models for creative tasks <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Serverless Deployment:** Simplifies deployment and management of AI application infrastructure <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **GPU Instances:** Highly configurable GPU instances, supporting up to eight GPUs per instance, which is uncommon on other platforms <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Templates:** Offers templates like [[setting_up_a_local_ai_cloud_stack | Ollama with Open Web UI]] for quick setup, and the ability to create custom templates from any container image <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This means a local package like the bolt.new fork can be [[deploying_local_ai_package_to_cloud_instances | deployed to cloud instances]] <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **OpenAI Compatibility:** Allows for easy integration into existing applications by overriding the base URL, enabling users to swap Novita AI for services like GPT <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

## Conclusion
The advancements in local and open-source AI, particularly with models like Quen 2.5 Coder 32B, are rapidly closing the [[comparing_local_and_cloudbased_large_language_models | gap between powerful cloud-based LLMs]] (like Claude 3.5 Sonnet or GPT) and those that can be run on personal machines for free <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>, <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. This shift makes it practical to run complex AI agents continuously without incurring API costs <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.