---
title: Integration of Qwen3 model in AI job search
videoId: ji_hECcyTjs
---

From: [[amiteshanand]] <br/> 

The Qwen3 model serves as the core AI component for an agent-based application designed to help users find jobs by analyzing their resumes <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This application leverages the [[integrating_multiple_ai_tools_with_google_adk | Google Agent Development Kit (ADK)]] framework to build a multi-agent system <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>, with Qwen3 powering its analytical and decision-making capabilities <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Qwen3 Capabilities and Benchmarks

Qwen3 is highlighted as a recent model possessing strong thinking capabilities <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. It has demonstrated impressive benchmark scores, particularly in the open-source domain <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Specifically, Qwen3 235B and 822B models are considered top performers <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The series also includes other models like 2B, 8B, and 14B <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. For the job search demo, the Qwen3 34B model was utilized <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Accessing Qwen3 via Nebius AI Studio

Rather than direct API calls, Qwen3 is accessed through [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI Studio]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Nebius AI Studio provides access to various Qwen3 models, including 30B, A3B, and 14B <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This platform was chosen due to its cost-effectiveness and available free credits <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Role in the AI Job Search Agent Workflow

In the sequential agent workflow built with Google ADK, Qwen3's capabilities are integral to several sub-agents <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>:

*   **LLM Definition**: Qwen3 is explicitly defined as the Large Language Model (LLM) for all sub-agents within the system <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Query Preparation Agent**: After the Mistral OCR tool extracts text from the resume, a dedicated "Query Prep Agent" utilizes Qwen3 to analyze the resume content and generate up to five precise job search queries. These queries focus on specific job goals, skills, experience, or technologies mentioned in the resume <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Qwen3's thinking capabilities are crucial for this query generation <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Job Filter Agent**: The "Job Filter Agent" also uses Qwen3 to compile and format job postings. It synthesizes information from the OCR output and search results from the [[linkup_search_tool_functionality_for_job_finding | Linkup search tool]] <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. This agent is instructed to prioritize job listings based on the experience needed, aiming to suggest roles with higher selection chances for the user <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### Evident Thinking Capabilities

During the execution of the agent app, Qwen3's "thinking" process is visible in the output, demonstrating its ability to analyze tasks and plan actions <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. Examples include:
*   Reflecting on the user's request to extract text from a PDF <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   Formulating precise search queries based on the extracted resume content <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
*   Analyzing job search results and filtering them according to the user's resume <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

The integration of Qwen3 ensures the AI job search application can intelligently process resumes, generate targeted search queries, and filter job results effectively, demonstrating the power of [[understanding_ai_agents | AI Agents]] and advanced LLMs.