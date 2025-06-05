---
title: Dgraph and its features
videoId: tYCu_57jzL8
---

From: [[aidotengineer]] <br/> 

Dgraph is an open-source graph database first released in 2017, designed to optimize for large-scale graph data [00:04:23]. Its "D" stands for distributed, focusing on scaling in terms of data volume [00:04:37]. The original Dgraph team was inspired by Google's Spanner graph [00:04:46].

## The Knowledge Graph Mullet

Dgraph embodies the concept of the [[knowledge_graph_mullet | knowledge graph mullet]], combining elements from both [[Property graphs and RDF triples | property graph]] and [[Property graphs and RDF triples | RDF triples]] worlds [00:01:01]. This hybrid approach offers a versatile way to work with knowledge graphs, leveraging the best of both paradigms [00:01:08].

Dgraph uses the [[Property graphs and RDF triples | property graph]] model for data modeling and querying, while employing [[Property graphs and RDF triples | RDF triples]] for data interchange, treating triples as the smallest unit of record [00:04:59].

### Property Graph Model

The [[Property graphs and RDF triples | property graph]] model, which Dgraph uses for data modeling and querying, defines a knowledge graph as an instance of a [[Property graphs and RDF triples | property graph]] [00:02:58]. Key components include:
*   **Nodes** Nodes can have one or more labels that indicate their type or group them, similar to tables in relational databases [00:03:03].
*   **Relationships** Relationships have a single type and direction [00:03:24].
*   **Properties** Arbitrary key-value pair properties can be stored on both nodes and relationships [00:03:30].

The semantics, or how entities are connected, are encoded in the data model [00:03:36]. Instead of simply stating two nodes are related, Dgraph specifies the nature of their connection, such as a "talk has a certain topic" or "was presented at a conference" [00:03:40]. This approach focuses on connecting "things, not strings," providing a canonical representation of entities [00:04:00].

### RDF Triples

In the RDF world, the focus is on ontologies and [[Property graphs and RDF triples | triples]] (subject-predicate-object) [00:01:54]. [[Property graphs and RDF triples | RDF triples]] originated from the semantic web and linked data [00:02:05].

In Dgraph, a [[Property graphs and RDF triples | property graph]] is modeled as an [[Property graphs and RDF triples | RDF triple]]:
*   A unique ID for each node is required to model a [[Property graphs and RDF triples | property graph]] as an [[Property graphs and RDF triples | RDF triple]] [00:06:10].
*   The subject is always a node, specifically a unique ID pointing to the node [00:06:40].
*   The predicate can be a relationship or a property [00:06:49].
*   The object is either another node ID (if the predicate is a relationship) or the value of a property [00:06:53].

### Optimization: Posting List

Dgraph employs an important optimization called a "posting list" [00:07:14]. This involves grouping by predicate and using a list of unique node IDs for all nodes connected by that predicate, allowing for efficient graph traversal [00:07:21].

## DQL: Dgraph Query Language

DQL is the query language used with Dgraph, heavily inspired by GraphQL [00:07:38].
*   **Traversal Structure** Every DQL graph traversal begins with a well-defined starting point, often using an index to find root nodes [00:08:12].
*   **Selection Set** Queries use a nested selection set structure to specify properties to return and represent graph traversals [00:08:29].
*   **JSON Output** Data returned from a DQL query is in JSON format, matching the structure of the selection set [00:08:49].

## Applications and Use Cases

### News Knowledge Graph Example

To illustrate Dgraph's capabilities, a news knowledge graph can be created [00:09:03].
*   **Modeling Entities** Entities mentioned in news articles, such as organizations, people, and topics, are modeled as nodes [00:09:16]. Authors, images, and unstructured data (like paragraphs) can also be represented as nodes [00:09:29].
*   **Unstructured Data Handling** Unstructured data is chunked (e.g., each paragraph as a chunk) and embedded [00:09:39]. The embedding of each chunk is calculated and stored as a node property, enabling vector search as an entry point into the graph [00:10:47].

### Graph RAG Workflows

In a [[graph_rag_workflows | graph RAG]] approach, vector search (lexical graph) identifies relevant chunks, which serve as a starting point [00:11:20]. The system then traverses the graph (domain graph) from these chunks to related articles, topics, and organizations to gather relevant context for the model [00:11:36]. Other entry points include:
*   **Geospatial Index** Finding news articles within a certain region or near a specific location [00:11:55].
*   **Image Similarity Search** Using image embeddings as an entry point for searching [00:12:21].

This concept of different subgraph entry points is central to [[graph_rag_workflows | graph RAG]] [00:12:32].

### Hands-on Example with Rattell

