---
title: Vzer product demo and stepbystep guide
videoId: sCFS_U7d9Do
---

From: [[gregisenberg]] <br/> 

Lee, the VP of Product at Vercel, introduces Vzer as an AI assistant specifically designed for web development <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>. The goal of Vzer is to make it as easy as possible to produce high-quality web products using technologies like JavaScript, HTML, CSS, and various frameworks and libraries <a class="yt-timestamp" data-t="01:36:58">[01:36:58]</a>.

## Getting the Most Out of Vzer

Vzer aims to help users build their own things for the web <a class="yt-timestamp" data-t="01:24:60">[01:24:60]</a>. Lee shares insights into how he thinks about maximizing its utility, offering tips and tricks for both design and backend development <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

### Creative Modes

When approaching Vzer, users can operate in two primary creative modes <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>:
1.  **Opinionated Mode**: Users have a clear vision of what they want to build and iterate to achieve that specific design <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
2.  **AI-Driven Mode**: Users don't have a strong opinion and allow the AI to generate initial designs, which they then refine <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

### Starting with Screenshots

A highly effective way to begin with Vzer is by providing screenshots of existing UIs or desired layouts <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. This helps Vzer understand the desired aesthetic and structure, even if the intention isn't to copy the design exactly <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>.

### Frontend and Backend Development

Vzer can be used for both creating great UIs and performing backend work <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. Beyond just making things look nice, Vzer can add interactivity and logic <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. It can help implement API calls, understand database schemas, and even generate ORMs (Object-Relational Mappers) for various programming languages and frameworks <a class="yt-timestamp" data-t="21:04:00">[21:04:00]</a>.

### Vzer Projects

Vzer has a concept of "projects," allowing users to group related chats and iterations for a specific application or feature <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. This enables continued development and refinement within a structured environment.

## Product Demo: Building a Music Player UI

Lee demonstrates an iterative process for building a music player UI similar to Spotify, but with a denser information display <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

*   **Initial Prompts & Refinements**:
    *   Starting with a screenshot, the initial version was functional but lacked the desired design sense <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.
    *   Instructions included using "warmer grays" and a "Sansada font" <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. Vzer knows how to import fonts from Google Fonts using Next.js's font features <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
    *   Requests like "tighter information density," "longer time playing bar," "actual search input," and "more realistic fake data" were added <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
    *   Further refinements included "less vertical spacing between rows," "album art to the left of each row," and adjusting image sizes <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.
*   **Leveraging Tailwind CSS Knowledge**: Vzer "thinks in Tailwind" <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. Users can explicitly provide Tailwind classes (e.g., "make it size four") to precisely control elements <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
*   **Content and Structure**:
    *   Users can upload and paste images for Vzer to use in designs <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
    *   Lee directed Vzer to place artist names in a separate column and use electronic music for placeholder data <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
    *   He also used normal language, like telling it "that now playing bar is pretty wide" <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>, to achieve the desired effect.
    *   Knowledge of CSS properties like `tabular-nums` can be directly leveraged to align numbers vertically <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.
*   **Mobile Responsiveness**: Vzer can make designs mobile responsive by simply asking it to <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. Users can then provide feedback if the responsiveness isn't quite right (e.g., "I can't see the table of songs because the image is so large") <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
*   **Code Generation**: Once a design is satisfactory, it can be forked and broken into components <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>, allowing users to add logic and adjust color schemes <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

## Learning Web Design with Vzer

Even for novices, Vzer can be a powerful learning tool.
*   **Learning by Asking**: If you don't know the right questions, Vzer can help you formulate them <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>. For example, asking "I am a novice at design, I don't really know how to make my design look better but it's just lacking something like what do I have to do to make it look a little bit better?" <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a> will yield valuable advice.
*   **Common Design Practices**: Vzer can suggest common web design practices such as <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>:
    *   Using a consistent color scheme (2-3 main colors) <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.
    *   Implementing white space, padding, and margins for breathability <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.
    *   Using readable fonts, like sans-serif fonts <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.
    *   Ensuring consistent layout, alignment, and organization <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
    *   Prioritizing high-quality images <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>.
*   **Understanding Typography**: Vzer can explain differences between font types, such as Serif and Sans Serif fonts, and monospace fonts <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>.
*   **Developing Taste**: By interacting with Vzer and learning from its suggestions, users can develop their own design taste and apply it more effectively <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>.

## Inspiration and Foundations

*   **Design Inspiration Websites**: Users can look at sites like [godly.website](https://godly.website/) and [patterns.dev](https://www.patterns.dev/) to get inspiration for layouts and elements <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. Screenshots from these sites can be used as starting points in Vzer <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   **Foundation in [[Shad CN UI]]**: Vzer is built on top of [[Shad CN UI]], a system that allows users to build their own component libraries <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
    *   The code generated by Vzer is not "throwaway code"; it produces real React components using production-ready technology <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.
    *   [[Shad CN UI]] provides pre-built UI patterns (e.g., mail app, dashboard app, cards, music player) that can be forked and customized within Vzer to match a brand's unique look <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>.
    *   Vzer understands this language, allowing users to request specific components like a "date picker" <a class="yt-timestamp" data-t="17:07:00">[17:07:00]</a>.

## More Vzer Use Cases

### SaaS Landing Page
Lee demonstrated building a SaaS landing page, iterating from a basic pricing page to a minimal, vertically organized layout <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>. He then added an animated terminal in the hero section and refined its animation speed and font <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>. This ultimately became the actual landing page for his SaaS template <a class="yt-timestamp" data-t="19:32:00">[19:32:00]</a>.

### Logged-in Dashboard View
From the landing page project, Lee forked it to create a logged-in dashboard view with sections for subscription management and user info updates <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>.
*   Vzer generated a UI for basic CRUD (Create, Read, Update, Delete) actions typical of an admin portal <a class="yt-timestamp" data-t="19:58:00">[19:58:00]</a>.
*   The generated mock data for elements like activity logs can be easily swapped out with real API calls or hooked up to a database schema provided to Vzer <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>.
*   Users can ask Vzer to optimize database performance (e.g., suggesting indexes) and provide the correct ORM schema for their application <a class="yt-timestamp" data-t="21:43:00">[21:43:00]</a>.

### Superhuman-Inspired Email Client
Lee also showcased an email client design inspired by Superhuman, starting with a screenshot <a class="yt-timestamp" data-t="24:23:00">[24:23:00]</a>.
*   He refined elements like action items hovering on selection <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>.
*   Vzer can provide specific technical details, such as how to improve animation speed and easing functions (e.g., using `cubic-bezier` in Tailwind animations), even if the user isn't familiar with these concepts <a class="yt-timestamp" data-t="25:06:00">[25:06:00]</a>.

## The Future of Building with AI

Lee emphasizes that AI tools like Vzer are not replacing human work but rather *augmenting* it <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>.
> "They're augmenting it in a way that is like I had that knowledgeable super senior engineer next to me that I could ask questions whenever I had issues and would help give me kind of some of these best practices along the way to build better products" <a class="yt-timestamp" data-t="27:25:00">[27:25:00]</a>.

In today's landscape, these tools empower individuals to build whatever they can imagine, from web apps to iOS or Android applications, as AI has extensive knowledge of various programming languages and platforms <a class="yt-timestamp" data-t="27:44:00">[27:44:00]</a>. He encourages builders to try these tools, suspend disbelief, and rethink their relationship with application development <a class="yt-timestamp" data-t="27:05:00">[27:05:00]</a>.

You can try Vzer for free at [vz.dev](https://vz.dev/) <a class="yt-timestamp" data-t="28:27:00">[28:27:00]</a>.