---
title: Open source alternatives for AI
videoId: aEOu9P4_2cU
---

From: [[amiteshanand]] <br/> 

The field of AI has seen the emergence of open-source alternatives to proprietary tools, offering accessible and customizable solutions for tasks such as deep research. One notable example is the "Open Deep Think Researcher," an open-source project designed to perform automated research tasks similar to OpenAI's Deep Research tool, but at a significantly lower cost <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. While OpenAI's version can cost around $200 for access, open-source alternatives reduce this expense, potentially to the cost of API key usage <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Existing Open-Source Research Tools

Before the Open Deep Think Researcher, other open-source versions of deep research tools were already available <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Zi's Gina Reader API**: One example seen utilized the Gina Reader API <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Mac's Open Deep Researcher**: Another popular tool, the "Open Deep Researcher" by Mac, gained significant traction with over 2.2k stars <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This tool uses:
    *   SerpAPI for Google searches <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   Gina for extracting webpage content <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   OpenRouter for Large Language Model (LLM) processing, specifically using the Cloud 3.5 model <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Open Deep Think Researcher: A Detailed Look

The "Open Deep Think Researcher" aims to provide the same functionality as its proprietary counterparts, with an emphasis on allowing the AI model more time to "think" and iterate <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Key Components

*   **Core AI Model**: DeepSeek R1 (fast version) is used, which is known for its iterative thinking process <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Inference Provider**: [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebius AI Studio]] (NVS AI Studio) provides the inference for DeepSeek R1 and offers access to various LLM models, embedding, text-to-image, and vision models <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>, <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Search API**: XSearch AI API is used to perform web searches and crawl pages to gather the latest information for the LLM to process <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **User Interface (UI)**: Gradio is used to provide an interface, making the application runnable in a Colab notebook, and it can also be deployed as a Python application <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Research Process

The Open Deep Think Researcher follows a structured approach to generate reports:
1.  **Query Generation**: The AI generates multiple search queries based on the user's input <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
2.  **Iterative Refinement**: It runs multiple iterations to refine and improve the quality of search results <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The maximum recommended iteration limit is 10 to balance thoroughness with processing time <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
3.  **Information Extraction**: Relevant information is identified and extracted from the search results <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This includes evaluating the relevance of web pages and extracting useful content <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
4.  **Final Report Generation**: DeepSeek R1 compiles all collected context and data into a final report, including a conclusion <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### Implementation and Requirements

To run this project, users need NVS API keys and XSearch API keys <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The default model is DeepSeek R1, and NVS AI Studio supports OpenAI formatting for API calls <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

A key optimization for speed involves setting a character limit for the web page content used in evaluation and processing. While the demo uses 200 characters for faster results (approximately 45 seconds) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, the repository suggests potential improvements for larger limits (2,000, 5,000, or 20,000 characters) for more comprehensive results, which would impact API usage and pricing <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Potential Improvements

The project is designed for contributions and further development. Potential improvements include:
*   Allowing users to select different LLM models via [[leveraging_nebas_ai_studio_for_open_source_model_access | NVS AI Studio]] through the Gradio UI <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>, <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   Deploying it as a full-stack Python application using frameworks like Reflex or Streamlit <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   Adding options for configurable content length (2,000, 5,000, or 20,000 words) for search queries and page content, which can impact API usage and pricing <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

By fostering an open-source approach, such projects enable continuous iteration and optimization, making AI research tools more accessible and adaptable <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>, <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.