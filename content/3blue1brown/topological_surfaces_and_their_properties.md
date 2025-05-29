---
title: Topological surfaces and their properties
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

## The Utilities Puzzle

The Utilities Puzzle challenges participants to connect three distinct houses to three different utilities (gas, power, and water) [01:01:00]. The goal is to draw a total of nine lines—one from each utility to each house—without any two lines crossing [01:05:05]. When attempted on a flat piece of paper, this puzzle "doesn't even sound possible" to many [01:25:05]. Initial attempts often lead to lines blocking access to houses, making it appear that no solution exists [02:37:00] [02:53:00].

## Impossibility on a Planar Surface

For a mathematician, a seemingly impossible puzzle prompts a "meta-puzzle" to prove its impossibility [05:02:00]. This particular challenge delves into [[planar_graphs_and_graph_theory | graph theory]], a branch of mathematics dealing with objects (vertices) and their connections (edges) [05:20:00].

The Utilities Puzzle can be represented as a graph, specifically a complete bipartite graph, K3-3 [05:52:00]. A graph is considered a [[planar_graphs_and_graph_theory | planar graph]] if it can be drawn on a plane without any edges crossing [05:43:00].

### Why the Puzzle is Impossible on a Plane

When drawing lines for the Utilities Puzzle on a plane, a crucial observation is made about enclosed regions: once an area is enclosed, no new line can enter or exit it without crossing an existing line [06:25:00] [06:36:00].

A key mathematical principle emerges: each new edge drawn in a graph either increases the number of connected vertices or increases the number of enclosed regions [08:06:00] [11:15:00].

*   The Utilities Puzzle has 6 vertices (3 houses, 3 utilities) [08:36:00].
*   It requires 9 edges (lines) [08:36:00].
*   Starting with one lit node and one region (the entire 2D plane) [08:31:00], five of the nine lines are used to light up the initially dim vertices [08:43:00].
*   The remaining four lines must, therefore, introduce new regions [08:59:00].
*   This implies that a hypothetical solution on a plane would cut the plane into five separate regions (the initial region plus four new ones) [09:13:00].

Furthermore, in this specific bipartite graph (K3-3), any cycle (a closed loop of edges) must consist of at least four edges [09:32:00]. This is because a cycle must alternate between houses and utilities, preventing shorter loops [09:37:00] [09:44:00].

Combining these facts:
*   A solution would create 5 regions [09:13:00].
*   Each region must be bounded by at least 4 edges [09:59:00].
*   If each of the 5 regions had at least 4 edges, summing the edges for all regions would give at least 5 * 4 = 20 edges [10:21:00].
*   Since each edge is part of exactly two regions, this sum double-counts the total edges [10:33:00].
*   Therefore, a planar solution would require at least 20 / 2 = 10 edges [10:41:00].
*   However, the Utilities Puzzle only has 9 edges [10:50:00].

> [!TIP] The proof:
>
> 5 regions * 4 (minimum) edges/region = 20 total boundary edges.
> Each edge borders 2 regions, so 20 / 2 = 10 unique edges required.
> The puzzle only has 9 edges.
> Thus, it is impossible to solve on a plane without lines crossing [11:01:00].

### Euler's Characteristic Formula

The reasoning used to prove the puzzle's impossibility on a plane leads to a fundamental mathematical truth for any [[planar_graphs_and_graph_theory | planar graph]]: the number of vertices (V) minus the number of edges (E) plus the number of regions (F/R) remains constant, always equaling two (V - E + R = 2) [11:35:00] [11:44:00] [11:48:00]. This relation is known as Euler's characteristic formula [11:51:00]. Historically, it first appeared in the context of convex polyhedra (like a cube), where vertices, edges, and faces (instead of regions) sum to two [11:54:00].

## Solving the Puzzle on a Mug

The puzzle becomes solvable when presented on a mug rather than a flat piece of paper [12:16:00]. The key lies in the mug's handle [12:21:00] [12:36:00].

> [!NOTE] [[Introduction to topology | Topology]]:
> Famously, a mug is [[Topology and its significance | topologically]] equivalent to a donut (a torus) [12:59:00] [13:05:00]. The handle provides the necessary "torusiness" for the solution [13:10:00] [13:13:00].

The handle acts as a bridge, allowing lines to cross over or under each other without intersecting on the main surface of the mug [13:30:00] [13:42:00] [13:57:00] [14:14:00] [16:30:00]. This means a line can be routed "around the mug" [03:42:00] or "underneath the handle" [03:48:00], effectively navigating around existing connections [13:45:00]. One strategy is to draw as many lines as possible on the main surface until a crossing is unavoidable, then use the handle to bypass it [13:38:00] [13:55:00].

The ability to use the mug's handle fundamentally changes the [[geometric_reasoning_and_sphere_surface_area | geometric]] properties of the surface, allowing for connections that would be impossible on a flat plane [13:02:00]. This highlights a core concept in [[introduction_to_topology | topology]]: the properties of shapes that remain unchanged under continuous deformation.

## The Mathematical Implication

The success of the puzzle on a mug, despite its impossibility on a plane, raises a profound mathematical question: Where exactly does the proof of impossibility (derived from Euler's characteristic formula) break down on the surface of a mug? [16:35:00] [16:42:00].

The answer is not simply that "Euler's formula is different on surfaces with a hole" [16:54:00]. Thinking through the specific line of reasoning, particularly the definition of regions and how edges create them, reveals how the presence of a hole (like the mug's handle) alters the underlying assumptions of the planar graph proof [16:58:00]. This deeper reflection enhances one's understanding of [[introduction_to_topology | topology]] and its implications for [[geometric_reasoning_in_higher_dimensions | geometric reasoning]] [17:04:00].