---
title: Eulers formula and mathematical proofs
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

The "utilities puzzle" is a classic mathematical challenge involving three houses and three utilities (gas, power, and water) [00:00:58]. The goal is to draw lines from each of the three utilities to each of the three houses—nine lines in total—without any two lines crossing [00:01:05].

Initially, the puzzle appears to be impossible on a flat surface, with many participants struggling to complete it without lines intersecting [00:02:25, 00:03:22, 00:05:02].

## Proving Impossibility on a Plane

In mathematics, objects with a notion of connection between them are called a "graph" [00:05:20]. A graph is often represented abstractly with dots (vertices) and lines (edges) [00:05:27]. While usually the way a graph is drawn doesn't matter, in some cases, like the utilities puzzle, how it's drawn is the central concern [00:05:34].

A graph that can be drawn on a plane without its edges crossing is called a [[mathematical_insights_and_elegant_solutions | planar graph]] [00:05:43]. The utilities puzzle graph is known as a complete bipartite graph, specifically K3-3 [00:05:52]. The core question is whether K3-3 is planar [00:05:52].

### The Meta-Puzzle: Proving Impossibility
When a puzzle seems difficult, a mathematician might attempt to solve a "meta-puzzle" by proving that the task itself is impossible [00:05:07]. This requires a rigorous [[mathematical_proofs_and_logical_deduction | logical deduction]].

One method involves focusing on "regions" created by drawing lines [00:06:25]. A region is an enclosed area that a "paint bucket tool" would fill [00:06:31]. Once a region is enclosed, no new line can enter or exit it [00:06:36].

Consider the impact of drawing new edges:
*   Each new edge either lights up one more vertex (if connecting to a dim vertex) [00:07:44, 00:08:06].
*   Or, if connecting to an already lit-up vertex, it closes off a new region [00:07:58, 00:08:11].

For the utilities puzzle:
*   You start with one node lit up and one region (all of 2D space) [00:08:31].
*   The puzzle requires drawing nine lines (edges) [00:08:36].
*   Five of these lines are needed to connect to and "light up" the six initial vertices (three houses, three utilities) [00:08:43].
*   The remaining four lines must each introduce a new region [00:08:59].
*   Therefore, a complete solution would cut the plane into five separate regions (the initial region plus four new ones) [00:09:13].

Next, observe the nature of cycles in the K3-3 graph:
*   Every cycle in this graph must have at least four edges [00:09:32]. This is because a line must go from a house to a utility, then to another house, and then back to a utility before returning to the starting house [00:09:37].
*   This implies that each region in a completed puzzle would be bounded by at least four edges [00:09:27].

Combining these facts leads to a contradiction:
*   If there are five regions, and each region is bounded by at least four edges, the total number of "edge-touches" (summing edges per region) would be at least 5 x 4 = 20 [00:10:06, 00:10:21].
*   Since each edge touches exactly two regions, this "20" effectively double-counts the total number of edges in the graph [00:10:33].
*   Thus, a [[mathematical_insights_and_elegant_solutions | planar graph]] with five regions, each touching at least four edges, would require at least 20 / 2 = 10 total edges [00:10:41].
*   However, the utilities puzzle (K3-3) only has nine edges [00:10:50].
*   Since the puzzle requires 10 edges based on the region count, but only has 9, it is impossible to solve on a piece of paper without lines crossing [00:10:55, 00:11:01]. This is considered a "slick proof" [00:11:07].

### Euler's Characteristic Formula
The logic that each new edge introduces either a new vertex or a new enclosed region is a general truth for any [[mathematical_insights_and_elegant_solutions | planar graph]] [00:11:15, 00:11:27]. This leads to [[eulers_characteristic_formula | Euler's characteristic formula]]:

$V - E + R = 2$ <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>
Where:
*   V = Number of Vertices
*   E = Number of Edges
*   R = Number of Regions (or Faces, historically)

This relation holds true for any planar graph and remains unchanged regardless of the graph drawn [00:11:39]. Historically, this formula emerged in the context of convex polyhedra (like a cube), where the number of vertices minus the number of edges plus the number of faces always equals two [00:11:54].

## The Mug Solution: Topology
Despite being impossible on a plane, the puzzle is solvable on a mug [00:12:16]. The key lies in the mug's handle, which provides an extra dimension or "hop" for lines [00:12:42].

> "I mean like famously, a mug is topologically the same as a donut." <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>
> "So to solve this thing, you're gonna have to use the torusiness of the mug. You're gonna have to use the handle somehow." <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>

The handle can be used as a "bridge" to prevent two lines from crossing on the surface [00:13:30, 00:14:03, 00:16:30]. This changes the topological surface on which the graph is drawn. The proof of impossibility for planar graphs breaks down on a surface with a "hole" [00:16:38]. The question of *where* the line of reasoning from the impossibility proof breaks down on the surface of a mug is a deeper mathematical challenge for personal exploration [00:16:47].