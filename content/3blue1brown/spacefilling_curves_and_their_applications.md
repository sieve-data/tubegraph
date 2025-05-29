---
title: spacefilling curves and their applications
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

[[spacefilling curves and their applications | Space-filling curves]] are intriguing [[mathematical_functions_and_graphs | mathematical functions and graphs]] that are both visually dynamic and prompt philosophical inquiries into how infinite mathematical concepts can be applied in finite contexts <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The substance of many mathematical results, especially those involving infinite quantities, often makes sense only in an infinite world <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, these infinite concepts can be surprisingly useful in real-world, finite applications <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Application: Translating Images to Sound

Consider the challenge of creating software that allows people to "see with their ears" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This involves taking image data from a camera and [[translating_image_data_to_sound_using_hilbert_curves | translating image data to sound using Hilbert curves]] in a meaningful way <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The premise is that the human brain is adaptable enough to build intuition from visual information, even when the raw data is presented in a different format <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

To facilitate initial experiments, images could be processed at a low resolution, such as 256x256 pixels <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Each pixel within this square grid would need to be associated with a unique frequency value <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. A brighter pixel would correspond to a louder frequency, and a darker pixel to a quieter one <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. The resulting sound would be a cacophony of overlaid frequencies, which the brain would ideally learn to interpret <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### The Challenge: 2D to 1D Mapping

The core difficulty lies in mapping two-dimensional pixel space to one-dimensional frequency space <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. While a random mapping could be tried, it is more beneficial to leverage existing human intuition about sound <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Ideally, frequencies that are close together in the sound spectrum should correspond to pixels that are close together in the image <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This ensures that even if two nearby frequencies are hard to distinguish, they refer to the same general location in the image <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

To achieve this, one could define a way to weave a line through every pixel <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. By fixing each pixel to a spot on this line and then straightening the line, it can be interpreted as a frequency space, establishing a direct association between pixels and frequencies <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Snake Curve vs. Hilbert Curve

One simple weaving method is to traverse the pixels one row at a time, alternating direction (left to right, then right to left) as it moves up the pixel space <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This is informally known as a "Snake Curve" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

