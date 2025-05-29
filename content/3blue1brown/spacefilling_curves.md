---
title: Spacefilling curves
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

[[spacefilling curves | Space-filling curves]] are fascinating mathematical constructs that are enjoyable to animate and prompt discussion on a philosophical question: how can mathematical results dealing with infinite quantities be useful in a finite context? <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>

> [!question] The Philosophical Question
> Math often deals with infinite quantities, sometimes so intimately that the very substance of a result only actually makes sense in an infinite world. How can these results ever be useful in a finite context? <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
> This question is best discussed after examining concrete cases and the underlying mathematics. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

## Application: Sound-to-Sight Software

One practical application of [[spacefilling curves | space-filling curves]], specifically the [[hilbert_curve_and_its_applications | Hilbert curve]], lies in software development, such as a hypothetical "sound-to-sight" application. <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a> This software would convert camera data into meaningful sound, leveraging the brain's plasticity to build intuition from data presented in a different format. <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

### The Challenge: Mapping Dimensions
The core challenge is to associate each pixel in a two-dimensional image (e.g., 256x256 pixels) with a unique frequency value in one-dimensional frequency space. <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> When a pixel is brighter, its associated frequency would be played louder; when darker, quieter. <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

While a random mapping could be attempted, it's beneficial to leverage existing human intuitions about sound. <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> Ideally, frequencies that are close together in sound space should correspond to pixels that are close together in image space. <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a> This ensures that if the ear has difficulty distinguishing nearby frequencies, they still refer to the same basic point in space. <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>

### Weaving a Line Through Pixels
To achieve this, one can define a method to weave a line through each pixel, fixing each pixel to a spot on that line. <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a> Unraveling this "thread" into a straight line allows it to be interpreted as frequency space, thus associating pixels with frequencies. <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

#### Snake Curve
A simple weaving method is the "Snake Curve," which traverses one row at a time, alternating between left and right as it moves up the pixel space. <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>

#### Pseudo-Hilbert Curves
A more effective approach involves using a [[hilbert_curve_and_its_applications | Hilbert curve]]. <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> What is referred to as a "pseudo-Hilbert curve" is an infinite family of curves defined by an iterative process:

*   **Order-one:** Divide a square into a 2x2 grid. Connect the center of the lower-left quadrant to the center of the upper-left, then to the upper-right, and down to the lower-right. <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
*   **Order-two:** Subdivide the square into a 4x4 grid. Trace a miniature order-one pseudo-Hilbert curve within each quadrant. The curves in the lower-left and lower-right quadrants are flipped to ensure smooth connections between quadrants. <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>
*   **Higher Orders:** The pattern continues, with an order-N curve involving an order-(N-1) curve in each quadrant, appropriately flipped and connected. <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>

For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used. <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a> This weaving method defines a function from pixel space to frequency space. <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>

### Advantage of Pseudo-Hilbert Curves: Stability
The significant advantage of pseudo-Hilbert curves over a Snake Curve lies in their stability when resolution increases. <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>

*   With a Snake Curve, upgrading from 256x256 to 512x512 resolution would cause many points on the frequency line to map to entirely different parts of pixel space. Users would have to re-learn their sight-via-sound intuitions. <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>
*   With the [[hilbert_curve_and_its_applications | Hilbert curve]] technique, as the order of a pseudo-Hilbert curve increases, a given point on the line moves less and less, approaching a more specific point in space. <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a> This allows users to fine-tune their intuitions rather than relearn everything. <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>

## Origins in Infinite Mathematics

The original motivation for [[spacefilling curves | space-filling curves]] emerged near the end of the 19th century, following Cantor's research on infinity. <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a> Mathematicians sought a mapping from a one-dimensional line into two-dimensional space such that the line passes through every single point in that space. <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>

This concept refers to continuous space, which is infinite, not a finite grid of pixels. The goal was for a line, which is infinitesimally thin and has zero area, to somehow pass through every infinitely many points making up the infinite area of space. <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>

Before 1890, this was widely considered impossible. However, Peano discovered the first [[spacefilling curves | space-filling curve]] in 1890, and [[hilbert_curve_and_its_applications | Hilbert]] followed with his slightly simpler version in 1891. <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a> While these curves technically fill a square, filling all of space is an extension. <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>

