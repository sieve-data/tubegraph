---
title: proof of slicing a cone to form an ellipse
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

If one had to choose a single proof to demonstrate the beauty and cleverness of mathematics, the proof showing the equivalence of different [[geometric_definitions_of_an_ellipse | definitions of an ellipse]] is a strong candidate <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This particular proof involves a "lovely bit of 3D geometry" that requires almost no background but captures the spirit of mathematical inventiveness <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Geometric Definitions of an Ellipse

There are at least three main ways to define an ellipse geometrically <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>:

1.  **Stretching a Circle**: An ellipse can be defined by taking a circle and stretching it out in one dimension, for example, by multiplying the x-coordinate of all points by a special factor <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
2.  **Two Thumbtacks and a String (Constant Focal Sum)**: This classic construction involves looping a string around two thumbtacks, pulling it taut with a pencil, and tracing a curve <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from the pencil point to the two thumbtack points (called "foci") remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
3.  **Slicing a Cone (Conic Section)**: An ellipse can also be defined by slicing a cone with a plane at an angle smaller than the slope of the cone itself <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The curve formed by the intersection of this plane and the cone is an ellipse <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This is why ellipses are often referred to as a "conic section" <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

Ellipses are a family of curves, ranging from a perfect circle to something infinitely stretched <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Their specific shape is quantified by a number called [[eccentricity and geometric properties of ellipses | eccentricity]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>:
*   A circle has an [[eccentricity and geometric properties of ellipses | eccentricity]] of 0 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   The more "squished" an ellipse is, the closer its [[eccentricity and geometric properties of ellipses | eccentricity]] is to 1 <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   For example, Earth's orbit has an [[eccentricity and geometric properties of ellipses | eccentricity]] of 0.0167, while Halley's comet has an orbit with an [[eccentricity and geometric properties of ellipses | eccentricity]] of 0.9671 <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

In the thumbtack definition, [[eccentricity and geometric properties of ellipses | eccentricity]] is determined by the distance between the two thumbtacks divided by the length of the ellipse's longest axis <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. For slicing a cone, [[eccentricity and geometric properties of ellipses | eccentricity]] is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The fundamental question is why these three seemingly different definitions produce precisely the same shapes <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. It might seem counter-intuitive that slicing a cone produces such a symmetric shape, rather than a lopsided egg shape <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## The Proof: Dandelin Spheres

To prove the equivalence, particularly that slicing a cone yields a curve that can also be drawn with the thumbtack construction, one needs to show that two "thumbtack points" (foci) exist within the slicing plane, such that the sum of the distances from any point on the intersection curve to these two points remains constant <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

The key insight for this proof, which was first found by Germinal Pierre Dandelin in 1822, is to introduce two spheres into the picture <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. These are sometimes called **Dandelin spheres** <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>:

1.  **Placement of Spheres**: One sphere is placed above the slicing plane and one below it <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  **Tangency**: Each sphere is sized precisely to be:
    *   Tangent to the cone along a circle of points <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   Tangent to the slicing plane at just a single point <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

These two tangency points in the plane are the proposed foci of the ellipse <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Steps of the Proof:

*   **Define a Point**: Let 'q' be any point on the ellipse formed by the intersection of the cone and the plane <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Draw Lines to Foci**: Draw lines from point 'q' to the two proposed focus points (the tangency points of the Dandelin spheres with the plane) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Identify Tangents to Spheres**:
    *   The line from 'q' to the first proposed focus is tangent to the large sphere <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   A line drawn from 'q' straight down along the cone (a generator of the cone) is also tangent to the large sphere at the point where it intersects the sphere's circle of tangency with the cone <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   Similarly, the line from 'q' to the second proposed focus is tangent to the small sphere <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   The same generator line from 'q' (extending upwards) is also tangent to the small sphere where it intersects that sphere's circle of tangency <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Property of Tangents**: A crucial geometric property states that if multiple lines are drawn from a common point to a sphere, and all are tangent to that sphere, then all these lines must have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   Therefore, the distance from 'q' to the first focus is equal to the distance from 'q' along the cone's generator to the large circle of tangency <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   Likewise, the distance from 'q' to the second focus is equal to the distance from 'q' along the cone's generator to the small circle of tangency <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Constant Sum**: The sum of the distances from 'q' to the two proposed focus points is thus equal to the straight-line distance along the cone's generator from the small circle of tangency down to the big circle of tangency <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Conclusion**: This sum of distances is constant regardless of which point 'q' is chosen on the ellipse, because the distance along any generator between the two circles of tangency is constant <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This demonstrates that the curve resulting from slicing a cone possesses the constant focal sum property, making it equivalent to the thumbtack construction of an ellipse <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

This same trick can also be used to show that slicing a cylinder at an angle will result in an ellipse <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Furthermore, if one accepts the claim that [[projection_of_sphere_onto_a_cylinder | projecting a shape from one plane onto another tilted plane]] simply stretches that shape, it also shows the equivalence between a sliced cone/cylinder and a stretched circle <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## Why This Proof is Significant

This proof is an excellent representative for mathematics for several reasons <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:

*   **Accessibility and Beauty**: It is substantive and beautiful without requiring extensive mathematical background <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Equivalence of Definitions**: It highlights a common feature in math where there isn't always a single "most fundamental" definition, but rather showing the equivalence between different definitions is what truly matters <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Creative Construction**: The proof involves a crucial moment of "creative construction"—the introduction of the two spheres <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This creative step, combined with a systematic and principled approach, exemplifies mathematical discovery <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Genius as Residue of Experience**: While ingenious, the idea of adding the spheres can be seen as the result of a mind immersed in various geometry problems, where relating lengths using circles and spheres is a common tactic <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. This perspective transforms "genius" from an inexplicable miracle into an active inspiration, suggesting that such insights are the "residue of experience" <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

Paul Lockhart, in his book *Measurement*, describes this particular proof:
> <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a> "What a lovely idea! Who thinks of these things? There is something incredibly daring and confident in this move. 'Let's just throw some spheres in there!' It's the move of a composer introducing a whole new instrument in the middle of a symphony. And it works!" <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>