---
title: Using Appify and OpenAI for content generation
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

This workflow details an end-to-end automation process for generating and publishing content on autopilot, specifically demonstrated for LinkedIn. The goal is to save significant time and create high-performing content by leveraging data from existing successful posts and videos <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Core Components and Tools

This content generation system integrates several key AI and automation tools:
*   **NADN (n8n)**: The primary workflow automation platform where the process is built <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Appify**: Used for web scraping data from platforms like YouTube and X (formerly Twitter) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **OpenAI LLMs**: Utilized for generating content ideas and creating images <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Claude 3.7 Sonnet**: Considered the best LLM for content writing as of recording <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Perplexity**: A research agent used to find facts, trends, and validate claims <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Open Router**: Allows access to multiple LLMs (like Perplexity, OpenAI, Claude) through a single node and pricing structure, simplifying integration <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Slack**: Used for the "human-in-the-loop" review step, sending a link to the draft content <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Google Docs**: Where the generated content draft is outputted for review and editing <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **YouTube and X (formerly Twitter)**: Primary data sources for content research <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **LinkedIn**: The target social media platform for automated content publishing <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Workflow Stages

### 1. Data Collection and Research
The process begins by entering a specific topic into a chat interface <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

*   **YouTube Scraping**: Appify scrapes the top 20-30 YouTube videos with high engagement related to the topic. These videos are then transcribed, providing rich content data <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **X (Twitter) Scraping**: Appify also scrapes the user's own X account for posts around relevant topics (e.g., workflow automation and AI) to capture brand voice and themes <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Data Merging**: All scraped and transcribed data is merged into one large text block, forming a comprehensive research base. This emulates the manual research a content creator would perform to understand existing content and identify opportunities <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This automated research saves extensive manual effort <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### 2. Content Idea Generation
An [[using_ai_for_content_generation_and_analysis | AI agent]], powered by an [[automating_content_creation_with_ai | OpenAI]] LLM, analyzes the aggregated text block to find fresh content angles and ideas, avoiding direct replication of researched content <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

*   **Prompting**: The [[prompting_techniques_for_aigenerated_content | prompt]] instructs the AI to generate actionable marketing-related content ideas based on the provided context. It specifies requirements for titles (short, clear), hooks (scroll-stopping), optimal format, and a unique angle (e.g., how marketers can scale efforts using AI and NADN) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Avoiding Jargon**: Instructions are included to avoid excessive technical jargon, tailoring content for a specific audience <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Refining Prompts**: Initial prompts are often refined using other LLMs like ChatGPT, Manis, or Claude by asking them to improve the prompt based on desired outcomes and example content <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 3. Research and Validation
A research agent, using Perplexity (accessed via Open Router), is employed to find specific facts, trends, and sources to back up claims and prevent AI hallucinations <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. This step gathers:
*   Use cases with real statistics <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   Industry trends and insights <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   Marketing-specific use cases and ideas <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   Stats, frameworks, case studies, and popular opinions <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

### 4. Content Creation
The generated ideas and research data are fed into a LinkedIn content agent, which uses Claude 3.7 Sonnet for writing <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

*   **Brand Voice**: The [[prompting_techniques_for_aigenerated_content | prompt]] includes detailed instructions on brand voice (e.g., authentic expertise, direct communication, confident, straightforward, avoiding corporate jargon) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Narrative and Actionability**: The AI is instructed to create narrative-driven posts that provide actionable insights and takeaways for readers <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Formatting and Style**: Specific instructions are given to avoid hashtags and emojis, and to follow a desired output format (e.g., title, content) <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. The AI is also explicitly told to avoid "M-dashes" to make the content feel less AI-generated <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.
*   **Conversion Copywriting**: The AI is framed as a "LinkedIn content strategist and conversion copywriter" to ensure the content leads readers through a journey with a strong hook, builds interest and desire, provides value, and includes a clear call to action <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

### 5. Image Generation
An image is created for the post using the [[aigenerated_assets_for_mobile_app_development | OpenAI image generation model]]. The prompt can be dynamic based on the post topic or simple, such as creating a 3D image communicating an AI system <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Users can also configure it to randomly select personal photos from a Google Drive folder for a more authentic feel <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### 6. Human-in-the-Loop Review
The generated content is sent as a Google Doc link to a Slack channel for review <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. This step allows for human editing and ensures quality before publishing <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

### 7. Automated Publishing
Once the content is approved in Slack (by clicking an "approve" button), it is automatically published to the designated social platform, such as LinkedIn <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.

## Benefits and Outcomes

*   **Content on Autopilot**: The entire process allows for [[automating_content_creation_with_ai | content creation on autopilot]], saving 10-15 hours per week <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
*   **Faster Testing**: Enables rapid testing of content angles, hooks, and topics, leading to more effective content <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Top-Performing Content**: By leveraging a vast amount of contextual data from top-performing content, the system generates high-quality posts that are likely to resonate and get likes and comments <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Validation**: The content is "validated" because it's based on data from existing highly engaged videos and posts, removing much of the guesswork <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Authenticity**: The workflow aims to produce content that passes the "Turing test," feeling authentic and human-written, rather than obviously AI-generated <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
*   **Business Applications**: This workflow can serve as a backbone to power [[monetizing_content_creation_through_ai | consulting or freelancing businesses]], or optimize agency operations <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Accessing the Workflow
A free JSON file containing the complete workflow is available at templates.vibemarketer.com/greg. This allows users to download, upload into NADN, and adapt it for their own content creation needs <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.