---
title: Future of AI in improving user experience and integrations
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

Kent C. Dodds teaches how to build excellent user experiences, initially for the web and now shifting to [[building_user_experiences_with_ai | AI]], as users are moving towards AI platforms <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. His course platform, epicai.pro, focuses on this transition <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The core focus is on how user interaction is changing, facilitated by Model Context Protocol (MCP), and the role product developers play in reaching users within AI assistants <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## The Ideal AI Assistant: Tony Stark's Jarvis

The aspiration for [[the_evolution_of_ai_interfaces_and_user_interaction | future AI interfaces]] is exemplified by Tony Stark's AI assistant, Jarvis <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Jarvis demonstrates an advanced level of interaction, performing complex tasks seamlessly <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

Jarvis's capabilities include:
*   Compiling databases from disparate sources (e.g., SHIELD, FBI, CIA intercepts) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Generating dynamic user interfaces (UI) on demand for complex data visualization <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   Accessing public and private records <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Analyzing and plotting data (e.g., thermogenic occurrences) <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   Joining across different datasets and filtering information <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   Showing related news articles <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Creating flight plans <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Interfacing with home systems (e.g., doorbell cameras) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   Utilizing various interaction methods beyond voice, such as typing and gestures <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

While some capabilities like creating databases from classified sources or holographic displays are still challenging, the technology exists for generating UI dynamically <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. The question then becomes, why don't we have our own Jarvis already <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>?

## The Challenge: Building Integrations

The primary obstacle preventing widespread adoption of universal AI assistants like Jarvis is the difficulty of building robust integrations <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Users desire one central AI that can interface with *everything*, not just a select few popular services <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Large companies like Google are unlikely to build integrations for niche services, such as a local city government website for reserving park pavilions <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. If an AI cannot do "everything," the incentive to spend time wiring up integrations for "some things" diminishes <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Evolution of AI Interaction and the Integration Problem

The evolution of AI interaction can be categorized into phases:

#### Phase 1: LLMs as Question Answering Systems (e.g., Early ChatGPT)
*   **Description:** Approximately three years ago, ChatGPT introduced a pivotal moment by providing a good user experience around a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. These LLMs could answer questions, generating tokens based on input <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Limitation:** Users had to manually provide context (e.g., copy-pasting code or text) and then manually extract the results <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. The LLM couldn't *do* anything directly, only answer questions <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

#### Phase 2: Host Application Integrations
*   **Description:** Host applications began to tell the LLM which services were available, allowing the LLM to request more context or perform actions through integrations like search engines, calendars, or Slack <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Limitation:** The capabilities were limited by the integrations built by the LLM developers (e.g., OpenAI or Anthropic) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. These developers wouldn't build integrations for highly specific or local services <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. While proprietary plugin systems like OpenAI's GPT plugins exist, building separate integrations for each LLM provider is impractical <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Users don't want multiple specialized AI wrappers; they want *one* Jarvis that can augment itself with any capability <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

#### Phase 3: Model Context Protocol (MCP)

Model Context Protocol (MCP) is introduced as the solution to the integration problem <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. MCP provides a standard mechanism for AI assistants to communicate with various tools and services <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### MCP Architecture and Benefits
*   **Standard Protocol:** MCP is a standard protocol that all AI assistants will support, allowing developers to build to the MCP specification and be usable by any AI assistant <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **Dynamic Services:** The host application communicates with the LLM, informing it of available services that can be dynamically added or removed <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. The LLM selects the most appropriate tool based on the user's query and available services <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Standardized Clients:** The host application creates a standard client for each service, eliminating the need for special integrations <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Service Provider Control:** Service providers create MCP servers that interface with their unique tools, resources, and prompts <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. This allows service providers to control the unique aspects of their offering, while the server-client communication remains standard <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **"Jarvis's Hands":** MCP gives AI assistants the ability to "do stuff" by providing a standardized way to interact with external services <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

## Enhancing User Experience with MCP: A Demo

A demonstration of MCP showcases how an LLM can interact with different MCP servers for a journaling task:
1.  **Location and Weather:** An MCP server called "locationator" determines the current location, and another "get weather" tool retrieves weather conditions based on coordinates <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
2.  **Authentication:** The EpicMe MCP server handles authentication using OAuth 2.1, allowing the AI client to perform authenticated tasks like creating journal entries <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This means [[customer_success_with_ai_solutions | customer success with AI solutions]] can be built securely.
3.  **Dynamic Tagging:** The LLM can check available tags and create new ones (e.g., "travel" for a trip entry), then apply them <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
4.  **Intelligent Formatting and Translation:**
    *   When retrieving a journal entry, the LLM can decide to format the raw JSON data into a more readable Markdown format with a title <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
    *   The LLM can translate responses from an MCP server (e.g., English) into the user's preferred language (e.g., Japanese), further enhancing [[the_evolution_of_ai_interfaces_and_user_interaction | user interaction]] <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

This demonstrates a significant shift in [[the_role_of_user_experience_in_ai | the role of user experience in AI]]. Users will no longer need to rely on specific keywords or search formats like in traditional search engines <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. Instead, they can speak naturally, and the AI will understand their intent to *accomplish a task*, not just find information <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. This leads to [[applications_and_future_of_ai_technology | AI applications]] that can actively perform actions for the user <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

## Conclusion and Future Outlook

The advent of MCP is poised to bring about a universal Jarvis-like experience for everyone <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. While AI clients are still developing to fully leverage MCP, the potential for seamless, integrated AI assistance is immense <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This marks a significant step in [[advancements_in_ai_and_future_implications | advancements in AI and its future implications]], particularly for [[integrating_ai_into_business_operations | integrating AI into business operations]] and personal workflows.

For further learning, resources include the Model Context Protocol specification and epicai.pro, which offers insights into AI and its impact on [[the_future_of_ai_engineering | AI engineering]] and [[future_of_voice_applications_in_ai | user interaction]] <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.