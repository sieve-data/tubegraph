---
title: Live tutorial with Bolt CEO Eric Simons
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

Eric Simons, the founder of Stack Blitz and Bolt, provided a live, unscripted demonstration of how to use Bolt to build web applications during a podcast recording <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This was one of the first times Eric had the opportunity to use Bolt meaningfully, as he typically serves as a "Chief bugfinder" for the product <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Bolt has been publicly available for about a month <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Building a Product Directory

The first project undertaken was building a product directory, inspired by the concept of Product Hunt <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The goal was to create a directory of products for Indie Hackers, builders, and bootstrap founders, focusing on tools that make their lives easier and more productive <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>, <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This type of directory can generate significant SEO traffic and can later evolve into a product with affiliate deals <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>, <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Initial Prompt and AI Behavior
Eric demonstrated how to prompt Bolt, starting with a high-level description of the target audience and the product's essence, which helps the AI generate good marketing copy <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The process of generating the initial codebase is very fast, with Bolt installing dependencies and writing files quickly <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

### Handling Errors
During the initial generation, an error occurred because the AI made a "dumb mistake" by not escaping a quote in the code <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>, <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Eric showed that users can simply copy and paste the error message into the chat, and Bolt will attempt to fix it <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Design and Functionality Iterations
After the initial generation, the directory displayed "Essential tools for Indie hackers" <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Bolt also automatically included royalty-free images from Unsplash, which are convenient for immediate visual appeal <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>, <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

Subsequent prompts aimed to refine the design and add functionality:
*   **Vertical Listing**: The products were changed to be listed vertically <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Gamification**: Features were added to show rankings (number one, two, three products) and allow users to upvote products, making it feel more like a game <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>, <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>, <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. The upvote feature was initially unlimited, which could be beneficial for showing high engagement <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
*   **Aesthetic Changes**: To add "pops of color" and "beautiful gradients," Eric uploaded a screenshot of the Arc browser's website to inspire Bolt's design <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>, <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>, <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>, <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. Bolt successfully adopted the color palette and added relevant icons, creating a "calming" and "unique" aesthetic <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>, <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>.

## Deployment with Bolt
Bolt allows for easy deployment to production hosts like Netlify with a single click of the "deploy" button <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>, <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. This process builds the application in the browser and uploads it directly, providing a real URL that can be shared or connected to a custom domain for SEO purposes <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>, <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.

## Bolt vs. Cursor
Bolt is significantly simpler for non-developers compared to tools like Cursor, which presents a more traditional IDE environment <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>, <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>. While Cursor is designed for heavyweight code bases and can build any type of software, Bolt excels at rapidly building and launching full-stack web applications <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>, <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. Users can create applications with backends, authentication (e.g., using Firebase or Supabase), and even integrate with services like Stripe for subscriptions <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>, <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>.

## Building a Live Chat Application
To demonstrate more complex functionality, they attempted to add a live chat page to the product directory site for Indie Hackers to communicate in real-time <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.

### Using Firebase
Eric chose Firebase as the backend for the chat, recommending it or Supabase for their built-in authentication, real-time data storage, and synchronization capabilities with Bolt <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>, <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.
*   **Setup Challenges**: Retrieving Firebase API keys required creating a web app within the Firebase console, which was not immediately obvious <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>, <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>.
*   **Iterative Debugging**: When an error occurred, they opted to temporarily remove the sign-in requirement to simplify debugging and focus on core chat functionality <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>, <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>. This highlights the strategy of adding functionality incrementally <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **Data Persistence**: Initially, chat messages were not persisting because Firebase has two database products (Firestore and Realtime Database), and the Realtime Database was chosen for its familiarity and suitability for real-time applications <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>, <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>.
*   **Live Chat**: After addressing the database configuration, a live chat page was successfully integrated and deployed, allowing the host and Eric to chat in real-time across the country <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>, <a class="yt-timestamp" data-t="00:45:51">[00:45:51]</a>.

## Real-World Impact
Bolt offers significant leverage for creative and entrepreneurial individuals, enabling them to build cool, professional-looking products rapidly and cost-effectively <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>, <a class="yt-timestamp" data-t="00:49:07">[00:49:07]</a>.

### Viral Hooks Example
A notable example is "Pitch" from Thailand, who built an app called Viral Hooks using Bolt <a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>, <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. Before Bolt, she was quoted $3,000-$5,000 and several months by developers on Upwork to build her idea <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>. By subscribing to Bolt's $50/month plan, she built the app in about one and a half to two weeks, achieving the outcome at 1/100th the cost and 5-10 times faster <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>, <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>. This highlights how Bolt empowers "Indie hackers" and "micro SaaS" builders <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>, <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.

Even Y Combinator startups have used Bolt to build landing pages, allowing their engineers to focus on core product development <a class="yt-timestamp" data-t="00:49:14">[00:49:14]</a>, <a class="yt-timestamp" data-t="00:49:44">[00:49:44]</a>. At least a dozen people have already launched products and gained their first customers using Bolt <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>.

## Getting Started with Bolt
To start building with Bolt, users can visit [bolt.new](https://bolt.new) and type in their ideas into the input box <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Additional resources include tutorials on the Stack Blitz YouTube channel (e.g., how to add a database to a Bolt app <a class="yt-timestamp" data-t="00:44:16">[00:44:16]</a>), updates on Stack Blitz's X account (@stackblitz), and the Discord server (discord.gg/stackblitz) <a class="yt-timestamp" data-t="00:51:55">[00:51:55]</a>.