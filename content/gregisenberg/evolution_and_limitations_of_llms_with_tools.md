---
title: Evolution and limitations of LLMs with tools
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Large Language Models (LLMs) have evolved significantly, but their capabilities and integrations have presented both advancements and challenges. Professor Ross Mike explains the current state and future of LLMs in conjunction with external tools and the role of new standards like MCP.

## Initial Limitations of LLMs
Initially, LLMs were limited in their direct capabilities. By themselves, LLMs are primarily good at predicting the next text based on their training data [00:02:42]. For example, if given "My Big Fat Greek," an LLM would predict "wedding" [00:03:30]. They can answer questions or provide information about historical figures [00:03:01], but they are incapable of performing meaningful external actions. An LLM cannot send an email directly [00:02:56] or perform specific tasks on behalf of a user [00:03:19].

## The Evolution: LLMs + Tools
The next evolution in LLM capability involved developers combining them with external tools, often in the form of APIs [00:03:48]. This integration allowed LLMs to interact with and leverage external services. For instance, chatbots like Perplexity gained the ability to search the internet by accessing external search services [00:04:00]. Similarly, an LLM could be connected to automation services like Zapier or End8 to perform tasks such as creating a spreadsheet entry every time an email is received [00:04:46]. This approach made LLMs "a bit more capable" [00:06:37].

### Challenges of Tool Integration
Despite the advancements, integrating multiple tools with LLMs quickly became cumbersome and frustrating [00:05:09]. The process often felt like "gluing a bunch of different things together" [00:08:29]. While standards like [[significance_of_standards_in_llms_and_apis | REST APIs]] exist for communication between systems, each service provider constructs their APIs differently, requiring varied information and setup [00:08:15].

The difficulties included:
*   **Complexity**: Creating an assistant that performs multiple functions (e.g., searching the internet, reading emails, summarizing content) requires extensive work to make these tools cohesive and work together [00:05:38].
*   **Manual Work**: Integrating tools often involves significant manual setup, step-by-step planning, and addressing numerous edge cases where the system might fail [00:09:38].
*   **Maintenance Nightmare**: If an external service's API updates (e.g., Slack or a text service), it can break existing automations, leading to extensive debugging and downtime [00:10:18].
*   **Hallucinations**: Even with tools, LLMs can be "very very dumb" by themselves [00:06:30], and engineers must ensure the LLM doesn't hallucinate or make errors when using external services [00:06:26].

These challenges are why a "Jarvis-level assistant" akin to Iron Man's AI has not yet been realized [00:05:30].

## The Next Step: Multi-Modal Communication Protocol (MCP)
[[tool_and_function_calling_in_ai_applications | MCP]] is a new standard designed to address the limitations of current LLM-tool integrations [00:12:51]. It acts as a unifying layer between the LLM and various services or tools [00:08:38].

### How MCP Works
MCP translates the diverse "languages" (different API structures and requirements) of various tools into a single, unified language that the LLM can consistently understand [00:08:45]. This simplifies the process for LLMs to connect with and access outside resources like databases (e.g., Convex or Superbase) [00:09:01].

The MCP ecosystem involves:
1.  **MCP Client**: The LLM-facing side (e.g., Tempo, Windsurf, Cursor) [00:11:13].
2.  **MCP Protocol**: The two-way communication standard between the client and server [00:11:32].
3.  **MCP Server**: Built by the service provider, this component translates the external service's capabilities for the client [00:11:38]. This means the responsibility for enabling LLM access shifts to the service providers themselves [00:12:18].
4.  **Service**: The external tool or API (e.g., a database, an email service) [00:11:41].

By shifting the responsibility for the MCP server to service providers, Anthropic (who developed MCP) encourages a standardized way for all external services to communicate with LLMs [00:11:51]. This promises to make LLMs more capable and integrations much smoother [00:12:46].

### Current State and Future Outlook
While MCP is a significant step towards more capable LLMs, it is still in its early stages. Setting up an MCP server can be annoying, involving local file management and copying [00:13:59]. There are "kinks that have to be figured out" before the standard is finalized [00:14:08].

The development of MCP highlights the importance of [[significance_of_standards_in_llms_and_apis | standards]] in making complex systems scalable and interoperable. Just as standards like HTTPS and SMTP led to the creation of large businesses, a finalized and widely adopted standard for LLM interaction with tools could unlock new entrepreneurial opportunities [00:15:54].

For technical individuals, there's potential in developing tools like an "MCP App Store" where users can easily deploy and connect to various MCP servers [00:16:38]. For non-technical individuals, the key is to stay informed about which platforms are adopting MCP and how the standards evolve. Observing this space will allow individuals to understand how future innovations will work and be prepared to strike when a finalized standard creates clear business opportunities [00:17:52]. This period is for observing and learning, as the space is very early, and the dominant standard may still change [00:19:11].