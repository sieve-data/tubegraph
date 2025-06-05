---
title: AI primitives versus frameworks
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

AI agent development is undergoing a significant shift, moving away from traditional [[ai_application_frameworks_and_architecture | AI application frameworks and architecture]] towards the use of foundational [[building_ai_agents_using_primitives | AI primitives]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This approach is advocated by Ahmed, who has extensive experience in software development, having contributed to major platforms like WordPress, Next.js, Node.js, and React, and even NASA helicopter missions <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. His journey in LLMs began in 2020 with early access to GPT-3, leading to work on projects like GitHub Copilot <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## The Case Against AI Frameworks

Many production-ready AI agents, including those by Perplexity and Cursor, are *not* built on top of [[ai_application_frameworks_and_architecture | AI application frameworks and architecture]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This is because frameworks are often seen as:
*   **Bloated** <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   **Slow-moving** <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   **Filled with unnecessary abstractions** <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   **Hard to debug** due to obscure abstractions <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>

The rapid pace of AI development, with new paradigms, LLMs, and solutions emerging weekly, makes sticking to a fixed framework challenging <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>. Building with frameworks can lead to being "stuck" with an abstraction that might not adapt to future advancements in [[role_of_ai_agents_and_agentic_frameworks | agentic workflows]] <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

## The Power of AI Primitives

[[building_ai_agents_using_primitives | AI primitives]] are small, composable building blocks that work exceptionally well in [[benefits_of_ai_primitives_in_production | production]] environments <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. They offer:
*   **Native scalability**: Similar to Amazon S3, primitives are low-level and inherently scalable <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Simplicity**: They are straightforward, with "no magic, nothing to learn" <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Composability**: Allowing engineers to combine them to build complex [[role_of_ai_agents_and_agentic_frameworks | AI agents]] <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Production readiness**: When primitives come with built-in cloud capabilities (like memory with auto-scaling vector stores), they enable serverless [[role_of_ai_agents_and_agentic_frameworks | AI agents]] that handle heavy lifting automatically <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

::startcallout
> [!NOTE] All engineers are becoming AI engineers.
> Ahmed believes that most engineers, including full-stack, web, front-end, DevOps, and ML engineers, are transitioning into [[ai_implementation_and_best_practices | AI engineering]] roles, actively shipping products with AI <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
::endcallout

## Key AI Primitives

Essential [[building_ai_agents_using_primitives | AI primitives]] for building agents include <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>:
*   **Memory**: An autonomous "rag engine" (retrieval-augmented generation) that can store and retrieve terabytes of data, often with an integrated vector store for similarity search <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Threads**: For storing and managing context and conversation history within an agent <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Parser**: To extract context from various file formats (e.g., PDF to text) <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Chunker**: To split extracted context into smaller, manageable pieces for similarity search <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Tools Infrastructure**: Enables agents to automatically call external APIs or interact with other systems <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Workflow Engine**: Purpose-built for multi-step agent processes <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

Langbase provides these primitives, aiming to be the fastest way to build production-ready [[role_of_ai_agents_and_agentic_frameworks | AI agents]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Common AI Agent Architectures Using Primitives

Ahmed demonstrates several common [[ai_application_frameworks_and_architecture | AI agent architectures]] built purely with [[building_ai_agents_using_primitives | AI primitives]] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>:

### 1. Augmented LLM
This is a fundamental agent that takes input and generates output using an LLM. It integrates [[tool_usage_and_development_in_ai_frameworks | tools]], threads (for short-term context/scratchpad), and memory (for long-term storage and retrieval of large datasets) <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This architecture can be used to build almost any type of [[role_of_ai_agents_and_agentic_frameworks | AI agent]] <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### 2. Prompt Chaining and Composition
This architecture involves multiple agents working together in a sequence. An input is processed by one agent, and its output determines the next step, potentially involving another agent. Examples include a summary agent feeding into a features agent, then a marketing copy agent <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This is implemented using plain JavaScript/TypeScript code <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

### 3. Agent Router (LLM Router)
Here, a routing agent (or LLM router) decides which specialized agent should be called next based on the input query <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **Example**: Three specialized agents (summary, reasoning, coding) built with different [[ai_models_and_training_methods | LLM models]] (Gemini, Llama 70B, Claude Sonnet) are available. A routing agent is configured to select the appropriate one based on the user's task <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. The router's job is to respond with valid JSON indicating the next agent <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

### 4. Running Agents in Parallel
For tasks that can be broken down into independent sub-tasks, multiple agents can be run concurrently. JavaScript's `Promise.all` function can easily orchestrate this without complex abstractions <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. An example includes running sentiment analysis, summarization, and a decision-maker agent in parallel <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### 5. Agent Orchestrator Worker
This pattern, resembling deep research agent architectures, involves an orchestrator agent that plans and creates subtasks. These subtasks are then completed by multiple worker agents in parallel, and their results are synthesized by another agent <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   **Example**: Writing a blog post on remote work benefits (productivity, work-life balance, environmental impact) <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   The orchestrator breaks this into subtasks: "write introduction," "write section on productivity," etc. <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
    *   Multiple worker agents execute these subtasks concurrently <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
    *   Finally, a synthesizing agent combines the results into a cohesive blog post <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

### 6. Evaluator Optimizer
An agent generates a response (e.g., marketing copy), which is then evaluated by another LLM acting as a "judge." This judge either accepts the response or rejects it with specific feedback. The feedback is then used to refine the generation in subsequent iterations <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. This iterative process allows for continuous improvement of generated content <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

### 7. Memory-Based Agents
A common pattern involves creating a memory for storing data (e.g., PDFs, web pages). This data is parsed, chunked, and embedded using primitives, allowing an [[role_of_ai_agents_and_agentic_frameworks | AI agent]] to perform similarity searches and answer questions based on the stored information <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Example 1: Chat with PDF**: Uploading PDF documents to a memory, then asking questions that retrieve and synthesize answers from the stored content <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Example 2: Receipt Checker**: Using OCR (Mistral) to process an image of a receipt, extracting relevant information like total paid and city <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
*   **Example 3: Chat with Image**: Analyzing an image URL using a vision-capable LLM (GPT-4o) to describe content, expressions, etc. <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.

These [[patterns_of_ai_native_development | patterns of AI Native Development]] leveraging primitives can cover approximately 80% of complex [[role_of_ai_agents_and_agentic_frameworks | AI agents]] <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

::startcallout
> [!TIP] Chai for Vibe Coding AI Agents
> Chai is a platform that allows users to "vibe code" [[role_of_ai_agents_and_agentic_frameworks | AI agents]] by building them on top of [[building_ai_agents_using_primitives | AI primitives]] instead of frameworks <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It simplifies the process of building, deploying, and using agents <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.
::endcallout