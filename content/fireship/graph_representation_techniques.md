---
title: Graph Representation Techniques
videoId: cWNEl4HE2OE
---

From: [[fireship]] <br/> 

A [[introduction_to_graphs_and_types|graph]] is a non-linear [[data_structures_and_algorithms|data structure]] that contains nodes and edges <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A node, also known as a vertex, is a single unique value <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, while an edge represents a connection or relationship between two nodes <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Types of Graphs

Graphs can be categorized based on the nature of their edges and nodes:

*   **Directed Graph**
    *   The relationship flows one way <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
    *   **Example**: Instagram, where following a user creates an edge from the follower to the followed, but not vice-versa <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   **Undirected Graph**
    *   The relationship goes both ways <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
    *   **Example**: Facebook friendships, where if one person is friends with another, the relationship is mutual <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Weighted Graph**
    *   The edge has additional data about the relationship <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
    *   **Example**: The distance between two airports <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Cycle**
    *   A node points back to itself <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   **Example**: An airplane taking off and landing at the same airport <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Real-world [[applications_of_graphs_in_software|Applications of Graphs]] in Software

[[introduction_to_graphs_and_types|Graphs]] are used in many real-life software products <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>, and knowledge of them is often tested in technical interviews <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

Common [[applications_of_graphs_in_software|applications of graphs]] include:
*   **Social Graphs**: Representing connections between users, like Facebook's social graph <a class="yt-timestamp" data-t="02:08:08">[02:08:08]</a>.
*   **Recommendation Engines**: Connecting businesses to users and reviews (e.g., Yelp), or connecting movies watched to potential future watches (e.g., Netflix) <a class="yt-timestamp" data-t="02:12:08">[02:12:08]</a>.
*   **Geographic Data**: Representing intersections as nodes and roads as edges with distances on maps (e.g., Google Maps) <a class="yt-timestamp" data-t="02:22:06">[02:22:06]</a>.
*   **Flight Connections**: Airports as nodes, and routes between them as edges <a class="yt-timestamp" data-t="02:35:05">[02:35:05]</a>.

## Representing Graphs in Code

When representing a [[introduction_to_graphs_and_types|graph]] in code, two primary methods are commonly used:

### Adjacency Matrix

An adjacency matrix uses a 2D array to represent a [[introduction_to_graphs_and_types|graph]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Structure**: One row and one column are created for every node <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. If two nodes have an edge, a `1` is added at their intersection point; otherwise, it's `0` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Pros**:
    *   Fast and easy to look up a specific edge or add a new one <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   Generally easier to visualize <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
*   **Cons**:
    *   Requires quadratic space complexity ($O(V^2)$ where V is the number of vertices) <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
    *   Takes quadratic time to insert a new node <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   Can be "sparse" (filled with many zeros) and take up unnecessary space if there are few routes relative to possible combinations <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

### Adjacency List

An adjacency list starts with a collection of nodes, where each node has its own array of its neighbors <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Pros**:
    *   Faster to iterate over a node's edges <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   More efficient with memory, especially when there are many nodes but few edges <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

#### Implementing an Adjacency List in JavaScript

An adjacency list can be implemented as a set of key-value pairs <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. The key is the node's name (e.g., airport name), and the value is an array of edges (other connected nodes) <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

While a regular JavaScript object can be used, a `Map` is often a better option for [[data_structures_and_algorithms|algorithm]] problems due to its additional API methods and behavior resembling a dictionary or hash map found in other languages <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

Here's how to build a basic [[introduction_to_graphs_and_types|graph]] API using a JavaScript Map:

1.  **Initialize the Graph**:
    ```javascript
    const adjacencyList = new Map(); // Represents the graph
    ```
2.  **Add a Node**: A function to add a new node to the map.
    ```javascript
    function addNode(airportCode) {
        adjacencyList.set(airportCode, []); // Node with an empty array for its edges
    }
    ```
    This function takes the airport code as an argument and initializes it with an empty array of connections <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
3.  **Add an Edge**: A function to connect two nodes. For an undirected [[introduction_to_graphs_and_types|graph]], the connection must be added both ways.
    ```javascript
    function addEdge(origin, destination) {
        adjacencyList.get(origin).push(destination); // Add destination to origin's list
        adjacencyList.get(destination).push(origin); // Add origin to destination's list
    }
    ```
    This involves grabbing the entry for the origin airport and pushing the destination onto its list, then doing the inverse for the destination airport <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

## Graph Traversal Algorithms

Once a [[introduction_to_graphs_and_types|graph]] is represented, it can be traversed to find paths or visit all nodes. Two common [[graph_traversal_algorithms|graph traversal algorithms]] are Depth-First Search (DFS) and Breadth-First Search (BFS).

### Breadth-First Search (BFS)

BFS explores the [[introduction_to_graphs_and_types|graph]] layer by layer <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It starts from a node, visits all its direct children, then all their children, and so on <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>.
*   **Mechanism**: Typically implemented using a queue [[data_structures_and_algorithms|data structure]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The starting node is added to the queue <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>. While the queue is not empty, the first item is dequeued, its neighbors are visited and enqueued (if not already visited), and the process continues <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>.
*   **Avoiding Loops**: A `Set` is used to keep track of visited nodes to prevent infinite loops in interconnected graphs <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.
*   **Use Case**: Ideal for finding the shortest path or all possible routes between two nodes <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.

### Depth-First Search (DFS)

DFS explores as deeply as possible along each branch before backtracking <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. It starts at a node, goes to its first child, then its first child's first child, and so on, until no more children are available <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Then, it backtracks and repeats the process <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Mechanism**: Usually implemented with a recursive function <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>. The function calls itself with the current destination and a set of visited nodes <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
*   **Use Case**: More efficient for finding *if* a route exists quickly, rather than all possible routes <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.

### Time Complexity

For both [[graph_traversal_algorithms|Breadth-First Search]] and [[graph_traversal_algorithms|Depth-First Search]], the time complexity is expressed as **Big O of V plus E ($O(V + E)$)** <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>, where V is the total number of nodes (vertices) and E is the number of edges <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>. This means the performance scales linearly with the number of nodes and edges in the [[introduction_to_graphs_and_types|graph]] <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.