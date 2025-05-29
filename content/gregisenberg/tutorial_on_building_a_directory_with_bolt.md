---
title: Tutorial on building a directory with Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

This article provides a tutorial on building an online directory using [[introduction_to_boltnew | Bolt]], a tool designed to rapidly bring ideas to market <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Eric, the founder of Stack Blitz (the maker of Bolt), demonstrates the process live, showcasing its capabilities for [[using_boltnew_for_rapid_prototyping | rapid prototyping]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Starting the Directory Project

The goal is to build an online directory, which is an excellent way to gain SEO traffic and evolve into a product <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The initial idea was to create a directory of products for Indie hackers, Builders, and Bootstrapped Founders, aiming to provide a trusted source for tools that enhance productivity <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Crafting the Initial Prompt

When using Bolt, it's beneficial to describe the project at a "spiritual level," conveying the desired vibe and target audience <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
The initial prompt was formulated to capture this essence, followed by more specific functionality requests <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

The prompt included:
*   **Audience:** Indie hackers, Builders, Bootstrapped Founders <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Purpose:** Looking for products to make their lives easier and more productive, seeking a trusted source <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Structure:** One main page featuring the top five "products of the day," with individual product pages for SEO optimization <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Monetization:** Potential for affiliate deals with featured products <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

The AI then started generating the code base, performing `npm install` and writing files <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Handling Initial Issues

An error occurred during the first generation due to an unescaped quote in the code <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Bolt allows users to copy and paste the error message directly into the chat, and the AI will attempt to fix it <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

Bolt is trained to pull royalty-free images from sources like Unsplash to provide visuals out of the box <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

The initial output successfully created an "Essential Tools for Indie Hackers" directory with appropriate marketing copy based on the initial prompt's "essence" <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. It included a main page and clickable product pages <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

## Refining Design and Adding Gamification

To enhance the directory, further modifications were requested:

*   **Layout Change:** Display products vertically instead of horizontally <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Gamification:** Implement a ranking system (e.g., "Product of the day #1, #2, #3") and allow users to upvote products <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This aligns with frameworks like Octalysis, which turns products into games with leaderboards, status points, and achievements <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

It's often good to break down prompts into distinct blocks for functionality and design <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This allows for using the "undo" button to revert changes if a specific modification doesn't work, without losing other correct changes <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

The result was a more game-like feel with an upvoting system <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. Initially, the upvoting allowed unlimited clicks, which could make the vote counts feel more "alive" <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

### Applying Design Inspirations

To add "pops of color" and a more "beautiful" aesthetic <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>, Bolt can take image inspiration. A screenshot of the Arc Browser site was provided, with a request to capture its "vibe" and colors <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

Bolt successfully integrated the color palette and added icons, creating a calming and unique design <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This highlights Bolt's ability to interpret abstract design "vibes" and apply them to the product <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

## Deployment to Production

One of Bolt's key [[features_and_challenges_of_boltnew | features]] is its built-in deployment capability. It allows users to deploy their application to Netlify directly from the browser <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

The process involves:
1.  Clicking the "deploy" button <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.
2.  Bolt performs a production build and uploads it <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.
3.  A real URL is generated, which can be shared or linked to a custom domain for SEO <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
4.  No login is required for this deployment, as the build happens in the browser <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

## Adding a Chat Feature (Micro SaaS Example)

To demonstrate more complex functionality, a live chat page for Indie hackers was added to the directory <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.

### Integrating Firebase

When adding backend functionality, Bolt recommends using providers like Firebase or Superbase due to their built-in authentication and real-time data synchronization <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

The process involved:
1.  **Prompting:** Requesting a live chat page using Firebase <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.
2.  **Firebase Setup:** Creating a new project ("Indie hacker chat") in the Firebase console and enabling the Realtime Database in test mode <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>. Test mode simplifies prototyping by relaxing permissions, which can be secured later for production <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
3.  **API Keys:** Locating Firebase API keys, which required navigating through project settings and creating a web app within Firebase <a class="yt-timestamp" data-t="00:39:11">[00:39:11]</a>. These keys were then copied and pasted into Bolt's configuration file <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>.
4.  **Debugging Dev Server:** Occasionally, the LLM might forget to restart the development server. A manual `npm run dev` command can fix this <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
5.  **Authentication Bypass:** For quick testing, the requirement to sign in to chat was temporarily removed <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>. This highlights the strategy of adding one feature at a time, starting with simple functionality before adding complexity <a class="yt-timestamp" data-t="00:40:58">[00:40:58]</a>.
6.  **Testing Chat:** The chat functionality was successfully tested in real-time between two users <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>. The chat data was stored in Firebase Firestore, and later directed to the Realtime Database for proper persistence <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>.
7.  **Deployment:** The updated app with the chat feature was deployed again <a class="yt-timestamp" data-t="00:44:39">[00:44:39]</a>. A minor issue with Bolt attempting to create an `.env` file (which is good practice for production but needs locking in the tool) was noted <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>.

For more detailed guidance on adding databases to Bolt, a tutorial by Tomac on how to use Firebase with Bolt is available <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>.

## Conclusion

Bolt allows users to go from an idea to a deployed production application rapidly <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>. It is notably simpler than tools like [[comparison_of_bolt_and_other_platforms_like_cursor | Cursor]] for non-developers, as it focuses on high-level discussion with the AI rather than directly exposing the code as the default view <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. Despite its simplicity, Bolt is powerful enough to build full-stack web applications with features like authentication and payment integrations (e.g., Stripe, Superbase) <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>.

Many "Indie hackers" and "micro SaaS" builders are adopting Bolt, successfully launching products and acquiring their first customers <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a> <a class="yt-timestamp" data-t="00:50:15">[00:50:15]</a>. An example is "Viral Hooks" by Pitch from Thailand, which was built with Bolt in a week and a half for a fraction of the cost quoted by developers <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. Even YC startups use Bolt for building landing pages, freeing their engineers for core product development <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>.

To get started with Bolt, visit [bolt.new](https://bolt.new) <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. You can also follow Stack Blitz on X (@stackBlitz) and join their Discord community (discord.gg/stackblitz) for more tutorials and support <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>.