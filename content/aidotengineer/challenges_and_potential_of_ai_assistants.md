---
title: Challenges and potential of AI assistants
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

User interaction is undergoing a significant transformation, with a shift towards AI assistance as users increasingly gravitate towards these platforms <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This evolution is being facilitated by developments like Model Context Protocol (MCP) <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The goal is to enable product developers to reach users where they want to be: inside AI assistants <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## The Vision: Tony Stark's Jarvis

An ideal AI assistant, exemplified by Tony Stark's Jarvis, demonstrates the vast potential of these technologies <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Jarvis can:
*   Compile databases from various sources (e.g., SHIELD, FBI, CIA intercepts) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Generate user interfaces (UI) on demand <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   Access public records <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Bring up and analyze data like thermogenic signatures <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Join and cross-reference different datasets <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   Show related news articles <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Create flight plans <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Provide real-time information, such as who is at the door <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Jarvis offers an amazing user experience, incorporating voice interaction, typing, gestures, and dynamic UI generation <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Without an AI assistant like Jarvis, such complex research and tasks would take significantly longer <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Current Challenges and Limitations of AI Assistants

Despite advancements, we don't yet have personal AI assistants like Jarvis widely available <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. While the technology for generating UI already exists <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, major [[challenges_in_ai_development | challenges]] persist.

The primary obstacle is the difficulty of building comprehensive integrations for all possible services and applications <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This is a significant part of the [[challenges_in_creating_effective_ai_agents | challenges in creating effective AI agents]] and [[challenges_in_ai_agent_development | challenges in AI agent development]]. Large companies like Google are unlikely to build integrations for niche services, such as a local city government website for reserving park pavilions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. If an AI assistant cannot integrate with "everything," users may not see the value in wiring it up for only "some things" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Evolution of AI Assistant Interaction and their Limitations
The development of AI assistants can be seen in three phases:

*   **Phase 1: ChatGPT Era (circa 3 years ago)**
    *   **Potential:** Large Language Models (LLMs) became pivotal due to their host application layer, which provided a good user experience for interfacing with LLMs, leading to rapid investment and improvement <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. They could answer questions effectively <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
    *   **Challenges:** Users had to manually provide context by copying and pasting information (e.g., code) into the LLM and then manually copying results back <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. LLMs could answer questions but couldn't *do* anything directly <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This manual context management was cumbersome <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

*   **Phase 2: Host Application Integrations**
    *   **Potential:** The host application began telling the LLM what tools were available, allowing the LLM to request more context or perform actions like scheduling meetings, accessing search engines, or summarizing Slack messages <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This addressed some of the [[challenges_in_building_ai_applications | challenges in building AI applications]] by enabling actions.
    *   **Challenges:** The capabilities were limited to the integrations built by the LLM developers (e.g., OpenAI, Anthropic), who lacked the time or incentive to integrate with every niche service <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Proprietary plugin systems (like OpenAI's GPT plugin system) mean developers must build unique integrations for each platform, which is unsustainable <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Users don't want to use multiple "LLM wrappers" or host applications; they desire a single Jarvis that can augment itself with any capability <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

## Model Context Protocol (MCP): A Solution to Integration Challenges

The Model Context Protocol (MCP) represents **Phase 3** in the evolution of AI assistants, aiming to overcome the current [[challenges_and_solutions_in_building_ai_agents | challenges and solutions in building AI agents]] by enabling pervasive integration <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### What is MCP?
MCP is a standard protocol that all AI assistants support or will soon support <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. It provides a standard mechanism for AI assistants to communicate with various tools and services <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### How MCP Works (Architecture)
*   The **host application** communicates with the LLM <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   The host application dynamically informs the LLM about available services, which can be added or removed <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   The LLM, knowing the available services and the user's query, selects the most appropriate tool <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   The host application creates a **standard client** for each service, meaning no special integration is needed <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Service providers** create MCP servers that interface with their specific tools, resources, prompts, and sampling mechanisms <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   The key is that the communication interface between the server and the client is standardized, while the unique aspects of each service are controlled by the service provider <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

This standardization gives Jarvis (the AI assistant) "hands" to perform actions <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

### Potential of MCP in Action
A demonstration illustrates MCP's capabilities, even though client-side dynamic UI support is still developing <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>:
*   An LLM, configured with MCP servers, can process requests like "Please write a journal entry for me" <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   MCP servers, such as "locationator" and "get weather," can determine current location and weather conditions, respectively <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
*   Authentication is built into MCP servers, using OAuth 2.1, ensuring security for authenticated tasks like creating journal entries <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   The LLM can generate and format content (e.g., a journal entry with a title and content) and even apply relevant tags <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   The server can communicate in a format sensible to it (e.g., JSON), and the client LLM can then reformat it for better user display (e.g., Markdown) <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   LLMs can translate responses from the MCP server into the user's preferred language, even if the server's native response is different <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   Tasks like deleting posts and logging out are handled securely through the authenticated MCP server <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

Currently, users might need to approve tool calls due to lack of trust or full capability, but this is expected to evolve <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## The Future: Beyond Browsers with AI Assistants

The transition ahead means users will increasingly move away from browsers and traditional search methods <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. Instead of typing specific keywords or phrases for search engines, users will naturally speak their questions and intentions to AI <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. The AI will not only understand what the user is trying to search for but also what they are trying to *do*, and then execute that action <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. This represents the vast [[challenges_and_benefits_of_ai_agents | challenges and benefits of AI agents]] and the significant potential of AI assistants to transform user experience.

MCP is instrumental in enabling this future, bringing us closer to a world where a "Jarvis for everybody" is a reality <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Resources
*   Model Context Protocol Specification <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>
*   EpicAI.pro: Learn more about MCP and AI in general, including posts, workshops, and cohorts <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.