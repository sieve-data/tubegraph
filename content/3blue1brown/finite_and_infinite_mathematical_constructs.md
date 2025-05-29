---
title: finite and infinite mathematical constructs
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

Mathematical concepts often involve infinite quantities, leading to questions about their practical application in finite contexts <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The substance of many mathematical results only makes sense in an infinite world <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This article explores how insights from such infinite constructs, like [[hilberts_curves_and_infinite_math | space-filling curves]], can be highly useful in finite applications <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## An Application: Sound-to-Sight Software

Consider a software designed to allow people to "see with their ears" by translating camera data into meaningful sound <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The idea is that brains are plastic enough to build intuition from scrambled data <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. For initial experiments, images might be treated at a low resolution, such as 256x256 pixels, represented as a square grid <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

A core challenge is associating each pixel in a two-dimensional space with a unique frequency value in a one-dimensional frequency space <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. When a pixel is brighter, its associated frequency would play louder, and quieter if darker <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Listening to all pixels simultaneously would result in overlaid frequencies <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

To leverage existing human intuitions about sound, it's beneficial if frequencies close together in frequency space also correspond to pixels close together in pixel space <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This ensures that even if nearby frequencies are hard to distinguish, they refer to the same basic point in space <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Weaving a Line Through Pixels

To achieve this, one could weave a line through each pixel, fixing each pixel to a spot on that line <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Unraveling this "thread" creates a straight line that can be interpreted as a frequency space, thus associating pixels with frequencies <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

#### Snake Curve
A simple weaving method is to go one row at a time, alternating left and right, moving up the pixel space <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This is called a "Snake Curve" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

#### Pseudo-[[hilberts_curves_and_infinite_math | Hilbert Curves]]
A more effective alternative is the [[hilberts_curves_and_infinite_math | Hilbert curve]] <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Although technically an infinite family of curves, it can be understood by starting with "pseudo-[[hilberts_curves_and_infinite_math | Hilbert curves]]" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

*   **Order-One Pseudo-[[hilberts_curves_and_infinite_math | Hilbert Curve]]**: Divide a square into a 2x2 grid and connect the centers of the quadrants in a specific order: lower-left to upper-left, to upper-right, then down to lower-right <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Order-Two Pseudo-[[hilberts_curves_and_infinite_math | Hilbert Curve]]**: Subdivide the square into a 4x4 grid <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. A miniature order-one pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] is traced within each quadrant <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. To ensure smooth connections, the curves in the lower-left and lower-right quadrants are flipped <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Higher Orders**: This pattern continues; an order-three curve divides the square into an 8x8 grid, placing order-two curves in each quadrant with appropriate flips <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

For a 256x256 pixel array, an order-eight pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] would be used <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Defining such a curve is essentially defining a function from pixel space to frequency space <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Stability Across Resolutions
The key advantage of [[hilberts_curves_and_infinite_math | Hilbert curves]] over snake curves emerges when considering resolution upgrades <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

*   With a **Snake Curve**, upgrading from 256x256 to 512x512 resolution would cause many points on the frequency line to map to completely different parts of pixel space <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This means users would have to re-learn their intuitions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   With the **[[hilberts_curves_and_infinite_math | Hilbert curve]] technique**, as the order of a pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] increases, a given point on the line moves less and less, approaching a more specific point in space <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This allows users to fine-tune existing intuitions rather than re-learning them <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Origins of Space-Filling Curves in Infinite Math

The original motivation for [[hilberts_curves_and_infinite_math | Hilbert curves]] arose near the end of the 19th century, following Cantor's research on infinity <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Mathematicians sought a mapping from a one-dimensional line into two-dimensional continuous space such that the line passes through *every* single point in space <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This differs from the finite pixel grid; it involves a continuous, infinite space <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The goal was for a line, which has zero area, to somehow fill the infinite area of space by hitting infinitely many points <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Before 1890, this was largely considered impossible <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

*   In 1890, Peano discovered the first of these [[hilberts_curves_and_infinite_math | space-filling curves]] <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   In 1891, Hilbert presented his own slightly simpler [[hilberts_curves_and_infinite_math | space-filling curve]] <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. These technically fill a square, but filling all of space from there is not an issue <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

> [!NOTE] Mathematical Terminology
> In mathematics, "curve" refers to a line running through space, even if it has jagged corners <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. For [[hilberts_curves_and_infinite_math | space-filling curves]], which consist mostly of sharp corners, the term "space-filling fractal" might be more intuitive, though "curve" is the standard <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

