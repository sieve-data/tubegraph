---
title: Ellipses and conic sections
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

For those who appreciate mathematics, the proof demonstrating why planets orbit in [[geometry_of_ellipses | ellipses]] and how different definitions of an [[geometry_of_ellipses | ellipse]] are equivalent is considered a beautiful illustration of mathematical progress and cleverness <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Defining an Ellipse

There are at least three primary geometric definitions for an [[geometry_of_ellipses | ellipse]]:

1.  **Stretching a [[geometry_and_circles | Circle]]**: An [[geometry_of_ellipses | ellipse]] can be defined by taking a [[geometry_and_circles | circle]] and stretching it in one dimension <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This can be visualized by multiplying the x-coordinate of all points by a specific factor <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  **Two Thumbtacks and String (Constant Focal Sum)**: This classic construction involves looping a string around two thumbtacks stuck into a piece of paper, pulling it taut with a pencil, and tracing a curve <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from the pencil point to the two thumbtack points remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. These two thumbtack points are called the *foci* of the [[geometry_of_ellipses | ellipse]], and this "constant focal sum" property defines an [[geometry_of_ellipses | ellipse]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
3.  **Slicing a Cone (Conic Section)**: An [[geometry_of_ellipses | ellipse]] can also be defined as the curve formed by slicing a cone with a plane at an angle smaller than the cone's slope <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The intersection of this plane and the cone forms an [[geometry_of_ellipses | ellipse]], which is why [[geometry_of_ellipses | ellipses]] are often referred to as a "conic section" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Eccentricity

An [[geometry_of_ellipses | ellipse]] is not a single curve but a family of curves, ranging from a perfect [[geometry_and_circles | circle]] to something infinitely stretched <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The specific shape of an [[geometry_of_ellipses | ellipse]] is quantified by its [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

*   A [[geometry_and_circles | circle]] has an [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] of 0 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   The more "squished" an [[geometry_of_ellipses | ellipse]] is, the closer its [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] is to 1 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   For example, Earth's orbit has a low [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] of 0.0167, making it very close to a [[geometry_and_circles | circle]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Halley's comet, by contrast, has a high [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] of 0.9671 <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

The [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] is determined differently depending on the definition:

*   In the thumbtack definition, [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] is determined by the distance between the two thumbtacks (foci) divided by the length of the [[geometry_of_ellipses | ellipse]]'s longest axis <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   For slicing a cone, [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Equivalence of Definitions

A key question is why these three distinct definitions produce precisely the same family of [[geometry_of_ellipses | curves]] <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. It might seem counter-intuitive that slicing a cone would yield such a symmetric shape, rather than a lopsided egg <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. However, the intersection curve is indeed an [[geometry_of_ellipses | ellipse]], identical to those produced by stretching a [[geometry_and_circles | circle]] or using the thumbtack construction <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Proof: Cone Slicing and Thumbtack Equivalence (Dandelin Spheres)

To demonstrate that slicing a cone produces a curve that could also be drawn using the thumbtack construction, one must show that there exist two focal points within the slicing plane such that the sum of the distances from any point on the intersection curve to these two points remains constant <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

The ingenious method for this proof, popularized by Paul Lockhart in "Measurement," involves introducing two spheres into the setup <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>:
1.  **Introducing the Spheres**: One sphere is placed above the slicing plane and one below it <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Each sphere is sized precisely to be tangent to the cone along a [[geometry_and_circles | circle]] of points, and also tangent to the slicing plane at a single point <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  **Identifying Foci**: The two points where the spheres are tangent to the slicing plane are the proposed focal points of the [[geometry_of_ellipses | ellipse]] <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
3.  **Key Geometric Property**: When multiple lines are drawn from a common point to a [[geometric_analysis_of_sphere_and_cylinder | sphere]], and all of these lines are tangent to that [[geometric_analysis_of_sphere_and_cylinder | sphere]], they all have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This property stems from the inherent symmetry of a [[geometric_analysis_of_sphere_and_cylinder | sphere]] <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
4.  **Proof Application**:
    *   Consider any point 'q' on the [[geometry_of_ellipses | ellipse]] (the intersection curve) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
    *   The line segment from 'q' to the first proposed focus (tangency point with the large sphere) is tangent to the big sphere <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   A line drawn from 'q' straight down along the cone to the large sphere's [[geometry_and_circles | circle]] of tangency is *also* tangent to the big sphere <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Therefore, by the geometric property, these two lines have the same length <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   Similarly, the line segment from 'q' to the second proposed focus (tangency point with the small sphere) is tangent to the small sphere <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   A line drawn from 'q' straight up along the cone to the small sphere's [[geometry_and_circles | circle]] of tangency is *also* tangent to the small sphere <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. These two lines also have the same length <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   Thus, the sum of the distances from 'q' to the two proposed focal points is equivalent to the straight-line distance along the cone from the small sphere's tangency [[geometry_and_circles | circle]] down to the big sphere's tangency [[geometry_and_circles | circle]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This distance is constant, regardless of the chosen point 'q' on the [[geometry_of_ellipses | ellipse]] <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

This elegant proof, first discovered by Germinal Pierre Dandelin in 1822, utilizes what are now known as **Dandelin spheres** <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The same trick can be used to show why slicing a [[geometric_analysis_of_sphere_and_cylinder | cylinder]] at an angle also yields an [[geometry_of_ellipses | ellipse]] <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Furthermore, it helps demonstrate that projecting a shape from one plane onto a tilted plane (which essentially stretches the shape) explains the equivalence of the "stretched [[geometry_and_circles | circle]]" definition with the other two <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Significance of the Proof

This proof is highly regarded in mathematics for several reasons <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:
*   It is substantive and beautiful without requiring extensive mathematical background <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   It illustrates that sometimes there isn't a single "most fundamental" way to define something, and that demonstrating equivalences between different definitions is crucial <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   The proof features a key moment of creative construction—the addition of the Dandelin spheres—while the rest of the proof follows a systematic and principled approach <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This blend of creative insight and structured deduction is a hallmark of mathematical discovery <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

As Paul Lockhart states in his book "Measurement":
> <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>

The seemingly miraculous nature of such insights can often be understood as the "residue of experience" <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. Mathematicians who have immersed themselves in various [[geometry_of_ellipses | geometry]] problems are primed to recognize how certain geometric objects, like [[geometric_analysis_of_sphere_and_cylinder | spheres]] and [[geometry_and_circles | circles]], can relate different lengths and properties, making the introduction of Dandelin spheres a logical, albeit ingenious, step within that experienced framework <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. This perspective transforms the idea of genius from bewildering to inspirational <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.