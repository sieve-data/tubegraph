---
title: Adoption challenges and future of AI protocols
videoId: ywMWpmOOaSo
---

From: [[colemedin]] <br/> 

Google recently introduced their Agent-to-Agent (A2A) protocol, a standard designed for AI agents to communicate effectively with each other <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This protocol is seen as revolutionary, similar to how the Model Context Protocol (MCP) standardized connecting agents to tools <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Both A2A and MCP are complementary and are expected to significantly impact the future of AI agents and their communication <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a> <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

While MCP did not immediately gain widespread attention, it gradually became recognized for its power <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. A2A, recently released, appears to be following a similar path, as technical protocols often take time for people to grasp and for creators to refine for wide adoption <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## What is A2A?

A2A is a high-level architecture rather than a downloadable tool or framework <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a> <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. The code available in its GitHub repository serves as examples for building agents that conform to the A2A protocol <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. Being 100% open-source is crucial for its wide adoption <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

Key components of the A2A architecture include:
*   **Agent Card:** A single metadata file that allows an agent to describe its capabilities, how to interact with it, and any authentication requirements to other agents <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Server/Client Model:** Agents run as servers (HTTP endpoints) and clients, similar to a microservices architecture <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Clients consume A2A services by calling these servers <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Tasks:** Communication involves generating a unique identifier for a task, sending a request (JSON payload) to the agent server, and receiving a response that includes the results and metadata about the task's execution <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a> <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a> <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Push Notifications:** A2A supports push notifications, allowing server-side agents to update client agents in real-time <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Benefits of A2A

A2A offers several significant advantages for [[integrations_and_collaboration_in_ai_platforms | AI agent integrations]]:
*   **Standardization and Accessibility:** It makes the process of connecting agents more accessible and standardized, similar to how MCP improved tool integration <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a> <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Flexibility in Development:** Agents can be built using different frameworks (e.g., Langraph, CrewAI, or no framework) and hosted by different vendors in various cloud environments. As long as they adhere to the A2A protocol, they can communicate seamlessly <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a> <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This flexibility is not easily achieved without such a protocol <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Agent Discovery:** A2A introduces the concept of "agent discovery," where one agent (e.g., a sales agent) can learn in real-time what another agent (e.g., a finance agent) is capable of and how to interact with it <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This dynamic capability significantly reduces the risk of breaking integrations when agents are updated, unlike traditional hardcoded integrations <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a> <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Complementary Protocols: A2A and MCP

A2A and MCP are highly complementary, operating on different layers of the agent architecture <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a> <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. MCP focuses on agent-to-tool communication, while A2A handles agent-to-agent communication <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. For example, a client agent can use A2A to call into a server agent, which then uses MCP and a tool (like the Brave API) to perform a web search and fulfill the client's request <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a> <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This combination allows for a complete backend for AI applications, with A2A managing servers and agents, and MCP providing tools <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## [[ai_agent_development_challenges | Challenges with AI Protocols (A2A & MCP)]]

Despite their power, these protocols face several [[ai_agent_development_challenges | challenges]] that must be addressed for widespread adoption and production readiness:

*   **Testing Complexity:** When an AI system is distributed across multiple nodes (A2A servers, MCP tools), testing becomes significantly more complex <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. This leads to "edge case explosions," where problems are hard to reproduce due to the many interacting components <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. The unpredictable nature of Large Language Models (LLMs) further complicates debugging, as failures might be due to hallucinations <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
*   **Security Concerns:** A distributed system with multiple nodes increases the surface area for cyber security attacks <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Relying on third-party MCP or A2A servers means more entities handle sensitive data, raising concerns about data privacy and security <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. Robust authentication challenges also arise in carrying user requests through the entire AI system with sub-agents and tools <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
*   **Hidden Complexity and Debugging:** Protocols can act as black boxes, making it difficult to fully understand their inner workings or how to interact with them correctly <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. In distributed systems, error attribution can be very challenging without excellent logging, monitoring, and tracing <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. Accountability for failures can also be hard to assign, as an issue with a tool might stem from incorrect parameters provided by an agent <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

## Future Outlook

Despite these [[ai_agent_development_challenges | challenges]], solutions are being developed. Google is working on authentication, and companies like Anthropic are addressing issues related to MCP <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. Historical engineering problems in areas like databases and microservices show that issues like edge case explosions and debugging complex systems can be overcome <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

It is anticipated that within one to two years, protocols like MCP and A2A will enable the easy creation of scalable, secure, and testable AI systems that can handle diverse requests <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>. Significant work is still required, but the progress indicates a promising [[future_of_ai_in_coding_and_development | future of AI in coding and development]] for these protocols <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.

A2A is poised to establish a new standard for [[importance_of_ai_agents_in_2025 | AI agents]] going forward <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. However, widespread adoption will take time as Google and other companies work to address the existing issues <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.