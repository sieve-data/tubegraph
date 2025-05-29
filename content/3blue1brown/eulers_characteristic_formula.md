---
title: Eulers characteristic formula
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

[[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's characteristic formula]] is a fundamental concept in graph theory and topology, providing a powerful tool for understanding the structure of graphs and polyhedra <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.

## Definition and Application to Planar Graphs

In the context of graph theory, a graph is a diagram composed of nodes (vertices) and lines (edges) connecting them <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. A **planar graph** is one that can be drawn without any of its lines intersecting each other <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

For any connected planar graph, the relationship between its vertices (V), edges (E), and faces (F, or regions) is given by the formula:
<a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>
> V - E + F = 2

Here, F includes all regions the graph divides the plane into, including the infinite outer region <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>. This formula holds true regardless of the specific planar graph chosen <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.

Historically, the equation originally described the vertices, edges, and faces of three-dimensional polyhedra <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

## Proof and Explanation

The validity of [[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's characteristic formula]] can be understood by considering how a graph is built up <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>:

1.  **Trivial Case**: Start with a single node (vertex) and no edges <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>. In this case, V=1, E=0, and F=1 (for the infinite outer region), satisfying V - E + F = 1 - 0 + 1 = 2 <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.
2.  **Building Edges**:
    *   **Adding a new vertex**: If a new edge is introduced that also creates a new vertex (i.e., connecting to a previously isolated point), V increases by 1 and E increases by 1 <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>. The equation V - E + F remains balanced <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.
    *   **Connecting to an existing vertex**: If a new edge connects to pre-existing vertices, it does not add a new vertex but encloses a new region of space <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. In this scenario, E increases by 1 and F also increases by 1, again leaving the equation balanced <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

As a graph is incrementally constructed through these methods, the value of V - E + F consistently remains fixed at 2 <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

## Application in Moser's Circle Problem

[[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's characteristic formula]] provides a critical tool for solving Moser's circle problem, which asks for the number of regions created by connecting points on a circle <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.

### Adapting the Formula
While Moser's circle problem involves intersecting lines (making it not a planar graph in its initial form), the key insight is to treat every intersection point within the circle as a new vertex <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>. This transforms the diagram into a planar graph suitable for [[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's formula]] <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.

To count only the regions *inside* the circle, the formula is slightly modified from V - E + F = 2 to F = E - V + 1, effectively removing the infinite outer region from the count <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

### Calculating Vertices and Edges for Moser's Circle Problem
For 'n' points on the circle, the total number of vertices (V) and edges (E) needed for the adapted formula are:

*   **Vertices (V)**: This includes the 'n' original points on the circle plus all the internal intersection points <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>. The number of intersection points is given by 'n choose 4' (C(n,4)) <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
    *   V = n + C(n,4) <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>
*   **Edges (E)**: This includes the initial chords and the arcs on the circle's circumference <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. Each internal intersection point divides what were originally two chords into four segments, effectively adding two new edges <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.
    *   Number of chords: C(n,2) <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>
    *   Additional edges from intersections: 2 * C(n,4) <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>
    *   Arcs on the circle: n <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>
    *   E = C(n,2) + 2 * C(n,4) + n <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>

### Final Formula for Regions
By substituting these expressions for V and E into the adapted [[eulers_characteristic_formula_and_its_application_to_planar_graphs | Euler's formula]] (F = E - V + 1), many terms cancel out <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. The resulting formula for the number of regions within the circle is:
<a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>
> Regions = 1 + C(n,2) + C(n,4)

This formula provides an exact solution to Moser's circle problem, explaining why the initial sequence appears to be powers of two before breaking <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.