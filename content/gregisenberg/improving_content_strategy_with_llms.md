---
title: Improving content strategy with LLMs
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

Modern content strategy can be significantly improved through the integration of Large Language Models (LLMs) and AI agents, enabling automated content creation and distribution on platforms like LinkedIn <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This approach aims to put content on autopilot, saving significant time—potentially 10 to 15 hours per week <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Workflow for Automated Content Creation

An end-to-end automation workflow leverages LLMs to produce content that receives likes and comments <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This system allows for faster testing of content angles, hooks, and topics, resulting in top-performing content by providing LLMs with ample context and information <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

The workflow consists of several key stages:

### 1. Data Collection and Research
The initial phase involves analyzing data from platforms like YouTube and X (formerly Twitter) to gather information about a specific niche or topic <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Scraping Top Content** The process begins by scraping highly engaged content from YouTube and X related to the chosen topic <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This is often done using tools like Appify, which offers APIs to access data from various internet platforms such as Instagram, Amazon, TikTok, YouTube, and X <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Content Transcription** Once scraped, YouTube videos are transcribed, and posts from X are collected, merging all this data into a single, large text block <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This comprehensive research ensures sufficient context for the subsequent LLM stages <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. This automates the manual research that savvy content creators typically undertake to understand existing content and identify opportunities <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

### 2. Content Idea Generation
After data collection, a content idea generator agent, powered by an OpenAI LLM, scans the aggregated text block to find fresh angles and content ideas <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Prompting for Innovation** The LLM is prompted to create actionable content ideas strictly related to marketing, focusing on unique angles rather than mere replication of researched content <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Instructions include requirements for short, clear titles, scroll-stopping hooks, optimal content formats, and unique points of view on how marketers can scale efforts using AI <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Brand Voice Integration** The system analyzes the user's top-performing X posts to identify brand voice, themes, and communication style, ensuring the generated ideas align with the creator's established presence <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Prompt Improvement with AI** Initial prompts can be refined by other LLMs (e.g., ChatGPT, Manas, Claude) to improve their effectiveness, emphasizing the importance of knowing what questions to ask and what constitutes "good" output <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### 3. Factual Research and Data Integration
To ensure content is backed by credible information and avoids "hallucinations," a research agent is employed <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Leveraging Perplexity** This agent uses tools like Perplexity to find real-world use cases, statistics, trends, insights, and case studies relevant to the marketing angles identified <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Multi-Model Access** Tools like Open Router allow seamless access to various LLMs (e.g., Perplexity, OpenAI, Claude) through a single node, enabling the selection of the best model for each specific task <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### 4. Content Generation and Refinement
The combined ideas and research data are then fed into a content agent tailored for a specific platform, such as LinkedIn <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Using Claude 3.7 Sonnet** Claude 3.7 Sonnet is highlighted as the best LLM for writing due to its power when provided with sufficient context and data <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. The key to powerful AI output is supplying "tons of data and tons of context" <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Brand Voice and Narrative** Prompts include detailed brand voice guidelines (e.g., authentic expertise, direct communication, confident, no corporate jargon) and instruct the LLM to create narrative-driven posts with actionable insights <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Conversion Copywriting Principles** The LLM is framed as a "LinkedIn content strategist and conversion copywriter," ensuring content has a strong hook, builds interest and desire, offers value, and includes a clear call to action <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **Avoiding AI Hallmarks** Specific instructions are given to avoid common AI-generated traits like excessive hashtags, emojis, and M-dashes, to make the content feel more authentic <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **Image Generation** The workflow also includes generating an image for the post using an OpenAI image generation model, with the capability for dynamic prompts <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. For personalized content, users can provide a folder of personal photos for random selection and attachment <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### 5. Human-in-the-Loop and Publishing
Before final publication, the content enters a human-in-the-loop step, where the generated post is sent to the user (e.g., via Slack) for review and approval <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
*   **Review and Edit** The draft is presented in a Google Doc, allowing for edits before going live <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This ensures quality control and allows for minor adjustments to maintain authenticity and alignment with personal style <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **One-Button Publication** Upon approval, the content can be published directly to the desired social platform with a single click <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.

## Benefits of this Approach

*   **Validated Content** The process generates social posts validated by existing engagement data from YouTube and X, significantly increasing the chances of content resonating with the audience <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Reduced Guesswork** It removes the guesswork from content creation by leveraging real validation from previously performing content <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Efficiency and Scalability** This workflow allows for testing multiple content ideas rapidly, doubling down on successful ones, and repurposing content for various channels <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
*   **Authenticity** The goal is to produce content that passes the "Turing test," making it difficult for readers to discern if it was AI-written <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.

This [[creating_multiformat_content_for_organic_growth | approach]] can serve as a powerful backbone for [[b2b_growth_and_content_strategies | B2B growth and content strategies]], optimizing [[frameworks_for_effective_writing_and_content_strategy | agency operations]], or powering consulting and freelancing businesses by leveraging [[integration_of_large_language_models_llms_with_external_tools | LLM integration with external tools]] <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. It contributes to [[the_importance_of_organic_content_for_messaging | organic short form content strategies]] by making content creation more data-driven and efficient, ultimately simplifying [[using_ai_to_simplify_content_consumption_and_creation | content consumption and creation]]. A template for this workflow is available for free to help users get started <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.