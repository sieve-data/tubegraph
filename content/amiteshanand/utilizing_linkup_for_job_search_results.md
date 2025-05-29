---
title: Utilizing Linkup for job search results
videoId: ji_hECcyTjs
---

From: [[amiteshanand]] <br/> 

Linkup is a specialized search tool designed to integrate search functionality into Large Language Model (LLM) based applications, making it a valuable asset for AI-powered job search tools <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. It provides extensive documentation to assist developers in its implementation <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Integration in a Job Finder Application

In a demo application built using the [[using_agent_development_kit_to_create_a_job_finder_app | Google Agent Development Kit]], Linkup plays a crucial role in finding job listings <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The application, which processes resumes to find suitable jobs, leverages the [[integration_of_apis_for_web_searching_and_processing | Linkup API]] to search for relevant job postings <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### Setup and Configuration
To incorporate Linkup, the Linkup SDK for Python needs to be installed <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. A dedicated "linkup search tool" is defined within the application, requiring a Linkup API key <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### Search Parameters
The Linkup search tool is configured with specific parameters to refine job searches:
*   **Site Restrictions**: Searches are explicitly limited to trusted job platforms like Hacker News and Wellfound to ensure relevant results <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>, <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>, <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. This restriction can be customized based on user preferences <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Deep Search**: The application utilizes Linkup's "deep search" capability. This feature enables more accurate and context-rich searches, allowing the system to pick up larger and more relevant contexts compared to general searches <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### Agent Workflow Interaction
Linkup is integrated into a sequential agent workflow:
1.  **Query Preparation Agent**: After the [[role_of_ml_ocr_in_resume_processing | ML OCR agent]] extracts text from a resume, a "query prep agent" analyzes the content and generates up to five precise search queries <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. These queries focus on specific job goals, skills, experience, or technologies mentioned in the resume <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This agent leverages [[introduction_to_qwen3_for_ai_and_job_search_functionality | Qwen3's]] thinking capabilities <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
2.  **Linkup Search Agent**: The generated queries are then passed to the Linkup search tool. This agent is specifically instructed to use the "link up deep search" tool to find job postings, limiting results to Hacker News and Wellfound, and prioritizing the most recent job links <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This explicit prompting helps Linkup return higher quality, active job listings <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
3.  **Job Filter Agent**: Finally, the search results from Linkup are combined with the original resume content by a "job filter agent." This agent compiles and formats a list of relevant job postings, including job titles, companies, application links, and sources <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. It also prioritizes jobs based on the likelihood of selection given the resume's experience <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### Performance and Monitoring
The Linkup dashboard allows developers to monitor the search activity, showing multiple search queries being executed (e.g., five searches corresponding to the five generated queries) to ensure comprehensive results <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>, <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.