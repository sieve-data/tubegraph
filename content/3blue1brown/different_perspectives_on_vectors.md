---
title: Different perspectives on vectors
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 

The fundamental building block for [[understanding_vectors_in_linear_algebra | linear algebra]] is the vector <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. There are broadly three distinct, but related, ideas about what a vector is <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>:
*   The physics student perspective <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   The computer science student perspective <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   The mathematician's perspective <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

## Physics Student Perspective

From a physics student's point of view, [[nature_of_vectors | vectors]] are arrows pointing in space <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A vector is defined by its length and the direction it points <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. As long as these two properties remain the same, a vector can be moved around in space and still be considered the same vector <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. [[vectors_in_two_and_three_dimensions | Vectors]] can exist in a flat plane (two-dimensional) or in broader space (three-dimensional) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Computer Science Student Perspective

In computer science, [[nature_of_vectors | vectors]] are often viewed as ordered lists of numbers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, if analyzing house prices based on square footage and price, each house could be modeled as a pair of numbers, where the first is square footage and the second is price <a class="yt-timestamp" data-t="00:00:55">[00:01:05]</a>. The order of these numbers matters <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. In this context, houses would be modeled as two-dimensional vectors, with "vector" being a term for a list, and its dimensionality determined by the list's length <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Mathematician's Perspective

The mathematician seeks to generalize both the physics and computer science views <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. From this abstract perspective, a vector is anything that supports a sensible notion of adding two vectors and multiplying a vector by a number <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. While this view is important for understanding [[functions_as_vectors | functions as vectors]] or generalized vector spaces, it is often best to understand more concrete settings first <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. However, this perspective highlights that vector addition and scalar multiplication are central to [[understanding_vectors_in_linear_algebra | linear algebra]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Preferred Geometric Focus in Linear Algebra

For understanding [[understanding_vectors_in_linear_algebra | linear algebra]], a geometric focus is often adopted <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. When a vector is mentioned, it's helpful to visualize it as an arrow within a coordinate system, such as the xy-plane, with its tail fixed at the origin <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This differs from the physics perspective, where vectors can freely exist anywhere in space <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. In [[understanding_vectors_in_linear_algebra | linear algebra]], vectors are almost always rooted at the origin <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Concepts are first understood geometrically, then translated to the list of numbers perspective by considering the vector's coordinates <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This translation is crucial as it bridges the two main ways of thinking about vectors <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Coordinate System and Vector Representation

In two dimensions, a coordinate system consists of a horizontal x-axis and a vertical y-axis <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Their intersection is the origin, which serves as the center of space and the root of all vectors <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Tick marks on each axis represent unit distances <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

The coordinates of a vector are a pair of numbers that provide instructions to get from its tail at the origin to its tip <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:
*   The first number indicates horizontal movement along the x-axis (positive for right, negative for left) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   The second number indicates vertical movement parallel to the y-axis (positive for up, negative for down) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

To distinguish vectors from points, these pairs of numbers are conventionally written vertically within square brackets <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Every pair of numbers corresponds to one unique vector, and every vector corresponds to one unique pair of numbers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This is part of the [[representation_of_vectors_using_basis_vectors | representation of vectors using basis vectors]] concept.

For [[vectors_in_two_and_three_dimensions | vectors in three dimensions]], a third axis (the z-axis) is added, perpendicular to both the x and y-axes <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Each vector is then associated with an ordered triplet of numbers, indicating movement along the x-axis, parallel to the y-axis, and parallel to the z-axis <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Similarly, every triplet of numbers defines a unique vector, and vice versa <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Fundamental Vector Operations

Every topic in [[understanding_vectors_in_linear_algebra | linear algebra]] revolves around two fundamental operations: vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Vector Addition

Geometrically, to add two vectors (e.g., one pointing up-right and another right-down), move the second vector so its tail sits at the tip of the first <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. The sum is a new vector drawn from the tail of the first to the tip of the second <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This "tip-to-tail" method is one of the few instances where vectors are allowed to stray from the origin in [[understanding_vectors_in_linear_algebra | linear algebra]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

Conceptually, vectors can represent movements <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. If you take a step described by the first vector, then another described by the second, the overall effect is equivalent to moving along their sum <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. This is analogous to adding numbers on a number line <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

Numerically, if the first vector has coordinates (1, 2) and the second has (3, -1), their sum is found by adding their corresponding components: (1+3, 2-1) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. In general, for vectors represented as lists of numbers, addition means matching up and adding each term together <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### Scalar Multiplication

Multiplication of a vector by a number (a "scalar") involves "scaling" the vector <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>:
*   Multiplying by a positive number like 2 stretches the vector to be twice as long <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   Multiplying by a fraction like one-third squishes it to one-third its original length <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   Multiplying by a negative number like -1.8 flips the vector's direction, then stretches it by that factor <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

The process of stretching, squishing, or reversing a vector's direction is called scaling <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Numbers that perform this scaling are called scalars <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. In [[understanding_vectors_in_linear_algebra | linear algebra]], the terms "scalar" and "number" are often used interchangeably <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

Numerically, scaling a vector by a factor (e.g., 2) means multiplying each of its components by that factor <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. If a vector is (1, 2), multiplying by 2 yields (2, 4) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## The Utility of Both Perspectives

[[understanding_vectors_in_linear_algebra | Linear algebra]] concepts fundamentally revolve around vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. While the mathematician's abstract view emphasizes these operations independent of representation, the practical value of [[understanding_vectors_in_linear_algebra | linear algebra]] lies in the ability to translate between the geometric (arrows in space) and numerical (lists of numbers) perspectives <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

This dual understanding provides significant benefits:
*   **Data Analysts**: It offers a visual way to conceptualize lists of numbers, clarifying data patterns and providing a global view of operations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This is relevant to [[applications_of_vectors_in_data_analysis_and_computer_graphics | applications of vectors in data analysis and computer graphics]].
*   **Physicists and Computer Graphics Programmers**: It provides a numerical language to describe and manipulate space, enabling computations <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. For example, creating animations involves thinking geometrically about spatial changes and then using [[understanding_vectors_in_linear_algebra | linear algebra]] to numerically determine pixel placement <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

Future discussions in [[understanding_vectors_in_linear_algebra | linear algebra]] will build upon these vector basics, introducing concepts like [[span_of_vectors | span]], bases, and linear dependence <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.