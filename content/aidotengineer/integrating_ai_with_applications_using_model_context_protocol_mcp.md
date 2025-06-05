---
title: Integrating AI with applications using Model Context Protocol MCP
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

Kent C. Dodds teaches how to build excellent user experiences, with a recent shift from web development to AI, as users are increasingly engaging with AI assistants <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The core topic of this discussion is how user interaction is evolving, how protocols like [[model_context_protocol_mcp|Model Context Protocol]] (MCP) facilitate this change, and the role of product developers in reaching users within AI assistance platforms <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The talk focuses on "Letting AI interface with your app with MCPS or [[model_context_protocol_mcp|Model Context Protocol]] services" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## The Vision: Jarvis and the Challenge of Integration

The aspiration for AI interaction is exemplified by Tony Stark's AI assistant, Jarvis, from the *Iron Man* movies <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Jarvis can perform a wide range of tasks, including:
*   Compiling databases from various sources (e.g., SHIELD, FBI, CIA intercepts) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   Generating user interfaces (UIs) on demand <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   Accessing public records <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Bringing up thermogenic signatures and analyzing data from cloud services and satellites <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   Joining across different datasets <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>, <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Showing related news articles <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Creating flight plans <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Interfacing with home systems, such as showing who is at the door <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Jarvis represents an ideal user experience that seamlessly integrates with various systems, allowing for voice commands, typing, gestures, and dynamic UI generation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. While the technology exists for many of these capabilities (e.g., UI generation <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>), the primary barrier to having a personal Jarvis is the sheer difficulty of building comprehensive **integrations** <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. It's impractical for major AI developers to build integrations for every possible tool or service, such as a local city government website for reserving park pavilions <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Users desire a single AI assistant that can augment itself with "any capability in the world" <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

## Evolution of AI Integration

The journey towards seamless AI integration can be understood through three phases:

### Phase 1: Initial LLMs and Manual Context
Around three years ago, the release of ChatGPT marked a pivotal moment, not because of the LLM itself (which had existed for some time), but due to the host application layer that provided a good user experience for interacting with LLMs <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This led to significant investment and rapid improvement in LLMs <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
The main limitation in this phase was the manual provision of context. Users had to copy and paste code or text into the LLM and then manually transfer its output back into their workflows, making context management cumbersome <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Phase 2: Host Application Integrations
In the second phase, host applications began to facilitate interaction between the LLM and external services. The host application could inform the LLM about available services (e.g., search engines, calendar integrations, Slack integrations) and retrieve additional context as needed <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
However, this approach was limited by the time and resources developers at LLM providers (like OpenAI or Anthropic) could dedicate to building specific integrations <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. While proprietary plugin systems like OpenAI's GPT plugin system exist, building separate integrations for different LLM providers (e.g., Anthropic, Google) is impractical <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Users don't want multiple wrappers; they want one unified Jarvis <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Phase 3: [[model_context_protocol_mcp|Model Context Protocol]] (MCP)
[[model_context_protocol_mcp|MCP]] ushers in the third phase by providing a standard protocol for AI assistants to communicate with diverse tools and services <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>, <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This standardization means that a service built to the [[model_context_protocol_mcp|MCP]] specification can be used by any AI assistant that supports the protocol <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This breakthrough is expected to lead to a "Jarvis for everybody" <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

## [[model_context_protocol_mcp|MCP]] Architecture

The [[model_context_protocol_mcp|MCP]] architecture involves several key components:
*   **Host Application**: Communicates with the LLM and informs it about available services. Services can be dynamically added or removed, with the host application managing this context <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **LLM**: Receives the user's query and the list of available services from the host application, then selects the most appropriate tool <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Client**: The host application creates a standard client for each service it wants to interface with, adhering to a defined interface <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Service Provider**: Creates [[model_context_protocol_mcp|MCP]] servers that interface with specific tools, resources, prompts, and sampling features <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. The unique logic for each service resides within the service provider's control <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

The standardization of communication between the server and client components is what makes [[model_context_protocol_mcp|MCP]] effective, essentially giving AI assistants "hands to be able to actually do stuff" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

## [[model_context_protocol_mcp|MCP]] in Action: A Demo

A demonstration of [[model_context_protocol_mcp|MCP]] showcases its capabilities through a journaling scenario:
1.  **Prompt**: A user asks the AI assistant (configured with three [[model_context_protocol_mcp|MCP]] servers) to write a journal entry about a trip, including their email address, deriving location and weather, and generating a creative story <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
2.  **Locationator Tool**: The assistant utilizes an [[model_context_protocol_mcp|MCP]] server called "locationator" to determine the current location <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. For now, users must approve tool calls, unlike Tony Stark's seamless interaction with Jarvis <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
3.  **Weather Tool**: Another [[model_context_protocol_mcp|MCP]] server, "get weather," retrieves current weather conditions based on the derived coordinates <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
4.  **Authentication**: The "EpicMe" [[model_context_protocol_mcp|MCP]] server initiates an authentication flow using OAuth 2.1, requiring the user to provide an email and then an OAuth token <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>, <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This ensures secure, authenticated tasks like creating journal entries <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
5.  **Journal Entry Creation**: The LLM writes the journal entry, and the [[model_context_protocol_mcp|MCP]] server configures the inputs <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. The system can also create and add relevant tags, such as a "travel" tag for the journal entry <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
6.  **Retrieval and Dynamic Display**: The user can then ask the LLM to display the journal entry. The [[model_context_protocol_mcp|MCP]] server provides the entry in a structured format (e.g., JSON), and the client can decide how to best format and display it to the user (e.g., as Markdown) <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This demonstrates the potential for dynamic UI generation <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
7.  **Multimodal Potential**: The LLM can also translate responses from the [[model_context_protocol_mcp|MCP]] server into different languages, even if the server only sends English <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
8.  **Further Actions**: The user can continue to interact with the assistant, for example, to delete the post and log out <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

Many [[model_context_protocol_mcp|MCP]] servers, like the EpicMe example, are designed to be exclusively accessible via [[model_context_protocol_mcp|MCP]] and its clients, not as traditional web applications <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

## Future Implications

The shift enabled by [[model_context_protocol_mcp|MCP]] moves towards more natural user interaction <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. Instead of navigating browsers or crafting specific search queries, users can speak their questions, and the AI will understand their intent, not just their search query, but what they are "actually trying to do," and then perform that action <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. This transition promises to fundamentally change how users interact with technology.

## Resources

*   [[introduction_to_model_context_protocol_mcp | Model Context Protocol Specification]]: An important document to review for understanding [[model_context_protocol_mcp|MCP]] <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
*   EpicAI.pro: A platform offering courses, posts, workshops, and cohorts on [[integrating_ai_into_natural_workflows|AI in general]] and the future of user interaction <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.