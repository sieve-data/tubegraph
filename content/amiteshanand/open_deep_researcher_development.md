---
title: Open Deep Researcher development
videoId: aEOu9P4_2cU
---

From: [[amiteshanand]] <br/> 

The Open Deep Researcher is an open-source alternative to OpenAI's Deep Research tool, which costs around $200 for access <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This project aims to provide similar deep research capabilities using open-source models and APIs <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Inspiration and Comparison

Several open-source versions of deep researchers are available <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   One version was developed by Ziyi, using their Gina reader API <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   A popular "Open Deep Researcher" by "Mac" uses Sur API for Google search, Gina for web page content extraction, and OpenRouter for LLM processing, specifically a Claude 3.5 model <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

The introduced Open Deep Researcher, also called "Open Deep Think Researcher," focuses on enabling the model to "think for more minutes or seconds" <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Key Technologies

The Open Deep Researcher leverages several components for its functionality:
*   **LLM (Large Language Model):** [[DeepSeek V3 and R1 for Technical Content Evaluation | DeepSeek R1]] (specifically the fast version) is used for core processing <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This model takes time to think and iterate <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Inference Provider:** [[Leveraging Nebas AI Studio for Open Source Model Access | Nebas AI Studio]] provides the inference for [[DeepSeek V3 and R1 for Technical Content Evaluation | DeepSeek R1]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. [[Leveraging Nebas AI Studio for Open Source Model Access | Nebas AI Studio]] supports OpenAI formatting, requiring only a change in the base URL for configuration <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Search and Crawling:** XSearch API (specifically `xapi`) is used to perform web searches, crawl pages, and retrieve the latest information for LLM processing <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a> <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **User Interface:** Gradio UI provides the interactive interface for the application <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## How it Works

The research process is automated through several steps:
1.  **Query Input:** A user inputs a research query <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
2.  **Query Generation:** The AI (DeepSeek R1 via Nebas AI Studio) generates up to four distinct search queries to gather comprehensive information <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
3.  **Search and Iteration:** XSearch API performs searches, and the system runs multiple iterations (up to 10 maximum) to refine and improve result quality <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:02:57">[00:02:58]</a>.
4.  **Content Evaluation and Extraction:** The LLM evaluates the relevance of web pages to the query and extracts useful information from the search results <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a> <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. A prompt guides the LLM to respond with "yes" or "no" if a page is useful <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
5.  **Final Report Generation:** [[DeepSeek V3 and R1 for Technical Content Evaluation | DeepSeek R1]] compiles all collected context and data to generate a final report <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Technical Implementation

The application can be run in a Colab notebook and potentially deployed as Python apps with further improvements <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Requirements:** To run the project, users need NVS API keys and XSearch API keys <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Setup:** Packages like `xapi`, `openai` (for [[Leveraging Nebas AI Studio for Open Source Model Access | Nebas AI Studio]]), and `gradio` are installed <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Character Limits:** For the demo, only the first 200 characters of web page content are processed to save time and increase speed <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a> <a class="yt-timestamp" data-t="00:09:39">[00:09:41]</a>. This allows for faster results, such as generating a report in about 45 seconds <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. In contrast, the original OpenAI Deep Researcher allows for 2,000 characters or more <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Example Output

When a query like "what happened around the world yesterday" (February 18, 2025) is submitted with two iterations, the system generates intermediate step logs <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   It generates initial search queries such as "Global events on February 18th, 2025" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   It aggregates unique links (e.g., 29 in the first iteration, 36 in the second) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a> <a class="yt-timestamp" data-t="00:07:20">[00:07:22]</a>.
*   It evaluates page usefulness (e.g., Wikipedia pages might be useful, YouTube videos might not be) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   The final report includes details on global events like Middle East tensions, airline incidents, and geopolitical talks, similar to Google search results for the given date <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The report also includes a conclusion <a class="yt-timestamp" data-t="00:08:00">[00:08:02]</a>.

## Potential Improvements and [[Open source contributions | Open Source Contributions]]

The repository includes a section for potential improvements, encouraging [[Open source contributions | open source contributions]] <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a> <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **LLM Model Selection:** Allow users to select different LLM models available via [[Leveraging Nebas AI Studio for Open Source Model Access | Nebas AI Studio]] through the Gradio UI <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Full-Stack Deployment:** Deploy the application as a full-stack Python app using frameworks like Reflex.io or Streamlit <a class="yt-timestamp" data-t="00:10:03">[00:10:05]</a>.
*   **Variable Content Extraction:** Provide options for processing different character limits for web page content (e.g., 2,000, 5,000, or 20,000 words) based on user preference and API key usage/pricing <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Optimization:** Further [[Optimizing AI research tools | optimizing AI research tools]] for speed and efficiency through prompt changes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

This open-source approach offers a cost-effective alternative, potentially costing dollars for API usage compared to $200 for proprietary solutions <a class="yt-timestamp" data-t="00:10:20">[00:10:22]</a>.