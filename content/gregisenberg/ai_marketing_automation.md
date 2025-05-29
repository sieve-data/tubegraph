---
title: AI marketing automation
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

[[AI tools for automating marketing workflows | AI marketing automation]] offers the ability to automate a marketing team with [[use_of_ai_agents_and_workflows_in_marketing | AI agents]], allowing content to be created on autopilot <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This approach aims to create content that genuinely gets likes and comments <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, saving an estimated 10 to 15 hours per week <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Core Principles

The workflow leverages [[ai_agents_and_automation | AI agents and automation]] to streamline content creation, moving from data gathering to automatic publishing <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The primary goal is to enable faster testing of content angles, hooks, and topics, resulting in top-performing content based on extensive context and information <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## LinkedIn Content Automation Workflow

A detailed example of an end-to-end automation workflow for LinkedIn content is provided, which can be adapted for any channel <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### 1. Data Collection and Research
The initial stage focuses on analyzing YouTube and X (formerly Twitter) for relevant topics <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Topic Input**: A keyword (e.g., "inadin") is entered <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Scraping Top Content**: The system scrapes the top 20-30 YouTube videos with high engagement and relevant posts from X accounts related to the topic <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Transcription and Merging**: All scraped YouTube videos are transcribed, and this content, along with X posts, is merged into one large text block for research <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This ensures sufficient context for the Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Tool**: Appify is used for scraping data from various internet platforms like YouTube and X <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### 2. Content Idea Generation
After gathering data, an AI agent, powered by an OpenAI LLM, scans the collected text to find fresh content angles and ideas, avoiding mere replication of researched content <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Prompting**: The LLM is instructed to create actionable content ideas strictly related to marketing, with a short, clear title, a scroll-stopping hook, optimal format suggestions, and a unique angle focused on how marketers can scale efforts using [[using_ai_and_automation_in_marketing | AI and automation]] <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Audience Framing**: Instructions include avoiding technical jargon and tailoring content to the specific audience <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Brand Voice Integration**: The AI also analyzes top-performing X posts to identify the speaker's tone, themes, and brand voice <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### 3. Factual Research and Augmentation
To prevent hallucinations and back up claims, a research agent using Perplexity searches for specific facts, trends, and sources <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Data Points**: It identifies use cases with real stats, industry trends, marketing insights, frameworks, case studies, and popular opinions relevant to workflow automation and AI <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Tool**: Perplexity is used for research, accessed via Open Router, which allows integration of various LLMs through a single node <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. Open Router provides access to models like Perplexity Sonar, OpenAI, and Claude <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### 4. Content Generation
The refined ideas and research data are fed into a LinkedIn content agent.
*   **LLM Choice**: Claude 3.7 Sonnet is preferred for content creation due to its strong writing capabilities <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Context is Key**: Emphasizes that providing ample context and data to Claude yields powerful results, unlike basic prompts that lead to generic output <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Prompting Best Practices**:
    *   **Brand Voice**: Include instructions for authentic expertise, direct communication, confidence, avoiding formality, corporate jargon, and marketing speak <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
    *   **Narrative**: Create narrative-driven posts with actionable insights <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
    *   **Data Usage**: Only use data if relevant and tied to the context <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
    *   **Formatting**: Specify desired output format (title, content) and avoid AI-generated elements like hashtags and excessive M-dashes <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   **Role-Playing**: Frame the LLM as a "LinkedIn content strategist and conversion copywriter" to ensure strong hooks, interest, desire, value, and a clear call to action <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Content Output**: The generated post is placed into a Google Doc <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

### 5. Image Generation
An image for the post is created using the OpenAI image generation model <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. Dynamic prompts can be used based on the post's topic <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. For a more personal touch, users could store personal photos in a Google Drive and have the AI randomly select and attach one <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>.

### 6. Human-in-the-Loop Review
Before publishing, the workflow includes a "human in the loop" step, sending a link to the Google Doc draft to Slack <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. This allows for review and editing <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
*   **Approval**: An "Approve" button in Slack can directly publish the content to LinkedIn <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.

### 7. Automated Publishing
Once approved, the content is automatically published to the desired social platform <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

## Benefits and Outcomes

*   **Time Savings**: Significantly reduces the manual effort in content creation <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Faster Testing**: Enables rapid testing of content angles, hooks, and topics <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Validated Content**: By scraping data from top-performing YouTube videos and X posts, the workflow removes guesswork, increasing the likelihood of creating content that resonates and gets engagement by 10x or 50x <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Reduced Guesswork**: Uses real validation from already performed content to inform new creations <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>.
*   **Iterative Improvement**: Allows users to test multiple posts, refine those that perform well, and delete those that don't <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

## [[tools_for_automating_marketing_tasks | Tools for Automating Marketing Tasks]]

*   **Appify**: A platform for scraping data from various internet sources like Instagram, Amazon, TikTok, YouTube, and X <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **OpenAI**: Used for LLM (Large Language Model) processing for content idea generation and image generation <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Perplexity**: Utilized as a research agent for finding facts, trends, and sources <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Open Router**: Allows access to multiple LLMs (like Perplexity, OpenAI, Claude) through a single API key and node, simplifying integration <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Claude 3.7 Sonnet**: Recommended LLM for content writing due to its strong writing capabilities, especially when provided with rich context <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Google Docs**: Used for outputting and reviewing generated content <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **Slack**: Integrated for the human-in-the-loop review and approval process <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

## Prompting Tips for [[use_of_ai_agents_and_workflows_in_marketing | AI Agents]]

Effective prompting is crucial for optimal AI output:
*   **Know What Questions to Ask**: Understand what information you need the AI to extract or generate <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Know What Good Looks Like**: Provide examples of desired content and use AI to improve your prompts based on these examples <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Provide Rich Context**: Arm the LLM with tons of data from research, top-performing content, and analysis of your own brand voice <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Define Brand Voice/Guidelines**: Clearly specify writing style, tone, and what to avoid (e.g., jargon, excessive formality, AI-specific quirks like M-dashes and hashtags) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Specify Output Format**: Clearly outline the structure and elements desired in the final output (e.g., title, content structure) <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   **Assign a Persona**: Frame the LLM with a specific role, such as a "LinkedIn content strategist and conversion copywriter," to guide its output towards desired outcomes like direct response and clear calls to action <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Business Applications

This workflow serves as an interesting backbone to power various businesses, including consulting businesses, freelancing, and optimizing agency operations <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Workflow Availability

A JSON file containing this complete workflow is available for download at `templates.thevibemarketer.com/greg` <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>. Users can upload it into N8N (or similar automation tools), customize it, and begin experimenting <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. This allows for immediate learning through tinkering and optimizing outputs based on results <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.