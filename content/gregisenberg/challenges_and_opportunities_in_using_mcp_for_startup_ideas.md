---
title: Challenges and opportunities in using MCP for startup ideas
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

MCP (Multimodal Communication Protocol) is a technical concept that has gone "completely viral" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, representing a significant evolution in how Large Language Models (LLMs) interact with the outside world <a class="yt-timestamp" data-t="08:55:04">[08:55:04]</a>. Professor Ross Mike explains MCP as a crucial standard designed to make LLMs more capable <a class="yt-timestamp" data-t="01:54:07">[01:54:07]</a>, addressing current frustrations in AI development <a class="yt-timestamp" data-t="05:09:12">[05:09:12]</a>.

## The Evolution of LLM Capabilities

Initially, LLMs were "incapable of doing anything meaningful" by themselves <a class="yt-timestamp" data-t="02:42:04">[02:42:04]</a>. Their primary function was "predicting the next text" <a class="yt-timestamp" data-t="03:25:29">[03:25:29]</a>, such as completing "My Big Fat Greek" with "Wedding" <a class="yt-timestamp" data-t="03:30:08">[03:30:08]</a>. They could not, for example, send an email <a class="yt-timestamp" data-t="02:53:07">[02:53:07]</a>.

The "next Evolution was developers figured out how to take LLMs and combine them with tools" <a class="yt-timestamp" data-t="03:44:03">[03:44:03]</a>. Tools can be thought of as APIs <a class="yt-timestamp" data-t="03:55:08">[03:55:08]</a>, allowing LLMs to perform external actions like searching the internet (e.g., Perplexity) <a class="yt-timestamp" data-t="04:00:23">[04:00:23]</a> or connecting to automation services like Zapier or End8 <a class="yt-timestamp" data-t="04:52:13">[04:52:13]</a>.

### Challenges with LLMs + Tools
While connecting LLMs to tools made them "a bit more powerful" <a class="yt-timestamp" data-t="03:34:02">[03:34:02]</a>, it presents significant challenges:
*   **Cumbersome Integration**: It becomes "very frustrating" when trying to build an assistant that performs multiple tasks, requiring developers to glue "a bunch of different tools" to LLMs <a class="yt-timestamp" data-t="05:09:12">[05:09:12]</a>.
*   **Lack of Cohesion**: Stacking tools and making them "cohesive" and "work together is a nightmare" <a class="yt-timestamp" data-t="05:40:11">[05:40:11]</a>.
*   **Manual Work & Edge Cases**: This approach involves "a lot of manual work," "step-by-step planning," and is prone to failure due to "edge cases" <a class="yt-timestamp" data-t="09:38:35">[09:38:35]</a>.
*   **Maintenance**: If an external service updates its API, it can "become a nightmare" and "terrifying" for the integrated system <a class="yt-timestamp" data-t="10:18:21">[10:18:21]</a>.
*   **LLM Hallucination**: Developers must ensure the LLM doesn't "hallucinate or do something stupid" <a class="yt-timestamp" data-t="06:26:40">[06:26:40]</a>, as LLMs can be "very very dumb" on their own <a class="yt-timestamp" data-t="06:30:35">[06:30:35]</a>.

These challenges explain why an "Iron Man level Jarvis assistant" doesn't yet exist <a class="yt-timestamp" data-t="05:30:22">[05:30:22]</a>.

## Introducing MCP: A Unified Language for LLMs
MCP is best understood as a "layer between your LLM and the services and the tools" <a class="yt-timestamp" data-t="08:38:29">[08:38:29]</a>. This layer "translates all those different languages into a unified language that makes complete sense to the LLM" <a class="yt-timestamp" data-t="08:48:20">[08:48:20]</a>. Essentially, MCP is a "standard for LLMs" <a class="yt-timestamp" data-t="15:29:14">[15:29:14]</a>, making them "more capable" <a class="yt-timestamp" data-t="14:24:49">[14:24:49]</a>.

