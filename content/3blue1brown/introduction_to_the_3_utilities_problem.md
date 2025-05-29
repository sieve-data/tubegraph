---
title: Introduction to the 3 utilities problem
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

The "3 utilities problem" is a classic mathematical puzzle that challenges individuals to connect three houses to three different utilities—gas, power, and water—without any of the connecting lines crossing each other <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This means drawing a total of nine lines, one from each of the three utilities to each of the three houses <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Initial Attempts and Apparent Impossibility

When attempting the puzzle on a flat surface, such as a piece of paper, many individuals find it incredibly challenging, often concluding that it's impossible <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Participants frequently get lines blocked, or "box in" houses, making it impossible to connect all utilities without intersections <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Proving Impossibility on a Plane

For mathematicians, when a puzzle seems difficult, the approach shifts to a "meta-puzzle": proving that the task is impossible <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This requires understanding concepts from [[problem_solving_strategies_in_mathematics | graph theory]]:

*   **Graphs, Vertices, and Edges**: Any set of objects with connections between them is called a graph <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The objects are represented as dots (vertices), and the connections as lines (edges) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. In the utilities puzzle, the houses and utilities are vertices, and the connecting lines are edges.
*   **Planar Graphs**: A graph is considered planar if it can be drawn on a flat surface (a plane) without any of its edges crossing <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The utilities puzzle graph is known as a complete bipartite graph, specifically K3-3 <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. The question is whether K3-3 is planar <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### The Logic of Impossibility

The proof of impossibility relies on understanding the relationship between vertices, edges, and regions formed by drawing the graph:

1.  **Regions**: When drawing lines, each time a new line hits a vertex that already has an edge, it can close off a new region <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
2.  **Edge-Region Relationship**: Each new edge either lights up a new vertex or increases the number of enclosed regions by one <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
3.  **Applying to K3-3**:
    *   There are 6 vertices (3 houses, 3 utilities) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   There are 9 edges (3 utilities x 3 houses) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   To connect all 6 vertices, 5 edges are needed to "light up" all the initially dim vertices <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
    *   The remaining 4 edges must each introduce a new region <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   Starting with 1 region (the entire 2D plane) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, adding 4 new regions means a hypothetical solution would cut the plane into 5 separate regions <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
4.  **Cycle Length**: In the K3-3 graph, any closed loop (cycle) must have at least four edges <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This is because to return to a starting house, one must go to a utility, then another house, then another utility, then back to the first house <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
5.  **Contradiction**: If there are 5 regions, and each region is bounded by at least 4 edges, then the total count of edges (summing edges per region) would be 5 regions * 4 edges/region = 20 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Since each edge touches exactly two regions, this sum double-counts the edges <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Therefore, such a graph would require 20 / 2 = 10 total edges <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. However, the utilities puzzle only has 9 edges <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This contradiction proves that the puzzle is impossible to solve on a flat piece of paper without lines crossing <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### Euler's Characteristic Formula

This reasoning leads to a more general truth known as Euler's characteristic formula for planar graphs: the number of vertices (V) minus the number of edges (E) plus the number of regions (F, for faces) always equals two (V - E + F = 2) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This formula originally arose in the context of convex polyhedra <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

## The Topological Solution: The Mug

The puzzle is *not* impossible when presented on a three-dimensional object like a mug, as the handle provides a crucial element <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. A mug is topologically equivalent to a donut (a torus), not a sphere <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. The handle can be used as a "bridge" to allow lines to cross in three-dimensional space without intersecting on the two-dimensional surface <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. By routing lines around or through the handle, players can successfully connect all utilities to all houses without any lines crossing on the *surface* of the mug <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

The key mathematical question then becomes: where exactly does the proof of impossibility (for graphs on a plane) break down when applied to the surface of a mug? <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a> Thinking through this provides a deeper [[understanding_difficult_math_problems | understanding of mathematics]] <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.

## Embracing Problem Solving

This puzzle exemplifies the value of [[problemsolving_strategies_in_mathematical_puzzles | problem-solving strategies]]: actively seeking new challenges, asking questions, being unafraid to start over, and embracing moments of apparent failure <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. Resources like Brilliant.org offer courses on [[problemsolving_strategies_in_mathematical_puzzles | problem solving]], helping individuals build genuinely good [[mathematical_problemsolving_and_flexibility | problem solving instincts]] through interactive puzzles <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.