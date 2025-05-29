---
title: column space
videoId: uQhTuRlWMxw
---

From: [[3blue1brown]] <br/> 

The concept of column space helps in understanding matrix and vector operations, particularly through the visual perspective of linear transformations <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This concept is part of a broader discussion that includes inverse matrices, [[rank]], and [[null_space | null space]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Definition

The **column space** of a matrix refers to the set of all possible outputs of the linear transformation associated with that matrix <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. This output can manifest as a line, a plane, 3D space, or any other dimension, depending on the transformation <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

The name "column space" comes from the fact that the columns of a matrix indicate where the basis vectors land after the transformation <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. The span of these transformed basis vectors then encompasses all possible outputs of the transformation <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Therefore, the column space is precisely the span of the columns of the matrix <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Properties

*   The zero vector is always part of the column space <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. This is because linear transformations inherently keep the origin fixed <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## Relationship with Rank

The [[rank]] of a transformation is defined as the number of dimensions in its column space <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a> <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. For example:
*   If the output of a transformation is a one-dimensional line, its [[rank]] is one <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   If all vectors land on a two-dimensional plane, the transformation has a [[rank]] of two <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   For a 3D transformation whose output fills all of 3D space, it has a [[rank]] of three <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

When the [[rank]] is as high as possible—equaling the number of columns in the matrix—the matrix is considered **full [[rank]]** <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. In such cases, the determinant is non-zero, meaning space is not squished into a lower dimension <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a> <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

## Significance in Linear Systems

The concept of column space is crucial for understanding linear systems of equations (Ax = V) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It helps to determine when a solution to such a system exists <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

When a transformation squishes space into a smaller dimension (i.e., its determinant is zero), there is no inverse transformation <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. In these scenarios, a solution to Ax = V only exists if the vector V happens to be located within the column space (the squished output space) <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. If V lies outside this space, no vector X can be transformed to land on V <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Conversely, if the matrix is full [[rank]] (non-zero determinant), its column space spans the entire output dimension, meaning there will always be a unique vector X that lands on V <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.