### The MCP Ecosystem
The MCP ecosystem consists of four main components <a class="yt-timestamp" data-t="11:02:18">[11:02:18]</a>:
1.  **MCP Client**: The LLM-facing side of the ecosystem. Examples include Tempo, Wind surf, and Cursor <a class="yt-timestamp" data-t="11:16:03">[11:16:03]</a>.
2.  **MCP Protocol**: The "two-way connection between the client and the server" <a class="yt-timestamp" data-t="11:32:02">[11:32:02]</a>.
3.  **MCP Server**: This component "translates that external service, its capabilities, and what it can do to the client" <a class="yt-timestamp" data-t="11:38:09">[11:38:09]</a>.
4.  **Service**: The external tool or data source (e.g., a database, Slack, a search engine) <a class="yt-timestamp" data-t="11:41:26">[11:41:26]</a>.

Anthropic, the creator of MCP, strategically placed the responsibility of constructing the MCP server "in the hands of the service provider" <a class="yt-timestamp" data-t="12:00:08">[12:00:08]</a>. This encourages service providers to build their own MCP servers, allowing LLMs to access their services more easily <a class="yt-timestamp" data-t="12:31:07">[12:31:07]</a>.

## Current Challenges with MCP
While MCP is a big deal, it's not "all sunshine and rainbows" yet <a class="yt-timestamp" data-t="13:50:06">[13:50:06]</a>.
*   **Setup Annoyance**: Setting up an MCP server can be "annoying" <a class="yt-timestamp" data-t="13:59:04">[13:59:04]</a>, involving "a lot of downloading," moving files, and copying data locally <a class="yt-timestamp" data-t="14:01:03">[14:01:03]</a>.
*   **Early Stages**: The technology is still in its early stages with "some Kinks that have to be figured out" <a class="yt-timestamp" data-t="14:08:29">[14:08:29]</a>. The standard might be updated or challenged by new ones <a class="yt-timestamp" data-t="17:41:43">[17:41:43]</a>.

Once these issues are "figured out," "finalized," and "polished," LLMs will become "more capable" <a class="yt-timestamp" data-t="14:09:30">[14:09:30]</a>.

## [[startup_ideas_and_brainstorming | Startup Ideas]] and Opportunities with MCP

The advent of a popularized protocol like MCP opens up significant [[entrepreneurship_and_startup_ideas | entrepreneurship and startup ideas]] <a class="yt-timestamp" data-t="16:04:36">[16:04:36]</a>.

### For Technical Persons
One specific [[startup_ideas_and_brainstorming | startup idea]] is an "MCP App Store" <a class="yt-timestamp" data-t="16:38:29">[16:38:29]</a>. This would be a website where users could <a class="yt-timestamp" data-t="16:50:56">[16:50:56]</a>:
*   Browse "different MCP servers" (repositories) <a class="yt-timestamp" data-t="16:50:56">[16:50:56]</a>.
*   View GitHub code <a class="yt-timestamp" data-t="17:09:23">[17:09:23]</a>.
*   "Click like install or deploy" to instantly deploy a server <a class="yt-timestamp" data-t="17:10:48">[17:10:48]</a>.
*   Receive a specific URL to paste into an MCP client <a class="yt-timestamp" data-t="17:14:24">[17:14:24]</a>.

This kind of platform would simplify the current complex setup process for MCP servers <a class="yt-timestamp" data-t="13:59:04">[13:59:04]</a>.

### For Non-Technical Persons
For individuals who are not technical, the advice is to "stay up to date with the platforms that are building out MCP capability" <a class="yt-timestamp" data-t="17:31:07">[17:31:07]</a> and "just see where the standards are going" <a class="yt-timestamp" data-t="17:37:37">[17:37:37]</a>.

> "I would say keep very close attention to what the final standard is going to be because once that standard is finalized and all these service providers start to like you know build out their mCP or whatever thing it is you can now start to integrate much seamlessly and much easier" <a class="yt-timestamp" data-t="17:52:13">[17:52:13]</a>.

It is crucial to "sit and you watch and you're just observing and learning and when the right thing at the right time happens you strike" <a class="yt-timestamp" data-t="19:11:39">[19:11:39]</a>. The current stage is very early, and it's not yet time to make "crazy business opportunities" for a non-technical person <a class="yt-timestamp" data-t="19:21:00">[19:21:00]</a>, especially since the standard might still evolve <a class="yt-timestamp" data-t="19:27:03">[19:27:03]</a>. However, understanding MCP now will provide a foundational knowledge for future developments <a class="yt-timestamp" data-t="19:33:04">[19:33:04]</a>.