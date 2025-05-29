---
title: AI workflow automation for marketers
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

[[automating_your_marketing_with_ai | Automating your marketing with AI]] with AI agents can enable content creation on autopilot, a concept that was once skeptical but is now achievable <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This approach leverages an end-to-end workflow to produce content that gains likes and comments <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Benefits of [[ai_workflow_automation_with_gum_loop | AI Workflow Automation]]
Implementing an AI workflow for content creation can save approximately 10 to 15 hours per week <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It allows marketers to test content angles, hooks, and topics much faster <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. By providing extensive context and information, the system generates top-performing content, including images, and can even auto-publish <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This removes the guesswork from content creation by validating posts based on past performance <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

## End-to-End Workflow Stages

The workflow is structured in distinct stages to systematically create and publish content:

### 1. Data Collection & Analysis
The process begins by analyzing YouTube and X (formerly Twitter) for relevant topics <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Keyword Input**: A specific keyword or topic is entered into the system <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Scraping**: The system then scrapes top-performing videos on YouTube that have high engagement and actively looks for posts on X related to the topic from a specified account <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This data collection is facilitated by platforms like Appify, which provides APIs for scraping various internet sources <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Transcription**: All identified YouTube videos are watched and transcribed, accumulating content from top videos and X posts <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **Data Consolidation**: All collected data is merged into one large text block, serving as the research phase to provide sufficient context for Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This automated research saves significant time compared to manual efforts <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### 2. Idea Generation
After data collection, an [[ai_agents_in_marketing | AI agent]] (content idea generator) connected to an OpenAI LLM scans the consolidated text block <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Its purpose is to find fresh content angles and ideas that don't merely replicate the researched material <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The AI is specifically prompted to create actionable content ideas strictly related to marketing, with requirements for a short and clear title, a scroll-stopping hook, optimal format, and a unique angle <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### 3. Research & Contextualization
To ensure accuracy and relevance, a research [[ai_agents_in_marketing | AI agent]] (using Perplexity via Open Router) is employed to find facts, trends, and sources to back up claims <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. This step identifies real use cases, statistics, industry trends, frameworks, case studies, and popular opinions, providing a robust data set for content creation <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

### 4. Content Creation
The identified ideas and research data are fed into a specific content agent, such as a LinkedIn content agent <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. Claude 3.7 Sonnet is highlighted as an excellent LLM for writing due to its power when armed with sufficient context and data <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. The AI is given explicit brand voice guidelines (e.g., authentic, direct, confident, avoiding jargon) and instructions for creating narrative-driven posts with actionable insights <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

### 5. Image Generation
An image for the post is generated using the OpenAI image generation model <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. While dynamic prompts are possible, a simple prompt can create a relevant image, such as a 3D image communicating an AI system <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. For more authentic results, storing personal photos in a Google Drive and having the system randomly select one can be implemented <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### 6. Human in the Loop Review
To ensure quality and authenticity, a human in the loop step is included <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. The system sends a link to the drafted content in a Google Doc via Slack <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. This allows for review and editing before final publication <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### 7. Automated Publishing
After review and approval (e.g., by clicking an "Approve" button in Slack), the content can be published directly to the desired social platform <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

## Key Tools and Platforms
*   **[[ai_workflow_automation_with_gum_loop | Inaden]]**: The primary platform for building and executing these workflows <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Appify**: Used for scraping data from various internet sources like YouTube, X, Instagram, or Amazon <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **OpenAI**: Provides LLMs for idea generation and content creation, as well as the image generation model <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Claude 3.7 Sonnet**: Recommended as the best LLM for writing, especially effective when given ample context and data <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Perplexity**: Utilized by the research agent to find facts, trends, and use cases <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Open Router**: Allows access to multiple LLMs (e.g., Perplexity, OpenAI, Claude) through a single node and a unified pricing model <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Slack**: Integrated for the "human in the loop" step, sending drafts for review <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Google Docs**: Where the drafted content is presented for review and editing <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

## Prompt Engineering Best Practices
To optimize [[automating content creation with AI | AI-generated content]], specific prompting techniques are crucial:
*   **Clear Objectives**: Know what questions to ask and what the desired "good" output looks like <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Iterative Improvement**: Use AI to refine and improve existing prompts <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Context and Data**: Provide LLMs with a wealth of data and context (e.g., top-performing content, brand voice analysis) to maximize output quality <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Brand Voice Guidelines**: Define specific brand voice attributes (e.g., authentic expertise, direct, confident, no jargon) to guide the AI's writing style <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Format Specification**: Clearly instruct the AI on the desired output format (e.g., title, content structure) <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   **Role Framing**: Assign a specific role to the LLM (e.g., "LinkedIn content strategist and conversion copywriter") to influence its approach <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Direct Response Principles**: Incorporate direct response or conversion copywriting principles (hook, interest, desire, value, call to action) to ensure engaging and effective content <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Avoid AI Tells**: Explicitly instruct the AI to avoid common stylistic elements that reveal AI authorship, such as excessive hashtags, emojis, or M dashes <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## Getting Started
A JSON file containing this complete workflow logic is available as a free template to help users get started immediately with [[ai_workflow_automation_with_gum_loop | Inaden]] <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. This allows for hands-on experimentation, tinkering, and optimization of the workflow <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.