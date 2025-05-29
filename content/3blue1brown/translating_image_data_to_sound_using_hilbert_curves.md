---
title: translating image data to sound using Hilbert curves
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

## Concept Overview

The idea of "seeing with ears" involves taking [[image_processing_and_convolutions | image processing]] data from a camera and translating it into sound in a meaningful way [00:00:44]. This concept leverages the brain's plasticity, which allows for intuition to be built from sight even when raw data is scrambled into a different format [00:00:56]. Initial experiments might use low-resolution images, such as 256x256 pixels, represented as a square grid where each cell corresponds to a pixel [00:01:08].

## The Challenge: Mapping Dimensions

A primary challenge in this software design is associating each pixel with a unique frequency value [00:01:25]. When a pixel is brighter, its associated frequency is played louder; when darker, the frequency is quieter [00:01:35]. Listening to all pixels simultaneously would result in an overlay of frequencies, with dominant frequencies from brighter regions potentially sounding like a [[harmonious_versus_cacophonous_sounds_in_music | cacophonous mess]] until the brain learns to interpret the information [00:01:43].

The core difficulty lies in the dimensionality mismatch: pixel space is two-dimensional, while frequency space is one-dimensional [00:02:14]. While a random mapping could be attempted, it is more effective to leverage existing human intuitions about sound [00:02:21]. Ideally, frequencies that are close together in the one-dimensional frequency space should map to pixels that are close together in the two-dimensional pixel space [00:02:36]. This ensures that even if an ear struggles to distinguish between two nearby frequencies, they refer to the same basic point in space [00:02:47].

## Weaving a Line Through Pixels

To achieve this, one must define a method to weave a line through each pixel [00:02:57]. If each pixel is fixed to a spot on this line and the line is then unraveled into a straight thread, this thread can be interpreted as a frequency space, thus creating an association from pixels to frequencies [00:03:04].

### The Snake Curve Approach

One straightforward weaving method is to traverse the pixels one row at a time, alternating direction (left to right, then right to left) as it moves up the pixel space [00:03:19]. This is akin to a "Snake Curve" [00:03:27].

However, the Snake Curve has a significant drawback: when upgrading to a higher resolution (e.g., from 256x256 to 512x512 pixels), many points on the frequency line would map to entirely different parts of the pixel space [00:06:16]. For instance, a point halfway along the frequency line might remain halfway up the pixel space but can wildly change its left-to-right position with increased resolution [00:06:27]. This instability would force users to re-learn their visual intuitions from scratch, as the correspondence between spatial points and frequencies would no longer apply [00:06:42].

## The Hilbert Curve Solution

A superior method for this [[spacefilling_curves_and_their_applications | space-filling curve]] application is the [[hilberts_curves_and_infinite_math | Hilbert curve]] [00:03:35].

### Pseudo-Hilbert Curves

The concept of a [[hilberts_curves_and_infinite_math | Hilbert curve]] is best understood by first examining "pseudo-Hilbert curves," which are an infinite family of approximations [00:03:41].

*   **Order-One Pseudo-Hilbert Curve**: Divides a square into a 2x2 grid. The curve connects the center of the lower-left quadrant to the upper-left, then to the upper-right, and finally down to the lower-right [00:03:58].
*   **Order-Two Pseudo-Hilbert Curve**: Subdivides the square into a 4x4 grid. A miniature order-one pseudo-Hilbert curve is traced within each quadrant before moving to the next [00:04:23]. To ensure a smooth connection between quadrants, the mini-curves in the lower-left and lower-right quadrants are flipped [00:04:35].
*   **Higher Orders**: This pattern continues for higher orders. An order-three curve, for example, divides the square into an 8x8 grid, places an order-two pseudo-Hilbert curve in each quadrant, flips the lower-left and lower-right appropriately, and connects them tip to tail [00:04:54].

For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used [00:05:22]. This process defines a function from pixel space to frequency space by associating each pixel with a point on the line [00:05:31].

### Key Advantage: Resolution Stability

The critical advantage of the [[hilberts_curves_and_infinite_math | Hilbert curve]] technique is its stability across resolutions [00:05:52]. As the order of a pseudo-Hilbert curve increases, a given point on the line moves around less and less, merely approaching a more specific point in space [00:06:54]. This means that upgrading to higher resolutions allows users to fine-tune their existing intuitions rather than having to re-learn everything from scratch [00:07:09]. This property makes the [[hilberts_curves_and_infinite_math | Hilbert curve]] approach "almost weirdly perfect" for the sound-to-sight application [00:07:26].

## Connection to Infinite Math

