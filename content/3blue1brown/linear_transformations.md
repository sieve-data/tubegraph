---
title: Linear transformations
videoId: TgKwz5Ikpc8
---

From: [[3blue1brown]] <br/> 

A [[Linear transformations and matrices | linear transformation]] is a function that takes in one vector and turns it into another, adhering to specific rules <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In the context of functions, these are sometimes referred to as "operators" instead of "transformations" <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. The formal definition of linearity is abstract and symbolically driven <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, offering generality across different types of "vectorish" things like arrows or functions <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Properties of Linear Transformations

A transformation is considered linear if it satisfies two fundamental [[Properties of linear transformations | properties of linear transformations]]: additivity and scaling <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. These properties ensure that [[Linear transformations and matrices | linear transformations]] "preserve the operations of vector addition and scalar multiplication" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

1.  **Additivity**: If you add two vectors, `v` and `w`, and then apply a transformation to their sum, the result is the same as if you first transformed `v` and `w` separately and then added their transformed versions <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
    *   Expressed symbolically: T(v + w) = T(v) + T(w) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

2.  **Scaling**: If you scale a vector `v` by a number, and then apply the transformation, the result is the same as if you first transformed `v` and then scaled the transformed version by the same amount <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   Expressed symbolically: T(c * v) = c * T(v) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

The visual concept of grid lines remaining parallel and evenly spaced, discussed in earlier videos, is an illustration of these two properties in the specific case of points in 2D space <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Consequences

One of the most important consequences of these properties, which enables [[Linear transformations and matrices | matrix-vector multiplication]], is that a [[Linear transformations and matrices | linear transformation]] is completely described by where it takes the basis vectors <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Since any vector can be expressed by scaling and adding the basis vectors in some way, finding the transformed version of that vector simply involves scaling and adding the transformed versions of the basis vectors in the same manner <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This principle holds true for functions as well as for arrows <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

## Linear Transformations of Functions

Functions can also be considered "vector-ish" and undergo [[Linear transformations and matrices | linear transformations]] <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Just as vectors can be added and scaled, so can functions <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### The Derivative as a Linear Transformation

A familiar example of a [[Linear transformations and matrices | linear transformation]] for functions comes from calculus: the derivative <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The derivative transforms one function into another function <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Calculus students implicitly use the fact that the derivative is additive and possesses the scaling property <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>:
*   If you add two functions and then take the derivative, it's the same as first taking the derivative of each one separately and then adding the results <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   If you scale a function and then take the derivative, it's the same as first taking the derivative and then scaling the result <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

#### Matrix Representation of the Derivative

While function spaces tend to be infinite-dimensional, it's possible to describe the derivative with a [[Linear transformations and matrices | matrix]] by limiting the scope to polynomials <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. By choosing pure powers of `x` (1, x, x², x³, etc.) as basis functions, any polynomial can be represented by coordinates that are its coefficients, followed by an infinite tail of zeros <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

In this coordinate system, the derivative can be described by an infinite [[Linear transformations and matrices | matrix]] that is mostly zeros, with positive integers counting down on an offset diagonal <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This [[Matrix representation of linear transformations | matrix]] effectively performs differentiation through [[Linear transformations and matrices | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. This is possible because the derivative is a [[Linear transformations and matrices | linear transformation]] <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This [[Matrix representation of linear transformations | matrix]] can be constructed by taking the derivative of each basis function and placing the coordinates of the results in each column <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

This demonstrates that seemingly different operations like matrix-vector multiplication and taking a derivative are fundamentally members of the same mathematical family <a class="yt-timestamp" data-t="00:10:59">[0:10:59]</a>.