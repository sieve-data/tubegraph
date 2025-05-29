---
title: Continuity and function limits in mathematical curves
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

Mathematical concepts involving infinite quantities can often raise the question of their utility in finite contexts <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, insights gained from infinite mathematics, such as the study of [[hilbert_curve_and_its_applications | space-filling curves]], frequently provide direct applications to finite problems <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Application: Sound-to-Sight Software

Consider the hypothetical development of software to enable "seeing with ears," which translates camera data into meaningful sound <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This requires mapping two-dimensional pixel space to one-dimensional frequency space <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. A crucial design principle for such a system is that nearby frequencies should correspond to nearby pixels in the visual field <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

To achieve this, one could define a path, or "curve," that weaves through each pixel in a grid, effectively fixing each pixel to a unique spot on a conceptual frequency line <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Challenges with Resolution Upgrades

A straightforward approach, like a "Snake Curve" (alternating rows left-to-right), has limitations <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. If the software's resolution is increased (e.g., from 256x256 to 512x512 pixels), the mapping from frequency to pixel space can change dramatically <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This would force users to completely relearn their spatial intuitions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## The [[hilbert_curve_and_its_applications | Hilbert Curve]] Solution

An alternative is the [[hilbert_curve_and_its_applications | Hilbert curve]] <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The [[hilbert_curve_and_its_applications | Hilbert curve]] offers a more stable mapping as resolution increases <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This stability means users can fine-tune their intuitions rather than restarting their learning process <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Defining [[hilbert_curve_and_its_applications | Pseudo-Hilbert Curves]]

The [[hilbert_curve_and_its_applications | Hilbert curve]] is understood through a sequence of finite approximations called "pseudo-Hilbert curves" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>:
*   **Order-one:** Divides a square into a 2x2 grid, connecting the centers of quadrants in a U-shape <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Order-two:** Subdivides into a 4x4 grid, placing a miniature order-one curve in each quadrant, with specific rotations to ensure smooth connections <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Higher orders:** The pattern continues, subdividing further and incorporating the previous order's curve in each quadrant, with appropriate flips <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Mathematical Origins and the [[limits_in_calculus | Limit]] of Curves

The original motivation for [[hilbert_curve_and_its_applications | space-filling curves]], dating back to the late 19th century, was to find a mapping from a one-dimensional line into a two-dimensional continuous space, such that the line passes through *every single point* <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This concept, initially thought impossible, was first demonstrated by Peano in 1890, followed by Hilbert's simpler version in 1891 <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>, <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

It's important to note that a "curve" in mathematics includes paths with jagged corners <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. The term "space-filling fractal" might be more intuitive for these shapes <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### The [[limits_in_calculus | Hilbert Curve]] as a [[limits_in_calculus | Limit]]

No finite pseudo-Hilbert curve can truly fill continuous space <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. The actual, bona fide [[hilbert_curve_and_its_applications | Hilbert curve]] is defined as the [[limits_in_calculus | limit]] of the infinite sequence of pseudo-Hilbert curves <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

To understand this rigorously, these curves are formalized as functions that take a single number (a point on a line between 0 and 1) and output a pair of numbers (coordinates in 2D space) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### The Concept of [[continuity_in_mathematical_geometry | Continuity]]

A core property defining such a function as a "curve" is [[continuity_in_mathematical_geometry | continuity]] <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Intuitive Definition:** A function is continuous if its output does not suddenly jump when its input changes smoothly <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Rigorous Definition:** For any given input point `a` and its output `b`, if you can make the circle of outputs around `b` as small as desired by choosing a sufficiently small circle of inputs around `a`, the function is continuous at `a` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>, <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. If there's a lower bound on the size of the output circle, it's discontinuous <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. A function is continuous if it's continuous at every input point <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Defining the [[limits_in_calculus | Hilbert Curve]] Function

The sequence of pseudo-Hilbert curves has a crucial property: for any given input point, the corresponding outputs of successive pseudo-Hilbert curves always converge to a particular point in space <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>, <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. This is not true for a "Snake Curve" <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

The [[hilbert_curve_and_its_applications | Hilbert curve]] function is formally defined by taking the [[limits_in_calculus | limit]] of these converging output points <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>, <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>, <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. Because the outputs consistently converge, this defines a well-behaved function <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

For this function to be a true [[hilbert_curve_and_its_applications | space-filling curve]], three properties must be proven <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>:
1.  The outputs of the pseudo-Hilbert curve functions indeed converge (well-defined) <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
2.  The resulting function is continuous <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
3.  Every single point in the unit square is an output of this function (fills space) <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
All three of these statements are true <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

The concept can be extended to fill all of 2D space by tiling it with squares and chaining [[hilbert_curve_and_its_applications | Hilbert curves]] together <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>, mapping the entire positive real number line into 2D space <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This demonstrates how a one-dimensional line can traverse and hit every point in a continuous, infinitely extending, two-dimensional space <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

## The Connection Between Infinite and Finite

The utility of [[hilbert_curve_and_its_applications | Hilbert curves]] in both the sound-to-sight application and their infinite origins lies in the property that points on the curve move less and less as the order of the curves increases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. In the finite application, this ensures stability upon resolution upgrades <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. In the infinite context, this property allows for the meaningful definition of a [[limits_in_calculus | limit]] for the sequence of curves <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

This connection between infinite and finite mathematics is a recurring theme <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Often, the same mathematical patterns and constructs used to define infinite facts have directly useful finite analogs <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. A theorem about an infinite object can frequently be seen as an encapsulation of a truth about a family of finite objects <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>, <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. Formalizing concepts like "stability as camera resolution increases" directly leads to defining what it means for a sequence of curves to have a [[limits_in_calculus | limit]] <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

Ultimately, even seemingly abstract mathematical statements can reveal practical insights when their underlying mechanics are examined <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.