---
title: User experience design with AI
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

Kent C. Dodds, an educator in building excellent user experiences, notes a significant shift towards AI as the next frontier for user interaction <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. His course platform, epicai.pro, focuses on how to build excellent [[usercentric_ai_design_and_feedback_loops | user experiences]] with AI <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The core topic of this shift is how [[usercentric_ai_design_and_feedback_loops | user interaction]] is changing and the role of product developers in reaching users within AI assistance platforms <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## The Vision: Jarvis as the Ideal AI Assistant

To illustrate the potential of AI, Tony Stark's AI assistant, Jarvis, from the Iron Man movies serves as a benchmark <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Jarvis's capabilities in a [[case_studies_and_practical_examples_of_ai_implementation | practical example]] include:
*   Compiling databases from various sources (e.g., SHIELD, FBI, CIA intercepts) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Initiating virtual crime scene reconstructions <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   Accessing public records <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Analyzing thermogenic signatures and performing cross-dataset joins <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Generating UIs on demand and interacting with them <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   Showing related news articles <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Creating flight plans <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Answering the doorbell and displaying visitor information <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Jarvis represents an "awesome [[usercentric_ai_design_and_feedback_loops | user experience]]" that leverages various input methods like typing, gestures, and [[voice_ai_and_its_applications_in_enhancing_customer_experience | voice AI]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. While some of Jarvis's abilities, like generating UIs, are already technically possible today <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, a key missing piece is the ability to create databases from classified information or display complex holographic interfaces <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## The Problem: The Challenge of Integrations

The primary obstacle preventing widespread adoption of Jarvis-like AI assistants is the immense difficulty of building comprehensive integrations for all possible services and applications <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Companies like Google or OpenAI are unlikely to build integrations for highly specific services, such as a local city's park pavilion reservation website <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Users desire a single AI assistant that can augment itself with any capability in the world, rather than managing multiple AI wrappers or applications <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

## Model Context Protocol (MCP) as the Solution

The Model Context Protocol (MCP) is introduced as a standard mechanism that enables AI assistants to communicate with various tools and services <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Evolution of AI Interactions
1.  **Phase One: ChatGPT and LLM Host Application Layer** <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>
    *   The release of ChatGPT marked a pivotal moment, not just for the LLM itself, but for the host application layer that provided a good [[usercentric_ai_design_and_feedback_loops | user experience]] for interfacing with LLMs <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
    *   Initial limitations included manual context provision (copy-pasting text or images) and lack of ability to *do* anything beyond answering questions <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

2.  **Phase Two: Host Application Enables Action** <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>
    *   The host application began informing the LLM about available services (e.g., search engines, calendar integrations, Slack integrations) to fetch context and perform actions <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
    *   This phase was still limited by the time developers at LLM providers (like OpenAI or Anthropic) could dedicate to building integrations <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Proprietary plugin systems (like OpenAI's GPT plugin system) create silos, requiring special builds for each platform <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

3.  **Phase Three: MCP - The "Do Anything" Era** <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>
    *   MCP is a standard protocol that all AI assistants will support, allowing developers to build to one specification and be usable by any assistant <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
    *   This is anticipated to bring about a general-purpose Jarvis for everyone <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

### MCP Architecture
The architecture of MCP involves:
*   **Host Application**: Communicates with the LLM and dynamically manages available services <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **LLM**: Knows what services are available and selects the most appropriate tool based on the user's query <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **MCP Client**: A standard client created by the host application for each service, featuring a standard interface <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **MCP Server**: Created by the service provider, interfacing with unique tools, resources, prompts, and sampling features <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

This standardization of communication between the server and client is what gives AI assistants "hands" to perform actions <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>, enabling [[enhancing_existing_systems_with_ai_capabilities | enhancing existing systems with AI capabilities]].

## Demonstration of MCP Capabilities

A demonstration showcased MCP servers integrated with a Cloud Desktop environment, which operates with an LLM <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Key features and capabilities demonstrated include:
*   **Location Awareness**: An MCP server called "locationator" determined the user's current location <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
*   **Weather Integration**: Another server, "get weather," retrieved current weather conditions for given coordinates <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **Authentication**: An "EpicMe" MCP server handled user authentication using OAuth 2.1, making it as secure as other OAuth-based systems <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   **Contextual Actions**: The LLM, informed by location and weather, could generate and create a journal entry through the authenticated MCP server <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   **Dynamic Tagging**: The system could check for available tags and create new ones (e.g., "travel" tag for a trip entry) <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   **Intelligent Rendering**: The LLM could retrieve the journal entry and decide on a user-friendly format (e.g., Markdown) rather than raw JSON, demonstrating the potential for dynamic UI display via future clients <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **Language Translation**: The LLM can translate server responses (e.g., English to Japanese) for the user, even if the server only sends responses in one language <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Full CRUD Operations**: The demo included deleting the post and logging out, showcasing full functionality <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. Notably, the EpicMe MCP server is designed to be accessible only via MCP clients, not as a traditional web application <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

## The Future of User Interaction

The transition facilitated by MCP means users will no longer need to rely on browsers or specific search engine phrasing <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. Instead, they can naturally speak their questions and intentions, and the AI will understand and execute the desired actions <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. This shift moves towards a more natural and direct way of interacting with technology, akin to the vision of Jarvis <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. This represents a significant [[strategies_for_effective_ai_implementation | strategy for effective AI implementation]] and a [[best_practices_for_implementing_ai_in_teams | best practice]] in future AI development.

## Resources

*   **Model Context Protocol Specification**: The core documentation for MCP <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
*   **EpicAI.pro**: Kent C. Dodds's platform for learning about MCP and AI in general, offering posts, workshops, and cohorts focused on the future of [[usercentric_ai_design_and_feedback_loops | user interaction]] with AI <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.