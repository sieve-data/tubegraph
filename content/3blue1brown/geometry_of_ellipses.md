---
title: Geometry of ellipses
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

Ellipses can be defined geometrically in several main ways, and a particularly elegant mathematical proof demonstrates their fundamental equivalence <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This proof highlights the beauty and inventiveness of [[geometry_in_higher_dimensions | geometry]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Definitions of an Ellipse

There are at least three primary geometric definitions for an ellipse:

1.  **Stretching a Circle**: An ellipse can be conceived as a [[geometry_and_circles | circle]] that has been stretched in one dimension <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. For instance, if points are represented by (x, y) coordinates, multiplying only the x-coordinate by a specific factor for all points yields an ellipse <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  **Two Thumbtacks and a String (Focal Sum Property)**: This classic construction involves looping a string around two thumbtacks stuck into a piece of paper, pulling it taut with a pencil, and tracing <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from each point to the two thumbtack points (called foci) remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This "constant focal sum property" defines the ellipse <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Slicing a Cone (Conic Section)**: An ellipse can also be defined by slicing a cone with a plane at an angle <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The angle of the plane must be smaller than the slope of the cone itself <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The curve formed by the intersection of this plane and the cone is an ellipse, leading to the term "[[ellipses_and_conic_sections | conic section]]" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Eccentricity

An ellipse is not a single curve but a family of curves, ranging from a perfect [[geometry_and_circles | circle]] to something infinitely stretched <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The specific shape is quantified by its [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

*   A [[geometry_and_circles | circle]] has an [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] of 0 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   As an ellipse becomes more squished, its [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] approaches 1 <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   For the thumbtack definition, [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] is determined by the distance between the foci divided by the length of the ellipse's longest axis <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   For the conic section definition, [[eccentricity_and_its_role_in_defining_ellipses | eccentricity]] is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The profound question arises: why should these three seemingly distinct definitions produce precisely the same family of shapes <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>?

## The Dandelin Spheres Proof

The equivalence between slicing a cone (conic section) and the thumbtack construction (constant focal sum) is beautifully demonstrated using Dandelin spheres <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This proof requires showing that for any ellipse formed by slicing a cone, there exist two points within the slicing plane (the foci) such that the sum of distances from any point on the ellipse to these two points is constant <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Introducing the Dandelin Spheres

The "stroke of genius" in this proof is the introduction of two spheres <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>:
*   One sphere is placed above the slicing plane and one below <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   Each sphere is sized perfectly to be tangent to the cone along a [[geometry_and_circles | circle]] of points <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   Each sphere is also tangent to the slicing plane at a single point <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

These two tangency points on the plane are conjectured to be the foci of the ellipse <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### The Proof Steps

1.  **Tangent Lines from a Point to a Sphere**: A crucial geometric property states that if multiple lines are drawn from a common external point to a sphere, and all these lines are tangent to the sphere, then they all have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This can be proven by considering the right triangles formed by the point, the center of the sphere, and the tangency points <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

2.  **Applying to the Ellipse**:
    *   Consider an arbitrary point 'q' on the ellipse (the intersection curve) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
    *   Draw a line segment from 'q' to the first proposed focus (where the larger sphere touches the plane) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This line segment is tangent to the larger sphere <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   Now, consider a line segment from 'q' that goes straight down along the cone until it touches the larger sphere's circle of tangency with the cone <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This line segment is also tangent to the larger sphere <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   According to the property of tangent lines from a common point, these two line segments have the same length <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   Repeat this process for the second proposed focus (where the smaller sphere touches the plane) and the smaller sphere <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. The line segment from 'q' to the second focus is tangent to the smaller sphere, as is the line segment from 'q' straight up along the cone to its tangency circle <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. These two segments also have the same length <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

3.  **Constant Focal Sum**: The sum of the distances from point 'q' to the two proposed focus points is equal to the sum of the lengths of the two line segments that travel along the cone's surface, one to the upper tangency circle and one to the lower tangency [[geometry_and_circles | circle]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This combined length is simply the straight-line distance along the cone from the lower tangency [[geometry_and_circles | circle]] to the upper tangency [[geometry_and_circles | circle]], passing through 'q' <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Crucially, this total distance is constant regardless of which point 'q' is chosen on the ellipse <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

Therefore, slicing a cone produces a curve with the constant focal sum property, proving its equivalence to the thumbtack construction <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Historical Context and Significance

This proof was first discovered by Germinal Pierre Dandelin in 1822 <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>, hence the spheres are known as Dandelin spheres <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. The same trick can be used to show why slicing a cylinder at an angle also yields an ellipse <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Furthermore, if one accepts that projecting a shape from one plane onto a tilted plane is equivalent to stretching that shape, this proof also connects the conic section definition to the stretched [[geometry_and_circles | circle]] definition <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

The Dandelin spheres proof is considered a prime example of mathematical beauty because <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:
*   It is substantive and elegant, requiring minimal prior mathematical background <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   It showcases a common feature in mathematics: often, there isn't a single "most fundamental" definition, but rather a focus on demonstrating equivalences between different definitions <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   It highlights a key aspect of mathematical discovery: a single moment of creative construction (adding the spheres) often underpins a systematic and principled proof <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This creativity is seen as the "residue of experience" built from engaging with numerous other [[geometry_in_higher_dimensions | geometry]] problems and understanding how geometric objects relate <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

> "A good proof is like a work of art. It is a thing of grace and beauty. It is the work of a master craftsman, not a journeyman. No self-respecting craftsman would simply pile up bricks in a wall without thinking about the structure, about the flow of forces, about the aesthetic effect." <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>
> — Paul Lockhart, *Measurement*