---
title: Technical opportunities with MCP for startups
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The Machine Communication Protocol (MCP) has gained significant attention in the AI and startup community <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains MCP as a standard that enables large language models (LLMs) to become more capable <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, drawing parallels to how standards like REST APIs allow engineers to build systems that communicate <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

## The Evolution of LLM Capabilities

### LLMs by Themselves: Limited Capabilities
Initially, LLMs were incapable of performing meaningful actions like sending an email <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. Their primary function was predicting the next word, like completing "My Big Fat Greek" with "Wedding" <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

### LLMs + Tools: The First Evolution
The next evolution involved developers combining LLMs with external tools or APIs <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This allowed LLMs to perform tasks like searching the internet, as seen with Perplexity <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. For example, an LLM could be connected to an automation service like Zapier to create a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

### Challenges with LLMs + Tools
However, combining multiple tools with LLMs quickly becomes frustrating and cumbersome <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. Each tool might use a different "language" or API structure, requiring significant manual work, step-by-step planning, and leading to numerous edge cases where the system can fail or the LLM might hallucinate <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>. This complexity is why a comprehensive "Iron Man level Jarvis assistant" has not yet been achieved <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

## Understanding MCP
MCP is a layer positioned between the LLM and the external services/tools <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. It translates all the different "languages" of various tools into a unified language that the LLM can understand <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. This simplifies the connection process, making it much easier for LLMs to access outside resources <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.

### The MCP Ecosystem
The MCP ecosystem consists of four main components <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>:
*   **MCP Client:** The LLM-facing side, examples include Tempo, Windsurf, and Cursor <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **MCP Protocol:** The two-way connection between the client and the server <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.
*   **MCP Server:** Translates the external service's capabilities for the client <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. Importantly, the MCP server is designed to be built and maintained by the service provider themselves <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.
*   **Service:** The external tool or API the LLM wishes to interact with, such as a database like Convex or Superbase <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.

Anthropic developed MCP with this architecture, essentially tasking service providers with constructing their own MCP servers to enable full access for clients <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.

## Current Challenges

Despite its promise, MCP is still in early stages <a class="yt-timestamp" data-t="17:49:00">[17:49:00]</a>. Setting up an MCP server can be "annoying," involving multiple downloads and local file movements <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>. There are still "kinks that have to be figured out" before it is finalized and polished <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>.

## [[AI opportunities and startup ideas | Startup Opportunities]]

While the standard is still evolving, there are clear [[AI opportunities and startup ideas | startup ideas]] emerging.

### For Technical Founders
One concrete [[AI startup ideas and market opportunities | startup idea]] is an **[[AI opportunities and startup ideas | MCP App Store]]** <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>. This would be a platform where users could browse existing MCP server repositories, and with a simple click, deploy a server, receiving a specific URL to integrate with an MCP client <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>. This would streamline the process of connecting LLMs to various services significantly.

### For Non-Technical Founders
For non-technical individuals, the advice is to **stay updated** with platforms developing MCP capabilities and observe where the standards are heading <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>.

> "Keep very close attention to what the final standard is going to be because once that standard is finalized and all these service providers start to like you know build out their mCP or whatever thing it is you can now start to integrate much seamlessly and much easier" <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>

The current challenge of making LLM-tool integrations cohesive, fast, and limiting hallucinations is very difficult <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>. MCP aims to make these integrations much easier, allowing capabilities to be stacked like Lego pieces <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>.

It is currently too early for most "smart business decisions" related to MCP <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>. The best approach is to observe and learn, waiting for the right moment to strike once the standard is finalized <a class="yt-timestamp" data-t="19:11:00">[19:11:00]</a>. Understanding MCP's mechanics now will provide a strong foundation for future [[emerging_trends_in_startups | opportunities]] as the technology matures <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>.