However, a better option is the [[hilberts_curves_and_infinite_math | Hilbert curve]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. An actual [[hilberts_curves_and_infinite_math | Hilbert curve]] is the limit of an infinite family of curves, which can be thought of as "pseudo-Hilbert curves" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

#### Constructing Pseudo-Hilbert Curves
Pseudo-Hilbert curves are constructed iteratively:
*   **Order-one pseudo-Hilbert curve**: Divide a square into a 2x2 grid. Connect the center of the lower-left quadrant to the upper-left, then to the upper-right, and finally down to the lower-right <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Order-two pseudo-Hilbert curve**: Subdivide the square into a 4x4 grid. Place a miniature order-one pseudo-Hilbert curve inside each of the four main quadrants <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. To ensure smooth connections between quadrants, the mini-curves in the lower-left and lower-right quadrants are flipped <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Order-three pseudo-Hilbert curve**: Divide the square into an 8x8 grid. Place an order-two pseudo-Hilbert curve in each quadrant, flipping the lower-left and lower-right appropriately, and connect them tip to tail <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

This pattern continues for higher orders <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Stability During Resolution Upgrades
The key advantage of [[hilberts_curves_and_infinite_math | Hilbert curves]] over Snake curves for the sound-to-sight application is their stability during resolution upgrades <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

*   **Snake Curve**: If the resolution of the image is increased (e.g., from 256x256 to 512x512), many points on the frequency line would map to completely different parts of pixel space <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This would force users to re-learn their intuitions, as the correspondence between frequencies and spatial points would change drastically <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Hilbert Curve**: As the order of a pseudo-Hilbert curve increases, a given point on the line moves around less and less, merely approaching a more specific point in space <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This allows users to fine-tune their existing intuitions rather than having to relearn everything <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This makes the [[hilberts_curves_and_infinite_math | Hilbert curve]] approach ideally suited for this specific application <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

## Origins in Infinite Mathematics

The original motivation for defining [[hilberts_curves_and_infinite_math | Hilbert curves]] arose in the late 19th century, following Cantor's research on infinity <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Mathematicians sought a mapping from a one-dimensional line into two-dimensional space such that the line would pass through every single point in that space <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This refers to continuous, infinitely dense space, not a finite grid of pixels <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

Before 1890, many believed this was impossible – how could a line with zero area fill an infinite area of space <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>? However, Peano discovered the first space-filling curve, followed by Hilbert in 1891 with his slightly simpler version <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. While these curves technically fill a square, filling all of space is an extension of this concept <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

In mathematics, the term "curve" refers to a line running through space, even if it has jagged corners <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. For a space-filling curve, which consists of nothing but sharp corners, "space-filling fractal" might be a more intuitive name, though "curve" remains the standard mathematical term <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### The Hilbert Curve as a Limit

None of the finite pseudo-Hilbert curves used for pixelated space are true space-filling curves <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. When considered in continuous space, these pseudo-curves only pass through a tiny, zero-area slice of any given region, not every point <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. An actual, "bonafide" [[hilberts_curves_and_infinite_math | Hilbert curve]] is defined as the limit of all these pseudo-Hilbert curves <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

To define this limit rigorously, these curves are formalized as [[mathematical_functions_and_graphs | mathematical functions and graphs]] that take a single number (between 0 and 1, representing a point on a line) as input and output a pair of numbers (coordinates in 2D space) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

#### Understanding Continuity
A core property that makes such a function a "curve" is continuity <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

> [!definition] Continuity
> A function is continuous if its output does not suddenly jump when its input changes smoothly <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. More formally:
> 1.  Consider an input point `a` and its corresponding output `b`.
> 2.  Draw a small circle around `a` (in the input space) and observe where all the input points within that circle are mapped in the output space.
> 3.  Draw the smallest circle around `b` (in the output space) that contains all these mapped outputs <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
> 4.  If the function is discontinuous at `a`, there will be a lower bound on the size of the circle around `b`, no matter how small the circle around `a` is <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
> 5.  If the circle around `b` can be made as small as desired by sufficiently small choices for circles around `a`, then the function is continuous at `a` <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
> A function is continuous overall if it is continuous at every possible input point <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Defining the Hilbert Curve Function
The sequence of pseudo-Hilbert curves has a critical property: for any given input point (e.g., 0.3), applying each successive pseudo-Hilbert curve function to this point yields outputs that approach a particular point in space <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This convergence of outputs ensures that the [[hilberts_curves_and_infinite_math | Hilbert curve]] function is well-defined <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This is not true for Snake curves, where outputs become erratic with increasing resolution <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

The [[hilberts_curves_and_infinite_math | Hilbert curve]] function, for a given input value, is defined as the limit of the sequence of points in 2D space obtained by applying each successive pseudo-Hilbert curve function to that input <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

To prove that this defines a space-filling curve, three things must be demonstrated:
1.  **Well-defined Function**: Prove that the outputs of the pseudo-Hilbert curve functions indeed converge <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
2.  **Continuity**: Show that this function is continuous, meaning it produces a "curve" <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
3.  **Space-filling**: Prove that every single point in the unit square is an output of this function <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
All three of these facts are true <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

The concept can be extended to fill all of space by tiling space with squares and chaining [[hilberts_curves_and_infinite_math | Hilbert curves]] together in a spiraling pattern <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This maps the entire positive real number line into all of 2D space <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This highlights that a line, a fundamentally thin object, can traverse and hit every point in an infinitely extending and dense space <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

## The Connection Between Infinite and Finite Worlds

The core property that makes pseudo-Hilbert curves useful, both in the sound-to-sight application and in their infinite origins, is that points on the curve move around less and less as the order of the curves increases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

*   In the sound-to-sight application, this means upgrading to higher resolutions does not necessitate retraining senses <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
*   For mathematicians studying continuous space, this property ensures that defining the limit of a sequence of curves is meaningful <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

This profound connection between the infinite and finite worlds is a recurring theme in mathematics <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Often, the same patterns and constructs used to define and prove infinite facts have directly useful finite analogs <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

Furthermore, theorems about an infinite object can frequently be viewed as equivalent to theorems concerning a family of finite objects <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. For instance, formalizing the stability of a curve as camera resolution increases effectively defines what it means for a sequence of curves to have a limit <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. An infinite object, whether a sequence or a fractal, can encapsulate a truth about a family of finite objects in a particularly clean way <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

This emphasizes that even abstract mathematical statements, seemingly far removed from reality, can hold insights for practical applications, like using [[hilberts_curves_and_infinite_math | Hilbert curves]] for [[translating_image_data_to_sound_using_hilbert_curves | translating image data to sound using Hilbert curves]] <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.