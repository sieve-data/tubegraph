---
title: Planar graphs and graph theory
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

The holiday season is a time for bringing people together, and sometimes, for tackling mathematical puzzles <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. A notable puzzle involves connecting utilities to houses without lines crossing <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This challenge serves as an excellent illustration of concepts in [[counting_intersections_in_planar_graphs | graph theory]], particularly concerning planar graphs.

## The Utilities Puzzle: An Introduction to Graph Theory

The puzzle involves three houses and three utilities (gas, power, and water) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The goal is to draw a line from each of the three utilities to each of the three houses, for a total of nine lines, without any two lines crossing <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This setup is known in [[mathematical_functions_and_graphs | graph theory]] as a complete bipartite graph, specifically designated as K3-3 <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### What is a Graph?
In mathematics, any set of objects with a notion of connection between them is called a graph <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Graphs are typically represented abstractly with:
*   **Vertices (nodes):** Dots representing the objects <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Edges (lines):** Lines representing the connections between vertices <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

While often the way a graph is drawn does not matter as much as its connections <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, in peculiar cases like the Utilities Puzzle, how it is drawn is crucial <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Planar Graphs
A graph is considered a [[counting_intersections_in_planar_graphs | planar graph]] if it can be drawn in a plane without any of its edges crossing <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The central question of the Utilities Puzzle is whether the K3-3 graph is planar <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## Proving Impossibility on a Plane

Trying to solve the Utilities Puzzle on a piece of paper typically leads to frustration because it's impossible to do so without lines crossing <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. Mathematicians approach such seemingly impossible tasks by attempting to prove their impossibility <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Regions in Planar Graphs
When drawing lines for a planar graph, it's important to observe how new regions are enclosed <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Once a region is enclosed, no new line can enter or exit it <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

A useful fact for understanding graph properties is that each new edge drawn in a graph either:
1.  Increases the number of lit-up (connected) nodes by one (if connecting to a previously dim vertex) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
2.  Increases the number of enclosed regions by one (if connecting to an already lit-up vertex, thereby closing a cycle) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

For the K3-3 graph:
*   It starts with one lit node and one region (the entire 2D space) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   There are nine lines (edges) to be drawn <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   Five of these lines will light up the initially dim vertices (three houses and two remaining utilities, as one utility is lit initially) <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   The remaining four lines must introduce new regions <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   Therefore, a hypothetical planar solution to the Utilities Puzzle would cut the plane into five separate regions (initial region + four new regions) <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### Edge Count and Impossibility
In the K3-3 graph, any cycle (a closed loop of edges) must consist of at least four edges <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This is because paths alternate between houses and utilities (e.g., house -> utility -> house -> utility), requiring four steps to return to the starting house <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

Given that a planar solution would create five regions, and each region must be bounded by at least four edges:
*   If you sum the number of edges bounding each of the five regions, you get 5 regions * 4 edges/region = 20 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   Since each edge in a planar graph touches exactly two regions, this sum double-counts the total number of edges <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   Thus, a graph fitting this description would need to have 20 / 2 = 10 total edges <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   However, the Utilities Puzzle (K3-3) only has nine edges (lines) available <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

Because the K3-3 graph has only nine edges, it is impossible for it to cut the plane into five regions where each region is bounded by at least four edges, thereby proving that it cannot be drawn in a plane without crossings <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### Euler's Characteristic Formula
The logic applied to the Utilities Puzzle reveals a general truth applicable to any [[counting_intersections_in_planar_graphs | planar graph]] <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>: the number of vertices (V) minus the number of edges (E) plus the number of regions (R) always remains unchanged and equals two <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This relationship is known as Euler's characteristic formula: V - E + R = 2 <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Historically, this formula also applies to convex polyhedra, where it relates vertices, edges, and faces (V - E + F = 2) <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

## Solving the Puzzle on a Mug: The Role of Topology

While impossible on a flat piece of paper, the puzzle is solvable on a mug <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. The key lies in the mug's handle <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

### Topological Surfaces
A mug is not topologically equivalent to a plane; it is topologically the same as a donut (a torus) <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. The handle provides an extra "dimension" or a way to route lines without crossing on the main surface <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. Lines can go "over the handle" or "underneath the handle," allowing connections that would otherwise cross on a flat plane <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This highlights a crucial concept in [[introduction_to_topology | topology]]: the properties of a surface can change which graphs are planar on it.

The question of where the proof of impossibility breaks down on the surface of a mug (a [[topological_surfaces_and_their_properties | surface with a hole]]) is a deeper mathematical inquiry <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. It invites further exploration into how Euler's formula changes for surfaces with different topological properties <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.