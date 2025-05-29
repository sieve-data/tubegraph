---
title: Workflow setup with N8N
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

This article outlines a workflow for automating content creation using [[ai_automation_tools_for_workflows | AI automation tools for workflows]] and N8N, enabling a marketing team to produce content on autopilot <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The workflow aims to save 10 to 15 hours per week <a class="yt-timestamp" data-t="01:30:17">[01:30:17]</a>.

## Potential Outcomes and Benefits
By implementing this workflow, users can:
*   Test content angles, hooks, and topics significantly faster <a class="yt-timestamp" data-t="02:08:08">[02:08:08]</a>.
*   Generate top-performing content by providing extensive context and information to large language models (LLMs) <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   Automatically create images and publish content <a class="yt-timestamp" data-t="02:27:03">[02:27:03]</a>.
*   Refine and test content before publishing, similar to A/B testing or using a secret account <a class="yt-timestamp" data-t="02:54:02">[02:54:02]</a>.
*   Leverage real validation from already-performing content to remove guesswork <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>, increasing the chances of content resonating by 10 to 50 times <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

## Workflow Stages in N8N
The workflow is divided into color-coded stages within N8N to provide actionable tips for [[building_simple_workflows_for_marketing_automation | building simple workflows for marketing automation]] <a class="yt-timestamp" data-t="03:09:12">[03:09:12]</a>. A complete workflow code in JSON format can be provided as a [[creating_and_using_templates_in_automation | starting template]] <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>, <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Stage 1: Data Collection and Research
This initial phase focuses on gathering comprehensive data around a niche or topic <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>.
1.  **Input Topic:** Begin by entering a specific topic or keyword into the chat interface <a class="yt-timestamp" data-t="03:53:14">[03:53:14]</a>.
2.  **Scraping Data:**
    *   The workflow scrapes YouTube for the top 20-30 videos with high engagement related to the topic <a class="yt-timestamp" data-t="04:07:07">[04:07:07]</a>, <a class="yt-timestamp" data-t="04:14:26">[04:14:26]</a>.
    *   It also scrapes X (formerly Twitter) for relevant posts, including analyzing the user's own account for insights into their brand voice and themes <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>, <a class="yt-timestamp" data-t="04:24:37">[04:24:37]</a>, <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
    *   **Appify Integration:** The process utilizes Apify, a platform that provides open APIs to scrape data from various internet sources like Instagram, Amazon, TikTok, YouTube, and X <a class="yt-timestamp" data-t="04:53:07">[04:53:07]</a>, <a class="yt-timestamp" data-t="04:56:07">[04:56:07]</a>. HTTP requests within N8N call these Apify APIs <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.
3.  **Transcription and Merging:**
    *   The workflow transcribes all content from the identified top YouTube videos <a class="yt-timestamp" data-t="04:39:19">[04:39:19]</a>.
    *   All collected data, including YouTube video transcripts, hooks, titles, content, and X posts, is merged into one large text block. This provides substantial context for the subsequent LLM processing <a class="yt-timestamp" data-t="05:36:13">[05:36:13]</a>, <a class="yt-timestamp" data-t="05:51:24">[05:51:24]</a>.

### Stage 2: Content Idea Generation
After collecting data, a content idea generator agent uses an OpenAI LLM to analyze the merged text block <a class="yt-timestamp" data-t="07:13:58">[07:13:58]</a>, <a class="yt-timestamp" data-t="07:19:30">[07:19:30]</a>.
*   **Objective:** The goal is to identify fresh angles and content ideas that are not merely replications of the researched material <a class="yt-timestamp" data-t="07:29:10">[07:29:10]</a>.
*   **Prompting Strategy:** The prompt instructs the AI to create actionable content ideas strictly related to marketing, specifically for scaling efforts using AI and N8N <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>, <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>. It specifies desired outputs like:
    *   Short and clear titles <a class="yt-timestamp" data-t="08:38:08">[08:38:08]</a>.
    *   Scroll-stopping hooks <a class="yt-timestamp" data-t="08:42:07">[08:42:07]</a>.
    *   Optimal content format <a class="yt-timestamp" data-t="08:49:03">[08:49:03]</a>.
    *   A unique angle (e.g., how marketers can scale with AI and N8N) <a class="yt-timestamp" data-t="08:52:03">[08:52:03]</a>.
