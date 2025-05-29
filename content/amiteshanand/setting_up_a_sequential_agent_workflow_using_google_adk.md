---
title: Setting up a sequential agent workflow using Google ADK
videoId: ji_hECcyTjs
---

From: [[amiteshanand]] <br/> 

This article details the process of setting up a sequential agent workflow using [[Agent Development Kit introduction and usage | Google Agent Development Kit (ADK)]] to create a job finder application. This application allows users to upload their resumes, which are then analyzed to find suitable job listings from platforms like Hacker News and Wellfound. The entire system operates as a multi-agent system, with different agents performing specific tasks in a defined sequence <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## Core Application Overview

The demo application is a resume analyzer and job finder that uses Google ADK, Mistral OCR, and LinkUp <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Its workflow involves:
1.  Extracting resume content from uploaded PDFs <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
2.  Preparing tailored job search queries based on the resume <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  Using the LinkUp API to search for jobs on Hacker News and Wellfound <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
4.  Compiling and formatting job listings relevant to the resume <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Tools and Technologies Used

The [[Building AI agents with Google ADK | agent app]] leverages several key tools:

*   **[[Agent Development Kit introduction and usage | Google Agent Development Kit (ADK)]]**: The primary framework for building the agent application and its sequential workflow <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. It supports integration with various LLM providers via LightLLM <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Mistral OCR**: An LLM-based model used for efficiently reading documents and images, specifically for extracting text from resumes <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Mistral OCR demonstrates high benchmark scores, outperforming other OCR models <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **LinkUp**: A search tool designed for AI applications, enabling the addition of search functionality to LLM-based apps <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a> <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. It allows for both general and "deep search" to pick up better, larger contexts <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Quinn 3 Model**: A recent large language model (LLM) known for its thinking capabilities. The Quinn 34B model is specifically used for the AI processing part of the agent <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. It's accessed via Navius AI Studio, which provides access to various open-source models <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Sequential Agent Workflow Setup

The application is set up using Google Colab for easy demonstration <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a> <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### 1. Installation and Setup
Required libraries include `google-generativeai`, `mi4_m_ocr`, `python-dotenv`, `lightllm`, and `linkup-sdk` <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a> <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. API keys for Navius AI Studio and LinkUp are configured <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. The LLM (Quinn 3) is set up using `lightllm` <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### 2. Defining Tools

*   **OCR Tool (`ocr_tool`)**: Uses the `ml_ocr` library to read PDF resumes. It processes a signed URL to extract plain text content <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **LinkUp Search Tool (`linkup_search_tool`)**: Utilizes the LinkUp API to find jobs. Site restrictions are implemented to search exclusively on Hacker News and Wellfound, although these can be customized <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a> <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. It uses deep search for better accuracy <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

### 3. Defining Sub-Agents
A [[sequential_agent_demo_with_google_adk | sequential agent workflow]] is implemented using four distinct sub-agents <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a> <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>:

*   **OCR Agent (`ocr_agent`)**:
    *   **Purpose**: Extracts text from the uploaded PDF resume.
    *   **Instruction**: "Use the Mistral OCR tool... Extract text from a given PDF file path. Only return the extracted plain text content. Do not include any explanation or commentary. Prefix your response with 'OCR'" <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a> <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

*   **Query Prep Agent (`query_prep_agent`)**:
    *   **Purpose**: Analyzes the OCR output (resume content) to generate up to five precise search queries for job platforms.
    *   **Instruction**: "Analyze the resume content from OCR output... and generate up to five precise search queries. Each search query should focus on a specific job goals, skills, experience or technologies mentioned... Target platform hyperl jobs and well founding list. Format each query as a bullet point prefix response with 'Query Agent'" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. It leverages the Quinn 3 model's thinking capabilities <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

*   **LinkUp Search Agent (`linkup_search_agent`)**:
    *   **Purpose**: Uses the generated search queries to perform job searches via the LinkUp API.
    *   **Instruction**: "Search for job using a link up require API with provided queries using the queries provided in linkup query... To search for job postings, limit the results to jobs from hacker muse and well found only pick most recent and latest job links. Prefix your response with 'Link up search'" <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a> <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Specific prompts are crucial for accurate, up-to-date results <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

*   **Job Filter Agent (`job_filter_agent`)**:
    *   **Purpose**: Compiles and formats a final list of suitable jobs based on the resume content and search results, prioritizing jobs with higher chances of selection.
    *   **Instruction**: "Using the resume content from OCR output... and the search result from link up search result... compile a list of relevant job postings for each job include job title company application link app if applicable if available source hacker news and well... Present the result in a clear easy to read format example number list. Make a priority order based on experience needed in jobs with higher chances to get selected... Prefix your response with 'Job filter'" <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a> <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

### 4. Pipeline and Execution Host Agent
A **Host Agent (`job_finder_agent`)** is defined to orchestrate the sequential flow of these sub-agents <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a> <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This agent defines the `OCR_sequential_agent` workflow, ensuring each sub-agent executes in order: OCR Agent, Query Prep Agent, LinkUp Search Agent, and Job Filter Agent <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a> <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

## Execution and Results

Once the setup is complete, the application prompts the user to upload a PDF resume <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. The workflow then executes:

*   **OCR Agent Output**: Shows the extracted plain text from the resume, including technical skills, education, projects, and achievements <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Query Prep Agent Output**: Displays the five precise search queries generated based on the resume content, demonstrating Quinn 3's "thinking" process <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a> <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
*   **LinkUp Search Agent Output**: Presents job listings found, including active hiring opportunities and links <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. The LinkUp dashboard confirms that five separate searches were performed, corresponding to the five generated queries <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Job Filter Agent Output**: Provides a filtered and prioritized list of relevant jobs, along with notes highlighting alignment with specific projects or skills mentioned in the resume <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a> <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

The output demonstrates the effectiveness of the [[Sequential agent demo with Google ADK | sequential agent workflow]] in automating the job search process by leveraging the strengths of each integrated tool <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

The full code and examples are available in the ADK example repository on GitHub <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.