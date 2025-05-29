---
title: Opportunities for startups with MCP implementation
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The advent of the Machine Common Sense Protocol (MCP) is creating new avenues for [[ai_startups_and_entrepreneurship | startups]] by standardizing how Large Language Models (LLMs) interact with external services and tools <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. While the concept is gaining viral attention, its implications for [[ai_startup_incubation_and_ideas | startup ideas]] and entrepreneurial opportunities are still being understood <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Understanding MCP's Significance

In programming, standards are crucial for engineers to build systems that communicate effectively <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Just as REST APIs became a standard for companies to construct their services <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, MCP aims to provide a unified language for LLMs to interact with diverse tools <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### The Evolution of LLMs

*   **LLMs Alone:** Initially, LLMs were limited to predicting the next text, like completing "My Big Fat Greek..." with "Wedding" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. They were incapable of performing meaningful tasks such as sending emails or doing specific actions on behalf of a user <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **LLMs with Tools:** Developers began combining LLMs with tools, primarily APIs, to expand their capabilities <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This allowed LLMs to search the internet (e.g., Perplexity) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a> or integrate with automation services like Zapier to perform tasks such as adding email entries to a spreadsheet <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   **Challenges:** Gluing multiple tools to LLMs proved frustrating and cumbersome <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Each tool might speak a "different language" in terms of API construction, requiring significant manual work, step-by-step planning, and leading to potential failures or maintenance nightmares when APIs update <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a> <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a> <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This complexity is why an "Iron Man level Jarvis assistant" doesn't widely exist yet <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Enter MCP:** MCP acts as a translation layer between the LLM and various services/tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. It unifies all those different "languages" into a single, cohesive language that the LLM can understand <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This simplifies connection and access to outside resources, making LLMs more capable of executing complex tasks <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## The MCP Ecosystem

The MCP ecosystem comprises:
*   **MCP Client:** The LLM-facing side (e.g., Tempo, Windsurf, Cursor) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **MCP Protocol:** The two-way connection between the client and server <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **MCP Server:** Translates an external service's capabilities for the client <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Service providers are responsible for constructing these MCP servers <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **Service:** The external tool or data source (e.g., a database, Slack) <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

This architecture, pioneered by Anthropic, shifts the burden of integration to service providers, encouraging them to build MCP servers to make their services accessible to LLMs <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This means LLMs will become far more capable and less prone to hallucination when interacting with external data <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a> <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

## Startup Opportunities with MCP

MCP, by introducing a standard, opens up new opportunities for [[brainstorming_startup_ideas | startup ideas]] and growth, similar to how HTTP or SMTP enabled new businesses <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

### For Technical Founders

*   **MCP App Store:** An "MCP App Store" where users can browse existing MCP servers (from GitHub repos) and easily deploy them, obtaining a URL to integrate with an MCP client <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This simplifies the current "annoying" setup process involving file downloads and local configurations <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### For Non-Technical Founders

Non-technical individuals should closely monitor platforms developing MCP capability and the evolving standards <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Once the standard is finalized and widely adopted by service providers, integrating new services will become significantly easier <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. This ease of integration will enable the creation of more seamless and powerful chatbot interfaces with diverse tools <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

## Challenges and Future Potential

While MCP is promising, there are [[challenges_and_future_potential_of_mcp_integration | technical challenges and future potential of MCP integration]]. Setting up MCP servers is currently cumbersome <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. These "kinks" need to be ironed out, and the standard may still evolve <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

> "I don't see any crazy business opportunities right now for a non-technical person, even for a technical person, like imagine if OpenAI comes with a standard tomorrow and we all just shift to that, right? It's very early stages, but I think understanding how this works means you'll understand how the next thing works and when that becomes finalized, you hit the ground running." <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>

For those exploring [[successful_startup_ideas_and_validation_techniques | successful startup ideas and validation techniques]] or [[evaluating_and_prioritizing_startup_ideas | evaluating and prioritizing startup ideas]], the advice is to observe and learn from this evolving landscape <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>. The potential for LLMs to become highly capable, integrating like "Lego pieces," will emerge as the standard solidifies <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.