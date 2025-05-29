---
title: continuity and mathematical functions
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

In the realm of [[finite_and_infinite_mathematical_constructs | mathematics]], concepts often deal with infinite quantities, and the essence of a result may only fully make sense in an infinite context <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, these results can still be incredibly useful in a finite context <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The study of [[Hilberts_curves_and_infinite_math | Hilbert curves]] provides a concrete example of this interplay, particularly in how they relate to the concept of [[mathematical_functions_and_graphs | mathematical functions]] and their continuity <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Functions in Image-to-Sound Translation

Consider software designed to enable "seeing with ears," where camera data is translated into sound <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For initial experiments, images might be processed at a low resolution, such as 256x256 pixels <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The challenge is to associate each pixel in a two-dimensional "pixel space" with a unique frequency value in a one-dimensional "frequency space" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This requires defining a [[mathematical_functions_and_graphs | function]] that maps from the two-dimensional pixel space to the one-dimensional frequency space <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

A desirable property for such a [[mathematical_functions_and_graphs | function]] is that frequencies close together should correspond to pixels close together in the pixel space <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This can be achieved by weaving a line through each pixel, fixing each pixel to a spot on that line, and then interpreting the unravelled straight line as the frequency space <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This method associates pixels with frequencies <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Pseudo-Hilbert Curves as Functions

The concept of [[Hilberts_curves_and_infinite_math | Hilbert curves]] provides an effective way to define such a mapping. These are not a single curve but rather an [[finite_and_infinite_mathematical_constructs | infinite]] family of curves <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

The construction of these "pseudo-Hilbert curves" proceeds iteratively:
*   **Order-one:** Divide a square into a 2x2 grid and connect the centers of the quadrants in a specific "U" shape <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Order-two:** Subdivide the square into a 4x4 grid. Place a miniature order-one pseudo-Hilbert curve inside each of the original 2x2 quadrants, orienting them appropriately (flipping the lower left and lower right) to ensure a smooth connection between quadrants <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Higher Orders:** The pattern continues, with an order-N curve embedding order-(N-1) curves in each quadrant, with appropriate flips and connections <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Defining such a curve that weaves through each pixel is equivalent to defining a [[mathematical_functions_and_graphs | function]] from pixel space to frequency space, as each pixel is associated with a point on the line <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

A key advantage of the [[Hilberts_curves_and_infinite_math | Hilbert curve]] technique over a simpler "snake curve" (which goes row by row) is its stability when increasing resolution <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. With a snake curve, upgrading from 256x256 to 512x512 pixels causes many points on the frequency line to map to entirely different parts of pixel space, requiring users to re-learn their intuitions <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. In contrast, with the [[Hilberts_curves_and_infinite_math | Hilbert curve]], as the order of the pseudo-Hilbert curve increases, a given point on the line moves less and less, approaching a more specific point in space <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This allows users to fine-tune rather than re-learn <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Defining Continuity for Mathematical Functions

To formally define the [[Hilberts_curves_and_infinite_math | Hilbert curve]] and understand its properties, it's necessary to formalize what these curves are as [[mathematical_functions_and_graphs | functions]] <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. These are [[mathematical_functions_and_graphs | functions]] that take a single number (e.g., between 0 and 1, representing a point on a line) as input and output a pair of numbers (coordinates in 2D space) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

The crucial property that distinguishes a curve from any arbitrary association between numbers is **continuity** <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

> [!definition] Continuity
> The intuition behind continuity is that the output of a [[mathematical_functions_and_graphs | function]] should not suddenly jump when its input changes smoothly <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
>
> More rigorously, a [[mathematical_functions_and_graphs | function]] is continuous at an input point 'a' if, for any desired smallness of a circle drawn around the output 'b' (which is the function's output for input 'a'), you can always find a sufficiently small circle around 'a' such that all input points within that 'a'-circle map to points within the 'b'-circle <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
>
> If there's a lower bound on how small the output circle can be made, no matter how small the input circle, then the [[mathematical_functions_and_graphs | function]] is discontinuous at that point <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. A [[mathematical_functions_and_graphs | function]] is continuous as a whole if it is continuous at every possible input point <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

## The Hilbert Curve as a Limit of Functions

An actual, bonafide [[Hilberts_curves_and_infinite_math | Hilbert curve]] is not any one of the pseudo-Hilbert curves, but rather **the limit of all of them** <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This rigorous definition relies on a key property: for a given input point (e.g., 0.3), applying each successive pseudo-Hilbert curve [[mathematical_functions_and_graphs | function]] to this point results in corresponding outputs that approach a particular point in space as the order of the curve increases <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This sequence of outputs always stabilizes and approaches a specific point in 2D space, regardless of the starting input <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. This is unlike snake curves, where outputs associated with a given input become wildly erratic with increasing resolution <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

The [[Hilberts_curves_and_infinite_math | Hilbert curve]] [[mathematical_functions_and_graphs | function]] is then defined as follows: for a given input value, the output is the limit of the sequence of points in 2D space obtained by applying each successive pseudo-Hilbert curve [[mathematical_functions_and_graphs | function]] at that input <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Since the sequence of pseudo-Hilbert curve outputs always converges, this [[mathematical_functions_and_graphs | function]] is well-defined <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

For this to be a true "space-filling curve," three things must be proved <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>:
1.  The outputs of the pseudo-Hilbert curve [[mathematical_functions_and_graphs | functions]] converge, ensuring the [[Hilberts_curves_and_infinite_math | Hilbert curve]] [[mathematical_functions_and_graphs | function]] is well-defined <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
2.  The resulting [[mathematical_functions_and_graphs | function]] is continuous, meaning it qualifies as a "curve" <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
3.  Every single point in the unit square is an output of this [[mathematical_functions_and_graphs | function]], confirming it fills space <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

These three facts are indeed true <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The [[Hilberts_curves_and_infinite_math | Hilbert curve]] can even be extended to fill all of continuous space by tiling space with squares and chaining [[Hilberts_curves_and_infinite_math | Hilbert curves]] together in a spiraling pattern <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This demonstrates that a one-dimensional line can hit every single point in an infinitely extending, richly dense two-dimensional space <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

## Connection Between Finite and Infinite

The core property that makes pseudo-Hilbert curves useful both in the finite sound-to-sight application and in their [[finite_and_infinite_mathematical_constructs | infinite]] origins is that points on the curve move less and less as the order of the curves increases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. In the finite context, this meant stable intuitions upon resolution upgrades <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. For mathematicians, this property ensured that the limit of a sequence of curves was a meaningful concept <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

This connection between the [[finite_and_infinite_mathematical_constructs | infinite]] and [[finite_and_infinite_mathematical_constructs | finite]] worlds is common in [[finite_and_infinite_mathematical_constructs | mathematics]] <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Often, the same patterns and constructs used to define and prove [[finite_and_infinite_mathematical_constructs | infinite]] facts have [[finite_and_infinite_mathematical_constructs | finite]] analogs that are directly useful <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. Theorems about an [[finite_and_infinite_mathematical_constructs | infinite]] object are frequently equivalent to theorems about a family of [[finite_and_infinite_mathematical_constructs | finite]] objects <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. For example, formalizing curve stability for increasing camera resolution would lead directly to the definition of a limit for a sequence of curves <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. An [[finite_and_infinite_mathematical_constructs | infinite]] object or fractal can be seen as a clean way to encapsulate a truth about a family of [[finite_and_infinite_mathematical_constructs | finite]] objects <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.