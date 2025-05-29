---
title: Creating a directory site using Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

[[introduction_to_bolt_by_eric_simons | Bolt]] is presented as a leading tool for bringing ideas to market quickly, often touted as a "Cursor AI killer" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Eric Simons, the founder of Stack Blitz, the company behind Bolt, demonstrated its capabilities by building a project live on the Startup Ideas podcast <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This live demonstration highlighted the product's ability to swiftly create functional applications <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Building a Directory of Products

The initial project idea was to [[how_to_start_an_online_directory | build a directory site]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Directories are considered excellent for generating SEO traffic, allowing for future product evolution <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The specific concept chosen was a directory of products for Indie hackers and builders, similar to Product Hunt, focusing on tools that enhance productivity <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Initial Prompt and Desired Features
When prompting Bolt, it's beneficial to describe the project at a "spiritual level," capturing the desired "vibe" along with concrete functionalities <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This approach helps the AI generate effective marketing copy for the product <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

The desired features for the directory included:
*   A single main page showcasing the top five products of the day/week <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   Individual product pages for SEO optimization <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   The potential to integrate affiliate deals with listed products for monetization <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Generation and Initial Look
Bolt generated the codebase and files quickly, demonstrating its speed compared to local development <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The initial generation automatically pulled royalty-free images from Unsplash, providing a good visual starting point <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

The generated site, titled "Essential tools for Indie hackers," effectively conveyed the intended marketing message due to the detailed initial prompt <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

> [00:13:00] "It would have you know, if you kind of squinted it, it's like, okay, yeah, there's a list of products, but now the marketing of these things are actually like the actual copy, makes more sense."

### Iterative Improvements and Design
Users can make iterative changes by prompting Bolt again. A "Prompt Enhancer" feature is available to expand on existing prompts, adding extra details for more specific outcomes <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. An "undo" button allows rolling back to the last working state if changes are undesired <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

For the directory site, the following changes were requested:
*   Vertical listing of products instead of horizontal <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   Gamification elements, including clear ranking (e.g., number one, two, three) and a user upvote feature <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

Bolt successfully implemented the upvoting functionality, allowing users to vote on products, which could lead to high engagement counts and a sense of "aliveness" <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

For design, the request was to add "pops of color" and "beautiful color gradients," referencing the aesthetic of the Arc Browser and Late Checkout Studio websites for inspiration <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. Bolt was able to capture the color palette and add visual elements, resulting in a unique and calming design <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.

> [00:22:15] "It took the color palette, you know, it added these like icons, you know, it's just it did a good job... to do this as like an engineer or designer, it's like it would take longer than what what we just did."

## [[deployment_and_realtime_features_with_bolt | Deployment and Real-time Features]]

[[live_demonstration_of_building_with_bolt | Bolt]] offers built-in deployment to production hosts like Netlify with a single click <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. This allows users to get a real URL, share their product, attach a custom domain, and enable Google SEO ranking <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. The deployment process happens directly in the browser <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

### Adding a Live Chat Feature
To make the directory more interactive, a live chat page for Indie hackers was added, enabling real-time communication <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>. For real-time functionality and authentication, Bolt recommends using Firebase or Superbase, as they integrate well and offer built-in features for data storage and synchronization <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

#### Troubleshooting and Best Practices
During the chat implementation, some issues arose, demonstrating the iterative nature of [[exploring_functionality_and_design_options_in_bolt | building with Bolt]].
*   **AI Error Correction**: When errors occur, copying and pasting the error message into Bolt's chat allows the AI to attempt a fix <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Dev Server Restart**: Sometimes, the LLM may forget to restart the development server, requiring a manual `npm run dev` command <a class="yt-timestamp" data-t="00:36:15">[00:36:15]</a>.
*   **Firebase Configuration**: Accessing Firebase API keys required navigating through project settings and creating a web app within the Firebase console <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. It's important to replace placeholder credentials with actual Firebase keys for deployment <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.
*   **Phased Functionality Adds**: For complex features like real-time chat, it's advisable to start with minimal functionality and add more sophistication (e.g., user presence) later <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>. This helps in debugging and ensures reliability <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>.

After resolving the issues and correctly configuring Firebase, the live chat feature was successfully integrated and deployed, allowing users to communicate in real-time on the live site <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a>.

## Bolt vs. Cursor AI and [[building_prototypes_with_boltnew_for_nontechnical_users | Empowering Non-Technical Users]]

[[introduction_to_boltnew_and_its_benefits_over_cursor_ai | Bolt]] is considered simpler than Cursor AI, especially for non-developers <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. While Cursor AI is a heavyweight tool designed for seasoned engineers and large codebases, Bolt simplifies the process for those who want to rapidly go from idea to production without deep coding knowledge <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.

Bolt allows users to build full-stack web applications, including backends with authentication, payment processing (e.g., Stripe), and databases (e.g., Superbase) <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>. Many users, including Indie hackers and micro-SaaS builders, have successfully launched real products and gained customers using Bolt <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.

## [[tips_and_guidance_for_beginners_exploring_ai_tools_like_boltnew | Tips for Using Bolt]]

*   **Creative Prompting**: Be creative and detailed with prompts, even describing "vibes" for design <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>.
*   **Iterative Development**: Add functionality one feature at a time, especially for complex additions, to simplify debugging <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **Leverage AI**: Becoming proficient at prompting LLMs offers significant "alpha" for entrepreneurs and non-engineers to build and launch products <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

Bolt is available at [bolt.new](http://bolt.new) <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Additional tutorials and community support can be found on Stack Blitz's X account (@stackblitz) and Discord (discord.gg/stackblitz) <a class="yt-timestamp" data-t="00:51:55">[00:51:55]</a>. A specific tutorial on adding a database to Bolt.new apps is available on YouTube <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.