---
title: Graph RAG workflows
videoId: tYCu_57jzL8
---

From: [[aidotengineer]] <br/> 

Graph RAG (Retrieval-Augmented Generation) workflows aim to reduce the complexity associated with traditional graph RAG systems <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This approach combines concepts from property graphs and RDF (Resource Description Framework) to create a hybrid and versatile method for working with knowledge graphs <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>.

## Extending Naive RAG with Graph Traversal

In a naive RAG approach, vector search is used to find relevant document chunks, which are then injected into a prompt to add context <a class="yt-timestamp" data-t="01:11:23">[01:11:23]</a>. However, in Graph RAG, this vector search is only the starting point <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>. After identifying initial chunks, the system traverses the graph to expand context by finding related entities such as article nodes, topics relevant to those articles, or other articles with the same topic or mentioning the same organization <a class="yt-timestamp" data-t="01:11:36">[01:11:36]</a>.

Graph RAG is characterized by its use of various subgraph entry points <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>. This includes:
*   **Lexical Graph:** Used for vector search with unstructured data <a class="yt-timestamp" data-t="01:12:36">[01:12:36]</a>.
*   **Domain Graph:** Traversed to find relevant context for the model <a class="yt-timestamp" data-t="01:12:40">[01:12:40]</a>.
*   **Other Entry Points:** Can include geospatial indices (e.g., finding news articles near a specific location) or image embedding models for image similarity search <a class="yt-timestamp" data-t="01:11:52">[01:11:52]</a>.

## Dgraph as a Foundation for Graph RAG

Dgraph is an open-source project that serves as a hybrid graph database, optimizing for large-scale distributed graph data <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>. It uses the property graph model for data modeling and querying, while employing RDF for data interchange, working with triples as the smallest unit of record <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

### Knowledge Graph Definition in Dgraph
A knowledge graph in Dgraph is considered an instance of a property graph <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **Nodes:** Can have one or more labels that define their type, similar to tables in a relational database <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
*   **Relationships:** Have a single type and direction <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.
*   **Properties:** Arbitrary key-value pairs can be stored on nodes and relationships <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   **Semantics:** How entities are connected is encoded in the data model, focusing on representing "things, not strings" <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. This ensures a canonical representation of entities <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.

### Modeling Property Graphs as RDF Triples in Dgraph
Dgraph models property graphs as RDF triples (subject, predicate, object) <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.
*   **Subject:** Always a unique ID for a node, acting as a pointer <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Predicate:** Represents a relationship or a property <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>.
*   **Object:** If the predicate is a relationship, the object is another node ID; if it's a property, the object is the value of that property <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>.

Dgraph uses an optimization called a "posting list" to group by predicate and list unique node IDs, allowing for efficient graph traversal <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.

### DQL Query Language
DQL (Dgraph Query Language) is inspired by GraphQL <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   **Starting Point:** Every traversal begins with a well-defined root criteria, often using an index to find initial nodes <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   **Selection Set:** A nested structure specifies properties to return and represents the graph traversal path <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.
*   **Output:** Data returned from a DQL query is in JSON format, matching the structure of the selection set <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

## Example: News Knowledge Graph
To illustrate Graph RAG, a news knowledge graph can be created <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
*   **Entities as Nodes:** Organizations, people, topics, authors, images, and even paragraphs (as chunks) can be modeled as nodes <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.
*   **Unstructured Data:** Unstructured data is chunked (e.g., each paragraph as a chunk) and embedded, with the embedding stored as a node property <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>. This allows for vector search as an entry point <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
*   **Traversals:** From an article, one can traverse to its author, mentioned topics, organizations, geographic areas, and related images <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>. This enables finding other articles with the same topic or location <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.
*   **Querying Examples:** Dgraph can be used for:
    *   Simple article counts <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
    *   Traversing from articles to topics <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>.
    *   Filtering by publication date and traversing to geographic areas <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>.
    *   Geographic distance search (e.g., news within a certain radius) <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.
    *   Vector similarity search, followed by graph traversal to find related topics, regions, or organizations <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
    *   More complex traversals combining vector search matches with topic overlap to discover indirectly related articles <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.

## Agentic Applications with Graph RAG
Graph RAG workflows provide the foundation for building AI agents <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

### Model Context Protocol (MCP)
MCP is a way to expose tools to models, enabling them to interact with databases like Dgraph <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>. Each Dgraph instance serves as an MCP server <a class="yt-timestamp" data-t="16:53:00">[16:53:00]</a>.
*   **Read-only instance:** Exposes query execution and schema inspection capabilities <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.
*   **Full endpoint:** Also exposes functionality for mutations (adding data) and schema alterations <a class="yt-timestamp" data-t="17:06:00">[17:10:00]</a>.

Use cases for Dgraph MCP servers include:
*   **Agentic Coding Assistants:** Tools that leverage schema and retrieved data to autogenerate CRUD endpoints or DQL queries <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.
*   **Exploratory Data Analysis:** Generating DQL queries to fetch and understand data in the graph, often through interfaces like Claude desktop <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>. The model generates queries and executes them, verifying results and iterating if needed <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>.

### Modus Agent Orchestration Framework
Modus is an open-source framework by Hypermode for building AI agents, focusing on bringing data to models and exposing tools for agentic flows <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>. It provides abstractions for working with models and data, along with a runtime for managing large numbers of stateful, long-running agents <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

Modus uses WebAssembly (Wasm) to target multiple languages for SDKs (e.g., Go, AssemblyScript), compiling logic to Wasm and generating a unified GraphQL API that leverages defined types and function signatures <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This provides a secure and sandboxed environment for AI agents <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

### Hypermode Agents
Hypermode Agents allow users to create domain-specific agents starting with a prompt and exposing tools via MCP servers <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. These agents can interact with various services (e.g., GitHub, Notion) via their respective MCP servers <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. For example, an agent can analyze a GitHub repository, generate social media posts, include relevant code snippets, and save the output to a Notion workspace <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. Hypermode Agents also offer the ability to "eject to code," allowing users to access the underlying Modus code to add more complex logic or connections <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.