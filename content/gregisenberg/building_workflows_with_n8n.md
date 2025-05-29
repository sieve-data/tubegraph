---
title: Building workflows with N8N
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

This article outlines an end-to-end N8N workflow designed to automate content creation and publishing, specifically for platforms like LinkedIn, saving significant time and ensuring content relevance <a class="yt-timestamp" data-t="01:28:09">[01:28:09]</a>. The workflow aims to produce content that receives likes and comments by leveraging data from top-performing posts <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

## Core Benefits
*   **Time Savings**: The workflow can save approximately 10 to 15 hours per week <a class="yt-timestamp" data-t="01:30:45">[01:30:45]</a>.
*   **Faster Testing**: Enables quicker testing of content angles, hooks, and topics <a class="yt-timestamp" data-t="02:08:14">[02:08:14]</a>.
*   **Top-Performing Content**: Generates high-quality content based on extensive context and information <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   **Validated Posts**: Content is validated by scraping and analyzing top-performing posts from platforms like YouTube and X, reducing guesswork <a class="yt-timestamp" data-t="02:08:14">[02:08:14]</a>, <a class="yt-timestamp" data-t="02:11:46">[02:11:46]</a>.

## Workflow Stages

The N8N workflow is color-coded and structured in distinct stages <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. A template (JSON file) for this complete workflow is available for free download to help users get started <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### 1. Data Collection and Research
This initial phase analyzes YouTube and X (formerly Twitter) for relevant topics <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   **Keyword Input**: Users enter a topic keyword into a chat interface <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>, such as "N8N" <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   **Web Scraping**: The workflow uses [[automating_content_creation_with_zapier_and_appify | Appify]] to scrape data <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
    *   It scrapes top YouTube videos related to the topic, identifying 20-30 videos with high engagement <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
    *   It scrapes the user's own X account for posts about workflow automation and AI <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
    *   [[automating_content_creation_with_zapier_and_appify | Appify]] provides open APIs for scraping various internet platforms like Instagram, Amazon, TikTok, YouTube, and X <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **Transcription**: The workflow transcribes content from the scraped YouTube videos <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   **Data Consolidation**: All collected data (transcribed YouTube videos, X posts, hooks, titles) are merged into one large text block for the research phase, ensuring sufficient context for the LLMs <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>. This process mimics what a savvy content creator would do manually, but automates the extensive research <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

### 2. Content Idea Generation
After data collection, a content idea generator agent is used <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.
*   **LLM Integration**: This agent plugs into an OpenAI LLM <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.
*   **Idea Generation**: It scans the large text block of researched content to find fresh, non-replicating content angles and ideas <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>. The AI generates these ideas <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
*   **Prompt Engineering**: The prompt instructs the AI to create actionable content ideas strictly related to marketing, focusing on repurposing insights from the broader topic <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
    *   Desired output format includes a short, clear title, a scroll-stopping hook, optimal content format, and a unique angle for marketers to scale efforts using AI and N8N <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
    *   Instructions also include avoiding technical jargon, tailoring content for a specific audience, and analyzing top-performing X posts for brand voice and themes <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.
    *   Prompts are often improved by using other AI tools like ChatGPT, Manis, or Claude, feeding them an initial prompt and examples of desired content <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>. This highlights the importance of knowing "what questions to ask and what good looks like" <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.

### 3. Deep Research for Content Enhancement
To prevent hallucinations and back claims with data, a research agent is used <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.
*   **Perplexity Integration**: This agent uses Perplexity to find real use cases, statistics, trends, marketing insights, frameworks, case studies, and popular opinions relevant to the marketing angles <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
*   **Multi-LLM Access**: Open Router is a helpful tool that allows access to various LLMs (like Perplexity, OpenAI, Claude) with a single node and a single subscription, simplifying integration <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.

### 4. Content Creation
The generated ideas and research data are merged and fed into a content agent <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>.
*   **LLM Choice**: Claude 3.7 Sonnet is preferred for content creation due to its current best writing capabilities <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>. Claude excels when provided with sufficient context and data <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
*   **Prompting Best Practices**:
    *   **Brand Voice**: Instructions include guidelines for an authentic, confident, straightforward, and direct communication style, avoiding corporate jargon and marketing speak <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
    *   **Narrative Structure**: The prompt instructs the AI to create a narrative-driven post with actionable insights that positively impact business <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>. Data should only be used if relevant <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
    *   **Format Control**: Specific instructions are given to avoid AI habits like excessive hashtags and emojis <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>, and "M dashes" <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>, which can make content feel less authentic <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>. A desired output format (e.g., title, content) is specified <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.
    *   **AI Persona**: The LLM is framed as a "LinkedIn content strategist and conversion copywriter," emphasizing direct response and a journey from a strong hook to a clear call to action <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>.

### 5. Image Generation
*   An image for the post is created using the OpenAI image generation model <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
*   Dynamic prompts can be used based on the post's topic <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. For LinkedIn, it's suggested to use personal photos stored in a Google Drive folder, allowing the workflow to randomly select and attach an image for a more natural feel <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>.

### 6. Human-in-the-Loop and Publishing
*   **Review Mechanism**: The workflow sends a link to the generated Google Doc (containing the draft post) to Slack <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>. This allows for human review and editing before publishing <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.
*   **One-Button Publishing**: Once approved via a button in Slack, the content can be automatically published to the desired social platform (e.g., LinkedIn) <a class="yt-timestamp" data-t="20:16:00">[20:16:00]</a>.

The effectiveness of this workflow is demonstrated by a LinkedIn post generated by the AI passing the "Turing test," with a user commenting on it as a "solid example" <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>.

## Accessing the Workflow Template
A free JSON file containing the complete workflow logic is available to help users upload it into N8N, make it their own, and begin experimenting <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>. This allows for immediate learning by tinkering and optimizing the output based on results <a class="yt-timestamp" data-t="22:55:00">[22:55:00]</a>. The template can be accessed at: `templates.vibemarketer.com/greg` <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>.