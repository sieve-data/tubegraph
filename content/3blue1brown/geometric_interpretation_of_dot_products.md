---
title: Geometric interpretation of dot products
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

Dot products are traditionally introduced early in a linear algebra course <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. However, a fuller understanding of their role in mathematics is best found under the light of linear [[transformations_involving_dot_product | linear transformations]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Numerical Definition of the Dot Product

Numerically, for two [[dot_products_and_vectors | vectors]] of the same dimension (lists of numbers with the same lengths), taking their [[dot_products_and_vectors | dot product]] involves pairing up coordinates, multiplying those pairs, and adding the results <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Examples
*   The [[dot_products_and_vectors | dot product]] of vector (1, 2) and (3, 4) is (1 * 3) + (2 * 4) = 3 + 8 = 11 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   The [[dot_products_and_vectors | dot product]] of (6, 2, 8, 3) and (1, 8, 5, 3) is (6 * 1) + (2 * 8) + (8 * 5) + (3 * 3) = 6 + 16 + 40 + 9 = 71 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Geometric Interpretation

This numerical computation has a distinct [[geometric_versus_numeric_understanding_in_linear_algebra | geometric interpretation]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

To understand the [[dot_products_and_vectors | dot product]] between two [[dot_products_and_vectors | vectors]], *v* and *w*, imagine projecting *w* onto the line passing through the origin and the tip of *v* <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The [[dot_products_and_vectors | dot product]] *v* · *w* is obtained by multiplying the length of this projection by the length of *v* <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Directional Implications
*   If the projection of *w* points in the opposite direction from *v*, the [[dot_products_and_vectors | dot product]] will be negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   When two [[dot_products_and_vectors | vectors]] generally point in the same direction, their [[dot_products_and_vectors | dot product]] is positive <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   When they are perpendicular (the projection of one onto the other is the zero vector), their [[dot_products_and_vectors | dot product]] is zero <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   If they point in generally the opposite direction, their [[dot_products_and_vectors | dot product]] is negative <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### [[symmetry_and_scaling_in_dot_products | Symmetry and Scaling]]

The geometric interpretation initially appears asymmetric, treating the two [[dot_products_and_vectors | vectors]] differently <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. However, the order of [[dot_products_and_vectors | vectors]] in a [[dot_products_and_vectors | dot product]] does not matter; projecting *v* onto *w* and multiplying by the length of *w* yields the same result as projecting *w* onto *v* and multiplying by the length of *v* <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

This [[symmetry_and_scaling_in_dot_products | symmetry]] can be understood:
*   If *v* and *w* have the same length, projecting *w* onto *v* and multiplying by the length of *v* is a mirror image of projecting *v* onto *w* and multiplying by the length of *w* <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   If one vector, say *v*, is scaled by a constant (e.g., 2*v*), the [[symmetry_and_scaling_in_dot_products | symmetry]] is broken <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   If *w* is projected onto *v*, scaling *v* by 2 doubles the length of the vector being projected onto, thus doubling the [[dot_products_and_vectors | dot product]] <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   If *v* is projected onto *w*, scaling *v* by 2 doubles the length of the projection, but the length of *w* remains constant, again doubling the [[dot_products_and_vectors | dot product]] <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   Even though the [[symmetry_and_scaling_in_dot_products | symmetry]] is broken, the effect of scaling on the [[dot_products_and_vectors | dot product]] value is the same under both interpretations <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Connecting Numerical and Geometric via Duality

A deeper reason for the connection between the numerical process and projection lies in the concept of duality <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Linear Transformations to the Number Line
Consider [[transformations_involving_dot_product | linear transformations]] that map multiple dimensions to one dimension (the number line) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. These functions take an *N*-dimensional vector and output a single number <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

*   A visual property of linear transformations is that a line of evenly spaced dots remains evenly spaced after transformation into the output space (the number line) <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   These transformations are completely determined by where they take the basis [[dot_products_and_vectors | vectors]] (e.g., i-hat and j-hat) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   Since each basis vector lands on a number, the transformation can be recorded as a 1x*N* matrix <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   Applying such a transformation to a vector involves matrix-vector multiplication, which computationally resembles a [[dot_products_and_vectors | dot product]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### The Duality Insight
There is an association between 1x*N* matrices and *N*-dimensional [[dot_products_and_vectors | vectors]], defined by tilting the numerical representation of a vector on its side to get the associated matrix, and vice versa <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This suggests a connection between [[transformations_involving_dot_product | linear transformations]] that map [[dot_products_and_vectors | vectors]] to numbers and the [[dot_products_and_vectors | vectors]] themselves <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

Consider projecting 2D [[dot_products_and_vectors | vectors]] straight onto a diagonal copy of the number line, where 0 sits at the origin <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Let *u-hat* be the 2D unit vector whose tip sits where the number 1 is on this diagonal number line <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This projection defines a [[transformations_involving_dot_product | linear transformation]] from 2D [[dot_products_and_vectors | vectors]] to numbers <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

To find the 1x2 matrix describing this projection transformation, consider where i-hat and j-hat land <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>:
*   Due to [[symmetry_and_scaling_in_dot_products | symmetry]], projecting i-hat onto the line passing through *u-hat* is equivalent to projecting *u-hat* onto the x-axis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. The number i-hat lands on is thus the x-coordinate of *u-hat* <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   Similarly, the y-coordinate of *u-hat* gives the number where j-hat lands when projected onto the number line <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   Therefore, the entries of the 1x2 matrix describing the projection transformation are the coordinates of *u-hat* <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

Computing this projection transformation for arbitrary [[dot_products_and_vectors | vectors]] (multiplying the matrix by the [[dot_products_and_vectors | vectors]]) is computationally identical to taking a [[dot_products_and_vectors | dot product]] with *u-hat* <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This explains why the [[dot_products_and_vectors | dot product]] with a unit vector can be interpreted as projecting a vector onto the span of that unit vector and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

For non-unit [[dot_products_and_vectors | vectors]] (e.g., *u-hat* scaled by 3), the numerical components are also scaled <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This implies the new matrix can be interpreted as projecting any vector onto the number line and then multiplying the result by 3 <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This is why the [[dot_products_and_vectors | dot product]] with a non-unit vector is interpreted as first projecting onto that vector, then scaling the length of that projection by the length of the vector <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Duality in Linear Algebra

The core insight is that any [[transformations_involving_dot_product | linear transformation]] whose output space is the number line, regardless of how it was defined, will correspond to a unique vector *v* <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. Applying the transformation is the same as taking a [[dot_products_and_vectors | dot product]] with that vector <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

This is an example of duality, which refers to a natural but surprising correspondence between two types of mathematical objects <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. In this case, the dual of a vector is the [[transformations_involving_dot_product | linear transformation]] it encodes, and the dual of a [[transformations_involving_dot_product | linear transformation]] from a space to one dimension is a certain vector in that space <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

Ultimately, while the [[dot_products_and_vectors | dot product]] is a useful geometric tool for understanding projections and directional tendencies <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>, at a deeper level, dotting two [[dot_products_and_vectors | vectors]] translates one of them into the world of [[transformations_involving_dot_product | transformations]] <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Sometimes, a vector is easier to understand not as an arrow in space, but as the physical embodiment of a [[transformations_involving_dot_product | linear transformation]] <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. This concept will be further explored with the [[introduction_to_cross_products | cross product]] <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.