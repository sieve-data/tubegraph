---
title: Hilberts curves and infinite math
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

Space-filling curves are a fascinating topic in mathematics, offering insights into the relationship between [[finite_and_infinite_mathematical_constructs | finite and infinite mathematical constructs]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While mathematics often deals with infinite quantities, raising questions about their utility in [[finite_and_infinite_mathematical_constructs | finite contexts]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, studying concrete examples like the Hilbert curve can clarify these philosophical points <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Application: Sound-to-Sight Software

One potential application of Hilbert curves is in software designed to translate visual data into sound, allowing people to "see with their ears" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The brain's plasticity suggests it could build intuition from scrambled data <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

For initial experiments, images might be treated at a low resolution, such as 256x256 pixels, represented as a square grid <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The challenge is to associate each pixel with a unique frequency value, where brighter pixels correspond to louder frequencies <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This requires mapping a two-dimensional pixel space to a one-dimensional frequency space <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

To leverage existing human intuitions about sound, it's beneficial if nearby frequencies in the sound space also correspond to nearby points in the pixel space <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This can be achieved by weaving a line through each pixel, fixing each pixel to a spot on that line, and then interpreting the unravelled line as a frequency space <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Snake Curve vs. Hilbert Curve

An intuitive weaving method is the "Snake Curve," which traverses pixels one row at a time, alternating direction <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. However, a more advantageous approach involves a "pseudo-Hilbert curve" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

Pseudo-Hilbert curves are defined by an iterative process:
*   **Order-one**: Divide a square into a 2x2 grid, connecting the centers of the lower-left, upper-left, upper-right, and lower-right quadrants <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Order-two**: Subdivide the square into a 4x4 grid. Place miniature order-one pseudo-Hilbert curves in each quadrant. The curves in the lower-left and lower-right quadrants are flipped to ensure smooth connections between them and the path <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   This pattern continues for higher orders, with an order-eight pseudo-Hilbert curve used for a 256x256 pixel array <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. Defining such a curve effectively creates a [[mathematical_functions_and_graphs | function]] from pixel space to frequency space <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Stability with Resolution Upgrades

A key advantage of the Hilbert curve over the snake curve lies in its stability when resolution increases <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   With a **snake curve**, upgrading from 256x256 to 512x512 pixels would cause many points on the frequency line to map to entirely different parts of the pixel space <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This would require users to re-learn their visual intuitions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   With the **Hilbert curve technique**, as the order of a pseudo-Hilbert curve increases, a given point on the line moves less and less, approaching a more specific point in space <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This allows users to fine-tune their intuitions rather than completely re-learning <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Origins in Infinite Math

The original motivation for Hilbert curves arose from late 19th-century mathematics, spurred by Cantor's research on infinity <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Mathematicians sought a mapping from a one-dimensional line into two-dimensional space such that the line would run through every single point in that space <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This concept differs from the finite pixel grid; it refers to continuous space, which is "very infinite" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The goal was for a line of zero area to somehow pass through infinitely many points of infinite area <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Before 1890, this was widely considered impossible <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. However, Peano discovered the first space-filling curve in 1890, followed by Hilbert's slightly simpler version in 1891 <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

Mathematicians use the term "curve" for a line through space, even if it has jagged corners, which is counterintuitive for a space-filling curve that often consists of sharp corners <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. A better name might be "space-filling [[introduction_to_newtons_fractals_and_its_infinite_complexity | fractal]]" <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

None of the finite-order pseudo-Hilbert curves are true space-filling curves, as they only pass through a zero-area slice of any continuous pixel <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. An actual Hilbert curve is defined as the *limit* of all these pseudo-Hilbert curves <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

### Defining Continuity

To rigorously define this limit, curves are formalized as [[mathematical_functions_and_graphs | functions]] that take a single number (a point on a line) as input and output a pair of numbers (coordinates in 2D space) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

The core property that makes such a [[mathematical_functions_and_graphs | function]] a "curve" is **continuity** <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Intuitively, continuity means the output of the [[mathematical_functions_and_graphs | function]] doesn't suddenly jump when the input changes smoothly <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

More formally, a [[mathematical_functions_and_graphs | function]] is continuous at an input point `a` if, for any desired small circle around the output `b`, one can find a sufficiently small circle around `a` such that all input points within `a`'s circle map to within `b`'s circle <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. If there's a lower bound on the size of the output circle regardless of the input circle's size, the function is discontinuous <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. A [[mathematical_functions_and_graphs | function]] is continuous overall if it's continuous at every input point <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### The Hilbert Curve as a Limit

The Hilbert curve is defined using a "wonderful property" of the pseudo-Hilbert curve sequence <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>: for any given input point, applying each successive pseudo-Hilbert curve function to this point yields outputs that approach a particular point in space <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This [[concept_of_infinite_sums_and_convergence | convergence]] is crucial and does not happen with snake curves, where outputs for a given input are erratic <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

The Hilbert curve [[mathematical_functions_and_graphs | function]]'s output for a given input value (between 0 and 1) is defined as the limit of the sequence of 2D points obtained by applying each successive pseudo-Hilbert curve function at that input <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. Because these sequences of outputs always [[concept_of_infinite_sums_and_convergence | converge]], the Hilbert curve function is well-defined <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

To prove that this yields a space-filling curve, one must verify:
1.  The pseudo-Hilbert curve function outputs indeed [[concept_of_infinite_sums_and_convergence | converge]] (well-defined).
2.  The resulting [[mathematical_functions_and_graphs | function]] is continuous (a curve).
3.  Every single point in the unit square is an output of this [[mathematical_functions_and_graphs | function]] (space-filling) <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

It is possible to extend this concept to a curve that fills all of space by tiling space with squares and chaining Hilbert curves together in a spiraling pattern <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This means the entire positive real number line can be mapped into all of 2D space <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

## Connecting Finite and Infinite Worlds

The core property that made pseudo-Hilbert curves useful in both the finite sound-to-sight application and their infinite origins is the stability of points on the curve; they move less and less as the order increases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   In the sound-to-sight application, this meant upgrading resolution didn't require re-training senses <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
*   For mathematicians, this property ensured that talking about the limit of a sequence of curves was a meaningful mathematical concept <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

This connection between [[finite_and_infinite_mathematical_constructs | infinite and finite worlds]] is common in mathematics <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Often, the same patterns and constructs used to define infinite facts have [[finite_and_infinite_mathematical_constructs | finite analogs]] that are directly useful <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. For example, understanding the formal definition of a sequence of curves having a limit is directly related to ensuring stability in resolution upgrades <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

A statement about an [[finite_and_infinite_mathematical_constructs | infinite object]], such as a sequence or a fractal, can often be seen as a clean way to encapsulate a truth about a family of [[finite_and_infinite_mathematical_constructs | finite objects]] <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. The lesson is to always examine the underlying mechanics of even abstract mathematical statements, as they can yield [[mathematical_insights_and_elegant_solutions | insights]] for practical applications <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.