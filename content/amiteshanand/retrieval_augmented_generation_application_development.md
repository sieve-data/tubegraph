---
title: Retrieval Augmented Generation application development
videoId: Cbwq8lUeyLk
---

From: [[amiteshanand]] <br/> 

This article explores the development of a Retrieval Augmented Generation (RAG) application, specifically focusing on building a Star Wars-themed planet search tool. The application leverages a combination of modern web frameworks, NoSQL databases with vector search capabilities, and advanced AI models for both text and image generation <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Core Technologies Utilized

The application is built using a stack of key technologies:

*   **Hono.js**: A lightweight web framework optimized for Edge and Serverless deployments <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   **Couchbase**: A powerful NoSQL distributed database with integrated support for Vector store and Vector search <a class="yt-timestamp" data-t="01:23">[01:23]</a>.
*   **Nebius AI**: Provides state-of-the-art open-source models for text generation (e.g., Llama 3.1) and text-to-image generation (e.g., Flux) <a class="yt-timestamp" data-t="03:32">[03:32]</a>, <a class="yt-timestamp" data-t="07:08">[07:08]</a>, <a class="yt-timestamp" data-t="09:18">[09:18]</a>.
*   **OpenAI**: Used for generating embeddings for the input queries <a class="yt-timestamp" data-t="05:04">[05:04]</a>.
*   **Cloudflare**: Utilized for deploying the application via Cloudflare Workers or Pages <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, <a class="yt-timestamp" data-t="08:29">[08:29]</a>.

## Application Functionality

The application is designed to help users find planets in the Star Wars universe similar to a specific planet they search for <a class="yt-timestamp" data-t="01:03">[01:03]</a>.

### Workflow:

1.  **User Query**: The user inputs a query, such as "find planets similar to Alderaan" <a class="yt-timestamp" data-t="02:41">[02:41]</a>.
2.  **Embedding Generation**: The input query is converted into an embedding using an OpenAI embedding model (specifically, `text-embedding-ada-002`) <a class="yt-timestamp" data-t="05:01">[05:01]</a>, <a class="yt-timestamp" data-t="05:15">[05:15]</a>.
3.  **Vector Search**: Couchbase, acting as the vector store, performs a vector search to find planets whose embeddings are closest to the input query's embedding <a class="yt-timestamp" data-t="01:17">[01:17]</a>, <a class="yt-timestamp" data-t="05:22">[05:22]</a>. The database already contains around 30 documents, each detailing a planet and its pre-generated 1500-dimension embeddings (also generated via OpenAI) <a class="yt-timestamp" data-t="01:28">[01:28]</a>, <a class="yt-timestamp" data-t="01:43">[01:43]</a>, <a class="yt-timestamp" data-t="05:36">[05:36]</a>.
4.  **Text Generation (RAG)**: The relevant planet details retrieved from Couchbase are fed as context into a text-based LLM model from Nebius AI (e.g., Llama 3.1 70B parameter model) <a class="yt-timestamp" data-t="06:51">[06:51]</a>, <a class="yt-timestamp" data-t="07:09">[07:09]</a>. This AI model then generates a response detailing the similar planets <a class="yt-timestamp" data-t="02:53">[02:53]</a>.
5.  **Image Generation**: Based on the description of the requested planet (e.g., Alderaan's characteristics like mountains, grasslands, temperate climate), a text-to-image generation model (Flux by Nebius AI) creates an image of how the planet might look <a class="yt-timestamp" data-t="02:23">[02:23]</a>, <a class="yt-timestamp" data-t="03:15">[03:15]</a>, <a class="yt-timestamp" data-t="07:18">[07:18]</a>. This demonstrates [[integrating_ai_tools_for_content_and_image_generation | integrating AI tools for content and image generation]] within the application.
6.  **Streaming Response**: The generated text and image are streamed back to the user interface <a class="yt-timestamp" data-t="07:30">[07:30]</a>.

For example, a query for "Alderaan" might return similar planets like Endor and Yavin 4, along with their details and a generated image of Alderaan <a class="yt-timestamp" data-t="03:06">[03:06]</a>.

## Technical Implementation Overview

The project structure involves several key files:

*   **`server.ts`**: This TypeScript file handles the initiation of the Couchbase connection, requiring connection string, username, and password <a class="yt-timestamp" data-t="04:17">[04:17]</a>.
*   **`index.tsx`**: This is the core logic file for the Hono.js application <a class="yt-timestamp" data-t="04:36">[04:36]</a>.
    *   It initializes the Hono app and connects to the Couchbase cluster <a class="yt-timestamp" data-t="04:39">[04:39]</a>.
    *   The `getRelevantDocuments` function performs the vector search, converting the user's input query into an embedding using OpenAI, and then querying Couchbase for the nearest vectors (similar planets) <a class="yt-timestamp" data-t="04:51">[04:51]</a>, <a class="yt-timestamp" data-t="05:22">[05:22]</a>.
    *   The API endpoint (`/api/chat`) handles the main RAG process: it takes the input query, converts it to an embedding, retrieves relevant documents, constructs a prompt (e.g., "You're a helpful AI assistant"), and uses Nebius AI (Llama 3.1) for text completion <a class="yt-timestamp" data-t="06:23">[06:23]</a>.
    *   For image generation, a prompt (e.g., "a beautiful detailed illustration of that particular planet") is sent to Nebius AI's Flux model <a class="yt-timestamp" data-t="07:19">[07:19]</a>.
    *   The response is streamed using a readable stream <a class="yt-timestamp" data-t="07:30">[07:30]</a>.
*   **`client.tsx`**: This file contains the frontend UI, handling state management for loading values and rendering the streamed text and image responses from the API <a class="yt-timestamp" data-t="07:41">[07:41]</a>. The UI is themed around Star Wars <a class="yt-timestamp" data-t="07:43">[07:43]</a>.
*   **`wrangler.toml`**: This configuration file is used for deploying the project with Cloudflare Workers, allowing specification of additional Cloudflare features like KV storage, R2 buckets, or D1 database if used <a class="yt-timestamp" data-t="08:31">[08:31]</a>.

## Advantages of Chosen Technologies

*   **Hono.js**: Offers a very low bundle size, support for server-side rendering, and TypeScript out-of-the-box <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It allows the use of Node.js-based npm modules (like Couchbase) without needing a dedicated Node.js server, similar to the server-like experience provided by Next.js <a class="yt-timestamp" data-t="00:40">[00:40]</a>.
*   **Couchbase**: A powerful, distributed NoSQL database that natively supports Vector store and Vector search, making it ideal for similarity searches based on embeddings <a class="yt-timestamp" data-t="01:23">[01:23]</a>, <a class="yt-timestamp" data-t="01:59">[01:59]</a>.
*   **Nebius AI**: Provides access to a range of state-of-the-art open-source models, including those for text generation, text-to-image, vision, and embeddings, complete with a playground for testing and SDKs for integration <a class="yt-timestamp" data-t="03:38">[03:38]</a>.
*   **Cloudflare**: Facilitates easy deployment of Hono.js projects to Cloudflare Workers or Pages <a class="yt-timestamp" data-t="09:00">[09:00]</a>.