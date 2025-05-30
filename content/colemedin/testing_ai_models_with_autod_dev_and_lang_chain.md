---
title: Testing AI models with autod Dev and Lang chain
videoId: y6Wh4SpRoao
---

From: [[colemedin]] <br/> 

The release of Quen 2.5 Coder 32B on November 11, 2024, marked a significant day for AI, particularly for open-source large language models (LLMs) <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This model has shown "insane" results in initial testing <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Quen 2.5 Coder 32B can be run entirely locally, offering significant advantages by eliminating API costs <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Quen 2.5 Coder 32B Overview

Quen 2.5 Coder 32B is a new version of an open-source large language model <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Its performance has been described as "that good" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This model excels in various tasks, including coding and AI agent interactions <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Setup and Hardware Requirements for Local LLMs

The recommended way to use local large language models is with Olama <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Users can download Olama from `olama.com` <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. To pull and run Quen 2.5 Coder 32B, a specific command is available on Olama's Quen 2.5 Coder page <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

Hardware recommendations for running the 32 billion parameter model include at least an Nvidia 3090 graphics card <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. The 32 billion parameter model can run on a single 3090 card <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

For users without high-end machines, other variations like the 7 billion parameter model or the 14 billion parameter model (Quen 2.5 Coder 14B) are good options <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Quantizing Models
Quantizing is a technique for local large language models that significantly reduces model size while minimally impacting performance <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. For example, a Q2 quantizing of the 32 billion parameter model reduces its size from 20 GB to 12 GB <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Testing with Autod Dev

[[testing_and_deploying_aiassisted_code_projects | Autod Dev]], specifically the `bolt.new` fork, is one of the best open-source AI coding assistants available <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Quen 2.5 Coder 32B was tested with Autod Dev using Olama <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Initial Test: React Chat Interface
The first test involved prompting Autod Dev to create a React chat interface with Tailwind CSS, allowing users to send a message and receive a sample message back <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Quen 2.5 Coder 32B successfully completed this basic task <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Advanced Test: Iterative Improvements
The next prompt added more complex requirements, including UI/UX specifications and functional elements, such as an AI agent responding with a sample message after a two-second delay with a loading indicator <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This iteration of the chat interface was also successfully completed by Quen 2.5 Coder 32B, including the loading indicator and sample message <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. This level of complexity often causes other local LLMs to fail <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Comparison with Code Llama 34B
Code Llama 34B, a larger model than Quen 2.5 Coder 32B, was tested with the same initial basic prompt <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Code Llama 34B failed to run the `npm run dev` command because it did not install Vite or perform the initial `npm install`, resulting in no preview <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This highlights the superior performance of Quen 2.5 Coder 32B, which can handle more complex coding tasks locally <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Testing with an AI Agent (LangChain/LangGraph)

Quen 2.5 Coder 32B was also tested with a custom-built AI agent designed to push the limits of LLMs <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This agent uses a Streamlit frontend and a [[setting_up_ai_agents_with_python_and_langchain | LangChain]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] backend <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. It integrates with various tools for diverse functionalities:
*   **Asana:** For task management <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Google Drive:** For file downloading, uploading, and searching <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Chroma:** As a local vector database for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This allows the agent to use Google Drive content as a knowledge base <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

This combination of tools creates a non-trivial agent that often causes local LLMs to struggle <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. For comparison, Llama 3.1 70B from Groq completely failed in previous tests with this agent <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### Agent Testing Scenarios:

1.  **Querying Asana Projects:** The agent successfully used the `get_asana_projects` tool to list existing projects (YouTube, Fitness, Business, Personal, Coding) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
2.  **Creating a Task in Asana:** The agent reasoned about the project ID, due date, and task name to invoke `create_asana_task`, successfully creating a task "build the first billion dollar agent" due by the 18th in the "Coding" project <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
3.  **Google Drive and RAG Integration:**
    *   The agent was prompted to download "meeting notes from 823" and add them to its knowledge base <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    *   Initially, it struggled with the specific date but successfully found and downloaded the file when given a more general prompt ("search for meeting notes") <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
    *   After downloading, it successfully added the file to the knowledge base <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
    *   To test RAG, the agent was asked "what are the action items from the 823 meeting notes?" The agent successfully queried the documents, retrieving the action items (discuss headphones, use AI to get rich, bake 13 cookies, mow the lawn) from the file via the vector database <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

Quen 2.5 Coder 32B performed exceptionally well across all these complex scenarios, where other models like Llama 3.1 70B would have failed <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## Novita AI (Sponsor)

Novita AI is an AI Cloud platform offering an LLM API, serverless deployment for AI applications, and configurable GPU instances (up to eight GPUs) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. It provides templates like Olama with Open Web UI and allows users to create custom templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Novita AI's LLM API includes a unique set of models for creative writing tasks and competitive pricing <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. It is OpenAI compatible, allowing easy integration by overriding the base URL <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

## Conclusion

The world of local and open-source AI is rapidly advancing, with Quen 2.5 Coder 32B being a major contributor to this excitement <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. The ability to run powerful models locally for free makes them practical for agents that need to run constantly without incurring high API costs <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. The performance gap between massive closed-source models (like GPT-4 and Claude 3.5 Sonnet) and local LLMs (like Quen 2.5) is quickly diminishing <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.