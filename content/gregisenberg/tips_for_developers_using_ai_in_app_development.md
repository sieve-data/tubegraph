---
title: Tips for developers using AI in app development
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris Baroque, a developer who has built a significant portfolio of native mobile apps using AI, shares his advanced workflow and key techniques for [[building_apps_using_ai_tools|AI app development]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. His approach allows him to create robust applications, like his daily planning app Ellie, with thousands of users, despite being a solo developer <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Key Tools and Models Used

Chris primarily uses the following [[tools_and_platforms_for_ai_app_development|tools and platforms for AI app development]]:
*   **Cursor** for coding <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. He has used AI for coding for about two years, trying various tools like GitHub Copilot, Windsurf, and Claude Code, but finds Cursor to be the best currently <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **ChatGPT** for asset generation <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. He notes a significant improvement in ChatGPT's ability to create high-quality assets <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Claude 3.7** as his preferred model <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. While Claude 3.5 is good, he finds 3.7 to be superior, especially for [[building_an_ios_app_using_ai|native iOS development]], despite its tendency to "go off the rails" sometimes <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Open Router** for swapping out LLM models <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This service allows testing different models (e.g., Gemini, Claude, OpenAI) with a single line of code, providing flexibility during development <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

## AI App Development Strategies

Chris employs several [[ai_app_development_strategies|AI app development strategies]] for efficient and effective mobile app creation:

### iOS Development with Cursor
Chris's method for [[building_an_ios_app_using_ai|native iOS development]] with Cursor involves opening the Xcode project file directly in Cursor <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. He makes file edits using Cursor's chat feature and then switches back to Xcode to build and test, repeating this process iteratively <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This is significantly faster than his old method of copy-pasting code into Claude <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Manual Project Setup
Crucially, Chris advises against using Cursor to set up the Xcode project initially <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Many manual settings in Xcode, such as selecting frameworks or enabling outgoing network requests, cannot be done by Cursor and must be configured manually <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. He notes that while Cursor can handle similar setups for React Native, Xcode requires manual intervention <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

### Phased Development: UI First
A core technique is to build the UI first using dummy data, then connect the backend or actual data <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This helps the AI focus on one task, increasing the chances of success <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. When requesting UI, he explicitly instructs the AI to "follow the similar UI as other parts of the app" to maintain consistency and prevent it from generating arbitrary components <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

### Utilizing Screenshots for UI Fixes
When the AI's generated UI is not perfect or has errors, Chris feeds screenshots of the app to Cursor, asking it to "fix it" repeatedly until the desired result is achieved <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. He also uses tools like Mobin to get UI inspiration and then feeds those screenshots to Cursor as a starting point <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

### Documenting Tools and APIs
Chris recommends feeding official documentation (e.g., Open Router docs) directly into Cursor by pasting the URL <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Cursor indexes the documentation, providing it with context for API calls and reducing "hallucinations," especially when working with rapidly changing AI APIs or Apple-specific development, where AI might generate non-existent features <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.

### Prompt Engineering and XML Format
Chris uses Claude to generate effective prompts, which are crucial for [[ai_app_development_strategies|AI app performance]] <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>. He advises formatting prompts in XML, which has a higher chance of producing good results from LLMs <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>. For example, he requests concise, friend-like responses without showing the AI's work <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.

### Generating Realistic Mock Data
To enhance testing and demos, Chris uses AI to generate realistic mock data that resonates with users <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. For his budgeting app, he asked the AI to create data for a "28-year-old male in Dallas," resulting in realistic restaurant names and spending patterns <a class="yt-timestamp" data-t="00:31:43">[00:31:43]</a>. This saves time and makes demos more compelling <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.

### Implementing Tool/Function Calling for Agents
To optimize LLM calls and reduce costs, Chris implements tool or function calling <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. Instead of feeding an entire dataset (e.g., two years of transactions) with every query, he gives the LLM tools (functions) it can call to retrieve specific, relevant data based on the user's question <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>. This enables the app to act more like an agent, intelligently fetching only the necessary information from the local database before responding <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. He explicitly instructs the AI to create *local* tools, not external API calls <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>.

### Monitoring Costs and Tokens
Chris added a feature to his app to display the total tokens used and the cost for each LLM response <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. This helps developers monitor expenses during development and testing, especially with Open Router's ability to show different model price points and context windows <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.

### Infinite Asset Generation with AI
Using GPT-4o, Chris demonstrates how to take a primary asset (like a mascot) and generate countless secondary assets in a consistent style for various app states (e.g., loading screens, empty states) <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>. By feeding existing images and providing specific prompts (e.g., "give it wired glasses and put it in front of a laptop"), developers can create unique and polished visual elements <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>.

## General Advice for Developers

### Embrace AI Tooling
Chris strongly encourages developers to embrace [[the_role_of_ai_and_new_technologies_in_app_development|AI and new technologies in app development]] <a class="yt-timestamp" data-t="00:53:46">[00:53:46]</a>. He believes that proficient developers who learn to leverage these tools will benefit the most and thrive in the coming decade, as AI in coding is inevitable <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>.

### Understand Fundamentals and Security
While AI can accelerate development, Chris cautions that tools like Cursor can be "dangerous" because they might place sensitive information, such as API keys, in the front end, leading to security vulnerabilities and unexpected costs <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. He advises non-developers to start with tools that have more "guardrails" like Replit or Lovable <a class="yt-timestamp" data-t="00:55:55">[00:55:55]</a>. It's essential for everyone to learn programming fundamentals and use AI as a teacher to build a strong foundation before diving into more advanced AI coding tools <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.

> "If you're a developer and you're on the fence of using this stuff, I think you should just do it. I know it is kind of like there's it's kind of taboo like some people are like it's it's kind of killing the art, but um this stuff is inevitable. I think it's better to really learn and those are the developers that are going to thrive for the next decade." <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>