---
title: Geometric representation of complex numbers
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

[[Complex numbers introduction | Complex numbers]] are a fundamental piece of mathematics, crucial to engineering, mathematics itself, and quantum mechanics, despite having a "terrible, terrible name" [0:00:04]. The components that give rise to [[Complex numbers introduction | complex numbers]] are called [[Complex numbers introduction | imaginary numbers]], a term that the speaker considers "genuinely absurd" [0:00:17, 0:10:32].

## The "Reality" of Numbers

The naming convention of "imaginary" numbers, coined by Rene Descartes, was originally derogatory, intended to mock the idea that such numbers could be considered serious mathematics [0:10:29]. However, engineers and mathematicians widely regard [[Complex numbers introduction | complex numbers]] as "as real a part of their work and their life as real numbers are" [0:07:32, 0:07:42, 0:07:50].

A poll conducted during the discussion asked participants which numbers they considered "to really exist" among 2, √2, √-1, and infinity [0:01:01, 0:02:44]. The results showed a significant portion of the audience accepted √-1 as "real" while rejecting infinity [0:14:23, 0:14:29, 0:14:41]. The speaker's personal view is that any numerical construct helpful in the real world should be considered real [0:04:37].

## Geometric Interpretation

One of the most elegant and useful aspects of [[Complex numbers introduction | complex numbers]] is their [[Complex numbers and 2D plane transformations | geometric representation]] [0:02:35]. The concept proposes that numbers are **two-dimensional** [0:08:37, 0:11:19].

Instead of just the traditional real number line, the [[Complex numbers introduction | imaginary unit]] `i` is said to "live in a different dimension," specifically "perpendicularly" to the real number line [0:08:23, 0:10:53, 0:10:56]. This means `i` is located "one unit perpendicularly above the real number line" [0:08:41, 0:11:19].

## Operations with Complex Numbers

### Addition

Adding [[Complex numbers introduction | complex numbers]] is straightforward and operates similarly to adding vectors [0:12:02, 0:12:07, 0:15:57]. If you have a number like 4 (representing 4 units on the real axis) and want to add it to a number like -2 + 2i (representing -2 on the real axis and 2 on the imaginary axis), you combine their respective real and imaginary parts [0:12:20, 0:12:45, 0:12:50]. For example, `(4) + (-2 + 2i)` would result in `2 + 2i` [0:17:58]. Most people found this intuitive [0:17:56, 0:18:23].

### Multiplication

While vector multiplication in a 2D plane is not typically defined to yield another vector, [[Complex numbers introduction | complex number]] multiplication behaves much like real number multiplication, allowing rules from algebra to carry over [0:18:32, 0:18:58, 0:19:03].

#### Multiplication by the Imaginary Unit `i`

The defining feature of `i` is that `i² = -1` [0:06:43, 0:20:55]. This property is crucial to its [[Complex numbers and 2D plane transformations | geometric action]]. When you multiply a [[Complex numbers introduction | complex number]] by `i`, it results in a [[Complex numbers and 2D plane transformations | 90-degree counter-clockwise rotation]] in the complex plane [0:02:27, 0:21:02, 0:21:53, 0:22:48].

For a point `(a, b)` (representing `a + bi`), multiplying by `i` involves swapping the coordinates and negating the new first coordinate (which was the original real part `a`) [0:21:16, 0:21:21-0:21:44].
For example, multiplying `3 + 2i` by `i`:
1.  Algebraically: `i * (3 + 2i) = 3i + 2i²` [0:20:42, 0:20:49].
2.  Since `i² = -1`, this becomes `3i + 2(-1) = -2 + 3i` [0:20:55, 0:21:02].
3.  Geometrically, the point `(3, 2)` (representing `3 + 2i`) rotates 90 degrees counter-clockwise to `(-2, 3)` (representing `-2 + 3i`) [0:19:59, 0:20:10, 0:20:23].

Multiplying by `i` twice (equivalent to `i² = -1`) results in a 180-degree rotation, which flips both coordinates to negative values (e.g., `(a, b)` becomes `(-a, -b)`), a geometrically consistent outcome [0:16:44, 0:17:08, 0:21:56].

#### General Complex Multiplication

[[Complex numbers introduction | Complex multiplication]] applies a consistent rule across the entire plane, scaling and rotating the plane in a way that preserves parallelism and perpendicularity [0:25:56, 0:26:08, 0:26:11]. The distributive property applies, meaning that `z * (c + di)` can be broken down into `c * z + d * (z * i)` [0:24:54, 0:25:05]. This implies that if you know where a [[Complex numbers introduction | complex number]] `z` maps 1 (which is `z`) and where it maps `i` (which is `z*i`), then its effect on any other [[Complex numbers introduction | complex number]] `(c + di)` is fully determined [0:24:47, 0:24:54, 0:25:21, 0:26:26].

## Significance and Applications

The ability of [[Complex numbers introduction | complex numbers]] to describe [[Complex numbers and 2D plane transformations | rotations]] in an elegant way is one of their main uses [0:02:35, 0:02:39, 0:22:15]. This [[connection_between_trigonometry_and_complex_numbers | connection between trigonometry and complex numbers]] allows for simpler derivations and understanding of complex trigonometric identities, such as addition formulas for cosine and sine, which are otherwise hard to remember [0:05:10, 0:05:40, 0:06:00, 0:06:17, 0:06:59]. Even if one doesn't "believe in the reality of the square root of negative one," its utility in making other mathematical concepts more understandable and useful is undeniable [0:07:22].