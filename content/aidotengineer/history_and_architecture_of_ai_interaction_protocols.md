---
title: History and architecture of AI interaction protocols
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

As user interaction paradigms shift, the focus is increasingly on [[user_experience_design_with_ai | building excellent user experiences within AI assistance]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This shift is fundamentally changing user interaction <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, driven significantly by concepts like [[model_context_protocol_and_ai_integration | Model Context Protocol]] (MCP) <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Jarvis Ideal

The ultimate vision for AI interaction is exemplified by Tony Stark's AI assistant, Jarvis <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Jarvis can perform a wide range of tasks, including:
*   Compiling databases from various sources (e.g., SHIELD, FBI, CIA intercepts) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Initiating virtual crime scene reconstructions <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   Generating user interfaces (UI) on demand <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   Accessing public records <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Bringing up and analyzing complex data like thermogenic signatures <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Performing complex data joins across different datasets (e.g., thermogenic occurrences with Mandarin attack locations) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   Creating flight plans <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Interacting with physical systems like doorbells <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Crucially, Jarvis supports not just voice, but also typing and gestures, generating dynamic UIs for seamless interaction <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. While some of these capabilities, like UI generation, are technically possible today <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, a personal Jarvis-like assistant is not yet commonplace <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## The Integration Challenge

The primary barrier to achieving a universal AI assistant like Jarvis is the complexity of building myriad integrations <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. It is incredibly difficult for major AI providers (like Google or OpenAI) to build integrations for every possible service, especially niche ones like a local city government website for reserving park pavilions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Without a way to interface with everything, the incentive to invest heavily in broad integration efforts diminishes <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Users desire one central AI capable of augmenting itself with any capability in the world <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

## Evolution of AI Interaction Protocols

The [[evolution_and_history_of_ai_technology | history and architecture of AI interaction protocols]] can be divided into three phases <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>:

### Phase 1: ChatGPT and Manual Context (Circa 3 years ago)

This phase began with the advent of ChatGPT <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Its pivotal contribution was not merely the Large Language Model (LLM), which had existed for some time, but the host application layer around it that provided a good [[user_experience_design_with_ai | user experience]] for interfacing with an LLM <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This led to significant investment and rapid improvement in LLMs <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

However, the major limitation was the need for users to manually provide context by copying and pasting text or images into the LLM, and then manually extracting results <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. While the LLM could answer questions, it couldn't *do* anything directly, and managing this context was cumbersome <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Phase 2: Host Application Tooling

In this phase, the host application began to interface directly with the LLM, informing it about available services and providing additional context when needed <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This enabled the AI to perform actions using tools like search engines, calendar integrations, or Slack integrations <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

Despite this progress, the functionality remained limited by the development time of the host application provider (e.g., OpenAI, Anthropic) to build integrations <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Proprietary plugin systems (like OpenAI's GPT plugin system) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> meant developers had to build separate integrations for each platform, which was not scalable <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. Users don't want multiple LLM wrappers; they want one central AI that can interface with everything <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Phase 3: Model Context Protocol (MCP)

This is the current and future phase, where [[model_context_protocol_and_ai_integration | Model Context Protocol]] (MCP) acts as a standard protocol that all AI assistants support or will soon support <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. By building to the MCP specification, developers can ensure their services are usable by any AI assistant <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. This standardization is expected to bring widespread access to Jarvis-like AI capabilities <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

## MCP Architecture and [[tool_usage_and_development_in_ai_frameworks | Tool Usage]]

The architecture of MCP involves several key components <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>:
*   **Host Application**: Communicates with the LLM and dynamically manages the available services <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **LLM**: Knows what services are available based on the host application's context and selects the most appropriate tool for the user's query <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
*   **Client**: The host application creates a standard client for each service it wants to interface with <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This client uses a standard interface, avoiding special integrations <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   **Service Provider**: Creates the MCP servers that interface with unique tools, resources, and specific prompts <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. This allows service providers to control the unique aspects of their service while maintaining a standard communication interface with the client <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

This standardized communication is what enables AI to "have hands" and perform real-world actions <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

### MCP Demo Example

An example demo of MCP in action illustrates its capabilities:
1.  **Journal Entry Request**: A user prompts an LLM configured with MCP servers to "write a journal entry," deriving location and weather, and creating a story <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
2.  **Location and Weather Tools**: The LLM uses a "locationator" MCP server to determine the current location <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a> and a "get weather" server to retrieve weather conditions <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
3.  **Authentication**: It then calls an "EpicMe" MCP server's authenticate tool. The user provides an email, receives an authentication token (using OAuth 2.1), and logs in, demonstrating [[building_trust_and_community_in_ai_applications | secure authentication]] built into the MCP server <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
4.  **Journaling and Tagging**: After authentication, the LLM requests the creation of a journal entry, configures inputs, and checks for available tags, even creating new ones (e.g., "travel") as needed <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
5.  **Dynamic Display**: The LLM can retrieve the journal entry and format it for display, even rendering it in Markdown. This highlights the ability for servers to communicate in a sensible way and clients to take context to display dynamic UIs, which is currently a developing feature in clients <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
6.  **Multilingual Capabilities**: An MCP server might send responses in English, but the LLM can translate them into any language (e.g., Japanese), further enhancing the user experience <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
7.  **Action Execution**: The demo concludes with the user instructing the AI to delete the post and log out, demonstrating the ability to perform authenticated actions <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

This shift means users will soon no longer need to navigate browsers or phrase search queries in specific ways; instead, they can speak naturally, and the AI will understand their intent and perform actions <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

## Conclusion

[[model_context_protocol_and_ai_integration | Model Context Protocol]] is a critical step in the [[future_directions_for_software_architecture_using_ai | future of software architecture]] and user interaction with AI. It provides a standard mechanism for AI assistants to communicate with a vast ecosystem of tools and services, overcoming the longstanding [[challenges_in_ai_for_architecture_design | challenges of AI integration]]. This promises a future where AI assistants can truly "do anything" <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>, enabling a seamless and intuitive user experience akin to the Jarvis ideal.

For further learning, explore the Model Context Protocol specification <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a> and resources on EpicAI.pro, which covers MCP and broader AI topics <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.