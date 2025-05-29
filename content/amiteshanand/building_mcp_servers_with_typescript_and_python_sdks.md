---
title: Building MCP Servers with Typescript and Python SDKs
videoId: H-3VJ7usA58
---

From: [[amiteshanand]] <br/> 

The [[model_context_protocol_mcp_overview | Model Context Protocol]] (MCP) is an open-source framework launched by Anthropic that has gained significant adoption in the developer world since its release three months ago <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It represents a fundamental shift in how developers interact with AI systems, moving beyond simple text generation to what is known as agentic AI <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## What is Agentic AI and Tool Calling?
Traditionally, interaction with large language models (LLMs) like ChatGPT or Claude involved asking a question and receiving a text-based response <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Agentic AI, however, allows these models to gain access to external tools <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This capability, known as "tool calling," enables LLMs to perform tasks beyond mere text generation <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

For instance, without tool calling, an LLM cannot directly interact with a real-time API or retrieve data from a database <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. With tool calling, LLMs can access external databases, APIs, and other tools <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The LLM analyzes the user's query and intelligently decides whether to provide a text-based response or to leverage an available tool to augment its response, providing real-time updates or access to proprietary data <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

The [[model_context_protocol_mcp_overview | Model Context Protocol]] allows LLMs like Claude to offer an enhanced experience by using external tools and data to augment their responses to user queries <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This significantly expands the potential use cases for LLMs <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Building MCP Servers
MCP servers can be built using either the TypeScript SDK or the Python SDK <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. These SDKs allow developers to define the server and the set of tools that a model (e.g., Claude) can access and utilize to perform actions beyond text generation <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Defining Tools and Handlers
When building an MCP server, developers define a set of tools. These tools are automatically identified by the LLM (e.g., Claude Desktop) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The LLM intelligently understands whether to use a tool based on the user's prompt <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The `server.setRequestHandler` function is used to define these tools <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

Key elements for defining a tool include:
*   **Name and Description:** These help the LLM identify the most relevant tool based on the input prompt <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Input Schema:** MCP requires a JSON input schema for tools <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This schema dictates how the LLM will pass data to the tool based on the user's prompt. The tool then generates a JSON response that is sent back to the LLM to augment its final output <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   In TypeScript, Zod is used for type safety and defining types, which are then converted to a JSON schema using `zodToJsonSchema` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

When the LLM decides to use a specific tool (tool calling), a request handler is invoked <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. A switch case can be used to direct the call to the appropriate function for that tool <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. These handlers execute predefined functions to fetch data, generate images, or perform other actions <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. The results from these functions are then used by the LLM to render its response <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Example: Star Wars Planet Data Server
A practical example of an MCP server involves retrieving and generating data about Star Wars planets <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This server can:
1.  Retrieve specific Star Wars planet data from a database like Couchbase <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  Find related planets using Couchbase vector search <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
3.  Generate an image of a planet using an external API like Nebu Studio <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Defined Tools in the Star Wars Server
*   `fetchPlanetName`: Used to fetch details about a specific planet given its name <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   `findSimilarPlanets`: Used to find planets similar to a given planet <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   `generatePlanetImage`: Used to generate an image for a specific planet <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

### Implementation Details
*   **Data Retrieval:** The `getCharacter` function (used by `fetchPlanetName`) queries a Couchbase collection to find and retrieve all data for a specific Star Wars planet <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Similar Planet Search:** The `findSimilarPlanets` function leverages vector search <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. It first retrieves the embedding for the input planet, then uses Couchbase's vector search index to find the most closely matching embeddings, which correspond to planets with the closest features <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The results include a score indicating the closeness of the match <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Image Generation:** The `generatePlanetImage` function integrates with [[using_thirdparty_tools_in_ai_development | Nebu Studio]], an AI service offering various open-source large models <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Specifically, it uses a text-to-image model like the Flux model <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. The `OpenAI` client is initialized with the Nebu Studio API key and base URL <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. A prompt is crafted (e.g., "realistic astronomical image of a Star Wars planet with the given name"), and the `client.images.generate` method is called <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. The image response is requested in Base64 format, which is compatible with Claude MCP <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### Interaction with Claude
Once the MCP server is initialized (e.g., named "Star Wars Server") <a class="yt-timestamp" data-t="00:09:59">[00:10:00]</a> and an `mcp.json` file is created (defining environment variables and other JSON data for the protocol) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, Claude can be used to interact with it.

When a prompt is given to Claude, such as "Show me planets that are probably similar to the planet Alderaan and include an image of Alderaan," Claude automatically identifies the relevant tools from the MCP server <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   It first uses `findSimilarPlanets` to fetch Alderaan data and then apply vector search to find similar planets <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   Then, it uses `generatePlanetImage` to create an image of Alderaan using the Nebu Studio AI <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

The information retrieved from these tool calls (structured JSON data about similar planets, including climate and terrain, and the generated image) is then used by Claude to enrich its final response to the user <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This demonstrates how LLMs can access external databases and APIs to provide highly augmented and dynamic responses <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

### Broader Implications
The ability for LLMs to make external tool calls and access databases and APIs opens up limitless possibilities for agentic workflows <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. For example, an LLM could:
*   Find the latest weather in a location and then use an external API to order weather-appropriate clothing for delivery <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   Access credit card information to complete transactions based on user requests <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

This capability allows developers to build sophisticated AI agents that not only generate text but also interact with the real world through various tools and data sources <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.