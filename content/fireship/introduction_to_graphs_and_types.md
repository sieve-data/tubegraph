---
title: Introduction to Graphs and Types
videoId: cWNEl4HE2OE
---

From: [[fireship]] <br/> 

A graph is a nonlinear [[data_structures_and_algorithms | data structure]] that consists of nodes and edges <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

*   **Node (or Vertex)**: A single, unique value <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.
*   **Edge**: Represents a connection or relationship between two nodes <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Types of Graphs

Graphs can be categorized based on the nature of their edges:

*   **Directed Graph**: The relationship between nodes flows in one direction <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. An example is Instagram, where following a user creates a directed edge from the follower to the followed user, but not necessarily vice-versa <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   **Undirected Graph**: The relationship between nodes goes both ways <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. An example is Facebook friendships, where being friends implies a mutual connection <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Weighted Graph**: A node has additional data about the relationship, such as the distance between two airports <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For instance, an edge representing a flight route might include the kilometers between airports <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Cycle**: Occurs when a node points back to itself, like an airplane taking off and landing at the same airport <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## [[applications_of_graphs_in_software | Applications of Graphs in Software]]

Graphs are widely used in real-life software products <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Common applications include:

*   **Social Networks**: Representing user connections (e.g., Facebook's social graph) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Recommendation Engines**: Connecting businesses to users and reviews (e.g., Yelp) or movies watched to movies a user might want to watch (e.g., Netflix) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Geographic Data**: Representing intersections as nodes and roads (with distances) as edges (e.g., Google Maps) <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Flight Connections**: Airports as nodes and flight routes as edges, potentially weighted with distances <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## [[graph_representation_techniques | Graph Representation Techniques]]

In technical interviews, you will often be asked to represent a graph in code <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Two common ways are:

### Adjacency Matrix
A 2D array where each row and column represents a node <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   If two nodes have a connection, a '1' is added at their intersection; otherwise, it's '0' <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Pros**: Fast and easy to look up or add a specific edge <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Generally easier to visualize <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Cons**: Takes quadratic space complexity (O(V^2), where V is the number of vertices) <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Quadratic time to insert a new node <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Can be very sparse (filled with zeros) and less efficient to iterate over if there are few edges relative to nodes <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Adjacency List
A collection of nodes, where each node has its own list (or array) of its neighbors <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   Can be implemented as a set of key-value pairs, where the key is the node name and the value is an array of connected nodes (edges) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   In JavaScript, a `Map` is often preferred over a regular `Object` for algorithm problems due to its additional API methods and hash map-like behavior <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Pros**: Faster to iterate over a node's edges <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. More memory efficient, especially when there are many nodes but few edges <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Basic API for building an adjacency list**:
    *   `addNode(node_code)`: Adds a node to the map with an empty array for its connections <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   `addEdge(origin, destination)`: Updates both the origin and destination nodes' lists to include each other (for undirected graphs) <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## [[graph_traversal_algorithms | Graph Traversal Algorithms]]

When working with graphs, you'll often need to traverse them. Two main ways to approach this are:

### Depth-First Search (DFS)
*   **How it works**: Starts at a random node, goes to its first child, then its first child, and continues as deep as possible <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. When there are no more children, it backtracks to the last node and continues the process <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Implementation**: Usually implemented with a recursive function <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **Tracking Visited Nodes**: A `Set` is used to keep track of visited nodes to prevent infinite loops and re-visiting <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Use Case**: More efficient for finding *any* route quickly, rather than all possible routes <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Breadth-First Search (BFS)
*   **How it works**: From the starting node, it adds all direct children to a queue <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Once they've been visited, it moves on to their children (grandchildren) and continues following this pattern in layers <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Implementation**: Uses a queue (which can be a JavaScript array where items are added to the end and removed from the beginning using `shift()`) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **Tracking Visited Nodes**: A `Set` is used to store visited airports to avoid re-visiting nodes and prevent infinite loops, ensuring each airport is enqueued only if it hasn't been visited yet <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Use Case**: Good for finding all possible routes or the shortest path, as it explores layer by layer <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Time Complexity (Big O Notation)

For both Breadth-First Search (BFS) and Depth-First Search (DFS), the time complexity is expressed as **O(V + E)** <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **V**: The total number of nodes (vertices) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **E**: The number of edges <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

This means the performance of these algorithms will scale linearly based on the number of nodes and edges added to the graph <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## [[implementing_graph_algorithms_in_javascript | Implementing Graph Algorithms in JavaScript]]

When implementing graph algorithms in an interview setting, it's crucial to explain your thinking process <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Technical interviewers prioritize insight into your thought process over perfectly formatted code <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.