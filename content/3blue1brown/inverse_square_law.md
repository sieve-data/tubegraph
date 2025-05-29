---
title: Inverse Square Law
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The [[basel_problem | Basel problem]], which seeks the sum of the inverses of square numbers (1 + 1/4 + 1/9 + 1/16 + ...), remained unsolved for 90 years until [[eulers_formula | Euler]] found the answer to be pi squared divided by 6 <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This problem can be understood through a physical representation involving light and the inverse square law <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Physical Representation with Lighthouses

Imagine an observer at the origin of a positive number line with lighthouses placed on every positive integer (1, 2, 3, 4, and so on) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
If the apparent brightness of the first lighthouse is set as one, the apparent brightness of the second lighthouse is 1/4 as much, the third is 1/9, and the fourth is 1/16, and so on <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This means the total brightness received from an infinite line of lighthouses is 1 + 1/4 + 1/9 + 1/16 and so on <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to show that this total brightness equals pi squared divided by 6 times the brightness of the first lighthouse <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Understanding Apparent Brightness

Apparent brightness to an observer can be conceptualized by considering what proportion of light rays hit a screen, or more precisely, the solid angle covered by the light in three dimensions <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### The Inverse Square Law Explained

The inverse square law is a distinctly three-dimensional phenomenon <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Distance and Area**: If light rays hit a screen one unit away from a source, and you double the distance, those rays will cover an area with twice the width and twice the height <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Light Reception**: To receive the same rays at twice the distance, it would take four copies of the original screen, meaning each individual screen receives only 1/4 as much light <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This illustrates why light appears 1/4 as bright two times the distance away <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Generalization**: Similarly, at three times the distance, nine copies of the original screen would be needed, so each individual screen receives 1/9 as much light <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **The Law**: This pattern continues: because the area hit by a light increases by the square of the distance, the brightness of that light decreases by the inverse square of that distance <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Broader Applications
The inverse square law is not exclusive to light <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. It appears whenever a quantity spreads out evenly from a point source, such as sound, heat, or radio signals <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Connection to the Basel Problem
The inverse square law is why an infinite array of evenly spaced lighthouses physically implements the [[basel_problem | Basel problem]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. The transformation of a single lighthouse into two others based on the [[inverse_pythagorean_theorem | Inverse Pythagorean Theorem]] is key to solving the problem by maintaining constant apparent brightness <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.