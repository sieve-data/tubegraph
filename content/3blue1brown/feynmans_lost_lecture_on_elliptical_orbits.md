---
title: Feynmans Lost Lecture on elliptical orbits
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

The concept of planets orbiting in ellipses was notably explored in a video titled "Feynman's Lost Lecture" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, which was published as a guest video on MinutePhysics <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This lecture touched upon why planets exhibit elliptical orbits, a fundamental aspect of [[Development of Keplers laws of planetary motion | Kepler's laws of planetary motion]].

## Geometric Definitions of an Ellipse

An ellipse can be defined geometrically in several ways:

*   **Stretched Circle** One method is to take a circle and stretch it out in one dimension <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This can be conceptualized by multiplying one coordinate (e.g., the x-coordinate) of all points by a specific factor <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Two Thumbtacks and String (Constant Focal Sum)** This classic construction involves looping a string around two thumbtacks stuck into paper, pulling it taut with a pencil, and tracing around <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from the pencil point to the two thumbtack points (called foci) remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Slicing a Cone (Conic Section)** An ellipse can also be defined by slicing a cone with a plane at an angle smaller than the cone's slope <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The curve formed by the intersection of the plane and the cone is an ellipse <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, hence the term "conic section" <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Eccentricity of Ellipses

An ellipse is not a single curve but a family of curves, ranging from a perfect circle to something infinitely stretched <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The specific shape of an ellipse is quantified by its [[eccentricity and geometric properties of ellipses | eccentricity]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

*   A circle has an eccentricity of 0 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   As an ellipse becomes more "squished," its eccentricity approaches 1 <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   Earth's orbit has a low eccentricity of 0.0167, indicating it is very close to a circle <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   Halley's Comet, in contrast, has an orbit with a high eccentricity of 0.9671 <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

In the thumbtack definition, eccentricity is determined by the distance between the two foci divided by the length of the longest axis of the ellipse <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. When slicing a cone, the eccentricity is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Equivalence of Definitions: The Dandelin Spheres Proof

A natural question arises as to why these three distinct definitions produce precisely the same shapes <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The proof demonstrating the equivalence between slicing a cone and the thumbtack construction is particularly illustrative <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. It shows that when a cone is sliced, there exist two points within the slicing plane such that the sum of the distances from any point on the intersection curve to these two points remains constant <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

This proof, first discovered by Germinal Pierre Dandelin in 1822 <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>, involves the ingenious addition of two spheres, often called **Dandelin spheres** <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

### The Proof Steps

1.  **Introducing Dandelin Spheres**: Two spheres are introduced into the setup: one above and one below the slicing plane <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Each sphere is sized to be tangent to the cone along a circle of points and tangent to the slicing plane at a single point <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. These two tangency points on the plane are conjectured to be the foci of the ellipse <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
2.  **Utilizing Tangency Properties**: For any point 'q' on the ellipse (the intersection curve):
    *   The line from 'q' to the proposed focus (where the larger sphere touches the plane) is tangent to the larger sphere <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   A line drawn from 'q' straight down along the cone to the large circle of tangency is also tangent to the larger sphere <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   A key geometric property is that if multiple lines are drawn from a common external point to a sphere and are all tangent to that sphere, they must all have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Therefore, the distance from 'q' to the larger focus point is equal to the distance from 'q' to the point on the larger tangency circle along the cone <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   Similarly, for the smaller sphere, the distance from 'q' to the smaller focus point is equal to the distance from 'q' to the point on the smaller tangency circle along the cone <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
3.  **Constant Sum**: The sum of the distances from point 'q' to the two proposed focus points is equal to the straight-line distance along the cone from the smaller tangency circle down to the larger tangency circle, passing through 'q' <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This distance is constant regardless of which point 'q' is chosen on the ellipse <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

This establishes that slicing a cone produces a curve with the constant focal sum property, thus proving its equivalence to the thumbtack construction <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This same trick can also be used to show why slicing a cylinder at an angle results in an ellipse <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, and why projecting a shape from one plane onto another tilted plane is equivalent to stretching it <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### The Creative Aspect of Proofs

This proof exemplifies the beauty of mathematics because it is substantive and beautiful without requiring extensive background knowledge <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. It highlights that there isn't always a single, most fundamental definition for a concept, but rather that showing equivalences between definitions is crucial <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. The introduction of the Dandelin spheres represents a "key moment of creative construction" <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>, which is a hallmark of mathematical discovery. Such ingenuity often arises from experience and a deep understanding of geometric relationships, allowing a seasoned mathematician to connect seemingly disparate ideas <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. As Paul Lockhart suggests in his book *Measurement*, such ideas may simply "come to you" <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. However, it can also be viewed as "the residue of experience," making genius actively inspirational rather than an inexplicable miracle <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.