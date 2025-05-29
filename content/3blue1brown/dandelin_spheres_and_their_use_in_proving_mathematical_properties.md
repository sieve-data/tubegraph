---
title: Dandelin spheres and their use in proving mathematical properties
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

When seeking to illustrate the beauty and cleverness inherent in mathematics, one particularly insightful proof involves the use of [[Dandelin spheres and their use in proving mathematical properties | Dandelin spheres]] to demonstrate the equivalence of various ellipse definitions <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This geometric proof requires almost no prior background, yet it elegantly captures the spirit of mathematical inventiveness <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Defining an Ellipse

Geometrically, an ellipse can be defined in at least three principal ways <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>:

1.  **Stretched Circle**: An ellipse can be considered a circle that has been stretched in one dimension <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. For example, by multiplying the x-coordinate of all points in a circle by a specific factor <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A perfect circle has an eccentricity of 0, and the more "squished" an ellipse is, the closer its eccentricity is to 1 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  **Two Thumbtacks and String (Constant Focal Sum)**: This classic construction involves looping a string around two thumbtacks stuck into paper, pulling it taut with a pencil, and tracing <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from the pencil point to the two thumbtack points (called "foci") remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The eccentricity in this definition is determined by the distance between the foci divided by the length of the ellipse's longest axis <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  **Conic Section**: An ellipse is formed by slicing a cone with a plane at an angle smaller than the slope of the cone itself <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The curve of intersection points between the plane and the cone forms an ellipse <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The eccentricity here is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

It may seem counterintuitive that these three distinct methods produce precisely the same family of curves <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. For instance, the intersection of a cone and a plane might appear to form a lopsided, egg-like shape rather than a symmetric ellipse <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## The Proof using Dandelin Spheres

The definitive proof demonstrating that slicing a cone yields a curve that can also be drawn using the thumbtack construction involves the ingenious introduction of two spheres, known as [[Dandelin spheres and their use in proving mathematical properties | Dandelin spheres]] <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This proof was first discovered by Germinal Pierre Dandelin in 1822 <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Construction of the Spheres

Imagine two spheres inserted into the cone: one above the slicing plane and one below it <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Each sphere is precisely sized to be:
*   Tangent to the cone along a circle of points <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   Tangent to the slicing plane at a single point <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

These two tangency points on the plane are the foci of the ellipse <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### The Key Insight

The core of the proof relies on a fundamental geometric property: if multiple lines are drawn from a common point to a sphere, and all these lines are tangent to that sphere, then they all have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

Consider an arbitrary point 'q' on the intersection curve (the ellipse) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
1.  Draw a line from 'q' to the first focus (where the larger sphere touches the plane) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This line is tangent to the larger sphere.
2.  Draw a line from 'q' straight down along the cone to the circle where the larger sphere is tangent to the cone <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This line is also tangent to the larger sphere.
3.  By the property stated above, these two lines from 'q' to the large sphere have the same length <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
4.  Similarly, draw a line from 'q' to the second focus (where the smaller sphere touches the plane) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This line is tangent to the smaller sphere.
5.  Draw a line from 'q' straight up along the cone to the circle where the smaller sphere is tangent to the cone <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. This line is also tangent to the smaller sphere.
6.  These two lines from 'q' to the small sphere have the same length <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

Therefore, the sum of the distances from point 'q' to the two foci is equal to the straight-line distance along the cone from the point on the small circle of tangency to the point on the big circle of tangency, passing through 'q' <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This sum is constant, regardless of which point 'q' is chosen on the ellipse <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This confirms that the conic section possesses the constant focal sum property, thus proving its equivalence to the thumbtack construction <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Broader Implications

This method can also be applied to prove that slicing a cylinder at an angle produces an ellipse <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Furthermore, it underpins the equivalence of the "stretched circle" definition, if one accepts that projecting a shape from one plane onto a tilted plane is equivalent to stretching it <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

The Dandelin sphere proof is often lauded as an exemplary piece of mathematics because it is substantive and beautiful without demanding extensive prior knowledge <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. It highlights that there may not be a single "most fundamental" definition for a mathematical object, but rather that demonstrating equivalences between different definitions is paramount <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

The creative act of introducing the two spheres, while initially appearing as an inexplicable miracle, can be seen as the "residue of experience" for someone deeply immersed in geometry <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a> <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. Paul Lockhart, in his book *Measurement*, describes such insights:
> [!quote] Paul Lockhart on Mathematical Ingenuity
> It's not a step you can deduce; it's a step you invent. It's a spontaneous act of creation in response to a felt need. That's what a good definition is, and that's what a good idea in mathematics is, a response to a need. <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>

The proof illustrates how understanding the properties of geometric objects, like the constant radius of a sphere leading to equal tangent lengths, primes a mathematician to consider such creative constructions to solve problems involving relationships between lengths <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. Thus, seemingly ingenious solutions are often the result of practiced intuition and deep engagement with mathematical concepts <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.