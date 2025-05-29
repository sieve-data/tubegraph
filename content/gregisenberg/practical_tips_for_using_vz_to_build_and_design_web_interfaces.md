---
title: Practical tips for using VZ to build and design web interfaces
videoId: sCFS_U7d9Do
---

From: [[gregisenberg]] <br/> 

VZ is an AI assistant developed by Vercel specifically for [[introduction_to_vercels_vz_for_web_development | web development]] <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. It focuses on working with JavaScript, HTML, CSS, and various new frameworks and libraries, aiming to simplify the process of getting high-quality web products <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

## Getting Started with VZ

*   **Understanding VZ's Purpose**: Think of VZ as an AI assistant for [[using_ai_tools_for_web_ui_and_backend_development | web development]] <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. It's designed to help with building high-quality web interfaces and adding interactivity <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
*   **Creative Modes**: Approach VZ in one of two ways <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>:
    *   **With an Opinion**: If you have a clear idea of what you want, start with a screenshot or detailed description <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
    *   **Without an Opinion**: If you're unsure, let VZ generate initial designs and then iterate from there <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

## UI Design Tips

*   **Start with Screenshots**: Providing screenshots is "super helpful" for VZ to understand your vision, especially if you have a specific UI in mind <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. This allows for iterative refinement <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **Use Specific Design Language**:
    *   **Colors**: Request "warmer Grays" or specific color adjustments like "make the colors a bit darker" but "not full black" <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>, <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.
    *   **Fonts**: Specify font types like "Sans Serif font" <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a> or "mono font monospace" <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>. You can even specify "from Google Fonts with Next.js font" for precise imports <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
    *   **Density & Spacing**: Ask for "tighter information density" <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a> or "less vertical spacing between the rows" <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.
    *   **Element Placement**: Direct VZ on where to place elements, e.g., "each row should have the album art to the left of it" <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a> or "put the artist names in a column versus under the title" <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
*   **Leverage Tailwind Knowledge**: VZ "thinks in Tailwind" <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. If you know [[building_websites_with_webflow | Tailwind CSS]], you can explicitly tell it the class you're looking for, such as "make it size four" for image dimensions <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>, or "use this CSS property called tabular nums" for number alignment <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>.
*   **Incorporate Imagery**: Upload and paste images for VZ to use in designs, as "so much of web design is just topography and imagery" <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>, <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. High-quality images make a huge difference <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>.
*   **Use Natural Language**: Talk to VZ "how I would talk to my designer" <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>, describing desired changes like "that now playing bar is pretty wide" <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   **Mobile Responsiveness**: Simply ask VZ to "make it mobile responsive" <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a> and refine based on its output <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.
*   **Experiment with Styles**: Don't be afraid to say "try a different style" if you don't like an initial output <a class="yt-timestamp" data-t="18:29:00">[18:29:00]</a>.
*   **Learn Through Prompts**: If you're new to [[design_and_user_interface_considerations_in_web_apps | web design]], ask VZ questions like "I'm a novice at web design... what can I try to make things look a little better?" <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>. It can provide common practices like consistent color schemes, whitespace, readable fonts, and aligned layouts <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>. You can follow up with specific questions like "what is a sans serif font and what are the differences?" <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>.
*   **Seek Inspiration**:
    *   **Godly.website**: Browse for design inspiration, filtering by startups to see beautiful websites. You can use screenshots from these sites as starting points <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a>.
    *   **Patterns**: Another resource for discovering UI patterns and understanding how to articulate them to VZ <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>.
    *   **Shad CN UI**: VZ is built on this system. It provides pre-built UI patterns and components (e.g., mail app, dashboard, music player). You can "fork" these components in VZ and customize them for your brand <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
*   **Study Existing Apps**: For specific design elements, like a "settings page," check your favorite apps and either screenshot them or describe their characteristics to VZ <a class="yt-timestamp" data-t="20:31:00">[20:31:00]</a>.
*   **Refine Animations**: For [[user_experience_and_design_strategies_for_app_development | animations]], ask VZ why an animation "feels slow" <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>. It can provide details on how to override Tailwind animations, adjust duration, and use easing functions like cubic bezier <a class="yt-timestamp" data-t="25:20:00">[25:20:00]</a>.

## Backend & Logic Tips

*   **Implement Interactivity**: Beyond just UI, VZ can help add interactivity to your components <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
*   **Break into Components**: Once you have a good design, ask VZ to "break this out into components" and "start trying to add some logic to it" <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
*   **Connect to Data**:
    *   V0 can provide mock data <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a>.
    *   You can ask VZ to make API calls using external APIs <a class="yt-timestamp" data-t="21:04:00">[21:04:00]</a>.
    *   Add your database schema as a source to your project, and VZ can help hook up components to real data <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.
*   **Backend Design Assistance**:
    *   Provide your Postgres schema and ask VZ for the ORM (e.g., Drizzle or Prisma for JavaScript/TypeScript) <a class="yt-timestamp" data-t="21:25:00">[21:25:00]</a>.
    *   Describe your data needs (e.g., "I need a table for users and emails") and VZ can help design the backend structure, including SQL code and relationships <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>.
    *   Ask VZ to "design it in a way that it's really fast" <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>, and it might suggest using indexes on your database <a class="yt-timestamp" data-t="23:22:00">[23:22:00]</a>.

## General Usage Philosophy

*   **No Prior Knowledge Required (But Helpful)**: While pre-existing web design knowledge helps you "fly faster," it's not a requirement <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>.
*   **AI as a Learning Tool**: VZ can help you learn by providing answers and even suggesting "questions to ask" <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>. This fosters taste development during the learning process <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
*   **Production-Ready Code**: VZ aims to generate "real React components that use the same technology you would build for your production website anyway," meaning the code isn't throwaway <a class="yt-timestamp" data-t="16:19:00">[16:19:00]</a>.
*   **Augmentation, Not Replacement**: AI tools like VZ are not replacing development work but "augmenting it" <a class="yt-timestamp" data-t="27:23:00">[27:23:00]</a>. They act like a "knowledgeable super senior engineer" providing best practices and assistance <a class="yt-timestamp" data-t="27:28:00">[27:28:00]</a>.
*   **Embrace the Power**: With these tools, it's "never been a better time" to build products, as you have the power to create "whatever you want" <a class="yt-timestamp" data-t="27:40:00">[27:40:00]</a>, <a class="yt-timestamp" data-t="27:45:00">[27:45:00]</a>.

For more information and to try VZ, visit [v0.dev](https://v0.dev/) <a class="yt-timestamp" data-t="28:27:00">[28:27:00]</a>.