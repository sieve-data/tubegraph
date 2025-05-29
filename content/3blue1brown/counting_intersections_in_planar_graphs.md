---
title: Counting intersections in planar graphs
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

In [[graph_theory|graph theory]], a planar graph is a diagram composed of nodes (called vertices) and lines (called edges) connecting them, which can be drawn on a plane without any of the edges intersecting <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This concept is fundamental to understanding how geometric arrangements divide space.

## Euler's Characteristic Formula

A wonderful fact about [[planar_graphs_and_graph_theory|planar graphs]] is summarized by Euler's characteristic formula, which states:

$V - E + F = 2$ <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>

Where:
*   $V$ is the total number of vertices <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>
*   $E$ is the total number of edges <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>
*   $F$ is the number of regions (or faces) that the graph divides the plane into, including the infinite outer region <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

This formula holds true for any [[planar_graphs_and_graph_theory|planar graph]] <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Intuition Behind the Formula

The consistency of Euler's formula can be understood by building up a graph incrementally from a trivial case <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
1.  **Starting point**: A single node with no edges. Here, $V=1$, $E=0$, and $F=1$ (the infinite outer region). The formula $1 - 0 + 1 = 2$ holds <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>, <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>, <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
2.  **Adding an edge and a new vertex**: If a new edge introduces a new vertex (e.g., extending a line), $V$ increases by one, and $E$ increases by one. This keeps the equation balanced ($+1 - 1 + 0 = 0$) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
3.  **Adding an edge between existing vertices**: If a new edge connects two pre-existing vertices, it creates a new enclosed region of space. In this case, $E$ increases by one, and $F$ also increases by one. This also keeps the equation balanced ($0 - 1 + 1 = 0$) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>, <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

Since any [[planar_graphs_and_graph_theory|planar graph]] can be constructed through these operations, the relationship $V - E + F = 2$ always remains fixed <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Applying Euler's Formula to Non-Planar Diagrams

While Euler's formula strictly applies to [[planar_graphs_and_graph_theory|planar graphs]], it can be cleverly used to analyze non-planar diagrams, such as those in Moser's Circle Problem, by re-interpreting intersection points <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>, <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

The key is to treat every intersection point within the diagram as a new vertex <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. This transforms the non-planar diagram into a [[planar_graphs_and_graph_theory|planar graph]] where the lines no longer cross each other.

### Calculating Vertices and Edges in the Modified Graph

Consider a circle with `n` points on its boundary, where all possible chords are drawn. Assuming no three chords intersect at a single point, the number of internal intersection points is given by `n choose 4` (<span class="inline-math">$\binom{n}{4}$</span>) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

1.  **Total Vertices (V)**: The vertices in this new planar graph are the original `n` points on the circle's boundary plus all internal intersection points <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
    $V = n + \binom{n}{4}$ <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>

2.  **Total Edges (E)**: Each intersection point effectively takes two initial lines and chops them into four smaller segments, thus adding two new edges <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>, <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>, <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   The initial number of chords is `n choose 2` (<span class="inline-math">$\binom{n}{2}$</span>) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Each of the $\binom{n}{4}$ intersection points adds 2 more edges to the total derived from chords <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>, <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
    *   Additionally, the `n` arcs along the circle's circumference must be counted as edges <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
    $E = \binom{n}{2} + 2\binom{n}{4} + n$ <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>, <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>

### Deriving the Number of Regions

The number of regions ($F$) can be found by rearranging Euler's formula: $F = E - V + 2$ <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>, <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
For the Moser's circle problem, we are interested in regions *inside* the circle, so we subtract the infinite outer region, resulting in $F_{internal} = E - V + 1$ <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

Plugging in the expressions for $V$ and $E$:
$F_{internal} = \left(\binom{n}{2} + 2\binom{n}{4} + n\right) - \left(n + \binom{n}{4}\right) + 1$ <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>, <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>, <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>

After cancellation (e.g., $n - n = 0$ and $2\binom{n}{4} - \binom{n}{4} = \binom{n}{4}$):
$F_{internal} = 1 + \binom{n}{2} + \binom{n}{4}$ <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>, <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>

This formula provides an exact solution for the number of regions created by connecting `n` points on a circle, and it is a key insight derived from adapting [[planar_graphs_and_graph_theory|planar graph]] principles to a seemingly non-planar problem <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>, <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.