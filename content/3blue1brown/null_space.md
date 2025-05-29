---
title: null space
videoId: uQhTuRlWMxw
---

From: [[3blue1brown]] <br/> 

The concept of null space is described through the visual lens of linear transformations <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Definition and Intuition
The null space of a matrix is the set of all vectors that, after a linear transformation, land on the origin (the zero vector) <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. It can also be referred to as the "kernel" of the matrix <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. This means it's the space of all vectors that become "null" by landing on the zero vector <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

## Null Space in Transformations
When a matrix is not [[full_rank_matrices | full rank]] (meaning it squishes space to a smaller dimension), many vectors can land on the origin <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

*   **2D to 1D:** If a 2D transformation squishes space onto a line, there is a separate line of vectors that get squished onto the origin <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **3D to 2D:** If a 3D transformation squishes space onto a plane, there is also a full line of vectors that land on the origin <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **3D to 1D:** If a 3D transformation squishes all of space onto a line, then a whole plane full of vectors lands on the origin <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

## Relation to Linear Systems of Equations
In the context of a linear system of equations, when the constant vector `V` (on the right-hand side of `Ax = V`) is the zero vector, the null space provides all possible solutions to that equation <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Understanding the null space helps to comprehend the set of all possible solutions <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.