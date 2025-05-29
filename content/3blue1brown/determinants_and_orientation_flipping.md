---
title: Determinants and orientation flipping
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 

While the [[determinants_and_area_scaling | determinant]] of a [[visual_intuition_of_linear_transformations | linear transformation]] is typically understood as a scaling factor for area or volume, the concept also allows for negative values <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. A negative determinant indicates that the transformation has inverted the "orientation" of space <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The absolute value of the determinant still represents the factor by which areas or volumes have been scaled <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Inverting Orientation in 2D Space

In two dimensions, a transformation that inverts orientation can be visualized as "flipping space over," similar to turning over a sheet of paper <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

A key way to determine orientation is by observing the relative positions of the basis vectors [[visual_understanding_of_linear_transformations | i-hat and j-hat]] <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>:
*   Initially, [[visual_understanding_of_linear_transformations | j-hat]] is to the left of [[visual_understanding_of_linear_transformations | i-hat]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   If, after a transformation, [[visual_understanding_of_linear_transformations | j-hat]] is positioned to the right of [[visual_understanding_of_linear_transformations | i-hat]], the orientation of space has been inverted <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. When this inversion occurs, the determinant will be negative <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

For example, a transformation with a determinant of -3 signifies that space has been flipped over, and areas are scaled by a factor of 3 <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Intuition for Negative Values

The concept of negative determinants naturally follows from a continuous change in orientation:
*   Consider a series of transformations where [[visual_understanding_of_linear_transformations | i-hat]] moves closer to [[visual_understanding_of_linear_transformations | j-hat]] <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   As they approach alignment, areas are increasingly squished, and the determinant approaches 0 <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   When [[visual_understanding_of_linear_transformations | i-hat]] perfectly aligns with [[visual_understanding_of_linear_transformations | j-hat]], the determinant is exactly 0 <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   If [[visual_understanding_of_linear_transformations | i-hat]] continues past this point, it feels natural for the determinant to continue decreasing into negative numbers <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Inverting Orientation in 3D Space

For [[threedimensional_linear_transformations | three-dimensional linear transformations]], the determinant indicates how much volumes are scaled <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Similar to 2D, a negative determinant in 3D indicates an orientation flip <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

The "right-hand rule" provides a visual way to understand orientation in 3D <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>:
1.  Point the forefinger of your right hand in the direction of [[threedimensional_linear_transformations | i-hat]] <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
2.  Extend your middle finger in the direction of [[threedimensional_linear_transformations | j-hat]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
3.  Your thumb will point in the direction of [[threedimensional_linear_transformations | k-hat]] <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

*   If you can still apply the right-hand rule after a transformation, the orientation has not changed, and the determinant is positive <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   If, after the transformation, it only makes sense to perform this gesture with your *left hand*, the orientation has been flipped, and the determinant is negative <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.