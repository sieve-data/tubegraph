---
title: Linear Transformations and Linearity
videoId: TgKwz5Ikpc8
---

From: [[3blue1brown]] <br/> 

## What are Vectors? Reconsidering the Definition

The fundamental nature of vectors can be a deceptively simple question [00:00:16]. Are two-dimensional vectors primarily arrows on a flat plane, described by coordinates for convenience, or are they fundamentally pairs of real numbers visualized as arrows [00:00:24]? Both perspectives might be manifestations of something deeper [00:00:38].

Defining vectors as a list of numbers provides a clear-cut and unambiguous approach, making concepts like four-dimensional or 100-dimensional vectors seem concrete and workable [00:00:42]. Without this numerical definition, higher dimensions can be vague geometric notions [00:00:55].

However, those who work with [[linear_transformations_in_linear_algebra | linear algebra]] often feel they are dealing with a space independent of the chosen coordinates, which can be arbitrary based on the basis vectors [00:01:05]. Core concepts like determinants and eigenvectors are indifferent to the coordinate system [00:01:24]. A determinant reflects how much a [[linear_transformations | transformation]] scales areas, and eigenvectors remain on their own span during a [[linear_transformations | transformation]] [00:01:31]. These properties are inherently spatial and their underlying values do not change with coordinate system changes [00:01:40]. This raises the question of what mathematicians mean by "space" or "spatial" if vectors aren't fundamentally lists of numbers [00:01:50].

## Functions as Vectors

Functions can be considered another type of vector due to their "vector-ish qualities" [00:02:09]. Just as two vectors can be added, two functions (f and g) can be added to form a new function (f plus g) [00:02:19]. The output of this new function at any input is the sum of the outputs of f and g at that same input (e.g., (f+g)(x) = f(x) + g(x)) [00:02:33]. This is analogous to adding vectors coordinate by coordinate, albeit with infinitely many coordinates [00:03:00].

Similarly, a function can be scaled by a real number by scaling all its outputs by that number [00:03:11]. This mirrors scaling a vector coordinate by coordinate, again suggesting infinitely many coordinates [00:03:20]. Because vectors can only be added or scaled, the useful constructs and problem-solving techniques of [[linear_transformations_in_linear_algebra | linear algebra]] can be applied to functions as well [00:03:28].

## [[linear_transformations | Linear Transformations]] of Functions

There is a reasonable notion of a [[linear_transformations | linear transformation]] for functions, which takes one function and converts it into another [00:03:46]. A familiar example from calculus is the derivative, which transforms one function into another [00:03:59]. In this context, these are sometimes called "operators" instead of [[linear_transformations | transformations]], but the meaning is the same [00:04:08].

### Defining [[linear_transformations | Linearity]]

A [[linear_transformations | transformation]] of functions is linear if it satisfies two properties: additivity and scaling [00:04:16]. While the formal definition of linearity is abstract, it is general enough to apply to functions as well as arrows [00:04:22].

*   **Additivity**: If two vectors (or functions) `v` and `w` are added, and then the [[linear_transformations | transformation]] is applied to their sum, the result is the same as if the [[linear_transformations | transformed]] versions of `v` and `w` were added together [00:04:46].
*   **Scaling**: If a vector (or function) `v` is scaled by a number, and then the [[linear_transformations | transformation]] is applied, the ultimate vector is the same as if the [[linear_transformations | transformed]] version of `v` was scaled by the same amount [00:05:04].

In essence, [[linear_transformations | linear transformations]] preserve the operations of vector addition and scalar multiplication [00:05:21]. The idea of [[visual_understanding_of_linear_transformations | gridlines remaining parallel and evenly spaced]] is an illustration of these properties for points in 2D space [00:05:32].

One significant consequence of these properties is that a [[linear_transformations | linear transformation]] is entirely described by where it maps the basis vectors [00:05:44]. Since any vector can be expressed as a combination of scaled and added basis vectors, the [[linear_transformations | transformed]] version of a vector can be found by scaling and adding the [[linear_transformations | transformed]] basis vectors in the same way [00:05:57]. This principle applies to functions as well as arrows [00:06:12].

Calculus students implicitly use the additive and scaling properties of the derivative [00:06:18]:
*   Adding two functions and then taking the derivative is the same as taking the derivative of each function separately and then adding the results [00:06:28].
*   Scaling a function and then taking the derivative is the same as first taking the derivative and then scaling the result [00:06:40].

### [[Matrix representation of linear transformations | Matrix Representation of the Derivative]]

