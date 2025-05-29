---
title: Exploring Large Language Models and their limitations
videoId: 6GVRFV940Qs
---

From: [[amiteshanand]] <br/> 

This article demonstrates how Large Language Models (LLMs) like GPT-4o LM can have limitations regarding knowledge of recent or niche topics, and how tools like Pieces Live Context can overcome these.

## Limitations of Large Language Models <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

When querying an LLM, such as GPT-4o LM, about a recently open-sourced topic like "Mop" (a Python-based UI framework), the model may not have this information in its knowledge base <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. For instance, when asked "What is Mop?", the LLM incorrectly identifies it as "Management Equity Stock Option Plan" <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, indicating it does not know about the UI framework <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Overcoming Limitations with Pieces Live Context <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

To address this limitation, Pieces Copilot features a "Live Context" capability <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### How Live Context Works <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
1.  **Enable Live Context:** Users activate the "Live Context" feature within Pieces Copilot <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  **Activate Work Stream Pattern (WSP):** Alongside Live Context, the "Work Stream Pattern" (WSP) algorithm must also be enabled <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. WSP is a feature running with Pieces that allows Live Context to function properly <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>, <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
3.  **Context Gathering:** With WSP active, Pieces Copilot observes the user's screen activity, such as scrolling through a webpage, and extracts relevant context from it <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Improved LLM Performance <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
After Live Context is enabled and context is gathered, the LLM can correctly answer questions <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. For example, when asked "What is Mop?" again, the LLM correctly defines "Mop" as a Python-based framework designed for rapidly building web applications, demos, and internal apps <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

The LLM can also answer follow-up questions, such as how to set up and install Mop, by providing step-by-step instructions <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. This demonstrates how Pieces Live Context enhances the LLM's capability by providing real-time contextual information <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.