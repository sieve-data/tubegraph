---
title: Eulers characteristic formula
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

[[eulers_formula | Euler's characteristic formula]] is a significant concept in graph theory and topology, initially describing properties of three-dimensional polyhedra. It establishes a fundamental relationship between the number of vertices, edges, and faces (regions) of a graph.

## Definition and Application to Planar Graphs
In the context of planar graphs, which are diagrams where lines (edges) do not intersect each other except at nodes (vertices) <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>, [[eulers_formula | Euler's characteristic formula]] states a remarkable constant relationship:

<a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>
> `V - E + F = 2`

Where:
*   `V` (Vertices) is the total number of nodes in the graph <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.
*   `E` (Edges) is the total number of lines connecting the nodes <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>.
*   `F` (Faces) is the total number of regions (or faces) that the graph divides the plane into, including the infinite outer region <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.

This formula consistently yields 2, regardless of the planar graph chosen <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. Originally, the equation was used to describe the vertices, edges, and faces of three-dimensional polyhedra <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

## Proof Sketch
The consistency of [[eulers_formula | Euler's characteristic formula]] can be intuitively understood by considering how a graph is built up incrementally <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>:

1.  **Starting Case**: Begin with a trivial graph consisting of a single node and no edges.
    *   `V = 1`, `E = 0`, `F = 1` (due to the infinite outer region) <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.
    *   Plugging these into the formula: `1 - 0 + 1 = 2`, which is true <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.

2.  **Adding Edges**: Consider adding edges to the graph one at a time <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>:
    *   **New Edge, New Vertex**: If a new edge introduces a new vertex (e.g., extending a line), `E` increases by one, and `V` also increases by one <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>. The change to the formula is `(+1) - (+1) + 0`, which keeps the equation balanced <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.
    *   **New Edge, Existing Vertices**: If a new edge connects to pre-existing vertices, it does not add a new vertex but encloses a new region of space <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. In this case, `E` increases by one, and `F` also increases by one <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>. The change to the formula is `0 - (+1) + (+1)`, which again keeps the equation balanced <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

Through this incremental process, the value of `V - E + F` always remains fixed at 2 <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

## Application to Moser's Circle Problem
[[eulers_formula | Euler's characteristic formula]] can be adapted to count the number of regions formed by chords within a circle, as seen in Moser's Circle Problem <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.

For this problem, the formula is rearranged to solve for `F` (number of regions):
`F = E - V + 2` <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>

However, since the problem is concerned only with the regions *inside* the circle (excluding the infinite outer region), the formula is adjusted to:
`F_internal = E - V + 1` <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>

To apply this to the circle problem, the intersecting chords must be treated as forming a *new* planar graph where:
1.  **Vertices (`V`)**: Include the original `n` points on the circle's boundary AND all the intersection points within the circle <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.
    *   The number of intersection points is given by "n choose 4" (the number of ways to choose 4 points from `n` original points, as each set of 4 points uniquely defines one intersection) <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
    *   So, `V = n + (n choose 4)` <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

2.  **Edges (`E`)**: Include all the segments of the chords that are created by the intersection points, plus the arcs along the circle's perimeter <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
    *   Each intersection point effectively adds two new edges (by splitting two original lines into four) <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
    *   The total number of original chords is "n choose 2" (number of ways to choose 2 points from `n` original points) <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
    *   There are also `n` arcs on the outside of the diagram <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.
    *   So, `E = (n choose 2) + 2 * (n choose 4) + n` <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.

By substituting these expressions for `V` and `E` into the adjusted [[eulers_formula | Euler's formula]] (`F_internal = E - V + 1`), many terms cancel out <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>, yielding the final formula for the number of regions in Moser's Circle Problem:

<a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>
> `F_internal = 1 + (n choose 2) + (n choose 4)`