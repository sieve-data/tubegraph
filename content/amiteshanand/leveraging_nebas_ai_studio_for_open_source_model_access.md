---
title: Leveraging Nebas AI Studio for Open Source Model Access
videoId: fjdcGj86CmA
---

From: [[amiteshanand]] <br/> 

Traditionally, technical writers creating content on platforms like Dev.to might need to use external tools for tasks such as generating images or reviewing text <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This often involves copying sections of text, navigating to new websites like ChatGPT or Claude, using an LLM for review, and then manually applying suggestions <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, a solution has been developed to integrate these functionalities directly into the writing platform <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

This integration is made possible through [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI Studio]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## What is Nebius AI Studio?

[[integration_of_nebius_ai_for_advanced_ai_functionalitiess | Nebius AI Studio]] is a platform that hosts a variety of [[open_source_alternatives_for_ai | open source]] models, including many state-of-the-art and recent models <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. It provides APIs in JavaScript, Python, or cURL requests, enabling developers to build applications that leverage these AI capabilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Key Features and Supported Models

[[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI Studio]] offers access to a range of models for different AI tasks:

*   **Text-to-Text Models:** For reviewing technical content and providing suggestions <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   Deepseek V3 <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
    *   Deepseek R1 (a reasoning model that uses Chain of Thought, similar to GPT-4, and is more cost-effective to run) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a> <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   **Text-to-Image Models:** For generating images based on textual content <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
    *   [[image_generation_with_nebius_ai_and_flux_model | Flux model]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a> <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    *   Stable Diffusion models <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>

## Practical Applications: A Chrome Extension Example

A Chrome extension has been developed utilizing [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI Studio]]'s APIs to empower technical writers directly within their blogging platform <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a> <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Integrated AI Tools

This extension allows users to:

*   **Generate Images from Text:** By selecting a portion of text within the blog post, users can right-click or use hovering buttons to generate an image based on the selected content, which can then be easily copied and pasted <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a> <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The [[image_generation_with_nebius_ai_and_flux_model | Flux model]] is used for this purpose <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Review Text with AI:** Users can select text and choose the "review text with AI" option to receive suggestions for their technical content <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The Deepseek V3 and Deepseek R1 models are used for this evaluation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Benefits

Leveraging [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI Studio]] in this manner provides several advantages:

*   **Seamless Workflow:** Writers no longer need to leave their platform to use external AI tools, streamlining the content creation process <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **On-the-Fly Functionality:** Images can be generated and text reviewed instantly based on the current content <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Ease of Use:** Features are accessible via right-click or hovering icons upon text selection <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a> <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Cost-Effectiveness:** Utilizing [[open_source_alternatives_for_ai | open source]] models like Deepseek R1 can be much cheaper compared to proprietary alternatives like GPT-4 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Focus on Content:** Allows writers to concentrate solely on the blog content without worrying about managing multiple tools <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.