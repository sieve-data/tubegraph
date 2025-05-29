---
title: Challenges and solutions in AIassisted software development
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

AI-assisted coding, particularly with Large Language Models (LLMs), is a rapidly evolving and challenging field <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. While online tutorials often present a smooth process where users can prompt an AI to build an entire application <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, the reality is often unpredictable <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. LLMs can hallucinate, leading to errors and a less-than-smooth development experience <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Key Challenges

*   **Unpredictable Results**
    *   LLM-based coding often yields unpredictable outcomes due to the inherent nature of models to hallucinate <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This contrasts sharply with edited online tutorials that show seamless execution <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Tool Usage Ambiguity**
    *   It's often unclear when to use specific [[Using AI tools for web development | AI tools for web development]] like Cursor, VZ, or Replit <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Open-Ended Prompting Issues**
    *   Keeping prompts open-ended often results in the AI not producing the desired output <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>, and making changes to an established structure can be very difficult <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Documentation and Structure Misinterpretation**
    *   AI tools like Cursor often fail to properly integrate provided documentation <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a> and struggle with understanding the project's file structure, leading to misplaced files and incorrect dependencies <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   Common web app requirements (e.g., `use client`, environment variables) are frequently missed or incorrectly implemented by AI <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
    *   Older model versions or incorrect support for features (e.g., structured output) can cause failures, even when documentation is provided <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.
*   **Debugging Difficulties**
    *   Errors often appear later in the development process if not addressed early <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
    *   Debugging can be frustrating, especially when changes made by the AI are incorrect or hard to discern <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>. Communicating specific, annoying errors to the AI can be challenging <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>.
*   **Performance Inconsistencies**
    *   AI coding tools like Cursor can exhibit variable performance, sometimes being fast, sometimes slow, or even down <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a>.

## Solutions and Workflow Improvements

To overcome these [[Challenges and solutions in AI app development | challenges]], a more structured and strategic approach to [[Using AI for app development | AI-assisted app development]] is recommended, moving beyond the "one-shot" approach of building an entire app with a single prompt <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.

### 1. Detailed Specification Writing

*   **Upfront Planning:** Spend significant time writing clear and detailed specifications (specs) before starting to code <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This reduces uncertainty and yields more consistent results <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Structured Specs:** Use a common structure for specs, including:
    *   Project overview (what is the goal?) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
    *   Core functionality breakdown (must-have features) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
    *   Implementation documentation for key features (e.g., proof-of-concept code snippets) <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
    *   Current file structure to guide the AI on where to create files <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   Additional requirements (e.g., specific web app considerations like `use client` or environment variables) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. These can be saved as common prompts for different project types (web, iOS) <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Engineer Manager Role Simulation:** Use a stronger AI model (e.g., GPT-4o) to expand the draft specs into a detailed Product Requirements Document (PRD), simulating an engineer manager filling in architectural and technical details <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. This defines functionality and file structures with more detail, leaving less ambiguity for engineers <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>.

### 2. Strategic Tool Utilization

*   **Functionality First, UI Later:** Prioritize building core functionality with tools like Cursor, completely ignoring the UI initially <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **UI Touch-ups with VZ:** Once functionality is robust, use tools like VZ to refine the user interface bit by bit <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This approach leads to greater success than trying to build everything at once <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Gradual Implementation:** Break down the project into smaller, manageable tasks. Implement one part of the specification at a time using tools like Cursor <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>. This "crawl, walk, run" strategy reduces errors and prevents the AI from skipping steps <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>.

### 3. Reusable Modular Prompts

*   **Standardized Features:** Identify common, standardized features (e.g., user authentication, payment systems) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Community Collection:** Develop and share a collection of reusable, modular prompts for these standard features <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This allows developers to quickly generate entire functionalities by providing a prompt to Cursor <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Future Development Tools:** Envision future developer tools that aggregate these modular prompts, simplifying integration into applications <a class="yt-timestamp" data-t="00:55:32">[00:55:32]</a>.

### 4. Debugging and Iteration

*   **Early Proof-of-Concept:** Build proof-of-concept code early for core functionalities to ensure they work as expected, e.g., fetching data from an API or using an LLM's structured output <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Step-by-Step Debugging:** When errors occur, use prompts like "help me debug" or "let's think step by step" to guide the AI through the problem <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. This technique, similar to "chain of thought" prompting, helps the AI break down complex problems and achieve better results <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.
*   **Add Debug Info:** If errors are difficult to diagnose, prompt the AI to add debug information to the code, providing a clearer path for communication and resolution <a class="yt-timestamp" data-t="00:42:47">[00:42:47]</a>.

By adopting these structured practices, developers can significantly improve the success rate and efficiency of [[Implementing AI in app development processes | AI-assisted software development]], transforming from casual AI users into proficient AI coders <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.