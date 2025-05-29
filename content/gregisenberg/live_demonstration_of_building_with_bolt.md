---
title: Live demonstration of building with Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

[[introduction_to_bolt_by_eric_simons | Bolt]], developed by Stack Blitz, is highlighted as a powerful tool for bringing ideas to market quickly, even described as a "Cursor AI killer" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Eric Simons, the founder of Stack Blitz and [[introduction_to_bolt_by_eric_simons | Bolt]], provided a live demonstration of building applications using the platform <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Eric, who typically acts as a "Chief bugfinder" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> for Bolt, emphasized that the demonstration was unrehearsed, reflecting a real-world user experience <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. [[introduction_to_bolt_by_eric_simons | Bolt]] has only been online for about a month, so encountering roadblocks during the live build was expected and valuable for product improvement <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## [[creating_a_directory_site_using_bolt | Creating a Directory Site]]

The first project tackled was a directory site <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Greg suggested this idea due to its potential for SEO traffic and evolution into a product <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The specific concept was a directory of great products curated for Indie hackers and builders, similar to Product Hunt <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Prompting Philosophy
Eric explained his approach to prompting [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]]'s AI: starting with a high-level, "spiritual" description of the desired vibe and target audience, followed by specific functionalities <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This method helps the AI generate effective marketing copy for the product <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Initial Build & Challenges
Upon submission, [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] quickly generated a real codebase, installing dependencies and writing files <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. An initial error occurred, which Eric diagnosed as a "dumb mistake" by the AI, failing to escape a quote character <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. He demonstrated fixing this by copying the error into the chat, allowing the AI to attempt a solution <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

Bolt's AI also pulls royalty-free images from sources like Unsplash by default, providing immediate visuals <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. The generated directory, "Essential Tools for Indie Hackers," included marketing copy aligned with the initial prompt <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a> and individual product pages for SEO <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. The entire process took only about five minutes <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.

### [[exploring_functionality_and_design_options_in_bolt | Refining the Directory]]
To enhance the site, Greg suggested:
*   Vertically listing products instead of horizontally <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   Adding gamification by showing product rankings (number one, two, three) <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   Allowing users to upvote products <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

Eric generally recommends breaking design and functionality changes into distinct, smaller prompts <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This allows for easier use of the "undo" button to revert changes if the AI's output isn't desirable <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. The updated directory included visible vote counts and an upvote button <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

For design, Greg asked for "more pops of color" and a "beautiful" aesthetic with color gradients <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. Eric confirmed [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] can capture such "vibes" <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. He then imported an image of the Arc browser's website to guide [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] on the desired color scheme and overall aesthetic <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>. The AI successfully adopted the color palette and added relevant icons, creating a visually appealing site <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

## [[deployment_and_realtime_features_with_bolt | Deployment and Realtime Features with Bolt]]

[[deployment_and_realtime_features_with_bolt | Bolt]] allows for quick deployment to production hosts like Netlify <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. By clicking a "deploy" button, Bolt performs a production build and generates a real URL, making it easy to share or attach a custom domain for SEO <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. The process runs in the browser, directly uploading to Netlify without requiring a login <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>. The deployed site maintained the chosen color scheme and design elements <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>.

## [[building_prototypes_with_boltnew_for_nontechnical_users | Building a Micro SaaS App with Real-time Chat]]

To demonstrate more complex functionality, Eric proposed adding a live chat page to the directory site for Indie hackers to communicate in real-time <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.

### Choosing a Backend
Eric specified the use of Firebase, as it tends to work best with [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] due to its built-in authentication, real-time data storage, and synchronization capabilities <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. He also noted that [[deployment_and_realtime_features_with_bolt | Bolt]] will soon have recommended one-click providers for seamless integration <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.

### Implementation Challenges & Solutions
The process encountered several issues:
1.  **AI Slowdown**: Eric observed a slowdown, speculating it might be due to increased usage of Anthropic's models (used by Bolt) after GitHub Copilot allowed Sonnet usage <a class="yt-timestamp" data-t="00:34:28">[00:34:28]</a>.
2.  **Dev Server Restart**: The LLM sometimes forgets to restart the development server, which Eric manually triggered <a class="yt-timestamp" data-t="00:36:15">[00:36:15]</a>.
3.  **Firebase Setup**: Finding the Firebase API keys was unexpectedly difficult within the Firebase console <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>, requiring a web search to find that a web app needed to be created first <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>.
4.  **Authentication Issue**: An error related to signing in for chat appeared <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>. Following the advice to simplify, Eric prompted the AI to temporarily remove the sign-in requirement <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>. This highlights the [[tips_and_guidance_for_beginners_exploring_ai_tools_like_boltnew | strategy]] of adding complex functionality incrementally <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.
5.  **Database Type**: The chat messages were initially stored in Firebase Firestore instead of the Realtime Database that Eric preferred <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>.

After resolving these issues, the chat functionality worked, demonstrating real-time communication between users on the deployed site <a class="yt-timestamp" data-t="00:44:17">[00:44:17]</a>. The AI also smartly moved API keys to an environment variable file (ENV) during deployment, a best practice for production <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>.

## General Insights and Benefits

Eric noted that [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] is much simpler to use for non-developers compared to tools like [[comparing_boltnew_with_other_ai_development_tools_like_cursor_and_v0 | Cursor AI]] <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. While [[comparing_boltnew_with_other_ai_development_tools_like_cursor_and_v0 | Cursor]] excels in large, complex codebases, [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] is ideal for quickly building and launching full-stack web applications, including those with backend features like authentication and payment processing (e.g., Stripe, Supabase) <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.

A compelling example shared was a user from Thailand who built a viral hooks app called "Viral Hooks" entirely with [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] for $50/month in a week and a half <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This contrasted with external developer quotes of $3,000-$5,000 and several months <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>. This demonstrates the "arbitrage opportunity" for creative, entrepreneurial individuals to leverage AI tools <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>. [[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] has already enabled dozens of users to launch products and acquire their first customers <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>, including Y Combinator startups for landing pages <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>.

## Getting Started

To [[tips_and_guidance_for_beginners_exploring_ai_tools_like_boltnew | get started with Bolt]], users can visit bolt.new, type in their idea, and hit enter <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Additional resources include:
*   YouTube tutorials, such as "How to add a database to your Bolt.new app" by Tomac <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>.
*   Following @stackblitz on X (formerly Twitter) <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.
*   Joining their Discord server at discord.gg/stackblitz <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a>.