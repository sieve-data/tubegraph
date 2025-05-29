---
title: Agent Development Kit introduction and usage
videoId: ji_hECcyTjs
---

From: [[amiteshanand]] <br/> 

The Agent Development Kit (ADK) is a framework from Google designed for [[building_ai_agents_with_Google_ADK | building AI agent applications]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It supports the creation of complex agent workflows, including [[sequential_agent_demo_with_Google_ADK | sequential agent workflows]] <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. The ADK has been previously discussed in detail in other videos <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Key Features of Google ADK
The Google ADK offers several [[features_of_google_agent_development_kit | features]]:
*   **Workflow Building**: It allows users to construct complex workflows for agents <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **LLM Provider Support**: It supports various Large Language Model (LLM) providers through `lightllm` <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **User Interface**: The ADK provides a user interface accessible via `ADK web` at `localhost:8000` when run locally <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

## Implementing an Agent App with Google ADK

A demonstration application, a "Resume Analyzer and Job Finder," showcases the use of Google ADK to create a multi-agent system <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. This app extracts resume content from PDFs, prepares tailored job search queries, and compiles relevant job listings from Hacker News and Wellfound <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Setup and Tools
The setup involves installing necessary libraries and defining tools:
*   **Installation**: The core component `google-agent-development-kit` needs to be installed <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **LLM Integration**: The app uses Cohere's Command R+ (Co:R+ 34B) model via Navius AI Studio for the AI part of the agent <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This is set up through `lightllm` <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **OCR Tool**: For reading resumes, the Mistral OCR (LLM-based model) is defined <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. It processes uploaded PDFs by getting a signed URL and then performing OCR <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Search Tool**: Linkup, a search tool designed for AI apps, is used to add search functionality to LLM-based applications <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. The Linkup search tool is configured with site restrictions to search only Hacker News and Wellfound for jobs <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. It performs a "deep search" for better accuracy and context <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

### Sequential Agent Workflow
The application follows a [[setting_up_a_sequential_agent_workflow_using_Google_ADK | sequential agent workflow]] by defining four sub-agents <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>:

1.  **OCR Agent**:
    *   **Purpose**: Extracts text from PDF using the Mistral OCR tool <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Instructions**: Return only plain text content from the PDF, without explanation, and prefix the response with "OCR" <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   **LLM**: Uses the configured LLM (Co:R+ 34B via Navius AI Studio) <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

2.  **Query Prep Agent**:
    *   **Purpose**: Analyzes the OCR output of the resume and generates up to five precise job search queries <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   **Instructions**: Queries should focus on specific job goals, skills, experience, or technologies mentioned in the resume. Target platforms are Hacker News and Wellfound <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Each query is formatted as a bullet point and prefixed with "Query Agent" <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
    *   **LLM**: Leverages the LLM's thinking capabilities to generate queries <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. The output key is named `linkup_query` <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

3.  **Linkup Search Agent**:
    *   **Purpose**: Uses the Linkup search tool to perform job searches based on the queries provided by the Query Prep Agent <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
    *   **Instructions**: Search for jobs only on Hacker News and Wellfound, limit results to the most recent and latest job links, and prefix the response with "Linkup Search" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

4.  **Job Filter Agent**:
    *   **Purpose**: Compiles and formats a final list of suitable job postings based on the uploaded resume and search results <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
    *   **Instructions**: Use content from the OCR output and Linkup search results. For each job, include title, company, application link (if available), and source (Hacker News or Wellfound) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Present results in a clear, numbered list and prioritize jobs based on experience needed and higher chances of selection <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Prefix the response with "Job Filter" <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Pipeline Execution
A main "host agent," named "Job Finder" and specifically "OCR Sequential Agent," orchestrates the entire workflow <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a> <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. This host agent utilizes the defined sub-agents in a sequence to complete the agentic flow <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. The process involves setting up a session and runner for execution <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Demonstration Walkthrough
During the demo, after uploading a PDF resume:
*   The `OCR Agent` processes the resume, demonstrating Mistral OCR's capability to accurately read and extract text from the document <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   The `Query Prep Agent` generates multiple precise search queries based on the extracted resume content, showcasing the LLM's thinking and analytical abilities <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   The `Linkup Search Agent` then executes these queries, performing multiple searches on Hacker News and Wellfound to find relevant job postings <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   Finally, the `Job Filter Agent` analyzes the search results against the resume, filtering and prioritizing job links based on the resume's experience and skills, adding relevant notes and explanations <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a> <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

This demonstration effectively illustrates [[integrating_multiple_ai_tools_with_Google_ADK | how Google ADK can integrate multiple AI tools]] (Mistral OCR, Linkup, Cohere's Command R+) to create a functional and intelligent multi-agent system <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The code for this demo is available on the ADK example repository <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.