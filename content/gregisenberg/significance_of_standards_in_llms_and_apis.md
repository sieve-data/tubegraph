---
title: Significance of standards in LLMs and APIs
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 
## Significance of Standards in LLMs and APIs

The emergence of Machine-Capable Protocols (MCPs) represents a significant development in the capabilities of Large Language Models (LLMs) by introducing a much-needed standardization for tool interaction <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### The Role of Standards in Engineering

In programming, standards are crucial for enabling different systems to communicate effectively <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. A well-known example is [[understanding_apis_and_integrating_with_ai_models | REST APIs]], which companies widely adopt when constructing their services, allowing engineers to connect with them seamlessly <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Engineering fundamentally relies on these formal standards to simplify interactions and ensure compatibility <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Initial Limitations of LLMs

By themselves, LLMs are fundamentally limited in their capabilities <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. For example, an LLM cannot directly send an email or perform specific tasks on behalf of a user <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Their core function is predicting the next word in a sequence based on their training data <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### The [[evolution_and_limitations_of_llms_with_tools | Evolution]] to LLMs with Tools

The first significant [[evolution_and_limitations_of_llms_with_tools | evolution]] in LLM capabilities came when developers learned how to combine them with external tools, such as [[understanding_apis_and_integrating_with_ai_models | APIs]] <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This allowed LLMs to perform actions like searching the internet (e.g., Perplexity) by fetching information from external services <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

However, this approach presents significant challenges:
*   **Complexity**: Connecting multiple tools to an LLM to perform diverse tasks (e.g., searching the internet, reading emails, summarizing) can become cumbersome and frustrating <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Integration Nightmare**: Stacking and ensuring cohesion between various tools is difficult <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. The absence of a unified language means each tool (e.g., an [[understanding_apis_and_integrating_with_ai_models | API]] for Slack, a text service) might require different setup and data passing, making it feel like "gluing a bunch of different things together" <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a> <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Maintenance Issues**: Updates to external service [[understanding_apis_and_integrating_with_ai_models | APIs]] can break integrations, leading to significant engineering effort to maintain functionality <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a> <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

### MCP: A Unified Standard for LLM-Tool Interaction

MCPs address these challenges by providing a standardized layer between an LLM and external services <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This layer translates the diverse "languages" of different tools into a single, unified language that the LLM can easily understand and interact with <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This makes it far simpler for LLMs to connect to and access external resources like databases or other tools <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

With MCP, the manual work, step-by-step planning, and managing of edge cases associated with current LLM-tool integrations are significantly reduced <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This moves the industry closer to achieving "Jarvis-level" AI assistants <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

#### The MCP Ecosystem Components
The MCP ecosystem consists of four main parts <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>:
1.  **MCP Client**: The LLM-facing side, such as Tempo or Cursor <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
2.  **MCP Protocol**: The two-way connection standard between the client and server <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
3.  **MCP Server**: Translates the capabilities of an external service to the client <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Notably, the responsibility for constructing the MCP server now rests with the service provider <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
4.  **Service**: The external tool or data source (e.g., a database) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

This architecture, championed by Anthropic, ensures that service providers build the necessary integration points for their services, making LLMs more capable <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

### Current Status and Future Outlook

MCPs represent a significant leap forward by standardizing how LLMs interact with the outside world, enabling them to move beyond mere text prediction to perform meaningful actions <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a> <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

However, the technology is still in its early stages <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>:
*   **Technical Challenges**: Setting up MCP servers can still be cumbersome and involves local configurations <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Standard Finalization**: It's currently unclear if MCP will be the definitive standard or if it will be updated or challenged by others <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

For non-technical individuals, the key is to stay informed about platforms developing MCP capabilities and observe the finalization of standards <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Once a standard is established and widely adopted by service providers, integrating LLMs will become much easier and more seamless, akin to building with Lego pieces <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a> <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. This understanding will be crucial for recognizing future business opportunities as the LLM landscape matures <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.