---
title: Monitoring tracing and evaluation in RAG systems
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

Monitoring, tracing, and evaluation are crucial aspects for ensuring the performance and reliability of Retrieval Augmented Generation (RAG) solutions, especially when deployed in production environments <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

## Monitoring and Tracing

Monitoring and tracing RAG solutions helps in troubleshooting and understanding the system's behavior <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. It allows users to identify where the majority of time is spent within the pipeline, such as in the large language model or other components <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

### Tools for Monitoring and Tracing
*   **Prototyping**: For prototyping, [[openrag_eval_project_overview | Langsmith Phoenix]] is a suitable solution <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Production**: In production, Arise Phoenix is often used, especially because it can be easily deployed in a Docker container <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. These tools allow for tracking and troubleshooting the RAG pipeline <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>.

## Evaluation

Evaluating the RAG solution is essential to assess its quality and effectiveness <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. While a single question might be used for initial testing, a comprehensive [[metrics_for_evaluating_rag_systems | RAG evaluation]] framework is needed to test across a much larger set of documents and queries <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>.

### Frameworks for Evaluation
*   **Ragas**: Ragas is highlighted as an excellent framework for [[metrics_for_evaluating_rag_systems | RAG evaluation]] <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. It helps check the quality of RAG solutions in various ways and integrates well with large language models, making the evaluation task relatively straightforward <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>.

## Components in a Production Docker Environment
A typical production environment leveraging Docker Compose would include specific Docker images for different RAG components, facilitating monitoring and evaluation:
*   **Data Ingestion**: An image for ingesting data, connected to the knowledge base to pull in HTML files <a class="yt-timestamp" data-t="17:57:00">[17:57:00]</a>.
*   **Vector Database**: An image for Quadrant, serving as the vector database, which can be pulled from Docker Hub <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.
*   **Front-end Application**: A front-end application for the solution <a class="yt-timestamp" data-t="18:09:00">[18:12:00]</a>.
*   **Model Serving**: Olama or Hugging Face's text generation inference engine to serve models <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.
*   **Tracing**: Phoenix for tracing <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>.
*   **Evaluation**: Ragas for evaluating models <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

These images can be run as containers within Docker Compose, with configurations for embedding, reranking, and large language models <a class="yt-timestamp" data-t="18:26:00">[18:26:00]</a>.