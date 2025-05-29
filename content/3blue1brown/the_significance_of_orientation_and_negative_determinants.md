---
title: The significance of orientation and negative determinants
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 
The determinant of a linear transformation is a special scaling factor that indicates how much the transformation changes the area of a region in two dimensions, or the volume of a region in three dimensions <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. Initially, the concept of the determinant focuses on positive scaling factors, but it also allows for negative values <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

### Orientation in 2D

The idea of scaling an area by a negative amount is directly linked to the concept of **orientation** <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.
*   **Flipping Space**
    Some transformations can cause space to "flip over," similar to turning a sheet of paper to its other side <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. Such transformations are described as "inverting the orientation of space" <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
*   **i-hat and j-hat relationship**
    Consider the initial positions of the basis vectors [[importance_of_geometric_understanding_in_linear_algebra | i-hat]] and [[importance_of_geometric_understanding_in_linear_algebra | j-hat]], where [[importance_of_geometric_understanding_in_linear_algebra | j-hat]] is to the left of [[importance_of_geometric_understanding_in_linear_algebra | i-hat]] <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. If, after a transformation, [[importance_of_geometric_understanding_in_linear_algebra | j-hat]] ends up on the right of [[importance_of_geometric_understanding_in_linear_algebra | i-hat]], the orientation of space has been inverted <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.
*   **Negative Determinant**
    Whenever the orientation of space is inverted, the determinant of the transformation will be negative <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. The absolute value of the determinant still represents the factor by which areas have been scaled <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. For instance, a transformation with a determinant of -3 means space is flipped over, and areas are scaled by a factor of 3 <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

### Why Negative? A Continuous Analogy

The concept of a negative determinant as a natural way to describe orientation flipping can be understood through a continuous series of transformations <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>:
*   Imagine [[importance_of_geometric_understanding_in_linear_algebra | i-hat]] slowly moving closer to [[importance_of_geometric_understanding_in_linear_algebra | j-hat]] <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
*   As [[importance_of_geometric_understanding_in_linear_algebra | i-hat]] approaches [[importance_of_geometric_understanding_in_linear_algebra | j-hat]], areas are increasingly squished, causing the determinant to approach 0 <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   When [[importance_of_geometric_understanding_in_linear_algebra | i-hat]] aligns perfectly with [[importance_of_geometric_understanding_in_linear_algebra | j-hat]], the determinant becomes 0 <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
*   If [[importance_of_geometric_understanding_in_linear_algebra | i-hat]] continues past this alignment, it feels natural for the determinant to continue decreasing into negative numbers, reflecting the inversion of orientation <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

### Orientation in 3D

In three dimensions, the determinant scales volumes <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>. The significance of a negative determinant extends to 3D orientation:
*   **Right-Hand Rule**
    Orientation in 3D can be described using the right-hand rule <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. If, after a transformation, you can still align your right hand's forefinger with [[importance_of_geometric_understanding_in_linear_algebra | i-hat]], middle finger with [[importance_of_geometric_understanding_in_linear_algebra | j-hat]], and thumb with [[importance_of_geometric_understanding_in_linear_algebra | k-hat]], the orientation is unchanged, and the determinant is positive <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.
*   **Orientation Flip**
    If, however, you can only make this alignment with your left hand after the transformation, the orientation has been flipped, and the determinant is negative <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.