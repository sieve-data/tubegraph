---
title: Prototyping and production environments in AI solutions
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

Developing and deploying AI solutions, particularly those involving Retrieval Augmented Generation (RAG) stacks, typically involves distinct phases for [[prototyping_and_idea_discovery_with_ai | prototyping]] and production <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Each phase utilizes different tools and strategies to meet its specific requirements.

## Prototyping Environment

The [[prototyping_and_idea_discovery_with_ai | prototyping]] phase focuses on rapid iteration and experimentation to validate concepts and build initial models <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Key Characteristics & Tools
*   **Platform:** Google Colab is a preferred environment for [[prototyping_and_idea_discovery_with_ai | prototyping]] due to its accessibility and provision of a free hardware accelerator <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Orchestration:** Llama Index or Lang Graph are suitable for orchestrating the RAG pipeline in the [[prototyping_and_idea_discovery_with_ai | prototyping]] stage <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Embedding Models:** Both closed models (via APIs for simplicity) and open models (e.g., from Nvidia or BAI) can be used <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The BGE small model from B AI is an example of an open embedding model that can be downloaded and used <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. OpenAI's text embedding ADA 002 or text embedding three large are default built-in options in some systems <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Vector Database:** Qdrant is a suitable choice, even as an in-memory solution for [[prototyping_and_idea_discovery_with_ai | prototyping]], given its scalability <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Large Language Models (LLMs):** Closed models are often used for their API simplicity, such as GPT-3.5 Turbo (default) or GPT-4 from OpenAI <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. Open models like those from Meta or Qwen 3 are also options <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Monitoring and Tracing:** Solutions like Langsmith or Phoenix Arise help track the performance of different components and aid troubleshooting <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
*   **Re-ranking:** Closed models, such as the one from Cohere, are used for re-ranking to improve accuracy after retrieval <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.
*   **Evaluation:** The Ragas framework is used to evaluate the quality of RAG solutions, supporting testing across many documents <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>, <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

## Production Environment

The production phase focuses on deploying robust, scalable, and secure AI solutions. [[role_of_engineering_teams_in_ai_agent_production | Engineering teams]] ensure that the solutions meet operational requirements.

### Key Characteristics & Tools
*   **Deployment:** Docker is a common solution for deployment, allowing for both on-premise and cloud environments <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This is particularly important for organizations like financial institutions that may have requirements for on-premise data processing <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Orchestration:** Llama Index is a suitable choice for orchestrating RAG pipelines in production <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Embedding Models:** Open models, such as those from BAI and Nvidia, are favored for production environments <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   **Vector Database:** Qdrant is recommended due to its ability to scale from a few documents to hundreds of thousands, making it suitable for production workloads <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
*   **Large Language Models (LLMs):** Open models like Llama 3.2 or Qwen 3.4 billion from Alibaba Cloud are often used and served within a Docker environment via Olama or Hugging Face Text Generation Inference <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Monitoring and Tracing:** Phoenix Arise is a robust solution for monitoring and tracing in production, with a Docker solution readily available <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Re-ranking:** Open solutions, such as those from Nvidia, are preferred in production for re-ranking to enhance accuracy <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Evaluation:** The Ragas framework remains crucial for checking the quality of RAG solutions across various metrics in a production context <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

### Docker Compose Configuration for Production

A typical production setup using Docker Compose involves a `compose.yaml` file to manage various services as containers <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. This allows for modular deployment of the RAG stack:

*   **Data Ingestion Image:** Connects to the knowledge base to pull in HTML files <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.
*   **Qdrant Image:** For the vector database, often pulled from Docker Hub <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   **Front-end Application Image:** For the user interface <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   **LLM Serving Image:** Uses Olama or Hugging Face Text Generation Inference to serve models <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.
*   **Phoenix Image:** For tracing and monitoring <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>.
*   **Ragas Image:** For evaluating model quality <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Model Details:** Configuration for embedding, re-ranking, and large language models <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

This structured approach helps in building and shipping production-ready generative AI solutions efficiently <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.