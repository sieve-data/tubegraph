---
title: Soundtosight software
videoId: 3s7h2MHQtxc
---

From: [[3blue1brown]] <br/> 

Sound-to-sight software is a conceptual application designed to allow people to "see with their ears" <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. This software would take data from a camera and translate it into sound in a meaningful way <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. The underlying thought is that human brains are adaptable enough to build intuition from sight, even when the raw data is scrambled into a different format <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

## Core Mechanism

To facilitate initial experiments, images would be processed at a low resolution, such as 256x256 pixels <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Each pixel within this square grid would be associated with a unique frequency value <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. The brightness of a pixel would determine the loudness of its associated frequency: brighter pixels would play louder, while darker pixels would be quieter <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. Listening to all pixels simultaneously would result in many frequencies overlaid, with dominant frequencies corresponding to brighter image regions <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Mapping Pixel Space to Frequency Space

The primary challenge in designing this software is mapping a two-dimensional pixel space to a one-dimensional frequency space <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. While a random mapping could be attempted, leveraging the brain's existing intuitions about sound suggests a better approach <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. Ideally, frequencies that are close together in the one-dimensional frequency space should correspond to pixels that are close together in the two-dimensional image space <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. This ensures that even if an ear struggles to distinguish between two nearby frequencies, they refer to roughly the same point in the visual space <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

### Weaving a Line Through Pixels

To achieve this proximity preservation, one method is to define a way to weave a line through each pixel <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. By fixing each pixel to a spot on this line and then unraveling the line to make it straight, this line can be interpreted as the frequency space, thus associating pixels with frequencies <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

#### Snake Curve

A simple weaving method is the "Snake Curve," which traverses the pixel grid one row at a time, alternating directions (left to right, then right to left) as it moves up the space <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

#### Hilbert Curve Approach

A more effective method, suggested by mathematicians, involves using a Hilbert curve <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. The specific curves used for pixelated space are referred to as "pseudo-Hilbert curves" <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

**Constructing Pseudo-Hilbert Curves:**
*   **Order-one:** Divide a square into a 2x2 grid. Connect the center of the lower-left quadrant to the upper-left, then to the upper-right, and finally down to the lower-right <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.
*   **Order-two:** Subdivide the square into a 4x4 grid. Trace a miniature order-one pseudo-Hilbert curve within each quadrant <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>. To ensure smooth connections between quadrants, the curves in the lower-left and lower-right quadrants are flipped <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>.
*   **Higher Orders:** The pattern continues, with an order-three curve dividing the square into an 8x8 grid, embedding order-two curves in each quadrant, and applying appropriate flips <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.

For a 256x256 pixel array, an order-eight pseudo-Hilbert curve would be used <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. This curve effectively defines a function from pixel space to frequency space by associating each pixel with a point on the line <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

## Advantages of the Hilbert Curve Approach

The Hilbert curve technique offers a significant advantage over the Snake Curve, particularly when upgrading camera resolution <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.

*   **Snake Curve Disadvantage:** If using a Snake Curve, upgrading resolution (e.g., from 256x256 to 512x512) would cause many points on the frequency line to map to entirely different parts of the pixel space <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>. This would force users to re-learn how to interpret the sound, as their established intuitions would no longer apply <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.
*   **Hilbert Curve Advantage:** With the Hilbert curve technique, as the order of a pseudo-Hilbert curve increases, a given point on the line moves around less and less, approaching a more specific point in space <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. This allows users to fine-tune their intuitions rather than completely re-learning them with resolution upgrades <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.

Therefore, the Hilbert curve approach is particularly well-suited for sound-to-sight applications due to its stability across different resolutions <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.

## Connection to Infinite Mathematics

The utility of pseudo-Hilbert curves in sound-to-sight software mirrors their origins in infinite mathematics, particularly in the study of space-filling curves <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>. Near the end of the 19th century, mathematicians sought to find mappings from a one-dimensional line into two-dimensional space such that the line would pass through every single point <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>. This refers to continuous space, which is infinite, where a line with zero area somehow fills the infinite area of space <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.

In 1890, Peano discovered the first space-filling curve, followed by Hilbert's slightly simpler version in 1891 <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. While pseudo-Hilbert curves used for pixelated space do not truly "fill" continuous space (as zooming in on a pixel shows the curve only passes through a tiny slice) <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>, an actual Hilbert curve is defined as the limit of these pseudo-Hilbert curves <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>.

The core property that makes the Hilbert curve useful in both the finite sound-to-sight application and its infinite origins is that points on the curve move around less and less as the order of the curves increases <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>. This ensures stability in resolution upgrades for practical applications and ensures the mathematical definition of the limit of a sequence of curves is meaningful <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>.

This connection highlights a broader principle in mathematics: the same patterns and constructs used to define infinite facts often have finite analogs that are directly useful <a class="yt-timestamp" data-t="16:19:00">[16:19:00]</a>. A statement about an infinite object can often be viewed as a clean way to encapsulate a truth about a family of finite objects <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>.