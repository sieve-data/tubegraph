---
title: Importance of standards like MCP in AI advancements
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The concept of "MCPs" (Machine Communication Protocols) has gained significant attention in the field of Artificial Intelligence, particularly concerning Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While the term has gone viral, its underlying meaning and implications for startups and AI development are often misunderstood <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Professor Ross Mike explains MCPs as a critical standard that enhances the capabilities of LLMs, moving beyond their inherent limitations <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>, <a class="yt-timestamp" data-t="01:45:45">[01:45:45]</a>.

## The Inherent Limitations of Large Language Models (LLMs)

By themselves, LLMs are fundamentally incapable of performing meaningful actions beyond predicting the next sequence of text <a class="yt-timestamp" data-t="03:08:08">[03:08:08]</a>, <a class="yt-timestamp" data-t="03:25:25">[03:25:25]</a>. For instance, an LLM cannot send an email or perform a specific task on its own; it can only respond to queries or generate text based on its training data <a class="yt-timestamp" data-t="02:53:53">[02:53:53]</a>, <a class="yt-timestamp" data-t="03:19:19">[03:19:19]</a>. Their primary function is prediction, similar to completing a phrase like "My Big Fat Greek..." with "Wedding" <a class="yt-timestamp" data-t="03:30:30">[03:30:30]</a>.

## Evolution: LLMs Combined with Tools

The next step in LLM development involved integrating them with external tools, such as APIs (Application Programming Interfaces) <a class="yt-timestamp" data-t="03:48:48">[03:48:48]</a>. This allowed LLMs to perform actions like searching the internet (e.g., Perplexity) by providing access to external services <a class="yt-timestamp" data-t="03:58:58">[03:58:58]</a>, <a class="yt-timestamp" data-t="04:19:19">[04:19:19]</a>.

However, this approach comes with significant [[challenges_and_limitations_of_ai_tools | challenges and limitations]]:
*   **Complexity:** Connecting multiple tools to an LLM, such as for tasks like processing emails and updating spreadsheets, becomes cumbersome and frustrating <a class="yt-timestamp" data-t="05:09:09">[05:09:09]</a>, <a class="yt-timestamp" data-t="05:19:19">[05:19:19]</a>.
*   **Lack of Cohesion:** Making these disparate tools work cohesively with the LLM and stack on top of each other is a "nightmare" <a class="yt-timestamp" data-t="05:38:38">[05:38:38]</a>, <a class="yt-timestamp" data-t="06:11:11">[06:11:11]</a>.
*   **Maintenance Burden:** Updates to external service APIs (e.g., Slack or text services) can break existing automations, leading to extensive engineering work to fix <a class="yt-timestamp" data-t="10:18:18">[10:18:18]</a>, <a class="yt-timestamp" data-t="10:35:35">[10:35:35]</a>.
*   **Hallucinations:** Despite their perceived coolness, LLMs can be "very very dumb" and prone to hallucination when integrated with tools <a class="yt-timestamp" data-t="06:26:26">[06:26:26]</a>, <a class="yt-timestamp" data-t="06:30:30">[06:30:30]</a>.

The difficulty of this "gluing" process explains why an "Iron Man level Jarvis assistant" is not yet widely available <a class="yt-timestamp" data-t="05:30:30">[05:30:30]</a>, <a class="yt-timestamp" data-t="09:47:47">[09:47:47]</a>.

## Introducing MCP: A Unifying Standard

MCP aims to solve these integration problems by acting as a universal translator between LLMs and external services <a class="yt-timestamp" data-t="08:34:34">[08:34:34]</a>, <a class="yt-timestamp" data-t="08:45:45">[08:45:45]</a>. Just as programming relies on standards like REST APIs to enable systems to communicate, MCP establishes a standard for LLM interaction <a class="yt-timestamp" data-t="01:54:54">[01:54:54]</a>, <a class="yt-timestamp" data-t="02:09:09">[02:09:09]</a>, <a class="yt-timestamp" data-t="13:17:17">[13:17:17]</a>.

