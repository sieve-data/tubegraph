---
title: Building multiagent systems using Google collab
videoId: ji_hECcyTjs
---

From: [[amiteshanand]] <br/> 

This article outlines how to build a multi-agent system, specifically a job finder application, using [[Google Agent Development Kit | Google Agent Development Kit]] (ADK) within a Google Colab environment <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The application allows users to upload their resume, which is then analyzed to find suitable job postings from Hacker News and Wellfound.com <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Key Tools and Technologies

The [[Applications and Implementation of AI Agents | agent app]] leverages several key technologies:

*   **[[Google Agent Development Kit | Google Agent Development Kit]] (ADK)**: A framework from Google used to build the agent application and orchestrate a sequential agent workflow <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. It supports defining host agents and sub-agents to perform a complete workflow <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Google ADK also provides a UI that can be accessed locally <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Mr. OCR**: An LLM-based model used for reading documents and images efficiently, specifically for extracting text from uploaded resumes (PDFs) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It demonstrates superior benchmark scores for OCR compared to other models, achieving 94.89% overall and 99.0% on a multilingual basis <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The Mr. OCR API is used directly as it is not available via Navius AI Studio <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Linkup**: A search tool designed for AI applications to add search functionality to LLM-based apps <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. It offers extensive documentation for integration <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. The application utilizes Linkup for deep searches to find jobs on Hacker News and Wellfound.com <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Coen 3**: A recent LLM model with strong thinking capabilities, used for the AI core of the agent <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The Coen 3 34B model is specifically employed <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Navius AI Studio**: Provides access to various Coen 3 models (e.g., 30BA, 3B, 14B, 4B) and other open-source models like Mistral <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. It is used as the provider for Coen 3 due to its affordability and available credits <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **LightLLM**: Used for setting up Navius AI Studio within the [[Google Agent Development Kit | Google Agent Development Kit]] as it supports other LLM providers <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Google Colab**: The development environment for setting up and showcasing the application <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

> [00:03:13] The speaker is a co-founder at Studio One, a technical agency providing blogs, content, developer advocacy, and tutorials to companies <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Application Overview: Job Finder App

The "Resume Analyzer and Job Finder" application demonstrates how to use [[Google Agent Development Kit | Google Agent Development Kit]] to create a multi-agent system <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Functionality:
1.  **Resume Content Extraction**: Extracts text from uploaded PDF resumes using Mr. OCR <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
2.  **Job Search Query Preparation**: Analyzes resume content to generate tailored job search queries <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  **Job Search Execution**: Uses the Linkup API to search for jobs on Hacker News and Wellfound <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
4.  **Job Listing Compilation**: Compiles and formats job listings relevant to the resume, powered by Coen 3 34B model via Navius AI Studio <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a> <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
5.  **Prioritization**: Orders the job listings based on experience needed and higher chances of selection <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Multi-Agent System Architecture

