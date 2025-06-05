---
title: Different architectures for AI agents
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

Building AI agents effectively relies on understanding various architectural patterns and leveraging AI primitives rather than relying on bloated frameworks <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. Many production-ready AI agents are not built on top of AI frameworks <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>, as frameworks can be slow, bloated, and filled with unnecessary abstractions <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Instead, the focus should be on [[building_ai_agents_without_frameworks | building on top of AI primitives]] <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## The Power of AI Primitives

[[building_and_improving_ai_agents | Building and deploying and scaling AI agent]] remains a significant challenge <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. AI agents represent a new way of writing code, changing how coding projects and SaaS are built <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Primitives have a "native ability of working really really well in production" <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>, similar to how Amazon S3 provides a simple, low-level primitive for object storage that scales massively <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

Instead of frameworks, the approach is to build small, reusable [[components_of_ai_agents | building blocks (primitives)]] that are useful across an entire stack <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

### Key AI Primitives

Several fundamental AI primitives are essential for building robust AI agents:
*   **Memory**: An "autonomous drag engine" <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a> that acts as long-term storage for data, potentially terabytes, and often includes a vector store for search <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. It enables searching through vast amounts of data when using an agent <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>.
*   **Threads**: Used to store and manage the context or history of a conversation <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>, acting like a scratchpad for relevant information <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
*   **Parser**: Extracts context from various file types, such as converting PDFs to text <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **Chunker**: Splits extracted text into smaller pieces of context for similarity search <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.
*   **Tools**: Allow the agent to automatically call external services or APIs <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **Workflow Engine**: Specifically built for multi-step agent tasks <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

[[building_and_improving_ai_agents | Building AI agents]] with these [[components_of_ai_agents | predefined, highly scalable, and composable AI primitives]] can lead to serverless AI agents that automatically handle heavy lifting <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

## Common AI Agent Architectures

Eight different AI agent architectures built purely with AI primitives have been identified <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

### 1. Augmented LLM

This is a common architecture where an agent receives input and generates output using an LLM <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.
It integrates several primitives:
*   **LLM**: The core language model for generation <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
*   **Tools**: To connect to external services or call APIs <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **Threads**: To store conversation history and context <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>.
*   **Memory**: For long-term storage of events or data, enabling searching of terabytes of information <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>.
Almost any type of AI agent can be built using this architecture <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.

### 2. Prompt Chaining and Composition

This architecture involves using multiple agents that work together sequentially <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>. An initial agent creates an output, and based on that output, a decision is made to proceed with another agent <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.
*   **Example**: An agent identifies if an email is spam; if not, another agent drafts a response email <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>. This can involve agents for summarization, feature extraction, or marketing copy generation <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.

### 3. Agent Router / LLM Router

In this pattern, an LLM router agent decides which specialized agent should be called next <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. This involves creating specialized agents for different tasks, each potentially using a different LLM <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.
*   **Example**:
    *   A **Summary Agent** (e.g., using Gemini) for summarizing text <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.
    *   A **Reasoning Agent** (e.g., using DeepSeek LLaMA 70B) for analysis and explanations <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.
    *   A **Coding Agent** (e.g., using Claude Sonnet) for writing code <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>.
The routing agent determines the appropriate agent based on the input task <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>.

### 4. Parallel Agents

This architecture allows a set of agents to run concurrently, typically using simple asynchronous patterns like `Promise.all` in JavaScript <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>.
*   **Example**: Running sentiment analysis, summarization, and decision-making agents in parallel <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.

### 5. Agent Orchestrator Worker

This architecture involves an orchestrator agent that plans and creates subtasks for multiple worker agents <a class="yt-timestamp" data-t="17:13:00">[17:13:00]</a>. The results from these worker agents are then synthesized by another agent <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>. This pattern resembles a deep research agent architecture <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.
*   **Example**: Writing a blog post on remote work benefits (productivity, work-life balance, environmental impact) <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>.
    1.  An orchestrator agent generates subtasks: "write introduction," "write section on productivity," "write section on work-life balance," "write section on environmental impact," and "write conclusion" <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.
    2.  Multiple worker agents are assigned to complete these subtasks <a class="yt-timestamp" data-t="18:44:00">[18:44:00]</a>.
    3.  Finally, the results from all worker agents are synthesized into a single output <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>.

### 6. Evaluator Optimizer

This architecture uses an LLM as a "judge" to evaluate responses generated by another agent <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>. The evaluator can accept the response or reject it with feedback <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>, allowing for iterative refinement.
*   **Example**: Generating an eco-friendly product description <a class="yt-timestamp" data-t="20:48:00">[20:48:00]</a>.
    1.  A generator agent creates a product description.
    2.  An evaluator LLM (chosen for its expertise in the domain) provides specific feedback if the description doesn't meet the criteria (e.g., missing the target audience of "eco-conscious millennials") <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>.
    3.  The generator uses this feedback to produce an improved iteration <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.

### 7. Memory-Based Agents

This is a common pattern where data is uploaded into a memory primitive, and an agent then retrieves and answers questions related to that data <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>.
*   **Example**: "Chat with PDF" <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.
    1.  A memory (with a vector store) is created for storing PDF content <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>.
    2.  PDF files are parsed and chunked into small pieces of context <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
    3.  An AI agent uses this memory to retrieve relevant context and generate answers to user questions <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.

### 8. Complex Agent Architectures

More complex agents can also be built by combining these primitives:
*   **Deep Researcher (Perplexity-like)**: Involves analyzing a query, performing a web search, consolidating results, and then creating a response <a class="yt-timestamp" data-t="22:37:00">[22:37:00]</a>.
*   **Receipt Checker**: Uses OCR (Optical Character Recognition) as a primitive to process images and extract information <a class="yt-timestamp" data-t="23:16:00">[23:16:00]</a>, potentially using multiple OCR models for robustness <a class="yt-timestamp" data-t="23:39:00">[23:39:00]</a>.
*   **Image Chat**: Leverages a vision-capable LLM (e.g., GPT-4o Vision) to analyze an image URL and answer questions about its content <a class="yt-timestamp" data-t="24:18:00">[24:18:00]</a>.

## Conclusion

By understanding and utilizing these [[components_of_ai_agents | AI primitive patterns]], developers can build approximately 80% of the most complex AI agents <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>. The rapidly evolving nature of AI means that new paradigms and LLMs emerge frequently <a class="yt-timestamp" data-t="25:54:00">[25:54:00]</a>, making it crucial to [[building_ai_agents_without_frameworks | build AI agents on top of flexible AI primitives]] rather than being constrained by pre-built, potentially outdated, framework abstractions <a class="yt-timestamp" data-t="25:58:00">[25:58:00]</a>. This approach ensures easier migration and adaptation as agentic workflows and LLM capabilities advance <a class="yt-timestamp" data-t="19:51:00">[19:51:00]</a>.