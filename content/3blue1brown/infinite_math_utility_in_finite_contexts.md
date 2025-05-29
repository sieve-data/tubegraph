---
title: Infinite math utility in finite contexts
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

Mathematics frequently engages with [[concept_of_infinite_sums_in_mathematics | infinite quantities]], so profoundly that the essence of a result may only fully make sense in an infinite setting <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This raises a key philosophical question: How can these infinite results be useful in finite contexts <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>? This article explores this question through the concrete example of space-filling curves <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Case Study: Sound-to-Sight Application

Consider the challenge of creating software that allows people to "see with their ears" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This involves translating camera data into meaningful sound <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The idea relies on the brain's plasticity to build [[spatial_intuition_in_math | intuition]] even when raw data is scrambled <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. For initial experiments, images might be treated at a low resolution, like 256x256 pixels <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, represented as a square grid where each cell is a pixel <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

The core problem is to associate each pixel in the two-dimensional "pixel space" with a unique value in the one-dimensional "frequency space" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a> <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. A brighter pixel would result in a louder associated frequency, and a darker pixel in a quieter one <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### The Challenge of Mapping Dimensions

While a random mapping could be tried, leveraging existing human [[mathematical_intuition_and_counterintuitive_results | intuition]] about sound is preferable <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. A crucial desire is for frequencies close together in frequency space to remain close together in pixel space <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This ensures that even if two nearby frequencies are hard to distinguish, they still refer to roughly the same point in space <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

One way to achieve this is to weave a line through every pixel <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. If each pixel is fixed to a spot on this line, and the line is then straightened, it can be interpreted as a frequency space, thus associating pixels with frequencies <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

#### Snake Curve vs. Hilbert Curve

A simple weaving method is the "Snake Curve," which goes one row at a time, alternating left and right as it moves up the pixel space <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a> <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

However, a "Hilbert curve" offers a significant advantage <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The Hilbert curve is part of an [[concept_of_infinite_sums_in_mathematics | infinite family]] of "pseudo-Hilbert curves" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. These are constructed iteratively:
*   **Order-one:** Divide a square into a 2x2 grid and connect the centers of the lower-left, upper-left, upper-right, and lower-right quadrants <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Order-two:** Subdivide into a 4x4 grid. Each quadrant contains a miniature order-one pseudo-Hilbert curve. The curves in the lower-left and lower-right quadrants are flipped to ensure smooth connections <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   This pattern continues for higher orders <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

#### The Advantage: Stability Across Resolutions

The key benefit of the Hilbert curve technique over the Snake Curve appears when upgrading resolution <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Snake Curve:** When increasing resolution (e.g., from 256x256 to 512x512), many points on the frequency line would map to entirely different parts of pixel space <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This would force users to re-learn their [[spatial_intuition_in_math | intuitions]] for vision via sound <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Hilbert Curve:** As the order of a pseudo-Hilbert curve increases, a given point on the line moves less and less, merely approaching a more specific point in space <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This allows users to fine-tune their existing [[mathematical_intuition_and_counterintuitive_results | intuitions]] rather than re-learning everything <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Origins in Infinite Mathematics

The utility of Hilbert curves in the sound-to-sight application seems "weirdly perfect" <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. Its original motivation, however, lies in abstract mathematics, particularly in the aftermath of Cantor's work on infinity in the late 19th century <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

Mathematicians sought a mapping from a one-dimensional line into two-dimensional space such that the line would run through every single point in space <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This refers to continuous space, which is infinitely dense and has infinite area, not a finite grid of pixels <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. It was largely considered impossible before 1890 <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

### Space-Filling Curves

In 1890, Peano discovered the first "space-filling curve," followed by Hilbert's slightly simpler version in 1891 <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a> <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. While technically these fill a square, they can be extended to fill all of space <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

*   **Terminology:** In mathematics, a "curve" can have jagged corners <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. A space-filling curve, which consists of only sharp corners, is sometimes called a "space-filling fractal" <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Pseudo-Hilbert vs. Hilbert:** No matter how high the order, pseudo-Hilbert curves are not true space-filling curves <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. A true Hilbert curve is defined as the *limit* of all these pseudo-Hilbert curves <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

### Formalizing the Limit

Defining this limit rigorously requires formalizing what these curves are as functions <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. They are functions that take a single number (a point on a line between 0 and 1) as input and output a pair of numbers (coordinates in 2D space) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

The core property that makes such a function a "curve" is continuity <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Continuity:** A function is continuous if its output does not suddenly jump when the input changes smoothly <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Formally, for any given output point `b`, the "circle" of outputs around `b` can be made as small as desired by choosing a sufficiently small "circle" of inputs around the corresponding input point `a` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a> <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. If there's a lower bound on the size of the output circle, the function is discontinuous <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

The Hilbert curve function is defined using a "limit" because the sequence of outputs from successive pseudo-Hilbert curves, when applied to a given input point, always approaches some particular point in 2D space <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a> <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. This convergence makes the Hilbert curve a well-defined function <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

To prove it's a space-filling curve, one must verify three things <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>:
1.  The pseudo-Hilbert curve outputs converge.
2.  The resulting function is continuous (a curve).
3.  Every point in the unit square is an output of the function (it fills space).
All three of these facts are true <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The curve can then be extended to fill all of 2D space by tiling it with squares and chaining Hilbert curves together <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This means a one-dimensional line can wander through an infinitely rich and dense 2D space, hitting every single point <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

## Connecting Infinite and Finite Worlds

The core property that made pseudo-Hilbert curves useful in both the finite sound-to-sight application and in their infinite origins is the stability of points on the curve: they move less and less as the order increases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. This enabled graceful resolution upgrades in the finite application and ensured the meaningful definition of a limit in the infinite case <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

This connection between the infinite and finite is a common rule in mathematics <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
*   **Analogy:** The same patterns and constructs used to define and prove [[infinite_series_and_sum_computations | infinite facts]] often have finite analogs that are directly useful <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. An example is the relationship between the [[concept_of_infinite_sums_in_mathematics | divergent sum]] of all powers of 2 and the representation of numbers in computers using bits <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   **Equivalence:** The connection is often deeper than a mere analogy. Theorems about an infinite object can be equivalent to theorems about a family of finite objects <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. Formalizing concepts like "curve stability" in a finite context can lead directly to the definition of a limit for a sequence of curves in an infinite context <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.
*   **Encapsulation:** A statement about an [[infinite_and_finite_simple_groups | infinite object]], such as a sequence or fractal, often provides a clean way to encapsulate a truth about a family of finite objects <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

This demonstrates the [[unreasonable_effectiveness_of_mathematics_in_natural_sciences | unreasonable effectiveness of mathematics in natural sciences]] and practical applications. Even when a mathematical statement seems far removed from reality, looking at its underlying "nuts and bolts" can reveal surprising insights and practical utility <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a> <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. This highlights the importance of [[mathematical_problemsolving_and_flexibility | mathematical problem-solving and flexibility]] and the [[challenges_of_formalizing_mathematical_insights | challenges of formalizing mathematical insights]]. It's a testament to the depth and interconnectedness found in [[mathematics in nature | mathematics]].