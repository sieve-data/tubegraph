---
title: Comparison of MCPs with Existing Standards
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

MCPs (Machine-Readable Common Protocols) are emerging as a significant topic in the field of artificial intelligence, particularly concerning Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains MCPs as a new standard designed to enhance the capabilities of LLMs <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## The Importance of Standards in Programming

In programming, standards are crucial because they enable engineers to build systems that can communicate with each other efficiently <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>, <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. A widely recognized example is REST APIs, which provide a standard framework that companies follow when constructing their APIs and services <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. This standardization makes it easier for engineers to connect with different services <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

## Limitations of LLMs and Current Tool Integration

By themselves, LLMs are "incapable of doing anything meaningful" beyond predicting the next word <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. For example, an LLM cannot send an email on its own <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

The initial evolution involved developers combining LLMs with external tools, such as APIs, to expand their functionality <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. This allows LLMs to perform actions like searching the internet, as seen with tools like Perplexity or Brave search <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>. Services like Zapier or End8 are used to build automations that connect an LLM to external services, making them "a bit more meaningful" <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>, <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

However, integrating multiple tools with an LLM is a "frustrating," "cumbersome," and "annoying" process <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>, <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>. Each service provider might construct their APIs differently, requiring varying information to be passed, which feels like "gluing a bunch of different things together" <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>, <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. This complexity is why an "Iron Man level Jarvis assistant" is not yet common <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>. Manual work, step-by-step planning, and dealing with edge cases make current integration difficult <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>. Furthermore, updates to a service's API can break existing automations, making maintenance a "nightmare" <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>, <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.

## MCPs as a Unified Standard for LLMs

[[understanding_mcps_and_their_importance | MCPs]] introduce a standard that unifies communication between LLMs and external services <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. Think of MCPs as a layer between the LLM and its tools that translates all their different "languages" into a single, unified language that the LLM understands <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>, <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. This simplifies the LLM's ability to connect and access outside resources <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

The [[understanding_mcps_and_their_importance | MCP ecosystem]] consists of:
*   **MCP client**: The LLM-facing side, with examples including Tempo, Wind surf, and Cursor <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **MCP protocol**: The two-way connection between the client and server <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.
*   **MCP server**: Translates the capabilities of an external service to the client <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.
*   **Service**: The external tool or resource, such as a database (e.g., Convex, Superbase) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>, <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>.

Anthropic, in developing this architecture, has put the responsibility of constructing the MCP server into the hands of the service providers themselves <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>, <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. This means service providers are building MCP servers to ensure their services can be accessed by LLMs through the MCP protocol <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>.

## Current Challenges and Future Outlook

While MCPs represent a significant step in making LLMs [[mcps_and_their_role_in_making_llms_more_capable | more capable]], there are [[the_challenges_of_implementing_mcp_servers | technical challenges]]. Setting up an MCP server can be "annoying," involving multiple file downloads and local configurations <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>. These "kinks" need to be resolved or the standard polished before MCPs can fully realize their potential <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>.

The introduction of MCPs is comparable to other foundational protocols like HTTPS or SMTP, which spawned many businesses <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>, <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>. For technical individuals, there are [[startup_opportunities_around_mcps | startup opportunities]], such as an "MCP App Store" where users could easily deploy MCP servers for various services <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.

For non-technical individuals and those evaluating [[startup_opportunities_around_mcps | startup ideas]], it is advised to stay updated on platforms building MCP capabilities and observe how the standard evolves <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. The space is still in its early stages <a class="yt-timestamp" data-t="17:49:00">[17:49:00]</a>. Once the standard is finalized and adopted by service providers, integrating LLMs will become much more seamless, akin to connecting "Lego pieces" <a class="yt-timestamp" data-t="18:05:00">[18:05:00]</a>, <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.