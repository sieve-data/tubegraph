---
title: Hilbert curve and its applications
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

The Hilbert curve is a type of [[spacefilling_curves | space-filling curve]] that is not only visually interesting but also provides a concrete example to address a philosophical question in mathematics: how can results dealing with infinite quantities be useful in a finite context? <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>

## Philosophical Question: Infinite vs. Finite <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>

Mathematics often deals with infinite quantities, sometimes so fundamentally that a result only makes sense in an infinite world. This raises the question of how such results can be applied in finite contexts <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This philosophical discussion is best approached after examining concrete cases and the underlying mathematics <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Application: Sound-to-Sight Software <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

Consider developing software that allows people to "see with their ears" by translating camera data into meaningful sound <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The idea is that brains are adaptable enough to build intuition from scrambled data formats <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

To begin, images might be treated with a low resolution, such as 256x256 pixels, represented as a square grid <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. A key challenge is associating each pixel with a unique frequency value, such that brighter pixels correspond to louder frequencies and darker pixels to quieter ones <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

The difficulty lies in translating two-dimensional pixel space into one-dimensional frequency space <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. While a random mapping could be used, it's beneficial to leverage existing human intuitions about sound <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Ideally, frequencies that are close together should map to pixels that are also close together <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Weaving a Line Through Pixels <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>

To achieve this, one could define a path or "curve" that weaves through each pixel <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. By fixing each pixel to a spot on this line and unraveling it, the line can be interpreted as frequency space, creating an association between pixels and frequencies <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

*   **Snake Curve**: A simple weaving method involves going one row at a time, alternating left and right <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This is analogous to the game Snake <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

*   **Hilbert Curve**: A more effective method uses a Hilbert curve <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

    *   **Pseudo-Hilbert Curves**: The Hilbert curve is best understood through an infinite family of "pseudo-Hilbert curves" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
        *   **Order-one**: Divides a square into a 2x2 grid, connecting the center of the lower-left, upper-left, upper-right, and lower-right quadrants sequentially <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
        *   **Order-two**: Subdivides the square into a 4x4 grid. A miniature order-one pseudo-Hilbert curve is traced within each quadrant, with the curves in the lower-left and lower-right quadrants flipped to ensure a continuous connection between them <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
        *   **Higher Orders**: This pattern continues, where an order-N curve uses order-(N-1) curves within its quadrants, appropriately flipped and connected <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Stability Across Resolutions <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>

The critical advantage of the Hilbert curve technique over the Snake curve lies in its stability when resolution increases <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

*   With a **Snake curve**, increasing the resolution (e.g., from 256x256 to 512x512) causes many points on the frequency line to map to drastically different parts of the pixel space <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This means users would have to re-learn their sound-to-sight intuitions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   With a **Hilbert curve**, as the order of the pseudo-Hilbert curve increases, a given point on the line moves less and less, merely approaching a more specific point in space <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This allows users to fine-tune their intuitions rather than completely re-learning <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This makes the Hilbert curve approach ideal for applications requiring scalable resolution <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

## Origins in Infinite Mathematics <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>

The original motivation for defining Hilbert curves came from late 19th-century mathematics, after Cantor's work on infinity <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Mathematicians sought a continuous mapping from a one-dimensional line into two-dimensional space that would run through every single point in that space <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This refers to continuous, infinite space, not a finite grid of pixels <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

Before 1890, this was considered impossible, but Peano discovered the first [[spacefilling_curves | space-filling curves]] in 1890 <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Hilbert followed in 1891 with his own simpler [[spacefilling_curves | space-filling curve]] <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. While these curves technically fill a square, they can be extended to fill all of space <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Defining a Hilbert Curve <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>

A true Hilbert curve is not any single pseudo-Hilbert curve, but rather the [[continuity_and_function_limits_in_mathematical_curves | limit]] of all of them <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. Rigorously defining this [[continuity_and_function_limits_in_mathematical_curves | limit]] requires formalizing the curves as functions <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

*   **Function Definition**: A pseudo-Hilbert curve function takes a single number (e.g., between 0 and 1, representing a point on a line) as input and outputs a pair of numbers (coordinates in 2D space) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For example, an order-2 pseudo-Hilbert curve maps 0.3 to (0.125, 0.75) <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

*   **[[continuity_and_function_limits_in_mathematical_curves | Continuity]]**: A core property for a function to be considered a "curve" (even with jagged corners, as allowed in mathematical terminology) is [[continuity_and_function_limits_in_mathematical_curves | continuity]] <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   The intuition for [[continuity_and_function_limits_in_mathematical_curves | continuity]] is that the function's output should not suddenly jump when the input changes smoothly <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   Rigorously, a function is continuous at a point `a` if, for any desired smallness of a circle around the output `b` (the function's value at `a`), there exists a sufficiently small circle around `a` such that all input points within that circle map to outputs within the circle around `b` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. If there's a lower bound on the size of the output circle regardless of the input circle's size, the function is discontinuous <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

*   **Hilbert Curve as a [[continuity_and_function_limits_in_mathematical_curves | Limit]]**: The sequence of pseudo-Hilbert curves has a critical property: for any given input point, applying each successive pseudo-Hilbert curve function to it yields outputs that approach a particular point in space <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This contrasts sharply with Snake curves, where outputs become erratic with increasing resolution <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   The Hilbert curve function is defined such that for a given input, its output is the [[continuity_and_function_limits_in_mathematical_curves | limit]] of the sequence of 2D points obtained by applying each successive pseudo-Hilbert curve function at that input <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This definition is well-defined because the sequence of pseudo-Hilbert curve outputs always converges <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
    *   To prove that this defines a [[spacefilling_curves | space-filling curve]], one must demonstrate:
        1.  The outputs of pseudo-Hilbert curves converge, proving the function is well-defined <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
        2.  The function is continuous, meaning it's a "curve" <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
        3.  The function fills space, meaning every point in the unit square is an output <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. All three of these facts are true <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

*   **Filling All of Space**: A Hilbert curve can be extended to fill all of 2D space by tiling space with squares and chaining Hilbert curves together in a spiraling pattern, connecting the end of one to the start of the next <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This means the entire positive real number line can be mapped into all of 2D space <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

## Conclusion: Connection Between Infinite and Finite <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>

The core property that makes pseudo-Hilbert curves useful in both the sound-to-sight application and their infinite origins is the stability of points on the curve as the order increases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. In the finite application, this meant upgrades didn't require re-training senses <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. In the infinite context, it ensured that the [[continuity_and_function_limits_in_mathematical_curves | limit]] of the sequence of curves was a meaningful concept <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

This connection between the infinite and finite worlds is a recurring theme in mathematics <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Often, infinite mathematical results are not directly useful in themselves, but the underlying patterns and constructs used to define and prove infinite facts have finite analogs that *are* directly useful <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. Furthermore, many theorems about infinite objects are equivalent to theorems regarding families of finite objects <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. A statement about an infinite object can be seen as a clean way to encapsulate a truth about a family of finite objects <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

This demonstrates that even seemingly abstract mathematical concepts can hold profound insights for practical applications by examining their fundamental structures <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.