*   **Refining Prompts:** Prompts are initially drafted and then refined using other LLMs like ChatGPT, Manis, or Claude, feeding in examples of desired content <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>. This process leverages the principle of knowing what questions to ask and what good looks like <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.

### Stage 3: Research and Content Creation
This stage focuses on adding factual depth and then generating the content.
1.  **Fact and Trend Research:**
    *   A research agent, using Perplexity, finds specific facts, trends, and sources to back up claims and prevent AI hallucinations <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
    *   It identifies use cases, stats, industry trends, insights, frameworks, case studies, and popular opinions relevant to marketing angles with workflow automation and AI <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>, <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
    *   **Open Router:** The workflow uses Open Router, which allows access to multiple LLMs (like Perplexity, OpenAI, Claude) through a single node and API key, simplifying integration and offering one pricing model <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>, <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.
2.  **LinkedIn Content Agent:**
    *   The combined ideas and research data are fed into a LinkedIn content agent. This can be adapted for any channel, but LinkedIn is used as an example <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
    *   **LLM Choice:** Claude 3.7 Sonnet is chosen for writing due to its current reputation as the best writing LLM <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>, <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>. It performs exceptionally well when provided with ample context and data <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
    *   **Prompting for Content:** Key instructions for the LinkedIn post agent include:
        *   **Brand Voice:** Authentic, direct, confident, straightforward, avoiding overly formal or academic tones, corporate jargon, and marketing speak <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>, <a class="yt-timestamp" data-t="14:39:00">[14:39:00]</a>.
        *   **Content Focus:** Create a narrative-driven post with actionable insights and takeaways for business impact <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>.
        *   **Data Use:** Only use relevant data; avoid picking topics blindly <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
        *   **Format:** Specify desired output format (e.g., title, content) <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.
        *   **AI Persona:** Frame the LLM as a "LinkedIn content strategist and conversion copywriter," emphasizing direct response and conversion copywriting <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>.
        *   **Desired Flow:** Ensure content has a strong hook, builds interest and desire, offers actionable value, and potentially a clear call to action <a class="yt-timestamp" data-t="16:13:00">[16:13:00]</a>.
        *   **Avoid AI tells:** Explicitly instruct the AI not to use hashtags, emojis, or M-dashes to make the content feel more authentic and less AI-generated <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>, <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>.
    *   **Image Generation:** The workflow also uses the OpenAI image generation model (DALL-E) to create a complementary image for the post, such as a 3D image communicating an AI system <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
        *   Future enhancement: Integrate a Google Drive folder of personal photos for random selection and attachment to posts, making them feel more natural <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>, <a class="yt-timestamp" data-t="20:40:00">[20:40:00]</a>.

### Stage 4: Human in the Loop and Publishing
This final stage incorporates human oversight before publishing.
1.  **Review via Slack:** The workflow sends a link to the drafted content in a Google Doc via Slack <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>. This allows for review and editing before it goes live <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>, <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.
2.  **One-Button Publishing:** Once approved in Slack, clicking an "approve" button publishes the content directly to the desired social platform, such as LinkedIn <a class="yt-timestamp" data-t="20:16:00">[20:16:00]</a>.
3.  **Validation:** The content generated is considered "validated" because it's based on data from top-performing YouTube videos and X posts, increasing the likelihood of engagement (likes, comments) <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>. The content aims to pass the Turing test, appearing authentically human-written <a class="yt-timestamp" data-t="22:07:00">[22:07:00]</a>.

This workflow serves as a powerful foundation for [[optimizing_content_creation_process | optimizing content creation process]] and leveraging [[ai_automation_tools_for_workflows | AI automation tools for workflows]] for marketing. It can also serve as a backbone for consulting businesses, freelancing, or agency operations, highlighting [[opportunities_in_automated_workflow_platforms | opportunities in automated workflow platforms]] <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.