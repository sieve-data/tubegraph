---
title: Topological differences between a mug torus and a plane
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

The "Utilities Puzzle" challenges participants to connect three houses to three utilities (gas, power, water) with nine lines in total, ensuring no two lines cross <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. While seemingly simple, the solvability of this puzzle depends critically on the surface it's attempted on.

## The Puzzle on a Plane: An Impossibility

When attempted on a piece of paper (a flat plane), the utilities puzzle is impossible to solve without lines crossing <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>. This impossibility can be mathematically proven using concepts from [[the_concept_of_topology | topology]] and graph theory.

### Graph Theory Fundamentals
Anytime there are objects with connections between them, this can be represented as a graph <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>. In graph theory, the objects are called *vertices* (dots) and the connections are called *edges* (lines) <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Usually, how a graph is drawn does not matter, only the connections <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>. However, in cases like the utilities puzzle, the drawing matters <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.

A graph that can be drawn on a plane without its edges crossing is called a *planar graph* <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. The utilities puzzle graph is known as a complete bipartite graph, specifically K3-3 <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.

### Proof of Impossibility
To prove its impossibility on a plane, one can reason about the regions created by drawing lines:
1.  **Regions and Edges**: As lines are drawn between homes and utilities, new regions are enclosed <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>. Once a region is enclosed, no new line can enter or exit it <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
2.  **Edge-Region Relationship**: Each new edge drawn either increases the number of "lit up" (connected) nodes by one, or it increases the number of enclosed regions by one <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
3.  **Expected Regions**:
    *   Starting with one lit node and one region (all of 2D space) <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
    *   The puzzle requires drawing nine lines (edges) <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.
    *   Five of these lines will light up the initially dim vertices (three houses, two additional utilities) <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.
    *   Therefore, the remaining four lines must each introduce a new region <a class="yt-timestamp" data-t="08:59:00">[08:59:00]</a>.
    *   A hypothetical solution on a plane would thus cut the plane into five separate regions (initial region + 4 new regions) <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.
4.  **Cycle Length**: In this specific graph (K3-3), any cycle must have at least four edges <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. This is because to return to the starting point, one must alternate between houses and utilities, requiring a path of at least house-utility-house-utility to complete a cycle <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. This implies that each of the five regions must be bounded by at least four edges <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.
5.  **Contradiction**:
    *   If there are five regions, each with a boundary of at least four edges, summing the edges for all regions would give 5 * 4 = 20 <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
    *   Since each edge touches exactly two regions, this sum (20) double counts the total number of edges <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.
    *   Therefore, such a graph would require 20 / 2 = 10 total edges <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.
    *   However, the utilities puzzle only has nine edges (three utilities connected to three houses) <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
    *   The requirement of 10 edges for a planar solution with these properties contradicts the available 9 edges, proving it is impossible to solve the puzzle on a plane without intersecting lines <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

This reasoning leads to [[euler_s_formula | Euler's characteristic formula]], which states that for any planar graph, the number of vertices (V) minus the number of edges (E) plus the number of regions (F/R) remains constant at two (V - E + R = 2) <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>. This formula was historically derived in the context of convex polyhedra <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

## The Puzzle on a Mug: A Solution Through Topology
Unlike a plane, a mug provides a crucial topological feature: its handle <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. Famously, a mug is [[the_concept_of_topology | topologically]] equivalent to a donut (a torus) <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.

The handle acts as a "bridge" or a means to route lines "over" or "underneath" other connections, effectively preventing them from crossing <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>. This allows the puzzle to be solved <a class="yt-timestamp" data-t="13:29:00">[13:29:00]</a>. For example, a line can be drawn over the handle while another goes underneath <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>. This ability to "hop one line over the other" using the handle is key <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>.

### Where the Proof Breaks Down
The proof of impossibility for a planar graph breaks down on the surface of a mug (torus) <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>. This is because [[euler_s_formula | Euler's formula]] is different on surfaces with a hole <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>. The fundamental difference lies in how regions are formed and how edges enclose them, especially when a hole is present, altering the characteristic that led to the planar graph contradiction. While the specific breakdown is left as an exercise for the viewer to foster a deeper [[understanding_and_visualizing_mathematical_concepts_in_topology | understanding of math]] <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>, it highlights the role of topology in solving mathematical problems <a class="yt-timestamp" data-t="17:04:00">[17:04:00]</a>.