---
title: Building AI agents using primitives
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

The process of [[building_effective_ai_agents | building AI agents]] is undergoing a significant transformation, moving away from traditional frameworks towards a more modular approach using AI primitives <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This method aims to accelerate the development of production-ready AI agents <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## The Shift from Frameworks to Primitives

Many production-ready AI agents, such as Perplexity, Cursor, V0, and Chai, are not built on top of AI frameworks <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>.

> [!CAUTION] Limitations of AI Frameworks
> Frameworks are often criticized for being bloated, moving slowly, and containing unnecessary abstractions that hinder development <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. In a rapidly evolving field where new paradigms and LLMs emerge weekly, frameworks can quickly become outdated or inflexible <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.

Instead of frameworks, the recommended approach is [[ai_primitives_versus_frameworks | building on top of AI primitives]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Primitives possess a native ability to perform well in production environments <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. A good analogy is Amazon S3, a low-level primitive for data storage that scales massively without being a framework <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

> [!INFO] Defining AI Agents
> AI agents represent a new paradigm for writing code, fundamentally changing how coding projects and SaaS products are built <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. They are designed to automate tasks and interact with data or other systems.

## Core AI Primitives for Agent Development

AI primitives are small, composable building blocks that are useful across various stacks <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Key primitives for building AI agents include <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>:

*   **Memory:** An autonomous knowledge engine that can include a vector store, capable of scaling to terabytes of data for long-term storage and search <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>, <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Workflow Engine:** Purpose-built for multi-step agent tasks <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Threads:** Used to store and manage the context and history of conversations with an agent <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>, <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This includes "scratch pads" for temporary, relevant information <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Parser:** Extracts context from various file formats, such as converting PDF to text <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Chunker:** Splits extracted text into smaller pieces of context for similarity search <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Tools Infrastructure:** Allows agents to automatically call external APIs or services <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

When [[building_effective_agents | agents]] with composable primitives that come with cloud-based capabilities (like auto-scaling memory), the result is a serverless AI agent that automates heavy lifting <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Common AI Agent Architectures Using Primitives

Various agent architectures can be constructed using these fundamental AI primitives <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>, <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:

### 1. Augmented LLM
This architecture involves an agent that takes input, generates output using an LLM, and has the ability to call tools, access threads for conversation history, and utilize long-term memory <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This is a foundational architecture for almost any type of AI agent <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### 2. Prompt Chaining and Composition
This involves multiple agents working together in sequence <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. For example, one agent might classify an email as spam or not, and if not spam, another agent might draft a response <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. Examples include summary agents, features agents, and marketing copy agents working in concert <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### 3. Agent Router (LLM Router)
In this architecture, a routing agent (an LLM) decides which specialized agent should be called next based on the input <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. An example involves a router agent selecting between a summary agent (using Gemini), a reasoning agent (using Llama 70B), or a coding agent (using Claude Sonnet) <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### 4. Parallel Agents
Certain tasks allow for multiple agents to run simultaneously <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. This is simplified in languages like JavaScript, where a set of agents (e.g., sentiment, summary, decision-maker) can be run concurrently using `Promise.all` <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.

### 5. Orchestrator-Worker Agents
This architecture involves an orchestrator agent that plans and creates subtasks, which are then completed by multiple worker agents. Finally, a synthesizer agent consolidates the results <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. This mirrors deep research agent architectures <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. For instance, an orchestrator might break down a request for a blog post into subtasks for introduction, specific sections (productivity, work-life balance, environmental impact), and conclusion, with each section handled by a separate worker agent <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

### 6. Evaluator-Optimizer
In this pattern, an LLM (generator agent) produces a response (e.g., marketing copy), which is then evaluated by another LLM acting as a "judge" <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. The judge either accepts the response or rejects it, providing specific feedback for improvement <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. This iterative feedback loop helps optimize the output.

### 7. Memory Agent
A very common pattern where data is uploaded to a memory (e.g., PDF files), which is then parsed, chunked, and embedded. An AI agent can then query this memory to answer questions based on the stored data <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

## Practical Demonstrations of Primitive-Based Agents

Several real-world examples illustrate the power of building with primitives:

*   **Chat with PDF:** A basic AI agent built with memory (vector store), parser, and chunker primitives to allow users to chat with PDF content <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Deep Researcher Agent (Perplexity-like):** Analyzes a query, performs web searches, consolidates results, and generates a comprehensive response using tools like Exa <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
*   **Receipt Checker (OCR Agent):** Utilizes an OCR primitive (e.g., from Mistral) and an LLM (e.g., GPT-4 Vision) to process images of receipts, extract information like total paid and city, and analyze results <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   **Chat with Image Agent:** Uses a vision-capable LLM (e.g., GPT-4 Vision) to analyze an image provided via URL and answer questions about its content, such as a person's expression <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.

These examples demonstrate that 80% of even the most complicated AI agents can be built using these AI primitive patterns <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>, <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. The core idea is to create simple, reusable code blocks that avoid complex abstraction layers, which could become a migration challenge as LLMs and [[developing_ai_agents_and_agentic_workflows | agentic workflows]] continue to evolve <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.