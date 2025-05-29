---
title: Introduction to Qwen3 for AI and job search functionality
videoId: ji_hECcyTjs
---

From: [[amiteshanand]] <br/> 

The Qwen3 model, a recent advancement in AI, plays a crucial role as the artificial intelligence component within a demo application designed to help users find jobs <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>, <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This application leverages Qwen3's capabilities for its core AI logic <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

## Qwen3 Model Overview

Qwen3 is presented as a state-of-the-art model known for its "thinking capabilities" <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. It has achieved high benchmark scores, notably being considered the best "thinking model" in the open-source domain at the time of the video, with the Qwen3 235B and 822B models being top performers <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. The Qwen3 series includes various models, such as 32B, 8B, and 14B <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. For the job search application demo, the Qwen3 34B model is specifically utilized <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

## Integration with Nebas AI Studio

Qwen3 models are accessible via [[Nebas AI Studio | Nebas AI Studio]], which provides access to various Qwen3 models, including the 34B, 3B, 14B, and 4B versions <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. The presenter notes that Nebas AI Studio is a cost-effective platform, offering free credits that were used for building the demo application <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## Qwen3's Role in Job Search Functionality

Within the [[Using Agent Development Kit to create a job finder app | Agent Development Kit]]-based job finder application, Qwen3 powers several key agents to facilitate the job search:

### Query Preparation

The "query prep agent" is responsible for analyzing the extracted resume content <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. Qwen3's "thinking capabilities" are leveraged by this agent to generate up to five precise search queries <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>, <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. Each query focuses on specific job goals, skills, experience, or technologies mentioned in the resume, targeting platforms like Hacker News and Wellfound <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. The model's thought process, such as "the user provided the resume content extracted from the PDF. Now they want me to generate up to five precise search queries," is visible during execution <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.

### Job Filtering and Prioritization

The "job filter agent" utilizes Qwen3 to compile and format relevant job postings <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>, <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>. This agent uses both the initial resume content and the search results obtained from the [[Utilizing Linkup for job search results | Linkup]] search tool <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. Qwen3 is instructed to prioritize job roles based on the experience needed, aiming to suggest opportunities with higher chances of selection given the resume's qualifications <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. It can also add notes to explain the alignment of job opportunities with specific projects or skills mentioned in the resume, demonstrating its contextual understanding <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>.

### Workflow Execution

Throughout the sequential agent workflow, Qwen3's internal "thinking" process is often displayed, showing how the model analyzes the task, plans its actions, and processes responses from various tools <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. This transparency highlights its advanced reasoning capabilities as it navigates the job search process <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.