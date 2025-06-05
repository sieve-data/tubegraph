---
title: The evolution of AI interfaces and user interaction
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

Kent C. Dodds, a developer focused on [[effective_design_of_ai_in_products | building excellent user experiences]], notes a significant shift from web-based interactions to AI-driven ones as users migrate to AI assistants <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This transition is fundamentally changing how users interact with technology, driven by innovations like Model Context Protocol (MCP) <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Vision: Jarvis and Advanced AI Assistants

The ideal AI interaction is exemplified by Tony Stark's AI assistant, Jarvis, from the *Iron Man* movies <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Jarvis performs a wide range of complex tasks that significantly augment Tony Stark's capabilities, making research and analysis much faster <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Jarvis's Capabilities

Jarvis demonstrates advanced interaction and utility, including:
*   Compiling databases from disparate sources (SHIELD, FBI, CIA intercepts) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Generating UIs on demand for data visualization (virtual crime scene reconstruction, thermogenic signatures) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Accessing public records <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Joining across different datasets for complex queries (e.g., filtering thermogenic occurrences by Mandarin attack locations) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>, <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   Showing related news articles <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Creating flight plans <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Interacting via voice, typing, and gestures <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   Generating dynamic UIs and interacting with them <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

### Current Technological Parallels and Gaps

While some Jarvis capabilities, like generating UI on demand, are achievable with current technology <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, obstacles remain. Creating databases from restricted sources like government intelligence agencies is not technically impossible but legally and access-wise difficult <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Holographic displays are still in development <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. The core question is why a personal "Jarvis" isn't ubiquitous yet <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## The Challenge: Building Integrations

The primary barrier to widespread, omni-capable AI assistants like Jarvis is the immense difficulty of [[future_of_ai_in_improving_user_experience_and_integrations | building integrations]] for every conceivable service and application <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Companies like Google, OpenAI, or Anthropic will not build integrations for every local or niche service (e.g., a city government website for reserving park pavilions) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Without comprehensive integration, users are less incentivized to invest in setting up an AI assistant that only performs some tasks <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Users desire a single AI assistant that can interface with *everything*, even services they use infrequently <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

## The Solution: Model Context Protocol (MCP)

[[history_and_evolution_of_ai | The history and evolution of AI]] interfaces, particularly with large language models (LLMs), can be understood in three phases, culminating in Model Context Protocol (MCP). MCP provides a standard mechanism for AI assistants to communicate with various tools and services <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>, aiming to overcome the integration challenge.

### Phase 1: ChatGPT and Manual Context

Around three years ago, the release of ChatGPT was pivotal, not just for its LLM (which had existed for some time), but for the host application layer that provided a good [[the_role_of_user_experience_in_ai | user experience]] for interacting with an LLM <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This led to significant investment and rapid improvement in LLMs <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

However, a key limitation was the need for manual context provision <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Users had to copy-paste code or text into the AI and then manually extract and apply results <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. While LLMs could answer questions, they couldn't "do" anything or manage context themselves, making it a "pain" <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Phase 2: Host Application Integrations

In the second phase, host applications began to integrate LLMs with external tools like search engines, calendars, or Slack <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. The host application could tell the LLM what services were available and retrieve necessary context or execute actions <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This allowed the AI to "do stuff" <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

The problem persisted: these integrations were limited by the development time of companies like OpenAI or Anthropic <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Proprietary plugin systems (e.g., OpenAI's GPT plug-in system) further fragmented efforts, as developers would need to build separate integrations for each platform (OpenAI, Anthropic, Google) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Users don't want a multitude of "LLM wrappers"; they want a single, versatile AI assistant <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### Phase 3: Model Context Protocol (MCP)

MCP represents the third phase, providing a standard protocol that AI assistants can support <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>, <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This means developers can build to the MCP specification and their services become usable by any compliant AI assistant <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

#### MCP Architecture and [[evolution_of_ai_engineering_and_tools | Collaboration between human engineers and AI]]
The architecture involves:
*   **Host Application:** Communicates with the LLM and dynamically informs it about available services <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **LLM:** Processes user queries and selects the most appropriate tool based on available services <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **MCP Client:** Created by the host application for each service, adhering to a standard interface <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **MCP Servers:** Created by service providers, interfacing with their unique tools, resources, and prompts <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

The standardization of communication between the client and server is what makes MCP powerful, allowing service providers to maintain control over their unique features while being universally accessible <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. This standardization gives AI "hands" to perform actions across different systems <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

## MCP in Action: A Journaling Demo

A demonstration showcases MCP's potential, despite current limitations in client readiness <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

### Workflow Example
The demo involves asking an AI assistant in a Cloud Desktop environment (configured with three MCP servers) to write a journal entry <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. The AI uses several MCP servers to fulfill the request:
1.  **Locationator:** Determines current device location, requiring user approval for tool calls due to current trust limitations <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
2.  **Get Weather:** Retrieves weather conditions for the derived location <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
3.  **EpicMe (Journaling Server):**
    *   Authenticates the user via OAUTH 2.1, providing enterprise-level security <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>, <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
    *   Allows the LLM to write a creative journal entry based on location and weather <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
    *   Manages journal entry tags, creating new ones (e.g., "travel") as needed <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
    *   Enables retrieval of the journal entry, where the LLM can format the JSON response into a readable Markdown display <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>, <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

### Implications for User Experience
*   **Dynamic UI:** While current clients don't fully support dynamic UI like cards, MCP enables the possibility for rich, context-aware displays <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   **[[multimodal_ai_and_the_future_of_human_interaction | Multimodal AI and the Future of Human Interaction]]:** LLMs can translate responses between languages (e.g., English server response to Japanese user query), enhancing accessibility <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Natural Interaction:** MCP facilitates a shift away from traditional browser-based interaction and keyword-specific searching <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. Instead, users can simply speak their questions, and the AI can understand intent and execute actions <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. This represents a return to more natural human-computer interaction <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

The vision is for users to eventually stop needing to "Google" or phrase questions precisely, instead communicating naturally with an AI that can understand and perform tasks for them <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>, <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

## Conclusion

MCP holds the promise of a future where a universal "Jarvis" becomes a reality for everyone, enabling AI assistants to integrate seamlessly with any service <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This represents an exciting [[future_of_ai_in_improving_user_experience_and_integrations | future of AI in improving user experience and integrations]] and [[building_user_experiences_with_ai | building user experiences with AI]] that prioritizes natural, intuitive interaction over complex manual processes <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>.

### Resources
*   Model Context Protocol Specification <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>
*   EpicAI.pro - for learning about MCP and AI in general <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.