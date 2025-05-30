---
title: Combining lightweight models with reasoning llms
videoId: uWDocIoiaXE
---

From: [[colemedin]] <br/> 

DeepSeek R1, a prominent [[Opensource reasoning LLMs | open-source reasoning LLM]], has been a significant topic in the AI community due to its implications, strengths, and weaknesses <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Beyond its core capabilities, DeepSeek R1 unlocks powerful agentic workflows that deserve more attention <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This article explores a simple yet potent agentic RAG (Retrieval Augmented Generation) setup utilizing R1, focusing on local execution with R1 Distill models and the Small Agents framework from Hugging Face <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## The Agentic RAG Setup

The core idea behind this agentic RAG setup is to leverage the power of [[Reasoning large language models and their impact | reasoning models]] like R1, which are highly capable but can be quite slow <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. To mitigate this, experimenters have combined the raw power of R1 with faster, more lightweight models that direct the overall conversation or agentic flow <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

The setup works by treating the [[Reasoning large language models and their impact | reasoning LLM]] (R1) as a tool accessible to the faster, primary model <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This allows the system to access more reasoning when necessary, at the expense of a slower response <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. For a RAG use case, this means an R1-driven RAG tool can extract in-depth insights from a [[Reasoning with local models and vector databases | knowledge base]] while the rest of the conversation remains nimble <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This approach has yielded significant results even with smaller DeepSeek R1 Distill models <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Workflow Diagram

The high-level conceptualization of this agentic RAG with R1 involves:
*   **Primary LLM (Fast Agent)**: A model like [[Using llama for LLMs | Llama]] or Qwen that is not a [[Reasoning large language models and their impact | reasoning LLM]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. With Small Agents, this primary LLM breaks down problems into steps and includes a loop where it "thinks to itself" <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **RAG Tool**: This entire component acts as a single tool for the primary LLM <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    1.  A user query is passed into the tool <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    2.  Retrieval is performed using RAG and a [[Reasoning with local models and vector databases | vector database]] to pull relevant context <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    3.  This context is fed into the [[Reasoning large language models and their impact | reasoning LLM]] (R1) to extract necessary insights <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    4.  The insights are then returned to the primary agent to continue the conversation <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Implementation Details

### Frameworks and Tools

*   **Small Agents**: A simple agent framework by Hugging Face, used to bootstrap the agentic workflow <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It supports custom tools and agents that execute actions through code <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **[[Using llama for LLMs | Ollama]]**: Used for [[Comparing local and cloudbased large language models | locally]] running DeepSeek R1 and other models <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. [[Using llama for LLMs | Ollama]] is OpenAI API compatible, allowing local models to be served via a local API endpoint <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Hugging Face**: Models can also be installed directly or used via their inference endpoints <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **LangChain**: Used for loading and splitting PDFs for the [[Reasoning with local models and vector databases | knowledge base]] <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **ChromaDB**: Utilized as the local [[Reasoning with local models and vector databases | vector database]] for storing and retrieving information <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Gradio UI**: Integrated with Small Agents to provide a simple user interface <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

### Model Selection and Configuration

*   **DeepSeek R1 Models**: The massive 671 billion parameter version is not feasible for personal hardware <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Smaller, more realistic versions, such as the 7 billion parameter R1 Distill models, are used for [[Comparing local and cloudbased large language models | local]] execution <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>, <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. DeepSeek fine-tuned competitor models like Qwen and [[Using llama for LLMs | Llama]] using data produced by DeepSeek R1 to create these smaller [[Reasoning large language models and their impact | reasoning LLMs]] <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **[[Using llama for LLMs | Ollama]] Context Limit**: By default, [[Using llama for LLMs | Ollama]] models have a limited context window (e.g., 2048 tokens), which is often insufficient <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. Instructions are provided to increase this limit to larger values, such as 8196 or even 32000 tokens, by creating custom `Modelfile` configurations <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>, <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This prevents hallucinations that can occur with smaller context windows <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Primary LLM**: A non-[[Reasoning large language models and their impact | reasoning LLM]] like Qwen 2.5 7B Instruct is used as the primary conversation driver <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

### Building the Agent

The process involves setting up both the [[Reasoning large language models and their impact | reasoning model]] (R1) and the RAG tool:
1.  **Reasoning Model Setup**: An instance of a Small Agents `CodeAgent` is created for R1. It is configured with `max_steps` (e.g., 2 steps) to limit its internal reasoning loop and prevent hallucination <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
2.  **Embedding Model**: A local embedding model from Hugging Face is used to embed user queries and match them against the [[Reasoning with local models and vector databases | vector database]] <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
3.  **RAG Tool Definition**:
    *   A custom tool, `rag_with_reasoner`, is defined using Small Agents' `@tool` decorator <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
    *   This tool performs a similarity search in the [[Reasoning with local models and vector databases | vector database]] to retrieve relevant chunks of information (e.g., top three) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
    *   The retrieved context and the user's question are formatted into a prompt and fed into the [[Reasoning large language models and their impact | reasoning LLM]] (R1) <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
    *   R1 is instructed to extract insights and, importantly, can return a *better query* to the primary LLM if insufficient information is found, allowing the primary LLM to retry the RAG loop <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This demonstrates the "agentic" nature of the RAG <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
4.  **Primary Agent Setup**: The primary LLM is set up as a `ToolCallingAgent` that uses the `rag_with_reasoner` tool <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

The entire workflow, including the UI, can be set up with minimal lines of code due to the integration of Small Agents with Gradio UI <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>, <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

## Advantages and Future Scope

This approach of combining a faster primary LLM with a powerful [[Reasoning large language models and their impact | reasoning LLM]] like R1 in an agentic workflow is highly effective <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>. It allows for in-depth analysis from the [[Reasoning with local models and vector databases | knowledge base]] while maintaining conversational speed.

> <p class="yt-timestamp" data-t="00:21:17">[00:21:17]</p>
> <p class="yt-timestamp" data-t="00:21:20">[00:21:20]</p>
> It's very much agentic rag where it reasons with itself and it's also agentic rag just because we're using entirely separate llm to handle the rag results as well.

While Small Agents simplifies the initial setup, there are plans for more robust implementations using frameworks like Pydantic AI and LangGraph, which can handle more complex agentic flows and address some quirks observed with Small Agents <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>, <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>, <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>. This showcases the immense potential for [[Strategies for scaling AI with local LLMs | scaling AI with local LLMs]] by orchestrating different models for specific tasks.