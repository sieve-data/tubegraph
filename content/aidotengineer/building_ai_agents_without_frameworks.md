---
title: Building AI agents without frameworks
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

The conventional approach to [[building_and_improving_ai_agents | building and improving AI agents]] often involves using AI frameworks. However, a significant trend among production-ready AI agents, including those from Perplexity, Cursor, v0, Lovable Bold, and Chai, indicates that these agents are not built on top of AI frameworks [00:00:51]. Instead, they are built using AI primitives [00:01:16].

## Why Avoid AI Frameworks?

AI frameworks are generally avoided for several reasons:
*   **Bloated** Frameworks tend to be overly complex [00:01:23].
*   **Slow Movement** They evolve slowly, which is problematic in the rapidly changing AI space [00:01:25].
*   **Unnecessary Abstractions** Frameworks are often filled with abstractions that developers don't need [00:01:27].
*   **Migration Challenges** Being tied to a framework's abstraction can make it difficult to migrate when LLMs and agentic workflows improve [00:19:44].

Instead, the recommendation is to build on top of AI primitives [00:01:31]. Primitives, like Amazon S3 for object storage, offer low-level, scalable components that can be used to build many different applications [00:02:29].

## What Are AI Primitives?

AI primitives are small, composable building blocks that are highly scalable and useful across an AI stack [00:03:56]. They have a native ability to work well in production environments [00:02:29].

Key [[components_of_ai_agents | components of AI agents]] that can be implemented as primitives include:
*   **Memory** An autonomous RAG (Retrieval Augmented Generation) engine that can store and retrieve terabytes of data, often with an integrated vector store, and automatically scales [00:05:24].
*   **Threads** Used to store and manage context or conversation history for an agent [00:04:01, 00:10:35, 00:11:39].
*   **Parsers** Extract context from various file types, such as converting PDFs to text [00:10:41].
*   **Chunkers** Split extracted context into smaller pieces for similarity search [00:10:43].
*   **Tools** Enable an agent to call external APIs or interact with other systems [00:11:33].
*   **Workflow Engine** Purpose-built for multi-step agents [00:10:30].

Using these primitives, developers can create serverless AI agents that automatically handle heavy lifting [00:05:13].

## Building AI Agents with Primitives

The process of [[building_and_improving_ai_agents | building and improving AI agents]] with primitives focuses on creating simple, composable blocks rather than complex, abstracted layers.

### Example: Chatting with a PDF

A common AI agent is a chatbot that interacts with data, such as a PDF [00:00:09, 00:00:19].
1.  **Create Memory**: A memory primitive is used to store the PDF content, which includes a vector store [00:06:16].
2.  **Upload Data**: PDF files are uploaded into this memory [00:07:39, 00:22:08].
3.  **Process Data**: A parser primitive converts PDFs to text, and a chunker primitive splits the text into small pieces of context for similarity search [00:08:14].
4.  **Generate Answers**: An AI agent (LLM) is built on top of this memory to answer questions by retrieving relevant content and generating responses [00:06:24, 00:08:57].

This setup allows the agent to retrieve information from multiple files in memory, even if the information is distributed [00:09:34].

### Different Architectures for AI Agents

Several [[different_architectures_for_ai_agents | different architectures for AI agents]] can be built using AI primitives:

#### 1. Augmented LLM
This is a basic agent architecture where an LLM is augmented with tools, threads, and memory primitives [00:11:18, 00:12:37]. It can take an input, generate an output, automatically call tools, store conversation context, and access long-term memory [00:11:24]. This architecture is versatile enough to build almost any type of AI agent [00:12:47].

#### 2. Prompt Chaining and Composition
This architecture involves multiple agents working together in sequence [00:13:06]. An input triggers an agent, whose output then determines if another agent should be called [00:13:16].
*   **Example**: An agent checks if an email is spam; if not, another agent drafts a response [00:13:22]. This can involve a summary agent, features agent, and marketing copy agent, all implemented in plain JavaScript or TypeScript [00:13:35].

#### 3. Agent Router / LLM Router
In this architecture, an agent or LLM router decides which specialized agent needs to be called next to handle a specific task [00:14:00, 00:14:02].
*   **Example**: Three specialized agents (summary, reasoning, coding) are built with different LLMs (Gemini, Llama 70B, Claude Sonnet, respectively) [00:14:26, 00:14:41]. A routing agent is given the task and accesses these agents, responding with valid JSON to pick the appropriate agent for the job [00:15:06].

#### 4. Running Agents in Parallel
For tasks that can be executed concurrently, multiple agents can be run in parallel [00:16:47, 00:16:50]. This is straightforward in JavaScript using `Promise.all` [00:16:55].
*   **Example**: A sentiment summary agent and a scene maker agent can run simultaneously [00:17:00].

#### 5. Agent Orchestrator Worker
This architecture involves an orchestrator agent that plans and creates subtasks, which are then completed by multiple worker agents. A final agent synthesizes the results [00:17:13]. This mirrors a deep research agent architecture [00:17:27].
*   **Example**: An orchestrator generates subtasks for writing a blog post (e.g., introduction, sections on productivity, work-life balance, environmental impact, conclusion) [00:18:10, 00:18:21]. Multiple worker agents then complete these individual subtasks, and a final step synthesizes the output [00:18:44, 00:19:02]. The code is typically short and simple, avoiding complex abstraction layers [00:19:08].

#### 6. Evaluator Optimizer
An agent generates a response (e.g., marketing copy), which is then evaluated by another LLM acting as a "judge" [00:20:08, 00:20:20]. The judge accepts or rejects the response, providing specific feedback if rejected [00:20:25, 00:21:08]. The generating agent then uses this feedback to improve its output in subsequent iterations [00:21:32].

#### 7. Memory-Based Agents
As demonstrated with the PDF chat, agents can be built around memory primitives where data is uploaded, and the agent retrieves and answers questions from that data [00:21:50, 00:22:19].

### Complex Agents Built with Primitives

With these AI primitive patterns, it's possible to build around 80% of the most complex AI agents [00:22:24]. Examples include:
*   **Deep Researcher**: Similar to Perplexity, it analyzes queries, performs web searches, consolidates results, and creates responses [00:22:37].
*   **Receipt Checker**: Uses an OCR (Optical Character Recognition) primitive to process images of receipts, extract information like total paid and city, and can use multiple OCR models for fallback and improved accuracy [00:23:13].
*   **Image Chat**: Allows users to chat with images by analyzing image URLs using vision-capable LLMs like GPT-4o [00:24:17].

## Conclusion

The rapidly evolving AI landscape, with new paradigms and LLMs emerging frequently, makes [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agent frameworks and orchestration layers in AI engineering]] cumbersome [00:25:51]. Building AI agents on robust, scalable AI primitives provides flexibility and avoids being stuck with pre-built abstractions [00:25:58, 00:26:08]. These primitives can be built custom or used from pre-existing libraries [00:26:13].