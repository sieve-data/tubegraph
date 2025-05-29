---
title: Generating content with AI tools
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

## Overview of AI-Powered Content Automation

The concept of automating marketing teams with AI agents to achieve content on autopilot is becoming a reality <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A specific "NADN workflow" is designed to create content that effectively drives likes and comments <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This workflow offers an end-to-end automation process, potentially saving 10 to 15 hours per week <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. It's particularly useful for platforms like LinkedIn, especially if manual content creation is disliked <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The primary outcome of [[generating_content_with_ai_tools | utilizing AI for content generation]] is the ability to rapidly test various content angles, hooks, and topics <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Instead of getting subpar results from direct use of tools like Claude or ChatGPT, this method gathers extensive context and information to produce top-performing content, including automatically generating images and posting <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. While AI can automate posting, it's often recommended to test content first, similar to how one might test tweets on a secret account before full publication <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The workflow includes a step for editing content before it goes live <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Workflow Stages

The content generation workflow is broken down into several color-coded stages for clarity <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. A template for this workflow is available for download, allowing users to upload it into NADN and customize it <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

#### 1. Research Phase: Analyzing Top-Performing Content

This initial phase focuses on gathering extensive data to provide sufficient context for the Large Language Models (LLMs) in subsequent steps <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Topic Input**: The process begins by entering a specific topic, such as "inade," into a chat interface <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Data Scraping**: The system then scrapes top videos on YouTube and posts on X (formerly Twitter) related to the topic, identifying content with high engagement <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Transcription and Merging**: The identified YouTube videos are automatically watched and transcribed <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. All collected data, including YouTube transcripts (hooks, titles, content) and X posts, are combined into one large text block <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Tools Used for Scraping**: Appify is a platform used for scraping content from various internet sources like Instagram, Amazon, TikTok, YouTube, or X, using open APIs that can be plugged into workflows <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. HTTP requests within the workflow call the Appify API for this purpose <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Automated Research Benefits**: Manual research of this depth would require constant online presence <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Automating this step allows users to leverage existing high-performing content as inspiration, short-cutting the content creation process <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

#### 2. Content Idea Generation

Following the research phase, a content idea generator agent is employed <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **LLM Integration**: This agent connects to an OpenAI LLM <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Idea Extraction**: It scans the large text block of researched content to find fresh angles and content ideas that go beyond simple replication <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The AI is tasked with generating these ideas <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Prompt Engineering for Ideas**:
    *   **Core Instruction**: Create actionable content ideas strictly related to marketing, using the provided research <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   **Specific Output Requirements**: Ideas should have a short and clear title, a "scroll-stopping" hook, an optimal format, and a unique angle on how marketers can scale efforts using AI and NADN <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   **Style Guidelines**: Avoid technical jargon and focus on the target audience <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. The agent also analyzes the user's top-performing X posts to understand their brand voice and themes <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Improving Prompts with AI**: Initial prompts can be refined by feeding them into other AI tools like ChatGPT, Manis, or Claude, along with examples of desired content, to improve their effectiveness <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This emphasizes the importance of knowing "what questions to ask and what good looks like" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

#### 3. Factual Research and Validation

To prevent AI "hallucinations" and ensure content accuracy, a research agent is used to find supporting facts, trends, and sources <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   **Tool Used**: Perplexity is used to find real stats, use cases, industry trends, insights, marketing applications, and popular opinions related to the marketing angles <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **LLM Access**: Open Router is a valuable tool that allows access to multiple LLMs (like Perplexity, OpenAI, Claude) through a single node and a single subscription, simplifying integration into workflows <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This enables the use of the "best LLM or the best model for each specific task" <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

#### 4. Content Creation and Image Generation

The identified ideas and research data are merged and fed into a content agent tailored for a specific channel, such as LinkedIn <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **LLM for Writing**: Claude 3.7 Sonnet is currently considered the best writing LLM <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. Its power lies in its ability to produce incredible results when given sufficient context and data <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. The common pitfall is not providing enough context, leading to poor output <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Prompting for Content Creation**:
    *   **Brand Voice**: Instructions include guidelines for an authentic, confident, straightforward, direct, and non-formal tone, avoiding corporate jargon or marketing speak <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
    *   **Narrative Structure**: The AI is prompted to create a narrative-driven post with actionable insights that positively impact business <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. Data should only be used if relevant to the context <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
    *   **Formatting**: Specific output formats are requested, including title and content sections <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. Instructions are also given to avoid AI habits like excessive hashtags and em dashes <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   **Role-Playing**: The LLM is framed as a "LinkedIn content strategist and conversion copywriter" <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Including "direct response" or "conversion copywriting" in prompts encourages content that leads people through a journey with a strong hook, builds interest and desire, offers actionable value, and has a clear call to action <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Image Generation**: The workflow uses the OpenAI image generation model. Prompts can be simple (e.g., "3D image communicating an AI system") or complex with dynamic prompts based on the post topic <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

#### 5. Human in the Loop and Publishing

Before final publication, a "human in the loop" step allows for review and editing, as AI content is not always ready for direct publishing <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
*   **Review Process**: A link to the generated Google Doc (containing the completed post and image) is sent via Slack <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. Users can review the draft, which often includes a personal narrative and actionable points <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Image Customization**: While AI can generate images, personal photos often resonate more on platforms like LinkedIn <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. It's possible to store a folder of personal images in Google Drive and have the workflow randomly select one to pair with the content <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **One-Button Publication**: After review, a single "approve" button in Slack can directly publish the content to the chosen social platform <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.

### Benefits of AI-Generated Content

*   **Validated Posts**: The content generated is "validated" because it's based on data scraped from top-performing YouTube videos and X posts <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. This significantly increases the chances of the content resonating with the audience <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.
*   **Reduced Guesswork**: It removes the guesswork from content creation by leveraging real validation from already successful content <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Testing and Refinement**: Users can test multiple variations, delete underperforming ones, and double down on those that show good early data <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
*   **Authenticity**: The goal is for AI-generated content to pass the "Turing test," making it feel as authentic as possible to the reader <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

This workflow and similar [[building_aipowered_content_generation_tools | AI-powered content generation tools]] can serve as a backbone for consulting, freelancing, or agency businesses by optimizing operations and content output <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

### Accessing the Workflow Template

A complete workflow template (JSON file) for NADN is available for free download at templates.vibemarketer.com/greg <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. This allows users to upload the file into NADN, make it their own, and begin experimenting with AI content generation <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. Playing around with the workflow, tinkering, and optimizing based on output data is the best way to understand and master it <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.