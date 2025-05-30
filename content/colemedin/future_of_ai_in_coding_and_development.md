---
title: Future of AI in coding and development
videoId: R6AYmqcOXaw
---

From: [[colemedin]] <br/> 

The future of AI in coding and development is moving towards a "hands-off-the-wheel" approach, where AI can even research to assist itself <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This represents a significant shift, offering a glimpse into highly automated development processes <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Current State and Limitations of AI Coding Assistants

[[role_of_no_code_tools_and_ai_coding_assistants_in_ai_development | AI coding assistants]], whether browser-based like Bolt New or Autodev, or IDE-integrated like Windsurf or Cursor, are powerful tools that save countless hours in building application prototypes <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

However, a major [[limitations_of_current_ai_coding_assistants | limitation of current AI coding assistants]] is their lack of [[external_knowledge_issues_in_ai_coding_tools | external knowledge]], particularly regarding up-to-date library documentation <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This means they may not have information on newer or smaller libraries <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Demonstration of External Knowledge Limitation

To illustrate this, an experiment was conducted using Bolt to build an application around the `N8N demo` library, a relatively new and smaller library that larger language models (LLMs) like Claude 3.5 Sonnet (used in Bolt) do not have knowledge of <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

Despite providing a prompt to build a frontend to display an N8N workflow using the `N8N demo` tool and its JSON workflow, Bolt completely failed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. It could not correctly install dependencies from npm or create a preview because it lacked the necessary information on the library's usage and installation (e.g., script tags) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This failure is a common issue across tools like Cursor, Windsurf, and Autodev, highlighting the pervasive nature of the external knowledge problem <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## The Solution: AI with Computer Control Capabilities

The ideal solution for this limitation is to enable AI coding assistants to perform "Retrieval Augmented Generation" (RAG) by fetching external information from the internet and feeding it into the prompt to augment its context <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

One approach is to build this research capability directly into platforms like Bolt <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Alternatively, an artificial intelligence controlling the computer could research libraries and then inject that information into the prompt before the code build begins <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### Claude API for Computer Use

The Claude API for computer use allows Claude to control a computer to perform tasks such as typing into input boxes, searching the web, and navigating applications <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This "first of its kind" capability enables the desired research and prompt injection <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

#### Experimental Environment

The Claude computer use API can be run via Docker in a virtual machine that operates within the browser, addressing security concerns <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This setup, appearing as a virtual machine on the right side of the screen with a prompt interface on the left, allows for safe experimentation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

#### The Hands-Off Demonstration

In an experimental setup, Claude was instructed to:
1.  Research the `N8N demo` component <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Figure out how to use and install it <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Inject that information into a prompt for Bolt <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
4.  Have Bolt create the full application <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

The process involved some initial "handholding" by providing Claude with the direct website for research to prevent it from finding the wrong resource <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Despite this, the experiment demonstrated a remarkable level of automation.

Initially, Claude made a small mistake by not including all necessary script tags during its research <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. However, it was then instructed to correct itself, demonstrating its ability to iterate and fix errors <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

After correction, the AI successfully prompted Bolt to create the application. Although the preview inside the web container didn't work due to iframe limitations, deploying the application to Netlify allowed for successful viewing of the N8N workflow preview widget <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This entire process was completed with minimal human intervention, showcasing AI researching, crafting prompts, writing code, and running commands <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Future Implications for AI in Development

This experimental demonstration points to a future where developers can be "hands-off the wheel," with AI performing research to assist itself <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. The ability for an LLM to research web documentation, craft a prompt, and feed it into another LLM to write and run code is a significant leap <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

As LLMs become more powerful, the need for human "handholding" will decrease <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. This progression could also lead to the creation of documentation specifically designed for AI scraping <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. The concept of [[external_knowledge_issues_in_ai_coding_tools | RAG for AI coding assistance]] will become increasingly feasible, either through direct AI computer use as demonstrated or via direct integrations within [[role_of_no_code_tools_and_ai_coding_assistants_in_ai_development | AI IDEs]] like Windsurf <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. While currently experimental, this technology is expected to evolve very rapidly <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.