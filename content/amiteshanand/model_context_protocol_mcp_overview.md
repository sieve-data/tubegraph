---
title: Model Context Protocol MCP Overview
videoId: H-3VJ7usA58
---

From: [[amiteshanand]] <br/> 

The Model Context Protocol (MCP) is an open-source framework launched by Anthropic, the company behind the large language model Claude <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It has seen significant adoption since its launch approximately three months prior <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Shift Towards Agentic AI and Tool Calling

Traditionally, interaction with large language models (LLMs) involved chat interfaces like ChatGPT or Claude, where users asked questions and the model generated a text-based response <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A fundamental shift is now occurring with the rise of agentic AI, where models can access external tools <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This enables LLMs to move beyond just text generation and carry out complex tasks <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

A core concept in agentic AI is "tool calling" <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. LLMs, by themselves, are limited to text generation and cannot directly perform actions like retrieving real-time API data or fetching information from a database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Tool calling allows LLMs to leverage external databases, APIs, and other tools <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

When a user provides a query, the LLM analyzes it to determine if a text-based response is sufficient or if an external tool should be used to augment the response, provide real-time updates, or access proprietary data <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. MCP facilitates this by enabling LLMs like Claude to use external tools and data to enhance their responses <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This significantly expands the potential use cases for LLMs <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Building MCP Servers

MCP allows developers to build servers that define a set of tools accessible to LLMs <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. These servers can be defined using either the [[building_mcp_servers_with_typescript_and_python_sdks | TypeScript SDK or Python SDK]] <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Key Components

*   **SDKs**: The Model Context Protocol Server SDKs (e.g., for TypeScript) help in defining the MCP server <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Tool Definition**: Tools are defined using `server.setRequestHandler` <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Each tool includes:
    *   **Name**: A unique identifier for the tool <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   **Description**: A detailed explanation of what the tool does, which helps the LLM intelligently identify when to use it based on the user's prompt <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   **Input Schema (JSON)**: MCP requires a JSON input schema to understand how the LLM should pass data to the tool <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For TypeScript, Zod can be used for type safety and then converted to a JSON schema <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Request Handlers**: These are functions that define the actions performed by each tool. A switch-case structure can be used to direct requests to the appropriate handler based on the tool identified by the LLM <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **JSON Output**: Tool responses are generated in JSON format, which is then sent back to the LLM to augment its final response <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **MCP JSON File**: A `model context protocol.json` file is required to define environment variables and other metadata about the MCP server <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Example: Star Wars Planet Data Server

An example MCP server was demonstrated to retrieve Star Wars planet data, find similar planets, and generate images <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Tools Defined

The example server registered four MCP tools:

1.  **`fetchPlanetName`**: Retrieves details about a specific Star Wars planet from a database <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
2.  **`findSimilarPlanets`**: Identifies planets similar to a given planet using vector search <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
3.  **`generatePlanetImage`**: Creates an image of a planet <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### How it Works in Practice

When a prompt like "Show me planets that are probably similar to the planet Alderaan and include an image of Alderaan" is given to Claude <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>:

1.  **Tool Identification**: Claude, interacting with the running MCP server, intelligently identifies which tools are most relevant <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
2.  **Execution - `findSimilarPlanets`**: It first uses the `findSimilarPlanets` tool <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
    *   This tool fetches Alderaan's data from a Couchbase database <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   It then retrieves the embedding for Alderaan <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   Using Couchbase's vector search index, it finds the top most similar planets based on their embeddings, returning a score for each match <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
3.  **Execution - `generatePlanetImage`**: Concurrently, or subsequently, it uses the `generatePlanetImage` tool <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
    *   This tool leverages the Nebulas AI Studio <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, which provides various open-source LLMs, including text-to-image models like Flux <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    *   Using an OpenAI client with Nebulas Studio as the base URL, it generates a realistic astronomical image of the planet based on its description <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. The response is requested in Base64 format, which is accepted by Claude MCP <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
4.  **Response Generation**: Claude combines the image generated by Nebulas Studio and the structured JSON output from the `findSimilarPlanets` tool (detailing climate, terrain, etc.) to present a comprehensive response to the user <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Core Functions within the Server

*   `getCharacter`: Fetches planet details from a Couchbase database collection based on the input name <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   `findSimilarCharacters`: Uses vector search in Couchbase to find planets with similar features by comparing embeddings <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   `generatePlanetImage`: Calls the Nebulas Studio API to create an image based on a text prompt describing the planet <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## Expanding LLM Capabilities with MCP

MCP significantly empowers LLMs by allowing them to:
*   Access external databases (e.g., Couchbase) <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   Make external API calls (e.g., Nebulas Studio for image generation) <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   Perform actions beyond mere text generation, such as ordering clothes based on weather or any other use case that can be connected via an API <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

This capability to build agentic workflows where LLMs can generate text and interact with the real world through tools makes the opportunities limitless <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.