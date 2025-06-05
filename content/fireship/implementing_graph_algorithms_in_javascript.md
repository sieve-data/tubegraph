---
title: Implementing Graph Algorithms in JavaScript
videoId: cWNEl4HE2OE
---

From: [[fireship]] <br/> 

A graph is a nonlinear [[data_structures_and_algorithms | data structure]] consisting of nodes (or vertices) and edges <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A node is a single unique value, while an edge represents a connection or relationship between two nodes <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. [[introduction_to_graphs_and_types | Graphs]] are widely used in real-life software products and are a common topic in technical interviews <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Types of Graphs
*   **Directed Graph**: The relationship flows one way, like following a user on Instagram (the follower follows the following, but not vice-versa) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Undirected Graph**: The relationship goes both ways, such as friendships on Facebook <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Weighted Graph**: Nodes have additional data about the relationship, like the distance between two airports <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Cycle**: A node points to itself, like an airplane taking off and landing at the same airport <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## [[Graph Representation Techniques | Graph Representation in Code]]
Graphs can be represented in code using various techniques. For programming interviews, you'll often need to choose the most efficient method for a given problem <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Adjacency Matrix
An adjacency matrix uses a 2D array, where each row and column represents a node <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. If two nodes have an edge, a `1` is added at their intersection; otherwise, it's `0` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Pros**: Fast and easy to look up a specific edge or add a new edge <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Generally easier to visualize <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Cons**: Takes quadratic space complexity (O(V^2)) and quadratic time to insert a new node <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Can be very sparse (filled with zeros) and inefficient if there are many nodes but few connections <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Adjacency List
An adjacency list represents a graph as a collection of nodes, where each node has its own array of its neighbors <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Pros**: Faster to iterate over a node's edges <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. More memory-efficient, especially when there are many nodes and few edges <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Implementation in JavaScript**: An adjacency list can be implemented as a set of key-value pairs, where the key is the node's name (e.g., airport code) and the value is an array of its connected nodes (edges) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. A `Map` is often preferred over a regular JavaScript object for algorithm problems due to its additional API methods and behavior resembling a dictionary or hash map <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

To build an adjacency list for an undirected, unweighted graph:
1.  Initialize an empty `Map` to serve as the graph <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  **Add Node Function**: Takes an airport code (node) as an argument and adds it to the `Map` with an empty array as its value (for its neighbors) <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
3.  **Add Edge Function**: Takes two airport codes (origin and destination) and updates both entries in the `Map` by pushing the destination onto the origin's list and vice-versa (for an undirected graph) <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## [[Graph Traversal Algorithms | Graph Traversal Algorithms]]
Once a graph is represented, you'll often need to traverse it to find information. Two common algorithms are Breadth-First Search and Depth-First Search <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Breadth-First Search (BFS)
BFS starts at a given node and explores all of its direct children (neighbors) first, then all of their children, and so on, moving in layers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. It's suitable for finding all possible routes or the shortest path <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Implementation Strategy**: Uses a queue (first-in, first-out) to manage the nodes to visit <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
    1.  Initialize a `queue` (e.g., a JavaScript array) with the starting node <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    2.  Initialize a `visited` `Set` to keep track of already visited nodes and prevent infinite loops <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    3.  While the `queue` has items:
        *   Dequeue the first item (e.g., using [[modern_javascript_array_methods | `array.shift()`]]) <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
        *   Get all edges/destinations for the current node from the adjacency list <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
        *   For each destination:
            *   If the destination has not been visited (check with `visited.has()`):
                *   Mark it as visited by adding it to the `visited` `Set` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
                *   Enqueue the destination <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
                *   Check if it's the target node.

### Depth-First Search (DFS)
DFS starts at a given node and explores as far as possible along each branch before backtracking <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. It's more efficient for finding *any* route quickly rather than all routes or the shortest <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Implementation Strategy**: Usually implemented with a recursive function <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    1.  Define a recursive [[functions_and_closures_in_javascript | function]] that takes the current node and a `visited` `Set` as arguments <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    2.  Add the current node to the `visited` `Set`.
    3.  Get all edges/destinations for the current node <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
    4.  For each destination:
        *   If the destination is the target node, return immediately (found the route) <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
        *   If the destination has not been visited:
            *   Recursively call the same function with the destination as the new current node and the updated `visited` `Set` <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Time Complexity
For both Breadth-First Search and Depth-First Search, the time complexity is expressed in Big O notation as O(V + E) <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This means the time performance of the algorithm scales linearly based on the total number of nodes (V) and edges (E) in the graph <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## [[Applications of Graphs in Software | Real-world Applications]]
[[applications_of_graphs_in_software | Graphs]] are used in many real-life software products <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   **Social Networks**: Representing user connections (e.g., Facebook's social graph) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Recommendation Engines**: Connecting businesses to users and reviews (e.g., Yelp) or movies watched to movies a user might want to watch (e.g., Netflix) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Geographic Data**: Representing intersections as nodes and roads (with distances) as edges (e.g., Google Maps) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Flight Connections**: Airports as nodes and flights as edges, potentially with additional data like kilometers for a weighted graph <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.