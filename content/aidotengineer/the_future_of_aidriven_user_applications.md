---
title: The future of AIdriven user applications
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

The future of user interaction is shifting towards [[the_impact_and_future_potential_of_ai_and_agents | AI assistance]], driven by advancements like the Model Context Protocol (MCP) <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>. This transition aims to bring users into [[the_impact_and_future_potential_of_ai_and_agents | AI assistance]] environments, fundamentally changing how product developers and others reach their audience <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>.

## The Jarvis Ideal: A Vision for AI User Experience

Tony Stark's [[the_impact_and_future_potential_of_ai_and_agents | AI assistant]], Jarvis, from the Iron Man movies, serves as a powerful example of an ideal [[the_impact_and_future_potential_of_ai_and_agents | AI-driven]] user experience <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>.

Jarvis's capabilities include:
*   Compiling databases from disparate sources like SHIELD, FBI, and CIA intercepts <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>, though this is currently technically difficult for reasons other than technical limitations <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   Generating user interfaces (UIs) on demand <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.
*   Accessing public records <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
*   Retrieving thermogenic signatures and performing complex data joins across different datasets <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
*   Showing related news articles <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.
*   Creating flight plans <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
*   Interfacing with home systems, such as answering the doorbell <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
*   Utilizing various interaction methods beyond voice, including typing, gestures, and dynamic UI generation <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

While many of these capabilities are technologically possible today, such as generating UIs <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>, the challenge lies in creating a unified experience where an [[the_impact_and_future_potential_of_ai_and_agents | AI assistant]] can interface with virtually *everything* <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

## The Integration Challenge

The primary obstacle to achieving a ubiquitous [[the_impact_and_future_potential_of_ai_and_agents | AI assistant]] like Jarvis is the complexity of integrations <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. It is extremely difficult to build integrations for every possible service and application <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. For example, major [[AI application frameworks and architecture | AI developers]] like Google, OpenAI, or Anthropic are unlikely to build specific integrations for niche services, such as a local city government's park pavilion reservation website <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. Users desire one central [[the_impact_and_future_potential_of_ai_and_agents | AI assistant]] that can augment itself with any capability in the world <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.

## Evolution of AI Assistance and Integrations

### Phase 1: LLMs as Question Answering Systems
Around three years ago, the release of ChatGPT marked a pivotal moment <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. What made ChatGPT revolutionary was not just the underlying Large Language Model (LLM), which had existed for a long time, but the host application layer that provided an excellent user experience for interacting with an LLM <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. Initially, users had to manually provide context by copying and pasting text or images into the LLM and then manually extracting results <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.

### Phase 2: Host Application-Enabled Actions
In this phase, the host application gained the ability to tell the LLM what services were available and to retrieve more context if needed <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. This enabled the LLM to perform actions beyond answering questions, such as using search engines, scheduling meetings via calendar integrations, or summarizing messages with Slack integrations <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. However, this approach is limited by the time developers at companies like OpenAI or Anthropic can dedicate to building specific integrations <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. Proprietary plugin systems, like OpenAI's GPT plugin system, further fragment the integration landscape, requiring developers to build specific solutions for each platform <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

### Phase 3: Model Context Protocol (MCP)
MCP represents a paradigm shift by offering a standard protocol that all [[the_impact_and_future_potential_of_ai_and_agents | AI assistants]] can support <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. This standardization allows developers to build to the MCP specification, ensuring their services are usable by any compliant [[the_impact_and_future_potential_of_ai_and_agents | AI assistant]] <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>.

Key architectural aspects of MCP:
*   The host application communicates with the LLM and dynamically manages the available services <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.
*   The LLM selects the most appropriate tool based on the user's query and available services <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.
*   The host application creates a standard client for each service integration <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.
*   Service providers create MCP servers that interface with unique tools, resources, and prompts <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.
*   The communication between the server and client is standardized, allowing service providers to control the unique aspects of their service while maintaining interoperability <a class="yt-timestamp" data-t="12:49:00">[12:49:00]</a>.
*   MCP servers can incorporate robust authentication, such as OAuth 2.1, making them as secure as other applications using the standard <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>.

This standardization provides [[the_impact_and_future_potential_of_ai_and_agents | AI assistants]] the "hands" to perform real-world actions <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>. While full client readiness for dynamic UI display is still developing, there is no technical barrier to achieving it <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.

A demonstration using MCP servers showed how an [[the_impact_and_future_potential_of_ai_and_agents | AI assistant]] could:
*   Determine current location using a "locationator" server <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>.
*   Check weather conditions via a "get weather" server <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
*   Authenticate with a journaling server (EpicMe) using an O token <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>.
*   Create and retrieve journal entries, with the LLM formatting the output in a user-friendly way (e.g., Markdown) <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.
*   Perform actions like deleting posts and logging out, all while handling authentication seamlessly <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>.

A key distinction from Jarvis is the current need for [[human_oversight_and_interaction_in_aidriven_analysis | human oversight]] to approve tool calls due to a lack of established trust and capability <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>.

## The Future of User Interaction

The future of [[future_of_creative_tools_and_user_interaction | user interaction]] will move away from traditional browser-based experiences and manual search queries <a class="yt-timestamp" data-t="18:17:00">[18:17:00]</a>. Users will be able to speak their questions naturally, and the [[the_impact_and_future_potential_of_ai_and_agents | AI]] will not only understand what they are trying to search for but also what they are trying to *do*, and then execute that action for them <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>. This shift signifies a move toward more intuitive and action-oriented [[ai_applications_and_customer_success_stories | AI applications]].

## Resources

*   **Model Context Protocol Specification:** A comprehensive document for understanding MCP <a class="yt-timestamp" data-t="19:04:00">[19:04:00]</a>.
*   **EpicAI.pro:** A platform by Kent C. Dodds offering courses, posts, workshops, and cohorts on [[AI Engineering Trends | AI in general]] and [[future_of_creative_tools_and_user_interaction | user interaction]] <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>.