---
title: Knowledge graph mullet
videoId: tYCu_57jzL8
---

From: [[aidotengineer]] <br/> 

The concept of the "knowledge graph mullet" combines elements from both the [[Property graphs and RDF triples | property graph]] world and the [[Property graphs and RDF triples | RDF triple]] world to create a hybrid and versatile approach for managing [[Use of Knowledge Graphs in Generative AI | knowledge graphs]] <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. This analogy, inspired by the mullet haircut, suggests "business in the front, party in the back" <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. In the context of [[Use of Knowledge Graphs in Generative AI | knowledge graphs]], this translates to a [[Property graphs and RDF triples | property graph]] model in the front and [[Property graphs and RDF triples | RDF triples]] in the back <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. The goal is to leverage the benefits of both paradigms, offering a low-maintenance, easy-to-work-with, yet versatile and adaptable solution <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.

## Property Graphs vs. RDF

Traditionally, [[Property graphs and RDF triples | property graphs]] and [[Property graphs and RDF triples | RDF]] are seen as distinct paradigms for working with graphs <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

### Property Graph Model
In the [[Property graphs and RDF triples | property graph]] world, the focus is on:
*   Nodes <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>
*   Relationships <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>
*   Key-value pair properties <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>
*   Graph traversal often uses pattern matching with query languages like Cypher <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

A [[Use of Knowledge Graphs in Generative AI | knowledge graph]] is considered an instance of a [[Property graphs and RDF triples | property graph]] <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. Nodes can have one or more labels for grouping, similar to tables in relational databases <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. Relationships have a single type and direction, and arbitrary key-value properties can be stored on both nodes and relationships <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. The semantics of how entities are connected are encoded in the data model, focusing on representing "things, not strings" <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

### RDF World
The [[Property graphs and RDF triples | RDF]] world typically focuses on:
*   Ontologies <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>
*   Query languages like SPARQL <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>
*   Triples (subject, predicate, object) <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>
[[Property graphs and RDF triples | RDF]] originates from the [[Semantic and graphbased data in AI systems | Semantic Web]] and linked data movements <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. A triple can be thought of as a sentence <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>:
*   **Subject**: Always a node (specifically, a unique ID pointing to a node) <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>, <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Predicate**: A relationship or a property <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
*   **Object**: If the predicate is a relationship, the object is another node; if it's a property, the object is the value of that property <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

## [[Dgraph and its features | Dgraph]] Implementation

[[Dgraph and its features | Dgraph]] is an open-source project designed to work with [[Use of Knowledge Graphs in Generative AI | knowledge graphs]] <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. Released in 2017, [[Dgraph and its features | Dgraph]] was initially optimized for large-scale distributed graph data, inspired by Google's Spanner <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>. It's a hybrid [[Benefits of Graph Databases in AI Applications | graph database]] that uses the [[Property graphs and RDF triples | property graph]] model for data modeling and querying, while employing [[Property graphs and RDF triples | RDF]] for data interchange, treating triples as the smallest unit of record <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

To model a [[Property graphs and RDF triples | property graph]] as an [[Property graphs and RDF triples | RDF triple]] in [[Dgraph and its features | Dgraph]]:
1.  Each node needs a unique ID, which maps to a disk offset for efficient traversal <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.
2.  The subject of an [[Property graphs and RDF triples | RDF triple]] is this unique node ID <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.
3.  The predicate is either a relationship or a property <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>.
4.  The object is either another node ID (for relationships) or the value of the property <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.

[[Dgraph and its features | Dgraph]] uses an optimization called a "posting list," which groups by predicate and lists unique node IDs connected by that predicate, enabling efficient graph traversal <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.

### DQL Query Language
[[Dgraph and its features | Dgraph]] uses DQL (Dgraph Query Language), which was inspired by GraphQL <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>. DQL queries start with a well-defined root criteria, often using an index to find starting nodes <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>. A nested selection set structure specifies both properties to return and represents the graph traversal <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. Results are returned in JSON format, matching the selection set's structure <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

## Application: News Knowledge Graph
A practical example of using [[Dgraph and its features | Dgraph]] is creating a [[Use of Knowledge Graphs in Generative AI | knowledge graph]] for news articles <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.

### Data Model
For a news article, entities like organizations, people, and topics are modeled as nodes <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>. An `Article` node can have properties like URL, publish date, title, and abstract, and relationships to `Author`, `Topic`, `Organization`, `GeographicArea`, and `Image` nodes <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. This model allows traversal from an article to a topic and then to other articles with the same topic or geographic location <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

### Unstructured Data and Graph RAG
Unstructured data, such as article paragraphs, can be chunked and embedded <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>. Each chunk's embedding is stored as a node property, enabling vector search as an entry point into the graph <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.

In a Graph RAG (Retrieval Augmented Generation) approach:
1.  **Vector Search**: Identifies relevant chunks in the "lexical graph" <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.
2.  **Graph Traversal**: From these initial chunks, the system traverses the "domain graph" to find related article nodes, topics, organizations, or other articles with overlapping interests <a class="yt-timestamp" data-t="11:36:00">[11:36:00]</a>. This provides richer context than a naive RAG approach that would simply inject the found document <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.

