---
title: Open Deep Researcher and its opensource version
videoId: aEOu9P4_2cU
---

From: [[amiteshanand]] <br/> 

The "Open Deep Researcher" is an open-source alternative to OpenAI's "Deep Research" tool, which costs approximately $200 for access <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Several open-source versions have emerged, including one from Ziyi using their Gina Reader API <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, and a popular one by Mac that uses SerpAPI for Google search, Gina for web page content extraction, and OpenRouter with Claude 3.5 for LLM processing <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Introducing "Open Deep Think Researcher"

An advanced open-source version, named "Open Deep Think Researcher," focuses on enabling the AI to "think for more minutes or seconds" <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This version utilizes [[using_deepseek_v3_and_r1_models | DeepSeek R1]] for its core research capabilities <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, leveraging its iterative thinking process <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Key Technologies

*   **LLM Inference:** [[using_deepseek_v3_and_r1_models | DeepSeek R1]] (specifically, the faster version via NVS Studio) for processing and report generation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. NVS Studio serves as an inference provider for various LLM models, including embedding, text-to-image, and vision models <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Search and Data Extraction:** XSearch API (XS API) is used to perform web searches, crawl pages, and gather the latest information for the LLM <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **User Interface:** Gradio UI provides the interface for the application, which runs in a Colab notebook <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### [[steps_and_processes_involved_in_creating_automated_research_reports | Steps and Processes Involved in Creating Automated Research Reports]]

The "Open Deep Think Researcher" follows a structured approach to generate automated research reports:
1.  **Query Generation:** The AI generates specific queries to search for information <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
2.  **Iterative Refinement:** Multiple iterations are run to refine and enhance the quality of search results <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
3.  **Information Extraction:** Relevant information is identified and extracted from the search results <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
4.  **Final Report Generation:** [[using_deepseek_v3_and_r1_models | DeepSeek R1]] compiles all collected context and data into a comprehensive final report <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Running the Application

To run the "Open Deep Think Researcher," users need two API keys:
*   NVS API key (for NVS Studio) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
*   XS API key (for XSearch API) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>

The application can be deployed as a Python app or run in a Colab notebook <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

#### Demonstration Example

In a demonstration, a query like "what happened around the world yesterday, 18th February 2025" was submitted <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. The system then performed the following:
*   Generated initial search queries, e.g., "Global events on February 18th, 2025" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   Ran two iterations, aggregating 29 unique links in the first iteration and 36 in the second <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   Evaluated the usefulness of web pages (e.g., Wikipedia page usefulness, YouTube content usefulness, Reuters usefulness) <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>, <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>, <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   Produced a final report titled "Global Events Report: February 18, 2025," detailing events like Middle East tensions, airline incidents (Delta), and geopolitical talks (US in Saudi Arabia) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

#### Code Structure and Prompts

The project uses `xapi` for XSearch, `openai` for NVS AI Studio, and `gradio` for the UI <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. NVS Studio supports OpenAI formatting, requiring only a change in the base URL <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

Key prompts include:
*   **Search Query Generation:** "You are an expert research assistant. Generate exactly four distinct search queries that will help gather complete information about this topic. Format your response as a Python list of strings." <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>
*   **Page Relevance Evaluation:** "Respond with exact one word: 'yes' if the page useful or 'no' if it's not. Do not include any extra text." <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>

The application initially processes the first 200 characters of web page content and search queries for speed, completing a report in about 45 seconds <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. However, it can be configured to process up to 2,000, 5,000, or 20,000 characters for more detailed reports, which would increase API usage and cost <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## [[potential_improvements_and_further_developments_for_the_open_deep_researcher | Potential Improvements and Further Developments for the Open Deep Researcher]]

The repository includes a section for [[potential_improvements_and_further_developments_for_the_open_deep_researcher | potential improvements and further developments for the Open Deep Researcher]] where users can contribute <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. These include:
*   **LLM Model Options:** Allowing users to select different LLM models via NVS Studio (which supports many open-source models) through the Gradio UI <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Full-Stack Deployment:** Deploying the application as a full-stack Python app using frameworks like Reflex or Streamlit <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Content Length Configuration:** Providing options for processing 2,000, 5,000, or 20,000 characters of web page content, depending on user preference and API cost considerations <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

This open-source project offers a cost-effective alternative to commercial AI research tools, enabling further iteration and optimization by the community <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. [[open_source_contributions | Open source contributions]] are encouraged to enhance its features and performance <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.