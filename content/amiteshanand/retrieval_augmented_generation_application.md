---
title: Retrieval augmented generation application
videoId: Cbwq8lUeyLk
---

From: [[amiteshanand]] <br/> 

This article describes the development and functionality of a retrieval augmented generation (RAG) application. The application focuses on the Star Wars universe, allowing users to find planets similar to a specified one and generating corresponding images and descriptions <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Core Technologies

The application is built using a combination of modern web technologies and AI models:
*   **Hono.js**: A lightweight web framework optimized for Edge and Serverless deployments <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. It supports server-side rendering and TypeScript, making it suitable for applications requiring a low bundle size and easy deployment to platforms like Cloudflare Workers, Vercel Edge, Deno, or Bun <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Couchbase**: A powerful, distributed NoSQL database with native support for vector stores and vector search <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. It serves as the main database for storing planet data and their embeddings <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Nebius AI**: A platform providing state-of-the-art open-source models for various AI tasks <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The application utilizes Nebius AI for:
    *   **Text Generation**: Using large language models (LLMs) such as Llama 3.1 (70 billion parameter model) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   **Image Generation**: Using text-to-image models like Flux <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **OpenAI**: Used for generating embeddings from user input queries <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, specifically the `text-embedding-ada-002` model <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Cloudflare**: Used for deploying the Hono.js application, specifically Cloudflare Pages for simplified deployment <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## How the Application Works

The application demonstrates [[leveraging_ai_for_star_wars_data_retrieval_and_image_generation | AI for Star Wars data retrieval and image generation]] through a sophisticated RAG pipeline:

### Data Storage and Embeddings
Approximately 30 documents, each detailing a Star Wars planet (e.g., Alderaan with its rotation period, orbital period, and climate), are stored in Couchbase <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. For each planet, high-dimensional embeddings (1500 dimensions) are pre-generated using OpenAI and stored alongside the planet's details <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. These embeddings represent the real-world features and characteristics of each planet <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Retrieval Augmented Generation Process
1.  **User Query Input**: A user inputs a query, such as "find planets similar to Alderaan" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
2.  **Embedding Generation for Query**: The user's input query is converted into a vector embedding using an OpenAI embedding model <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
3.  **Vector Search (Retrieval)**: Couchbase's vector search capability is then used to find the "nearest vectors" to the query's embedding <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. This process identifies planets whose embeddings are closest to the query's embedding, indicating similar real-world features <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The relevant documents (planet details) are retrieved from the database <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
4.  **Text Generation (Augmentation)**: The retrieved planet data is provided as context to a large language model (LLM) from Nebius AI (specifically, the Llama 3.1 70 billion parameter model) <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. The LLM acts as a "helpful AI assistant" and generates a natural language response describing the similar planets found <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This showcases [[using_deep_learning_models_for_content_generation | using deep learning models for content generation]].
5.  **Image Generation**: In parallel, based on the description and characteristics of the input planet (e.g., Alderaan having mountains and grasslands) <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, a text-to-image model (Flux, offered by Nebius AI Studio) generates an image that visually represents the planet <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. This highlights the [[text_and_image_generation_using_nebius_ai_models | text and image generation capabilities using Nebius AI models]].
6.  **Streaming Response**: The generated text and image are streamed back to the user interface <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Example: Finding Planets Similar to Alderaan
When a user queries "find planets similar to Alderaan" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, the application:
*   Performs a vector search to identify planets like Endor and Yavin 4 that share similar characteristics <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   Generates an image of Alderaan based on its description (e.g., mountains, grasslands, temperate climate) <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Codebase Structure
The Hono.js project's key files include:
*   `server.ts`: Handles the initial Couchbase connection <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   `index.tsx`: Contains the core logic for the RAG pipeline. It manages the connection to Couchbase, performs the vector search (`getRelevantDocuments` function), integrates with OpenAI for embeddings, and uses Nebius AI for text and image generation <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   `client.tsx`: Represents the frontend UI, handling user input, state management, and rendering the chat responses, including text and generated images <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   `wrangler.toml`: The configuration file for deploying the Hono.js project using Cloudflare Workers or Pages <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

This project serves as a comprehensive example of building a full-stack RAG application leveraging modern AI capabilities and serverless deployment strategies <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.