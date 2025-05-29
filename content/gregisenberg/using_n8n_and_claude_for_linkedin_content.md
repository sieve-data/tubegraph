---
title: Using N8N and Claude for LinkedIn content
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

This article outlines a workflow using AI agents to automate the creation and distribution of content for LinkedIn, aiming to put content creation on autopilot <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The process involves leveraging [[Automating workflows with AI tools like MCP NADN and Claude | AI tools]] like [[Nocode AI tools for workflow automation | N8N]] and Claude to generate high-performing content based on real-time data <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## Key Benefits
*   **Time Saving:** The workflow can save approximately 10 to 15 hours per week by automating content creation and publishing processes <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
*   **Faster Content Testing:** Allows for quicker testing of content angles, hooks, and topics <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   **Top-Performing Content:** Generates content that performs well by incorporating context and information from already successful posts <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   **Validated Social Posts:** Content is based on scraped data from high-engagement YouTube videos and X (formerly Twitter) posts, increasing the likelihood of likes and comments <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a> <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a> <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.
*   **Reduced Guesswork:** Eliminates the need to guess what content will resonate, relying instead on validated data <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.
*   **Business Optimization:** Provides a backbone for powering consulting, freelancing, or agency operations <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>.

## Workflow Stages

The workflow is broken down into distinct, color-coded stages within [[Nocode AI tools for workflow automation | N8N]] to provide actionable steps for building similar automation <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. A complete workflow template (JSON file) is available for download <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a> <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>.

### 1. Research Phase
This stage focuses on gathering extensive data to inform content creation.
*   **Topic Input:** The user inputs a specific topic, such as "inadin" (N8N) <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
*   **Data Scraping:**
    *   The system uses Appify to scrape the top 20-30 videos on YouTube related to the topic, focusing on high engagement <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
    *   It also scrapes posts from X (formerly Twitter) related to the topic and the user's account (e.g., workflow automation and AI) <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
    *   Appify is utilized for its open APIs that allow scraping various platforms like Instagram, Amazon, TikTok, YouTube, and X <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **Transcription and Merging:** The workflow automatically transcribes the scraped YouTube videos <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a> and merges all the collected data (transcribed videos, hooks, titles, X posts) into one large text block <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.
*   **Purpose:** This "research phase" ensures sufficient context is available to feed into Large Language Models (LLMs) in subsequent steps <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>. It mimics the manual research a savvy content creator would do to understand existing content and identify opportunities <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

### 2. Content Idea Generation
After gathering research, an AI agent generates new content ideas.
*   **LLM Integration:** An agent node, connected to an OpenAI LLM, scans the large block of collected text <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.
*   **Idea Generation:** It identifies fresh angles and content ideas, avoiding mere replication of researched content <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **Prompting Details:**
    *   The prompt instructs the AI to create actionable content ideas strictly related to marketing, even if the initial keyword (e.g., "inadin") is broad <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.
    *   Desired output format includes a short and clear title, a "scroll-stopping" hook, optimal content format, and a unique angle (e.g., how marketers can scale using AI and N8N) <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
    *   The AI is instructed to avoid technical jargon and tailor content to the specific audience, even referencing the user's top-performing X posts for brand voice <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.
*   **Prompt Optimization:** The user often refines initial prompts by feeding them into other LLMs like ChatGPT, Manis, or [[Automating workflows with AI tools like MCP NADN and Claude | Claude]] with examples of desired content <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>. This highlights the importance of knowing "what questions to ask and what good looks like" <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.

### 3. Fact and Trend Research
This stage ensures the generated content is accurate and well-supported.
*   **Research Agent:** A research agent utilizes Perplexity to find specific facts, trends, and sources to back up content claims <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
*   **Data Collection:** It gathers real stats, use cases, industry trends, marketing use cases, frameworks, case studies, and popular opinions to enrich the content <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.
*   **Avoiding Hallucination:** This step is crucial to prevent the LLM from generating inaccurate or nonsensical information <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.
*   **OpenRouter Integration:** [[Nocode AI tools for workflow automation | N8N]] uses OpenRouter, which allows access to various LLMs (Perplexity, OpenAI, [[Automating workflows with AI tools like MCP NADN and Claude | Claude]]) through a single node and a single price point <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. This enables selection of the best LLM for each specific task <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.

### 4. Content Creation
The compiled ideas and research are used to generate the final content.
*   **LinkedIn Content Agent:** The merged ideas and research are fed into a LinkedIn content agent, though this can be replicated for any social media channel <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>.
*   **LLM Choice:** [[Automating workflows with AI tools like MCP NADN and Claude | Claude]] 3.7 Sonnet is chosen for content creation, identified as the best writing LLM currently available <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>.
*   **Context is Key:** The effectiveness of Claude is highly dependent on providing it with ample context and data <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
*   **Prompting for Brand Voice and Tone:**
    *   Instructions include writing with authentic expertise, direct communication, confidence, avoiding overly formal or academic tones, and corporate jargon <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
    *   The prompt specifies creating a narrative-driven post with actionable insights and takeaways that positively impact business <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>.
    *   Specific rules like "don't use hashtags" and avoiding common AI tells like excessive M-dashes are included <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a> <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>.
*   **Conversion Focus:** The LLM is framed as a "LinkedIn content strategist and conversion copywriter" to ensure content has a direct response or conversion focus, leading readers through a journey with a strong hook, building interest and desire, providing value, and including a clear call to action <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>.

### 5. Image Generation
An image is created to accompany the post.
*   **OpenAI Image Gen:** The workflow uses the OpenAI image generation model <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
*   **Prompting:** A simple prompt like "create a 3D image communicating an AI system" can be used, though dynamic prompts are possible based on the post topic <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>.
*   **Personalized Images:** It is suggested that using personal photos stored in a Google Drive folder, randomly selected by AI, could make posts feel more natural and less "AI-generated" <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>.

### 6. Human in the Loop & Publishing
This stage allows for review and final publication.
*   **Review in Slack:** The workflow sends a link to the drafted Google Doc in Slack, enabling the user to review and edit the content <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>.
*   **Example Post:** An example post title generated by the workflow is "Three ways to scale your marketing without hiring another team," which includes a personal narrative about automating marketing tasks using N8N <a class="yt-timestamp" data-t="18:55:00">[18:55:00]</a>.
*   **Automated Publishing:** A "trigger" or "approve" button in Slack allows for direct publication to LinkedIn or other social platforms after review <a class="yt-timestamp" data-t="20:16:00">[20:16:00]</a>.

This end-to-end automation allows users to test and refine content rapidly, doubling down on what performs well and adapting it for other channels <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a> <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>. The generated content aims to pass the "Turing test" by appearing authentic and human-written <a class="yt-timestamp" data-t="22:04:00">[22:04:00]</a>.