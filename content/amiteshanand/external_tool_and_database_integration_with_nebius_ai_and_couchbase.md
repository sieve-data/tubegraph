---
title: External Tool and Database Integration with Nebius AI and Couchbase
videoId: H-3VJ7usA58
---

From: [[amiteshanand]] <br/> 

The Model Context Protocol (MCP) is an open-source framework launched by Anthropic, the company behind the Claude large language model <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It has rapidly gained adoption since its launch due to its ability to fundamentally shift how users interact with AI systems <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## The Rise of Agentic AI and Tool Calling

Traditionally, interaction with large language models (LLMs) like ChatGPT or Claude involved simple chat interfaces where a user asks a question and the LLM generates a text-based response <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. However, there's a shift towards "agentic AI," where models gain access to external tools, allowing them to perform tasks beyond mere text generation <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

A fundamental concept in this shift is **tool calling** <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Since LLMs are typically limited to text generation, they cannot directly:
*   Respond to questions related to real-time APIs <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   Retrieve data from a user's database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Tool calling enables LLMs to access external databases, APIs, and other tools <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Based on a user's query, the LLM intelligently analyzes whether to provide a text-based response or to leverage one of these tools to:
*   Augment its response <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   Give real-time updates <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   Access proprietary data stored in a database <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The MCP protocol enhances LLMs like Claude by allowing them to utilize external tools and data to provide augmented responses based on user queries, significantly expanding potential use cases <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Building an MCP Server

MCP servers can be built using either a TypeScript SDK or a Python SDK <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. These servers define a set of tools that LLMs, such as Claude, can access and use to perform actions beyond basic text generation <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

Key aspects of defining an MCP server:
*   **Tool Definition**: Tools are defined using `server.setRequestHandler`, which outlines the available tools <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Intelligent Tool Selection**: The LLM (e.g., Claude) automatically identifies the most relevant tool to use based on the user's input prompt <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The tool's `description` and `name` are crucial for this identification <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Input Schema**: MCP requires a JSON input schema for tools to understand how to process user prompts <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. For TypeScript, `Zod` can be used for type safety and `Zod to JSON schema` for schema definition <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Responses are also generated in JSON format <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Request Handlers**: A switch-case mechanism within the request handlers executes the appropriate function for the identified tool <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. These handlers call pre-defined functions to fetch data or generate images <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. The results from these functions are then used by the LLM to render an augmented response <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Example: Star Wars Planet Data Retrieval and Image Generation

A practical example demonstrates how an MCP server can retrieve Star Wars planet data and generate images. This server integrates with [[couchbase_as_a_distributed_nosql_database | Couchbase]] for data retrieval and [[Text and image generation using Nebius AI models | Nebius AI Studio]] for image generation <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

The example MCP server defines several tools:
1.  **`fetchPlanetName`**: Retrieves details about a specific Star Wars planet from a database <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
2.  **`findSimilarPlanets`**: Uses [[couchbase_as_a_distributed_nosql_database | Couchbase]] Vector Search to find planets similar to a given one <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
3.  **`generatePlanetImage`**: Creates an image of a planet using [[Text and image generation using Nebius AI models | Nebius AI Studio]] <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Integration with Couchbase

For data retrieval and finding similar planets:
*   The `getCharacter` function fetches planet details from a [[couchbase_as_a_distributed_nosql_database | Couchbase]] collection based on the planet's name from the input query <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   To find similar planets, the system leverages [[couchbase_as_a_distributed_nosql_database | Couchbase]]'s Vector Search <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>:
    *   It first retrieves the embedding for the input planet <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   Then, it defines a vector search index within [[couchbase_as_a_distributed_nosql_database | Couchbase]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   A vector search query is executed to find the closest embeddings (and thus, similar planets) to the input planet's embedding, returning a score of match <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Integration with Nebius AI Studio

[[Text and image generation using Nebius AI models | Nebius AI Studio]] provides various open-source large language models, including text-to-text and embedding generation models <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. For image generation:
*   The `generatePlanetImage` function uses [[Text and image generation using Nebius AI models | Nebius AI Studio]]'s text-to-image model, specifically the Flux model <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>, <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   An OpenAI client is initialized with the [[Text and image generation using Nebius AI models | Nebius AI Studio]] base URL and an API key <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   The `clients.images.generate` method is called with a prompt (e.g., "realistic astronomical image of a Star Wars planet with the given name") and the Flux model <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   The response is requested in Base64 format, which is accepted by Claude MCP <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Demonstration with Claude

When using the MCP server with Claude, the registered MCP tools become accessible <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Claude can intelligently determine which tool to use based on the user's prompt <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

For instance, a prompt like "Show me planets that are probably similar to the planet Alderaan and include an image of Alderaan" demonstrates the integration <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
1.  Claude calls the `findSimilarPlanets` tool, correctly identifying Alderaan <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
2.  It fetches Alderaan's data from the [[couchbase_as_a_distributed_nosql_database | Couchbase]] database <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
3.  It then uses vector search to find similar planets, returning their details and a vector store score indicating closeness <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>, <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
4.  Concurrently, Claude calls the `generatePlanetImage` tool <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
5.  [[Text and image generation using Nebius AI models | Nebius AI Studio]] (Flux model) generates a realistic image of Alderaan based on its description <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
6.  Finally, Claude combines the image and the structured JSON output from the tool calls to present a rich, augmented response, including details like climate and terrain of similar planets <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>, <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### Expanding Capabilities

This approach empowers LLMs to:
*   Access external databases like [[couchbase_as_a_distributed_nosql_database | Couchbase]] <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   Leverage external APIs such as [[Text and image generation using Nebius AI models | Nebius AI Studio]] for specialized tasks <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

The opportunities for expanding use cases are limitless, from finding real-time weather and ordering clothes based on conditions to integrating with any external API <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. By leveraging the Model Context Protocol for tool calling, LLMs can move beyond text generation to build "agentic workflows" that access external data and tools, significantly enhancing their capabilities <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.