---
title: AI IDEs and Platforms
videoId: yRIEpNlacd0
---

From: [[colemedin]] <br/> 

This article explores the process of building a custom front-end for AI agents using a combination of [[ai_coding_assistants | AI coding assistants]] and [[evolution_of_ai_ides | AI IDEs]], highlighting their unique strengths and how they can be used in tandem to achieve a flexible, fast, and free development workflow <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The examples shared focus on creating a GitHub agent that can process entire repositories for code Q&A <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Categories of [[ai_development_tools | AI Development Tools]]

Different [[ai_development_tools | AI development tools]] offer various advantages for building applications:

*   **[[ai_coding_assistants | In-Browser AI Coding Assistants]]**
    *   Platforms like Lovable and Bolt.new are optimized for single large language models (LLMs) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
    *   They excel at quickly starting a project and laying a solid foundation, often providing free credits for initial development <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   They are significantly faster at getting a project started compared to [[evolution_of_ai_ides | AI IDEs]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
    *   However, continuous tweaking on these platforms can consume many credits <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **[[opensource_ai_coding_assistants_and_community_building | Open-Source AI Coding Assistants]]**
    *   [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] is an [[opensource_ai_coding_assistants_and_community_building | open-source AI coding assistant]] built by a community <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   It allows users to utilize any large language model, many of which are free <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
    *   While it may not offer the best initial performance for creating a foundation compared to single-LLM optimized platforms <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, its open-source nature means you can use it for free to make continuous changes without running out of usage or credits <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>, <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   A limitation is that the web container in Bolt.DIY blocks requests to Local Host agents, preventing direct interaction with agents <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **[[evolution_of_ai_ides | AI IDEs]]**
    *   Tools like Windsurf and Cursor run directly on your computer <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   They are highly effective for making more directed or granular changes to applications <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
    *   Some, like Windsurf, also offer free credits <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

## Integrated Development Process

The recommended process for building an AI agent's front end combines these tools for optimal efficiency and cost-effectiveness <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>:

1.  **Initial Foundation with Lovable/Bolt.new**:
    *   Start the project with a powerful, single-LLM optimized platform like Lovable or Bolt.new to establish a strong foundation with a single prompt <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Lovable is particularly good for chat-style applications <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   This step leverages free credits to get the project off the ground <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

2.  **Continuous Iteration with [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]]**:
    *   Publish the initial project from Lovable (or Bolt.new) to GitHub <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   Pull the project into [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] from GitHub <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   Use Bolt.DIY with free LLMs (e.g., Gemini 2.0 Flash) to make extensive UI/UX tweaks and refinements without incurring costs <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>, <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.
    *   When prompting, it's advised to request one change at a time for better accuracy from the LLM <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. Bolt.DIY also supports image inputs for visual context <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.

3.  **Final Polish with [[evolution_of_ai_ides | AI IDEs]]**:
    *   Download the project from Bolt.DIY <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   Bring the project into an [[evolution_of_ai_ides | AI IDE]] like Windsurf or Cursor for final, more directed modifications and local testing <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

### Building a GitHub Agent Front End

The series demonstrates building a front end for a GitHub agent <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The agent was previously integrated with the Agent Zero platform, providing a polished front end <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The current goal is to create a fully custom front end for this agent <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

#### Live Agent Studio

The Live Agent Studio is a platform for collaborating on [[opensource_ai_coding_assistants_and_community_building | open-source AI agents]] <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>. Agents built with platforms like Python, n8n, or Voiceflow can be published there <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. The project involves taking an existing AI agent, turning it into an API endpoint, and hooking it into any front end <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

#### Prompting Lovable for the Foundation

To create the initial front end with Lovable, a detailed prompt is essential. Key elements to include are:

*   **UI Specifications**: General instructions for the UI, e.g., "beautiful dark theme" with specific colors <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Agent URL**: The API endpoint URL for the agent <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Input Schema**: The payload structure expected by the API endpoint <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Output Schema**: The expected format of responses from the API <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Superbase Integration**:
    *   Baking the Superbase URL and public key directly into the code (instead of an `.env` file) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. These are public and safe to include in the prompt <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   Specifying the schema for the `messages` table in Superbase, which stores conversation history <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
    *   Clarifying that real-time updates are enabled for the `messages` table, allowing the front end to subscribe to changes and display new messages immediately <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
    *   Instructions for setting up the `messages` table and enabling real-time communication are available in the Automator Live Agent Studio developer guide <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   Including a requirement for Superbase authentication with email and password <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Additional Requirements**: A list of miscellaneous functional and UX requirements (e.g., markdown handling, loading indicators, enter to send message) <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

The initial result from Lovable, generated with a single prompt (and a few minor follow-up suggestions), provides a functional front end with Superbase authentication and conversation history <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>, <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

#### Refining with [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]]

After getting the base from Lovable, the project is pushed to a public GitHub repository <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] is installed locally (requiring Node.js and Git) <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>, <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>, and the GitHub repository is cloned into it <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. Bolt.DIY allows developers to iterate on the UI/UX using free LLMs like Gemini 2.0 Flash <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, significantly improving the design and functionality (e.g., adding a header, refining button styles, enabling enter to send messages, and theme toggling) <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

#### Local Deployment and [[evolution_of_ai_ides | AI IDE]] Usage

Once satisfied with the changes in [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]], the code is downloaded as a zip file <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. This downloaded project can then be run locally on the developer's machine using `npm install` and `npm run dev` <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>, <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>. For more directed, specific changes, the project can be imported into an [[evolution_of_ai_ides | AI IDE]] like Windsurf or Cursor <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. This multi-tool approach ensures the front end is functional, polished, and ready for further development and deployment <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

## Conclusion

Combining different [[ai_coding_assistants | AI coding assistants]] and [[evolution_of_ai_ides | AI IDEs]] offers a powerful and efficient workflow for building AI agent front ends <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>. This tandem approach provides the perfect blend of being free, flexible, and fast <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. This method is applicable for building various front ends and serves as a robust process for refining, testing, and eventually monetizing AI agents <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>, <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.