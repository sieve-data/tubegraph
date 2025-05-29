---
title: geometric definitions of an ellipse
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

An ellipse is a fundamental curve in mathematics, often chosen to illustrate the beauty and ingenuity of mathematical proofs <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is not just a single curve, but rather a family of curves that range from a perfect circle to something infinitely stretched <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Geometric Definitions of an Ellipse

There are at least three primary geometric ways to define an ellipse:

1.  **Stretched Circle**
    An ellipse can be defined as a circle stretched out in one dimension <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This can be conceptualized by taking all points defined by `(x, y)` coordinates and multiplying just the `x` coordinate by a specific factor <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

2.  **Two Thumbtacks and a String (Constant Focal Sum Property)**
    This classic construction involves looping a string around two thumbtacks stuck into a piece of paper, pulling the string taut with a pencil, and tracing around while keeping the string taut <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The resulting curve is the set of all points where the sum of the distances from the pencil point to the two thumbtack points (called *foci*) remains constant <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This constant focal sum property defines an ellipse <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

3.  **Slicing a Cone (Conic Section)**
    An ellipse can also be defined by slicing a cone with a plane at an angle smaller than the slope of the cone itself <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The curve of points where the plane and the cone intersect forms an ellipse, which is why ellipses are often referred to as a conic section <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Eccentricity

The specific "squishification" or shape of an ellipse is quantified by a number called its [[eccentricity_and_geometric_properties_of_ellipses | eccentricity]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   A perfect circle has an eccentricity of 0 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   As an ellipse becomes more squished, its [[eccentricity_and_geometric_properties_of_ellipses | eccentricity]] approaches 1 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   Earth's orbit, for instance, has an eccentricity of 0.0167, indicating it's very close to a circle <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   Halley's Comet has an orbit with an eccentricity of 0.9671, showing a very high squishification <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

In the thumbtack definition, [[eccentricity_and_geometric_properties_of_ellipses | eccentricity]] is determined by the distance between the two thumbtacks (foci) divided by the length of the longest axis of the ellipse <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. For cone slicing, [[eccentricity_and_geometric_properties_of_ellipses | eccentricity]] is determined by the slope of the slicing plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Equivalence of Definitions: The Dandelin Spheres Proof

It is remarkable that these three distinct methods produce precisely the same family of shapes <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. One might expect a cone slice to produce a lopsided, egg-like shape, but it is indeed a perfectly symmetric ellipse <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

A significant [[proof_of_slicing_a_cone_to_form_an_ellipse | proof of slicing a cone to form an ellipse]] involves demonstrating that the curve formed by slicing a cone also possesses the constant focal sum property of the thumbtack construction <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This proof requires showing that two specific "thumbtack points" (foci) exist within the slicing plane, such that the sum of the distances from any point on the intersection curve to these two points remains constant <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Dandelin Spheres

The key insight, first described by Paul Lockhart in "Measurement," involves introducing two spheres into the setup <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   One sphere is placed above the slicing plane and one below <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   Each sphere is sized perfectly to be tangent to the cone along a circle of points and tangent to the slicing plane at a single point <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

These two points of tangency between the spheres and the slicing plane are precisely the focal points of the ellipse <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### The Proof Steps

1.  Consider any point `q` on the ellipse (the intersection curve) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
2.  Draw a line from `q` to the first proposed focus (where the larger sphere touches the plane) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This line is tangent to the larger sphere <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
3.  Draw a line from `q` straight down along the cone to the circle of tangency with the larger sphere <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This line is also tangent to the larger sphere <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
4.  A fundamental [[geometric_properties_of_ellipses | geometric property]] is that if multiple lines are drawn from a common point to a sphere and are all tangent to that sphere, they must all have the same length <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Therefore, the distance from `q` to the first focus is equal to the distance from `q` to the point where the line along the cone touches the larger sphere's tangency circle <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
5.  Similarly, the distance from `q` to the second proposed focus (where the smaller sphere touches the plane) is equal to the distance from `q` to the point where the line along the cone touches the smaller sphere's tangency circle <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
6.  Thus, the sum of the distances from `q` to the two proposed focal points is equal to the total straight-line distance along the cone from the smaller sphere's tangency circle down to the larger sphere's tangency circle, passing through `q` <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
7.  This total distance along the cone between the two tangency circles is constant, regardless of the choice of `q` on the ellipse <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

This elegant proof, first discovered by Germinal Pierre Dandelin in 1822, confirms that slicing a cone produces a curve with the constant focal sum property, thus establishing the equivalence between the conic section definition and the thumbtack construction <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. These spheres are now known as Dandelin spheres <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. The same trick can also be used to show that slicing a cylinder at an angle results in an ellipse <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, and it also demonstrates why stretching a circle yields the same family of curves <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## Significance of the Proof

This [[proof_of_slicing_a_cone_to_form_an_ellipse | proof of slicing a cone to form an ellipse]] is considered a prime example of mathematical beauty because <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:
*   It is substantive and beautiful without requiring extensive mathematical background <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   It highlights a common feature of mathematics: often, there isn't one "most fundamental" way to define something; what truly matters is demonstrating equivalences between different definitions <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   The proof showcases a pivotal moment of creative construction—the addition of the two spheres—within a largely systematic and principled approach <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This type of creative insight is a thought-provoking aspect of mathematical discovery <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

Paul Lockhart, in "Measurement," eloquently describes the experience of encountering such a proof:
> <cite>"Why would anyone think of that? It's not a step in any logical chain of reasoning, it's a new idea, a new object, an invention. And like all great inventions, it seems to appear out of nowhere, completely fresh and unexpected, utterly original. The world is different for it."</cite> <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>

While ingenious, such "miracles" in mathematics can often be viewed as the result of accumulated experience and immersion in related problems <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. For instance, relating lengths is a common tactic in [[geometric_properties_of_ellipses | geometry]], and the consistent property of tangent lines to spheres provides a means to do so <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. This perspective transforms the idea of genius from mesmerizing to actively inspirational <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.