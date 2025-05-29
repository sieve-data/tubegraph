---
title: What is Model Context Protocol MCP and why it matters
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The Model Context Protocol (MCP) is a concept that has recently gained significant traction, aiming to address critical challenges in integrating Large Language Models (LLMs) with external tools and services <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains MCP as a crucial step in the [[the_evolution_of_large_language_models_llms_with_tools_and_mcp | evolution of LLMs]], making them significantly more capable <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## The Challenge: LLMs and Tools

In the realm of programming, standards are paramount as they enable different systems to communicate seamlessly <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. A well-known example is REST APIs, which provide a common standard for companies to build services that engineers can connect to <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

However, LLMs inherently possess significant limitations:
*   **Incapability on their own** LLMs alone cannot perform meaningful actions like sending an email <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Their primary function is predicting the next word in a sequence <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **The "LLM + Tools" Evolution** To overcome these limitations, developers began integrating LLMs with external tools, such as APIs. This allows LLMs to perform tasks like searching the internet, as seen with Perplexity <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Services like Zapier or N8N can connect LLMs to various automations, such as recording emails in a spreadsheet <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **The Problem with Tools Alone** While adding tools makes LLMs more capable, it becomes cumbersome and frustrating to integrate multiple tools <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Stacking these tools coherently is a "nightmare," hindering the development of advanced AI assistants akin to Iron Man's Jarvis <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Each tool might have its own "language" or different API setup requirements, making integration feel like "gluing a bunch of different things together" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Furthermore, updates to external APIs can break existing integrations, requiring significant manual re-engineering <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Even with tools, LLMs can still hallucinate or act "stupidly" <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. [[overview_of_manis_ais_capabilities | Manis AI]] is cited as an example of an AI startup that has engineered many tools cohesively, but this required extensive engineering hours <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

## What is Model Context Protocol (MCP)?

MCP is best understood as a **standard** <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a> and a **layer** between an LLM and various services or tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Its core function is to translate all the different "languages" of various tools into a single, unified language that the LLM can perfectly understand <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

This standard makes it much simpler for LLMs to connect with and access outside resources and data sources, such as databases <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. With MCP, an LLM could be told to create a new database entry and know exactly how to do it efficiently <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. This eliminates much of the manual work, step-by-step planning, and reduces edge cases where integrations might fail <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

In essence, MCP unifies the LLM and the service, creating an efficient communication layer <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## The MCP Ecosystem

The MCP ecosystem comprises four key components:
1.  **MCP Client**: The client-facing or LLM-facing side of the ecosystem, exemplified by tools like Tempo, Windsurf, or Cursor <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
2.  **Protocol**: The two-way connection between the client and the server <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
3.  **MCP Server**: This server translates the capabilities of an external service to the client <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Notably, the responsibility for constructing and maintaining the MCP server now falls to the service provider <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Anthropic designed this architecture to encourage service providers to make their services accessible to LLMs <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
4.  **Service**: The external tool or API that the LLM interacts with (e.g., a database, an email service) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

This structure means LLMs will become more capable, as all companies and engineers are expected to adopt this new standard <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. Just as common languages enable widespread communication, MCP allows LLMs to communicate efficiently with diverse services <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## [[Challenges and opportunities with integrating MCP in AI systems | Challenges and Future Outlook]]

While MCP presents a significant leap forward, it faces [[challenges_and_opportunities_with_integrating_mcp_in_ai_systems | current technical challenges]]. Setting up an MCP server can be cumbersome, involving multiple file downloads and local configurations <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. These "kinks" need to be resolved for the standard to be fully polished <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

However, once these issues are addressed and the standard is finalized, it will usher in a new era of highly capable LLMs <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. MCP is seen as the "next evolution" beyond simply connecting LLMs with individual tools <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

## [[Potential startup ideas and business opportunities with MCP | Startup Opportunities]]

For those looking to build startups or capitalize on emerging trends, MCP presents [[potential_startup_ideas_and_business_opportunities_with_mcp | opportunities]]:

*   **For Technical Individuals**: An "MCP App Store" could be a valuable concept. This platform would allow users to browse and easily deploy MCP servers from various repositories, providing a URL to integrate into an MCP client <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **For Non-Technical Individuals**: The best approach is to stay informed about platforms that are developing MCP capabilities <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. It's crucial to observe how the standard evolves and when it becomes finalized <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. Once the standard is stable and service providers integrate MCP, building seamless integrations will become significantly easier <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. This will allow for the stacking of AI capabilities like "Lego pieces" <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

It is currently an early stage, and while exciting, it's a time for observation and learning rather than immediate, large-scale business decisions <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. Understanding MCP now will enable quicker adaptation when the standard solidifies <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.