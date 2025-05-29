---
title: Chrome Extension Development with JavaScript APIs
videoId: fjdcGj86CmA
---

From: [[amiteshanand]] <br/> 

This article details the development and functionality of a Chrome extension designed to assist technical writers directly within their blogging platforms, such as dev.to <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The extension streamlines the content creation process by integrating AI-powered tools for content review and image generation without requiring the user to leave their current writing environment <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Core Functionality

The developed Chrome extension provides two primary features:

1.  **Content Review** <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>: Users can select a section of their blog post and receive AI-generated suggestions for technical review and improvement <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This feature eliminates the need to copy text to external tools like ChatGPT or Claude for review <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
2.  **Image Generation** <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>: Based on selected text content, the extension can generate relevant images on the fly <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. These images can then be easily copied and inserted directly into the blog post <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Technology Stack

The extension leverages Nebula's AI Studio, a platform that hosts various state-of-the-art open-source AI models <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### AI Models Utilized

*   **Text-to-Text Models**:
    *   Deepseek V3 <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
    *   Deepseek R1: A reasoning model similar to GPT-4o, often more cost-effective to run <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Text-to-Image Models**:
    *   FluX Scheller <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
    *   Stable Diffusion models <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>

### API Integration

Nebula's AI Studio provides APIs (Application Programming Interfaces) accessible via JavaScript, Python, or cURL requests <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The [[building_a_chrome_extension_for_blogging | Chrome extension]] was specifically built using these JavaScript APIs <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## User Experience

The extension integrates seamlessly into the user's workflow:

*   **Context Menu**: Users can select text within their blog editor, right-click, and access "AI tools" to generate an image or review text <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Hovering Icons**: When text is selected, hovering buttons or icons appear, providing direct options to leverage features like image generation <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

This design ensures that technical writers can remain focused on their content, eliminating the need to navigate to multiple [[online_tools_for_software_development | external online tools]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.