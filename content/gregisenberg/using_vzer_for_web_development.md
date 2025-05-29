---
title: Using Vzer for web development
videoId: sCFS_U7d9Do
---

From: [[gregisenberg]] <br/> 

Vercel's VP of Product, Lee, discusses how to effectively leverage Vzer as an AI assistant for web development <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is Vzer?
Vzer is an AI assistant specifically designed for web development <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. It focuses on working with web technologies like JavaScript, HTML, CSS, and various frameworks and libraries to produce high-quality web products <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. The goal is to make it as easy as possible to generate code for web applications <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

## Key Capabilities and Use Cases
Vzer can be used for various aspects of web development, from user interfaces to backend logic:

### UI/UX Design and Prototyping
*   **Generating UIs from prompts:** Vzer can build a page based on a description, even if the user doesn't have a clear idea of the UI <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. For example, it generated a component for integrating with [[using_zapier_for_automation_in_web_development | Zapier]] from a simple request <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.
*   **Iterating on existing designs:** Users can start with a screenshot or a basic idea and iteratively refine the design <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>. Lee demonstrated this by building a music player similar to Spotify, refining its appearance and information density <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.
*   **Applying specific design elements:** Users can instruct Vzer to use specific fonts (e.g., "Sanda font from Google fonts with next font") <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>, adjust information density ("tighter information density") <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>, and refine layout <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.
*   **Integrating imagery:** Vzer can use uploaded images in designs, which significantly enhances the visual appeal of generated web designs <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>, <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>.
*   **Ensuring Responsiveness:** Vzer can make layouts mobile responsive <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Creating specific page types:** It can build common web components like SAS landing pages <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>, pricing pages <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>, and dashboard views with subscription management and user info updates <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>.
*   **Implementing Animations:** Vzer can be instructed to use specific animation properties, such as easing functions, to control the feel of UI transitions <a class="yt-timestamp" data-t="25:06:00">[25:06:00]</a>.

### Backend and Data Management
*   **Generating Backend Logic:** Beyond UI, Vzer can handle backend work, including integrating interactivity <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>, <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   **Connecting to APIs and Databases:** Vzer can fetch data from external APIs or hook up generated UIs to real data by understanding database schemas <a class="yt-timestamp" data-t="21:04:00">[21:04:00]</a>.
*   **ORM Generation:** It can help generate Object-Relational Mapping (ORM) code (e.g., for Drizzle or Prisma in JavaScript/TypeScript) based on a Postgres schema <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>.
*   **Database Design Advice:** Users can ask Vzer to design efficient database structures, including suggestions for indexing <a class="yt-timestamp" data-t="23:15:00">[23:15:00]</a>.

## Tips for Effective Use
Lee provides several insights for getting the most out of Vzer:

1.  **Start with Screenshots:** Using screenshots as initial prompts is highly effective for guiding Vzer's output <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
2.  **Be Explicit with Design Preferences:** Clearly state desired design attributes such as color schemes ("warmer Grays"), fonts ("Sanda font"), and information density ("tighter information density") <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>, <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
3.  **Utilize Tailwind CSS Knowledge:** Vzer "thinks in Tailwind" <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. If you know Tailwind CSS classes, you can explicitly tell Vzer the exact values or styles you want, providing precise control over the output <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>, <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.
4.  **Upload Images:** Incorporating images into your prompts can significantly improve the visual quality of the generated designs <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>, <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>.
5.  **Iterate and Refine:** Don't expect perfection on the first try. Continuously provide feedback and ask for adjustments to achieve the desired result <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
6.  **Learn Design Principles from Vzer:** If you're a novice in web design, you can ask Vzer directly for advice on improving designs, such as common practices for color schemes, white space, and readable fonts <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.
7.  **Seek External Inspiration:** Utilize design inspiration websites like Godly.website and Patterns to find UI patterns or overall aesthetics, then use screenshots or descriptions in Vzer <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>, <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>.
8.  **Leverage Shad CN UI Patterns:** Vzer is built on Shad CN UI, which provides a component library with common UI patterns (e.g., mail app, dashboard, music player) <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. You can fork these patterns within Vzer and customize them to fit your brand <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.
9.  **Think of it as a Pair Programmer:** Treat Vzer like a knowledgeable colleague, asking questions and providing feedback as if collaborating with a human <a class="yt-timestamp" data-t="19:15:00">[19:15:00]</a>, <a class="yt-timestamp" data-t="27:28:00">[27:28:00]</a>.

## Vzer's Foundation
Vzer generates real React components using the same technology typically used for production websites, specifically built on top of the Shad CN UI system <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>, <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>. This means the code it produces is not "throwaway" but rather ready for integration into a project <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.

## AI as an Augmentation Tool
Lee emphasizes that AI tools like Vzer are not replacing developers but augmenting their capabilities <a class="yt-timestamp" data-t="27:23:00">[27:23:00]</a>. They act as an assistant, providing best practices and accelerating the building process, allowing users to build almost anything they can imagine <a class="yt-timestamp" data-t="27:34:00">[27:34:00]</a>, <a class="yt-timestamp" data-t="27:45:00">[27:45:00]</a>.

## Trying Vzer
Vzer offers a free tier for users to experiment with its capabilities <a class="yt-timestamp" data-t="28:27:00">[28:27:00]</a>. It can be accessed at vz.dev <a class="yt-timestamp" data-t="28:27:00">[28:27:00]</a>.