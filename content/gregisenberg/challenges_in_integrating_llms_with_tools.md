---
title: Challenges in integrating LLMs with tools
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Large Language Models (LLMs) alone are fundamentally limited in their capabilities, primarily excelling at predicting the next word or answering questions based on their training data <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. They cannot, for instance, send an email or perform specific tasks on a user's behalf without external assistance <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. The evolution of LLMs has led to combining them with external "tools" or Application Programming Interfaces (APIs) to extend their functionality <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

## Limitations of Standalone LLMs
LLMs in their inherent state are good at predicting the next text <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>, such as completing "My Big Fat Greek" with "wedding" <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. However, they are "truly incapable of doing anything meaningful" like sending an email or performing a specific task on behalf of a user <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. Despite their apparent sophistication, LLMs "by themselves they're very very dumb" <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.

## The Evolution to LLM + Tools
To make LLMs more powerful and capable, developers began connecting them with tools, which can be thought of as APIs <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
Examples of such integrations include:
*   Enabling chatbots to search the internet (e.g., Perplexity) <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.
*   Connecting to services like Brave Search or OpenAI's API <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.
*   Automating tasks like creating a spreadsheet entry every time an email is received, using services like Zapier or End8 <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.

While these tools make LLMs "a bit more capable," the process of connecting them introduces significant challenges <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

## Core Challenges of Integration
Integrating multiple tools with LLMs to create sophisticated assistants presents substantial difficulties:

### Lack of Unified Standards
Although programming relies on standards like REST APIs for system communication <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>, each service provider constructs their APIs differently <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. This means different information needs to be passed, and various setup requirements exist <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>. The analogy used is that each tool speaks a "different language" (e.g., English, Spanish, Japanese) <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.

### Complexity and Cumbersomeness
Building an assistant that performs multiple functions (e.g., searching the internet, reading emails, summarizing) quickly becomes frustrating <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. Developers end up "gluing a bunch of different tools" to LLMs <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>, which is cumbersome and makes scaling very difficult <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. This is a primary reason why an "Iron Man level Jarvis assistant" is not yet common <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

### Manual Work and Maintenance Nightmares
Integrating tools involves significant manual work and step-by-step planning <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>. There are also many "edge cases where it can fail" <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. A major problem arises when an integrated service updates its API; this can break the entire automation or step-by-step process, turning it into a "nightmare" <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

### Hallucination and Quality Control
Even when connected to tools, LLMs can "hallucinate or do something stupid" <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. Ensuring a flawless user experience, fast performance, and limiting hallucinations with these integrations is "very very hard" and requires extensive engineering hours <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>. Companies like Tempo, an AI startup, dedicate considerable effort to managing these issues <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

## The Role of MCP as a Solution
The concept of MCP (Model-Controller-Protocol) emerges as a potential solution to these integration challenges. It acts as an intermediary layer between the LLM and the external services/tools <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. This layer translates all disparate tool languages into a unified language that the LLM can understand, simplifying connections to outside resources <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>. MCP aims to provide a standard that makes LLMs more capable and integrates seamlessly with various services <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>.

However, even with MCP, there are still [[challenges_and_limitations_of_ai_tools | technical challenges]], such as the annoying setup of MCP servers, which often involve local file movements <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>. The future of [[the_role_of_mcp_in_enhancing_llm_capability | LLM capability]] heavily relies on a finalized and universally adopted standard like MCP <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>.