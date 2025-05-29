---
title: Integration of Large Language Models LLMs with external tools
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Large Language Models (LLMs) have gained significant attention for their predictive text capabilities, but their real power is unlocked when integrated with external tools and services. This integration, however, presents several challenges that the emerging "MCP" standard aims to address.

## Initial Capabilities of LLMs <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>

By themselves, LLMs are limited in their functionality <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. They excel at predicting the next word in a sequence <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, such as completing "My Big Fat Greek" with "Wedding" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. However, they cannot perform meaningful actions like sending an email directly <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> or conducting an internet search <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## Evolution: LLMs + Tools <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>

The next evolution in LLM capabilities involved developers combining LLMs with external tools, often via APIs <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This allowed LLMs to:
*   Search the internet, as seen with platforms like Perplexity AI <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   Perform automated tasks, like creating a spreadsheet entry every time an email is received, by connecting to services such as Zapier or End8 <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Challenges of Tool Integration <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>

While connecting LLMs to tools makes them more powerful, it becomes "frustrating" when building an assistant that needs to perform multiple tasks, such as searching the internet, reading emails, and summarizing <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. This process often feels like "gluing a bunch of different things together" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Key difficulties include:
*   **Cumbersome Integration** Every service provider constructs their APIs differently, requiring varied information and setups <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Scaling Issues** While individual integrations might work, scaling them becomes very difficult <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Maintenance Burden** Updates to an API (e.g., Slack's API) can break complex automation sequences, leading to significant maintenance nightmares <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Hallucination Risk** Despite their coolness, LLMs can be "very very dumb" and may hallucinate or misuse tools if not carefully managed <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

The complexity of combining and stacking these tools cohesively is a major hurdle to creating advanced AI assistants like "Iron Man level Jarvis" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Introducing MCP: A Standard for LLM Integration <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>

MCP (Machine Capabilities Protocol) is introduced as the "next evolution" in integrating LLMs with tools <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. It addresses the challenges of disparate tool languages by acting as a unifying layer <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### What MCP Does <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>
MCP provides a standard way for LLMs to connect and access outside resources <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. It translates the "different languages" of various tools into a "unified language" that the LLM can understand <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This reduces manual work and edge cases where integrations might fail <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

### The MCP Ecosystem <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>
The MCP ecosystem comprises four main components:
1.  **MCP Client**: The LLM-facing side, examples include Tempo, Windswept, and Cursor <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
2.  **MCP Protocol**: The two-way connection standard that facilitates communication between the client and server <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
3.  **MCP Server**: Responsible for translating an external service's capabilities for the client <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
4.  **Service**: The external tool or resource (e.g., a database like Convex or Superbase) that the LLM wants to interact with <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

A key aspect of MCP is that the MCP server is managed by the service provider <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. This means companies offering services (like a database) are responsible for building the MCP server to allow LLMs to access their services fully <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Anthropic is noted for designing this architecture, pushing the burden of integration onto service providers <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

## Technical Challenges and Future Outlook <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>

While promising, setting up an MCP server currently involves "annoying" manual steps and local configurations <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. There are "Kinks that have to be figured out" before the standard is fully polished and finalized <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. Once these issues are resolved, LLMs will become significantly more capable <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

## Startup Opportunities and Advice <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>

### For Technical Individuals <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>
One proposed idea is an "MCP App Store" <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This platform would allow users to browse and deploy existing MCP servers (available as repos) with a click, receiving a URL to paste into an MCP client <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. This would simplify the deployment and connection process significantly.

### For Non-Technical Individuals <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>
It's advised to:
*   **Stay Updated**: Follow platforms that are building out MCP capabilities <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   **Observe and Learn**: The MCP standard is still early <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>, and it's essential to watch for its finalization or potential updates/challenges from other entities like OpenAI <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
*   **Prepare to Act**: Once the standard is finalized and widely adopted by service providers, the ability to [[combining_different_ai_tools_for_effective_development | integrate]] seamlessly will open up significant opportunities for building robust chatbot interfaces and applications with new tools <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

The ability to stack these "Lego pieces" of integration easily will make it simpler to build powerful, cohesive user experiences that currently require extensive engineering effort to limit hallucinations and ensure smooth operation <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.