Rattell, a query workbench for Dgraph, allows users to execute DQL queries and visualize results [00:12:55]. Examples include:
*   Counting articles [00:13:10].
*   Searching for articles and traversing to connected topics [00:13:14].
*   Filtering articles by publication date and traversing to mentioned geographic areas [00:13:36].
*   Geographic distance search (e.g., finding news areas within 50 km of New York City) [00:13:57].
*   Vector search (e.g., finding articles close in vector space to a phrase like "money laundering") [00:14:20].
*   Complex traversals combining vector search results with topic-based traversals to find related articles not caught by initial vector search [00:14:51].

### Product Recommendations

Dgraph can be used for generating personalized product recommendations [00:22:01]. This is a typical graph database use case, where recommendations are generated by traversing the graph [00:22:08]. Approaches include:
*   **Collaborative Filtering** Finding similar users and identifying products they purchased that the target user has not [00:22:17].
*   **Content-Based Recommendations** Based on a user's purchase history and product attributes [00:22:35].
*   **Demographic Approaches** Using demographic data to inform recommendations [00:22:43].

These approaches can be combined into a single database query [00:22:52].

## Model Context Protocol (MCP) Server

Dgraph's latest release includes a Model Context Protocol (MCP) server, which exposes tools to models, enabling them to interact with the database [00:15:37].
*   **Dgraph MCP Server** Each Dgraph instance serves an MCP server [00:16:50].
    *   A **read-only instance** allows models to execute queries or inspect the schema [00:16:58].
    *   A **full endpoint** also enables mutations (adding data) and altering the schema [00:17:06].
*   **Use Cases**
    *   **Agentic Coding Assistant Environments** Tools like Windsurf or Cursor can leverage the schema or retrieved data from the MCP server to auto-generate code, such as CRUD endpoints or DQL queries [00:17:21].
    *   **Exploratory Data Analysis** Tools like Claude desktop can generate DQL queries and fetch data to understand the graph's contents [00:17:54].

### Claude Desktop Integration

A demonstration shows integrating Dgraph's MCP server with Claude desktop [00:18:15].
1.  **Deploying Dgraph** A Hypermode graph, powered by Dgraph, is deployed, including the MCP server endpoint [00:18:22].
2.  **Configuring Claude** The MCP configuration is copied into Claude desktop's developer config [00:18:46].
3.  **Schema and Data Generation** Claude inspects the empty database, generates a graph schema (e.g., for e-commerce customer, product, and order data), and then generates a series of mutations to populate the graph with fictitious data [00:19:21].
4.  **Model-Generated Queries** The model generates database queries (DQL) and uses the MCP server tools to execute them against the database [00:20:00]. Claude can verify data creation and correct missing relationships through further mutations [00:20:16].
5.  **Graph Visualization** Claude can generate queries to fetch data and then produce JavaScript to render a graph visualization, aiding in understanding graph connections [00:21:07]. Different layout options (force-directed, hierarchical, radial) are available [00:21:41].
6.  **Learning Tool** This interaction serves as a valuable way to learn new developer tooling and query languages like DQL without needing to write them manually initially [00:20:45].

## Modus Agent Orchestration Framework

Dgraph integrates with the open-source Modus agent orchestration framework, created by Hypermode to enable building agentic apps [00:24:07]. Modus provides abstractions for working with models and data, along with a runtime for managing large numbers of stateful, long-running AI agents [00:24:46]. It leverages WebAssembly for multi-language SDKs (e.g., Go, AssemblyScript) and generates a unified GraphQL API [00:25:16].

## Hypermode Agents

Hypermode agents are powered by Dgraph and the Modus framework [00:26:21]. These domain-specific agents can be created starting with a prompt and by exposing tools via MCP servers [00:26:31]. Agents can interact with various services (e.g., GitHub, Notion, company docs via Ref) through their respective MCP servers [00:27:50].

### Agent Demonstration

An example demonstrates a social media intern agent [00:27:13]:
*   **Task** Analyze a GitHub repo (Hypernews, containing Dgraph tooling for news knowledge graphs) and generate social media posts [00:28:17].
*   **Tool Calls** The agent searches for the repo, fetches file contents using GitHub MCP server tools, and generates posts [00:28:44].
*   **Iteration** The agent can be prompted to update posts to include relevant code snippets by accessing source files via GitHub tools [00:29:16].
*   **Saving Output** The agent can save the generated content to a Notion workspace page using Notion MCP server tools [00:30:00].
*   **Code Ejection** Users can "eject to code" to view the underlying Modus code running the agent, allowing for further customization and enhancement [00:31:18].

Hypermode agents are in early access [00:32:02].

## Conclusion

Dgraph provides a powerful foundation for building AI agents and [[graph_rag_workflows | graph RAG workflows]] by combining the strengths of [[Property graphs and RDF triples | property graph]] and [[Property graphs and RDF triples | RDF triples]] ecosystems in a [[knowledge_graph_mullet | knowledge graph mullet]] approach [00:32:17]. Its features, including DQL, distributed architecture, and the MCP server, facilitate effective interaction between AI models and knowledge graphs.