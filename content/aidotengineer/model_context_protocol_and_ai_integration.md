---
title: Model context protocol and AI integration
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

Kent C. Dodds, a developer focused on building excellent user experiences, notes a shift towards AI, where users are increasingly found <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. He teaches people how to build excellent user experiences with AI through his course platform, epicai.pro <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This article discusses how user interaction is changing, how [[model_context_protocol_mcp | Model Context Protocol]] (MCP) and similar technologies facilitate this change, and the role of product developers in this evolution <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The core idea is "letting AI interface with your app with MCPs or [[model_context_protocol_mcp | Model Context Protocol]] services" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## The Ideal AI Assistant: Jarvis

Tony Stark's AI assistant, Jarvis, from the Iron Man movies, exemplifies an ideal AI user experience <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Jarvis can:
*   Compile databases from various sources like SHIELD, FBI, and CIA intercepts <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Initiate virtual crime scene reconstructions <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   Access public records <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Bring up thermogenic signatures and factor in data like 3,000°C heat <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Access satellites and plot historical occurrences <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   Perform joins across different datasets, like filtering out areas with "Mandarin attacks" from thermogenic occurrences <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   Show related news articles <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   Create a flight plan <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Answer the doorbell and display visitor information <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   Generate dynamic UIs and interact with them <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   Interface through voice, typing, and gestures <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

While some capabilities like creating databases from classified sources or holographic displays are still challenging <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>, the technology for generating UIs dynamically already exists <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. The core barrier to having a personal Jarvis is not the underlying technology, but the difficulty of building all the necessary [[integration_of_mcp_with_ai_applications | integrations]] <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. It's impractical for major AI developers like Google, OpenAI, or Anthropic to build [[integration_of_mcp_with_ai_applications | integrations]] for every niche service, such as a local city government website for reserving park pavilions <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Users desire one unified robot that can interface with everything <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

## [[History and architecture of AI interaction protocols | History and Architecture of AI Interaction Protocols]]

The evolution of AI interaction can be divided into phases:

### Phase 1: Early LLMs and Manual Context (Approx. 3 Years Ago)
When ChatGPT emerged, it was pivotal because of its host application layer, which provided a good user experience for interfacing with LLMs <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. In this phase, users had to manually provide context by copy-pasting text or images <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. LLMs could answer questions but couldn't perform actions, and managing context was cumbersome <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Phase 2: Host Application Integrations
In this phase, the host application (e.g., ChatGPT itself) started to act as an intermediary, telling the LLM which services were available to it <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This allowed LLMs to do "stuff," such as accessing search engines, calendar [[integration_of_mcp_with_ai_applications | integrations]], or Slack [[integration_of_mcp_with_ai_applications | integrations]] <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. However, this approach was limited by the time and resources of the host application developers to build specific [[integration_of_mcp_with_ai_applications | integrations]] <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Proprietary systems like OpenAI's GPT plug-in system also meant developers had to build separate [[integration_of_mcp_with_ai_applications | integrations]] for different platforms (e.g., OpenAI, Anthropic, Google) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Users don't want multiple LLM wrappers; they want one "Jarvis" that can augment itself with any capability <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### Phase 3: Model Context Protocol (MCP)
This phase introduces [[model_context_protocol_mcp | Model Context Protocol]] (MCP), which enables AI to do "anything" <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. MCP is a standard protocol that AI assistants support or will soon support, allowing developers to build to a single specification and be usable by any AI assistant <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

#### [[Model Context Protocol mCP Overview | MCP Architecture]]
The [[history_and_architecture_of_ai_interaction_protocols | architecture]] of MCP involves:
*   **Host Application:** Communicates with the LLM and dynamically manages available services <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **LLM:** Knows what services are available and selects the most appropriate tool based on the user's query <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Standard Client:** The host application creates a standard client for each service, requiring no special [[integration_of_mcp_with_ai_applications | integration]] <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Service Provider:** Creates MCP servers that interface with unique tools, resources, prompts, and sampling <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

The key is that the communication between the server and the standard client is consistent, allowing service providers to control the unique aspects of their service while maintaining a universal interface <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. This mechanism provides "Jarvis hands" to actually perform tasks <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

## Demonstration of MCP

Kent C. Dodds demonstrates MCP using Cloud Desktop, configured with three MCP servers: a journaling server (EpicMe), a location service (locationator), and a weather service <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

A user prompt like "Please write a journal entry for me... about my trip with my daughter. I would like you to derive my location and weather conditions from my device location and make up a creative story with relevant text" triggers several MCP calls <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>:

1.  **Location Determination:** The `locationator` MCP server determines the current location <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
2.  **Weather Retrieval:** The `get weather` MCP server retrieves current weather conditions for the given coordinates <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
3.  **Authentication:** The `EpicMe` server's `authenticate` tool is called, prompting for user email and an OAuth 2.1 token for secure access <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This authentication ensures secure access to personal data <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
4.  **Journal Entry Creation:** The LLM generates the journal entry, and the MCP server creates it <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
5.  **Tagging:** The system checks for available tags, creates a new "travel" tag if needed, and adds it to the entry <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
6.  **Retrieval and Formatting:** The user can request to see the journal entry <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. The MCP server provides the data, and the LLM client can then format it in a user-friendly way (e.g., Markdown with a title) <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
7.  **Multimodal Capabilities:** While the server sends responses in English, an LLM could translate it into other languages like Japanese, showcasing multimodal capabilities <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
8.  **Action Execution:** The user can command the AI to perform actions like deleting the post and logging out, demonstrating the AI's ability to act on behalf of the user <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

This demonstrates the shift from traditional browser-based interaction, where users Google and phrase questions with keywords, to a more natural interaction where users speak their intent, and the AI figures out how to accomplish the task through MCP-enabled services <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

## Conclusion

[[model_context_protocol_mcp | Model Context Protocol]] (MCP) is a standard mechanism that enables AI assistants to communicate with various tools and services <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. It addresses the challenge of building extensive [[integration_of_mcp_with_ai_applications | integrations]] by providing a [[unified_interfaces_for_ai_ecosystems | unified interface]] <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This advancement is expected to lead to a future where everyone can have a "Jarvis-like" AI assistant, capable of augmenting itself with any capability in the world <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>, thereby enhancing [[importance_of_context_in_ai_agent_performance | AI agent performance]] and [[tool_usage_and_development_in_ai_frameworks | tool usage]].

## Resources

*   The specification for [[model_context_protocol_mcp | Model Context Protocol]] <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
*   epicai.pro: A platform to learn about MCP and AI in general, offering posts, workshops, and cohorts on the future of user interaction and how AI is changing the game <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.