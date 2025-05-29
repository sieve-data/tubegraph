---
title: Dandelin spheres in mathematical proofs
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

The proof involving Dandelin spheres is considered a prime example of mathematical beauty and inventiveness, demonstrating how seemingly disparate definitions of geometric shapes can be equivalent <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This proof is particularly effective because it requires minimal background knowledge while still capturing the spirit of progress and cleverness in mathematics <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Defining an Ellipse

To understand the significance of Dandelin spheres, it's helpful to first review the main ways an ellipse can be geometrically defined <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>:

1.  **Stretching a Circle**: An ellipse can be formed by taking a circle and stretching it along one dimension <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This can be visualized by multiplying only the x-coordinates of all points by a special factor <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
2.  **Two Thumbtacks and a String**: This classic construction involves looping a string around two thumbtacks, pulling it taut with a pencil, and tracing a curve while keeping the string taut <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from each point to the two thumbtack points remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. These thumbtack points are known as the *foci* of the ellipse, and this "constant focal sum" property defines an ellipse <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
3.  **Slicing a Cone (Conic Section)**: An ellipse can also be defined by slicing a cone with a plane at an angle smaller than the slope of the cone itself <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The curve formed by the intersection of the plane and the cone is an ellipse, which is why ellipses are often referred to as conic sections <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

Ellipses are a family of curves, ranging from a perfect circle to something infinitely stretched <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Their specific shape is quantified by their *eccentricity*, often thought of as "squishification" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. A circle has an eccentricity of 0, and the more squished an ellipse is, the closer its eccentricity is to 1 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. For example, Earth's orbit has an eccentricity of 0.0167 (very low squishification), while Halley's Comet's orbit has an eccentricity of 0.9671 (very high squishification) <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

In the thumbtack definition, eccentricity is determined by the distance between the two thumbtacks (foci) divided by the length of the ellipse's longest axis <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. When slicing a cone, the eccentricity is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. A key question arises: why should these three distinct definitions produce precisely the same family of curves <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>? It might intuitively seem that slicing a cone could produce a lopsided, egg-like shape rather than a symmetric ellipse <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## The Proof: Using Dandelin Spheres

Mathematical proofs provide the airtight demonstration that these definitions are equivalent <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. A particularly elegant proof shows that slicing a cone produces a curve that can also be drawn using the thumbtack construction (i.e., it possesses the constant focal sum property) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

The ingenious step in this proof, which Paul Lockhart highlights in his book *Measurement*, is the introduction of two spheres <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>:
*   One sphere is placed above the slicing plane.
*   The other sphere is placed below the slicing plane.
*   Each sphere is sized perfectly to be tangent to the cone along a circle of points and tangent to the plane at a single point <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

The two points where these spheres are tangent to the slicing plane are precisely the focal points of the ellipse <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Steps of the Proof:

1.  Consider any point *q* on the ellipse (the intersection curve) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
2.  Draw a line from *q* to the first proposed focus (where the large sphere touches the plane) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This line segment is tangent to the large sphere.
3.  Draw a line from *q* straight down along the cone to the circle of tangency of the large sphere <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This line segment is also tangent to the large sphere.
4.  A fundamental property of spheres states that all tangent lines drawn from a common external point to a sphere have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Therefore, the distance from *q* to the proposed focus is equal to the distance from *q* to the point on the large circle of tangency along the cone <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
5.  Apply the same logic to the smaller sphere and its proposed focus (where the small sphere touches the plane) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. The distance from *q* to this second focus is equal to the distance from *q* to the point on the small circle of tangency along the cone <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
6.  The sum of the distances from *q* to the two proposed focus points is therefore equal to the sum of the distances from *q* to the two tangency circles along the cone <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
7.  Crucially, the combined path along the cone from the small circle of tangency, through *q*, to the large circle of tangency, represents a straight line segment on the cone's surface <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. The length of this combined path is constant regardless of where *q* is on the ellipse, as it's simply the straight-line distance between the two circles of tangency along the cone's surface <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

Since the sum of the distances from *q* to the two proposed foci is constant, this proves that the curve formed by slicing a cone possesses the constant focal sum property, thus confirming it is indeed an ellipse identical to one drawn with the thumbtack method <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

This proof was discovered by Germinal Pierre Dandelin in 1822, leading to the spheres being named Dandelin spheres <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The same technique can be used to show that slicing a cylinder at an angle also yields an ellipse <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Furthermore, it implies the equivalence with the "stretched circle" definition, assuming that projecting a shape from one plane onto a tilted plane effectively stretches it <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## Why This Proof is a Good Representative for Math

This proof is often cited as a powerful example of mathematical beauty for several reasons <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:

*   **Substantive and Accessible**: It delivers a profound result without requiring extensive prior mathematical knowledge <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Equivalence of Definitions**: It beautifully illustrates a common feature of mathematics: sometimes there isn't a single "most fundamental" way to define something, and what matters more is proving equivalences between different definitions <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Creative Construction**: The proof showcases a key moment of creative construction—the idea of introducing the two spheres—while the rest of the proof follows a systematic and principled approach <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This balance between ingenious insight and rigorous deduction is a hallmark of mathematical discovery <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

The origin of such "ingenious" ideas like adding the Dandelin spheres might seem like an inexplicable miracle <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. However, it can often be viewed as the "residue of experience" for someone deeply immersed in [[Geometric reasoning in higher dimensions | geometry problems]] <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. A common tactic in geometry involves relating lengths, and the spheres provide a natural way to connect various lengths due to the defining property of tangents to a sphere <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. This perspective transforms the idea of genius from merely mesmerizing to actively inspirational <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.