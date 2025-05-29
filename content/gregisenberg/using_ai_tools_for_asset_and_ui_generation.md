---
title: Using AI tools for asset and UI generation
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris Barok, a developer who has built a portfolio of mobile applications, leverages [[Using AI tools for content creation | AI tools]] to streamline and enhance his development process, particularly for UI and asset generation <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. He emphasizes how AI helps achieve a higher level of polish in native apps <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## UI Generation with Cursor

Chris uses Cursor for building native iOS applications <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. His approach to UI generation involves:

*   **Focusing on UI First**
    Chris's technique is to first prompt the AI to generate only the User Interface (UI), often with dummy data <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. This strategy makes it easier for the AI to follow instructions as it can focus on a single task <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. For example, he prompted Cursor to create a new tab for an AI chat, asking it to make the UI and hardcode dummy data <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Matching Existing UI**
    When generating UI, Chris instructs the AI to "try to follow the similar UI as other parts of the app" <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. This ensures consistency in design elements like color schemes and component usage <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. For instance, the AI successfully matched the purple color scheme of his budgeting app <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Iterative Refinement and Visual Feedback**
    During UI development, Chris frequently feeds screenshots of the app to Cursor, showing it what he sees and allowing it to identify and fix errors or refine the UI <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This visual feedback loop helps in correcting layout issues, such as a message area being hidden <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   **Handling Unexpected Features**
    In one instance, after prompting for the chat UI, Cursor automatically hardcoded responses and even an animation where messages scrolled down <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. This demonstrates the AI's ability to incorporate standard UX patterns for messaging apps without explicit prompting <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

> "Cursor knew exactly what to do. Yeah. Yeah, you didn't you didn't have to, you know, it's that was insane. Yeah." <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>

### Challenges in UI Setup

While AI excels at generating UI elements, it struggles with the initial project setup for Xcode, requiring manual configuration of settings and frameworks <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Tasks like enabling outgoing network requests must also be done manually in Xcode <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

## Asset Generation with GPT-4o

Chris uses GPT-4o for asset generation, noting its significant improvement in quality in recent weeks <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a> <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. This capability allows him to add a "level of polish" to his apps <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a> and [[Optimizing workflow with AI design tools | consistently create]] high-quality assets <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Techniques for Asset Generation:

*   **Generating Secondary Assets from a Primary One**
    By providing GPT-4o with an existing mascot or character image, Chris can generate an "infinite number of secondary assets" for various uses like loading screens or empty states <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>. Examples include:
    *   Adding wired glasses and placing the mascot in front of a laptop <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>.
    *   Changing the background color to purple and making the mascot appear to float <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.
    *   Adding specific objects like a coffee cup or books under a tree <a class="yt-timestamp" data-t="00:49:58">[00:49:58]</a>.
    *   Modifying specific features, such as removing legs or making a dog look like a specific pet by feeding in its image <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a> <a class="yt-timestamp" data-t="00:50:17">[00:50:17]</a>.
*   **Adding "Delight" and Humanizing Apps**
    [[Using AI for design and branding | AI-generated assets]] can add a crucial "dimension" to apps, allowing for cool empty states and illustrations <a class="yt-timestamp" data-t="00:51:40">[00:51:40]</a>. This helps "humanize" the app, making it more appealing and relatable to users <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>.
*   **Brainstorming Mascots and Logos**
    Chris also uses [[Utilizing AI for writing and content creation | AI to brainstorm]] ideas for mascots or logos. For his meeting transcription tool, he asked for mascot ideas for an app that "lives in the background," which eventually led to the concept of a ghost <a class="yt-timestamp" data-t="00:53:06">[00:53:06]</a> <a class="yt-timestamp" data-t="00:53:24">[00:53:24]</a>.

### Challenges in Asset Generation:

*   **Specificity in Prompts**
    While powerful, AI asset generation often requires very specific prompts. For example, when trying to remove a mouth from a dog illustration, the AI also removed the nose, demonstrating the need for precise instructions <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a> <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>.
*   **Success Rate**
    Chris estimates the AI gets it right about 60-70% of the time, which he still considers worthwhile due to the time saved <a class="yt-timestamp" data-t="00:51:12">[00:51:12]</a> <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>.

## Generating Realistic Mock Data

[[Generating content with AI tools | AI tools]] can also be used to generate realistic mock data for testing and demonstrations <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. Instead of generic data, Chris prompted the AI to create mock transactions for a 28-year-old male in Dallas, including real restaurants, which made the demo much more compelling <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>. This technique helps potential users envision themselves using the app <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.

> "It's not even just for you. So what you can do is you can come up with an idea for a startup, use cursor to build it, use some of this mock data, rec, you know, compile, build, record a video now with that data that's way more interesting, post it on X, see if people actually want the app." <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>

## Overall Impact

Chris believes that [[Leveraging AI for Content and Image Generation | AI tools]] will lead to "a lot more beautiful apps" <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a> and encourage developers to go beyond bare-bones designs <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>. He encourages developers to embrace [[Building AIpowered content generation tools | AI tooling]] as it is inevitable and will be crucial for thriving in the coming decade <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a> <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. He suggests non-developers use AI as a learning tool, perhaps with more guided tools like Replit or Lovable, to build foundational programming skills before diving into more "dangerous" tools like Cursor <a class="yt-timestamp" data-t="00:54:42">[00:54:42]</a> <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.