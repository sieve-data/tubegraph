---
title: Specialized subagents in coding
videoId: Ri3iyi3qFlI
---

From: [[colemedin]] <br/> 

The landscape of coding is evolving rapidly, with many individuals, including non-coders, utilizing [[ai_coding_assistants | AI coding assistants]] like Windsurf or Cursor to achieve remarkable feats in productivity <a class="yt-timestamp" data-t="00:00:00">[00:00:08]</a>. While these tools offer significant strengths, such as documentation retrieval and Claude mCP support, they also come with notable flaws <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A primary issue is their tendency to hallucinate awful code, even when provided with extensive documentation and instructions <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This has highlighted the need for a significant upgrade to tackle these hallucination problems <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The next evolution in [[ai_coding_assistants | AI coding assistants]] is believed to be a complete paradigm shift centered around [[specialized_ai_agents | specialized sub-agents]] and Claude's mCP protocol <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## The Problem with Generalist AI Coders

Current [[ai_coding_assistants | AI coding assistants]] are often too general, acting as "Jack of all trades but also the master of none" when it comes to coding with diverse frameworks, tools, and libraries <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Providing them with documentation for a specific framework isn't enough; they remain too general, leading to inconsistent and error-prone code <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## The Solution: Specialized Sub-Agents

The proposed solution involves developing [[specialized_ai_agents | specialized agents]] designed specifically to code with particular tools or frameworks <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These [[specialized_ai_agents | specialized agents]] can then be called upon by general [[ai_coding_assistants | AI coders]] like Windsurf or Cursor when their specific expertise is required <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. This approach combines the flexibility of general coders with the precision of specialists <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

This is made possible through the Claude mCP (Model Communication Protocol) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. mCP is a protocol developed by Claude to standardize the use of tools with large language models (LLMs) <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. It allows for the creation of servers that expose API endpoints for various services (e.g., GitHub, Google Drive), dynamically providing these tools to an LLM <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### Archon: An Example of a Specialized Sub-Agent

Archon is an [[ai_agents_and_their_development | AI meta-agent]] designed to build other [[ai_agents_and_their_development | AI agents]] using Pydantic AI and LangGraph <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>, <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. The goal is to develop Archon into a robust [[specialized_ai_agents | specialized sub-agent]] that can be used within [[ai_coding_assistants | AI coders]] for agent development <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. By integrating Archon as an mCP tool, LLMs like Claude 3.5 Sonnet in Windsurf can access its specialized workflow for coding agents <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

#### Demonstration of Archon in Windsurf

A demonstration showcases Archon operating within Windsurf to build an [[ai_agents_and_their_development | AI agent]] capable of web searching using Brave <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

1.  **Prompting**: A simple prompt, "build me an [[ai_agents_and_their_development | AI agent]] using Archon that is able to search the web using Brave," is given to Windsurf <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  **Tool Invocation**: Windsurf, recognizing the need for agent creation, calls upon Archon via its mCP tools <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   First, a tool is used to create a "thread ID," which Archon uses to manage conversation history, similar to how Windsurf manages its own conversations <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    *   The primary tool then invokes Archon's API endpoint to begin the agent creation process <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
3.  **Archon's Workflow**: Archon executes its internal LangGraph workflow, which typically involves:
    *   A Reasoner model (e.g., 03 Mini) defining the scope for the agent and identifying relevant Pydantic AI documentation <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.
    *   A Coder agent (e.g., GPT-4o) performing Retrieval Augmented Generation (RAG) on the documentation to produce the initial version of the AI agent's code <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>, <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
4.  **Control Transfer**: Once Archon finishes generating the agent code, control is seamlessly passed back to Windsurf, which then creates the necessary files (e.g., `agent.py`, `requirements.txt`, `tools.py`, `.env.example`) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This demonstrates the effective collaboration between a general coder and a specialized sub-agent <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

#### Human-in-the-Loop Feedback

The system supports a human-in-the-loop feedback mechanism <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For instance, if the initial code for the Brave search agent sets the model to `None`, the user can prompt Windsurf to "ask Archon to fix the model" and specify `GPT-4o` <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. Archon is then invoked again using the same thread ID, jumping directly to the coder agent to make the necessary updates <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

> "I just love that like it just shows it like this is an agent asking another agent for help a sub agent when it knows it has the expertise it doesn't" <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>

## Why Not Just Use Built-in Documentation Features?

A common question is why not simply use the documentation features built into [[ai_coding_assistants | AI coders]] like Windsurf or Cursor (e.g., `@PydanticAI` for Pydantic AI documentation) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. There are two primary reasons for leveraging [[specialized_ai_agents | specialized sub-agents]] like Archon:

*   **Consistent Output and Structure**: Archon's "agentic flow," including its Reasoner model and system prompts, ensures a very consistent output structure for generated files and scripts <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. General coders like Windsurf produce code that varies significantly with each attempt <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Better Code Quality and Robustness**: Archon's structured approach, with plans for self-feedback loops and breaking problems into smaller steps, leads to more robust code <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This contrasts with general coders that "spew out all the code at once," potentially introducing more errors <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Managing Conversation History (Thread ID)

While mCP servers are generally designed to be stateless (tools respond and then forget everything) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, Archon, as a [[specialized_ai_agents | specialized sub-agent]], is stateful and maintains conversation history through its LangGraph graph <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This allows for iterative improvements via the human-in-the-loop feedback loop <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

To facilitate this, Archon creates a "thread ID" at the start of a conversation, which the LLM (e.g., in Windsurf) must remember and pass back to Archon for all future calls related to that conversation <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Although relying on the LLM to remember this ID is "a little bit uncomfortable," it has proven to work reliably <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

## Technical Implementation Details

mCP is a protocol developed by Claude that allows LLMs to dynamically access tools by spinning up servers that have access to API endpoints for various services <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

*   **Archon as an mCP Tool**: Archon is exposed as an mCP tool through a Fast API endpoint <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. This API endpoint wraps Archon's core LangGraph workflow, making it accessible to LLMs <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **Docstrings for LLM Guidance**: Python docstrings defined at the top of Archon's function definitions are crucial <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. These strings are included in the prompt for the LLM, informing it when and how to use Archon's tools <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. For example, instructions specify that the LLM must generate a thread ID before running Archon for the first time, and pass the same ID for subsequent iterations <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Simplified Setup**: A setup script automates the process of creating a virtual environment and generating the necessary mCP configuration for integration with [[ai_coding_assistants | AI coders]] like Windsurf or Cursor <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

## The Future of Specialized Sub-Agents

The integration of [[specialized_ai_agents | specialized sub-agents]] like Archon into [[ai_coding_assistants | AI IDEs]] via mCP opens up immense possibilities <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. The ability to run wild with complex agentic flows for specific tasks, without worrying about file creation and editing logistics (as the [[ai_coding_assistants | AI coders]] handle that), is a significant advantage <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.

Future plans for Archon include:
*   Adding more nodes and improving system prompts <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>.
*   Implementing self-feedback loops <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.
*   Breaking down agent creation into smaller, more manageable steps <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.
*   Developing a comprehensive tool library <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>, which would provide pre-made components (e.g., a Brave search tool) to prevent hallucinations related to external APIs <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.

Archon is a community-driven project, encouraging contributions and suggestions for its development <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>. This approach aims to create massively powerful sub-agents for building other agents with preferred frameworks <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.