Rather than each tool speaking a different "language" (e.g., English, Spanish, Japanese for APIs) due to varied constructions and information requirements, MCP provides a unified language that the LLM can understand <a class="yt-timestamp" data-t="08:02:02">[08:02:02]</a>, <a class="yt-timestamp" data-t="08:48:48">[08:48:48]</a>. This layer simplifies the connection and access to outside resources <a class="yt-timestamp" data-t="09:01:01">[09:01:01]</a>.

### The MCP Ecosystem
The MCP ecosystem consists of four main components <a class="yt-timestamp" data-t="11:02:02">[11:02:02]</a>:
1.  **MCP Client:** The LLM-facing side, such as Tempo, Wind Surf, or Cursor <a class="yt-timestamp" data-t="11:16:16">[11:16:16]</a>, <a class="yt-timestamp" data-t="11:24:24">[11:24:24]</a>.
2.  **MCP Protocol:** The two-way connection standard between the client and the server <a class="yt-timestamp" data-t="11:32:32">[11:32:32]</a>.
3.  **MCP Server:** This component translates the capabilities of an external service to the client <a class="yt-timestamp" data-t="11:38:38">[11:38:38]</a>. Significantly, the responsibility for constructing the MCP server now falls on the service provider (e.g., a database company) <a class="yt-timestamp" data-t="11:59:59">[11:59:59]</a>, <a class="yt-timestamp" data-t="12:18:18">[12:18:18]</a>. This shift empowers external service providers to build compatible interfaces <a class="yt-timestamp" data-t="12:36:36">[12:36:36]</a>.
4.  **Service:** The external tool or data source (e.g., database, API) <a class="yt-timestamp" data-t="11:13:13">[11:13:13]</a>.

## Benefits and Future Outlook

MCP makes LLMs more capable by unifying their communication with external services <a class="yt-timestamp" data-t="12:46:46">[12:46:46]</a>, <a class="yt-timestamp" data-t="13:38:38">[13:38:38]</a>. It transforms integrating diverse services into an easier process, allowing them to function like cohesive "Lego pieces" that can be stacked <a class="yt-timestamp" data-t="18:40:40">[18:40:40]</a>, <a class="yt-timestamp" data-t="18:46:46">[18:46:46]</a>. This reduces manual work, step-by-step planning, and the risk of failure in edge cases previously associated with LLM-tool integrations <a class="yt-timestamp" data-t="09:36:36">[09:36:36]</a>, <a class="yt-timestamp" data-t="09:41:41">[09:41:41]</a>.

While MCP represents a significant leap, it is still in its early stages <a class="yt-timestamp" data-t="17:52:52">[17:52:52]</a>. There are current [[challenges_and_limitations_of_ai_tools | technical challenges]] in setting up MCP servers, involving local file management and "Kinks" that need to be ironed out <a class="yt-timestamp" data-t="13:59:59">[13:59:59]</a>, <a class="yt-timestamp" data-t="14:08:08">[14:08:08]</a>. However, once these issues are resolved or a final standard emerges, LLMs will become even more powerful <a class="yt-timestamp" data-t="14:12:12">[14:12:12]</a>, <a class="yt-timestamp" data-t="14:19:19">[14:19:19]</a>.

For individuals seeking [[opportunities_for_ai_applications_in_career_advancement | business opportunities]] in this evolving landscape, it's advised to closely monitor how the standard develops and when it is finalized <a class="yt-timestamp" data-t="17:31:31">[17:31:31]</a>, <a class="yt-timestamp" data-t="17:57:57">[17:57:57]</a>. While the current stage is for observation rather than immediate major business decisions, understanding MCP ensures readiness to "hit the ground running" when the standard matures <a class="yt-timestamp" data-t="19:11:11">[19:11:11]</a>, <a class="yt-timestamp" data-t="19:37:37">[19:37:37]</a>. An example of an early opportunity for technical individuals is creating an "MCP App Store" to simplify the deployment of MCP servers <a class="yt-timestamp" data-t="16:38:38">[16:38:38]</a>.

In essence, MCP is not a complex new law of physics but a crucial standard for LLMs, paving the way for more capable and seamlessly integrated AI assistants <a class="yt-timestamp" data-t="15:21:21">[15:21:21]</a>, <a class="yt-timestamp" data-t="15:27:27">[15:27:27]</a>.