---
title: Using AI to develop Chrome extensions
videoId: 5lNHx6IC8Fc
---

From: [[gregisenberg]] <br/> 

Developing [[chrome_extensions_as_a_profitable_business_model | Chrome extensions]] is presented as a significant opportunity, with the potential to generate substantial revenue, ranging from $10,000 to $100,000 per month <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process is less work than commonly thought, especially when leveraging AI tools <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Why Build Chrome Extensions?

[[building_a_successful_chrome_extension | Chrome extensions]] are considered an excellent starting point for entrepreneurs and developers for several reasons:
*   **Minimal Viable Product (MVP)**: A Chrome extension can serve as a great MVP before scaling up to a full [[using_ai_tools_for_web_ui_and_backend_development | SaaS business]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. VidIQ, a popular YouTube creator tool, began as a Chrome extension and evolved into a full [[using_ai_tools_for_web_ui_and_backend_development | SaaS business]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Lower Barrier to Entry**: Compared to complex [[using_ai_tools_for_web_ui_and_backend_development | web apps]] requiring extensive teams, Chrome extensions can be built and maintained by smaller teams or even individuals <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **High ROI**: The return on investment for building a Chrome extension, from development to monetization, is significantly higher than for more complex applications <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.

## Ideation and Market Research

While the focus is on development, several methods for [[market_research_for_chrome_extension_ideas | coming up with Chrome extension ideas]] were discussed:
*   **GitHub Issue Mining**: Look for unresolved problems in GitHub issues, which can serve as inspiration for extensions or even [[using_ai_tools_for_saas_development | SaaS businesses]] <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Chrome Web Store Analysis**: Browse the Chrome Web Store, particularly focusing on highly-rated apps, and consider how [[incorporating_ai_features_in_applications | AI features]] could be added to them <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Product Hunt**: Search for popular Chrome extensions or [[using_ai_tools_for_saas_development | SaaS products]] on Product Hunt to understand what users like and dislike, and identify opportunities to adapt [[using_ai_tools_for_saas_development | SaaS products]] into extensions <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Reddit Pain Point Tracking**: Set up alerts (e.g., using IFTTT) for phrases like "I wish Chrome could..." on Reddit, as users often complain about problems that can be solved by an extension <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **YouTube Tutorial Comments**: Scrape comments on YouTube tutorials to identify common struggles users face, which can indicate unmet needs <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **Feature Requests for SaaS Products**: Monitor platforms like Twitter/X for user requests regarding features for existing [[using_ai_tools_for_saas_development | SaaS products]] <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   **Using AI for Review Analysis**: Utilize AI tools like GPT to summarize one-star reviews of existing extensions to identify flaws that a new extension could address <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## Building a Chrome Extension with AI: A Practical Example

An example of [[building_apps_with_ai_tools | building an app]] – specifically a Chrome extension – using AI tools is demonstrated. The goal was to create an extension that scrapes the HTML and CSS of any given website <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Tools Used
*   **Claude**: An AI model used for generating code and instructions <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   **Cursor**: A code editor integrated with AI capabilities <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### The Development Process
1.  **Initial Prompt**: A prompt was given to Claude to build a Chrome extension that scrapes HTML and CSS of any site <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. Claude provided step-by-step guidelines, including necessary files and installation instructions <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
2.  **File Creation**: The following files were created as instructed:
    *   `manifest.json` <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>
    *   `popup.html` <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>
    *   `popup.js` <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>
    *   `background.js` <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>
3.  **Code Implementation**: Code provided by Claude was copied into these files <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
4.  **Loading the Extension**: The extension was loaded in Chrome (or Chromium-based browsers like Arc) by enabling developer mode and selecting the extension directory <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
5.  **Iterative Refinement**: Initial testing showed the extension scraped content but did not render it correctly. Through iterative prompts to Cursor, the AI refined the code to ensure the scraped HTML and CSS were renderable in an editor <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
6.  **Addressing Site-Specific Issues**: It was discovered that some sites, like YouTube, block script injection due to Content Security Policies (CSP) to prevent cross-site scripting attacks, meaning the extension could not scrape them effectively <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. However, other sites like New York Times, Twitter (X.com), Wikipedia, and Arc's website were successfully scraped <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>, <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>, <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>, <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.
7.  **Implementing Best Practices and Design**: The AI was then prompted to review the codebase for best practices and to improve the visual design of the extension <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>.

The process demonstrated that even without prior experience, a functional Chrome extension can be built quickly with AI assistance <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

## Publishing to the Chrome Web Store

Once an extension is developed, AI can guide you through the [[steps_to_publish_a_chrome_extension_on_the_chrome_store | publishing process]] on the [[steps_to_publish_a_chrome_extension_on_the_chrome_store | Google Chrome Store]] <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>. This includes:
*   Ensuring the code is tested and complete <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.
*   Creating icons (16x16, 48x48, 128x128) and a compelling description <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
*   Creating a developer account and paying a one-time $5 registration fee <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>.
*   Zipping and uploading all extension files <a class="yt-timestamp" data-t="00:27:42">[00:27:42]</a>.

The $5 fee is a relatively low barrier to entry for publishing <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.

## Becoming a "Chrome Extension Factory"

The recommendation is to embrace the idea of becoming a "Chrome extension factory" <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>. By regularly [[building_a_successful_chrome_extension | building Chrome extensions]] (e.g., one every few weeks), individuals can gain valuable programming knowledge and experience, even without a traditional developer background <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>. This practical experience builds a foundational "developer mind" that will be beneficial when transitioning to more complex [[using_ai_tools_for_web_ui_and_backend_development | web apps]] that involve elements like payments, databases, and authentication <a class="yt-timestamp" data-t="00:28:32">[00:28:32]</a>.