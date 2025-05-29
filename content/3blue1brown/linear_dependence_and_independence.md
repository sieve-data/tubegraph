---
title: linear dependence and independence
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

In [[linear_algebra_foundations | linear algebra]], understanding how vectors relate to each other through operations like vector addition and scalar multiplication is fundamental <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Concepts like [[linear_combinations | linear combinations]], span, and basis are essential for this understanding <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## The Span of Vectors

The "span" of a set of vectors refers to the collection of all possible vectors that can be reached by forming [[linear_combinations | linear combinations]] of those vectors <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. It asks what vectors are reachable using only vector addition and scalar multiplication with the given vectors <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

For example:
*   **In 2D space:**
    *   The span of most pairs of 2D vectors is the entire 2D space <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, meaning every possible 2D vector can be reached <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   If two 2D vectors "line up" (are parallel), their span is limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   If both vectors are zero, the span is just the origin <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **In 3D space:**
    *   The span of two vectors in 3D space that are not pointing in the same direction forms a flat sheet (a plane) cutting through the origin <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   Adding a third vector:
        *   If the third vector is already within the span of the first two (i.e., it lies on the plane defined by the first two), then the span does not change; it remains the same flat sheet <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
        *   If the third vector is not on the span of the first two, it "unlocks access to every possible three-dimensional vector," making the span the entire 3D space <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

> [!NOTE] Vectors as Points
> When considering collections of vectors, it's often helpful to conceptualize each vector as a point at its tip, assuming its tail is at the origin. This makes it easier to visualize the "span" as a line, plane, or entire space <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Linearly Dependent Vectors

Vectors are said to be **linearly dependent** if you have multiple vectors and you could remove one without reducing their span <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This means at least one of the vectors is redundant <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

Another way to phrase this is that one of the vectors can be expressed as a [[linear_combinations | linear combination]] of the others, since it's already within the span of the others <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

**Examples of Linear Dependence:**
*   Two 2D vectors that "line up" (are parallel) are linearly dependent because removing one still results in a span that is a line <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   In 3D, if a third vector happens to be sitting on the span (plane) of the first two, the three vectors are linearly dependent, as adding it does not expand the span <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

## Linearly Independent Vectors

Conversely, vectors are considered **linearly independent** if each vector truly adds another dimension to the span <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. In this case, removing any vector *would* reduce the span.

**Examples of Linear Independence:**
*   Most pairs of 2D vectors are linearly independent, as their span covers the entire 2D plane <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   In 3D, if a third vector is randomly chosen and is *not* sitting on the span of the first two, these three vectors are linearly independent, and their span becomes the entire 3D space <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

## Connection to Basis Vectors

The concept of linear independence and span is crucial to defining a "basis" in [[coordinate_systems_in_linear_algebra | coordinate systems]].

The technical definition of a basis of a space is:
> A set of **linearly independent** vectors that **span** that space <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

For instance, the standard basis vectors in the XY [[coordinate_systems_in_linear_algebra | coordinate system]], `i-hat` (unit vector in x-direction) and `j-hat` (unit vector in y-direction), are linearly independent and span the entire 2D plane <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. When coordinates describe a vector, they represent the scalars used to scale these basis vectors in a [[linear_combinations | linear combination]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The choice of basis vectors implicitly influences how vectors are numerically described <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.