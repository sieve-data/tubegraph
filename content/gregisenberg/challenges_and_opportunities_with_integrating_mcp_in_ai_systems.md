---
title: Challenges and opportunities with integrating MCP in AI systems
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The concept of MCPs (Multi-Capability Protocols) has gained significant traction, but their purpose and the opportunities they present are often unclear to many <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains MCPs as a crucial standard for making Large Language Models (LLMs) more capable and integrated with external services <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Limitations of LLMs Alone <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>

By themselves, LLMs are fundamentally incapable of performing meaningful actions beyond predicting the next text <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For example, an LLM cannot send an email or search the internet directly <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Their core function is to predict the most probable next word in a sequence, such as completing "My Big Fat Greek" with "wedding" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Evolution: LLMs + Tools <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>

The first significant evolution involved developers combining LLMs with external tools, such as APIs <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This enabled LLMs to perform actions like searching the internet (e.g., Perplexity) or automating tasks through services like Zapier or N8N <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. For instance, an LLM could be connected to an automation to create a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Challenges with LLM + Tools <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

Despite the increased capability, integrating multiple tools with LLMs presents significant [[overcoming_challenges_in_aiassisted_app_development | challenges]]:

*   **Complexity of Integration**: Building an assistant that performs multiple functions, like searching the internet, reading emails, and summarizing, requires "gluing a bunch of different tools" together <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This process can be cumbersome and frustrating <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Lack of Standardization**: While REST APIs provide a standard for how APIs work, each service provider constructs their APIs differently <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. This means different information has to be passed, making integration feel like connecting tools that speak different languages <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Maintenance Nightmare**: Changes in external service APIs can break existing automations <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This requires constant manual work, step-by-step planning, and can lead to many edge cases where the system fails <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **LLM Limitations**: Even with tools, LLMs can "hallucinate" or act "dumb" <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Difficulty Scaling**: While possible for simple tasks, scaling integrations with numerous disparate tools becomes very difficult <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. This is a key reason why a comprehensive "Iron Man level Jarvis assistant" doesn't exist yet <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## What is MCP? <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>

MCP acts as an intermediary layer between an LLM and external services or tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Its primary function is to translate the various "languages" of different tools into a single, unified language that the LLM can understand <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This makes it significantly simpler for LLMs to connect with and access outside resources like databases <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### The MCP Ecosystem <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>

The MCP ecosystem comprises:
*   **MCP Client**: The LLM-facing component (e.g., Tempo, Wind Surf, Cursor) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **MCP Protocol**: The two-way communication standard between the client and server <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **MCP Server**: Responsible for translating the capabilities of an external service to the client <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

Notably, companies like Anthropic have designed the MCP architecture such that the **service provider** is responsible for building and maintaining the MCP server for their specific service <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This pushes the burden of integration to the service side, encouraging standardization across the ecosystem <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

## Benefits and Opportunities <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>

MCP is considered the "next evolution" in making LLMs more capable <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   **Enhanced LLM Capabilities**: By unifying communication, MCP allows LLMs to access and perform actions with external services much more efficiently <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Seamless Integration**: It simplifies the integration process, acting like "Lego pieces" that can be easily stacked to add more functionalities <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
*   **Standardization**: MCP is a standard that appears to be adopted by many companies and engineers, which is crucial for scalable and interoperable systems <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

## Current Challenges with MCP <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>

Despite its potential, MCP is still in its early stages and faces [[limitations_and_challenges_of_using_manis_ai | challenges]]:
*   **Setup Complexity**: Setting up an MCP server can be "annoying" due to manual downloading and file management <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Evolving Standard**: The standard is not yet finalized and may undergo updates or even be challenged by competing standards (e.g., from OpenAI) <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>, <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

## Startup Opportunities <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>

The emergence of a standardized protocol like MCP presents [[opportunities_and_challenges_in_the_ai_app_development_market | new business opportunities]]:
*   **MCP App Store**: A potential idea is an "MCP App Store" where users can browse, install, and deploy MCP servers from various repositories, receiving a URL to integrate with their MCP clients <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This would streamline the adoption and deployment of MCP servers.

For non-technical individuals, the key is to stay updated on platforms that are building MCP capabilities and observe how the standard evolves and finalizes <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>, <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. Once the standard is solidified and widely adopted by service providers, integrating and building solutions will become significantly easier, enabling new innovations in AI-powered services <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. While it's too early for "crazy business opportunities" for non-technical users, understanding MCP now means being prepared to "hit the ground running" when the standard matures <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.