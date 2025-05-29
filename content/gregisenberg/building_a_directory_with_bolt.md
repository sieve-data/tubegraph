---
title: Building a directory with Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

[[Introduction to Bolt | Bolt]] is presented as a powerful tool for quickly bringing ideas to market, even being called a "Cursor AI killer" by some <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Eric, the founder of Stack Blitz (the maker of [[Introduction to Bolt | Bolt]]), demonstrated how to use the product by building a directory live <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This hands-on approach helps identify areas for improvement in the product <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Why Build a Directory?
A directory is highlighted as an excellent way to generate significant SEO traffic, which can then be evolved into a full product <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The concept of [[Using AI for building directories | building a directory]] similar to Product Hunt was suggested <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Such a directory could focus on products for Indie hackers, Builders, and Boot Shop Founders, providing a trusted source for tools to enhance productivity <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. Eventually, this can lead to affiliate deals with listed products, creating a viable business model <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## Initiating the Build Process
The process begins by clearly defining the project to [[Introduction to Bolt | Bolt]]. This involves describing the target audience and the overall "vibe" or aesthetic <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. For example, a directory for Indie hackers seeking tools would be described as "a directory of great products for Indie hackers and Builders who are looking for products to make their lives easier and more productive, and they want a trusted source" <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

It's helpful to then specify the desired functionality, such as:
*   A main page displaying five key products for the day <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   Individual product pages that users can click into, which serve as additional SEO-optimized content <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

This detailed prompting helps [[Introduction to Bolt | Bolt]] generate appropriate marketing copy and structure <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. [[Introduction to Bolt | Bolt]] is capable of rapidly creating a real codebase, including installing npm packages and writing necessary files <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. It can also automatically pull royalty-free images from sources like Unsplash <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Prompting Strategy
While a long prompt can be effective, it's often beneficial to use "small, focused prompts" for specific tasks <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. For example, when making design changes, a list of improvements can be given <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>. For adding functionality, it's better to be conservative and add minimal features one at a time <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

## Handling Errors and Iteration
Sometimes, [[Introduction to Bolt | Bolt]] may encounter errors during the generation process <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. To resolve these, you can copy and paste the error message directly into the chat, and the AI will attempt to fix it <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. For example, a syntax error like an unescaped quote can be corrected this way <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

[[Prototype creation with Bolt new | Bolt]] also includes an "undo" button, which allows users to revert to the last working checkpoint if a generated change is undesirable <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

## Adding Gamification and Design Elements
To make the directory more engaging, gamification elements can be added. This was demonstrated by adding the ability for users to upvote products, with a visible vote count next to each item <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. The idea was to allow unlimited upvoting to create large, active vote counts, making the directory feel more "alive" <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

For design, users can provide inspiration, even by uploading screenshots or referencing external sites like the Arc Browser website <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>. [[Introduction to Bolt | Bolt]] can capture the "vibe" and apply color palettes and aesthetic elements from the inspiration <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

## [[Design and deployment with Bolt | Deployment and Troubleshooting with Bolt]]
[[Deployment and troubleshooting with Bolt new | Bolt]] offers built-in deployment to production hosts like Netlify <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. With a single click of the "deploy" button, [[Introduction to Bolt | Bolt]] performs a production build and generates a real URL <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>. This allows users to share the link, attach a custom domain, and benefit from Google SEO ranking <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>. The build and deployment process happens directly in the browser, without needing to log in <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.

## Extending Functionality: Live Chat Example
[[Using Bolt for web app development | Bolt]] is not limited to UI; it can also create backend functionalities <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>. A demonstration included adding a live chat page to the directory, enabling real-time communication among Indie hackers <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.

For chat functionality, [[Integrating Firebase with Bolt | Firebase]] (or Supabase) is recommended due to its built-in authentication, real-time data storage, and synchronization capabilities <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

When integrating external services like Firebase:
*   Sometimes the AI forgets to restart the dev server, which can be manually triggered with `npm run Dev` <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
*   Firebase configuration credentials need to be replaced with actual keys for deployment, often found in project settings after creating a web app within Firebase <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>.
*   Initial setup can be done in "test mode" to quickly get functionality working, with proper database permissions added later for production <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   If authentication issues arise (e.g., "need to sign in to chat"), the requirement to sign in can be temporarily removed via a prompt to streamline testing <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.

Once deployed, the live chat functionality allows users to communicate across different locations in real-time, demonstrating [[Using Bolt for web app development | Bolt]]'s ability to create interactive web applications <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.

## Real-world Examples and Benefits
[[Bolt new tool overview | Bolt]] enables non-developers and entrepreneurs to build and launch real products quickly. For instance, an app called "Viral Hooks" was built entirely with [[Introduction to Bolt | Bolt]] in about a week and a half for a cost of $50/month, whereas a developer quote for the same app was $3,000-$5,000 and several months <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>.

Even YC startups have used [[Introduction to Bolt | Bolt]] to build professional-looking landing pages in 30 minutes, freeing up their engineers to focus on core product development <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>. This highlights the significant "arbitrage opportunity" for creative, entrepreneurial individuals who can effectively use AI tools <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>.

## Getting Started with Bolt
To begin [[Prototype creation with Bolt new | prototyping with Bolt]], visit bolt.new <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Users can type in their ideas into an input box and hit enter <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>. Additional tutorials and updates can be found by following @stackBlitz on X or joining their Discord at discord.gg/stackblitz <a class="yt-timestamp" data-t="00:51:55">[00:51:55]</a>. A specific tutorial on [[Integrating Firebase with Bolt | how to add a database to your Bolt.new app]] is also available on YouTube <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>.