---
title: End to end workflow for content creation and publishing
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

This article details an end-to-end workflow designed to automate content creation and publishing, leveraging [[ai_tools_for_content_creation_and_marketing | AI tools]] and agents to produce high-performing content on autopilot <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The process aims to save content creators significant time, potentially 10 to 15 hours per week <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, by automating tasks from research to publishing <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

This workflow is particularly useful for platforms like LinkedIn, where consistent content creation can be time-consuming <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The primary benefit is the ability to rapidly test content angles, hooks, and topics, resulting in top-performing content based on extensive context and information <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. It even generates images and can auto-post <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Workflow Stages

The workflow is structured into color-coded stages, offering actionable tips for building similar processes <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The entire workflow template is available as a JSON file for download, allowing users to upload it into Inaden and customize it <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.

### 1. Research Phase: Analyzing YouTube and X

This initial phase focuses on gathering data around a specific niche or topic <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
1.  **Topic Input**: Users enter a topic keyword into a chat interface <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Data Scraping**: The system uses Appify to scrape the internet <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>:
    *   **YouTube**: Scrapes the top 20-30 videos with high engagement related to the topic <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   **X (formerly Twitter)**: Scrapes posts from the user's account related to workflow automation and AI <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
3.  **Transcription and Merging**: The system watches and transcribes all identified YouTube videos <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. All scraped data (YouTube transcripts, titles, hooks, X posts) are merged into one large text block, forming a comprehensive research base <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

This automated research saves immense time compared to manual efforts <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. It's akin to how a savvy content creator would manually research what's performing well and identify opportunities <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

### 2. Idea Generation: Content Idea Generator Agent

After the research phase, the large text block is fed into a content idea generator agent, which connects to an OpenAI LLM <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Fresh Angles**: This agent scans the research data to find fresh content angles and ideas, avoiding mere replication of existing content <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The goal is to use the research as inspiration to generate unique ideas <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Prompting for Specificity**: The agent is prompted to create actionable content ideas strictly related to marketing <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. For example, if the keyword is "Inaden," it will extract ideas for marketing applications rather than general automation <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Desired Output Format**: Instructions include desired characteristics for the output <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>:
    *   Short, clear title <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>
    *   Scroll-stopping hook <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>
    *   Optimal content format suggestion <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>
    *   Unique angle focusing on how marketers can scale using AI and Inaden <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Audience-Specific Framing**: The AI is instructed to avoid technical jargon and focus on content relevant to the target audience <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. It also analyzes the user's top-performing X posts to match brand voice and themes <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### 3. Fact-Checking and Augmentation: Research Agent

To ensure claims are backed by data and prevent AI hallucinations <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>, a research agent is used.
*   **Tool**: This agent uses Perplexity to find real stats, trends, insights, marketing use cases, and case studies <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Data Points**: It identifies factual data such as:
    *   Real use cases with stats <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>
    *   Trends and insights <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
    *   Industry marketing use cases <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>
    *   Frameworks or case studies <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>
    *   Popular opinions <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>
*   **LLM Access**: Open Router is used to access various LLMs (like Perplexity, OpenAI, Claude) through a single node and subscription, simplifying integration <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

This step generates a powerful dataset to create the right type of content for the audience <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### 4. Content Creation: LinkedIn Content Agent

The merged ideas and research data are fed into a content agent designed for a specific channel, such as LinkedIn <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Tool**: Claude 3.7 Sonnet is chosen as the LLM for its superior writing capabilities <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. Its power is maximized when given ample context and data <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   **Prompting Tips**:
    *   **Brand Voice**: Includes specific guidelines to ensure authentic expertise, direct communication, confidence, and avoidance of overly formal or corporate jargon <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. These guidelines are refined through trial and error <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
    *   **Narrative-Driven Posts**: Instructions to create narrative-driven posts that offer actionable insights and positive business impact <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. Data is only used if relevant <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
    *   **Formatting**: Explicitly tells the AI to avoid common AI habits like excessive hashtags and emojis <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>, and specifies desired output format (title, content, etc.) <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
    *   **Role-Playing**: Frames the LLM as a "LinkedIn content strategist and conversion copywriter" to guide its output towards direct response and a clear customer journey (hook, interest, desire, value, call to action) <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
    *   **Avoiding AI tells**: Specifically instructs to avoid "M dashes" as they are a giveaway for AI-generated content <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

### 5. Image Generation

The workflow also includes an OpenAI image generation model to create a complementary image for the post <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. While dynamic prompts are possible, a simple prompt is used to create a 3D image communicating an AI system <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

A future enhancement could involve storing personal photos in Google Drive and having the AI randomly select one to attach, making the post feel more authentic and less AI-generated <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

### 6. Human-in-the-Loop Review

Recognizing that AI isn't always perfect for direct publishing <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>, a human review step is integrated.
*   **Slack Integration**: The workflow sends a link to the drafted Google Doc in a Slack channel <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **Editing**: Users can open the Google Doc, review the content, and make any necessary edits to ensure authenticity and quality <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Example Post**: An example LinkedIn post generated by the workflow demonstrates its capability, featuring a personal narrative hook and actionable insights related to automating marketing tasks with Inaden <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

### 7. Publishing

Once reviewed and approved, the content can be published with a single click.
*   **One-Button Publish**: A "publish" or "approve" button in Slack allows direct posting to the chosen social platform, such as LinkedIn <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
*   **Validated Content**: The key advantage is that these are "validated social posts" <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. Because the content is generated based on scraped data from top-performing YouTube videos and X posts, the likelihood of it resonating with the audience is significantly higher <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. This removes guesswork and allows for quick testing and refinement <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

## Benefits and Outcomes

*   **Time Savings**: Saves 10-15 hours per week <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Rapid Testing**: Allows for faster testing of content angles, hooks, and topics <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **High-Performing Content**: Generates top-performing content by leveraging extensive research and data <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Reduced Guesswork**: Removes the guesswork from content creation by using data from already validated posts <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Business Leverage**: This workflow can serve as a backbone to power a consulting business, freelancing business, or optimize agency operations <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. It can be used for [[creating_and_marketing_content_for_startup_ideas | creating and marketing content for startup ideas]] by finding things that are already working <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Prompting Tips for AI

*   **Know what questions to ask**: Clearly define your objectives <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Know what good looks like**: Provide examples of desired content outputs to guide the AI <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Use AI to improve your prompts**: Start with a baseline prompt and use another AI to refine it for better results <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Provide ample context**: Feed the model with tons of data from research to maximize its output quality <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Define brand voice and guidelines**: Implement guardrails to prevent "fluff" and ensure authenticity <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Specify format and unwanted elements**: Clearly state desired output structure and instruct AI to avoid certain patterns (e.g., hashtags, M dashes) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **Role-play for specific styles**: Frame the LLM with a specific role (e.g., "conversion copywriter") to guide its writing style <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Availability of Workflow Template

The complete Inaden workflow, including all prompts and templates, is freely available for download <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a> <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. Users can upload this JSON file into Inaden to begin experimenting and learning about [[ai_powered_content_automation | AI-powered content automation]] <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. The best way to understand these [[systems_and_routines_for_creative_content_production_and_audience_engagement | systems and routines for creative content production and audience engagement]] is by playing with them, tinkering, and optimizing based on the output data <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

The workflow has been shown to pass the Turing test, with users unable to distinguish its AI origin <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.