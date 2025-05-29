---
title: Using AI for creating steps in startup projects
videoId: ehK-QqPstJ4
---

From: [[gregisenberg]] <br/> 

There's a significant opportunity to create agencies and products now, even if it feels difficult, because the individuals who start now will be able to create even better sites by the time the process becomes easier for the masses <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Not many people are currently pushing the boundaries of AI websites, which is where the most profitable industries or interesting niches can be found <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Building a Social App for Startup Ideas
The process involves [[building_apps_with_ai_tools | building apps with AI tools]] through iterative design and development. The goal was to create a community social app for sharing startup ideas where users could:
*   Create a profile <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   Type in a startup idea <a class="yt-timestamp" data-t="01:50:51">[01:50:51]</a>.
*   Use AI to generate necessary steps for the idea <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   Rate and comment on other people's startup ideas <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

This app, initially estimated at $29,000 for traditional development, was built rapidly using AI tools <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.

### Design and Iteration with V0
The initial design for the app's homepage using V0 was not visually appealing <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. Through iterative prompts, the design was refined to a clean, simple layout <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

Key design considerations included:
*   **Color Scheme:** Shifting from a super colorful background to a white background with gray cards and neon text, matching a specific YouTube channel's branding <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.
*   **Component-based Design:** It is more effective to design one component at a time, such as a single card, rather than the entire page at once <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. This allows for faster iterations and prevents overwhelming the AI's context window <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.
*   **Saving and Organizing Components:** Publishing and forking V0 designs allows for easy tracking of individual components and their corresponding code <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.

### Core Functionality Development
The app was developed using a template built on Next.js, allowing integration with various APIs like OpenAI and Firebase <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. Firebase serves as the database for storing user data, images, and handling Google authentication <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

The development process emphasized:
*   **Template Use:** A pre-configured template was used to set up the basic structure and APIs, streamlining the initial setup which often involves the hardest "plumbing" code <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   **Cursor's Composer Mode:** This mode allows for editing multiple files simultaneously and is the primary interface for instructing the AI <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   **Prompting Strategy:**
    *   Start by telling Cursor to follow instructions in a specific file or the entire codebase using the `@` symbol (e.g., `@social media` or `@codebase`) <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.
    *   Describe the current problem or state, then specify what is desired <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Be overly specific, like instructing an intern <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.
    *   For design issues, screenshots with annotations (e.g., using CleanShot X) can be highly effective <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
    *   For smaller changes, multiple requests can be combined into one prompt, but for larger changes, focus on one change per prompt <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.
*   **Error Handling:** Expect errors, especially when starting out <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. The primary method for resolving errors is to copy the error message and paste it back into the AI's prompt <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
*   **Version Control:** Save changes frequently using the Git tab in Replit. This allows reverting to previous states if a change introduces significant issues, preventing wasted time <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

## [[leveraging_ai_for_startup_idea_generation | Leveraging AI for Startup Idea Generation]]
The core AI feature allows users to input a startup idea, and the OpenAI API generates necessary steps to achieve that idea <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. This functionality could be extended to use custom AI assistants trained on specific content, such as a podcast's archive of startup ideas <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.

## Refining and Polishing
After establishing core functionality, the focus shifted to aesthetics and user experience:
*   **UI Cleanup:** Addressing issues like duplicate navigation bars and styling inconsistencies <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.
*   **Styling Integration:** Applying the clean, gray card design developed in V0 to the displayed startup idea posts <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.
*   **Profile Management:** Implementing profile picture uploads and ensuring they appear on the homepage, which presented challenges related to data storage and access <a class="yt-timestamp" data-t="01:16:12">[01:16:12]</a>.
*   **Dark Mode Compatibility:** Ensuring the app functions correctly across different system appearance settings (light/dark mode) <a class="yt-timestamp" data-t="01:07:01">[01:07:01]</a>.

## Key Takeaways for [[building_a_startup_using_ai_tools | Building a Startup Using AI Tools]]
*   **Don't Wait:** There's a "massive opportunity right now" <a class="yt-timestamp" data-t="01:19:53">[01:19:53]</a>; don't wait for AI tools to get easier <a class="yt-timestamp" data-t="01:20:26">[01:20:26]</a>. Those who start now will be more advanced when AI development becomes simpler <a class="yt-timestamp" data-t="01:20:01">[01:20:01]</a>.
*   **Iterate Relentlessly:** Embrace errors as learning opportunities. Copying and pasting errors back into the AI prompt is a common and effective troubleshooting method <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
*   **Start with a Plan:** Coming in with a full plan is "very very very useful" and reduces the likelihood of getting stuck <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
*   **Be Specific with Prompts:** Clearly describe the current situation and precisely what changes are desired <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Use visual aids like screenshots when possible <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
*   **Manage Context:** Reset the AI's composer window when starting a new feature or encountering persistent issues to avoid overwhelming its context <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>.
*   **Prioritize Functionality Over Design:** Focus on the core functionality first, as a beautiful app without core features is just "a pretty piece of artwork" <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>. Design can be refined later <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   **Learn from Others:** Observe others building and solving problems. Being part of a community and watching live "cooking" sessions can expose you to different errors and solutions, accelerating learning <a class="yt-timestamp" data-t="01:28:30">[01:28:30]</a>.
*   **Treat Software Like a Tweet:** The goal is to make [[building_apps_with_ai_tools | building apps with AI tools]] as easy as tweeting. This encourages frequent experimentation and putting ideas out there to see what gains traction <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

This approach transforms the startup creation process, making it possible to build a functional social media app with AI-generated features in under two hours <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>.

## Community and Resources
*   **Senior Software Composer:** A community for learning to create and deploy web apps using AI <a class="yt-timestamp" data-t="01:38:40">[01:38:40]</a>.
*   **Greg Eisenberg:** A resource for startup ideas and content <a class="yt-timestamp" data-t="01:40:13">[01:40:13]</a>.
*   **CleanShot X:** A recommended tool for quick screen grabs and annotations <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **TalkTastic:** A tool for using voice commands in development <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.