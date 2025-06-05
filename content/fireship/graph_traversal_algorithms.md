---
title: Graph Traversal Algorithms
videoId: cWNEl4HE2OE
---

From: [[fireship]] <br/> 

A graph is a non-linear [[data_structures_and_algorithms | data structure]] that contains nodes (or vertices) and edges <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A node is a single unique value, while an edge represents a connection or relationship between two nodes <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## [[introduction_to_graphs_and_types | Types of Graphs]]

Graphs can be categorized based on their edge properties:
*   **Directed Graph** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>: The relationship flows one way. An example is Instagram, where following a user creates a directed edge from follower to following <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   **Undirected Graph** <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>: The relationship goes both ways. Facebook friendships are an example, as the connection is mutual <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Weighted Graph** <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>: Edges contain additional data about the relationship, such as the distance between two airports <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Cycle** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>: A node points back to itself, or a path leads back to a previously visited node <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## [[applications_of_graphs_in_software | Applications of Graphs]]

Graphs are widely used in real-life [[applications_of_graphs_in_software | software products]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Examples include:
*   **Social Graphs**: Facebook's social network connects users <a class="yt-timestamp" data-t="02:08:06">[02:08:06]</a>.
*   **Recommendation Engines**: Yelp connects businesses to users and reviews, and Netflix connects movies you've watched to movies you might want to watch <a class="yt-timestamp" data-t="02:12:08">[02:12:08]</a>.
*   **Geographic Data**: Google Maps represents intersections as nodes and roads as edges with distances <a class="yt-timestamp" data-t="02:22:04">[02:22:04]</a>.

## [[graph_representation_techniques | Graph Representation in Code]]

When representing a graph in code, two common approaches are:

### Adjacency Matrix
An adjacency matrix uses a 2D array where each row and column represents a node <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. If two nodes have an edge, a '1' is placed at their intersection point <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Pros**: Fast and easy to look up a specific edge or add a new one <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Easier to visualize as a 2D array <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
*   **Cons**: Takes quadratic space complexity (O(V^2)) and quadratic time to insert a new node <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Can be very sparse (many zeros) and inefficient with memory, especially for graphs with many nodes and few edges <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

### Adjacency List
An adjacency list represents a graph as a collection of nodes, where each node has its own array of its neighbors <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. In JavaScript, this can be implemented as a Map where the key is the node name and the value is an array of connected edges <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
*   **Pros**: Faster to iterate over a node's edges <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. More memory efficient, especially when there are many nodes and few edges <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Implementation Note**: A JavaScript Map is generally preferred over a regular object for algorithm problems as it behaves more like a hash map and offers additional API methods <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

## Graph Traversal Algorithms

Graph traversal involves visiting every node in a graph. Two primary methods are:

### Breadth-First Search (BFS)
BFS explores the graph layer by layer <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
*   **Concept**: Start at a node, visit all its direct children, then all their children, and so on, level by level <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>.
*   **Implementation in JavaScript**:
    *   Uses a `queue` (implemented as an array) to store nodes to visit. The starting node is added to the queue <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.
    *   A `Set` is used to keep track of `visited` nodes to prevent revisiting the same nodes and avoid infinite loops, especially in interconnected graphs <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.
    *   Nodes are dequeued from the front of the queue (`array.shift()`), their unvisited neighbors are added to the queue and marked as visited <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>, <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.
*   **Use Case**: Ideal for finding all possible routes or determining the most efficient route (e.g., shortest path) between two nodes <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.

### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Concept**: Start at a node, go to its first child, then its first child, and continue as deep as possible <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. When there are no more children, backtrack to the last node and continue <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Implementation in JavaScript**:
    *   Typically implemented with a recursive function <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   The recursive function takes the current node and a `visited` set as arguments <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
    *   It checks if a node has been visited before calling itself recursively on its unvisited neighbors, ensuring the algorithm goes deeper into the graph's branches <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.
*   **Use Case**: More efficient for simply determining if a route exists between two nodes as quickly as possible, without needing to find all possible routes <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.

## Time Complexity (Big O Notation)

For both Breadth-First Search and Depth-First Search algorithms, the time complexity is expressed as O(V + E) <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.
*   **V**: Represents the total number of nodes (vertices) in the graph <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.
*   **E**: Represents the total number of edges in the graph <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.

This means the time performance of these algorithms will scale linearly based on the number of nodes and edges added to the graph <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.

For more detailed implementations, one might explore [[implementing_graph_algorithms_in_javascript | implementing graph algorithms in JavaScript]].