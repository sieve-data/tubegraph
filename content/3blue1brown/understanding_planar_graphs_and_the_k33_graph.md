---
title: Understanding planar graphs and the K33 graph
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

The "Utilities Puzzle" is a classic problem in graph theory that challenges participants to connect three houses to three utilities (gas, power, and water) without any of the connection lines crossing <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This means a total of nine lines must be drawn <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. When attempting this puzzle on a flat surface, such as paper, it quickly becomes apparent that it's difficult, seemingly impossible, to avoid line crossings <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Graph Theory Basics

### Graphs
In mathematics, when you have a set of objects and a defined notion of connection between them, this structure is called a graph <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Graphs are often represented abstractly with dots, known as *vertices*, representing the objects, and lines, known as *edges*, representing the connections <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Typically, the way a graph is drawn does not matter, only the connections between vertices <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Planar Graphs
However, in specific cases, such as the Utilities Puzzle, the way a graph is drawn becomes crucial <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. If a graph can be drawn on a flat surface (the plane) without any of its edges crossing, it is called a *planar graph* <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### The K3-3 Graph (Utilities Puzzle Graph)
The Utilities Puzzle can be formally described as a complete bipartite graph, specifically denoted as K3-3 <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. The question then becomes whether the K3-3 graph is planar <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## Proof of Impossibility on a Plane
It can be proven that the K3-3 graph is impossible to draw on a flat piece of paper without lines crossing <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### The Role of Regions
When drawing lines in a graph, one must pay attention to the regions enclosed <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Once a region is enclosed, no new line can enter or exit it without crossing an existing line <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

A useful problem-solving tactic in such situations is to focus on new constructs introduced, such as these regions <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Edge-Region Relationship
Consider the process of drawing a graph:
*   Each new edge drawn either illuminates an initially dim vertex (by connecting to it) or it closes off a new region <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   In the Utilities Puzzle, there are 6 vertices (3 houses + 3 utilities) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   The puzzle requires 9 edges (lines) to be drawn <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   Initially, there's 1 lit node (vertex) and 1 region (all of 2D space) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   To connect all vertices, 5 edges will be used to light up the initially dim vertices (6 total vertices, minus the starting lit one) <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   The remaining 4 edges (9 total edges - 5 vertex-lighting edges) must each introduce a new region <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   Therefore, a complete solution would divide the plane into 5 separate regions (initial region + 4 new regions) <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### Cycle Lengths
In the K3-3 graph, any cycle (a closed path of edges) must have at least four edges <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This is because if you start at a house, the next line must go to a utility, and the line out of that utility must go to another house. You cannot cycle back to the starting point immediately because you must go to a different utility before returning to the first house <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. Consequently, each region created by the graph is bounded by at least four edges <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>, <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Deducing Impossibility
If there are 5 regions, and each region is bounded by at least 4 edges, then summing the edges for all regions would give 5 regions * 4 edges/region = 20 edge-sides <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Since each edge in the graph touches exactly two regions, this sum of 20 precisely double-counts the total number of edges <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Thus, such a graph would require 20 / 2 = 10 total edges <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. However, the Utilities Puzzle (K3-3) only has 9 edges <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This contradiction proves that it is impossible to solve the puzzle on a flat plane without intersecting lines <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>, <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## Connection to [[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's Characteristic Formula]]
The reasoning used to prove the impossibility of the K3-3 puzzle on a plane leads to a fundamental truth in graph theory known as [[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's characteristic formula]] <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This formula states that for any planar graph, the number of vertices (V) minus the number of edges (E) plus the number of regions (R) always equals 2 (V - E + R = 2) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>, <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

Historically, this formula first appeared in the context of convex polyhedra (like a cube), where the number of vertices minus the number of edges plus the number of faces always equals two <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

## Solving the Puzzle on a Mug
While impossible on a plane, the Utilities Puzzle can be solved on a mug <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>, <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

### Topological Equivalence
A mug, despite its appearance, is topologically equivalent to a donut (a torus) <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. This means that from a topological perspective, they share the same fundamental properties regarding how shapes can be deformed without tearing or gluing.

### The Mug Handle as a Bridge
The key to solving the puzzle on a mug lies in utilizing the mug's handle <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>, <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. The handle acts as a "bridge" or a "hole" that allows lines to pass over or under each other without actually crossing in the plane <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>, <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. By drawing lines around the handle, connections can be made that would otherwise intersect on a flat surface <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>, <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

### Why the Proof Fails on a Torus
The proof of impossibility for planar graphs breaks down when applied to a surface with a hole, like a mug <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This is because the underlying assumptions of [[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's formula]] for planar graphs do not directly apply in the same way to surfaces with different genus (number of holes) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. Understanding where the line of reasoning from the planar graph proof specifically fails on a mug provides deeper insight into the principles of topology and graph theory <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.