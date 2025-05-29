---
title: The concept of topology
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

Topology is a field of mathematics concerned with [[continuous_mapping_and_its_application_in_topology | continuous associations]] between objects, and understanding what is or is not possible under those associations <a class="yt-timestamp" data-t="02:26:26">[02:26:26]</a>, <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>. The famous shapes from this field of study, such as the Möbius strip or Klein bottle, are not merely bizarre curiosities but representatives of huge families of shapes that behave similarly under continuous maps <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>, <a class="yt-timestamp" data-t="02:40:40">[02:40:40]</a>.

## Understanding Topology

Topology is often popularly presented as:
*   The study of bizarre shapes, like applying a half-twist to paper to form a Möbius strip <a class="yt-timestamp" data-t="02:12:12">[02:12:12]</a>, <a class="yt-timestamp" data-t="02:17:17">[02:17:17]</a>.
*   "Rubber sheet geometry," where shapes are considered the same if one can be deformed into another without tearing <a class="yt-timestamp" data-t="02:35:35">[02:35:35]</a>, <a class="yt-timestamp" data-t="02:38:38">[02:38:38]</a>.

However, these common notions, while illustrative, do not fully capture what topology is *actually* about, nor do they immediately reveal how these concepts help [[role_of_topology_in_solving_mathematical_problems | solve mathematical problems]] <a class="yt-timestamp" data-t="02:43:43">[02:43:43]</a>, <a class="yt-timestamp" data-t="02:52:52">[02:52:52]</a>, <a class="yt-timestamp" data-t="02:53:53">[02:53:53]</a>. The core idea is that these shapes and their unique properties serve as tools for logic and deduction <a class="yt-timestamp" data-t="02:55:55">[02:55:55]</a>, <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Mathematicians are excited by "bizarre properties and impossibilities" because they act as "fuel for progress" in logical proofs <a class="yt-timestamp" data-t="02:47:47">[02:47:47]</a>, <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>, <a class="yt-timestamp" data-t="02:53:53">[02:53:53]</a>.

### Topological Spaces

A Möbius strip is not defined by any single physical representation but by its mathematical properties; it can be represented in infinitely many ways, including abstractly as the set of all unordered pairs of points on a loop <a class="yt-timestamp" data-t="02:44:44">[02:44:44]</a>, <a class="yt-timestamp" data-t="02:47:47">[02:47:47]</a>, <a class="yt-timestamp" data-t="02:51:51">[02:51:51]</a>. This points to the concept of a "topological space," which is not a particular shape but an infinite family of shapes connected by a notion of equivalence <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>, <a class="yt-timestamp" data-t="02:03:03">[02:03:03]</a>, <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. The formal definition of a topological space is subtle and doesn't immediately shed light on its essence <a class="yt-timestamp" data-t="02:11:11">[02:11:11]</a>, <a class="yt-timestamp" data-t="02:15:15">[02:15:15]</a>.

## Application in Problem Solving: The Inscribed Rectangle Problem

Topology offers a powerful approach to solving problems, as demonstrated by the proof that every closed continuous loop necessarily has an inscribed rectangle.

### The Inscribed Square Problem

The inscribed square problem, originally posed by Otto Toeplitz in 1911, asks whether every possible closed continuous loop necessarily has an inscribed square <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>, <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. This question remains unsolved for all types of curves <a class="yt-timestamp" data-t="02:05:05">[02:05:05]</a>.

### The Inscribed Rectangle Proof

A simpler version of the problem, proving the existence of an inscribed rectangle for any closed continuous loop, has a beautiful proof attributed to Herbert Vaughan <a class="yt-timestamp" data-t="00:38:38">[00:38:38]</a>, <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>, <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. This proof highlights how topological concepts become problem-solving tools <a class="yt-timestamp" data-t="00:58:58">[00:58:58]</a>.

#### Reframing the Problem

Instead of searching for four points that form a rectangle, the problem is reframed as searching for two distinct pairs of points on the loop where the line segments connecting them have the same midpoint and the same length <a class="yt-timestamp" data-t="03:07:07">[03:07:07]</a>, <a class="yt-timestamp" data-t="03:10:10">[03:10:10]</a>. This condition guarantees the formation of a rectangle <a class="yt-timestamp" data-t="03:27:27">[03:27:27]</a>, <a class="yt-timestamp" data-t="03:29:29">[03:29:29]</a>, <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>.

#### Mapping Pairs of Points to 3D Space

