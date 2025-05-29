---
title: Building a directory or scheduling app using Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

[[introduction_to_bolt_and_its_capabilities | Bolt]] is a platform designed to accelerate the process of bringing ideas to market, allowing users to build and deploy applications rapidly <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It is created by Stack Blitz <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, and its founder, Eric, demonstrates its capabilities by building applications live <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. [[introduction_to_bolt_and_its_capabilities | Bolt]] aims to simplify the app development process, particularly for non-developers and entrepreneurs <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>.

## Building a Directory Application

The first project demonstrated with [[using_bolt_for_rapid_prototyping_and_deployment | Bolt]] is an online directory <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Directories are considered a good way to gain SEO traffic, which can then be evolved into a product <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Initial Prompt and Concept
The concept for the directory was inspired by Product Hunt, aiming to create a directory of products for Indie Hackers, Builders, and Bootstrapped Founders <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The goal is to provide a trusted source for products that enhance productivity and ease of life <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

The initial prompt to [[introduction_to_bolt_and_its_capabilities | Bolt]] described the target audience and the high-level product idea <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. It's often helpful to describe the "vibe" or "aesthetic" desired for the application <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The desired functionality included a main page showcasing "five products you need to have a look at today" and individual product pages for SEO optimization <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Such a directory could eventually monetize through affiliate deals <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

Using longer, descriptive prompts, especially initially, can help [[introduction_to_bolt_and_its_capabilities | Bolt]] generate better marketing copy and names for the product <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Generation and Initial Preview
[[introduction_to_bolt_and_its_capabilities | Bolt]] quickly generated the codebase, performing actions like `npm install` and writing files <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. The first generation may take a moment as it writes all necessary files <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

[[challenges_and_troubleshooting_while_using_bolt | Bolt]] automatically pulls royalty-free images from providers like Unsplash, providing a visually appealing design out of the box <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. The generated directory, "Essential Tools for Indie Hackers," included a list of products and individual product pages <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Troubleshooting and Iteration
During the build, an error occurred because the AI made a "dumb mistake" by not escaping a quote in the code, preventing compilation <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. When errors happen, users can copy and paste the error message into the chat, and [[challenges_and_troubleshooting_while_using_bolt | Bolt]] will attempt to resolve it <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

For design and functionality changes, it's recommended to break them into distinct, smaller prompts <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. [[challenges_and_troubleshooting_while_using_bolt | Bolt]] includes an "undo" button to revert to a previous working state if a change is undesirable <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

Requested design and functionality updates for the directory included:
*   Vertically listing products instead of horizontally <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   Adding gamification by showing product rankings (number one, number two, etc.) <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
*   Allowing users to upvote products <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   Adding "Pops of color" and "beautiful color gradients" to the design <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. The user even provided a screenshot of the Arc browser's website for color inspiration <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.

[[introduction_to_bolt_and_its_capabilities | Bolt]] successfully incorporated these changes, including the upvoting mechanism and adopting the requested color palette and aesthetic <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

### Deployment
One of [[utilizing_bolt_for_ai_model_integration_and_application_development | Bolt]]'s key features is its built-in deployment to production hosts like Netlify <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. By clicking a "deploy" button, [[utilizing_bolt_for_ai_model_integration_and_application_development | Bolt]] performs a production build and provides a real URL for the application <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This allows users to share the link or attach a custom domain, enabling SEO ranking <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. The entire build and upload process happens directly in the browser <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

## Building a Chat Application

To demonstrate more complex functionality, a live chat page was added to the existing directory site <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>. The prompt requested a page for Indie Hackers to communicate in real-time with one another <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>.

### Firebase Integration
For real-time data storage and synchronization, Firebase (or Supabase) is recommended due to its built-in authentication and real-time capabilities that integrate well with [[introduction_to_bolt_and_its_capabilities | Bolt]] <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

Integrating Firebase involved:
1.  Creating a Firebase project and a Realtime Database (or Firestore) <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.
2.  Setting the database to test mode for quicker prototyping <a class="yt-timestamp" data-t="00:35:26">[00:35:26]</a>.
3.  Locating and inserting Firebase API keys into the application's configuration <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>. (Note: Locating the keys within Firebase can sometimes be non-obvious, requiring the creation of a web app within Firebase project settings <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>.)
4.  Troubleshooting a potential dev server restart issue or pop-up blocker interfering with authentication <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.
5.  Temporarily removing the sign-in requirement to simplify testing <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.

For functional changes, it's crucial to be conservative and add minimal functionality at a time to ensure reliability and ease of debugging <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>.

After successful integration and deployment, users could chat in real-time across different locations <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

## Bolt vs. Cursor

[[introduction_to_bolt_and_its_capabilities | Bolt]] is often compared to Cursor AI <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While Cursor is a powerful tool for engineers working with complex, decades-old codebases (e.g., Fortune 500 companies), [[introduction_to_bolt_and_its_capabilities | Bolt]] is designed for simplicity and ease of use, particularly for non-developers and entrepreneurs <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

[[introduction_to_bolt_and_its_capabilities | Bolt]]'s core advantage lies in abstracting away the underlying code, allowing users to interact with the AI agent at a higher, more conceptual level <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. This means users don't need to clone repositories or manually install dependencies to start building <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

For building full-stack web applications, including those with backend features like authentication (Stripe, Supabase, Firebase), [[introduction_to_bolt_and_its_capabilities | Bolt]] is highly effective <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>. While Cursor can build any software, [[introduction_to_bolt_and_its_capabilities | Bolt]] excels in the speed and simplicity of web app development <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>.

## Use Cases and Success Stories

[[building_a_prototype_with_bolt_for_nontechnical_users | Bolt]] is particularly beneficial for:
*   **Micro-SaaS builders** <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **Indie Hackers** <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.
*   **Individuals bootstrapping side projects** <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
*   **YC startups** building landing pages to focus on their core product <a class="yt-timestamp" data-t="00:49:14">[00:49:14]</a>.

One success story highlights a user from Thailand who built "Viral Hooks," an app for generating viral content hooks, entirely with [[utilizing_bolt_for_ai_model_integration_and_application_development | Bolt]] <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This individual was previously quoted thousands of dollars and months of development time by Upwork freelancers <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>. By using [[utilizing_bolt_for_ai_model_integration_and_application_development | Bolt]], she built the app in a week and a half for a monthly subscription, demonstrating a significant reduction in cost and time <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>.

The ability to generate professional-looking applications quickly provides a significant "arbitrage opportunity" for creative, entrepreneurial individuals, especially those who may not be seasoned engineers <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.

## Getting Started with Bolt

To begin building with [[introduction_to_bolt_and_its_capabilities | Bolt]], visit bolt.new <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Users can simply type their ideas into an input box to start the development process <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>. Additional resources include tutorials on the Stack Blitz YouTube channel (e.g., "How to add a database to your bolt.new app" <a class="yt-timestamp" data-t="00:44:16">[00:44:16]</a>), and Stack Blitz's presence on X (@stackblitz) and Discord (discord.gg/stackblitz) <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>.