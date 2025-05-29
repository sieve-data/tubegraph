---
title: Eulers characteristic formula and its application to planar graphs
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 
The utilities puzzle, also known as the three houses and three utilities problem, is a classic mathematical challenge that involves connecting three houses to three different utilities (gas, power, and water) without any of the connection lines crossing <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. The puzzle requires a total of nine lines to be drawn <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

## The Puzzle on a Plane
When attempted on a flat piece of paper, the puzzle proves to be impossible <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. This impossibility can be mathematically proven.

### Graph Theory Fundamentals
Anytime there are objects with a notion of connection between them, it's called a graph <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. These objects are represented as dots, called vertices, and the connections as lines, called edges <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

While typically the way a graph is drawn doesn't matter (only the connections), in certain cases, like the utilities puzzle, the drawing itself is critical <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. If a graph can be drawn on a plane without its edges crossing, it is known as a [[understanding_planar_graphs_and_the_k33_graph | planar graph]] <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

The utilities puzzle graph is known as a [[understanding_planar_graphs_and_the_k33_graph | complete bipartite graph, K3-3]] <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>. The central question for solving it on paper is whether this [[understanding_planar_graphs_and_the_k33_graph | K3-3 graph]] is [[understanding_planar_graphs_and_the_k33_graph | planar]] or not <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.

### Proof of Impossibility
The proof of impossibility relies on understanding the relationship between vertices, edges, and regions formed by drawing a [[understanding_planar_graphs_and_the_k33_graph | planar graph]].

1.  **Regions**: When drawing lines, enclosing a new region means that no new line can enter or exit that area <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
2.  **Edge-Region Relationship**: Each new edge drawn either increases the number of "lit up" nodes (connecting to an untouched vertex) or increases the number of enclosed regions (connecting to an already "lit up" vertex) <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
    *   Starting with one lit node and one region (all of 2D space) <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
    *   The puzzle has three houses and three utilities, so there are six vertices in total <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
    *   There are nine lines (edges) to be drawn <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.
    *   Five of these lines will initially "light up" the other five dim vertices (starting with one already lit) <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.
    *   The remaining four lines must then each introduce a new region <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
    *   Therefore, a hypothetical solution to the puzzle on a plane would cut the plane into five separate regions <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.

3.  **Cycles and Edges per Region**: In the utilities puzzle graph (K3-3), any cycle (a closed loop) must have at least four edges <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. This is because a line from a house goes to a utility, then from that utility to another house, and then from that house to another utility before it can return to the starting house <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. Each region, therefore, is bounded by at least four edges <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.

4.  **The Contradiction**:
    *   If there are five regions, and each region is bounded by at least four edges, then multiplying these numbers (5 regions * 4 edges/region) yields 20 <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
    *   This sum overcounts the total number of edges in the graph because each edge touches exactly two regions <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.
    *   Thus, the total number of edges in such a graph would have to be 20 / 2 = 10 edges <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.
    *   However, the utilities puzzle only has nine edges <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
    *   Since 9 is less than 10, it's impossible to cut the plane into five regions where each has at least four edges, thus proving the puzzle's impossibility on a flat surface <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>.

## [[eulers_characteristic_formula | Euler's Characteristic Formula]]
The logic used to prove the puzzle's impossibility on a plane can be generalized into a fundamental mathematical truth for any [[understanding_planar_graphs_and_the_k33_graph | planar graph]]: the number of vertices ($V$) minus the number of edges ($E$) plus the number of regions ($R$) always remains unchanged <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>. This constant value is always two ($V - E + R = 2$) <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>. This relationship is known as [[eulers_characteristic_formula | Euler's characteristic formula]] <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>.

Historically, [[eulers_characteristic_formula | Euler's characteristic formula]] emerged in the context of convex polyhedra (like a cube), where the number of vertices ($V$) minus the number of edges ($E$) plus the number of faces ($F$) always equals two ($V - E + F = 2$) <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

## Solving the Puzzle on a Mug
Despite its impossibility on a flat plane, the utilities puzzle *can* be solved when drawn on the surface of a mug <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.

This is because a mug is topologically equivalent to a donut, also known as a torus <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>. The handle of the mug provides an extra dimension or "bridge" that allows lines to cross over or under each other without intersecting on the surface <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>. By utilizing the handle, lines can be routed around the mug's surface to connect all houses to all utilities without crossing <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. This means the proof of impossibility for [[understanding_planar_graphs_and_the_k33_graph | planar graphs]] breaks down on a surface with a hole, as [[eulers_characteristic_formula | Euler's formula]] itself changes on surfaces with different topological properties <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>.