None of the pseudo-[[hilberts_curves_and_infinite_math | Hilbert curves]] used for pixelated space count as true [[hilberts_curves_and_infinite_math | space-filling curves]], as they only pass through a tiny, zero-area slice of a continuous pixel when zoomed in <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Defining the Actual Hilbert Curve

A true [[hilberts_curves_and_infinite_math | Hilbert curve]] is not any single pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]], but rather the **limit of all of them** <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

To define this rigorously, these curves are formalized as functions that take a single number between 0 and 1 (a point on a line) as input and output a pair of numbers (coordinates in 2D space) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

For example, an order-2 pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] might map 0.3 to (0.125, 0.75), while an order-3 curve maps the same 0.3 to (0.0758, 0.6875) <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### The Role of [[continuity and mathematical functions | Continuity]]
The core property that makes a function a "curve" is [[continuity and mathematical functions | continuity]] <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

*   **Intuition**: The output of a function should not suddenly jump when the input changes smoothly <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Rigorous Definition**:
    *   Consider an input point `a` and its output `b`.
    *   Draw a small circle around `a` in the input space.
    *   Look at where the function maps all points within that input circle in the output space.
    *   Draw the smallest circle around `b` that contains these outputs <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   If the function *jumps* at `a`, no matter how small the input circle, the output circle around `b` cannot be smaller than that jump <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. The function is **discontinuous** if there's any lower bound on the size of the output circle <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
    *   If the output circle around `b` can be made as small as desired by choosing a sufficiently small input circle around `a`, then the function is **continuous** at `a` <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. A function is continuous if it's continuous at every input point <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### The Limit of Pseudo-[[hilberts_curves_and_infinite_math | Hilbert Curves]]
The sequence of pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] outputs, when applied to a given input point (e.g., 0.3), approaches a particular point in space as the order of the curve increases <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This means the sequence of outputs always stabilizes and approaches a specific point in 2D space <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. This is *not* true for snake curves, where outputs for a given input are wildly erratic as resolution increases <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

Because of this property, a [[hilberts_curves_and_infinite_math | Hilbert curve]] function is defined as the limit of the sequence of points in 2D space generated by applying each successive pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] function to a given input value <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. Since the sequence of pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] outputs always [[concept_of_infinite_sums_and_convergence | converges]], this definition is well-defined <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

To prove that this defines a [[hilberts_curves_and_infinite_math | space-filling curve]], three things must be verified:
1.  The pseudo-[[hilberts_curves_and_infinite_math | Hilbert curve]] function outputs indeed [[concept_of_infinite_sums_and_convergence | converge]], making the function well-defined <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
2.  The resulting function is [[continuity and mathematical functions | continuous]], confirming it's a curve <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
3.  Every single point in the unit square is an output of this function, meaning it fills space <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. All three of these facts are true <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

A [[hilberts_curves_and_infinite_math | Hilbert curve]] can be extended to fill all of 2D space by tiling space with squares and chaining multiple [[hilberts_curves_and_infinite_math | Hilbert curves]] together in a spiraling pattern <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This means an entire positive real number line can be mapped into all of 2D space <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

> [!INFO] [[Paradoxical and nonintuitive mathematical truths | Paradoxical Truth]]
> A line, the platonic form of thinness, can wander through an infinitely extending and richly dense space and hit every single point <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

## The Interplay of Finite and Infinite Worlds

The core property that made pseudo-[[hilberts_curves_and_infinite_math | Hilbert curves]] useful in both the sound-to-sight application and their infinite origins is the stability of points on the curve as the order increases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. For the sound-to-sight application, this meant resolution upgrades didn't require retraining senses <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. For mathematicians, this property ensured that the concept of the limit of a sequence of curves was meaningful <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

This connection between infinite and finite worlds is a recurring theme in mathematics <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Often, the same patterns and constructs used to define and prove infinite facts have finite analogs that are directly useful <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

For instance, formally defining what it means for a curve to remain stable as camera resolution increases is effectively writing the definition of what it means for a sequence of curves to have a limit <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. A statement about an infinite object, such as a sequence or a fractal, can often be viewed as a clean way to encapsulate a truth about a family of finite objects <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

The lesson is to always examine the underlying mechanisms and definitions of even the most abstract mathematical statements, as they often hold insights for practical applications <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.