Other entry points can include geospatial indexes (e.g., finding news near a location) or image embedding similarity searches <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>. Graph RAG is characterized by utilizing different subgraph entry points to gather relevant context for a model <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>.

[[Dgraph and its features | Dgraph]]'s vector similarity search allows finding articles close in vector space to a given embedding (e.g., "money laundering") <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>. Further traversal can then identify related topics, geographic regions, or organizations, and even discover other articles with overlapping topics not found by vector search alone <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.

## [[Use of Knowledge Graphs in Generative AI | Dgraph]] MCP Server
The latest release of [[Dgraph and its features | Dgraph]] includes the Model Context Protocol (MCP) server <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a>. Fundamentally, MCP exposes tools to models, enabling models to interact with a database <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>.

Each [[Dgraph and its features | Dgraph]] instance serves an MCP server:
*   **Read-only instance**: Exposes the ability to execute queries or inspect the schema <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>.
*   **Full endpoint**: Also exposes functionality for mutations (adding data) and altering the schema <a class="yt-timestamp" data-t="17:06:00">[17:06:00]</a>.

### Use Cases
[[Use of Knowledge Graphs in Generative AI | Dgraph]] MCP server use cases include:
*   **Agentic coding assistant environments**: Tools like Windsurf or Cursor can leverage schema or retrieved data to autogenerate CRUD endpoints or DQL queries <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.
*   **Exploratory data analysis**: Tools like Claude Desktop can generate DQL queries and fetch data to understand the graph's contents <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>.

When using database MCP servers, the model generates the database query and then uses the tools defined in the MCP server to execute those queries against the database <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>. This allows users to create graph schemas and add data without deep knowledge of the specific query language, while simultaneously serving as a learning tool for the query language <a class="yt-timestamp" data-t="20:45:00">[20:45:00]</a>.

## Agent Orchestration with Modus
To build agentic applications, Hypermode created the Modus agent orchestration framework <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>. Modus is an open-source framework for creating AI agents, bringing data to models, and exposing tools and abstractions for agentic flows <a class="yt-timestamp" data-t="24:21:00">[24:21:00]</a>. Key functionalities include:
*   Abstractions for working with models and data <a class="yt-timestamp" data-t="24:46:00">[24:46:00]</a>.
*   A runtime for managing a large number of stateful, long-running agents <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>.
*   An SDK library for working with agents <a class="yt-timestamp" data-t="25:13:00">[25:13:00]</a>.

Modus leverages WebAssembly to target multiple languages (like Go or AssemblyScript) for different SDKs, compiling code to WebAssembly and generating a unified GraphQL API <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>. The WebAssembly runtime also provides security and a sandboxed environment for AI agents <a class="yt-timestamp" data-t="25:55:00">[25:55:00]</a>.

## Hypermode Agents
Hypermode Agents allow users to build domain-specific agents primarily from a prompt, exposing tools via MCP servers <a class="yt-timestamp" data-t="26:31:00">[26:31:00]</a>.

### Example: Social Media Intern Agent
An agent can be defined with a background prompt (e.g., "social media expert") and a reasoning model (e.g., GPT-4) <a class="yt-timestamp" data-t="27:19:00">[27:19:00]</a>. Connections to MCP servers (e.g., GitHub, Notion, company docs) allow the agent to interact with its environment <a class="yt-timestamp" data-t="27:47:00">[27:47:00]</a>.

A task could involve analyzing a GitHub repo (like Hypernews, which contains [[Dgraph and its features | Dgraph]] tooling) and generating social media posts explaining technical concepts <a class="yt-timestamp" data-t="28:17:00">[28:17:00]</a>. The agent makes tool calls to search the repo and fetch file contents <a class="yt-timestamp" data-t="28:44:00">[28:44:00]</a>. It can then be prompted to update these posts with relevant code snippets, using its tools to access source files <a class="yt-timestamp" data-t="29:16:00">[29:16:00]</a>. Finally, the agent can save these posts to a Notion workspace by accessing it through the Notion MCP server <a class="yt-timestamp" data-t="30:00:00">[30:00:00]</a>.

A notable feature is the ability to "eject to code," allowing users to obtain the underlying Modus code for the agent, enabling further customization and complex logic <a class="yt-timestamp" data-t="31:18:00">[31:18:00]</a>.

## Conclusion
The "knowledge graph mullet" approach, implemented through tools like [[Dgraph and its features | Dgraph]], combines the strengths of [[Property graphs and RDF triples | property graphs]] and [[Property graphs and RDF triples | RDF triples]] to build powerful Graph RAG workflows <a class="yt-timestamp" data-t="32:17:00">[32:17:00]</a>. This foundation can then be leveraged for constructing advanced AI agents, with features like the [[Use of Knowledge Graphs in Generative AI | Dgraph]] MCP server and agent orchestration frameworks like Modus facilitating interaction with [[Use of Knowledge Graphs in Generative AI | knowledge graphs]] and other services <a class="yt-timestamp" data-t="32:30:00">[32:30:00]</a>.