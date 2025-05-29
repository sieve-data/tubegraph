---
title: Integration of APIs for web searching and processing
videoId: aEOu9P4_2cU
---

From: [[amiteshanand]] <br/> 

This article explores the creation of an open-source deep researcher, similar to OpenAI's Deep Research, but built using open-source components and accessible APIs <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While OpenAI's version costs around $200 for access <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, this open-source alternative aims to provide similar functionality at a lower cost <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Overview of Open Deep Think Researcher

The "Open Deep Think Researcher" is designed to perform automated research based on user queries <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. It leverages a combination of AI models and search APIs to generate comprehensive reports <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Core Components

The system relies on the following key components:
*   **DeepSeek R1**: Used for the thinking and iteration process of the researcher <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The "fast version" of DeepSeek R1 is used for optimized and faster results <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   [[API and model integration with Nebius AI Studio | Nebius AI Studio]] (NVS AI Studio): Serves as the inference provider for DeepSeek R1 <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. It offers various LLM models, embedding, and vision models <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. [[API integration with nvs AI Studio for model usage | NVS AI Studio]] supports OpenAI formatting, requiring only a change in the base URL for compatibility <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   [[External Tool and Database Integration with Nebius AI and Couchbase | XSearch API]]: Utilized to perform web searches, crawl pages, and retrieve the latest information for processing by the LLM <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Gradio UI**: Provides the user interface for interacting with the application, typically run within a [[Building multiagent systems using Google collab | Colab notebook]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Workflow and Process

The research process within the Open Deep Think Researcher follows these steps:
1.  **Query Generation**: The AI generates initial search queries based on the user's input <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The system prompts the LLM to generate exactly four distinct search queries formatted as a Python list of strings <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
2.  **Information Retrieval**: The [[External Tool and Database Integration with Nebius AI and Couchbase | XSearch API]] performs the search and content retrieval <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
3.  **Relevance Evaluation**: The LLM (via [[API and model integration with Nebius AI Studio | NVS]]) evaluates the relevance of web pages to the query <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It responds with "yes" if the page is useful or "no" if it's not, without extra text <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
4.  **Information Extraction**: Useful information is identified and extracted from the search results <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
5.  **Iteration and Refinement**: Multiple iterations are run to refine and improve the quality of results <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The maximum number of iterations is limited to 10 to manage processing time <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
6.  **Final Report Generation**: DeepSeek R1 generates a final report using all collected context and data <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Implementation and Setup

To run this project, users need:
*   [[API and model integration with Nebius AI Studio | NVS API]] keys <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   [[External Tool and Database Integration with Nebius AI and Couchbase | XSearch API]] keys <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

The application is typically run within a [[Building multiagent systems using Google collab | Google Colab notebook]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The Gradio UI provides an interactive interface within the notebook or via a public URL <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

#### Project Structure and Code

The project's code structure includes:
*   `async_research`: Handles the execution of research <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   [[API and model integration with Nebius AI Studio | NVS]] (`nvus_async`): Generates responses and research queries based on UI input <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   [[External Tool and Database Integration with Nebius AI and Couchbase | XSearch API]]: Fetches search results <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   LLM-based evaluation and content extraction: [[API and model integration with Nebius AI Studio | NVS]] is used to evaluate web page relevance and extract meaningful content <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   Gradio: Used for displaying the interface and results <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Demonstration Example

In a demonstration, a query like "What happened around the world yesterday, February 18th, 2025?" was submitted with two iterations <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. The system displayed intermediate step logs, showing the extraction of information using XSearch, content processing, and usefulness evaluations for various links (e.g., Wikipedia, YouTube, Reuters) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

The final report included sections on global events, such as Middle East tensions, airline incidents (Delta Airlines crash), and geopolitical talks (US talks in Saudi Arabia) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. It also provided a conclusion <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Customization and Potential Improvements

The current demo uses a character limit of 200 for web page content and search queries for speed <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. However, users can modify this to 2,000, 5,000, or 20,000 characters for more comprehensive results, which might affect API usage and pricing <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

Potential improvements include:
*   **LLM Model Selection**: Allow users to choose any LLM model available via [[API and model integration with Nebius AI Studio | NVS Studio]] through the Gradio UI <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Deployment as Full-Stack App**: Deploy as a full-stack Python application using frameworks like Reflex or Streamlit <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Content Length Options**: Implement options in the UI to select desired content extraction length (e.g., 200, 2000, 5000, 20000 characters) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

This open-source approach offers a cost-effective alternative to proprietary deep research tools, allowing for community contributions and further optimization <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.