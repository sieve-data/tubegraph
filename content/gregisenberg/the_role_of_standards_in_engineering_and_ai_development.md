---
title: The role of standards in engineering and AI development
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Standards are crucial in programming and engineering because they enable systems to communicate with each other effectively <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. A well-known example is [[integrating_apis_in_ai_app_development | REST APIs]], which provide a standard for companies to construct their APIs and services, allowing engineers to connect with them <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. Standards create formalities that simplify the engineering process <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

## Limitations of Large Language Models (LLMs)

By themselves, Large Language Models (LLMs) are incapable of performing meaningful actions beyond predicting the next word <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>, <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. For example, an LLM cannot send an email on its own; it can only tell you it's incapable <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. Their primary function is predicting text, such as completing "My Big Fat Greek" with "wedding" <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

## Evolution: LLMs + Tools

The next evolution involved developers combining LLMs with external tools, such as APIs <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This allowed LLMs to perform tasks like searching the internet (e.g., Perplexity) <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. Other examples include connecting an LLM to automation services like Zapier or Integromat to perform tasks such as creating a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.

However, integrating multiple tools with LLMs can be frustrating and cumbersome <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. Building an assistant that handles searching the internet, reading emails, and summarizing becomes an extensive process of "gluing" different tools together <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. This complexity is why a comprehensive "Iron Man level Jarvis assistant" doesn't yet exist <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

Challenges with this approach include:
*   Difficulty in connecting tools, as each service provider constructs their APIs differently with varying requirements <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.
*   Manual work, step-by-step planning, and managing edge cases where the system can fail <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.
*   Vulnerability to external changes; for example, if Slack or a text service updates its API, it can break existing automations, making maintenance a "nightmare" <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
*   Despite their capabilities, LLMs can be "very very dumb" on their own <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.

## Introducing MCP: A Unified Standard

MCP (Multi-tool Coordination Protocol) is presented as the next evolution, addressing the challenges of integrating tools with LLMs <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>, <a class="yt-timestamp" data-t="14:34:00">[14:34:00]</a>. It acts as a translation layer between the LLM and various services and tools <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. This layer unifies the different "languages" of various tools into a single language that the LLM can understand, making integration much simpler <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.

### The MCP Ecosystem
The MCP ecosystem consists of four main components <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>:
1.  **MCP Client**: The client-facing or LLM-facing side of the ecosystem (e.g., Tempo, Wind Surf, Cursor) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
2.  **MCP Protocol**: The two-way connection between the client and the server <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.
3.  **MCP Server**: Translates the external service's capabilities to the client <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.
4.  **Service**: The external tool or data source (e.g., a database like Convex or Supabase) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>, <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.

A key aspect of MCP's architecture, championed by Anthropic, is that the MCP server is managed by the service provider <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. This means if a company offers a database, it is their responsibility to build the MCP server to allow LLMs to access it <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>. This encourages external service providers to build out different MCP servers <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.

MCP, therefore, is essentially a standard that allows LLMs to become more capable by communicating efficiently with services <a class="yt-timestamp" data-t="12:45:00">[12:45:00]</a>, <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>. It's not a complex new law of physics, but a standard for LLMs <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.

## Current State and Future Implications

While MCP is a significant development, it faces technical challenges, such as the cumbersome setup of MCP servers on clients <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>. However, once these "kinks" are resolved and the standard is polished, LLMs will become even more capable <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>. This allows for easier [[integrating_apis_in_ai_app_development | integration of APIs in AI app development]] and enables building [[best_practices_for_utilizing_ai_tools_in_app_development | AI tools in app development]] as cohesive "Lego pieces" that can be continuously stacked <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>.

The widespread adoption of a standard like MCP means that service providers will build their offerings in a way that allows other developers and businesses to connect seamlessly <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

## Startup Opportunities

Historically, the popularization of protocols (like HTTPS or SMTP) has led to the creation of many large businesses <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. Similarly, MCP could open new opportunities.

For technical individuals, an "MCP App Store" could be a viable idea <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>. This platform would allow users to browse different MCP servers, view their GitHub code, and deploy them with a single click, receiving a URL to integrate with an MCP client <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>.

For [[nonengineers_building_software_with_ai | non-technical individuals]] and business owners, the recommendation is to closely monitor platforms that are building out MCP capability and observe where the standards are heading <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. It's still early, and the ultimate standard (whether MCP is finalized or challenged by another) is uncertain <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>. However, understanding how this works is key to understanding future developments <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>. While immediate "crazy business opportunities" may not be apparent for the [[nonengineers_building_software_with_ai | non-technical person]], staying informed will enable them to act when the right time and finalized standard emerge <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>.