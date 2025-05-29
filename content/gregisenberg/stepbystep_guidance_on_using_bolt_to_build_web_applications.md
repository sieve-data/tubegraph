---
title: Stepbystep guidance on using Bolt to build web applications
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

[[Introduction to Boltnew | Bolt]] is a tool designed to help users bring their ideas to market quickly, particularly for web applications <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Developed by StackBlitz, Bolt allows users to build and deploy full-stack web apps efficiently <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a> <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. This guide outlines the process of [[Building a prototype with Boltnew | building a prototype]] and adding features using Bolt, as demonstrated by founder Eric.

## Getting Started with Bolt

To begin, users interact with Bolt through a chat interface, describing their desired application <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Crafting Your Prompt
It's beneficial to describe the project at a "spiritual level," conveying the overall vibe and target audience, followed by specific functionalities <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

An example of a detailed prompt structure:
1.  **High-Level Target Audience**: Who is the product for? <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
2.  **High-Level Product Description**: What is the core purpose of the product? <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>
3.  **Specific Functionality**: What exact features should it include? <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>

This detailed approach helps Bolt generate good marketing copy for the application's descriptions and calls to action (CTAs) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Prompt Enhancer
For more specific and deterministic results, Bolt offers a "Prompt Enhancer" feature (a sparkly icon at the bottom of the chat) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Clicking this sends the current prompt to the AI model, which then expands it with extra details, helping to scaffold a very specific prompt <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

## Building a Directory Site

As a first example, a directory site for Indie hackers was chosen, similar to Product Hunt, focusing on products that make their lives easier and more productive <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a> <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Initial Generation
Bolt rapidly generates the code base, installing necessary packages and writing files <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This process is significantly faster than local development <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

### Handling Errors
Occasionally, errors may occur. For example, the AI might make a "dumb mistake" like not escaping a quote <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. When a "fix errors" button doesn't automatically appear, users can copy and paste the error message directly into the chat, and Bolt will attempt to resolve it <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a> <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Initial Output & Design
The initial directory, titled "Essential Tools for Indie Hackers," included product listings with descriptions and images <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. Bolt automatically pulled royalty-free images from sources like Unsplash <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Enhancing Functionality and Design

#### Gamification and Upvoting
To enhance the directory, features like vertical listing, showing product rankings (Number 1, Number 2, etc.), and allowing users to upvote products were requested <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a> <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a> <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. This quickly transformed the site, adding a "game-like" feel <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. The upvoting feature was implemented, initially storing votes in memory, but could be integrated with Firebase or Supabase for persistent storage <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a> <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

#### Visual Design
Users can provide design feedback by describing desired aesthetics, such as "pops of color" or "gradients" <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a> <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. Bolt can also interpret visual inspiration by taking a screenshot of a reference site (e.g., Arc Browser) and applying its color palette and vibe to the generated application <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a> <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.

## [[Deployment challenges with Boltnew | Deployment]]
A key feature of Bolt is its [[Deployment challenges with Boltnew | built-in deployment]] to production hosts like Netlify <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

*   Simply click the "deploy" button in the top right <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.
*   Bolt performs a production build and provides a real URL <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.
*   This allows users to share the link, attach custom domains, and benefit from SEO ranking <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a> <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.
*   The build is done directly in the browser and uploaded to Netlify without requiring a separate login <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

## Building a Chat Application
As a more complex example, a live chat page for Indie hackers was added to the existing directory site <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.

### Backend Integration
For real-time functionality, a backend database is required. While Bolt will suggest providers, Firebase and Supabase are often recommended due to their built-in authentication, real-time data storage, and synchronization capabilities <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a> <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

### Troubleshooting and Best Practices
*   **Restarting Dev Server**: Sometimes, the AI might forget to restart the development server after making changes. Users can manually prompt it to do so (e.g., "restart the dev server") <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
*   **Firebase Configuration**: Accessing Firebase API keys requires creating a web app within the Firebase project settings <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a> <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>. These credentials then need to be populated in the Bolt project's configuration <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>.
*   **Iterative Development**: When adding complex functionality like a chat, it's best to start with minimal requirements and gradually add features <a class="yt-timestamp" data-t="00:40:44">[00:40:44]</a>. For instance, temporary removal of authentication allows for faster prototyping <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>. This "one feature at a time" approach minimizes potential issues <a class="yt-timestamp" data-t="00:40:45">[00:40:45]</a>.
*   **Firebase Database Types**: Firebase offers both Realtime Database and Firestore. It's important to be aware of which one the AI uses and if it aligns with your preference <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>.

## [[Comparison between Bolt and other development tools like Cursor | Bolt's Advantages]]
Bolt is simpler to use than tools like [[Comparison between Bolt and other development tools like Cursor | Cursor AI]], especially for non-developers <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. While Cursor is a heavyweight tool for complex codebases and Fortune 500 companies <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>, Bolt focuses on abstracting away the code and providing a more powerful, high-level discussion with the AI agent <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a> <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.

Bolt allows users to build full-stack web apps with features like backend integration, authentication, and payment processing (e.g., Stripe for subscriptions) <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a> <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.

### [[Reallife examples of products built using Bolt | Real-Life Examples]]
*   **Viral Hooks by Pitch**: A user from Thailand built an app to help create viral hooks for TikTok posts entirely with Bolt <a class="yt-timestamp" data-t="00:47:08">[00:47:08]</a>. This project, quoted at $3-5K and several months by traditional developers, was built in about two weeks for $50/month using Bolt <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a> <a class="yt-timestamp" data-t="00:48:19">[00:48:19]</a>.
*   **YC Startups**: Some Y Combinator (YC) startups have used Bolt to build their landing pages, saving their engineers time to focus on core product development <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>.

These examples highlight the significant time and cost savings offered by Bolt, providing immense [[Benefits of using Boltnew for nontechnical users | leverage for creative and entrepreneurial individuals]] <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a> <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>. Bolt also emphasizes the ability to build web apps directly in the browser, similar to how one would use Figma for design or Google Docs for writing <a class="yt-timestamp" data-t="00:50:40">[00:50:40]</a>.

## Getting Started with Bolt
To begin using Bolt, visit [bolt.new](https://bolt.new) <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Simply type your idea into the input box and hit enter <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>.

**Resources:**
*   **Firebase Integration Tutorial**: Search for "how to add a database to your bolt.new app" on YouTube <a class="yt-timestamp" data-t="00:44:16">[00:44:16]</a>.
*   **X (Twitter)**: Follow @stackblitz for updates <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.
*   **Discord**: Join the community at [discord.gg/stackblitz](https://discord.gg/stackblitz) <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a>.