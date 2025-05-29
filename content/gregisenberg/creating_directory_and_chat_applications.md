---
title: Creating directory and chat applications
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

Bolt is presented as a powerful tool for [[creating_applications_and_websites_with_minimal_coding | creating applications and websites with minimal coding]] and getting ideas to market quickly <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Eric, the founder of StackBlitz (the maker of Bolt), demonstrated how to build applications live using the platform <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The demonstration emphasized that users can start building without prior preparation, mirroring how many entrepreneurs approach their ideas <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Building an Online Directory

A suggested project for Bolt was an online directory, recognized as a valuable way to generate SEO traffic and evolve into a product <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Idea and Target Audience
The chosen directory idea was a product directory similar to Product Hunt <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. It would curate products for [[Indie hackers and Builders and Boot Shop Founders | Indie hackers]], builders, and bootstrap founders, aiming to provide a trusted source for tools to make their lives easier and more productive <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. The directory could eventually lead to affiliate deals with listed products <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Prompting Strategy
When prompting Bolt, it's beneficial to describe the "vibe" or "spiritual level" of the desired output, in addition to concrete functionalities <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. This allows the AI to generate marketing copy that aligns with the target audience <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. For the directory, the request included:
*   A main page displaying five essential products <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   Individual product pages for SEO optimization <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Initial Build and Challenges
Bolt can quickly generate a real codebase, including `npm install` and file creation <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. During the initial build, an error occurred because the AI made a mistake in escaping a quote in the code <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. The solution was to copy and paste the error message directly into the chat for Bolt to attempt a fix <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Bolt also automatically pulls royalty-free images from sources like Unsplash <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

### Iterative Design and Functionality
After the initial build, further design and functionality requests were made:
*   **Vertical Listing**: Changing the product display from horizontal to vertical <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Gamification**: Displaying product ranks (number one, number two, etc.) and allowing users to upvote products <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Design Aesthetics**: Adding "pops of color" and capturing the "vibe" of a specific website (e.g., Arc Browser) <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. Images can be used as design inspiration <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. This iterative approach allows for changes, with an "undo" button to revert to previous checkpoints if results are unsatisfactory <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. Breaking down complex requests into smaller, focused prompts is recommended for functionality changes <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

### Deployment
Bolt offers built-in deployment to Netlify, providing a real URL for the application <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. The build process occurs directly in the browser, eliminating the need for local setup or login <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>. This allows users to start getting Google SEO rankings for their site <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.

## Comparison: Bolt vs. Cursor
Bolt is significantly simpler for non-developers compared to Cursor <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. While Cursor provides an IDE-like interface with code, Bolt focuses on a higher-level, simpler discussion with the AI agent <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. Although Cursor can build any type of software and handle heavyweight codebases (like those at Fortune 500 companies) <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>, Bolt excels at rapidly building and deploying full-stack web applications <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. Bolt users have successfully launched real products with backend functionality, accepting Stripe payments and using Supabase for authentication <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.

## Building a Chat Application
To demonstrate building a more complex application, a live chat page was added to the existing directory site, allowing Indie hackers to communicate in real-time <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.

### Backend and Challenges
Firebase was chosen as the backend for its built-in authentication and real-time data storage capabilities, making it ideal for Bolt <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.

Challenges encountered during chat implementation:
*   **Firebase Configuration**: Difficulty in finding the Firebase API keys and understanding the need to create a web app within Firebase to obtain them <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>.
*   **Dev Server Restart**: The LLM sometimes forgot to restart the development server after making changes <a class="yt-timestamp" data-t="00:36:15">[00:36:15]</a>.
*   **Environment Variables**: The AI attempted to move hardcoded variables into an `.env` file for production best practices, which required manual adjustment <a class="yt-timestamp" data-t="00:45:13">[00:45:13]</a>.

To debug, it was advised to remove authentication temporarily to simplify the process and get the core functionality working first <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>. A helpful tutorial on using Firebase with Bolt is available on YouTube <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.

## Real-World Success with Bolt
Bolt provides significant leverage for creative and entrepreneurial individuals <a class="yt-timestamp" data-t="00:48:39">[00:48:39]</a>. An example is the "Viral Hooks" app, built entirely with Bolt by a user in Thailand. This app was built in about a week and a half for $50/month, compared to an Upwork quote of $3-5k and several months for traditional development <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>. Y Combinator startups have also used Bolt to build professional-looking landing pages, freeing their engineers to focus on core product development <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>.

## Getting Started with Bolt
To start building with Bolt, users can visit bolt.new <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. The platform encourages users to type in their ideas, from simple to complex, and observe the rapid creation of functional web applications <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>. Additional resources are available via the StackBlitz X (formerly Twitter) account (@stackblitz) and their Discord server (discord.gg/stackblitz) <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.