In mathematics, the word "curve" can refer to a line running through space even if it has jagged corners, which can be counterintuitive for [[spacefilling curves | space-filling curves]] that consist of sharp corners. Some prefer the term "space-filling fractal." <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>

### The True Hilbert Curve
None of the pseudo-Hilbert curves, no matter how high their order, qualify as a true [[spacefilling curves | space-filling curve]]. <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a> When viewed in continuous space, the pseudo-Hilbert curve only passes through an infinitesimally small, zero-area slice of any given pixel. <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>

An actual, bonafide [[hilbert_curve_and_its_applications | Hilbert curve]] is defined as the *limit* of all these pseudo-Hilbert curves. <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>

### Defining the Limit Rigorously
To define this limit rigorously, the curves are formalized as functions that take a single number between 0 and 1 (a point on the line) as input and output a pair of numbers (coordinates in 2D space). <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>

#### The Concept of [[continuity_and_function_limits_in_mathematical_curves | Continuity]]
A core property that makes such a function a "curve" (and not just any association of numbers) is [[continuity_and_function_limits_in_mathematical_curves | continuity]]. <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a> The intuition behind [[continuity_and_function_limits_in_mathematical_curves | continuity]] is that the function's output should not suddenly jump when the input changes smoothly. <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>

Mathematically, [[continuity_and_function_limits_in_mathematical_curves | continuity]] at a point `a` means that for any desired smallness of the output circle around `b` (the function's output at `a`), there exists a sufficiently small input circle around `a` such that all points within the input circle map to points within the output circle. <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a> If there's a lower bound on the size of the output circle regardless of the input circle's smallness, the function is discontinuous. <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a> A function is continuous if it is continuous at every input point. <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

#### The [[hilbert_curve_and_its_applications | Hilbert Curve]] as a Limit
The sequence of pseudo-Hilbert curves possesses a crucial property: for a given input point, the corresponding outputs of successive pseudo-Hilbert curve functions approach a particular point in space. <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a> This convergence is not true for Snake Curves or most other sequences of curves filling pixelated space. <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>

The [[hilbert_curve_and_its_applications | Hilbert curve]] function is defined such that for any input value between 0 and 1, its output is the limit of the sequence of points in 2D space generated by applying each successive pseudo-Hilbert curve function to that input. <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a> This makes it a well-defined function because the pseudo-Hilbert curve outputs always converge. <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>

To prove that this limit function is a [[spacefilling curves | space-filling curve]], one must:
1.  Verify that the outputs of the pseudo-Hilbert curve functions converge. <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>
2.  Show that this function is continuous (i.e., it is a curve). <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>
3.  Prove that it fills space, meaning every single point in the unit square is an output of this function. <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>
All three of these facts are true. <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>

A [[spacefilling curves | space-filling curve]] can be extended to fill all of space by tiling space with squares and chaining [[hilbert_curve_and_its_applications | Hilbert curves]] together in a spiraling pattern of tiles. <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a> This maps the entire positive real number line into all of 2D space. <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>

## The Connection Between Infinite and Finite Worlds

The core property that makes pseudo-Hilbert curves useful in both the sound-to-sight application and their infinite origins is the stability of points on the curve: they move less and less as the order of the curves increases. <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>

*   For image translation, this meant higher resolutions didn't require retraining senses. <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>
*   For mathematicians defining [[spacefilling curves | space-filling curves]], this property ensured that taking the limit of a sequence of curves was meaningful. <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>

This connection between the infinite and finite worlds is more of a rule than an exception in mathematics. <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a> It's not that infinite results are directly useful, but rather that the same patterns and constructs used to define and prove infinite facts have finite analogs that *are* directly useful. <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>

Often, theorems about an infinite object are equivalent to theorems about a family of finite objects. <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a> For instance, formalizing what it means for a curve to stay stable as camera resolution increases effectively leads to defining what it means for a sequence of curves to have a limit. <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a> A statement about an infinite object can be seen as a clean way to encapsulate a truth about a family of finite objects. <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>

The lesson is to always look "under the hood" at the nuts and bolts of what is being said, even when a mathematical statement seems far removed from reality. <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a> This can yield unexpected insights, such as [[curve design | curve design]] for "seeing with your ears" from the study of [[spacefilling curves | space-filling curves]]. <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>