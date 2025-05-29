---
title: The evolution of large language models LLMs with tools and MCP
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The landscape of artificial intelligence, particularly concerning Large Language Models (LLMs), is undergoing rapid transformation. Initially, LLMs had significant limitations in performing meaningful tasks beyond generating text. However, with the integration of external tools and, more recently, the advent of the [[What is Model Context Protocol MCP and why it matters|Model Context Protocol (MCP)]], their capabilities are expanding dramatically <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

## Initial Capabilities of LLMs

By themselves, LLMs are limited to predicting the next word in a sequence <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. For example, an LLM trained on sufficient data can complete "My Big Fat Greek..." with "Wedding" <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. They excel at answering questions or generating creative text like poems <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>, <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>. However, LLMs are fundamentally incapable of performing actions such as sending an email or executing a specific task on behalf of a user <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

## The First Evolution: LLMs with Tools

The significant leap in LLM utility came when developers learned to combine LLMs with external tools, often through Application Programming Interfaces (APIs) <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>, <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. This integration allows LLMs to interact with the outside world.

Examples of such integrations include:
*   **Internet Search:** Chatbots like Perplexity can search the internet and present information, even though the LLM itself doesn't possess this capability <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>, <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
*   **Automation:** Connecting an LLM to automation services like Zapier or N8N allows it to perform tasks such as creating a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>, <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

While these integrations make LLMs more powerful and "meaningful" <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>, they introduce a new set of challenges <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.

## Challenges with Multi-Tool Integration

Integrating multiple tools with LLMs can be cumbersome and frustrating <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. Building an assistant that can perform diverse actions like searching the internet, reading emails, and summarizing content often involves "gluing" together many different tools <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>, <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.

Key issues include:
*   **Lack of Standardization:** While general API standards like REST exist, each service provider constructs their APIs differently, requiring varying information to be passed and different setups <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>, <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. This is akin to tools speaking different languages <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Complexity and Cumbersomeness:** Making multiple tools work cohesively with an LLM, especially at scale, is a significant engineering challenge <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>, <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>, <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. This difficulty is why a "Jarvis-level" AI assistant remains elusive <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>, <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.
*   **Maintenance Headaches:** Updates to a service's API can break integrated automations, leading to extensive debugging and maintenance <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>, <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

## The Rise of [[What is Model Context Protocol MCP and why it matters|Model Context Protocol (MCP)]]

[[What is Model Context Protocol MCP and why it matters|MCP]] is designed to address the complexities of tool integration by providing a unified communication standard for LLMs and external services <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>, <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. It acts as a translation layer, converting the "different languages" of various tools into a single, cohesive language that the LLM can understand <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>, <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.

### [[What is Model Context Protocol MCP and why it matters|MCP]] Ecosystem Components

The [[What is Model Context Protocol MCP and why it matters|MCP]] ecosystem consists of four main parts <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>:
1.  **[[What is Model Context Protocol MCP and why it matters|MCP]] Client:** This is the LLM-facing side, used by applications like Tempo, Wind Surf, and Cursor <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>, <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>.
2.  **[[What is Model Context Protocol MCP and why it matters|MCP]] Protocol:** The two-way communication standard that facilitates interaction between the client and server <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>, <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
3.  **[[What is Model Context Protocol MCP and why it matters|MCP]] Server:** This component translates the capabilities of an external service so the [[What is Model Context Protocol MCP and why it matters|MCP]] client (and thus the LLM) can understand them <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>, <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. Critically, the responsibility for constructing the [[What is Model Context Protocol MCP and why it matters|MCP]] server falls to the service provider <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>, <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>. This strategic decision by developers like Anthropic pushes external service providers to build their own [[What is Model Context Protocol MCP and why it matters|MCP]] integrations <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>, <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.
4.  **Service:** The external tool or database that the LLM interacts with, such as Convex or Supabase <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>, <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>, <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>, <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>.

[[What is Model Context Protocol MCP and why it matters|MCP]] simplifies the process for LLMs to connect and access outside resources <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. It removes much of the manual work, step-by-step planning, and edge case handling previously required for integrating tools <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>, <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

## Current State and Future Implications

While [[What is Model Context Protocol MCP and why it matters|MCP]] holds immense promise, it is still in its early stages. There are [[Challenges and opportunities with integrating MCP in AI systems|technical challenges]], such as the current annoyance of setting up [[What is Model Context Protocol MCP and why it matters|MCP]] servers with existing clients, often involving manual file transfers and local configurations <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>, <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. These "kinks" need to be resolved for wider adoption <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>.

However, once the [[What is Model Context Protocol MCP and why it matters|MCP]] standard is finalized and polished, or a superior standard emerges, LLMs are expected to become significantly more capable <a class="yt-timestamp" data-t="14:12:00">[14:12:00]</a>, <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>, <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>. This standardization will allow for more seamless integration of "Lego pieces" (tools) that can be easily stacked to create complex AI systems <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.

For individuals interested in startups or business opportunities, it's advised to closely monitor the development and finalization of these standards <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>, <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>. While direct business opportunities for non-technical individuals might not be immediately apparent, understanding how [[What is Model Context Protocol MCP and why it matters|MCP]] works will be crucial for comprehending future advancements and striking at the opportune moment <a class="yt-timestamp" data-t="19:11:00">[19:11:00]</a>, <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>, <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.

One potential technical opportunity is the creation of an "[[What is Model Context Protocol MCP and why it matters|MCP]] App Store" that allows users to easily install and deploy [[What is Model Context Protocol MCP and why it matters|MCP]] servers from various repositories, generating a URL for connection to an [[What is Model Context Protocol MCP and why it matters|MCP]] client <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>, <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.

In essence, [[What is Model Context Protocol MCP and why it matters|MCP]] is a standard that unifies LLMs and services, making LLMs significantly more capable and laying the groundwork for the next generation of AI applications <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>, <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>, <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.