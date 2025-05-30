---
title: Using llama for LLMs
videoId: V_0dNE-H2gw
---

From: [[colemedin]] <br/> 

This article focuses on the integration and use of [[opensource_reasoning_LLMs | Ollama]] within a self-hosted AI starter kit developed by the n8n team. This package provides a comprehensive solution for local AI infrastructure, leveraging open-source models like [[metas_llama_32_language_models | Llama]] that are increasingly powerful enough to compete with closed-source alternatives such as GPT and Claude <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Components of the Self-Hosted AI Starter Kit

The self-hosted AI starter kit bundles several key technologies into a single package for local AI:
*   [[opensource_reasoning_LLMs | Ollama]] for LLMs <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   Qdrant for the vector database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   PostgreSQL for the SQL database <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   n8n for workflow automations, tying everything together <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

These components are brought together using Docker Compose <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Setting Up [[opensource_reasoning_LLMs | Ollama]]

To utilize [[opensource_reasoning_LLMs | Ollama]] effectively within this self-hosted environment, some initial setup and configuration are required:

### Dependencies
Before starting, ensure you have Git and Docker installed. Docker Desktop is recommended as it includes Docker Compose <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Configuration in Docker Compose
The `docker-compose.yaml` file is central to configuring the services. For [[opensource_reasoning_LLMs | Ollama]], specific additions are recommended:
*   **Pulling [[metas_llama_32_language_models | Llama 3.1]]**: By default, the `ollama` container pulls [[metas_llama_32_language_models | Llama 3.1]] (specifically the 8 billion parameter model) upon initialization <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Pulling an Embedding Model**: To enable [[use_of_web_scraping_with_llms | Ollama]] for embeddings with the vector database, an additional line must be added to the `docker-compose.yaml` file to pull an [[opensource_reasoning_LLMs | Ollama]] embedding model <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Port Exposure**: The default port for [[opensource_reasoning_LLMs | Ollama]] is `11434` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

### Starting the Services
Once configured, the services are started using a `docker compose` command, which can be adapted for different architectures (Nvidia GPU, Mac, or CPU) <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The initial startup will involve pulling [[opensource_reasoning_LLMs | Ollama]] and other images, which may take some time <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Using [[opensource_reasoning_LLMs | Ollama]] within n8n for a RAG Agent

The local infrastructure, including [[opensource_reasoning_LLMs | Ollama]], can be used to [[creating_applications_with_local_llms_in_autod_dev | create a fully local RAG (Retrieval Augmented Generation) AI agent within n8n]] <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Configuring the AI Agent
Within n8n, the AI agent node integrates [[opensource_reasoning_LLMs | Ollama]] for both the LLM and embedding model:
*   **[[opensource_reasoning_LLMs | Ollama]] Chat Model**: Reference [[metas_llama_32_language_models | `llama 3.1:latest`]] for the chat model <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Users can pull and use any [[opensource_reasoning_LLMs | Ollama]] LLM <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Credentials**: The base URL for [[opensource_reasoning_LLMs | Ollama]] is `http://host.docker.internal:11434`. It's crucial to use `host.docker.internal` instead of `localhost` when containers need to communicate with each other <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Embeddings**: [[opensource_reasoning_LLMs | Ollama]] is also used for embeddings to work with the Qdrant vector store <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Response Parsing**: [[metas_llama_32_language_models | Llama 3.1]] is also used to parse responses from RAG lookups <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

### Performance Considerations
When running [[metas_llama_32_language_models | Llama 3.1]] locally, especially on less powerful machines, responses might take some time <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. To mitigate this, consider using smaller chunk sizes for documents in the RAG pipeline to keep context shorter and reduce prompt size, thereby improving [[speed_and_performance_comparison_with_other_llms | speed and performance]] <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

## Future Expansions

The current setup serves as a strong starting point for local AI. Future expansions could include:
*   Adding Redis for caching <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   Integrating a self-hosted Supabase for authentication capabilities <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
*   Developing a complete local AI tech stack that includes a front end <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   Baking in best practices for RAG and LLMs into n8n workflows to create more accessible templates for local AI development <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.