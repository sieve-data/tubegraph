---
title: Using APIs for deep research projects
videoId: aEOu9P4_2cU
---

From: [[amiteshanand]] <br/> 

The "open deep researcher" is an open-source alternative to OpenAI's Deep Research, which costs approximately $200 for access <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Other open-source versions are available, including one from Zilliz that utilizes their Gina reader API <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Another popular version by Mac uses the Surfer API for Google search, Gina for web page content extraction, and OpenRouter for LLM processing, leveraging the Claude 3.5 model <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>, <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Open Deep Think Researcher

The "open deep think researcher" is a similar open-source project designed to perform automated research <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This project uses [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] for its research capabilities <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Core Components and APIs

This research project integrates several APIs:
*   **[[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]]**: Used for the inference of [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] serves as an inference provider with multiple LLM models, including embedding, text-to-image, and vision models <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>, <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. A faster version of [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] is used to optimize result speed <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **XSearch API**: Performs web searches and crawls pages to gather the latest information for the LLM to process <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Research Workflow

The automated research process involves several steps:
1.  **Query Generation**: The AI generates specific search queries based on the user's input <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
2.  **Iterative Refinement**: Multiple iterations are run to refine and improve the quality of search results <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
3.  **Information Extraction**: Relevant information is identified and extracted from the search results <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
4.  **Report Generation**: Finally, [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] generates a comprehensive report using all collected context and data <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

The system evaluates web page relevance using the LLM and extracts useful information before compiling the final report <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>, <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Implementation and Setup

The "open deep think researcher" is demonstrated running in a Colab notebook, using a Gradio UI for the interface <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It can also be deployed as a Python application <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

To run the project, only two API keys are required: [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] API keys and XSearch API keys <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

The project structure includes:
*   `async_research`: Handles the execution of research tasks <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   `nvus_ai`: Used for generating responses <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   `xapi_ai`: For fetching search results <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Gradio: For displaying the UI <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

The default model is [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] supports OpenAI formatting, requiring only a base URL change <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Performance and Customization

For the demo, the system extracts the first 200 characters of web page content and search queries to ensure fast results, completing a search in about 45 seconds <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>, <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. However, users can increase this limit to 2,000, 5,000, or 20,000 characters for more comprehensive results, though this may increase API usage and cost <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

The system allows setting a maximum of 10 iterations for research, as increasing iterations takes longer <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>, <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### Potential Improvements

The project's repository includes a section for potential improvements and contributions <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>, such as:
*   Allowing users to select different LLM models via [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]]'s diverse open-source model offerings <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>, <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   Deploying a full-stack Python application using frameworks like Reflex or Streamlit <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   Adding options for users to specify the character limit for page content (e.g., 2,000, 5,000, or 20,000 words) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

Using open-source solutions like this project can be significantly more cost-effective than proprietary alternatives, potentially costing around $2 for API usage compared to $200 for OpenAI's research service <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>, <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. The open-source nature encourages iteration and optimization <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.