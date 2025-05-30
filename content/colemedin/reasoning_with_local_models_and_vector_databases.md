---
title: Reasoning with local models and vector databases
videoId: uWDocIoiaXE
---

From: [[colemedin]] <br/> 

DeepSeek R1, a powerful open-source reasoning large language model (LLM), has demonstrated significant capabilities, particularly in unlocking agentic workflows <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores a powerful agentic Retrieval Augmented Generation (RAG) setup that leverages DeepSeek R1 and other [[working_with_local_large_language_models|local large language models]], combined with a local [[creating_and_utilizing_a_vector_database_for_RAG|vector database]], to create a nimble and insightful AI system <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Combining Lightweight and Reasoning Models

Reasoning models like DeepSeek R1 are potent but often slow <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. To address this, a common strategy is to combine the raw power of these models with faster, more [[combining_lightweight_models_with_reasoning_llms|lightweight models]] that direct the overall conversation or agentic flow <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This approach treats the reasoning model as a "tool" accessible when deeper reasoning is required, accepting a slower response in those instances <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

For RAG applications, this means an R1-driven RAG tool can extract in-depth insights from a knowledge base, while the primary conversation remains nimble <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This setup has shown incredible results even with smaller distill versions of R1 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Agentic RAG Architecture

The core of this agentic RAG setup involves a primary LLM (referred to as a "fast agent") and a specialized RAG tool that incorporates the reasoning LLM <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Workflow Overview
1.  **Primary LLM (Fast Agent)**: This model (e.g., Llama or Qwen) drives the main conversation <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a> <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. When using frameworks like Small Agents, it breaks down problems into steps and can enter a feedback loop for better query refinement <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a> <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
2.  **RAG Tool**: When the primary LLM determines that knowledge lookup is necessary, it calls this tool <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   **Retrieval**: The tool first performs a retrieval operation using a [[choosing_vector_databases_for_rag_applications|vector database]] to pull relevant context based on the user query <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    *   **Reasoning LLM (R1)**: The retrieved context is then fed into DeepSeek R1, which extracts necessary insights from the context <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   **Feedback Loop**: R1 can return the extracted insights to the primary agent to continue the conversation <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Crucially, if R1 determines the information is insufficient, it can suggest a better query back to the primary LLM, enabling the system to try again with a refined search <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This makes it a truly agentic RAG setup <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

### Key Technologies

*   **Small Agents (Hugging Face)**: A simple agent framework used for building and managing the agentic workflow <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It provides functionality for agents, tools, and even a UI <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **[[incorporating_ai_models_and_databases_in_a_local_setup|Ollama]]**: Used for running DeepSeek R1 and other LLMs locally <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Hugging Face Inference Endpoints**: An alternative for accessing models, particularly for those with API restrictions or better rate limits <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a> <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **ChromaDB**: Utilized as the local [[creating_and_utilizing_a_vector_database_for_RAG|vector database]] for storing and retrieving knowledge <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **LangChain**: Used for loading and splitting PDF documents into manageable chunks for the knowledge base <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **Gradio UI**: Integrates directly with Small Agents to provide a simple user interface for interaction <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

## Implementation Details

### Setting Up Local Models with [[incorporating_ai_models_and_databases_in a_local_setup|Ollama]]

To run models like DeepSeek R1 and Qwen locally, [[using_local_large_language_models_with_autod_dev|Ollama]] is used. [[incorporating_ai_models_and_databases_in_a_local_setup|Ollama]] offers various versions of DeepSeek R1, including smaller distill models (e.g., 7 billion parameter version) that are realistic to run on personal hardware <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a> <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

A critical tip for using [[incorporating_ai_models_and_databases_in_a_local_setup|Ollama]] models is to increase their default context limit from 2,048 tokens <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. This is done by creating a custom model file within the [[incorporating_ai_models_and_databases_in_a_local_setup|Ollama]] models folder, specifying a larger context (e.g., 8,096 tokens or even 32,000 tokens for larger LLMs) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a> <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. This significantly reduces hallucinations and improves performance in most use cases <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a> <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

### Constructing the RAG Tool (`rag_with_reasoner`)

The RAG tool is defined using Small Agents' `tool` decorator <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
1.  **Embedding Model**: An embedding model (e.g., `all-MiniLM-L6-v2`) is loaded locally to embed user queries and match them against the [[creating_and_utilizing_a_vector_database_for_RAG|vector database]] <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a> <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
2.  **Vector Database Interaction**: The tool performs a similarity search in the [[creating_and_utilizing_a_vector_database_for_RAG|vector database]] (ChromaDB) to retrieve the top three relevant chunks of information <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
3.  **Reasoning with R1**: The retrieved context is formatted into a prompt and fed into the DeepSeek R1 reasoning model. R1's task is to extract necessary insights from the context and user's question <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. R1 is configured to have a limited number of "self-reasoning" steps (e.g., `max_steps=2`) to prevent hallucination <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a> <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
4.  **Returning Results**: The response from R1, containing the insights, is returned to the primary LLM <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

### Knowledge Base Setup

A local knowledge base is set up using ChromaDB <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. The setup script leverages LangChain to:
*   Load PDF documents from a specified data directory <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   Split the documents into chunks <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   Create embeddings for all chunks using the same embedding model as the RAG tool <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
*   Insert these embeddings into the ChromaDB database <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

```python
# Example command to ingest PDFs
python ingest_pdfs.py <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>
```

## Benefits and Future Directions

This setup demonstrates a powerful form of "agentic RAG," where models reason with themselves and collaborate effectively <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. The ability for the reasoning LLM (R1) to not only extract insights but also suggest better queries to the primary LLM adds a significant layer of intelligence beyond simple one-shot RAG <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

While the current example uses a simplified framework (Small Agents) for introduction, future implementations aim for more robust solutions using frameworks like Pydantic AI and LangGraph, further expanding the capabilities of [[integrating_knowledge_graphs_with_vector_databases_for_AI_solutions|integrating knowledge graphs with vector databases for AI solutions]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. The concept of combining a powerful reasoning model like DeepSeek R1 or O3 mini with faster LLMs in a workflow is highly adaptable and promising for many advanced AI agent applications <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a> <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.