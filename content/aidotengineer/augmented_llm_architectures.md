---
title: Augmented LLM architectures
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

Augmented LLM architectures represent a new way of building AI agents, focusing on the use of fundamental **AI primitives** rather than traditional, often bloated, AI frameworks [00:01:16]. The core idea is that production-ready AI agents, especially those used by millions of people, are typically not built on top of AI frameworks due to their bloat, slow movement, and unnecessary abstractions [00:01:01]. Instead, they leverage low-level, composable AI primitives that offer massive scalability and flexibility [00:02:29].

AI agents are fundamentally "a new way of writing code" [00:03:32], enabling engineers to transition into "AI engineers" and ship AI products rapidly [00:04:17].

## Key AI Primitives

The development of robust AI agents relies on a set of specialized primitives, which are small, composable building blocks that can be integrated seamlessly:

*   **Memory** <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>: An autonomous retrieval engine that can store and scale with terabytes of data, typically incorporating a vector store for efficient similarity search <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. It serves as the long-term memory for an agent <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Threads** <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>: Used to store and manage the context or history of a conversation, acting like a scratchpad for short-term information relevant to a task <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Parser** <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>: Extracts context from various file types, such as converting PDFs to text <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Chunker** <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>: Splits extracted context into smaller, manageable pieces for use in similarity searches <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Tools** <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>: Mechanisms that allow LLMs to automatically call external APIs or interact with other systems <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Workflow Engine** <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>: A purpose-built component for managing multi-step agent processes <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

Building with these primitives allows for the creation of serverless AI agents that automatically handle heavy lifting and scaling <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Common Augmented LLM Architectures

Several common [[mCPs Role in Augmented LLM Systems | AI agent architectures]] can be built using these primitives:

### 1. Basic Augmented LLM

This is the most common architecture, where an agent takes an input and generates an output using an LLM. It's augmented with the ability to automatically call [[llm_access_to_tools_and_tool_integrations | tools]], access threads for conversational context, and utilize long-term memory (often with a vector store) for vast amounts of data <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This versatile architecture can form the basis of almost any AI agent <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### 2. Chat with Data (RAG Pattern)

One of the most common [[integration_of_llms_with_recommendation_systems | AI agents]] in production involves a chatbot interacting with specific data <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
Example: **Chat with PDF** <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
This architecture involves:
*   Creating a **memory** (with a vector store) to store PDF content <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   Utilizing a **parser** primitive to convert PDFs to text <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   Employing a **chunker** primitive to split the text into smaller pieces for similarity search <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   An LLM agent then uses this memory to answer questions related to the uploaded data <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

### 3. Prompt Chaining and Composition

This architecture involves multiple agents working together in sequence <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. An input leads to an output from one agent, which then informs the decision to proceed with another agent.
Example: Processing an email for spam, then using another agent to draft a response if it's not spam <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. This can involve specialized agents like a summary agent, features agent, and marketing copy agent, all interacting through plain JavaScript/TypeScript code <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### 4. Agent Router (LLM Router)

In this setup, an agent, or an LLM router, decides which other specialized agent should be called next based on the input query <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
Example: Routing agent for different tasks <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   A **summary agent** (e.g., using Gemini) for summarizing text <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   A **reasoning agent** (e.g., using DeepSeek Llama 70B) for analysis and explanations <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   A **coding agent** (e.g., using Claude Sonnet) for code generation <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
The routing agent determines the most appropriate specialized agent to handle the task <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. This leverages [[comparison_between_general_and_specific_llms | domain-specific LLMs]] for specific tasks.

### 5. Parallel Agent Execution

This architecture is straightforward, running multiple agents simultaneously to process different aspects of an input <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. In JavaScript, this can be achieved using `Promise.all` to run a set of agents concurrently <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
Example: Sentiment analysis, summarization, and decision-making agents running in parallel <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### 6. Agent Orchestrator Worker

This is a sophisticated architecture, resembling a deep research agent system <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. An orchestrator agent plans and creates subtasks, which are then distributed to multiple worker agents. The results from these worker agents are finally synthesized by another agent <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
Example: Writing a blog post on remote work benefits <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   The orchestrator agent generates subtasks like "write introduction," "write section on productivity," "write conclusion" <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.
*   Each subtask is assigned to a simple worker agent that completes it <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   Finally, a synthesizing agent combines the outputs of all worker agents into a cohesive response <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. This highlights [[leveraging_llms_for_creative_tool_automation | automation capabilities]] for complex content generation.

### 7. Evaluator Optimizer (Self-Correction Loop)

This architecture uses an LLM as a "judge" to evaluate responses generated by another agent <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. The judge agent either accepts the response or rejects it with specific feedback, which is then used by the generator to improve its next attempt <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. This pattern is crucial for [[evaluation_of_llms_using_realworld_scenarios | refining LLM outputs]].
Example: Generating an eco-friendly product description <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
*   A generator agent creates the description <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.
*   An evaluator agent provides feedback (e.g., "missing the point with eco-conscious millennials") <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   The generator then uses this feedback to produce an improved version <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
The evaluator should be built using the best possible LLM for the specific evaluation domain <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.

### 8. Deep Researcher (Perplexity-like)

This advanced architecture combines multiple steps and external [[llm_access_to_tools_and_tool_integrations | tool integrations]] to perform comprehensive research <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
Steps include:
*   Analyzing the query <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.
*   Performing web searches (e.g., using Exa) <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>.
*   Consolidating the results <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
*   Creating a synthesized response <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

### 9. Receipt Checker (OCR Integration)

This agent combines an LLM with Optical Character Recognition (OCR) to extract information from images <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. It can utilize external OCR primitives (e.g., from Mistral) to process images, then use a capable LLM (e.g., GPT-4V) to extract and interpret relevant data <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. This demonstrates the power of integrating specialized capabilities that are not native to the LLM itself.

### 10. Image Chatbot (Vision LLM)

A simple agent that leverages a vision-capable LLM (e.g., GPT-4V) to analyze and chat about images provided via a URL <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>. The LLM processes the image and answers questions about its content <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

## Advantages of Primitives over Frameworks

*   **Flexibility & Agility**: In a fast-moving space where new paradigms and LLMs emerge weekly, primitives allow for quick adaptation and migration, unlike frameworks that can lead to being "stuck" with an abstraction layer <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.
*   **Scalability**: Primitives like Amazon S3 are designed for massive scale, offering inherent production readiness <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Reduced Bloat**: Frameworks are often bloated with unnecessary abstractions, whereas primitives provide only the necessary low-level building blocks <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Debugging Ease**: Complex frameworks with obscure abstractions can be hard to debug <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. Primitives, being simpler, make debugging easier.
*   **Direct Control**: Building with primitives means writing plain code, without "magic" or steep learning curves associated with frameworks <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   **Accelerated Development**: For AI engineers, using pre-built, highly scalable, and composable AI primitives significantly improves the speed of building production-ready AI agents <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

By understanding and utilizing these AI primitive patterns, developers can build approximately 80% of the most complex AI agents in existence <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.