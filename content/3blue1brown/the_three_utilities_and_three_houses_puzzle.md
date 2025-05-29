---
title: The three utilities and three houses puzzle
videoId: VvCytJvd4H0
---

From: [[3blue1brown]] <br/> 

The "three utilities and three houses" puzzle is a classic mathematical problem that challenges participants to connect three houses to three different utilities (gas, power, and water) without any of the connection lines crossing <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. This means drawing nine lines in total, one from each utility to each house <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.

## Initial Attempts and Frustrations

Several content creators, including Matt Parker from Stand Up Maths <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>, Sam from Wendover Productions <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>, James Grime from the Singing Bin Honor channel <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>, Brady from Numberphile <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>, Stephen Welch from Welch Labs <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>, and a representative from Looking Glass Universe <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>, were tasked with solving this [[Puzzles and geometric problemsolving | puzzle]] on a mug, which behaves like a flat surface for most initial attempts <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

Participants quickly discovered the difficulty, finding it seemingly impossible to connect all utilities without lines intersecting <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Common issues included "boxing in" a house, making it impossible to connect to remaining utilities <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. This led many to switch to paper, only to encounter the same fundamental problem <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

## Mathematical Analysis: Planar Graphs

The [[Threedimensional puzzles and fourdimensional insights | puzzle]]'s difficulty on a flat surface can be understood through graph theory <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.

### Graph Theory Fundamentals

*   A graph consists of objects (vertices, represented as dots) and connections between them (edges, represented as lines) <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.
*   In most applications, the way a graph is drawn doesn't matter, only the connections <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>. However, in cases like this [[Puzzles and geometric problemsolving | puzzle]], the drawing itself is crucial <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.
*   A graph is called a **planar graph** if it can be drawn in a plane without any of its edges crossing <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

The three utilities and three houses puzzle represents a specific type of graph called a **complete bipartite graph**, known in lingo as K3-3 <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>. The central question is whether K3-3 is planar <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

### Proof of Impossibility on a Plane

The impossibility of solving the K3-3 [[Threedimensional puzzles and fourdimensional insights | puzzle]] on a flat piece of paper without crossing lines can be proven by analyzing the regions created by drawing lines:

1.  **Region Formation**: When drawing lines for a planar graph, a new region is enclosed every time an edge connects to an already-connected vertex, closing a cycle <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>. Each new edge either increases the number of connected nodes or increases the number of enclosed regions <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
2.  **Number of Regions**: Starting with one lit node and one region (all of 2D space) <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>, the K3-3 puzzle requires drawing nine lines <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>. Five of these lines connect initially dim vertices <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>. Therefore, the remaining four lines must each introduce a new region <a class="yt-timestamp" data-t="08:59:00">[08:59:00]</a>. This means a hypothetical solution would divide the plane into five separate regions <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.
3.  **Edges per Region**: In the K3-3 graph, any cycle (an enclosed region) must have at least four edges <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. This is because to return to a starting house, the path must alternate between houses and utilities, requiring at least four steps (House -> Utility -> House -> Utility -> House) <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
4.  **Contradiction**: If there are five regions, and each region is bounded by at least four edges, then summing the edges for each region would give 5 * 4 = 20 edges <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. Since each edge touches exactly two regions, this sum double counts the total number of edges <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>. Thus, a graph fitting these criteria would require 20 / 2 = 10 total edges <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>. However, the K3-3 puzzle only has nine edges (3 utilities * 3 houses = 9 connections) <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
5.  **Conclusion**: The requirement of 10 edges for five regions (each with at least 4 edges) contradicts the fact that the puzzle only has 9 edges <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. Therefore, it is impossible to solve this [[Threedimensional puzzles and fourdimensional insights | puzzle]] on a flat piece of paper without lines intersecting <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

### Euler's Characteristic Formula

This line of reasoning leads to a general truth for any planar graph, known as **Euler's characteristic formula**: the number of vertices (V) minus the number of edges (E) plus the number of regions (F, or Faces) always equals two (V - E + F = 2) <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>. This formula also applies to convex polyhedra, where faces are equivalent to regions <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

## The Mug's Handle: A Topological Solution

The puzzle is given on a mug for a reason: the handle provides a way to circumvent the planar graph impossibility <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. Topologically, a mug is equivalent to a donut, which is a torus <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>. This "torusiness" allows lines to effectively "hop over" others, avoiding intersections on the visible surface <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>.

Several participants successfully used the handle:
*   By looping a line over the handle <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>.
*   By going under the handle and back around <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>.
*   By drawing lines through the "inside" of the handle <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>.
*   By conceptually "moving" the handle to create another connection point <a class="yt-timestamp" data-t="14:59:00">[14:59:00]</a>.

This makes the puzzle "hard but not impossible" <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>, as the handle acts as a bridge to prevent lines from crossing <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>.

## Mathematical Question: Where the Proof Breaks Down

The core mathematical question is precisely where the proof of impossibility for planar graphs breaks down when applying it to the surface of a mug (a torus) <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>. It is not simply that Euler's formula is different for surfaces with a hole, but understanding the specific step in the reasoning that no longer holds true on a non-planar surface <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>.

## Problem-Solving Philosophy

Engaging with such [[Puzzles and geometric problemsolving | puzzles]] encourages valuable [[problemsolving_styles_using_the_cube_shadow_puzzle | problem solving]] skills. Smart people actively seek out new challenges, ask questions, are not afraid to start over, and embrace moments of failure <a class="yt-timestamp" data-t="17:14:00">[17:14:00]</a>.

For those interested in practicing [[Brilliantorg problemsolving puzzles | problem solving]], platforms like Brilliant.org offer courses and quizzes, such as their "Intro to Problem Solving" course and the "Flipping Pairs" sequence, which build problem-solving instincts <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.