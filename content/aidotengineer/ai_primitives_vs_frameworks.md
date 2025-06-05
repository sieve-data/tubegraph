---
title: AI primitives vs frameworks
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

The landscape of AI engineering is rapidly evolving, with a key debate centering on the best approach to building AI agents: using established frameworks or focusing on fundamental AI primitives. Many production-ready AI agents are notably not built on top of [[agent_frameworks_and_orchestration_layers_in_ai_engineering | AI frameworks]] <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>.

## The Case Against AI Frameworks

According to Ahmed, [[agent_frameworks_and_orchestration_layers_in_ai_engineering | frameworks]] for AI agents often present several issues:
*   They don't add significant value <a class="yt-timestamp" data-t="01:21:38">[01:21:38]</a>.
*   They are "bloated" <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a>.
*   They move "super slowly" in a fast-evolving space <a class="yt-timestamp" data-t="01:24:99">[01:24:99]</a>, <a class="yt-timestamp" data-t="02:54:26">[02:54:26]</a>.
*   They are "filled with these abstractions that nobody really needs" <a class="yt-timestamp" data-t="01:27:01">[01:27:01]</a>.
*   Frameworks can be hard to debug <a class="yt-timestamp" data-t="05:05:07">[05:05:07]</a>.
*   They can lead to difficulty in migrating off abstractions when LLMs improve at agentic workflows <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>, <a class="yt-timestamp" data-t="01:54:26">[01:54:26]</a>.

Instead of frameworks, the recommendation is to build on top of [[the_role_of_ai_primitives_in_scaling | AI primitives]] <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## The Power of AI Primitives

[[the_role_of_ai_primitives_in_scaling | AI primitives]] are described as fundamental, low-level building blocks for AI agents <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>, <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. They offer several advantages:

*   **Native Scalability**: Primitives possess a "native ability of working really, really well in production" and can scale massively, much like Amazon S3 <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>, <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. When [[the_role_of_ai_primitives_in_scaling | AI primitives]] are composable and cloud-integrated (e.g., memory with an auto-scaling vector store), they enable serverless AI agents that handle heavy lifting automatically <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>, <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>, <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>, <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.
*   **Simplicity and Composability**: They are simple, low-level components that can be used to build a wide variety of solutions <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>, <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
*   **Faster Development**: Building on predefined, highly scalable, and composable [[the_role_of_ai_primitives_in_scaling | AI primitives]] is presented as the fastest way to build a production-ready AI agent <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>, <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **Flexibility**: Primitives allow engineers to build their own custom "AI framework" on top of them, avoiding the constraints of a pre-built, bloated framework <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

### Examples of AI Primitives
Core [[the_role_of_ai_primitives_in_scaling | AI primitives]] highlighted include:
*   **Memory**: An autonomous "rag engine" or long-term memory, often incorporating a vector store, capable of handling terabytes of data for similarity searches <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>, <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>, <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.
*   **Threads**: For storing and managing context and conversation history within an agent <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>, <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>, <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. This includes "scratch pad" functionality for temporary context <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
*   **Parser**: To extract context from various data formats (e.g., PDF to text) <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>, <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.
*   **Chunker**: To split extracted context into smaller, manageable pieces for efficient processing <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>, <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.
*   **Tools Infrastructure**: The ability to automatically call tools and connect to APIs (e.g., MCPS) <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>, <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>.

## Building AI Agents with Primitives

The core idea is that an AI agent is a "new way of writing code" <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>, and it's large enough that a single framework abstraction might not suffice <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. Instead, focus on small, reusable building blocks <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

Most engineers are expected to transition into [[evolution_of_ai_engineering_and_tools | AI engineering]] roles, needing efficient ways to build and ship AI products <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>, <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>, <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

Chai, a platform, demonstrates [[building_ai_agents_without_frameworks | building AI agents without frameworks]] by providing [[the_role_of_ai_primitives_in_scaling | AI primitives]] to streamline the process <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>, <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>, <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.

### Common AI Agent Architectures using Primitives
[[different_architectures_for_ai_agents | Different architectures for AI agents]] can be built purely with [[the_role_of_ai_primitives_in_scaling | AI primitives]]:

*   **Augmented LLM**: An agent that takes input, generates output using an LLM, and has access to tools, threads, and memory <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.
*   **Prompt Chaining and Composition**: Multiple agents work together sequentially, where one agent's output influences the next <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Agent Router / LLM Router**: An agent or LLM that decides which other specialized agent should be called next based on the input task (e.g., summary, reasoning, coding) <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>, <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.
*   **Parallel Agents**: Multiple agents run simultaneously to process different aspects of an input, often managed using JavaScript's `Promise.all` <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>.
*   **Agent Orchestrator Worker**: An orchestrator agent plans and creates subtasks, which are then distributed to multiple worker agents for execution, with another agent synthesizing the results <a class="yt-timestamp" data-t="17:10:00">[17:10:00]</a>, <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>. This pattern is common in deep research agent architectures <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.
*   **Evaluator Optimizer**: An agent generates content (e.g., marketing copy), and a separate LLM acts as a "judge" to evaluate it, providing feedback for optimization if rejected <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>.
*   **Memory Agent (RAG)**: An agent that uploads data to a memory primitive (like a vector store), retrieves relevant information, and then answers questions based on that data <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>, <a class="yt-timestamp" data-t="21:59:00">[21:59:00]</a>.

These patterns illustrate how [[the_role_of_ai_primitives_in_scaling | AI primitives]] enable the creation of complex and specialized AI agents without relying on cumbersome frameworks <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>. This approach covers approximately 80% of the most intricate AI agents <a class="yt-timestamp" data-t="22:29:00">[22:29:00]</a>.

## Conclusion

In a rapidly evolving AI landscape where new paradigms and LLMs emerge frequently <a class="yt-timestamp" data-t="02:54:26">[02:54:26]</a>, [[the_role_of_ai_primitives_in_scaling | AI primitives]] offer a more stable and flexible foundation for [[ai_native_development_patterns | AI native development patterns]] <a class="yt-timestamp" data-t="02:54:26">[02:54:26]</a>, <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. The argument is to build AI agents on top of these robust, pre-built, or custom-developed primitives, avoiding unnecessary abstractions that can hinder scalability and adaptability <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>, <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.