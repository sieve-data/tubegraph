---
title: Using AI to create Chrome extensions
videoId: 5lNHx6IC8Fc
---

From: [[gregisenberg]] <br/> 

[[Developing and launching Chrome extensions | Creating Chrome extensions]] presents a significant opportunity for founders to experiment and potentially generate substantial revenue, ranging from $10,000 to $100,000 per month <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. The process is often less work than anticipated, especially when [[optimizing_aienhancements_in_web_development | leveraging AI tools]] <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## Identifying Chrome Extension Ideas

Identifying viable ideas is the first step, and several strategies can be employed:

*   **GitHub Issue Mining** One approach is to explore GitHub for unresolved problems in various projects <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. These unresolved issues can highlight pain points that a Chrome extension could solve <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. A Chrome extension can serve as an excellent [[building_a_profitable_chrome_extension | Minimal Viable Product (MVP)]] before potentially evolving into a full-fledged SaaS business, as exemplified by VidIQ <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   **Google Chrome Store Analysis** Browse the Google Chrome Store, particularly focusing on highly-rated applications <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. Consider how existing popular apps could be "AI-ified" by adding AI capabilities <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. [[Using AI to Build HighTraffic Websites | Reverse engineering]] an existing extension and integrating AI is not difficult, even for non-developers with sufficient grit <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.
*   **Product Hunt Exploration** Product Hunt is a valuable resource for discovering popular products, including Chrome extensions <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. Analyzing user reviews can reveal what people like or dislike, offering insights for new ideas <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. Additionally, evaluate successful SaaS products and brainstorm how they could be adapted into a Chrome extension <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>.
*   **Reddit Pain Point Tracking** Reddit is a common platform for users to express frustrations and pain points <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. Setting up IFTTT (If This Then That) alerts for phrases like "I wish Chrome could..." on Reddit can automatically flag potential startup ideas <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. Tools like Gummy Search can further assist in extracting pain points from specific subreddits <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.
*   **Chrome Web Store Review Analysis** Similar to Product Hunt, analyzing one-star reviews on the Chrome Web Store can uncover critical flaws in existing extensions <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. Tools like GPT can be used to summarize these negative reviews, helping identify areas for improvement <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.
*   **API Change Log Monitoring** For developers, monitoring API change logs can reveal new integrations that could be leveraged for "first to market" Chrome extensions <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
*   **YouTube Tutorial Comment Scraping** Reviewing comments on YouTube tutorials can highlight common struggles or desired functionalities that a Chrome extension could address <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.
*   **Feature Requests for SaaS Products** Pay attention to feature requests mentioned for SaaS products on platforms like Twitter/X <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>. These requests often indicate unmet needs that a Chrome extension can fulfill <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.

## Building a Chrome Extension with AI

Building a Chrome extension, even without prior experience, is made significantly easier with AI <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>. The process often involves an iterative dialogue with the AI model.

### Practical Example: HTML/CSS Scraper

A demonstration illustrates how to build a Chrome extension that scrapes the HTML and CSS of any given website <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.

1.  **AI Tool Selection**: While Cursor AI can be used, directly [[utilizing_ai_for_writing_and_content_creation | utilizing AI tools]] like Claude or ChatGPT might offer better results and a more conversational interface <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.
2.  **Initial Prompt**: Start by asking the AI how to build a Chrome extension that scrapes HTML and CSS <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>.
3.  **File Generation**: The AI will provide step-by-step instructions, including the necessary files: `manifest.json`, `popup.html`, `popup.js`, and `background.js` <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a>. These files are created in a new directory <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
4.  **Code Implementation**: Copy and paste the AI-generated code into the respective files <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>. This manual step, though seemingly simple, aids in learning the fundamental structure of Chrome extensions <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.
5.  **Loading the Extension**:
    *   Open Chrome (or a Chromium-based browser like Arc) <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.
    *   Navigate to `chrome://extensions`.
    *   Enable "Developer mode" <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
    *   Click "Load unpacked" and select the extension directory <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>.
6.  **Iterative Refinement**:
    *   **Initial Test**: Test the extension. If it doesn't work as expected (e.g., the scrape button doesn't do anything) <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>.
    *   **Prompting for Fixes**: Go back to the AI and describe the issue, providing the codebase for context. For example, "Make it so that when I click 'scrape this page' that it actually scrapes the page and gives me the HTML and CSS that I can copy" <a class="yt-timestamp" data-t="19:22:00">[19:22:00]</a>.
    *   **Addressing Rendering Issues**: If the scraped HTML/CSS isn't renderable, prompt the AI to modify the code so it works on any HTML editor/renderer <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>.
    *   **Troubleshooting Site Blocks**: Some sites, like YouTube, implement Content Security Policies (CSP) that prevent extensions from injecting script files, thus blocking scraping <a class="yt-timestamp" data-t="33:35:00">[33:35:00]</a>. The AI can help identify such reasons <a class="yt-timestamp" data-t="34:12:00">[34:12:00]</a>.
    *   **Design and Best Practices**: Once functionality is confirmed, further prompt the AI to "make it cuter and more fun" or to "review the code base and make sure I'm following best practices" <a class="yt-timestamp" data-t="29:25:00">[29:25:00]</a>.

Through a few iterative prompts, a functional Chrome extension can be built, even performing complex tasks like scraping website layouts with animations <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>.

## Publishing and Monetization

Once the extension is built, publishing it to the Chrome Web Store is straightforward <a class="yt-timestamp" data-t="27:07:00">[27:07:00]</a>:

*   **AI Guidance**: The AI can provide a step-by-step plan for publishing, including ensuring code completeness, creating icons and descriptions, and signing up for a developer account <a class="yt-timestamp" data-t="27:28:00">[27:28:00]</a>.
*   **Low Barrier to Entry**: The main requirement is a one-time $5 registration fee <a class="yt-timestamp" data-t="27:53:00">[27:53:00]</a>.
*   **Monetization**: While not explicitly detailed in the example, the overall goal is to build extensions that can eventually be charged for <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>, contributing to the idea of [[building_a_profitable_chrome_extension | creating a profitable Chrome extension]] factory <a class="yt-timestamp" data-t="26:38:00">[26:38:00]</a>.

Developing Chrome extensions with AI is an accessible entry point for those with great ideas, enabling them to build an MVP and learn development fundamentals before potentially transitioning to more complex web applications <a class="yt-timestamp" data-t="28:02:00">[28:02:00]</a>.