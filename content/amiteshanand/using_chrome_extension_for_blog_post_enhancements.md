---
title: Using Chrome Extension for Blog Post Enhancements
videoId: fjdcGj86CmA
---

From: [[amiteshanand]] <br/> 

Technical writers often face challenges when creating blog posts, such as needing external tools for image generation or content review. This typically involves copying sections of content, navigating to another website like ChatGPT or Claude, applying prompts, and then manually copying suggestions back to the blog post <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. A new Chrome extension streamlines this process by integrating these capabilities directly into the [[blog_writing_platforms | blog writing platform]], such as dev.to <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Core Functionality

This [[building_a_chrome_extension_with_deepseek_and_flux | Chrome extension]] allows users to:
*   Review blog post content directly within the writing platform <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   Generate images on the fly based on the content <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Technology Behind the Extension

The extension's capabilities are powered by Nebius AI Studio, a platform that hosts various state-of-the-art open-source AI models <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

Key models utilized include:
*   **DeepSeek V3 and DeepSeek R1**: Used for text-to-text tasks, specifically for evaluating technical content and providing suggestions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. DeepSeek R1 is a reasoning model similar to GPT-4o1 but is more cost-effective to run <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **FLUX Schell and Stable Diffusion models**: Used for text-to-image generation <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The FLUX model is specifically used for image generation in this demonstration <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Nebius AI Studio provides APIs in JavaScript, Python, and even cURL requests, which were used to build this Chrome extension <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## How It Works in Practice

When writing an article, such as one on integrating fast LLM inferencing with vector search <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, the extension offers a seamless workflow:

1.  **Select Text**: Highlight a section of the text within the blog post <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  **Access AI Tools**:
    *   **Right-Click Menu**: A right-click context menu provides an "AI tool" option <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   **Hover Items**: Alternatively, hovering buttons and icons appear when text is selected, offering direct options <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
3.  **Generate Image**: Selecting "Generate image from text" creates an image based on the selected content, which can then be easily copied and pasted into the blog <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
4.  **Review Text with AI**: Selecting "Review the text with AI" uses models like DeepSeek V3 or DeepSeek R1 to analyze the content and provide suggestions for improvement <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These suggestions can then be applied directly <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Benefits

This Chrome extension significantly enhances the [[blog_creation_using_pieces_and_live_context | blog creation]] process by:
*   **Eliminating Context Switching**: Writers do not need to leave their [[blog_writing_platforms | blog writing platform]] to use external tools for image generation or content review <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Improving Efficiency**: The ability to generate images and review content on the fly saves time and effort <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Empowering Writers**: It allows writers to focus primarily on the content of their blog, providing an "ease of use tool" to empower them <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.