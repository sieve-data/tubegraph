---
title: Property graphs and RDF triples
videoId: tYCu_57jzL8
---

From: [[aidotengineer]] <br/> 

The concepts of property graphs and RDF (Resource Description Framework) are typically considered two distinct paradigms for working with graphs <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. However, these concepts can be leveraged together to combine their benefits and create a versatile approach for working with knowledge graphs <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a> <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## The Knowledge Graph Mullet

The "knowledge graph mullet" analogy describes a hybrid approach: "property graph in the front and RDF triples in the back" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This approach aims to expose a property graph model for thinking about and querying data, while leveraging the scalability of RDF triples in the knowledge graph <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

## Property Graphs

A knowledge graph is often defined as an instance of a property graph <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. The property graph model is built upon fundamental elements:
*   **Nodes** Nodes can have one or more labels, which categorize them and are similar to tables in relational databases <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a> <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a> <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Relationships** These connect nodes and have a single type and direction <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a> <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Properties** Arbitrary key-value pair properties can be stored on both nodes and relationships <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a> <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

The semantics of how entities are connected are encoded directly in the data model <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Instead of simply stating two nodes are related, a property graph specifies the nature of that relationship (e.g., "this talk has a certain topic" or "this talk was presented at a conference") <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a> <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. A core idea is having a canonical representation of "the thing" being modeled <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

In the property graph world, traversal often uses pattern matching with a query language like Cypher <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a> <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## RDF Triples

RDF originates from the Semantic Web and linked data world <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a> <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The core concept of RDF is the triple:
*   **Subject**
*   **Predicate**
*   **Object**

These can be thought of as a sentence <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. In RDF, ontologies are typically used, and the query language is SPARQL <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a> <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a> <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## How Dgraph Combines Both

[[Dgraph and its features | Dgraph]] is an open-source project that serves as a hybrid graph database <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a> <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It uses the property graph model for data modeling and querying, but internally it uses RDF for data interchange, working with triples as the smallest unit of record <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a> <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a> <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### Modeling Property Graphs as RDF Triples in Dgraph
To model a property graph as an RDF triple in [[Dgraph and its features | Dgraph]]:
1.  **Unique ID for Each Node** Each node requires a unique ID, which maps to an offset on disk for efficient graph traversal <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a> <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a> <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
2.  **Subject** The subject of an RDF triple is always a node, specifically its unique ID, which acts as a pointer to the node <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a> <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a> <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a> <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a> <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
3.  **Predicate** The predicate can represent either a relationship type or a property <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a> <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
4.  **Object**
    *   If the predicate is a relationship, the object is another node's unique ID <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a> <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   If the predicate is a property, the object is the value of that property <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

[[Dgraph and its features | Dgraph]] employs a "posting list" optimization, which groups data by predicate and uses a list of unique node IDs connected by that predicate, allowing for efficient graph traversal <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a> <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a> <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a> <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a> <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a> <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

[[Dgraph and its features | Dgraph]]'s query language, DQL, is inspired by GraphQL <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a> <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. DQL graph traversals start with a defined root criteria (often using an index) and use a nested selection set structure to specify both desired properties and the traversal path <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a> <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a> <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Data returned from a DQL query is JSON, matching the selection set structure <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a> <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

This hybrid approach makes [[Dgraph and its features | Dgraph]] a powerful tool for [[graph_rag_workflows | Graph RAG workflows]] and other AI applications requiring complex data modeling and scalable graph processing <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a> <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a> <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.