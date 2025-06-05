---
title: Building user experiences with AI
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

Kent C. Dodds teaches how to build excellent user experiences, initially for the web, and now with AI through his course platform, epicai.pro <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The focus is on how [[the_evolution_of_ai_interfaces_and_user_interaction | user interaction]] is changing, enabled by technologies like Model Context Protocol (MCP), to reach users where they want to be: inside AI assistants <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

## The Vision: Jarvis as the Ideal AI Assistant

The ideal [[the_role_of_user_experience_in_ai | user experience]] is exemplified by Tony Stark's AI assistant, Jarvis <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. Jarvis can perform a wide range of actions that would take a human much longer, if not be impossible, to do without AI assistance <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

**Jarvis's Capabilities:**
*   Compiles databases from various sources (e.g., SHIELD, FBI, CIA intercepts) <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   Generates UIs on demand <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   Accesses public records <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   Brings up thermogenic signatures <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   Joins across different datasets to filter information <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   Shows related news articles <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   Creates flight plans <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   Interacts with physical environment (e.g., answering doorbell, displaying visitor info) <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   Offers multi-modal interaction: talking, typing, gestures, and dynamic UI generation <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

While generating UIs is already possible <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>, creating databases from sensitive government sources or developing holographic interfaces are still areas of advancement <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. The core question is why we don't each have a Jarvis already, given that the technology for many of these capabilities exists <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

## The Challenge: Integrations

The primary obstacle to a widespread Jarvis-like AI assistant is the difficulty of building comprehensive **integrations** <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. Users desire a single robot that can interface with *everything*, from well-known services to niche local government websites <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>. Building individual integrations for every conceivable service is impractical for large AI companies like Google or OpenAI <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. Without universal capability, the incentive to invest in wiring up partial solutions diminishes <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

Users want an AI assistant that can interface with a service they've never used before and may never use again, without requiring manual website navigation <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>. They want their Large Language Model (LLM) to "figure that out" <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.

## The Solution: Model Context Protocol (MCP)

Model Context Protocol (MCP) aims to provide a standard mechanism for AI assistants to communicate with various tools and services <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.

### History and Evolution of AI Interaction

The evolution of AI interaction can be categorized into three phases:

#### Phase 1: ChatGPT and LLM Host Applications
Around three years ago, ChatGPT's release marked a pivotal moment, not primarily because of the LLM itself (which had existed for a while), but due to the host application layer that provided a good [[the_role_of_user_experience_in_ai | user experience]] for interfacing with an LLM <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>. This application layer drove significant investment and rapid improvement in LLMs <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>.

*   **Capabilities:** Answered questions <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.
*   **Limitations:** Users had to manually provide context (copy-pasting code, text, or images) and manually apply results <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>. The LLM couldn't perform actions or manage context automatically <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.

#### Phase 2: LLMs with Built-in Integrations
In this phase, the host application became more sophisticated, integrating with the LLM to provide context and enable actions <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. Examples include search engines, calendar integrations, and Slack summarizers <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.

*   **Capabilities:** LLMs could "do stuff" beyond just answering questions <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.
*   **Limitations:** Capabilities were limited by the developer's time at companies like OpenAI or Anthropic to build integrations <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. Proprietary plugin systems (like OpenAI's GPT plugin system) required building specific solutions for each platform, lacking a universal standard <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. Users don't want multiple LLM "wrappers" with specific tools; they desire one universal Jarvis <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

#### Phase 3: Model Context Protocol (MCP)
MCP represents the next leap, enabling AI assistants to "do anything" <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>. It is designed as a standard protocol that various AI assistants will support, allowing developers to build to the MCP specification and be usable by any compliant AI assistant <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>.

*   **Capabilities:** Enables universal integration and capability for AI assistants. It promises to bring us "just one really good [[the_role_of_user_experience_in_ai | user experience]] application away from Jarvis for everybody" <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.

### MCP Architecture

The MCP architecture facilitates seamless communication and capability expansion:
1.  **Host Application to LLM:** The host application communicates with the LLM, informing it about available services, which can be dynamically added or removed <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>. The LLM uses this context, along with the user's query, to select the most appropriate tool <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>.
2.  **Host Application Client:** The host application creates a standard client for each service it wants to interface with. This client uses a standard interface, avoiding special integrations <a class="yt-timestamp" data-t="12:09:00">[12:09:09]</a>.
3.  **Service Provider MCP Servers:** Service providers create MCP servers that interface with their specific tools, resources, and prompts. This unique part is controlled by the service provider, while the server-client communication remains standard <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>.

This standardized communication is what gives "Jarvis hands" to actually perform tasks <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>.

### MCP in Action (Demo)

A demo showcased MCP servers in action, configured with a Cloud Desktop host application <a class="yt-timestamp" data-t="13:20:00">[13:20:00]</a>. While current clients may require user approval for tool calls (unlike Jarvis, who has built trust with Tony), the potential is clear <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>.

**Example Scenario:**
*   **Prompt:** "Please write a journal entry for me... derive my location and weather conditions from my device location and make up a creative story." <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>
*   **MCP Server Interactions:**
    *   **Locationator:** Determines current location <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>.
    *   **Get Weather:** Retrieves weather conditions for given coordinates <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
    *   **EpicMe (Journaling Server):**
        *   **Authentication:** Uses OAuth 2.1 for secure login <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>.
        *   **Create Journal Entry:** The LLM writes the entry, and the server configures inputs <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.
        *   **Tag Management:** Checks and creates relevant tags (e.g., "travel") for the entry <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>.
        *   **Retrieval and Formatting:** The server can retrieve entries and format them in a sensible way (e.g., Markdown), which the client can then display dynamically <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>.
        *   **Language Translation:** The LLM can translate server responses (e.g., English to Japanese) if the user is interacting in a different language <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
        *   **Deletion and Logout:** Demonstrates full functionality including authenticated actions <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>.

This transition means users will soon no longer need to use browsers or meticulously phrase search queries <a class="yt-timestamp" data-t="18:17:00">[18:17:00]</a>. Instead, they can speak naturally, and the AI will understand their intent ("what you're actually trying to do") and perform the action <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>. This is what MCP enables and makes the [[future_of_ai_in_improving_user_experience_and_integrations | future of AI in improving user experience and integrations]] so exciting <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.

## Resources

*   The Model Context Protocol specification <a class="yt-timestamp" data-t="19:04:00">[19:04:00]</a>.
*   EpicAI (epicai.pro) offers resources on MCP, AI in general, the [[the_evolution_of_ai_interfaces_and_user_interaction | future of user interaction]], and workshops <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>.