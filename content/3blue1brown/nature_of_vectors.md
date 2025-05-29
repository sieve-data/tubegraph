---
title: Nature of vectors
videoId: TgKwz5Ikpc8
---

From: [[3blue1brown]] <br/> 

The fundamental question "What are vectors?" has deceptively simple answers that hint at a deeper mathematical concept <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While seemingly straightforward, the nature of a vector can be viewed from [[different_perspectives_on_vectors | different perspectives]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Different Perspectives on Vectors

Two primary viewpoints initially emerge when considering what a vector is:

*   **As an arrow on a flat plane**: This visual representation describes a two-dimensional vector with coordinates for convenience <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **As a pair of real numbers**: This defines a vector fundamentally as a list of numbers, which is then visualized as an arrow <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

Each perspective has its advantages:

*   **List of numbers**: Defining vectors as a list of numbers feels unambiguous and makes concepts like four-dimensional or 100-dimensional vectors seem concrete and workable <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Without this, higher dimensions might remain a vague geometric notion <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Spatial/Geometric**: For those fluent in linear algebra, particularly with changing [[basis_vectors | basis]], there's a sensation that a space exists independently of the coordinates given to it <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Coordinates are seen as somewhat arbitrary, depending on the chosen [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Core linear algebra concepts like determinants and eigenvectors are inherently spatial and indifferent to the choice of coordinate systems <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

This leads to the question of whether both are merely manifestations of something deeper <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. If vectors are not fundamentally lists of numbers but something more spatial, it raises the question of what "space" or "spatial" truly means in mathematics <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Functions as Vectors

The concept of a vector extends beyond arrows or lists of numbers to include [[functions_as_vectors | functions]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Properties of Functions analogous to Vectors

*   **Addition**: Just like vectors, two [[functions_as_vectors | functions]] (f and g) can be added together to produce a new function (f + g) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. The output of this new function at any input is the sum of the individual function outputs at that same input <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This is analogous to adding vectors coordinate by coordinate, but with infinitely many coordinates <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Scaling**: A function can be scaled by a real number by scaling all of its outputs by that number <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This is similar to scaling a vector coordinate by coordinate <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Since vectors are primarily defined by their ability to be added and scaled, the problem-solving techniques of linear algebra can be applied to [[functions_as_vectors | functions]] <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Linear Transformations for Functions

A [[understanding_vector_fields | linear transformation]] can also apply to functions, transforming one function into another <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. In this context, they are sometimes called "operators" <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

An example is the derivative from calculus <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. A transformation is linear if it satisfies two properties:

1.  **Additivity**: Adding two vectors (or functions) and then applying the transformation yields the same result as applying the transformation to each individually and then adding their transformed versions <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. For derivatives, taking the derivative of a sum of functions is the same as summing their individual derivatives <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
2.  **Scaling**: Scaling a vector (or function) by a number and then applying the transformation yields the same result as applying the transformation first and then scaling the transformed version <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. For derivatives, scaling a function and then taking its derivative is the same as taking the derivative and then scaling the result <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

These properties mean linear transformations preserve the operations of vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. A key consequence is that a linear transformation is entirely described by where it maps the [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This principle holds true for functions as well as arrows <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

### The Derivative as a Matrix Operation

To describe the derivative with a matrix, consider a space of polynomials <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
1.  **Choosing a basis**: Powers of x (e.g., 1, x, x², x³) naturally serve as [[basis_vectors | basis functions]] <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This set of [[basis_vectors | basis functions]] is infinite as polynomials can have arbitrarily large degrees <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
2.  **Coordinates for polynomials**: A polynomial like x² + 3x + 5 can be represented by coordinates (5, 3, 1, 0, 0, ...) reflecting the coefficients of its [[basis_vectors | basis functions]] <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
3.  **The matrix**: The derivative can then be described by an infinite matrix with positive integers counting down an offset diagonal <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Applying this matrix to the coordinate representation of a polynomial yields the coordinates of its derivative <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

This demonstrates that matrix-vector multiplication and taking a derivative are fundamentally members of the same family of operations because the derivative is linear <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Many linear algebra concepts, such as the dot product or eigenvectors, have direct analogues in the world of functions, often under different names (e.g., inner product or eigenfunction) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## What is a Vector? The Abstract View

The modern mathematical answer to "what is a vector?" ignores the specific form <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Any set of objects where there's a sensible notion of scaling and adding can be considered "vectorish" <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This includes arrows, lists of numbers, [[functions_as_vectors | functions]], or other abstract entities <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

These sets of "vectorish" things are called [[abstract_vector_spaces | vector spaces]] <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. To ensure that all the tools of linear algebra apply generally, mathematicians establish a list of rules, or **axioms**, that vector addition and scaling must abide by <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. The modern theory of linear algebra uses eight such axioms <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

> [!NOTE] Axioms of Vector Spaces
> These axioms serve as a checklist to ensure that the definitions of vector addition and scalar multiplication behave as expected <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. They act as an interface between mathematicians developing results and others applying those results to new kinds of [[abstract_vector_spaces | vector spaces]] <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. By proving results only in terms of these axioms, mathematicians ensure their work applies to any system satisfying them, regardless of the system's specific nature <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

Consequently, mathematical results in linear algebra are often phrased abstractly, centering on these axioms rather than specific types of vectors like arrows or functions <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This is why textbooks define linear transformations by additivity and scaling, even if a geometric interpretation (like gridlines remaining parallel and evenly spaced) is more intuitive for beginners <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

A vector, therefore, is an abstraction for many embodiments, much like the number 3 abstracts all possible triplets of things <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. While it's beneficial to start learning about vectors in a concrete, visualizable setting (like 2D space with arrows) <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>, understanding the broader applicability of linear algebra tools is crucial as one progresses in the topic <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.