---
title: Vector search and embeddings with OpenAI
videoId: Cbwq8lUeyLk
---

From: [[amiteshanand]] <br/> 

This article details the construction of a retrieval augmented generation (RAG) application leveraging [[leveraging_ai_for_star_wars_data_retrieval_and_image_generation | Hono.js]], Couchbase, Nebulas AI, and Cloudflare. The application's core functionality revolves around vector search and embeddings, specifically utilizing OpenAI for embedding generation <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Application Overview

The application is designed to find planets within the Star Wars universe that are similar to a user-specified planet <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It functions as a retrieval augmented generation (RAG) system, where an AI model provides responses based on retrieved information <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Key Technologies
*   **Hono.js**: A lightweight web framework optimized for Edge and Serverless deployments, supporting server-side rendering and TypeScript <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   **Couchbase**: A powerful NoSQL distributed database with integrated support for vector stores and vector search <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **OpenAI**: Used for generating embeddings from text data <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Nebulas AI Studio**: Provides state-of-the-art open-source models for text generation (e.g., Llama 3.1 70B parameter model) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, and text-to-image generation (e.g., Flux model) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. It offers various models including [[using_deepseek_v3_and_r1_models | DeepSeek V3 and R1]] for text, and Flux for images, along with vision and embedding models <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Data Storage and Embeddings
The application uses Couchbase as its primary database, storing approximately 30 documents, each detailing a Star Wars planet with properties like rotation period, orbital period, and crucial embeddings <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These embeddings, which are of 1500 dimensions, are generated using OpenAI <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. They represent the real-world functionalities or features of a particular planet <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Vector Search with OpenAI Embeddings

The core mechanism for finding similar planets relies on vector search.
1.  **Query Embedding**: When a user inputs a query (e.g., "find planets similar to Alderaan"), the input query is first converted into an embedding using the OpenAI `text-embedding-ada-002` model <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
2.  **Nearest Vector Search**: This generated query embedding is then used with Couchbase's vector search functionality to find the nearest vectors among the stored planet embeddings <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. The principle is that if two embeddings are close to each other, their corresponding real-world features are also similar <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
3.  **Retrieval**: The system finds the set of closest planet documents, which are then used as context for the AI model <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

For instance, searching for planets similar to Alderaan yields results like Endor and Yavin 4, along with their details <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Text and Image Generation
After retrieving relevant planet data via vector search:
*   **Text Generation**: A text-based Large Language Model (LLM) from Nebulas AI Studio (specifically the Llama 3.1 70 billion parameter model) is used to generate a response, acting as a helpful AI assistant that summarizes the similar planets based on the provided context <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Image Generation**: A text-to-image generation model, the Flux CXL model, also powered by Nebulas AI, creates an image of the queried planet (e.g., Alderaan) based on its description, capturing visual elements like mountains, grasslands, and temperate climate <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Codebase Structure
The project's key files include:
*   `server.TS`: Initializes the Couchbase connection <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   `index.DSX`: Contains the core logic for the Hono app, including:
    *   Connecting to the Couchbase cluster <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   `getRelevantDocuments` function: Performs the vector search. It converts the user's input query into an embedding using OpenAI's `text-embedding-ada-002` model and then queries Couchbase's vector search index to find the nearest relevant documents (planets) <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   API endpoint (`/api/chat`): Orchestrates the query embedding, text generation (using Llama 3.1), and image generation (using Flux CXL) <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   `client.PSX`: Handles the front-end UI, manages state, sends user messages to the API, and renders the streamed text and image responses <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

## Deployment
The application is deployed using Cloudflare Pages, leveraging the `wrangler.toml` file for project configuration, which is essential for deploying Hono projects with Cloudflare Workers <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.