Even though function spaces can be infinite-dimensional, the derivative can be described with a matrix [00:06:56]. Consider the space of polynomials, which include polynomials with arbitrarily large degrees but finitely many terms [00:07:04].

To give coordinates to this space, a basis is chosen. Natural basis functions are pure powers of `x`: `b0(x) = 1`, `b1(x) = x`, `b2(x) = x squared`, `b3(x) = x cubed`, and so on [00:07:28]. These basis functions serve a role similar to `i-hat`, `j-hat`, and `k-hat` for vectors as arrows [00:07:53].

Since polynomials can have arbitrarily large degrees, this set of basis functions is infinite, meaning polynomials as vectors will have infinitely many coordinates [00:08:02]. For example:
*   `x squared + 3x + 5` would have coordinates `(5, 3, 1, 0, 0, ...)` [00:08:15]. This means it's `5` times the first basis function (`1`), plus `3` times the second basis function (`x`), plus `1` times the third basis function (`x squared`), and so on [00:08:26].
*   `4x to the seventh - 5x squared` would have coordinates `(0, 0, -5, 0, 0, 0, 0, 4, 0, 0, ...)` [00:08:40].

In this coordinate system, the derivative is described by an infinite [[Matrix representations of linear transformations | matrix]] with positive integers counting down on an offset diagonal [00:09:06]. This matrix can be constructed by taking the derivative of each basis function and placing the coordinates of the results into each column [00:10:34].

For example, applying this [[Matrix representations of linear transformations | matrix]] to the coordinates of `x cubed + 5x squared + 4x + 5` (which are `(5, 4, 5, 1, 0, ...)`) results in the coordinates for its derivative:
*   The first coordinate of the result (constant term) is `1 * 4 = 4` (derivative of `4x` is `4`) [00:09:40].
*   The second coordinate (coefficient of `x`) is `2 * 5 = 10` (derivative of `5x squared` is `10x`) [00:09:55].
*   The third coordinate (coefficient of `x squared`) is `3 * 1 = 3` (derivative of `x cubed` is `3x squared`) [00:10:10].
*   Subsequent terms are zero [00:10:23].

This demonstrates how matrix-vector multiplication and taking a derivative, seemingly disparate operations, are part of the same family because the derivative is [[linear_transformations | linear]] [00:11:03].

## The Abstract Nature of Vectors and Vector Spaces

Many concepts from [[linear_transformations_in_linear_algebra | linear algebra]], such as the dot product or eigenvectors, have direct analogs in the world of functions (e.g., inner product or eigenfunction) [00:11:11].

The core idea is that "vector-ish" things in mathematics are abundant [00:11:31]. As long as a set of objects has a reasonable notion of scaling and adding—whether arrows, lists of numbers, functions, or other definitions—all the tools of [[linear_transformations_in_linear_algebra | linear algebra]], including [[linear_transformations | linear transformations]], can apply [00:11:35].

Mathematicians define vector spaces to ensure their definitions and discoveries apply broadly [00:11:57]. A vector space is a set of "vectorish things" that adheres to a list of rules for vector addition and scaling, known as axioms [00:12:18]. There are eight axioms in modern [[linear_transformations_in_linear_algebra | linear algebra]] that any vector space must satisfy for the theory to apply [00:12:36]. These axioms are not fundamental rules of nature but rather an "interface" between the mathematician developing results and others who might apply those results to new vector spaces [00:12:58].

For instance, if someone defines a new type of vector space (e.g., "pi creatures" with custom addition and scaling), they must verify that their definitions satisfy these axioms before applying [[linear_transformations_in_linear_algebra | linear algebra]] results [00:13:11]. This allows mathematicians to prove results abstractly, based only on these axioms, without needing to consider every specific embodiment of a vector [00:13:34].

Consequently, textbooks and lectures define [[linear_transformations | linear transformations]] in terms of additivity and scaling, rather than intuitive visual aids like gridlines [00:14:01]. This abstract approach is crucial for the generality of the theory [00:14:13].

The modern mathematical answer to "what are vectors?" is to largely disregard their concrete form [00:14:22]. Arrows, lists, functions, or any other defined entity can be a vector, provided their addition and scaling operations follow the established axioms [00:14:31]. Just as the number `3` is an abstraction for all possible triplets of things, vectors are an abstraction for all possible embodiments of objects that behave according to the vector space axioms [00:14:41].

While it's beneficial to start learning [[linear_transformations_in_linear_algebra | linear algebra]] with concrete, visualizable settings like 2D arrows, it's important to recognize that these tools apply much more generally [00:15:08]. This broader applicability is the underlying reason for the abstract phrasing found in advanced texts and lectures [00:15:22].