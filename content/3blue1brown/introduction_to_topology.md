---
title: Introduction to topology
videoId: AmgkSdhK4K8
---

From: [[3blue1brown]] <br/> 

## What is Topology?
[[The concept of topology|Topology]] is a field of mathematics that helps in understanding certain shapes and their properties <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. It's about developing tools to solve concrete problems <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

## Early Exposure to Topology
For many, the topic of [[the_concept_of_topology|topology]] is introduced to excite imagination <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Common demonstrations include:
*   **Möbius strip**: Building it from construction paper by twisting a rectangle and gluing its ends <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, revealing it as a surface with just one side <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Coffee mugs and donuts**: [[Understanding and visualizing mathematical concepts in topology|Topologists]] view these as the same thing because each has just one hole <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

These demonstrations often leave the question of "How is this math?" and "How does any of this actually help to solve problems?" <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. However, [[the_concept_of_topology|topology]] becomes more tangible when applied to problems.

## The Inscribed Square Problem
An example that demonstrates the [[role_of_topology_in_solving_mathematical_problems|role of topology in solving mathematical problems]] is the unsolved inscribed square problem <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This problem asks whether, for any closed loop (a line squiggled through space that ends back where it started), you can always find four points on this loop that form a square <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   For a circle, it's easy to find an inscribed square <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   For an ellipse, it's also relatively easy <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
The challenge lies in proving this for *every* possible closed loop, no matter how complex <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Currently, mathematical tools can neither confirm nor deny the existence of a loop without an inscribed square <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## The Inscribed Rectangle Problem
A weaker version of the problem, asking about inscribed rectangles instead of squares, has an elegant solution that highlights the power of [[the_concept_of_topology|topology]] <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Properties of a Rectangle
For any rectangle ABCD, the pair of points AC has the same distance and midpoint as the pair of points BD <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Conversely, if two distinct pairs of points (AC and BD) share a midpoint and have equal distances between them, they form a rectangle <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
The goal is to prove that for any closed loop, it's always possible to find two distinct pairs of points on that loop that share a midpoint and are the same distance apart <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Mapping Pairs of Points to 3D Space
To approach this, a function is defined that takes in pairs of points on the loop and outputs a single point in 3D space, encoding their midpoint and distance <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
1.  Place the closed loop on the xy-plane <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
2.  For a given pair of points on the loop, label their midpoint `m` (on the xy-plane) and their distance `d` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  Plot a point `d` units above `m` in the z-direction <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
Doing this for all possible pairs of points generates a surface in 3D space <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

#### Key Property of the Surface
*   As a pair of points on the loop gets closer, the plotted point gets lower (since its height is `d`) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   The midpoint also gets closer to the loop <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   When the pair of points coincides (e.g., `xx`), the plotted point is exactly on the loop itself <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
This function is [[continuous_mapping_and_its_application_in_topology|continuous]], meaning slight adjustments to the input pair result in only slight adjustments to the output in 3D space <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. The goal is to show this function has a "collision" – two distinct pairs mapping to the same spot in 3D space <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Representing Pairs of Points Topologically
To demonstrate this collision, it's necessary to understand the [[the_concept_of_topology|topological]] representation of pairs of points on a loop <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

#### Ordered Pairs and the Torus
1.  Straighten out the loop by cutting it at one point and deforming it into an interval (e.g., from 0 to 1) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The cut point corresponds to both 0 and 1 <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
2.  Represent ordered pairs of points from this interval using a 1x1 square <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. Each point (x,y) in the square corresponds to a pair of points on the loop <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
3.  To reflect that the endpoints 0 and 1 on the interval represent the same point on the loop, the edges of the square need to be "glued":
    *   The left edge (x=0) is glued to the right edge (x=1) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   The bottom edge (y=0) is glued to the top edge (y=1) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
This process of bending the square into a cylinder and then gluing the ends of the cylinder results in a **torus** (the surface of a doughnut) <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. Every point on this torus corresponds to a unique ordered pair of points on the loop, and vice-versa <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. This association is [[continuous_mapping_and_its_application_in_topology|continuous]] <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

#### Unordered Pairs and the Möbius Strip
For unordered pairs (where AB is the same as BA), we need to account for this symmetry in the unit square representation <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This means points (x,y) and (y,x) must represent the same pair <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
1.  This idea is captured by folding the square over diagonally, gluing points (x,y) to (y,x) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
2.  The diagonal line of this fold represents pairs of points that look like `xx` (a single point listed twice) <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
3.  The remaining edges (bottom and right) must be glued <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This requires a specific orientation, leading to a diagonal cut and a twist before gluing <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
The resulting shape is a **[[the_concept_of_topology|Möbius strip]]** <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. The edge of this [[the_concept_of_topology|Möbius strip]] corresponds to the pairs of points like `xx` <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. This [[the_concept_of_topology|Möbius strip]] is the natural shape for unordered pairs of points on the loop <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

### Proof of the Inscribed Rectangle
Using the [[the_concept_of_topology|Möbius strip]] representation for unordered pairs of points:
1.  The special 3D function (which plots midpoint `m` and distance `d`) can be viewed as a [[continuous_mapping_and_its_application_in_topology|continuous map]] from the [[the_concept_of_topology|Möbius strip]] onto the surface it creates in 3D space <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
2.  When pairs of points on the loop are extremely close, the output of the function is right above the loop <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. For pairs like `xx`, the output is *exactly* on the loop <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
3.  Since the red edge of the [[the_concept_of_topology|Möbius strip]] corresponds to pairs like `xx`, when the [[the_concept_of_topology|Möbius strip]] is mapped onto the surface, its edge must map directly onto the original loop in the xy-plane <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
4.  Crucially, it is [[the_concept_of_topology|topologically]] impossible to glue the edge of a [[the_concept_of_topology|Möbius strip]] to something two-dimensional (like the xy-plane) without forcing the strip to intersect itself <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
5.  If the [[the_concept_of_topology|Möbius strip]] intersects itself during this mapping, it means there are at least two distinct pairs of points on the loop that correspond to the same output on the surface <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
6.  This "collision" implies those two distinct pairs share a common midpoint and are the same distance apart <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>, thus forming a rectangle <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

This proof demonstrates how [[the_concept_of_topology|topology]] provides the framework to reason about abstract properties of shapes and transformations to solve concrete geometric problems <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. Understanding why the [[the_concept_of_topology|Möbius strip]] must self-intersect when its edge is mapped to a plane is a fundamental exercise in developing a rigorous understanding of [[the_concept_of_topology|topology]] <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.