---
title: Using VZ for web development
videoId: sCFS_U7d9Do
---

From: [[gregisenberg]] <br/> 

VZ is an AI assistant developed by [[overview_of_vercel_and_vz | Vercel]], specifically designed to aid in web development <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Its primary goal is to simplify the process of getting high-quality web products by assisting with JavaScript, HTML, CSS, and various new frameworks, tools, and libraries <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. VZ can help with both user interface (UI) and backend work, including adding interactivity to applications <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Getting the Most Out of VZ

To maximize VZ's capabilities, users can employ several strategies:

### Starting with Visuals
Beginning with screenshots is highly effective <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. If you have an idea of what you want (e.g., a Spotify-like UI), providing a visual reference helps VZ understand your taste and opinion <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Alternatively, if you're unsure, you can let VZ generate initial designs and then refine them iteratively <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. For instance, a one-shot component for a link-to-Slack integration was created without specific UI instructions <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### Iterative Prompting and Design Refinement
VZ thrives on iterative feedback. Users can continuously refine designs by:
*   **Giving specific aesthetic instructions**: Examples include "make it have warmer Grays," "use a Sanda font," or specifying "from Google fonts with next font" for proper import <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>, <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Adjusting information density**: "make the UI have a tighter information density" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Detailing component behavior**: "the time playing bar should be longer," "the search input should have an actual input in it" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Providing realistic data**: "add more realistic fake data for the songs" <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Using Tailwind CSS terminology**: VZ "thinks in Tailwind" <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Explicitly stating Tailwind classes like "make it size four" can steer the assistant precisely <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Applying CSS properties**: Suggesting specific CSS properties, such as `tabular-nums` for vertical alignment of numbers, can ensure precise design outcomes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>, <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Implementing mobile responsiveness**: Simply asking "make the table mobile responsive" can initiate the process, followed by further refinement for optimal display on smaller screens <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Using natural language**: Phrases like "hm that now playing bar is pretty wide like I would probably make that less" mimic human communication with a designer <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Leveraging images**: Uploading and pasting images allows VZ to incorporate them into designs, significantly enhancing the visual appeal <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. High-quality imagery is crucial for web design <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Forking projects**: Users can "fork" existing projects to experiment with new colors, fonts, or general vibes for different pages within an application <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>, <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

### Incorporating Existing UI Patterns
VZ is built on top of Shad CN UI, a system that allows users to build their own component libraries <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This means VZ generates real React components using production-grade technology, preventing the need for later re-architecture <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Shad CN UI provides common UI patterns like mail apps, dashboards, and music players <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. Users can fork these components within VZ and customize them to fit their brand <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. VZ understands this language, allowing prompts like "give me a component for the date picker" <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

### Backend Integration
Beyond UI, VZ can assist with backend development:
*   **Implementing UI elements with logic**: Once a UI is styled, users can ask VZ to implement the underlying logic <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
*   **Data integration**: VZ can fetch data from external APIs or connect to databases by understanding database schemas <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   **ORM generation**: VZ can generate Object-Relational Mapping (ORM) code for various languages (e.g., Drizzle or Prisma for JavaScript/TypeScript, Rails or Laravel for other languages) based on a Postgres schema <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.
*   **Database design**: Users can describe desired tables (e.g., "a table for users and emails") and VZ can help design the backend and suggest optimizations like using indexes for faster queries <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>, <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>.

### Learning and Developing Taste
For those new to design or web development, VZ can act as a learning tool <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. Users can ask VZ questions like "I am a novice at design, what can I try to make things look a little better? Any common practices or patterns?" <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. VZ can provide guidance on:
*   Consistent color schemes (2-3 main colors, often via Tailwind's design system) <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   White space, padding, and margins <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
*   Readable fonts (e.g., sans-serif fonts) <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   Layout alignment and organization <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   Use of high-quality images <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   Animation principles (e.g., easing functions, duration) <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.

Users can also seek external inspiration from sites like [godly.website](https://godly.website) or [patterns.dev](https://patterns.dev) for design ideas and patterns to feed into VZ <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## VZ as an Augmentation Tool
VZ, like other AI tools, is not a replacement for human developers but an augmentation <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. It acts as a "knowledgeable super senior engineer" that can provide best practices and answer questions, making the development process faster and more efficient <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. This allows [[exploring_the_potential_of_developer_tools | builders]] to create whatever they can imagine, from web to iOS or Android apps, by leveraging AI's knowledge of various languages and frameworks <a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>.

> "Once you get that mindset you realize right now more than any other time in history there's you can build whatever you want you have all of the power now with these tools" <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.

## Try VZ
VZ offers a free tier for users to experiment with <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. You can try it at [vz.dev](https://vz.dev) <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>.