---
title: Challenges in creating AI assistants like Jarvis
videoId: EyZiAp0pelw
---

From: [[aidotengineer]] <br/> 

The concept of a highly capable personal AI assistant, epitomized by Tony Stark's Jarvis, is a long-held aspiration for users and developers alike <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Jarvis can perform a wide range of complex tasks, from compiling databases and generating dynamic user interfaces (UIs) to accessing public records, joining disparate datasets, creating flight plans, and even interacting with smart home systems <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. While current technology allows for UI generation <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, the pervasive availability of a Jarvis-like AI remains elusive <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Unmet Capabilities of Current AI Assistants

Despite advancements, several of Jarvis's abilities are still beyond the common user's reach:
*   **Database Compilation from Disparate Sources**: Currently, creating databases from sensitive, inter-agency sources like SHIELD, FBI, and CIA intercepts is not technically feasible <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Seamless Dynamic UI & Multimodal Interaction**: While dynamic UI generation is possible <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, the fluid holographic interfaces and integrated voice/typing/gesture interactions seen with Jarvis are still being developed <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Complete Autonomy and Trust**: Tony Stark didn't need to approve every action Jarvis took, indicating a high level of trust and autonomous capability that current AI assistants lack <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Users currently have to approve tool calls due to a lack of established trust and capability <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## The Core Challenge: Integrations

The primary obstacle preventing widespread adoption of Jarvis-like AI assistants is the immense [[challenges_in_developing_ai_agents | difficulty of building integrations]] <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Users desire a single AI that can interface with *everything* <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Integration Hurdles
*   **Scale of Services**: There are countless online services, both technical and everyday, that a truly universal AI would need to interact with <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Developer Resource Limitations**: Large AI companies like Google, OpenAI, or Anthropic cannot realistically build integrations for every niche service, such as a local city government website for reserving park pavilions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Proprietary Systems**: Existing plugin systems, like OpenAI's GPT plugin system, are proprietary <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This forces developers to build separate integrations for each major AI platform (e.g., ChatGPT, Anthropic, Google), which is not sustainable <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

If an AI cannot do "everything," the incentive to spend time wiring up complex integrations for "some things" diminishes, especially for infrequent activities <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Users want a single Jarvis capable of augmenting itself with any capability in the world, without needing to switch between different LLM wrappers or manually transfer context <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

## Historical Challenges in AI Development

### Phase 1: Manual Context Management
When LLMs like ChatGPT first emerged around three years ago, they were pivotal for their ability to answer questions and for the user experience provided by their host application layer <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. However, a significant [[challenges_with_current_ai_implementation | challenge with current AI implementation]] was the requirement for users to manually provide context by copying and pasting information (e.g., code) and then manually extracting the LLM's output back into their workflows <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This made managing context a laborious process <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Phase 2: Host Application Limitations
The next phase saw host applications integrating with LLMs, allowing the LLM to request more context or trigger actions like searching, scheduling, or summarizing messages via pre-built integrations (e.g., calendar, Slack) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This enabled LLMs to "do stuff" <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. However, this approach was still limited by the specific integrations built by the LLM provider's developers <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Users who couldn't get a built-in integration often had to build their own wrapper applications with custom tools <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

## Model Context Protocol (MCP): The Solution

Model Context Protocol (MCP) is presented as the standard mechanism to overcome these [[design_challenges_for_ai_agents | design challenges for AI agents]] and integration hurdles <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. MCP provides a standardized way for AI assistants to communicate with various tools and services <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### How MCP Addresses Challenges
*   **Standardization**: MCP is designed as a standard protocol that all different AI assistants are expected to support, or will support soon <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This means developers can build to the MCP spec once, and their service will be usable by any compliant AI assistant <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
*   **Dynamic Service Provision**: Host applications communicate available services to the LLM, and these services can be dynamically added or removed, allowing for flexible context management <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. The LLM selects the most appropriate tool based on the user's query <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Service Provider Control**: Service providers create MCP servers that interface with their unique tools, resources, and prompts, while the communication between the server and the standard client remains consistent <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Built-in Authentication**: MCP servers incorporate authentication, such as OAuth 2.1, ensuring secure interactions <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   **Enhanced User Experience**: MCP facilitates a more natural user interaction, allowing users to simply speak their questions and intentions, rather than needing to formulate specific search queries or navigate complex UIs <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. The AI can then figure out what the user is trying to accomplish and perform the action directly <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   **Multimodal and Dynamic Output**: While current clients might not fully support dynamic UIs or cards, the protocol allows servers to communicate in a way that enables clients to display content beyond raw JSON, potentially even rendering Markdown or translating responses into different languages <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>, <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

While client applications are not yet fully ready at the time of recording, MCP is anticipated to bring about a monumental shift, enabling "Jarvis for everybody" by providing AI assistants with the "hands" to perform actual tasks <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>, <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>, <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. This transition is expected to move users away from traditional browser-based interactions towards more intuitive AI-driven interfaces <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.