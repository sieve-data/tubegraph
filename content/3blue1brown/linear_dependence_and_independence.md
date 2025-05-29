---
title: Linear dependence and independence
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

In [[understanding_linear_algebra | linear algebra]], [[linear_combinations_and_their_significance | linear combinations]], span, and the concepts of linear dependence and independence are fundamental to understanding how vectors relate to each other and define spaces <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.

## Vector Coordinates and Linear Combinations

Vector coordinates, such as a pair of numbers like (3, -2) for a two-dimensional vector, can be thought of as scalars <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. In the standard xy coordinate system, there are two special vectors:
*   **i-hat**: The unit vector in the x direction (length 1, pointing right) <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.
*   **j-hat**: The unit vector in the y direction (length 1, pointing straight up) <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.

The x-coordinate scales i-hat, and the y-coordinate scales j-hat <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. The vector that these coordinates describe is the sum of these two scaled vectors <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. This concept of adding together two scaled vectors is called a [[linear_combinations_and_their_significance | linear combination]] <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>, <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.

These two vectors, i-hat and j-hat, form the **basis** of a coordinate system <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. When coordinates are viewed as scalars, the basis vectors are what those scalars scale <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. Different basis vectors can be chosen to create completely reasonable new coordinate systems <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Any numerical description of vectors relies on an implicit choice of basis vectors <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

## Span of Vectors

The **span** of a given pair of vectors is the set of all possible vectors that can be reached using a [[linear_combinations_and_their_significance | linear combination]] of those two vectors <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>, <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. This concept basically asks what vectors can be reached using only vector addition and scalar multiplication <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

### Geometric Interpretation of Span

*   **Two-dimensional vectors**:
    *   For most pairs of 2D vectors, their span is all vectors of 2D space, meaning every possible point in the plane <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>, <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.
    *   If the two original vectors happen to line up (are collinear), their span is limited to a single line passing through the origin <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>, <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
    *   If both vectors are zero, the span is just the origin <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
*   **Three-dimensional vectors**:
    *   If two vectors in 3D space are not pointing in the same direction, their span is a flat sheet (a plane) cutting through the origin of three-dimensional space <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>, <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
    *   Adding a third vector:
        *   If the third vector is already within the span of the first two (i.e., it lies on the same flat sheet), the span does not change <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
        *   If the third vector is not in the span of the first two (points in a separate direction), it unlocks access to every possible three-dimensional vector, meaning the span becomes all of 3D space <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>, <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

## Linear Dependence

Multiple vectors are considered **linearly dependent** if one or more of them can be removed without reducing their span <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>, <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. This means that at least one of the vectors is redundant <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. Another way to phrase this is that one of the vectors can be expressed as a [[linear_combinations_and_their_significance | linear combination]] of the others, since it is already within their span <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.

**Examples of Linear Dependence:**
*   Two 2D vectors that line up (are collinear) are linearly dependent because one can be scaled to become the other, and removing one would not change the span (it would still be a line) <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>, <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
*   Three 3D vectors where the third vector already sits on the plane spanned by the first two are linearly dependent, as the third vector doesn't add any new dimensions to the span <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>, <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.

## Linear Independence

Conversely, if each vector truly adds another dimension to the span, the vectors are said to be **linearly independent** <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>, <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. This means no vector in the set can be expressed as a [[linear_combinations_and_their_significance | linear combination]] of the others.

## Basis and its Definition

The technical definition of a **basis** of a space is a set of [[linear_transformations | linearly independent]] vectors that span that space <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>, <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>. This definition makes sense because:
*   **Span that space**: The basis vectors must be able to generate all other vectors in the space through [[linear_combinations_and_their_significance | linear combinations]] <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.
*   **Linearly independent**: There should be no redundant vectors in the basis; each vector must contribute uniquely to the span <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>.