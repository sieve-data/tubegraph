---
title: Building AI agents using Context 7
videoId: G7gK8H6u7Rs
---

From: [[colemedin]] <br/> 

[[limitations_of_ai_coding_assistants_and_overcoming_them_with_context_7 | AI coding assistants]] are powerful tools that can significantly increase a software engineer's speed or enable non-technical individuals to build complex applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, a major limitation of these assistants is their tendency to hallucinate when working with specific tools or frameworks <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This issue highlights the need for a tool that provides instant Retrieval Augmented Generation (RAG) for AI coding assistants, offering the necessary context for tools and frameworks <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Context 7 is a free tool designed to address this, providing comprehensive and up-to-date documentation <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## [[features_and_capabilities_of_context_7_for_ai_coding | Features and Capabilities of Context 7]]

Context 7 supports 1,856 different tools and frameworks, allowing [[limitations_of_ai_coding_assistants_and_overcoming_them_with_context_7 | AI coding assistants]] to perform RAG on extensive documentation <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This includes popular technologies like Nex.js, MongoDB, Superbase, Pydantic AI, React, LangGraph, and MCP <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

Key [[features_and_capabilities_of_context_7_for_ai_coding | features]] include:
*   **Up-to-date Documentation**: Documentation can be refreshed at any point to ensure it's completely current <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Structured Examples**: Context 7 curates individual components as small snippets, making it easy for Large Language Models (LLMs) to parse <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. These snippets often serve as examples, which is crucial for helping LLMs code reliably <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This structured approach, rich in examples, makes Context 7 more powerful than custom documentation features built into some [[limitations_of_ai_coding_assistants_and_overcoming_them_with_context_7 | AI coding assistants]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

## [[integration_of_context_7_into_ai_development_environments | Integration of Context 7 into AI Development Environments]]

Context 7 can be integrated into various [[integration_of_context_7_into_ai_development_environments | AI development environments]] like Cursor, Windsurf, Client, and Rue Code <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The integration process typically involves copying a JSON configuration into an MCP (Multi-Agent Communication Protocol) config file <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

Once configured, Context 7 provides two primary tools to the [[understanding_ai_agents | AI agent]]:
1.  **Resolve Library ID**: This tool allows the [[understanding_ai_agents | AI agent]] to input a search term (e.g., "Superbase") and receive a list of the most relevant documentation pages, along with their unique IDs <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
2.  **Get Library Docs**: After obtaining a specific library ID, the [[understanding_ai_agents | AI agent]] calls this function to perform RAG over the documentation for that framework or tool <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. The [[understanding_ai_agents | AI agent]] also decides the search topic (e.g., "authentication") and the number of tokens to retrieve from the search <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This ability to reason about and control the token count further enhances its power compared to simpler custom documentation features <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## [[building_ai_agents | Building AI Agents]] with Context 7: A Practical Example

An [[building_ai_agents | AI agent]] can be built to leverage Context 7 for its RAG capabilities, creating a "meta" scenario where an [[building_ai_agents | AI agent]] uses Context 7 to build another [[building_ai_agents | AI agent]] that also uses Context 7 <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Setup and Configuration
To set up an [[building_ai_agents | AI agent]] in an environment like Windsurf, global rules can be defined to instruct the [[understanding_ai_agents | agent]] on how to use Context 7's tools <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. For instance, the rules can specify to start a search with 5,000 tokens, increase to 20,000 if needed, and use a fallback search service if Context 7 fails <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Agent Construction
A demonstration involved [[building_ai_agents_with_python | building an AI agent]] using the Pydantic AI framework in Windsurf, with Context 7 providing the necessary documentation <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The process included:
*   **Documentation Retrieval**: The [[understanding_ai_agents | agent]] first called the `resolve_library_id` tool for Pydantic AI, then `get_library_docs` to retrieve 20,000 tokens of documentation, including examples <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Environment Variables**: The [[understanding_ai_agents | agent]] was designed to use environment variables for its base URL and model, allowing flexibility with different LLM providers like Open Router, Olama, Gemini, and OpenAI <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Command Line Interface**: A simple command line interface was created to interact with the [[understanding_ai_agents | agent]] <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

### Agent Demonstration
After construction, the [[understanding_ai_agents | agent]] was run from the terminal <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. It successfully responded to basic conversational queries and, more importantly, demonstrated its integration with Context 7:
*   **Listing Available Docs**: When asked "What superbase docs are available to me?", the [[understanding_ai_agents | agent]] used the `resolve_library_id` tool to list available Superbase documentation IDs <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Retrieving Specific Code Examples**: When prompted "Great use this to tell me how to watch for real time changes in my Superbase DB", the [[understanding_ai_agents | agent]] performed RAG on the Superbase documentation, providing working code examples from Context 7's structured data <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

## Impact
Context 7 streamlines the process of providing up-to-date, version-specific documentation with code examples directly from source <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. It eliminates the need for developers to manually scrape, store, and embed documentation, making it a game-changer for both [[building_ai_agents | AI agents]] and [[limitations_of_ai_coding_assistants_and_overcoming_them_with_context_7 | AI coding assistants]] <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. Its MCP server can be integrated into any existing [[integration_of_context_7_into_ai_development_environments | AI coding assistance]] workflow, enhancing their power <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.