The utility of [[hilberts_curves_and_infinite_math | Hilbert curves]] in finite applications like sound-to-sight translation stems from their origins in infinite mathematics [00:00:11].

### Original Motivation: [[spacefilling_curves_and_their_applications | Space-Filling Curves]]

Near the end of the 19th century, following Cantor's research on infinity, mathematicians sought to find a mapping from a one-dimensional line into two-dimensional space such that the line would run through every single point in space [00:07:39]. This refers to continuous space, which is infinite, where a line with zero area somehow passes through infinitely many points of infinite area [00:08:02]. Before 1890, this was widely considered impossible, but Giuseppe Peano discovered the first [[spacefilling_curves_and_their_applications | space-filling curve]] in 1890, followed by David Hilbert's slightly simpler version in 1891 [00:08:19].

Although these curves technically "fill a square," filling all of space from a line is achievable by tiling space with squares and chaining [[hilberts_curves_and_infinite_math | Hilbert curves]] together in a spiraling pattern [00:08:35].

A "curve" in mathematics refers to a line running through space, even if it has jagged corners [00:08:44]. A more intuitive term for these might be "space-filling fractal" [00:09:00].

### The "Actual" Hilbert Curve

None of the finite pseudo-Hilbert curves used for pixelated space are considered true [[hilberts_curves_and_infinite_math | space-filling curves]] [00:09:10]. An actual [[hilberts_curves_and_infinite_math | Hilbert curve]] is defined as the *limit* of all these pseudo-Hilbert curves [00:09:33].

Defining this limit rigorously requires formalizing curves as functions that take a single number (e.g., between 0 and 1) as input and output a pair of numbers (coordinates in 2D space) [00:09:47]. The core property that makes such a function a "curve" is **continuity** [00:10:33].

> [!NOTE] Continuity
> Continuity describes a function where the output does not suddenly jump when the input changes smoothly [00:10:43]. Formally, for any given output point `b` corresponding to an input `a`, the circle around `b` (containing the outputs of input points near `a`) can be made arbitrarily small by choosing a sufficiently small circle around `a` [00:12:17]. If there is a lower bound on the size of the output circle, the function is discontinuous at that point [00:12:07]. A function is continuous if it is continuous at every possible input point [00:12:27].

The definition of a [[hilberts_curves_and_infinite_math | Hilbert curve]] function relies on a property of pseudo-Hilbert curves: for any given input point, applying each successive pseudo-Hilbert curve function to this point yields outputs that approach a particular point in space [00:12:40]. This convergence means the output of the [[hilberts_curves_and_infinite_math | Hilbert curve]] function for a given input is simply the limit of the outputs from the sequence of pseudo-Hilbert curves [00:13:41]. This is a well-defined function, unlike what would happen with snake curves, where outputs become erratic with increasing resolution and never approach a single point [00:13:15].

For a function to be a [[spacefilling_curves_and_their_applications | space-filling curve]], three things must be proven [00:14:17]:
1.  The outputs of the pseudo-Hilbert curve functions converge (it is well-defined) [00:14:19].
2.  The function is continuous (it gives a curve) [00:14:35].
3.  Every single point in the unit square is an output of this function (it fills space) [00:14:38].
All three of these facts are true for the [[hilberts_curves_and_infinite_math | Hilbert curve]] [00:14:48].

## Interplay Between Infinite and Finite

The consistent property that makes [[hilberts_curves_and_infinite_math | Hilbert curves]] useful in both the finite sound-to-sight application and their infinite mathematical origins is that points on the curve move around less and less as the order of the curves increases [00:15:43]. For the sound-to-sight project, this stability ensures that higher-resolution upgrades do not necessitate retraining senses [00:16:02]. For mathematicians, this property guarantees that the limit of a sequence of curves is meaningful [00:16:07].

This connection between the infinite and finite worlds is a recurring theme in mathematics [00:16:19]. Often, the same patterns and constructs used to define and prove facts about infinite objects have direct, useful finite analogs [00:16:39]. Theorems about infinite objects can frequently be viewed as a concise encapsulation of truths about a family of finite objects [00:16:58]. Formalizing the stability of a curve as camera resolution increases, for example, directly leads to the definition of a sequence of curves having a limit [00:17:06]. This illustrates that even abstract mathematical statements can yield practical insights, such as [[fourier_transform_as_a_tool_for_analyzing_frequency_content_of_signals | applying Fourier transforms]] in [[application_of_fourier_transform_in_sound_editing | sound editing]] or developing "seeing with ears" technology from [[hilberts_curves_and_infinite_math | space-filling curves]] [00:17:37].