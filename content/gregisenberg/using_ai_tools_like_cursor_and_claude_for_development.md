---
title: Using AI tools like Cursor and Claude for development
videoId: 5lNHx6IC8Fc
---

From: [[gregisenberg]] <br/> 

This article explores how artificial intelligence (AI) tools, specifically [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] and Claude, can be utilized to conceptualize and build Chrome extensions, turning ideas into revenue-generating products or impactful tools [00:00:05]. The process is presented as less work than often perceived, making it accessible even for those new to development [00:00:19].

## The Opportunity of Chrome Extensions
The Chrome Store offers a significant opportunity for founders to experiment and create [00:01:32]. Chrome extensions can serve as an excellent Minimum Viable Product (MVP) before potentially evolving into a full Software as a Service (SaaS) business, as exemplified by VidIQ [00:02:26]. Building developer tools, including Chrome extensions, is particularly appealing because it often doesn't require large teams [00:04:15].

## Generating Ideas for Chrome Extensions

Several strategies can be employed to generate ideas for Chrome extensions:

### 1. GitHub Issue Mining
Developers can explore GitHub issues on unresolved problems [00:01:59]. Identifying repetitive issues within open-source projects can highlight opportunities for new extensions or SaaS businesses [00:03:08]. For example, the `tanack query` library solved a significant data fetching issue in React, which was a widespread problem [00:03:18]. The developer market is vast, with companies like Superbase raising significant capital by solving developer problems [00:03:56].

### 2. Google Chrome Store Analysis
Browsing the Google Chrome Store for existing extensions, particularly highly-rated ones, can spark ideas [00:04:47]. The goal is to identify popular apps and consider how AI can be integrated to "AI-ify" them, creating an enhanced version [00:05:06]. This approach benefits from AI's ability to "reverse engineer" existing Chrome extensions and add AI functionalities [00:05:44].

### 3. Product Hunt Exploration
Product Hunt is another platform to discover popular Chrome extensions [00:07:01]. By examining reviews, one can learn what users like and dislike about existing products [00:07:27]. Additionally, Product Hunt can be used to identify successful SaaS products and brainstorm how to create a Chrome extension counterpart [00:07:50].

### 4. Reddit Pain Point Tracking
Reddit is known for users expressing complaints, making it a valuable source for identifying pain points [00:08:51]. Tools like IFTTT (If This Then That) can be set up to alert users when phrases like "I wish Chrome could..." appear, directly pointing to unmet needs and potential startup ideas [00:08:28]. Gummy Search is another tool that helps extract pain points from various subreddits [00:10:52].

### 5. Chrome Web Store Review Analysis
Similar to Product Hunt, analyzing reviews on the Chrome Web Store can provide insights [00:09:03]. Focusing on one-star reviews is particularly useful, as they often detail specific flaws or missing features that an AI tool like GPT could help summarize and address [00:09:38].

### 6. API Change Log Monitoring
For developers, monitoring API change logs can reveal new opportunities [00:10:20]. Being "first to market" with integrations for new API features can lead to successful extensions [00:10:22].

### 7. YouTube Tutorial Comment Scraping
Analyzing comments on YouTube tutorials can uncover common struggles or areas where users need more assistance, which could be solved by a Chrome extension [00:10:29].

### 8. SAS Product Feature Requests on Social Media
Platforms like Twitter/X are rich sources for feature requests [00:11:04]. Users often express desires like "I wish Figma did XYZ" or "I wish this product did XYZ," providing direct ideas for extensions [00:11:06].

## Building a Chrome Extension with AI: A Practical Demonstration

A practical demonstration showcased [[building_an_ai_app_with_cursor | building an AI app with Cursor]] and Claude to create a Chrome extension capable of scraping the HTML and CSS of any given website [00:11:14].

### Initial Setup and AI Choice
The process began by asking Claude to provide instructions for building a Chrome extension that scrapes HTML and CSS [00:13:40]. Claude was chosen over [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] for the initial prompt because the speaker found Claude's direct output and chat interface yielded "much better" and "burrier" results [00:13:20].

Claude provided a step-by-step guide, including the necessary files (`manifest.json`, `popup.html`, `popup.js`, `background.js`) and instructions for installing the extension in developer mode [00:14:44]. The speaker, having never built a Chrome extension before this, noted the simplicity of the process with AI assistance [00:15:17].

### Step-by-Step Development
1.  **File Creation**: The required files (`manifest.json`, `popup.html`, `popup.js`, `background.js`) were manually created based on Claude's instructions [00:16:13].
2.  **Code Copying**: Code provided by Claude was copied and pasted into each respective file [00:16:44].
3.  **Installation**: The extension was loaded in Chrome's developer mode by selecting the directory containing the files [00:17:26].

### Iterative Refinement with [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]]
Upon initial testing, the "scrape this page" button didn't perform as expected [00:19:19]. This is where [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] was utilized. A prompt was given to [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] to make the button functional and to output copyable HTML and CSS [00:19:26]. [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] applied changes to the codebase, which were then accepted and reloaded into the extension [00:20:00].

Although the extension successfully scraped, the output HTML and CSS were not immediately renderable [00:21:00]. Another prompt was given to [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]], instructing it to make the HTML and CSS renderable in any editor [00:21:10]. After this refinement, the extension was able to correctly scrape and render sites like the New York Times and X.com [00:24:49].

### Encountering and Understanding Limitations
Attempts to scrape YouTube failed [00:33:35]. When asked, [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] explained that YouTube implements a strict Content Security Policy (CSP) to prevent cross-site scripting attacks, which blocks the injection of script files by Chrome extensions [00:34:12]. This also explains why many ad blockers struggle on YouTube [00:35:11]. Claude further elaborated on the legal risks and suggested using the YouTube API instead [00:37:46].

Despite these limitations, the extension successfully scraped other complex sites like Arc Browser, even retaining some animations [00:36:17].

### Enhancing the Extension
The final step involved asking [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] to review the code and apply [[best_practices_for_using_cursor_ai | best practices for using Cursor AI]] for Chrome extension design, as well as to make the interface "cuter and more fun" [00:29:52]. This demonstrates the iterative nature of [[using_ai_for_app_development | using AI for app development]], where developers can continuously improve their creations.

## Publishing a Chrome Extension
Claude also provided a step-by-step plan for pushing the extension to the Google Chrome Store [00:27:10]. This includes ensuring the code is tested, creating compelling icons and descriptions, establishing a developer account, paying a one-time $5 registration fee, and zipping all extension files for upload [00:27:28].

## Conclusion
The demonstration highlights the ease and efficiency of [[utilizing_ai_and_tools_for_business_development | utilizing AI and tools for business development]] like Claude and [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Cursor]] in creating functional Chrome extensions [00:26:51]. This process builds a foundational "knowledge base" for aspiring developers, teaching them the components needed for extensions, and preparing them for more complex [[using_ai_for_app_development | app development]] later [00:28:20]. The low barrier to entry, particularly the $5 registration fee, makes it an accessible starting point for those with innovative ideas [00:27:52].