---
title: Limitations and enhancements of large language models LLMs
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

## Overview of LLM Capabilities and Limitations

Large Language Models (LLMs) are foundational AI systems that, on their own, have significant limitations despite their advanced capabilities in text prediction <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. An LLM's core function is to predict the next word in a sequence based on its training data <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. For example, if given "My Big Fat Greek," an LLM would predict "Wedding" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

However, LLMs by themselves are "incapable of doing anything meaningful" in terms of external actions <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. They cannot, for instance, send an email directly or perform specific tasks on a user's behalf <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. While they excel at answering questions or generating creative text like poems, they are described as "very very dumb" without external connections <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## Evolution: LLMs with External Tools

The first significant enhancement to LLM capabilities involved developers combining them with external "tools" or APIs (Application Programming Interfaces) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This integration allows LLMs to perform actions beyond simple text generation:
*   **Internet Search:** Chatbots like Perplexity can search the internet by connecting to external search services <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Automation:** They can interact with services like Zapier or End8 to automate tasks, such as creating a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **API Interaction:** LLMs can be given access to [[evolution_and_integration_of_llms_with_external_tools_and_services | external services]] via APIs, making them more capable <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Challenges with Tool Integration
While [[evolution_and_integration_of_llms_with_external_tools_and_services | connecting LLMs to external tools]] makes them more powerful, this approach presents several significant challenges:
*   **Complexity:** Building an assistant that performs multiple tasks (e.g., searching, reading emails, summarizing) becomes "frustrating" <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. It often feels like "gluing a bunch of different things together" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Lack of Standardization:** Each service provider constructs their APIs differently, requiring custom integration for each tool. This is likened to each tool speaking a different language (English, Spanish, Japanese) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Maintenance Burden:** Updates to external APIs can break existing automations, turning maintenance into a "nightmare" <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This requires significant engineering hours <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Reliability:** LLMs can still "hallucinate or do something stupid" even when integrated with tools <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Absence of Jarvis-level AI:** The difficulty of combining and stacking these tools cohesively is a major reason why an "Iron Man level Jarvis assistant" doesn't yet exist <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## The Next Evolution: MCP (Model Control Protocol)

MCP is seen as the "next evolution" in enhancing LLM capabilities by addressing the challenges of tool integration <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

### What is MCP?
MCP is a standard that acts as a "layer" between an LLM and external services/tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Its primary function is to translate the "different languages" of various tools into a "unified language that makes complete sense to the LLM" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

In essence, MCP makes it simple for LLMs to connect to and access diverse outside resources, such as databases like Convex or Superbase <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This eliminates the need for extensive manual work, step-by-step planning, and reduces the likelihood of failures from edge cases <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

> [00:12:29] "Anthropic in a way sort of said listen we want our llms to be more powerful more capable uh but it's your job to figure this out."

### The MCP Ecosystem
The MCP ecosystem consists of:
*   **MCP Client:** The LLM-facing side of the ecosystem, exemplified by tools like Tempo, Windsurf, or Cursor <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **MCP Protocol:** The two-way communication standard between the client and server <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **MCP Server:** This component translates the external service's capabilities to the client <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. A key aspect is that the MCP server is built and maintained by the service provider (e.g., a database company would build an MCP server for their database) <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

### Benefits of MCP
*   **Unified Communication:** MCP creates a layer where LLMs and services can communicate efficiently <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Increased LLM Capability:** It directly contributes to making LLMs "more capable" by allowing them to perform important tasks <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Scalability and Growth:** By establishing a standard, MCP allows companies to scale and grow, making it easier for other developers and businesses to connect with their services <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **Simplified Integration:** Integrations become significantly easier, resembling "Lego pieces that you can continue to stack" <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

### Current Challenges and Future Outlook for MCP
While MCP is a significant advancement, it's still in its early stages <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Setup Annoyances:** Setting up an MCP server can be "annoying," involving multiple manual steps like downloading and moving files <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Standardization Evolution:** The MCP standard may still evolve, be updated, or even be challenged by a better alternative <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

The finalization of a standard like MCP will significantly impact how LLMs integrate with external services, leading to more seamless and robust AI applications <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.