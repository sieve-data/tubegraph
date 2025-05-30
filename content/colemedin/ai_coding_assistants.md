---
title: AI Coding Assistants
videoId: yRIEpNlacd0
---

From: [[colemedin]] <br/> 

[[ai_coding_assistants | AI coding assistants]] are tools that help developers build applications, often by generating code or assisting with development workflows <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. They have various pros and cons, but when used in tandem, they can provide a powerful, flexible, and fast development experience <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

## Types of [[ai_coding_assistants | AI Coding Assistants]]

[[ai_coding_assistants | AI coding assistants]] can generally be categorized into two main types based on their operating environment:

*   **In-browser editors**: These platforms run in the web browser <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Examples include Lovable, Bolt.new, and [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. They are often much faster at getting a project started <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **AI IDEs**: These are integrated development environments (IDEs) that run directly on your computer <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Examples include Windsurf and Cursor <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. They are phenomenal for making more directed changes to applications <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Characteristics of Specific [[ai_coding_assistants | AI Coding Assistants]]

### [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]]

[[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] is an open-source [[ai_coding_assistants | AI coding assistant]] that the community is building to be a leading open-source tool <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

*   **Customization**: It allows users to integrate any large language model (LLM), many of which are completely free to use <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>, <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Performance**: Due to its focus on supporting many different LLMs, it may not be optimized for just one, potentially leading to less efficient initial project creation compared to tools optimized for single LLMs <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Cost-effectiveness**: It solves the problem of hitting credit limits seen in other platforms by allowing users to run it locally and use free models, enabling continuous, free iterations and tweaks on projects <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>, <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
*   **Local Operation**: [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] runs on your local computer, accessed via a Local Host URL <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>, <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
*   **Limitations**: Its web container blocks requests to Local Host agents, meaning that direct interaction with agents might not work within [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

### Lovable and Bolt.new

These in-browser [[ai_coding_assistants | AI coding assistants]] are designed to optimize for a single LLM <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

*   **Performance**: They generally provide better performance when starting an application from scratch and laying a solid foundation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Specialization**: Lovable is noted to perform better for chat-style applications, while Bolt.new excels at building landing pages <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Cost**: They typically offer free credits to get started, but continuous tweaking and changes can consume more credits, potentially leading to usage limits <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Functionality**: Lovable does not block requests to Local Host agents, allowing direct chatting with an agent within its environment <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.

### AI IDEs (Windsurf and Cursor)

These are desktop-based [[ai_coding_assistants | AI coding assistants]].

*   **Control**: They are excellent for making more directed and precise changes to applications <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
*   **Complementary Use**: They are best used after an initial project foundation has been established with an in-browser editor <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.

## [[ai_coding_workflows_and_processes | AI Coding Workflows and Processes]]

A recommended workflow for building a custom front end for an AI agent involves combining different [[ai_coding_assistants | AI coding assistants]] to leverage their respective strengths <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>:

1.  **Foundation with Lovable/Bolt.new**: Start by generating the initial project foundation using a single prompt in Lovable or Bolt.new <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. These tools are effective for establishing the core structure, including UI, API connections, and authentication <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
    *   When prompting, be very clear about how the agent communicates, including input and output schemas, and how messages are handled <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. It's more important to be specific about functionality than UI <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   Integrate Superbase for chat history and authentication by providing the project URL, public key, and messages table schema in the prompt <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>, <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Ensure real-time communication is enabled for the messages table to pull new messages instantly <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>, <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
    *   After creation, publish the project to GitHub, making it public if desired, to facilitate transfer to other tools <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>, <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>, <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

2.  **Refinement with [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]]**: Transfer the project to [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] to make free, continuous tweaks to the UI and UX <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>, <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
    *   Install [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] locally using Node.js and Git <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>, <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
    *   Clone the GitHub repository into [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   When prompting [[ai_coding_assistants | AI coding assistants]] for changes, request one thing at a time for better understanding and implementation <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.
    *   Utilize features like image support (e.g., Gemini in [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]]) to provide visual context for desired changes <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>, <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.

3.  **Final Touches with AI IDEs**: Download the project from [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] and import it into an AI IDE like Windsurf or Cursor <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>, <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. This step is for making final, directed changes and preparing for deployment <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>, <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.

This combined approach allows for rapid prototyping, cost-effective iteration, and precise final adjustments, leading to a fully custom and polished front end <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>, <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.