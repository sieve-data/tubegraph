---
title: Live product demonstration with Eric Simons
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

Eric Simons, founder of Stack Blitz and the creator of Bolt, conducted a live demonstration of his product, showcasing its capabilities for rapidly developing and deploying web applications <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This was one of the first times Simons publicly demonstrated how to use Bolt <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. He approached the demonstration completely unprepared, mirroring the typical user experience <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Simons also shared debugging tips and insights into the product's underlying structure <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Building a Product Directory

The first project undertaken was a product directory similar to Product Hunt, aimed at Indie hackers, builders, and bootstrap founders seeking tools to enhance productivity <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The directory was envisioned as a single main page displaying the top five products of the day, with individual product pages for SEO optimization <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This type of directory can eventually lead to affiliate deals with featured products <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

Simons explained his prompting strategy, which involves describing the target audience and product essence at a "spiritual level" before detailing specific functionality <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This approach helps the AI generate good marketing copy for product names and descriptions <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

The initial generation process with Bolt is fast, creating a real codebase with all files and dependencies installed <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Bolt also includes a "Prompt Enhancer" feature, which expands initial prompts with additional details to make the AI's output more deterministic <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

During the build, an error occurred because the AI failed to escape a quote in the code <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. Simons demonstrated how to fix this by simply copying and pasting the error message into the chat, allowing Bolt to attempt a solution <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Bolt is trained to pull royalty-free images from Unsplash and other providers, which are included out of the box <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

The generated directory, named "Essential Tools for Indie Hackers," successfully conveyed the intended audience and product purpose <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Adding Gamification and Design

To enhance the directory, the team decided to add gamification elements, including displaying product rankings (number one, number two, etc.) and allowing users to upvote products <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Simons suggested breaking down complex requests into distinct blocks to allow for easier rollback using the undo button if a specific change isn't desired <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

The implemented upvoting feature initially allowed unlimited votes, which was seen as a potential benefit to create a sense of activity and value <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

For design, the request was to add "pops of color" and "beautiful color gradients," capturing the "vibe" of inspiring sites like Arc Browser or Late Checkout Studio <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. Bolt was able to capture the color palette and add visual elements like icons and shadows from the provided image inspiration <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.

## Deployment and Real-time Capabilities

A key feature of Bolt is its integrated deployment to production hosts like Netlify <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. By clicking a single "deploy" button, Bolt performs a production build and provides a real URL, allowing users to share the link or attach a custom domain for SEO ranking <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>. The entire build process occurs in the browser without requiring a local login <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.

## Comparison with Cursor and Building a Chat App

Bolt is simpler for non-developers compared to tools like Cursor, as it prioritizes a high-level discussion with the AI agent over direct code interaction <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. While Cursor is a powerful tool for large, decades-old codebases, Bolt excels at rapidly building full-stack web applications, including features like authentication and payment processing <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. Users have launched real products with Bolt, integrating services like Stripe for subscriptions and Supabase for authentication <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>.

To demonstrate more complex functionality, a live chat page was added to the directory site for Indie hackers to communicate in real time <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>. For real-time applications, Eric recommended using Firebase or Supabase due to their built-in authentication and real-time data synchronization <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

When integrating external services like Firebase, users typically need to configure API keys. During the demo, Simons encountered an issue locating the Firebase API keys, highlighting a potential area for improvement in external service onboarding and the need to follow specific steps like creating a web app within Firebase <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>. He leveraged Claude, an AI, to find the necessary steps <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>.

A common debugging strategy, especially for non-developers or when dealing with complex features like chat, is to incrementally add functionality and ensure each step works before moving to the next <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.

Once the Firebase configuration was resolved, the chat functionality was live and persistent, allowing users to send messages in real-time across different devices <a class="yt-timestamp" data-t="00:44:36">[00:44:36]</a>. A tutorial on how to use Firebase with Bolt is available <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.

## Real-world Impact and Future Vision

Bolt provides significant leverage for creative, entrepreneurial individuals to build and launch products quickly <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>. An example shared was "Viral Hooks," an app built entirely with Bolt by a user who was previously quoted thousands of dollars and months of development time by contractors <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This user built her app in a week and a half or two weeks for a $50/month plan, achieving a 100x cost reduction and 5-10x faster development <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>.

YC startups have also used Bolt to build landing pages, allowing their engineers to focus on core product development <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>. Numerous Bolt users have already secured their first customers or dozens of customers after launching their products <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>.

The core vision behind Stack Blitz and Bolt is to enable people to build web applications using only the web, without needing to download software to their computers <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.

To start using Bolt, users can visit bolt.new, enter their idea, and hit enter <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Updates and tutorials are available on X (@stackBlitz) and Discord (discord.gg/stackblitz) <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.