---
title: Concept of duality in math
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

Traditionally, the dot product is introduced early in a linear algebra course, often at the very beginning <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While a basic understanding of vectors is sufficient for its initial introduction, a deeper comprehension of its role in mathematics becomes clear through the lens of linear transformations <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This deeper understanding reveals a powerful concept known as duality <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## The Standard Dot Product

Numerically, the dot product of two vectors of the same dimension involves pairing up their coordinates, multiplying those pairs, and summing the results <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, the dot product of vectors (1, 2) and (3, 4) is (1 * 3) + (2 * 4) <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

This computation has a significant geometric interpretation <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>:
*   To find the dot product of vectors `v` and `w`, one can project `w` onto the line defined by `v` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The dot product `v ⋅ w` is then the length of this projection multiplied by the length of `v` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   If the projection of `w` points in the opposite direction from `v`, the dot product is negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   If vectors generally point in the same direction, their dot product is positive <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   If they are perpendicular (the projection of one onto the other is the zero vector), their dot product is zero <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   If they point in generally opposite directions, their dot product is negative <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

Despite this seemingly asymmetric interpretation, the order of vectors in a dot product does not matter; projecting `v` onto `w` and multiplying by the length of `w` yields the same result as projecting `w` onto `v` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This symmetry holds even when vectors have different lengths, as scaling one vector affects both interpretations of the dot product identically <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Dot Products and Linear Transformations

The connection between the numerical dot product and its geometric projection interpretation can be understood through linear transformations from multiple dimensions to a single dimension (the number line) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

Linear transformations preserve the even spacing of dots on a line when they map from an input space to the number line <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Such a transformation is entirely defined by where it maps the basis vectors (like `i-hat` and `j-hat`) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Since the output space is a single number, the mapping of basis vectors forms a matrix with a single row, e.g., a 1x2 matrix for a 2D input <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

Applying this 1x2 matrix to a vector computationally resembles a dot product <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. This numerical resemblance suggests a deeper geometric link: there is a natural association between 1x2 matrices and 2D vectors, where one can be obtained by "tipping" the other on its side <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This hints at a connection between linear transformations that map vectors to numbers and vectors themselves <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This concept contributes to [[visualizing_mathematical_concepts | visualizing mathematical concepts]] and provides a [[visual_approach_to_math_concepts | visual approach to math concepts]].

### Geometric Derivation of Projection through Linearity

Consider placing a copy of the number line diagonally in 2D space, with zero at the origin <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. If we define a function by projecting 2D vectors straight onto this diagonal number line, this function is a linear transformation <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Let `u-hat` be the 2D unit vector whose tip lies at the number 1 on this diagonal number line <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. To find the 1x2 matrix that describes this projection transformation, we observe where the basis vectors `i-hat` and `j-hat` land <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

By symmetry, projecting `i-hat` onto the line through `u-hat` is equivalent to projecting `u-hat` onto the x-axis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Projecting `u-hat` onto the x-axis simply gives its x-coordinate <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Therefore, the number where `i-hat` lands under this projection transformation is the x-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Similarly, `j-hat` lands on the y-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

Thus, the entries of the 1x2 matrix for this projection transformation are the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Computing this projection for any vector by multiplying it with this matrix is computationally identical to taking the dot product with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This demonstrates why the dot product with a unit vector can be interpreted as projecting a vector onto the span of that unit vector and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

For non-unit vectors, if `u-hat` is scaled by a factor (e.g., 3), its components are similarly scaled <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. The corresponding matrix will also scale `i-hat` and `j-hat` by the same factor <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This means the dot product with a non-unit vector involves projecting the vector onto that vector and then scaling the length of that projection by the length of the vector <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This shifts understanding from [[graphical_intuition_versus_transformational_understanding_in_calculus | graphical intuition]] to a deeper, transformational view.

## What is Duality?

The profound insight is that any linear transformation from a space to the number line, regardless of its definition, corresponds to a unique vector <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. Applying this transformation is equivalent to taking a dot product with that unique vector <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

> [Duality] refers to situations where you have a natural but surprising correspondence between two types of mathematical thing <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

In the context of linear algebra, the duality lies in the relationship between vectors and linear transformations that output to one dimension (the number line) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. The "dual" of a vector is the linear transformation it encodes, and the "dual" of a linear transformation to one dimension is a specific vector in the input space <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

This concept highlights that while the dot product is a valuable geometric tool for understanding projections and vector alignment <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>, its deeper significance lies in its ability to translate one vector into the domain of transformations <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Sometimes, understanding a vector as the physical embodiment of a linear transformation provides greater clarity than viewing it merely as an arrow in space <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. A vector can be considered a conceptual shorthand for a particular transformation <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.