---
title: Problemsolving strategies in mathematical puzzles
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

## The Utilities Puzzle: K3-3

The "Utilities Puzzle" challenges individuals to connect three distinct houses to three different utilities (gas, power, water) with lines, such that none of the nine total lines cross <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>, <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. Initial attempts often lead to lines crossing or houses becoming "boxed in," making further connections impossible <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>, <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

## Mathematical Problem-Solving Strategies

When a puzzle seems particularly difficult, a key [[problemsolving_strategies_in_mathematics | problem-solving strategy]] is to shift focus to a "meta-puzzle": proving whether the task is impossible <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>, <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

### Graph Theory Concepts

For [[understanding_difficult_math_problems | understanding difficult math problems]] like the Utilities Puzzle, concepts from graph theory are essential <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.
*   **Graph**: A collection of objects (vertices) with connections (edges) between them <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>, <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
*   **Planar Graph**: A graph that can be drawn on a plane without any edges crossing <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>, <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
*   **Complete Bipartite Graph (K3-3)**: The specific graph representation of the Utilities Puzzle, consisting of two sets of three vertices where every vertex in one set is connected to every vertex in the other set <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>, <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

### Proof of Impossibility on a Plane

To prove the impossibility of solving the Utilities Puzzle on a flat plane, one can analyze the regions created by drawing lines <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.

A useful [[problem_solving_strategies_in_mathematics | problem-solving strategy]] is to focus on new constructs, such as the enclosed regions <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>, <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. A key insight is that each new edge drawn either increases the number of "lit-up" nodes by one or increases the number of enclosed regions by one <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>, <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

For the Utilities Puzzle (K3-3), there are six vertices and nine edges <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
*   Starting with one lit-up node and one region (the entire 2D space) <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>, <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.
*   Five lines are needed to light up the remaining five initially dim vertices <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>, <a class="yt-timestamp" data-t="08:59:00">[08:59:00]</a>.
*   The remaining four lines must each introduce a new region <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.
*   Therefore, a hypothetical solution would cut the plane into five separate regions (the initial region plus four new ones) <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>, <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

Furthermore, for a bipartite graph like K3-3, every cycle (enclosed region) must contain at least four edges <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>, <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
*   If there are five regions, and each requires at least four edges to form its boundary, then the total count of edges (summing edges per region) would be 5 x 4 = 20 <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>, <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>, <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.
*   Since each edge borders exactly two regions, this sum double-counts the edges <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>, <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>.
*   Thus, any such graph would need 20 / 2 = 10 total edges <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>, <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.
*   However, the Utilities Puzzle (K3-3) has only nine edges <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>, <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>.

This contradiction proves that the Utilities Puzzle is impossible to solve on a flat piece of paper without lines intersecting <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>, <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.

### Euler's Characteristic Formula

This proof illustrates a general truth known as Euler's characteristic formula for planar graphs: the number of vertices (V) minus the number of edges (E) plus the number of regions (R) always equals 2 (V - E + R = 2) <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>, <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>, <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. Historically, this formula also applies to convex polyhedra, where faces (F) replace regions (V - E + F = 2) <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>, <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>, <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>.

## Solving the Puzzle on a Mug

The puzzle's setup on a mug provides a crucial hint: the handle <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>, <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>. A mug is topologically equivalent to a donut (a torus) <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>, <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>. This means the surface has a hole, which changes the topological properties of the space in which the graph is drawn. The handle acts as a "bridge," allowing lines to pass over or under other connections without technically crossing on the main surface of the mug <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>, <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>, <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>.

This ability to "hop" lines over or under using the handle circumvents the planar graph restriction, making the puzzle solvable <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>, <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>, <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>, <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>. The question of where the mathematical proof of impossibility breaks down on the surface of a mug provides a deeper understanding of [[role_of_topology_in_solving_mathematical_problems | the role of topology in solving mathematical problems]] <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>, <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>, <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>.

## General Problem-Solving Instincts

Engaging with puzzles, even "toy puzzles," builds strong [[problemsolving_strategies_in_mathematics | problem-solving strategies in mathematics]] <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>, <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>. Smart problem solvers actively seek out new challenges, ask new questions, are not afraid to start over, and embrace moments of failure <a class="yt-timestamp" data-t="17:14:00">[17:14:00]</a>, <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>, <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>.