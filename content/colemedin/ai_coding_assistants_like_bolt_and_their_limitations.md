---
title: AI coding assistants like Bolt and their limitations
videoId: R6AYmqcOXaw
---

From: [[colemedin]] <br/> 

[[AI coding assistants]] are powerful tools, available both as browser-based platforms like Bolt, Autodev <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, and as Integrated Development Environments (IDEs) such as Windsurf or Cursor <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. They are highly effective, saving countless hours and enabling the rapid development of application prototypes <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Current Limitations: Lack of External Knowledge
A significant drawback of current [[AI coding assistants]], including Bolt, is their lack of external knowledge <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This means they often do not have up-to-date information on crucial resources like library documentation <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This limitation leads to failures when trying to code with newer or less common libraries <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Demonstration with N8N Demo Library
To illustrate this limitation, an experiment was conducted using Bolt to build a frontend application that displays an N8N workflow with the `N8N demo` tool <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The `N8N demo` library is a relatively new and smaller library that allows N8N to display preview widgets for its AI automation workflows <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

Even though installation guides and instructions are available, a large language model (LLM) like Claude 3.5 Sonnet, used in Bolt, does not have access to this specific information <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. When prompted with the request and the JSON for the workflow, Bolt completely failed to build the application because it lacked the necessary knowledge about the `N8N demo` library <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This resulted in failed dependency installations and no preview <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This problem is not unique to Bolt but applies to other [[ai_coding_assistants]] like Cursor, Windsurf, and Autodev, as it stems from the fundamental lack of external knowledge <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Overcoming Limitations: AI-Controlled Research

To address the issue of limited external knowledge, a solution akin to Retrieval Augmented Generation (RAG) for [[ai_coding_assistants]] is needed <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This involves an AI capable of researching the internet for relevant information, such as library documentation and installation methods, and then augmenting the prompt for the [[AI coding assistants]] with this context <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

One approach is to integrate web research capabilities directly into platforms like Bolt, allowing them to research before fulfilling a request <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Alternatively, an artificial intelligence could control the computer, performing research and then injecting its findings into the prompt of an [[AI coding assistants]] like Bolt <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### Using Claude API for Computer Use
The Claude API for computer use allows an LLM to control a computer, performing actions like typing, web searching, and clicking through applications <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This experimental API facilitates the research and integration of external knowledge <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

In a demonstration, the Claude API was used within a virtual machine environment to:
1.  Research the `N8N demo` component, figuring out its usage and installation <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Inject this researched information into a prompt for Bolt <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
3.  Have Bolt create the full application based on the augmented prompt <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

While the process required some "handholding" in the prompt to Claude due to its experimental nature <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, and an initial correction was needed for missing script tags <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, the overall process was successful. The AI, without direct human intervention after the initial prompt, navigated to the `N8N demo` website, extracted the necessary information, and then used that information to instruct Bolt to create the correct application <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The resulting N8N workflow preview was successfully displayed after deployment to Netlify <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

## Future of [[AI Coding Assistants]]
This experiment highlights the future direction of [[AI coding assistants]]. The ability for AI to research and assist itself, essentially being "hands-off the wheel," is a significant step forward <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. As LLMs become more powerful, they will require less human guidance <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. This could also lead to a future where web documentation is specifically structured for AI to scrape effectively <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. The concept of RAG for [[ai_coding_assistants]] is becoming increasingly feasible, either through direct AI computer control or integrated functionalities within IDEs like Windsurf <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.