To approach this, all possible pairs of points on a loop are considered <a class="yt-timestamp" data-t="03:56:56">[03:56:56]</a>. For each pair, two pieces of information are relevant:
1.  The `xy` coordinates of its midpoint <a class="yt-timestamp" data-t="04:04:04">[04:04:04]</a>, <a class="yt-timestamp" data-t="04:06:06">[04:06:06]</a>.
2.  The distance `d` between the points <a class="yt-timestamp" data-t="04:12:12">[04:12:12]</a>, <a class="yt-timestamp" data-t="04:15:15">[04:15:15]</a>.

These three numbers (`x`, `y`, `d`) can be packaged together as a single point in a three-dimensional space <a class="yt-timestamp" data-t="04:17:17">[04:17:17]</a>, <a class="yt-timestamp" data-t="04:22:22">[04:22:22]</a>, <a class="yt-timestamp" data-t="04:26:26">[04:26:26]</a>. This creates a continuous mapping from pairs of points on the loop to points in 3D space <a class="yt-timestamp" data-t="04:56:56">[04:56:56]</a>, <a class="yt-timestamp" data-t="04:58:58">[04:58:58]</a>, <a class="yt-timestamp" data-t="05:03:03">[05:03:03]</a>. The goal is to prove that this mapping must result in a "collision" or self-intersection, where two distinct pairs of points map to the same output <a class="yt-timestamp" data-t="05:16:16">[05:16:16]</a>, <a class="yt-timestamp" data-t="05:20:20">[05:20:20]</a>. The set of all possible outputs forms a complex surface in 3D space <a class="yt-timestamp" data-t="06:02:02">[06:02:02]</a>, <a class="yt-timestamp" data-t="06:07:07">[06:07:07]</a>.

#### Representing Unordered Pairs of Points

To avoid trivial rectangle solutions (where a pair `a,b` is distinct from `b,a`), the concept of unordered pairs of points is introduced <a class="yt-timestamp" data-t="14:17:17">[14:17:17]</a>, <a class="yt-timestamp" data-t="14:21:21">[14:21:21]</a>. This leads to the construction of another surface that naturally represents these unordered pairs: the Möbius strip <a class="yt-timestamp" data-t="15:54:54">[15:54:54]</a>, <a class="yt-timestamp" data-t="15:58:58">[15:58:58]</a>, <a class="yt-timestamp" data-t="16:03:03">[16:03:03]</a>.

The process involves:
1.  Assigning each point on the loop a number between 0 and 1, with 0 and 1 representing the same point (like snipping and flattening the loop) <a class="yt-timestamp" data-t="10:53:53">[10:53:53]</a>, <a class="yt-timestamp" data-t="10:58:58">[10:58:58]</a>.
2.  Representing pairs of points using a unit square, where `(x,y)` encodes the two points <a class="yt-timestamp" data-t="11:40:40">[11:40:40]</a>, <a class="yt-timestamp" data-t="11:43:43">[11:43:43]</a>.
3.  Gluing the edges of the square to represent the loop's continuity (0 and 1 being the same point), initially forming a torus <a class="yt-timestamp" data-t="12:08:08">[12:08:08]</a>, <a class="yt-timestamp" data-t="12:13:13">[12:13:13]</a>, <a class="yt-timestamp" data-t="12:48:48">[12:48:48]</a>, <a class="yt-timestamp" data-t="12:52:52">[12:52:52]</a>, <a class="yt-timestamp" data-t="13:02:02">[13:02:02]</a>.
4.  Folding the square along its diagonal to identify `(x,y)` with `(y,x)` (representing unordered pairs), transforming the surface into a Möbius strip <a class="yt-timestamp" data-t="14:33:33">[14:33:33]</a>, <a class="yt-timestamp" data-t="14:36:36">[14:36:36]</a>, <a class="yt-timestamp" data-t="14:40:40">[14:40:40]</a>, <a class="yt-timestamp" data-t="15:58:58">[15:58:58]</a>, <a class="yt-timestamp" data-t="16:03:03">[16:03:03]</a>.

#### The Role of the Möbius Strip and Klein Bottle

The proof concludes by demonstrating that the Möbius strip, which represents all unordered pairs of points, must map onto the 3D surface (encoding midpoint and distance data) in a way that causes self-intersection <a class="yt-timestamp" data-t="17:05:05">[17:05:05]</a>, <a class="yt-timestamp" data-t="17:09:09">[17:09:09]</a>. A key constraint is that the edge of the Möbius strip (representing pairs of identical points, `x,x`) must land on the original loop itself, confined to the xy-plane <a class="yt-timestamp" data-t="17:39:39">[17:39:39]</a>, <a class="yt-timestamp" data-t="17:42:42">[17:42:42]</a>, <a class="yt-timestamp" data-t="17:48:48">[17:48:48]</a>.

