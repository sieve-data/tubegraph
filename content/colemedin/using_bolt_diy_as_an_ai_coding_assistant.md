---
title: Using bolt DIY as an AI coding assistant
videoId: xfFyAumTjT0
---

From: [[colemedin]] <br/> 

[[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]] is an [[opensource_ai_coding_assistant_development | open-source AI coding assistant]] designed to help users code applications by leveraging various large language models (LLMs) <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. It serves as a platform to compare and utilize different LLMs for coding tasks <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Purpose and Functionality

[[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]] allows users to generate code and build applications with [[ai_coding_assistants_like_bolt_and_their_limitations | AI coding assistants]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The platform was specifically used in one instance to compare the coding capabilities of Deep Seek R1 and OpenAI's O3 mini <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This comparison aimed to determine which LLM provided better results for [[building_applications_with_ai_assistance | building applications with AI assistance]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Setting Up and Running Bolt DIY

The [[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]] repository is accessible via the URL bolt.DIY, which redirects to the source code for the [[opensource_ai_coding_assistant_development | open source AI coding assistant]] <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. The homepage's README file provides a list of features and instructions for local setup and execution <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Integrating LLMs

[[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]] supports integrating different LLMs:
*   **O3 mini**: Used directly through the OpenAI API <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Deep Seek R1**: Accessed via OpenRouter, with a "Nitro" version available for improved reliability due to occasional outages with the direct Deep Seek API <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. While the Nitro version is pricier, the regular Deep Seek R1 is generally more affordable <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Error Correction Feature

A key feature of [[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]] is its ease of error correction <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. If an error occurs in the front end, a dedicated button allows users to automatically paste the entire error message into the LLM for it to fix <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

## Testing LLMs for Coding with Bolt DIY

[[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]] was used to compare O3 mini and Deep Seek R1 across various coding challenges <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Simple Application Creation

*   **Task**: Build a simple React with Tailwind to-do app using a starter template <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **O3 mini Performance**:
    *   **Speed**: Completed the task in approximately 10 seconds <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   **Functionality**: Successfully built the app but did not automatically run the command to start the site, requiring manual intervention <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The app had some minor UI peculiarities, like an irrelevant "background photo is by unsplash" text, but its core functionality (adding, marking off, deleting tasks) worked well <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Deep Seek R1 Performance**:
    *   **Speed**: Took longer, approximately 20-30 seconds <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   **Functionality**: Successfully built the app and automatically ran the command to start the site, demonstrating a "true one shot" capability <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. R1's output was more feature-rich and better reasoned, adding features like a task counter ("zero of two complete") that updated in real-time, even without explicit prompting <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. It also included a peaceful message when the task list was empty <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Initial Conclusion**: R1 showed better functionality and UI, while O3 mini was faster <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Complex Chat Frontend Application

*   **Task**: Build a full chat frontend for [[ai_coding_assistants_like_bolt_and_their_limitations | AI agents]], integrating with Superbase for authentication and chat history management, using a detailed prompt <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **O3 mini Performance**:
    *   **Effort**: Took multiple attempts and error corrections to reach a working state <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Initial issues included mixing up routes and other errors <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
    *   **Functionality**: Once working, the app allowed loading conversation history and continuing conversations <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. The primary flaw was duplicating the user message in the display due to a misunderstanding of how the message came from the database <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. Overall, it was impressive compared to previous tests with other tools <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   **Deep Seek R1 Performance**:
    *   **Speed**: Took significantly longer than O3 mini <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
    *   **Effort**: Compiled correctly on the first attempt <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. Only minor corrections were needed for functionality <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
    *   **Functionality**: The UI looked much better than O3 mini's <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. However, it had a notable glitch of not loading past conversations initially <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>, and it also duplicated user messages like O3 mini <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. Despite glitches, it offered more functionality <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
*   **Conclusion**: O3 mini required more initial effort but had fewer functional glitches; R1 offered a superior UI and more features but had a few more functional issues <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. It suggested a potential to combine their strengths <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

### Complex, Creative Chess Site

*   **Task**: Build a fully functional chess site with a single, simple prompt to grant creative freedom <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **O3 mini Performance**:
    *   **Effort**: Again, it messed up initially, starting with a default template, and required corrections <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   **Functionality**: Produced a chessboard that allowed piece movement and captures <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. However, it did not follow the rules of chess (e.g., pawns couldn't move two spaces on their first move, allowed capturing the king, and allowed putting oneself in check) <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. It did attempt to handle illegal moves <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Deep Seek R1 Performance**:
    *   **UI**: Produced a significantly better-looking UI for the chessboard <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.
    *   **Functionality**: Also did not follow the rules of chess, allowing pieces to move anywhere, similar to O3 mini <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. Its functionality was worse than O3 mini, as it didn't even attempt to enforce rules or handle illegal moves <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Overall Conclusion**: R1 generally produces a better UI and demonstrates better reasoning for understanding desired outcomes <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. O3 mini shows an edge in implementing functionality correctly and offers faster performance <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. This suggests an opportunity to potentially combine both LLMs for optimal results in [[effective_use_of_ai_coding_assistants | effective use of AI coding assistants]] <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

## Hosting Bolt DIY

[[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]] can be deployed via platforms like Repo Cloud, an open-source app marketplace <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. Repo Cloud offers one-click deployments for open-source applications, including [[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]], with competitive pricing and elastic auto-scaling <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.