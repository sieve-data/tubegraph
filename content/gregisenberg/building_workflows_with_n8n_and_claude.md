---
title: Building workflows with N8N and Claude
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

This article details an [[ai_workflow_automation | AI workflow automation]] system built using N8N, designed to automate content creation and publishing, particularly for platforms like LinkedIn <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>. The workflow aims to save significant time, potentially 10 to 15 hours per week, by automating the entire process from research to publication <a class="yt-timestamp" data-t="01:30:32">[01:30:32]</a>.

The system was developed by Mr. Vibe Marketing and provides a comprehensive, end-to-end automation solution for [[content_creation_and_seo_with_claude | content creation]] <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. It's pitched as a way to run a business on autopilot <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a> and could serve as an "interesting backbone" for a consulting or freelancing business, or for optimizing agency operations <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.

## Workflow Overview

The core idea is to create content on autopilot that still garners engagement <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>. The workflow leverages various AI models and tools to ensure the generated content is high-performing and relevant, based on existing successful posts <a class="yt-timestamp" data-t="02:24:26">[02:24:26]</a>. It allows users to rapidly test content angles, hooks, and topics <a class="yt-timestamp" data-t="02:09:08">[02:09:08]</a>.

The process is structured in several stages:
1.  **Data Collection/Research:** Analyzing platforms like YouTube and X (formerly Twitter) for trending topics and engaged content <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
2.  **Content Idea Generation:** Using LLMs to generate fresh content angles inspired by the gathered data <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.
3.  **Deep Research:** Gathering facts, trends, and sources to back up content claims <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.
4.  **Content Creation:** Crafting the actual post using a powerful LLM <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
5.  **Image Generation:** Creating an accompanying image for the post <a class="yt-timestamp" data-t="17:37:00">[17:37:00]</a>.
6.  **Human-in-the-Loop Review:** Allowing for human editing and approval before publishing <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.
7.  **Automated Publishing:** Posting the content directly to the chosen platform <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>.

## Key Components and Stages

### 1. Data Collection and Research
The workflow begins by taking a user-defined keyword or topic <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
*   **YouTube and X Scraping:** The system scrapes top-performing videos from YouTube and high-engagement posts from X related to the input topic <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. It also looks at the user's own X account for posts related to workflow automation and AI to inform brand voice <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **Appify Integration:** [[Nocode automation tools | Nocode automation tools]] like Appify are used to access APIs for scraping data from platforms like YouTube and X <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
*   **Transcription:** The scraped YouTube videos are automatically transcribed, and this content is merged with X posts into one large text block for the research phase <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. This step mimics what a savvy content creator would do manually to understand existing content and identify opportunities <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

### 2. Content Idea Generation
*   **OpenAI LLM Integration:** The merged text block is fed into an OpenAI LLM, which acts as a content idea generator <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.
*   **Prompting for Fresh Angles:** The prompt instructs the LLM to find fresh content ideas and angles that don't just replicate the researched material <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **Specific Requirements:** The AI is instructed to generate ideas with specific outputs: short and clear titles, scroll-stopping hooks, optimal content formats, and unique angles relevant to marketing <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. It's also guided to avoid technical jargon and focus on the target audience <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### 3. Deep Research
*   **Perplexity Integration:** A research agent using Perplexity is employed to find specific facts, trends, and real stats to back up content claims and prevent AI hallucinations <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>. This includes identifying marketing use cases, industry insights, and popular opinions <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
*   **Open Router for LLM Access:** Open Router is used to access various LLMs (like Perplexity, OpenAI, and Claude) from a single node, simplifying integration and offering cost efficiency <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.

### 4. Content Creation
*   **Claude 3.7 Sonnet for Writing:** The combined data from idea generation and deep research is fed into a LinkedIn content agent, which specifically uses Claude 3.7 Sonnet, noted as the "best writing LLM" at the time of recording <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>. Claude excels when provided with sufficient context and data <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
*   **Brand Voice Guidelines:** Detailed prompting includes brand voice guidelines to ensure authentic, direct, confident, and straightforward communication, avoiding corporate jargon, marketing speak, hashtags, and emojis <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
*   **Conversion Copywriting Focus:** The LLM is framed as a "LinkedIn content strategist and conversion copywriter" to ensure narrative-driven posts with strong hooks, building interest and desire, providing actionable value, and including clear calls to action <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>.

### 5. Image Generation
*   **OpenAI Image Gen Model:** The workflow includes a step to create an image for the post using OpenAI's image generation model <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>. While dynamic prompts based on topic are possible, a simple prompt for a 3D image communicating an AI system is used for demonstration <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>.
*   **Personalized Images (Future Enhancement):** The idea of storing personal photos in a Google Drive and having the workflow randomly select one to pair with content was suggested to make posts feel more natural and less "AI" <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>.

### 6. Human-in-the-Loop Review
*   **Slack Integration:** The generated content (and image) is sent as a Google Doc link to a Slack channel <a class="yt-timestamp" data-t="18:27:00">[18:27:00]</a>. This allows for human review and editing before publication <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.
*   **Approval Button:** An "approve" button within Slack triggers the final automated publishing step <a class="yt-timestamp" data-t="20:16:00">[20:16:00]</a>.

### 7. Automated Publishing
*   With a single button click, the fully formatted and approved content can be published directly to the chosen social platform <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>.

## Benefits of the Workflow

*   **Time Savings:** Automates manual research and content creation, saving 10-15 hours per week <a class="yt-timestamp" data-t="01:30:32">[01:30:32]</a>.
*   **Validated Content:** By scraping top-performing content, the workflow ensures the generated posts are highly relevant and likely to resonate with the audience, removing guesswork <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.
*   **Faster Iteration:** Enables rapid testing of different content angles and topics <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **High-Quality Output:** Leveraging powerful LLMs like Claude 3.7 with extensive context leads to "top performing content" <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
*   **Authenticity:** Prompting techniques and human review help maintain an authentic voice that passes the Turing test <a class="yt-timestamp" data-t="22:07:00">[22:07:00]</a>.

## Tips for Building Workflows

*   **Use the Best LLM for Each Task:** Employ different LLMs for specific tasks (e.g., Perplexity for research, Claude for writing) <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
*   **Provide Sufficient Context:** To get the most out of AI models, feed them tons of data and context <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>.
*   **Know What Questions to Ask and What Good Looks Like:** Have a baseline prompt and use AI to improve it, providing examples of desired content <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.
*   **Iterate and Optimize:** Experiment with the workflow, tinker with settings, observe the output, and optimize based on data <a class="yt-timestamp" data-t="22:57:00">[22:57:00]</a>.
*   **Human-in-the-Loop:** Include steps for human review, especially for initial deployment, as AI is not always ready for direct publishing <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.

## Accessing the Workflow Template

A JSON file containing the complete N8N workflow is available for free. Users can download it and upload it into their N8N instance to get a starting template for [[automating_workflows_using_ai | automating workflows using AI]] <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>. This template allows users to begin learning and experimenting with [[building_simple_and_powerful_workflows | building simple and powerful workflows]] immediately <a class="yt-timestamp" data-t="22:57:00">[22:57:00]</a>. The template can be accessed at `templates.thevibemarketer.com/greg` <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>. This provides a practical starting point for [[building_an_ai_startup_workflow | building an AI startup workflow]] or enhancing existing operations.