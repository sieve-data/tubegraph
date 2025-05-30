---
title: Building applications with AI assistance
videoId: R6AYmqcOXaw
---

From: [[colemedin]] <br/> 

The field of AI is rapidly advancing towards a future where development can be largely "hands-off the wheel," with AI capable of self-research and self-assistance <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This approach enables a glimpse into a highly automated future for software development <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## The Power and Limitations of AI Coding Assistants

[[using_ai_coding_assistance | AI coding assistants]], whether browser-based like Bolt, AutoDev, or IDE-integrated like Windsurf or Cursor, are incredibly powerful tools <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. They can save hours in [[building_and_deploying_custom_ai_front_ends | building]] nearly any application prototype <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

However, a significant limitation of these assistants is their lack of external knowledge for crucial information, such as current library documentation <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This means they may not be up-to-date with many coding requirements <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Demonstration of External Knowledge Gap
To illustrate this flaw, an experiment was conducted using Bolt, an AI coding assistant that uses Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The task was to [[building_and_deploying_custom_ai_front_ends | build a front-end]] to display an N8N workflow using a relatively new and small library called N8N demo <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This library is used by N8N to display preview widgets for their AI automation workflows <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> and has specific HTML and JavaScript installation instructions <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

When prompted to [[building_and_deploying_custom_ai_front_ends | build]] the application, Bolt failed completely because it lacked access to the N8N demo library's documentation <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. It even failed to install dependencies correctly <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, demonstrating that this isn't a fault of Bolt specifically, but a common problem across [[effective_use_of_ai_coding_assistants | AI coding assistants]] like Cursor, Windsurf, or AutoDev <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Bridging the Gap: RAG for AI Coding Assistance

This scenario highlights the need for a "Retrieval-Augmented Generation" (RAG) approach for [[using_ai_coding_assistance | AI coding assistance]] <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. RAG would allow the AI to go out to the internet, fetch necessary information like library documentation and installation guides, and then feed that into the prompt to augment its knowledge base before generating code <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

This capability could be integrated directly into platforms like Bolt, allowing them to research the web before fulfilling requests <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Alternatively, an artificial intelligence controlling a computer could perform this research and inject the findings into the prompt of an AI coding assistant before code generation <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### The Claude Computer Use API
The Claude computer use API is a tool that allows Claude to control a computer to perform tasks like typing, web searches, and navigating applications <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This is a novel capability that enables advanced AI assistance <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

For security, the API typically operates within a virtual machine environment accessible via a web browser, rather than directly controlling the user's main computer <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This test environment allows for experimentation without security concerns <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## An Experimental Demonstration

An experiment was conducted using the Claude computer use API to research the N8N demo component, understand its usage and installation, and then inject that information into a prompt for Bolt to create the application <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This entire process was done hands-off, with Claude navigating the virtual environment <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

The initial attempt required some "handholding" in the prompt to Claude, including providing the specific website for research, though future models might be able to find resources independently <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The prompt also included the workflow JSON and instructions for fulfilling the request <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

Initially, Claude made a small error in its research, only including one of three necessary script tags <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. After a manual correction by the user, Claude successfully updated itself and generated the correct code <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Although the in-browser preview within the virtual machine did not work due to iframe limitations <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>, the application was successfully [[testing_and_deploying_aiassisted_code_projects | deployed]] to Netlify <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. The deployed application correctly displayed the N8N workflow preview widget <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, demonstrating that the AI, with the right external knowledge, could successfully [[building_and_deploying_custom_ai_front_ends | build]] the desired front-end <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## The Future of AI-Assisted Development

This experiment highlights the transformative direction of AI, where AI can research the web for documentation, craft prompts for other LLMs to write code, run commands, and manage environments, all with minimal human intervention <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

As large language models become more powerful, the need for "handholding" will decrease <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Furthermore, the future may involve documentation specifically structured for AI to scrape efficiently <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

The concept of RAG for [[effective_use_of_ai_coding_assistants | AI coding assistance]] is becoming increasingly feasible, either through AI controlling the computer as demonstrated or through direct integrations within [[effective_use_of_ai_coding_assistants | AI IDEs]] like Windsurf <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This experimental stage is rapidly evolving into a very real and impactful reality for software development <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.