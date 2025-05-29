---
title: Potential Opportunities with MCP in Startups
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The concept of Micro-Capability Protocols (MCPs) has garnered significant attention, prompting discussions about its meaning and the [[aidriven_startup_ideas_and_entrepreneurship | startup opportunities]] it presents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains MCP as a crucial evolution for making Large Language Models (LLMs) more capable <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Understanding MCP

In programming, standards are vital for engineers to build systems that communicate effectively <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A well-known standard is REST APIs, which companies follow to structure their services for easy connection <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Limitations of LLMs Alone
LLMs, by themselves, are incapable of performing meaningful actions like sending an email <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Their primary function is predicting the next text, such as completing "My Big Fat Greek" with "Wedding" based on training data <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Evolution: LLMs with Tools
The next phase involved developers combining LLMs with external tools, such as APIs, enabling capabilities like searching the internet (e.g., Perplexity) <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This allows LLMs to become more powerful by accessing outside services <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. For example, an LLM could be set up to create a spreadsheet entry every time an email is received, using automation services like Zapier or End8 <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

However, connecting multiple tools to an LLM to build a sophisticated assistant (like an "Iron Man level Jarvis") becomes frustrating and cumbersome <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Stacking these tools cohesively is a significant challenge, making LLMs, despite their cool factor, "very, very dumb" without proper integration <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Different service providers construct their APIs differently, making it feel like "gluing a bunch of different things together," which is difficult to scale <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Even minor updates to an API can break complex, step-by-step automations, causing significant engineering nightmares <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### MCP as the Solution
MCP introduces a translation layer between the LLM and various services/tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This layer unifies the "different languages" of various tools into a single, comprehensive language that the LLM understands, simplifying connection and access to external resources <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This eliminates much of the manual work and step-by-step planning required in the previous evolution, reducing edge cases where systems can fail <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. MCP unifies the LLM and the service, creating an efficient communication layer <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## The MCP Ecosystem
The MCP ecosystem consists of four main components <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>:
*   **MCP Client:** The LLM-facing side (e.g., Tempo, Windsurf, Cursor) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Protocol:** The two-way connection between the client and the server <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **MCP Server:** Translates the external service's capabilities to the client <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   **Service:** The external tool or data source (e.g., database, API) <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

A key aspect of this architecture, designed by Anthropic, is that the MCP server responsibility now falls on the service providers <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This means if a company builds a database and wants LLMs to access it, they are responsible for constructing the MCP server <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. This has led many external service providers to build their own MCP servers and repositories <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. Essentially, MCP is a standard that companies and engineers are adopting to ensure interoperability and scalability, allowing LLMs to become capable of "important stuff" <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

## [[Technical Challenges and Future of MCP | Current Challenges]]
Despite its promise, there are [[technical_challenges_and_future_of_mcp | technical challenges]] <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Setting up an MCP server can be annoying, involving many local steps like downloading and moving files <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. Once these kinks are resolved, or the standard is updated and polished, LLMs will become even more capable <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

## [[Brainstorming startup ideas | Startup Opportunities]] with MCP

The advent of popularized protocols like HTTP or SMTP has historically opened new opportunities for businesses <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. While it's still early days for MCP, understanding it is crucial for future ventures <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### For Technical Founders
*   **MCP App Store:** An idea for a technical founder is to create an "MCP App Store" <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This platform would allow users to browse different MCP servers from repositories, click "install" or "deploy," receive a specific URL, and then paste that URL into an MCP client <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

### For Non-Technical Founders
For non-technical individuals, the advice is to stay updated on platforms adopting MCP capability and observe the direction of the standards <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. It's too early for concrete business decisions, as the standard is not fully finalized and might be challenged or updated by entities like Anthropic or OpenAI <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

*   **Strategic Observation:** The current phase calls for observation and learning <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. When the standard is finalized and service providers fully integrate MCP, seamless integration will become possible <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. This will make it significantly easier to integrate LLMs with external tools, akin to stacking "Lego pieces" <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Focus on User Experience:** While building integrated LLM solutions is challenging (requiring significant engineering hours to ensure cohesion, speed, and limit hallucinations), MCP will simplify the integration aspect <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

MCP, as a standard for LLMs, makes them more capable by simplifying their connection to external services <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. While the [[technical_challenges_and_future_of_mcp | technical challenges]] are being worked out, keeping a close watch on the evolution of this standard is key for future [[aidriven_startup_ideas_and_entrepreneurship | entrepreneurial opportunities]] <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.