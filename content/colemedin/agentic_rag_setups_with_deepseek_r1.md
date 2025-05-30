---
title: Agentic rag setups with DeepSeek R1
videoId: uWDocIoiaXE
---

From: [[colemedin]] <br/> 

[[DeepSeek R1 model features | DeepSeek R1]], an open-source reasoning large language model (LLM), has garnered significant attention for its implications and capabilities <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Beyond its general strengths and weaknesses, [[DeepSeek R1 model features | R1]] uniquely enables powerful [[agentic_rag_setup | agentic workflows]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This article details a simple yet potent [[agentic_rag_setup | agentic RAG setup]] utilizing [[DeepSeek R1 model features | R1]] locally with distilled models and the Small Agents framework from Hugging Face <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Core Concept: Combining Reasoning Power with Speed

The [[agentic_rag_setup | agentic RAG setup]] leverages the fact that reasoning models like [[DeepSeek R1 model features | R1]] are powerful but often slow <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The strategy involves combining the raw power of [[DeepSeek R1 model features | R1]] with faster, more lightweight models that direct the overall conversation or [[Agentic RAG strategy and implementation | agentic flow]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. In this architecture, [[DeepSeek R1 model features | R1]] acts as a specialized tool for the primary LLM <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

This means a primary, faster LLM can maintain a nimble conversation, while an [[DeepSeek R1 model features | R1]]-driven RAG tool is invoked when in-depth insights are required from a knowledge base <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This approach has yielded impressive results, even with the smaller distilled [[DeepSeek R1 model features | R1]] models <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Architectural Overview

The [[agentic_rag_setup | agentic RAG system]] is conceptualized with two main components <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  **Primary LLM (Fast Agent):** This is a non-reasoning LLM, such as Llama or Qwen, responsible for driving the overall conversation <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. When using Small Agents, this LLM breaks down problems into steps and can enter a feedback loop <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
2.  **RAG Tool:** This is a single, specialized tool for the primary LLM <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. When the primary LLM determines it needs external knowledge, it calls this tool <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   **Retrieval:** The tool first takes the user query and performs a retrieval operation against a vector database to pull relevant context <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   **Reasoning:** The retrieved context is then fed into the reasoning LLM ([[DeepSeek R1 model features | R1]]) to extract necessary insights <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   **Response:** The insights from [[DeepSeek R1 model features | R1]] are returned to the primary agent to continue the conversation <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

This dual-LLM approach allows for a highly nimble conversation while providing access to deep reasoning when required, albeit with a slower response time for the reasoning portion <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Implementation Details

### Frameworks and Tools

*   **Small Agents:** A simple agent framework by Hugging Face used to bootstrap the [[agentic_rag_setup | agentic workflow]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It provides mechanisms for agents to break down problems and utilize tools <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Ollama:** Used for running [[DeepSeek R1 model features | R1]] and other LLMs (like Qwen Instruct) locally <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This allows for entirely local operation <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Hugging Face Inference API:** An alternative for models if not running entirely locally <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **ChromaDB:** A local vector database for managing the knowledge base <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **LangChain:** Used for loading and chunking PDF documents into the vector database <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **Gradio UI:** Integrated directly with Small Agents, providing a quick user interface for interaction <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

### Model Selection and Configuration

The setup uses distilled versions of [[DeepSeek R1 model features | R1]], which are fine-tuned versions of competitors like Qwen and Llama based on data produced from the full [[DeepSeek R1 model features | R1]] model <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. For local deployment, the 7 billion parameter version of [[DeepSeek R1 model features | R1]] Distill and the 7 billion parameter version of Qwen Instruct are recommended <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

A crucial tip for Ollama models is to increase their default context limit (from 2,048 tokens) to a more suitable size, such as 8,196 tokens, by creating custom Ollama model files <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. This prevents hallucinations that can occur with smaller context windows <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

### Building the [[Agentic RAG AI agent template | AI Agent]]

1.  **Import Libraries and Load Environment Variables:** Key classes from Small Agents are imported, and environment variables for model IDs (reasoning and tool models) and Hugging Face API tokens (optional) are loaded <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
2.  **Model Loading Function:** A utility function (`get_model`) is defined to load models either via the Hugging Face API or locally via Ollama's OpenAI API compatibility layer <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
3.  **Reasoning Agent Setup:** The [[DeepSeek R1 model features | R1]] instance is set up as a `CodeAgent` in Small Agents <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. This agent is configured without external tools and with a `max_steps` limit (e.g., 2 steps) to prevent it from looping and hallucinating <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
4.  **RAG Tool Definition (`rag_with_reasoner`):**
    *   An embedding model (e.g., local Hugging Face embedding model) is used to embed user queries <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
    *   The tool performs a similarity search in the ChromaDB vector database, returning the top relevant chunks <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
    *   A prompt, including the retrieved context and user question, is formatted and fed into the [[DeepSeek R1 model features | R1]] reasoning agent <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
    *   The tool includes logic for [[Agentic RAG strategy and implementation | R1]] to return a "better query" if insufficient information is found, allowing the primary LLM to refine its search and re-engage the RAG tool in a loop <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
    *   The [[DeepSeek R1 model features | R1]] agent is called with `model.run(prompt, reset=False)` to maintain conversation history <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
5.  **Primary Agent Setup:** The main conversational LLM is set up as a `ToolCallingAgent` <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. Its primary tool is the `rag_with_reasoner` function <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
6.  **User Interface:** A Gradio UI is quickly created and launched with a single line of code, automatically maintaining conversation history <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### Knowledge Base Setup

A local knowledge base is set up using ChromaDB. A script is provided to clear the database and re-ingest PDF documents (e.g., fake competitor analysis data) from a `data` directory <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. This ensures a clean slate each time, avoiding duplicate data <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. LangChain handles the PDF loading and text splitting <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## Demonstration

Upon running the setup, the Gradio UI appears, showing the conversational flow <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. When a complex query (e.g., comparing company services) is posed, the primary agent decides to use the `rag_with_reasoner` tool <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>. The relevant context is fetched from the vector database and passed to [[DeepSeek R1 model features | R1]] for detailed reasoning <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

The UI provides visibility into the steps taken by the agents, including function calls and execution logs <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. The [[Agentic RAG strategy and implementation | agentic RAG]] system demonstrates its capability by providing comprehensive answers and, if necessary, allowing [[DeepSeek R1 model features | R1]] to instruct the primary agent to refine its query for a better search <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

## [[Agentic RAG advantages and future applications | Future Directions]]

This simple [[agentic_rag_setup | agentic RAG setup]] serves as an introduction to [[enhancing_ai_agents_with_rag_technology | enhancing AI agents with RAG technology]] and highlights the power of combining reasoning LLMs like [[DeepSeek R1 model features | R1]] with faster models in complex workflows <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. Future work includes expanding this setup into a more robust [[rag_ai_agent_development | RAG AI agent development]] with Pydantic AI and LangGraph, offering even more sophisticated [[advanced_rag_implementation_techniques | advanced RAG implementation techniques]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>.