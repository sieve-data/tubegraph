---
title: span of vectors
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

Understanding vector coordinates involves a back-and-forth between pairs of numbers and two-dimensional vectors <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Each coordinate can be thought of as a scalar that stretches or squishes vectors <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

In the xy coordinate system, two special [[basis_vectors|basis vectors]] are common:
*   **i-hat**: The unit vector pointing right with length 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **j-hat**: The unit vector pointing straight up with length 1 <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The x-coordinate scales i-hat, and the y-coordinate scales j-hat <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The vector described by these coordinates is the sum of these two scaled vectors <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. These [[basis_vectors|basis vectors]] (i-hat and j-hat) form the "basis" of a coordinate system <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Linear Combinations

When you scale two vectors and add them together, this operation is called a **linear combination** of those two vectors <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The term "linear" can be intuitively understood by noting that if one scalar is fixed and the other changes freely, the tip of the resulting vector draws a straight line <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## The Span of Vectors

The **span** of a given pair of vectors is the set of all possible vectors that can be reached with a linear combination of those two vectors <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This concept asks what vectors can be created using only vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Span in Two Dimensions (2D)

For two-dimensional vectors, two main outcomes are possible for their span:
*   **Entire Plane**: For most pairs of 2D vectors, if they don't line up, their span is all possible two-dimensional vectors, effectively the entire 2D plane <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **A Line**: If your two original vectors happen to line up (are collinear), the tip of the resulting vector is limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **The Origin**: If both vectors are zero, the span is just the origin <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Visualizing Collections of Vectors

When dealing with collections of vectors, such as in the context of span, it's common to represent each vector with just the point at its tip, assuming its tail is at the origin <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This means:
*   To think about every possible vector whose tip sits on a certain line, you can just think about the line itself <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   To think about all possible two-dimensional vectors, conceptualize each one as the point where its tip sits, which effectively means thinking about the infinite flat sheet of two-dimensional space itself <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Span in Three Dimensions (3D)

The idea of span becomes more complex and interesting in three-dimensional space <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

*   **Span of Two 3D Vectors**: If you take two vectors in 3D space that are not pointing in the same direction, their span is the collection of all possible linear combinations of those two vectors <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The tip of the resulting vector will trace out a flat sheet (a plane) cutting through the origin of three-dimensional space <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

*   **Span of Three 3D Vectors**: A linear combination of three vectors involves choosing three scalars, scaling each vector, and adding them together <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   If the third vector happens to be sitting on the span (plane) of the first two, the span does not change and remains that same flat sheet <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   If the third vector is not sitting on the span of the first two (i.e., it points in a separate direction), it "unlocks" access to every possible three-dimensional vector, meaning the span becomes all of 3D space <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

## Linear Dependence and Independence

When dealing with the span of multiple vectors, specific terminology describes whether vectors add "new" dimensions to the span:

*   **Linearly Dependent**: This occurs when you have multiple vectors and can remove one without reducing the span <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Another way to phrase this is that one of the vectors can be expressed as a linear combination of the others, as it is already within the span of the others <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This happens when two vectors line up in 2D, or when a third vector lies on the plane spanned by the first two in 3D <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Linearly Independent**: If each vector truly adds another dimension to the span, they are said to be linearly independent <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

The technical definition of a [[basis_vectors|basis]] of a space is a set of linearly independent vectors that span that space <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.