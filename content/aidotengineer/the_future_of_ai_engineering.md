---
title: The future of AI engineering
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

The landscape of AI engineering is rapidly evolving, with a significant shift away from traditional AI frameworks towards the use of foundational [[evolution_of_ai_engineering_and_tools | AI primitives]]. This transition is redefining how developers approach building and deploying AI agents, emphasizing agility, scalability, and direct control over core components <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Current State of AI Agents

Many production-ready AI agents, such as Perplexity, Cursor, and Chai, are not built on top of conventional AI frameworks <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Frameworks are often criticized for being bloated, slow, and filled with unnecessary abstractions <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Instead, successful agents leverage [[evolution_of_ai_engineering_and_tools | AI primitives]], which offer a more direct and efficient approach to development <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

> "All these AI agents in production are actually not built on top of any AI frameworks because, well, frameworks do not really add that much value. They're bloated. They move super slowly and they they're filled with these abstraction that nobody really needs. Instead, you should be building on top of AI primitives." <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>

This shift is compared to the utility of Amazon S3, a simple, low-level primitive for data storage that scales massively without requiring an object storage framework <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## AI Agents as a New Way of Coding

AI agents represent a fundamental change in how code is written and projects are built <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. The complexity of building and deploying scalable AI agents remains a significant challenge <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This new paradigm is too significant to be constrained by rigid frameworks; instead, it calls for small, reusable building blocks <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### The Rise of the AI Engineer

A prevailing belief is that most engineers will transition into [[collaboration_between_human_engineers_and_ai | AI engineers]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This trend is already visible with full-stack, web, and front-end developers rapidly adopting AI engineering roles, building products with LLMs and vector stores <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. DevOps and ML engineers are also increasingly shipping AI-powered products <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Improving the AI Engineering Experience

The goal in this evolving space is to provide the fastest possible way to build production-ready AI agents <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This involves moving away from the "painful way" of using frameworks with obscure, hard-to-debug abstractions and deployment challenges <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

Instead, the focus is on building atop predefined, highly scalable, and composable [[evolution_of_ai_engineering_and_tools | AI primitives]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Essential AI Primitives

Several core primitives are vital for building robust AI agents:

*   **Memory:** An autonomous RAG (Retrieval Augmented Generation) engine that can store and scale with terabytes of data via a vector store <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Threads:** For storing and managing context and conversation history within an agent <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Parser:** To extract context from various data formats, such as converting PDFs to text <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Chunker:** To split extracted content into smaller, manageable pieces for similarity search <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Tools Infrastructure:** Allows agents to connect to external APIs and services <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Workflow Engine:** Purpose-built for multi-step agent processes <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

Building with these primitives allows for the creation of serverless AI agents that automatically handle heavy lifting and scaling <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Common AI Agent Architectures Built with Primitives

### Augmented LLM

This is a foundational architecture where an agent, powered by an LLM, processes input and generates output. It integrates:
*   **Tools:** For calling external APIs <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Threads:** For storing conversational context and scratchpad information <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
*   **Memory:** For long-term data storage and retrieval, often requiring a vector store <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

### Prompt Chaining and Composition

This architecture involves multiple AI agents working together in sequence. An input is processed by one agent, and its output determines the next action, potentially triggering another agent <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. Examples include an agent identifying spam emails, then another drafting a response <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

### Agent Router (LLM Router)

An LLM-based router decides which specialized agent should be called next based on the task <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This allows for specialized agents (e.g., summary, reasoning, coding agents), each potentially optimized with a different LLM (e.g., Gemini for summary, Llama 70B for reasoning, Claude for coding) <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. The router's job is to respond with valid JSON indicating the appropriate agent <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

### Parallel Agent Execution

For tasks where multiple agents can operate independently, they can be run in parallel using simple programming constructs like `Promise.all` in JavaScript <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. Examples include sentiment analysis, summarization, and decision-making agents <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### Agent Orchestrator Worker

This sophisticated architecture involves an orchestrator agent that plans and creates subtasks, which are then assigned to multiple worker agents. The results from worker agents are then synthesized by another agent <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. This mimics a "deep research agent" architecture <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

### Evaluator Optimizer

An LLM (acting as a generator) produces a response (e.g., a marketing copy), which is then evaluated by another LLM (acting as a judge). The judge either accepts or rejects the output, providing specific feedback for improvement <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. This feedback loop allows for iterative refinement of the generated content <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

## Implications for the [[future of AI in coding | Future of AI in Coding]]

The reliance on [[evolution_of_ai_engineering_and_tools | AI primitives]] over frameworks ensures adaptability in a fast-moving AI landscape <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>. New paradigms, LLMs, and problem-solving techniques emerge frequently <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. Building with primitives avoids being "stuck" with an abstraction layer that might hinder migration when LLMs become more sophisticated in handling agentic workflows <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. This approach enables rapid development and deployment of scalable AI agents <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.

### [[State of AI Engineering | State of AI Engineering]] Research

Further insights into building agents, the types of primitives used, and LLM requirements across industries can be found through dedicated research efforts <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.