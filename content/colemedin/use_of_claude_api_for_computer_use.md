---
title: Use of Claude API for computer use
videoId: R6AYmqcOXaw
---

From: [[colemedin]] <br/> 

The [[integration_of_mcp_in_ai_tools | Claude API for computer use]] allows Claude to control a computer, performing actions like typing in input boxes, searching the web, and navigating through applications <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This represents a significant step towards AI being able to assist itself through research and interaction <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Addressing the Knowledge Gap in AI Coding Assistants

Current [[opensource_ai_coding_assistant_development | AI coding assistants]], such as Bolt, Autodev, Windsurf, and Cursor, are powerful tools that can save hours in building application prototypes <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. However, a major limitation is their lack of external knowledge, particularly regarding new or smaller library documentation <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. This often means they are not up-to-date with current coding requirements <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

### Demonstration of the Problem

An attempt to build a frontend to display an N8N workflow using the `N8N demo` library with Bolt, which utilizes [[comparison_with_claude_35_sonet | Claude 3.5 Sonnet]], failed because the LLM lacked knowledge of this relatively new and smaller library <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. The assistant was unable to correctly install dependencies or generate the required code, even after prompts to fix itself <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. This highlights the need for Retrieval Augmented Generation (RAG) capabilities for AI coding assistants <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

## Solving the Problem with Claude's Computer Use API

The [[integration_of_mcp_in_ai_tools | Claude API for computer use]] offers a solution by allowing an AI to research necessary information and then inject it into the prompt of another AI coding assistant <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

### Implementation and Setup

Anthropic provides a reference implementation of the Claude computer use API on GitHub, which can be easily run using Docker <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. This setup spins up a virtual machine accessible in the browser, ensuring security by not directly controlling the user's main computer <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. Users can prompt Claude on the left side of the interface, while the virtual machine environment is displayed on the right <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

### Hands-Off Demonstration Workflow

The process involves Claude researching the `N8N demo` component, understanding its usage and installation, and then injecting this information into a prompt for Bolt to create the application <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.

1.  **Initial Prompting:** Claude is given access to Bolt in the browser and directed to a specific website for `N8N demo` component research <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. It's also provided with the workflow JSON to be included <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.
2.  **Autonomous Research and Code Generation:** Claude navigates the virtual environment and attempts to build the application <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>.
3.  **Correction:** The initial attempt by Claude resulted in an incomplete solution due to missing script tags <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. A simple correction prompt was given to Claude to include the necessary script tags <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
4.  **Successful Deployment:** After correction, the application was successfully created. Although the preview widget with iframes did not work within the web container due to a policy, it was successfully deployed to Netlify, where the N8N workflow preview widget functioned as expected <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.

## Future Implications

This experiment demonstrates a future where AI can be "hands-off the wheel," researching to assist itself <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>. The ability of a large language model to research web documentation, craft a prompt, feed it to another LLM to write code, run commands, and spin up an environment with minimal human intervention is significant <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. This capability, termed "Rag for AI coding assistance," is expected to become very doable either through computer use APIs or direct integrations within [[opensource_ai_coding_assistant_development | AI IDEs]] <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. The development of documentation specifically optimized for AI scraping is also anticipated <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.