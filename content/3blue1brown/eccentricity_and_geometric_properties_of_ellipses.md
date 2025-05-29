---
title: eccentricity and geometric properties of ellipses
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

If one had to choose a single mathematical proof to demonstrate the beauty and cleverness of mathematics, the proof showing the equivalence of different [[geometric_definitions_of_an_ellipse | geometric definitions of an ellipse]] would be a strong candidate <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This particular [[proof_of_slicing_a_cone_to_form_an_ellipse | proof of slicing a cone to form an ellipse]] involves 3D geometry and requires almost no prior background, yet it captures the spirit of mathematical inventiveness <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Geometric Definitions of an Ellipse

There are at least three primary ways to define an ellipse geometrically <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>:

1.  **Stretching a Circle**: An ellipse can be defined by taking a circle and stretching it out in one dimension <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This can be visualized by considering all points as XY coordinates and multiplying only the X-coordinate by a special factor <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  **Two Thumbtacks and a String (Focal Sum Property)**: This classic construction involves looping a string around two thumbtacks stuck into paper, pulling it taut with a pencil, and tracing <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from the pencil point to the two thumbtack points (called foci) remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
3.  **Slicing a Cone (Conic Section)**: An ellipse can also be defined by slicing a cone with a plane at an angle smaller than the slope of the cone itself <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The curve formed by the intersection of this plane and the cone is an ellipse, hence why ellipses are often referred to as conic sections <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

It's natural to wonder why these three distinct definitions produce precisely the same family of curves <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. For instance, slicing a cone might intuitively seem to produce a lopsided, egg-like shape rather than a symmetric ellipse <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Eccentricity

An ellipse is not just one curve but a family of curves, ranging from a perfect circle to something infinitely stretched <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The specific shape of an ellipse is quantified by a number called its **eccentricity** <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

*   A circle has an eccentricity of 0 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   The more "squished" an ellipse is, the closer its eccentricity is to 1 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

For example, Earth's orbit has an eccentricity of 0.0167, indicating it is very close to being a circle <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. In contrast, Halley's Comet has an orbit with an eccentricity of 0.9671, signifying a very high "squishification" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

In the thumbtack definition, eccentricity is determined by the distance between the two thumbtacks (foci) divided by the length of the ellipse's longest axis <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. For the cone-slicing definition, eccentricity is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Proof of Equivalence: Dandelin Spheres

To prove that slicing a cone yields a curve that can also be drawn with the thumbtack construction, one must show that there exist two points within the slicing plane (the foci) such that the sum of the distances from any point on the intersection curve to these two points remains constant <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

The ingenious trick to demonstrating this, first introduced by Germinal Pierre Dandelin in 1822 <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>, is to introduce two spheres into the setup, known as **Dandelin spheres** <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

1.  **Introducing the Spheres**: Two spheres are positioned, one above the plane and one below, each sized to be tangent to the cone along a circle of points, and simultaneously tangent to the plane at a single point <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  **Identifying the Foci**: The points where these spheres are tangent to the plane are the proposed focal points of the ellipse <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
3.  **The Key Geometric Principle**: A fundamental property used in this proof is that if multiple lines are drawn from a common point to a sphere, and all these lines are tangent to the sphere, then they all have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This is a consequence of the setup's symmetry <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
4.  **Demonstrating Constant Focal Sum**:
    *   Consider any point 'q' on the elliptical intersection curve <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
    *   The line from 'q' to the first proposed focus (tangency point with the large sphere) is tangent to the large sphere <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   The line from 'q' straight down along the cone (to the circle of tangency with the large sphere) is also tangent to the large sphere <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. By the key principle, these two lines have the same length <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   Similarly, the line from 'q' to the second proposed focus (tangency point with the small sphere) is tangent to the small sphere <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   The line from 'q' straight up along the cone (to the circle of tangency with the small sphere) is also tangent to the small sphere <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. These two lines also have the same length <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   Therefore, the sum of the distances from 'q' to the two proposed focal points is equal to the constant straight-line distance along the cone from the little circle of tangency to the big circle of tangency, passing through 'q' <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
    *   Since this sum does not depend on the specific point 'q' chosen on the ellipse, the constant focal sum property is proven <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

This same technique can be used to show why slicing a cylinder at an angle also produces an ellipse <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Furthermore, if one accepts that projecting a shape from one plane onto another tilted plane effectively stretches that shape, this proof also links the [[geometric_definitions_of_an_ellipse | definition of an ellipse]] as a stretched circle to the other two <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## The Beauty of Mathematical Proofs

This proof is considered an excellent representation of mathematics for several reasons <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:

*   It is substantive and beautiful without requiring extensive prior knowledge <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   It illustrates that sometimes there isn't one "most fundamental" way to define something, and that demonstrating equivalences between definitions is crucial <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   The proof features a key moment of creative construction (adding the Dandelin spheres), combined with a systematic and principled approach for the rest <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

The creative leap of introducing the spheres is a thought-provoking aspect of mathematical discovery <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. As Paul Lockhart writes in his book *Measurement*:
> "No amount of logical rigor or formal deduction can make up for the lack of a good idea. That’s what a proof is—a good idea." <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>

While ingenious, such creative constructions are not inexplicable miracles <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. They often stem from experience and immersion in related geometric problems <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. For instance, in geometry, relating one length to another is a common tactic <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. Circles and spheres frequently facilitate such relationships due to their defining features <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. Thus, what appears as genius can often be viewed as the residue of extensive experience, transforming the idea of genius from mesmerizing to actively inspirational <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.