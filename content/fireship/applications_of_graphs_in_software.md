---
title: Applications of Graphs in Software
videoId: cWNEl4HE2OE
---

From: [[fireship]] <br/> 
A [[introduction_to_graphs_and_types | graph]] is a nonlinear [[data_structures_and_algorithms | data structure]] that contains nodes and edges <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A node (or vertex) is a single unique value, while an edge represents a connection or relationship between two nodes <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. [[introduction_to_graphs_and_types | Graphs]] are utilized in many real-life [[programming_software | software]] products <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, and developers will encounter various implementations of [[introduction_to_graphs_and_types | graphs]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Social Networks
Social media platforms are a common application of [[introduction_to_graphs_and_types | graphs]]:
*   **Instagram** Every user can be considered a node, and when a user follows another, an edge is created connecting two nodes <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This represents a [[introduction_to_graphs_and_types | directed graph]] because the relationship flows one way (follower follows the following, not vice-versa) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Facebook** Friendships form the edges in this type of [[introduction_to_graphs_and_types | graph]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Since friendships go both ways, this is an example of an [[introduction_to_graphs_and_types | undirected graph]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Recommendation Engines
[[introduction_to_graphs_and_types | Graphs]] are commonly used for recommendation engines <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>:
*   **Yelp** Connects businesses to users and reviews <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Netflix** Connects movies a user watches to other movies they might want to watch in the future <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Geographic Data and Navigation
[[introduction_to_graphs_and_types | Graphs]] are also used to represent geographic data <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>:
*   **Google Maps** Every intersection can be considered a node, and every road and its distance acts as an edge connecting these two nodes <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This would be a [[introduction_to_graphs_and_types | weighted graph]] if the edges include data like distance <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Flight Connections
A practical example of [[introduction_to_graphs_and_types | graphs]] is representing flight connections between airports <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Each airport is a node, and an edge indicates whether it's possible to fly from one airport to another <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. The edge could contain additional information, such as the kilometers between the airports, making it a [[introduction_to_graphs_and_types | weighted graph]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Routes can be one-way (a [[introduction_to_graphs_and_types | directed graph]]) or two-way (an [[introduction_to_graphs_and_types | undirected graph]]) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Graph Representation and Traversal
In a [[problemsolving_skills_in_software_development | technical interview]], you'll often be asked to [[graph_representation_techniques | represent a graph]] in code <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Common methods include:
*   [[graph_representation_techniques | Adjacency Matrix]]: A 2D array where rows and columns represent nodes, and a '1' indicates an edge <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. While fast for lookup and adding edges, it has quadratic space and time complexity for node insertion <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   [[graph_representation_techniques | Adjacency List]]: A collection of nodes where each node has its own array of neighbors <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This is faster for iterating over a node's edges and more memory-efficient for sparse graphs <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. An [[graph_representation_techniques | adjacency list]] can be implemented using a Map in JavaScript, where the key is the node name and the value is an array of connected nodes <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

You'll also likely need to [[Graph Traversal Algorithms | traverse your graph]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The two main [[data_structures_and_algorithms | algorithms]] for this are:
*   [[Graph Traversal Algorithms | Depth-First Search (DFS)]]: Starts at a random node, then goes to its first child, then that child's first child, and so on, until it can go no deeper <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. It then backtracks and continues the process <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This is typically implemented with a recursive function <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> and is efficient for finding if a route exists quickly <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   [[Graph Traversal Algorithms | Breadth-First Search (BFS)]]: From a starting node, it adds all direct children to a queue, visits them, then moves on to their children (grandchildren), following this pattern in layers <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It's good for finding all possible routes or the most efficient route <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

Both [[Graph Traversal Algorithms | Breadth-First Search]] and [[Graph Traversal Algorithms | Depth-First Search]] [[data_structures_and_algorithms | algorithms]] have a time complexity of O(V + E), where V is the total number of nodes (vertices) and E is the number of edges <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This means their performance scales linearly with the number of nodes and edges in the [[introduction_to_graphs_and_types | graph]] <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.