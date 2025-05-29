---
title: Automating social media content creation
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

Automating a marketing team with [[using_ai_for_content_automation | AI agents]] can put content creation on autopilot <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This concept, initially met with skepticism, involves a comprehensive workflow to generate social media content that actively engages audiences <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The presented workflow demonstrates how to achieve this, even providing prompts and templates for implementation <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Overview of the Workflow

This end-to-end automation aims to save 10 to 15 hours per week on content creation <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Specifically demonstrated with LinkedIn, the workflow uses [[ai_tools_for_content_creation_and_marketing | AI to assist with content creation]] for platforms the user dislikes creating content for manually <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The potential outcomes of this workflow include:
*   Faster testing of content angles, hooks, and topics <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Creation of top-performing content by leveraging extensive context and information <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   Automatic image generation and posting <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

While [[utilizing_ai_to_create_marketing_content_and_automate_processes | AI can automate the full process]], it's recommended to test and refine content, potentially using a "secret account" or by implementing a human review step before publishing <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The workflow includes an optional editing step before content goes live <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

The complete workflow code is shared as a JSON file, allowing users to download and upload it into their [[systems_and_strategies_for_consistent_content_creation | Inaden]] setup as a starting template <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Key Tools Utilized

*   **[[systems_and_strategies_for_consistent_content_creation | Inaden]]**: The primary platform used to build and manage the workflow <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Appify**: Used for scraping data from various internet platforms like YouTube, X, Instagram, Amazon, and TikTok via open APIs <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **OpenAI LLM**: Employed for content idea generation <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a> and image generation <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Perplexity**: Used by the research agent to find use cases, stats, trends, insights, and popular opinions to back up content claims <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **OpenRouter**: Allows access to multiple large language models (LLMs) like Perplexity, OpenAI, and Claude through a single node and a single subscription <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Claude 3.7 Sonnet**: Recommended as the best writing LLM for content creation as of the recording <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Google Docs**: Used to output the created content draft for review <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **Slack**: Facilitates the "human in the loop" step by sending a link to the Google Doc for review and an approval button to publish <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

## The Automated Content Creation Workflow Stages

### 1. Research Phase: Analyzing Top-Performing Content
The workflow begins by analyzing content on YouTube and X (formerly Twitter) related to a specified topic <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Input**: A single keyword or topic (e.g., "Inaden") <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Process**:
    *   Scrapes 20-30 top-engaging YouTube videos related to the topic <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   Scrapes posts from the user's X account around workflow automation and AI <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   Transcribes all identified YouTube videos and compiles topics from X <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
    *   Merges all scraped and transcribed data into one large text block for context <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Purpose**: This phase ensures enough context to feed LLMs, replicating a savvy content creator's initial research without manual effort <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. It leverages existing performing content to "shortcut" the content creation process <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### 2. Content Idea Generation
An [[ai_tools_for_content_creation_and_marketing | AI agent]] (using OpenAI LLM) analyzes the gathered text block to find fresh angles and content ideas <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Objective**: Generate new, actionable content ideas related to marketing, distinct from the researched content but inspired by it <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Prompting**: The prompt includes specific instructions for the AI:
    *   Create a list of actionable content ideas strictly related to marketing from the provided content <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   Specify output format: short, clear title; scroll-stopping hook; optimal content format; unique angle (e.g., how marketers scale using AI and Inaden) <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   Avoid technical jargon and frame content for a specific audience <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
    *   Analyze the user's top-performing X posts to match brand voice and themes <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### 3. Factual Research and Data Sourcing
A research agent (using Perplexity via OpenRouter) finds facts, trends, and sources to support content claims and prevent hallucinations <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Data Points**: Identifies use cases, real stats, trends, marketing insights, frameworks, case studies, and popular opinions relevant to the marketing angles <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### 4. Content Creation (e.g., LinkedIn Post)
The merged data (ideas and research) is fed into a content agent (using Claude 3.7 Sonnet) to draft the social media post <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Key to Success**: Providing extensive context and data to Claude enables it to produce highly powerful and credible content <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Prompting Tips**:
    *   **Brand Voice**: Include guardrails to prevent fluff, specifying authentic expertise, direct communication, confidence, and avoidance of formal or corporate jargon <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
    *   **Narrative**: Instruct the AI to create narrative-driven posts with actionable insights that positively impact business <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
    *   **Data Usage**: Only use data if relevant and ensure topics are tied to the context <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
    *   **Formatting**: Specify output format (title, content) and restrict elements like hashtags and emojis <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
    *   **Role-Playing**: Frame the LLM as a "LinkedIn content strategist" and "conversion copywriter" to ensure direct response and conversion-focused content <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
    *   **AIDA Model**: Guide the AI to create a strong hook, build interest and desire, provide actionable value, and include a clear call to action <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
    *   **Avoid AI tells**: Specifically instruct against elements like "M dashes" which can indicate AI authorship <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
    *   **Learning from Examples**: The prompt is refined by using AI to improve it and by feeding in examples of desired content from other creators <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### 5. Image Generation
The workflow uses the OpenAI image generation model to create a visual for the post <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Dynamic prompts can be used based on the post's topic <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. An alternative suggested is storing a Google Drive folder with personal photos and having the AI randomly select one to attach, making the post feel more natural <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

### 6. Human in the Loop
To ensure quality and authenticity, a "human in the loop" step is integrated <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
*   **Process**: The workflow sends a link to the Google Doc containing the draft post via Slack <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. The user can review and edit the content <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

### 7. Publishing
After human review, a single click on an "approve" button in Slack publishes the post directly to the desired social platform (e.g., LinkedIn) <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.

## Benefits of Automated Content Creation

*   **Validation**: The content generated is "validated" because it's based on data from top-performing YouTube videos and X posts, significantly increasing the chances of audience resonance <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Reduced Guesswork**: Removes the need to guess what content will perform well, relying instead on real validation <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Speed and Efficiency**: Enables faster testing and refinement of multiple content pieces <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, saving significant time <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Scalability**: The workflow can be adapted for any social media channel <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a> and can serve as a backbone for consulting, freelancing, or agency operations <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Authenticity**: With careful prompting and human review, the [[using_ai_in_content_creation | AI-generated content]] can pass the "Turing test" and feel authentic <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.

## General Tips for [[effective_content_creation_using_ai_for_marketing | AI Content Creation]]

*   **Know What Questions to Ask**: Formulate clear and specific prompts <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Know What Good Looks Like**: Provide examples of desired content to the AI <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Iterate on Prompts**: Use AI itself to improve your prompts <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Power with Data**: Feed the AI with tons of data and context to maximize its output quality <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Continuous Optimization**: Play around with the workflow, tinker, and optimize based on the output data received <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.

## Workflow Template

A free JSON file containing the complete workflow is available at templates.vibemarketer.com/greg <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. Users can download and upload it into their [[systems_and_strategies_for_consistent_content_creation | Inaden]] setup to begin learning and experimenting immediately <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.