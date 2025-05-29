---
title: Using N Studio and Gradio for AI model inference and UI development
videoId: aEOu9P4_2cU
---

From: [[amiteshanand]] <br/> 

This article explores the creation of an "open deep think researcher" application, an open-source alternative to OpenAI's Deep Research, demonstrating the integration of [[features_of_nebas_ai_studio | NVS AI Studio]] for AI model inference and Gradio for user interface development <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The project aims to provide an automated research tool that generates reports based on user queries <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## NVS AI Studio: An Inference Provider

[[features_of_nebas_ai_studio | NVS AI Studio]] serves as an inference provider, offering a variety of models for different use cases <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
It includes:
*   Multiple Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   Embedding models <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>
*   Speech-to-Image (s2i) models <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>
*   Vision models <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>

For the "open deep think researcher," the DeepSeek R1 fast version model is utilized from [[api_integration_with_nvs_ai_studio_for_model_usage | NVS AI Studio]] for its optimized and faster results in processing and thinking <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. [[features_of_nebas_ai_studio | NVS AI Studio]] also supports OpenAI formatting, simplifying its integration <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Gradio: User Interface Development

Gradio is employed to create a user-friendly interface for the application <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. While the app runs within a Colab notebook for demonstration <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, Gradio allows for deployment as standalone Python applications with further improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The Gradio UI is configured to present a clear interface for inputting queries and viewing results <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Integrating NVS AI Studio and Gradio for Deep Research

The "open deep think researcher" leverages both [[api_integration_with_nvs_ai_studio_for_model_usage | NVS AI Studio]] and Gradio to function:

*   **Inference Engine** The DeepSeek R1 model via [[api_and_model_integration_with_nebius_ai_studio | NVS AI Studio]] performs the core LLM processing and generates the final reports <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Search and Content Extraction** Alongside [[api_integration_with_nvs_ai_studio_for_model_usage | NVS AI Studio]], [[using_thirdparty_tools_in_ai_development | third-party tools]] like Exa Search API are used to perform web searches and crawl pages for information <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **UI Interaction** Gradio provides the web-based interface where users input research queries and set iteration limits <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### How the Researcher Works

The automated research process involves several steps facilitated by this integration:
1.  **Query Generation** The AI model (DeepSeek R1 via [[api_integration_with_nvs_ai_studio_for_model_usage | NVS AI Studio]]) generates distinct search queries based on the user's input <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
2.  **Information Retrieval** Exa Search API fetches search results and content <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
3.  **Content Evaluation** The LLM evaluates the relevance of web pages to the query and extracts useful information <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
4.  **Iteration and Refinement** Multiple iterations are run to refine and improve the quality of results <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
5.  **Report Generation** The AI model compiles all collected context and data into a final research report <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

The process is logged, showing steps like initial query generation, content processing, and usefulness evaluations for each retrieved link <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Setup and Usage

To run the application, users need [[api_integration_with_nvs_ai_studio_for_model_usage | NVS API]] keys and Exa Search API keys <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The application is demonstrated in a Colab notebook, where these keys are configured <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The Gradio UI is then accessible via a public URL or directly within the Colab environment <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Potential Improvements

The project's repository outlines several potential improvements for future contributions:
*   **Model Selection** Allowing users to choose any LLM model available via [[api_integration_with_nvs_ai_studio_for_model_usage | NVS AI Studio]] through the Gradio UI <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Deployment Options** Deploying the application as a full-stack Python app using frameworks like Reflex or Streamlit <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Content Length Control** Adding options for users to adjust the character limit for page content extraction (e.g., 2,000, 5,000, or 20,000 characters), which impacts API usage and pricing <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. The current demo uses a 200-character limit for speed <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

This open-source approach offers a cost-effective and customizable alternative to proprietary deep research tools <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.