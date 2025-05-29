---
title: Functions as Vectors
videoId: TgKwz5Ikpc8
---

From: [[3blue1brown]] <br/> 

The traditional understanding of vectors often starts with visualizable concepts like arrows on a flat plane or lists of numbers <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. However, linear algebra delves into a deeper, more abstract notion of what a vector truly is <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This deeper understanding reveals that even functions can be considered a type of vector <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Vector-ish Qualities of Functions

Functions exhibit properties analogous to those of traditional vectors:

*   **Addition**: Just as two vectors can be added, two functions (f and g) can be added to produce a new function (f + g) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. The output of this new function at any given input (e.g., -4) is the sum of the outputs of f and g at that same input <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. More generally, (f + g)(x) = f(x) + g(x) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This parallels adding vectors coordinate by coordinate, though with potentially infinitely many "coordinates" <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Scaling**: Functions can also be scaled by a real number, meaning all outputs are multiplied by that number <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This is analogous to scaling a vector by multiplying each of its coordinates <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Given that the fundamental operations for vectors are addition and scaling, it is possible to apply the concepts and problem-solving techniques of linear algebra, originally conceived for arrows in space, to functions as well <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Linear Transformations for Functions

The concept of a linear transformation also applies to functions, where it takes one function and transforms it into another <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. In this context, these transformations are sometimes called "operators" <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

A prominent example from calculus is the derivative <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The derivative transforms one function into another <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. For a transformation to be linear, it must satisfy two properties:

*   **Additivity**: If you add two functions (f and g) and then apply the transformation, the result is the same as applying the transformation to each function separately and then adding the transformed versions <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. For derivatives: d/dx (f(x) + g(x)) = d/dx f(x) + d/dx g(x) <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Scaling**: If you scale a function by a number and then apply the transformation, the result is the same as first applying the transformation and then scaling the result by the same amount <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. For derivatives: d/dx (c * f(x)) = c * d/dx f(x) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

These properties are what define [[Visualizing transformations with vectors|linear transformations]] in an abstract sense <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, allowing them to apply to functions as well as geometric arrows <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. A key consequence of linearity is that a linear transformation is completely described by where it maps the [[Basis vectors in three dimensions|basis vectors]] <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Representing the Derivative with a Matrix

To illustrate how functions can be treated as vectors and undergo [[matrixvector multiplication|matrix-vector multiplication]], consider the space of polynomials, such as `x^2 + 3x + 5` or `4x^7 - 5x^2` <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

1.  **Choosing a Basis**: Polynomials are naturally expressed as sums of scaled powers of `x`. Therefore, a natural choice for basis functions are `b0(x) = 1`, `b1(x) = x`, `b2(x) = x^2`, `b3(x) = x^3`, and so on <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This set of basis functions is infinite because polynomials can have arbitrarily large degrees <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
2.  **Assigning Coordinates**: Each polynomial can be described by coordinates based on these basis functions. For example, `x^2 + 3x + 5` would have coordinates `(5, 3, 1, 0, 0, ...)` (5 times `b0`, 3 times `b1`, 1 time `b2`, and infinitely many zeros) <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. A polynomial like `4x^7 - 5x^2` would be `(0, 0, -5, 0, 0, 0, 0, 4, 0, ...)` <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
3.  **The Derivative as a Matrix**: In this coordinate system, the derivative can be represented by an infinite matrix <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This matrix is mostly zeros but has positive integers counting down on an offset diagonal <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   Applying this matrix to the coordinates `(5, 4, 1, 1, 0, ...)` representing `x^3 + 5x^2 + 4x + 5` demonstrates its action <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
    *   The first coordinate of the result `(4, 10, 3, 0, ...)` comes from `1 * 4`, corresponding to the derivative of `4x` being `4` <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
    *   The second coordinate comes from `2 * 5`, corresponding to the derivative of `5x^2` being `10x` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   The third coordinate comes from `3 * 1`, corresponding to the derivative of `x^3` being `3x^2` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    *   This works because the derivative is a linear transformation <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. The matrix can be constructed by finding the derivative of each basis function and placing the coordinates of the results in each column <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

This demonstrates that [[matrixvector multiplication|matrix-vector multiplication]] and taking a derivative, seemingly distinct operations, are fundamentally related within the framework of linear algebra <a class="yt-timestamp" data-t="00:10:59">[00:11:03]</a>.

## The Abstract Nature of Vectors

Many core concepts of linear algebra, such as the [[Dot products and vectors|dot product]] or [[Dot products and vectors|eigenvectors]], have direct counterparts in the world of functions, often under different names like "inner product" or "eigenfunction" <a class="yt-timestamp" data-t="00:11:11">[00:11:19]</a>.

Ultimately, linear algebra defines "vectors" not by their specific form (arrows, lists of numbers), but by their behavior <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. Any set of objects where there's a reasonable notion of scaling and adding that adheres to a specific list of rules, known as axioms, can be considered a "vector space" <a class="yt-timestamp" data-t="00:11:35">[00:11:51]</a>. These eight axioms ensure that the theory and constructs of linear algebra apply broadly <a class="yt-timestamp" data-t="00:12:32">[00:12:40]</a>.

For instance, the definition of [[Visualizing transformations with vectors|linear transformations]] in textbooks is often phrased in terms of additivity and scaling (the axioms) rather than visualizable gridlines, precisely so it can apply to all types of "vectorish" things, including functions <a class="yt-timestamp" data-t="00:14:01">[00:14:09]</a>.

The modern answer to "[[Definition and Nature of Vectors|What are vectors?]]" is to view them as an abstraction <a class="yt-timestamp" data-t="00:14:22">[00:14:27]</a>. Just as the number `3` is an abstraction for all possible triplets of things, a vector is an abstraction for all entities that can be added and scaled according to the vector space axioms <a class="yt-timestamp" data-t="00:14:41">[00:15:02]</a>. While an intuitive understanding often begins with concrete examples like arrows in 2D space, linear algebra's power lies in its broad applicability to functions and other abstract mathematical objects <a class="yt-timestamp" data-t="00:15:08">[00:15:24]</a>.