For the proof, the constructed surface (and its reflection) effectively form a Klein bottle <a class="yt-timestamp" data-t="20:10:10">[20:10:10]</a>, <a class="yt-timestamp" data-t="20:15:15">[20:15:15]</a>, <a class="yt-timestamp" data-t="20:18:18">[20:18:18]</a>, <a class="yt-timestamp" data-t="21:29:29">[21:29:29]</a>, <a class="yt-timestamp" data-t="21:31:31">[21:31:31]</a>. A fundamental property of a Klein bottle is that it cannot be properly represented in three dimensions without self-intersection <a class="yt-timestamp" data-t="21:46:46">[21:46:46]</a>, <a class="yt-timestamp" data-t="21:49:49">[21:49:49]</a>, <a class="yt-timestamp" data-t="21:52:52">[21:52:52]</a>. This impossibility directly implies that the original 3D surface must have a self-intersection, which corresponds to two distinct pairs of points having the same midpoint and distance, thus forming an inscribed rectangle <a class="yt-timestamp" data-t="22:07:07">[22:07:07]</a>, <a class="yt-timestamp" data-t="22:12:12">[22:12:12]</a>, <a class="yt-timestamp" data-t="22:20:20">[22:20:20]</a>. This highlights how topological properties and "impossibilities" are used as logical tools in mathematical proofs <a class="yt-timestamp" data-t="22:01:01">[22:01:01]</a>, <a class="yt-timestamp" data-t="22:04:04">[22:04:04]</a>.

## Extensions to Higher Dimensions

For the inscribed square problem, if one also tracks the angle of the line segment connecting the pair of points, it adds a fourth dimension to the data <a class="yt-timestamp" data-t="22:52:52">[22:52:52]</a>, <a class="yt-timestamp" data-t="22:55:55">[22:55:55]</a>, <a class="yt-timestamp" data-t="22:58:58">[22:58:58]</a>, <a class="yt-timestamp" data-t="23:01:01">[23:01:01]</a>. This leads to considering embeddings of Möbius strips and [[geometry_in_higher_dimensions | Klein bottles into four-dimensional space]] <a class="yt-timestamp" data-t="23:14:14">[23:14:14]</a>, <a class="yt-timestamp" data-t="23:16:16">[23:16:16]</a>, <a class="yt-timestamp" data-t="23:51:51">[23:51:51]</a>. Recent research in 2020 by Joshua Green and Andrew Lobb, for instance, proved that for smooth curves, rectangles of every possible aspect ratio can be found, involving the embedding of topological surfaces into higher-dimensional spaces <a class="yt-timestamp" data-t="23:22:22">[23:22:22]</a>, <a class="yt-timestamp" data-t="23:26:26">[23:26:26]</a>, <a class="yt-timestamp" data-t="23:30:30">[23:30:30]</a>, <a class="yt-timestamp" data-t="23:44:44">[23:44:44]</a>, <a class="yt-timestamp" data-t="23:47:47">[23:47:47]</a>.

The difficulty in solving the inscribed square problem for all curves lies in "rough curves," like fractals, where the limiting behavior of the angle of line segments between points (e.g., tangent lines) is not well-defined <a class="yt-timestamp" data-t="24:57:57">[24:57:57]</a>, <a class="yt-timestamp" data-t="25:02:02">[25:02:02]</a>, <a class="yt-timestamp" data-t="25:05:05">[25:05:05]</a>, <a class="yt-timestamp" data-t="25:10:10">[25:10:10]</a>.

## Conclusion

[[introduction_to_topology | Topology]] provides a framework for [[understanding_and_visualizing_mathematical_concepts_in_topology | visualizing mathematical concepts]] and solving problems by exploring [[continuous_mapping_and_its_application_in_topology | continuous associations]] and their constraints <a class="yt-timestamp" data-t="25:10:10">[25:10:10]</a>, <a class="yt-timestamp" data-t="25:13:13">[25:13:13]</a>. Its emphasis on how shapes behave under continuous transformations reveals underlying structures crucial for logical deduction and mathematical proof <a class="yt-timestamp" data-t="25:22:22">[25:22:22]</a>, <a class="yt-timestamp" data-t="25:26:26">[25:26:26]</a>.