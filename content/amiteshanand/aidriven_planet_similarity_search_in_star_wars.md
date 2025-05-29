---
title: AIdriven planet similarity search in Star Wars
videoId: Cbwq8lUeyLk
---

From: [[amiteshanand]] <br/> 

This article details the development of a retrieval augmented generation (RAG) application designed to find similar planets within the Star Wars universe. The application leverages Hono.js for its lightweight web framework, Couchbase as its primary database and vector store, and [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]] Studio for advanced AI functionalities including text and image generation. Cloudflare is used for deployment [00:00:05].

## Technology Stack

### Hono.js Web Framework
Hono is a lightweight web framework optimized for Edge and Serverless deployments [00:00:12]. It offers easy deployment with platforms like Cloudflare Workers, Vercel Edge, Deno, or Bun [00:00:17]. Key features include server-side rendering and TypeScript support built-in [00:00:27]. Its small bundle size makes it ideal for applications requiring a low footprint [00:00:33]. Hono allows the use of Node-based npm modules (like Couchbase), providing a server-like experience without needing a dedicated Node.js server [00:00:40].

### Couchbase as Vector Store
Couchbase is a powerful NoSQL distributed database that supports Vector Store and Vector Search functionalities [00:01:23]. The application uses Couchbase to store approximately 30 documents, each containing details about a specific Star Wars planet, such as rotation period, orbital period, and embeddings [00:01:28].

### OpenAI for Embeddings
Planet data embeddings are generated using OpenAI's `text-embedding-ada-002` model, with a dimension of 1500 [00:01:41]. These embeddings represent the real-world features of each planet [00:02:06]. When a user queries for a planet, the input query is also converted into an embedding using OpenAI [00:05:04].

### [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]] Studio for AI Models
[[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]] Studio provides a suite of state-of-the-art open-source AI models [00:03:38]:
*   **Text Generation**: Includes models like [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3 and R1]] [00:03:42]. For the planet similarity search, the Llama 3.1 70 billion parameter model is used to generate textual responses [00:07:08].
*   **Text-to-Image Generation**: Features models like [[image_generation_with_nebius_ai_and_flux_model | Flux]] [00:03:46]. This is used to generate images of the planets based on their descriptions [00:03:30].
*   **Vision Models**: For describing content in images [00:03:51].
*   **Embedding Models**: Also available for generating embeddings [00:03:56].

[[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]] Studio offers a playground for testing models and provides Python and JavaScript SDKs for integration via API keys [00:04:01].

## Application Functionality

The application is a retrieval augmented generation (RAG) system [00:01:10]. When a user searches for planets similar to a given one, such as "Alderaan" [00:02:41]:
1.  **Vector Search**: The application performs a vector search in Couchbase to find planets whose embeddings are closest to the queried planet's embedding [00:02:48]. This identifies planets with similar characteristics [00:02:02].
2.  **AI Response Generation**:
    *   A text-based LLM from [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]] (Llama 3.1 70B parameter model) generates a detailed response about the similar planets found, providing their characteristics [00:03:11, 00:07:08].
    *   A text-to-image model, specifically the [[image_generation_with_nebius_ai_and_flux_model | Flux]] model from [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]], generates an image of the queried planet based on its stored description (e.g., Alderaan with mountains and grasslands) [00:02:23, 00:03:22, 00:07:25].

### Example: Searching for Alderaan
Upon querying "Find planets similar to Alderaan" [00:02:41]:
*   The system performs a vector search to identify similar planets like Endor and Yavin 4 [00:03:06].
*   It generates a textual description of these similar planets [00:03:12].
*   An image is generated depicting how Alderaan might look based on its known temperate climate, mountains, and grasslands [00:02:58, 00:03:26].

## Codebase Structure

The project is built with Hono.js and deployed using Cloudflare Pages.

*   `server.ts`: Initializes the Couchbase connection, including connection string, username, password, and bucket name [00:04:16].
*   `index.tsx`: This is the core logic file.
    *   Initializes the Hono app and establishes connection to the Couchbase cluster [00:04:38].
    *   `getRelevantDocuments` function:
        *   Converts the user's input query into an embedding using OpenAI's `text-embedding-ada-002` model [00:05:01].
        *   Performs a vector search in Couchbase to find the nearest vectors (similar planet embeddings) [00:05:22].
        *   Populates search results with the identified similar planets [00:06:09].
    *   `/api/chat` endpoint:
        *   Takes the user's message as input [00:05:57].
        *   Uses [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]]'s Llama 3.1 70B parameter model for text generation based on the retrieved context (similar planets) [00:06:56].
        *   Uses [[integration_of_nebius_ai_for_advanced_ai_functionaliti | Nebius AI]]'s [[image_generation_with_nebius_ai_and_flux_model | Flux]] model to generate an image based on a prompt (e.g., "beautiful detailed illustration of that particular planet") [00:07:18].
        *   Streams the generated text and image responses back to the client [00:07:30].
*   `client.tsx`: The front-end UI responsible for rendering the chat interface, managing state for loading values, and displaying the decoded text and images from the API [00:07:41].
*   `wrangler.toml`: Configuration file for deploying the project with Cloudflare Workers/Pages, allowing for specification of Cloudflare features like KV storage or R2 buckets [00:08:31].

## Deployment
The application is designed for deployment to Cloudflare Workers or Pages [00:08:29, 00:09:00]. The `wrangler.toml` file manages the configuration for Cloudflare services [00:08:47].

This project demonstrates a robust RAG application by combining a lightweight web framework, a powerful NoSQL database with vector search capabilities, and advanced AI models for both text and image generation.