The application is built using a [[Sequential Agent Workflows | sequential agent workflow]] within [[Google Agent Development Kit | Google Agent Development Kit]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a> <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. It comprises one host agent and four sub-agents:

### Host Agent
*   **`job_finder` (named `OCR_sequential_agent`)**: Orchestrates the entire workflow by sequentially calling the sub-agents <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Sub-Agents
1.  **OCR Agent (`OCR_agent`)**:
    *   **Purpose**: Extracts plain text from the uploaded PDF resume <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Tool Used**: Mr. OCR tool <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   **Instruction**: "Use the Mr. OCR tool... Extract text from a given PDF file path only return the extracted plain text content. Do not include any explanation or commentary. Prefix your response with OCR." <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
    *   **LLM**: Coen 3 (via Navius AI Studio) <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

2.  **Query Preparation Agent (`query_prep_agent`)**:
    *   **Purpose**: Analyzes the OCR output (resume content) and generates up to five precise job search queries <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   **Instruction**: "Analyze the resume content from OCR output... and generate up to five precise search queries. Each search query should focus on a specific job goals, skills, experience or technologies mentioned. Target platform hyperl jobs and well founding list. Format each query as a bullet point prefix response with query agent." <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
    *   **LLM**: Coen 3 (using its thinking capabilities) <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
    *   **Output Key**: `linkup_query` <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

3.  **Linkup Search Agent (`linkup_search_agent`)**:
    *   **Purpose**: Performs job searches using the Linkup API based on the queries provided by the `query_prep_agent` <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
    *   **Tool Used**: Linkup deep search tool <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   **Instruction**: "Search for job using a link up require API with provided queries using the queries provided in linkup query... Limit the results to jobs from hacker muse and well found only pick most recent and latest job links. Prefix your response with link up search." <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
    *   **Site Restrictions**: Explicitly limited to `yc.com` (Hacker News) and `wellfound.com` to ensure relevant job sources <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

4.  **Job Filter Agent (`job_filter_agent`)**:
    *   **Purpose**: Compiles, formats, and prioritizes a final list of suitable jobs based on the resume content and search results <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
    *   **Instruction**: "Using the resume content from OCR output... and the search result from link up search result... compile a list of relevant job postings for each job include job title company application link app if applicable if available source hacker news and well... Present the result in a clear easy to read format example number list. Make a priority order based on experience needed in jobs with higher chances to get selected." <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   **Output Prefix**: `job filter` <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## Implementation Details

The implementation steps within Google Colab involve:

1.  **Installation**: Installing necessary libraries such as [[Google Agent Development Kit | Google Agent Development Kit]], Mr. OCR, `python-dotenv`, `lightllm`, and Linkup SDK <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  **Library Imports**: Running required libraries for Linkup and [[Google Agent Development Kit | Google Agent Development Kit]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
3.  **API Key Setup**: Configuring API keys for Mr. OCR, Linkup, and Navius AI Studio <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
4.  **LLM Setup**: Defining the LLM (Coen 3 via Navius AI Studio) using LightLLM <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
5.  **Tool Definition**:
    *   **OCR Tool**: Defined to read PDFs by first getting a signed URL and then processing the OCR <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   **Linkup Search Tool**: Defined with site restrictions (`yc.com`, `wellfound.com`) and set to perform deep searches <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
6.  **Sub-Agent Definition**: Each of the four sub-agents (OCR, Query Preparation, Linkup Search, Job Filter) is defined with its specific role, LLM, and instructions <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
7.  **Host Agent and Pipeline Execution**: The host agent (`job_finder` / `OCR_sequential_agent`) is defined to orchestrate the sequential flow of the sub-agents. A session and runner are set up for execution <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a> <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
8.  **Main Function**: A main function provides the option to upload a PDF file and generates formatted output <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

## Results and Observations

Upon execution, the [[Types and Features of AI Agents | agent app]] demonstrates a clear workflow:

*   **Agent Thinking**: The Coen 3 model actively shows its "thinking" process, explaining its steps and reasoning (e.g., "The user asked me to extract text from PDF... I use the run Mr. OCR tool for that response came back...") <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Resume Extraction**: The Mr. OCR tool successfully extracts detailed information from the resume, including technical skills, education, and project achievements <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **Query Generation**: The query preparation agent generates multiple precise search queries (up to five, as instructed) based on the extracted resume content <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   **Job Search**: The Linkup search agent performs multiple searches based on these queries, retrieving job listings from the specified platforms <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. The Linkup dashboard confirms five distinct searches were performed, correlating with the five generated queries <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Job Filtering and Prioritization**: The job filter agent compiles a list of relevant jobs, providing details like job title, company, application link, and source. It also adds notes, prioritizing jobs with higher chances of selection and aligning them with specific projects or skills mentioned in the resume (e.g., medical imaging expertise, demand forecast project) <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a> <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

This demonstration highlights the effectiveness of a multi-agent system in automating complex tasks like job searching by breaking them down into sequential, specialized agent roles.

## Additional Resources

The full Google Colab notebook for this application will be available on the speaker's [[Google Agent Development Kit | ADK]] example repository on GitHub <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. This repository also includes other [[Building AI Agents with Google ADK | agent app]] examples, such as email agents, multi-tool search agents, and other sequential agents <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.