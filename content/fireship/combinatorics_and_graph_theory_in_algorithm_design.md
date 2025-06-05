---
title: Combinatorics and graph theory in algorithm design
videoId: bOCHTHkBoAs
---

From: [[fireship]] <br/> 

When discussing structures with a finite number of elements, we enter the realm of [[Programming Concepts and Paradigms | discrete math]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This is distinct from continuous math, like geometry and calculus, which deal with real numbers and approximations <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. [[data_structures_and_algorithms | Algorithms]] often rely on concepts from [[Programming Concepts and Paradigms | discrete math]] to solve problems efficiently.

## Combinatorics

[[Programming Concepts and Paradigms | Combinatorics]] is essentially the study of counting things <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, especially when combining sets into combinations or permutations <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Applications in Algorithm Design
*   **Counting possibilities**: In applications like Tinder, [[Programming Concepts and Paradigms | combinatorics]] might be used to count all possible combinations of matches as part of a more complex [[data_structures_and_algorithms | algorithm]] that determines what to display to the user <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Database partitioning**: For globally distributed databases, [[Programming Concepts and Paradigms | combinatorics]] can help in figuring out the number of database partitions needed worldwide <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Pattern understanding**: Ultimately, [[Programming Concepts and Paradigms | combinatorics]] is about understanding how patterns can emerge <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Fibonacci Sequence**: The Fibonacci sequence is an example where a function can be written to generate it <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   **Google Maps**: Engineers at Google use [[Programming Concepts and Paradigms | combinatorics]]-like logic to render tiles on tools such as Google Maps <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Graph Theory

[[Programming Concepts and Paradigms | Graph theory]] is closely related to [[Programming Concepts and Paradigms | combinatorics]] <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. A graph consists of two fundamental parts:
*   **Nodes (or vertices)**: These are the individual points in a graph <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Edges**: These are connections that link nodes together <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

For instance, a person could be a node, and a relationship connecting two people could be an edge <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Types of Graphs
*   **Undirected Graph**: A relationship that goes both ways, such as mutual love between a person and their mother, creates an undirected graph <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Directed Graph**: A relationship that only goes one way, like loving an OnlyFans girlfriend without reciprocation, forms a directed graph <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Weighted Edges**: Edges can also be weighted, meaning one relationship might be more important than another <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **Cyclic vs. Acyclic**: If a node can traverse back to itself, the graph is considered cyclic; otherwise, it's acyclic <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Graph Algorithms
As a programmer, you will often need to build graphs from scratch and, more importantly, know how to traverse them <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Dijkstra's Algorithm**: This [[data_structures_and_algorithms | algorithm]] is used to find the most efficient way to navigate through a network, similar to finding the best route through traffic <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Complexity Theory**: Before implementing [[data_structures_and_algorithms | graph traversal algorithms]], understanding [[data_structures_and_algorithms | complexity theory]] is crucial. This theory, often expressed using Big O notation, indicates how much time and memory an [[data_structures_and_algorithms | algorithm]] is expected to use <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. For example, [[Logarithms and logarithmic functions in algorithms | logarithmic time]] is achieved by sophisticated [[data_structures_and_algorithms | algorithms]] like [[data_structures_and_algorithms | binary search]], which cut the search area in half after each iteration <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Understanding [[data_structures_and_algorithms | complexity]] is essential for [[common_coding_interview_questions | technical interviews]] <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.