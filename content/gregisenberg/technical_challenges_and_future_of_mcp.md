---
title: Technical Challenges and Future of MCP
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

[[Understanding Model Context Protocol MCP | Model Context Protocol (MCP)]] has gained significant attention, despite many people not fully understanding its implications or the startup opportunities it presents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains [[Understanding Model Context Protocol MCP | MCP]] as a crucial step in the evolution of Large Language Models (LLMs), addressing current limitations and paving the way for more capable AI systems <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Evolution of LLMs and Tools

Initially, LLMs were limited in their capabilities <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. By themselves, they could only predict the next text or answer questions, unable to perform meaningful actions like sending an email <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The first major evolution involved developers combining LLMs with external tools, such as APIs for internet searches (e.g., Perplexity) or automation services like Zapier or N8 <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

However, this approach comes with significant [[Challenges and limitations faced by nontechnical users in coding environments | difficulties]]:
*   **Cumbersome Integration** <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>: Building an assistant that performs multiple tasks (e.g., searching the internet, reading emails, summarizing) involves "gluing a bunch of different tools" to the LLM, which can be frustrating and cumbersome <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Lack of Standardization** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>: While APIs have standards, every service provider constructs their APIs differently, requiring varied information and setup <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This makes scaling difficult <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Maintenance Nightmare** <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>: If a service's API (e.g., Slack's) updates, it can break existing connections and complex automation flows, leading to extensive engineering hours and debugging <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **LLM Hallucinations** <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>: Despite being powerful, LLMs on their own are "very, very dumb" and can hallucinate or produce illogical results when integrated with tools <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

These challenges prevent the creation of a "Jarvis level assistant" similar to Iron Man's AI <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## How MCP Addresses These Challenges

[[Understanding Model Context Protocol MCP | MCP]] serves as a crucial layer between an LLM and external services or tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. It translates the disparate "languages" of different tools into a unified language that the LLM can readily understand <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This simplifies the LLM's ability to connect to and access outside resources, such as databases or other data sources <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

The [[Understanding Model Context Protocol MCP | MCP]] ecosystem comprises:
1.  **MCP Client**: The LLM-facing side (e.g., Tempo, Wind Surf, Cursor) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
2.  **MCP Protocol**: The two-way connection standard between the client and server <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
3.  **MCP Server**: Translates the external service's capabilities for the client <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

A key aspect of [[Understanding Model Context Protocol MCP | MCP]]'s architecture is that the **MCP server is built and maintained by the service provider** <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. This means that companies offering services (like a database or a dev tool) are responsible for constructing their own [[Understanding Model Context Protocol MCP | MCP]] server to ensure LLMs can fully access their offerings <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. Anthropic, the creator of [[Understanding Model Context Protocol MCP | MCP]], essentially made it the service providers' responsibility to integrate with the protocol to make LLMs more powerful <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

## Technical Challenges of MCP

While [[Understanding Model Context Protocol MCP | MCP]] aims to unify LLM-tool communication, it is not without its current technical challenges:
*   **Setup Complexity** <a class="yt-timestamp" data-t="00:13:59">[01:13:59]</a>: Setting up an [[Understanding Model Context Protocol MCP | MCP]] server on clients is currently "annoying," involving manual downloading and moving of files, often locally <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **"Kinks" to be Figured Out** <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>: The protocol is still in its early stages, and there are "kinks that have to be figured out" or finalized <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

## Future of MCP and AI

[[Understanding Model Context Protocol MCP | MCP]] represents the "next evolution" in making LLMs more capable <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. Once the standard is finalized and polished, or a better one emerges, it will lead to a world where LLMs are significantly more capable of performing meaningful tasks <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

### [[Potential Opportunities with MCP in Startups | Startup Opportunities]]

For those looking to build startups or leverage this technology:
*   **Technical Opportunities**: A significant opportunity exists in creating an **"MCP App Store"** <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This would allow users to browse different [[Understanding Model Context Protocol MCP | MCP]] servers (available as open-source repositories), click "install" or "deploy" to get a URL, and then paste that into an [[Understanding Model Context Protocol MCP | MCP]] client <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This would greatly simplify the current complex setup process.
*   **Non-Technical Opportunities**: For non-technical individuals, the advice is to **stay informed** <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. It's crucial to monitor which platforms are building out [[Understanding Model Context Protocol MCP | MCP]] capability and observe the direction of the standards <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Once the [[Understanding Model Context Protocol MCP | MCP]] standard is finalized and service providers adopt it, integration will become much easier <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. This will open up new possibilities for building seamless AI-powered user experiences, akin to stacking Lego pieces <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

While it's still "very early stages" for [[Understanding Model Context Protocol MCP | MCP]], understanding its mechanics now will enable individuals to "hit the ground running" when the standard becomes finalized <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. It's a time for observation and learning, rather than immediate, drastic business decisions <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

In essence, [[Understanding Model Context Protocol MCP | MCP]] is a standard for LLMs that makes them more capable by simplifying their interaction with external tools and services <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. It is seen as an exciting development that will unify the AI ecosystem, similar to how other protocols like HTTPS or SMTP enabled widespread business creation <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.