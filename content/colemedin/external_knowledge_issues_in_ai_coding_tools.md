---
title: External knowledge issues in AI coding tools
videoId: R6AYmqcOXaw
---

From: [[colemedin]] <br/> 

AI coding assistants, whether browser-based like Bolt or Autodev, or integrated into an IDE like Windsurf or Cursor, are powerful tools that can save hours when building application prototypes <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. However, a significant [[issues_with_current_ai_coding_assistants | major flaw]] with these tools is their lack of [[limitations_of_current_ai_coding_assistants | external knowledge]] for crucial information, such as library documentation <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This means they are often not up-to-date with many things developers might want to code <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## The Problem: Lack of External Knowledge

The primary [[issues_with_current_ai_coding_assistants | issue]] with current AI coding assistants is their inability to access real-time or specialized external documentation <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This is because large language models (LLMs) like Claude 3.5 Sonnet, used in tools like Bolt, do not have access to this information <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Case Study: N8N Demo Library

To illustrate this [[limitations_of_current_ai_coding_assistants | limitation]], an experiment was conducted using Bolt to build an application around a small, relatively new library called N8N demo <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This library is used by N8N to display preview widgets for AI automation workflows on their website, and provides specific instructions for HTML inclusion and script tags for JavaScript <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

When prompted to build a frontend to display an N8N workflow using the N8N demo tool, Bolt (and any other AI coding assistant like Cursor, Windsurf, or Autodev) completely failed <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. It could not install dependencies correctly, tried to fetch from npm unsuccessfully, and produced no preview <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Even attempts to self-correct failed because the LLM simply lacked the external knowledge of this specific library <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Overcoming Limitations with Retrieval-Augmented Generation (RAG)

The solution to this [[limitations_of_current_ai_coding_assistants_and_overcoming_them_with_context_7 | external knowledge problem]] is akin to implementing Retrieval-Augmented Generation (RAG) for an AI coding assistant <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This approach involves:
*   Going out to the internet to fetch relevant information, such as how to use and install a library <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   Feeding this information into the prompt to augment it, providing the necessary context <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

This functionality could be built directly into platforms like Bolt, allowing them to research the web before fulfilling a request <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Alternatively, an artificial intelligence could control the computer, conduct the research, and then inject its findings into the AI coding assistant's prompt before the code build begins <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Experimental Solution: Claude API for Computer Use

An experimental approach to implement RAG for AI coding assistants involves [[using_external_knowledge_in_ai_coding | using]] the Claude API for computer use <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### How it Works

The Claude API for computer use allows Claude to control a computer, performing actions such as typing into input boxes, searching the web, and clicking through applications <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This is a first-of-its-kind capability <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

For security, the reference implementation of this API runs within a virtual machine in the browser <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Users can prompt Claude on one side of the UI, and the virtual machine operates on the other, ensuring a safe test environment <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Demonstration: Claude Researching N8N Demo for Bolt

In a demonstration, the Claude computer use API was tasked with researching the N8N demo component, figuring out its usage and installation, and then injecting this information into a prompt for Bolt to create the application <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. The user remained hands-off while Claude navigated the environment <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

Initially, Claude's research slightly missed some required script tags <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. However, after a small correction from the user, Claude successfully updated the prompt <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

The application, once built, could not display the N8N workflow preview within the Bolt web container due to iframe limitations <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. However, upon deployment to Netlify, the N8N workflow preview widget successfully loaded and functioned as intended, demonstrating the [[effective_use_of_ai_coding_assistants | successful integration]] of external knowledge <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

This experiment showcased how an LLM can research web documentation, craft a prompt with the found information, and feed it to another LLM to write code and set up environments <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Future Direction of AI Coding

This experimental demonstration provides a glimpse into the future of AI in coding <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Soon, developers will be able to be "hands off the wheel," with AI even researching to assist itself <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. The need for user "hand-holding" will decrease as LLMs become more powerful <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

There is a future where documentation on the web might be specifically created for AI to scrape <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. The concept of RAG for [[using_ai_coding_assistance | AI coding assistance]] will become very doable, either through computer control as demonstrated or through direct integrations within AI IDEs like Windsurf <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. This highly experimental technology is expected to become a very real and significant part of AI development rapidly <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.