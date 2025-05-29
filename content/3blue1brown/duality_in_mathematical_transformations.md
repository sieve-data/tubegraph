---
title: Duality in mathematical transformations
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

In mathematics, **duality** refers to a natural, often surprising, correspondence between two types of mathematical objects or concepts <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. It appears in various forms and contexts throughout mathematics <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. In the context of linear algebra, duality illustrates a fundamental connection between vectors and certain [[linear_transformations|linear transformations]] <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

While [[transformations_involving_dot_product|dot products]] are often introduced early in [[linear_transformations_in_linear_algebra|linear algebra]] courses, a fuller understanding of their role, particularly their geometric interpretation, is best revealed through the lens of [[linear_transformations|linear transformations]] and the concept of duality <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Linear Transformations to a Number Line

A key aspect of understanding duality in this context involves [[linear_transformations|linear transformations]] that map vectors from multiple dimensions (e.g., 2D space) to a single dimension, such as the number line <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. These functions take a vector as input and produce a single number as output <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

Similar to [[visual_intuition_of_linear_transformations|linear transformations]] in higher dimensions, these transformations preserve the even spacing of dots on a line when they land on the number line <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Any [[linear_transformations|linear transformation]] is fully determined by where it maps the basis vectors (e.g., i-hat and j-hat) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. In this case, since the output space is the number line, each basis vector lands on a single number <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

When recording where the basis vectors land, they form the columns of a matrix. For a transformation from 2D to 1D, this results in a 1x2 matrix, where each column consists of a single number <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Applying such a transformation to a vector involves [[transformations_involving_dot_product|matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### Connection to the Dot Product

Numerically, the operation of multiplying a 1x2 matrix by a vector is identical to taking the [[transformations_involving_dot_product|dot product]] of two vectors <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This suggests a direct association between 1x2 matrices and 2D vectors, where one can be obtained by "tipping" the other on its side <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

This numerical similarity hints at a profound geometric connection: there is a relationship between [[linear_transformations|linear transformations]] that map vectors to numbers and the vectors themselves <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

## Duality and Projection

Consider a specific [[linear_transformations|linear transformation]] defined by projecting 2D vectors onto a diagonal copy of the number line embedded in 2D space <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Let's call the unit vector pointing in the direction of the number '1' on this embedded line `u-hat` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

This projection function is a [[linear_transformations|linear transformation]] from 2D vectors to numbers <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. By examining where the basis vectors i-hat and j-hat land when projected onto this diagonal line, we find a remarkable symmetry:
*   Projecting i-hat onto the line passing through `u-hat` is symmetric to projecting `u-hat` onto the x-axis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Therefore, the number where i-hat lands after projection is precisely the x-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   Similarly, the number where j-hat lands is the y-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

Thus, the entries of the 1x2 matrix describing this projection transformation are the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Consequently, applying this projection transformation to any vector is computationally identical to taking the [[transformations_involving_dot_product|dot product]] with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

This explains why taking the [[transformations_involving_dot_product|dot product]] with a unit vector can be interpreted as projecting a vector onto the span of that unit vector and measuring its length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. If the vector is not a unit vector (e.g., `3 * u-hat`), the dot product with this scaled vector corresponds to projecting onto its span and then scaling the projected length by the magnitude of the non-unit vector <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## The Essence of Duality

This example illustrates a profound aspect of duality: any [[linear_transformations|linear transformation]] whose output space is the number line can be uniquely associated with a specific vector `v` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. Applying this transformation is mathematically equivalent to taking a [[transformations_involving_dot_product|dot product]] with that corresponding vector `v` <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

In this specific case of linear algebra:
*   The dual of a vector is the [[linear_transformations|linear transformation]] it encodes <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   The dual of a [[linear_transformations|linear transformation]] from a space to one dimension is a specific vector within that space <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

At a deeper level, the [[transformations_involving_dot_product|dot product]] serves as a bridge, allowing one vector to be "translated" into the realm of transformations <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This highlights that a vector can sometimes be understood not merely as an arrow in space, but as the conceptual embodiment of a [[linear_transformations|linear transformation]] <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.