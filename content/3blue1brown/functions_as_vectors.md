---
title: Functions as vectors
videoId: TgKwz5Ikpc8
---

From: [[3blue1brown]] <br/> 

The question of "what are vectors?" extends beyond the common visualization of arrows or lists of numbers, suggesting a deeper, more fundamental nature. One perspective explores whether both of these ideas are simply manifestations of something more profound <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. While defining vectors as lists of numbers offers a clear and unambiguous approach, especially for high-dimensional vectors, it can lack a concrete geometric intuition <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Conversely, many who work with linear algebra, particularly when adept at changing their [[Representation of vectors using basis vectors|basis vectors]], feel they are interacting with a space that exists independently of its given coordinates <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This points to a spatial essence, even if the definition of "space" or "spatial" needs further clarification <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

To explore this deeper essence, it's useful to consider objects that are neither arrows nor lists of numbers but possess "vector-ish qualities": functions <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Functions as a Type of Vector

Functions can be understood as another type of vector <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Just as vectors can be added and scaled, so too can functions:

*   **Addition**: There is a sensible way to add two functions, *f* and *g*, to create a new function, *f* plus *g* <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. The output of this new function at any given input *x* is the sum of the outputs of *f*(*x*) and *g*(*x*) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This is analogous to adding vectors coordinate by coordinate, but with "infinitely many coordinates" <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Scalar Multiplication**: Similarly, a function can be scaled by a real number by scaling all its outputs by that number <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This is analogous to scaling a vector coordinate by coordinate, again with the feeling of infinitely many coordinates <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Since the fundamental operations of vectors are addition and scaling, it implies that the useful constructs and problem-solving techniques of linear algebra, originally conceived for arrows and space, can be applied to functions as well <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Linear Transformations of Functions

A direct parallel exists for linear transformations in the context of functions <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. These transformations take one function and turn it into another <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

A familiar example from calculus is the **derivative** <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The derivative transforms one function into another <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. In this context, such transformations are often called **operators** <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

A transformation of functions is considered **linear** if it satisfies two properties <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>:
1.  **Additivity**: If you add two functions (*f* and *g*) and then apply the transformation, the result is the same as if you applied the transformation to each function separately and then added the results <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>, e.g., d/dx (*f* + *g*) = d/dx *f* + d/dx *g* <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
2.  **Scaling**: If you scale a function (*f*) by some number (*c*) and then apply the transformation, the result is the same as if you first applied the transformation to *f* and then scaled the result by *c* <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>, e.g., d/dx (*c* *f*) = *c* * d/dx *f* <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

These properties mean that linear transformations "preserve the operations of vector addition and scalar multiplication" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. A significant consequence is that a linear transformation is entirely described by where it takes the [[basis_vectors|basis vectors]] <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This principle applies equally to functions as it does to arrows <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

### Representing Functions with a Matrix

While function spaces often have infinite dimensions, the derivative can be described with a matrix by limiting the scope, for example, to polynomials <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

1.  **Choosing a Basis**: Polynomials are naturally expressed as sums of scaled powers of *x* (e.g., x² + 3x + 5). Therefore, natural [[basis_vectors|basis vectors]] (or basis functions) can be chosen as pure powers of *x*: b₀(*x*) = 1, b₁(*x*) = *x*, b₂(*x*) = *x*², b₃(*x*) = *x*³, and so on <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This set of basis functions is infinite because polynomials can have arbitrarily large degrees <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
2.  **Assigning Coordinates**: Treating polynomials as vectors means they will have infinitely many coordinates <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. For example, x² + 3x + 5 would be represented by the coordinates [5, 3, 1, 0, 0, ...] (5 times b₀, 3 times b₁, 1 time b₂, and zeros for higher powers) <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
3.  **The Derivative Matrix**: In this coordinate system, the derivative can be represented by an infinite matrix <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This matrix is mostly zeros but has positive integers counting down on an offset diagonal <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This matrix can be constructed by taking the derivative of each basis function and placing the coordinates of the results into each column <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

Applying this matrix to the coordinate representation of a polynomial yields the coordinates of its derivative <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. For instance, deriving x³ + 5x² + 4x + 5 results in 3x² + 10x + 4, which aligns with the matrix multiplication process <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. The ability to describe the derivative with a matrix is possible precisely because the derivative is linear <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

This demonstrates that matrix-vector multiplication and taking a derivative, seemingly disparate operations, are fundamentally members of the same family <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Many [[Understanding vectors in linear algebra|linear algebra concepts]], such as dot products or eigenvectors, have direct parallels in the world of functions, often under different names like "inner product" or "eigenfunction" <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## [[Abstract vector spaces|Abstract Vector Spaces]]

The understanding that functions can behave as vectors points to the idea that there are many "vectorish things" in mathematics <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. As long as a set of objects allows for a reasonable notion of scaling and adding—whether they are arrows, lists of numbers, functions, or other concepts—all the tools of linear algebra can be applied <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

These sets of "vectorish things" are called [[Abstract vector spaces|vector spaces]] <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. To ensure that linear algebra definitions and discoveries apply generally, mathematicians establish a set of rules, called **axioms**, that vector addition and scaling must adhere to <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. There are eight such axioms that any vector space must satisfy <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. These axioms serve as an interface, allowing discoveries proven in terms of these abstract rules to be applied to any system that satisfies them, without needing to consider every specific embodiment <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

Consequently, modern linear algebra tends to define results abstractly, based only on these axioms, rather than focusing on a specific type of vector like arrows in space or functions <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. This is why linear transformations are formally defined by their additivity and scaling properties, even though visual analogies (like gridlines remaining parallel and evenly spaced) can be more intuitive for beginners <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

Ultimately, in modern linear algebra, the specific form that vectors take is less important <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. The core idea is that as long as addition and scaling follow the established axioms, the full theory of linear algebra applies <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. Vectors, in this view, are an abstraction that encompasses many different embodiments, allowing for a single theoretical framework to reason about them all <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.