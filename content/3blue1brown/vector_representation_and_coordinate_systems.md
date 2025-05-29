---
title: Vector representation and coordinate systems
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 

The fundamental building block for linear algebra is the vector <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Understanding vectors requires distinguishing between three perspectives: the physics student, the computer science student, and the mathematician <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Perspectives on Vectors

### Physics Student Perspective
From a physics student's viewpoint, vectors are arrows pointing in space <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A vector is defined by its length and direction; it remains the same vector even if moved to a different location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Vectors can be two-dimensional (in a flat plane) or three-dimensional (in broader space) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Computer Science Student Perspective
For a computer science student, vectors are ordered lists of numbers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, analyzing house prices might involve modeling each house with a pair of numbers, where the first is square footage and the second is price <a class="yt="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The order of these numbers matters <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. In this context, "vector" is essentially a fancy word for a list, and its dimension is determined by the length of that list <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Mathematician's Perspective
The mathematician's perspective generalizes both views, defining a vector as anything where there is a sensible notion of adding two vectors and multiplying a vector by a number <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. While abstract, this view highlights the importance of vector addition and scalar multiplication in linear algebra <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For practical purposes, it's often healthy to initially favor a more concrete setting <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## The Chosen Perspective for Linear Algebra
For this series, the primary mental image for a vector will be an arrow <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Specifically, think of this arrow within a [[coordinate_systems_and_basis_vectors | coordinate system]], such as the xy-plane, with its tail fixed at the origin <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This differs from the physics student's view, as vectors in linear algebra are almost always rooted at the origin <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Once a concept is understood geometrically, it can be translated to the "list of numbers" perspective by considering the vector's coordinates <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## [[coordinate_systems_and_basis_vectors | Coordinate Systems]]

[[coordinate_systems_and_basis_vectors | Coordinate systems]] are essential for translating between the arrow and list perspectives of vectors <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Two-Dimensional Space
In two dimensions, a [[coordinate_systems_and_basis_vectors | coordinate system]] consists of a horizontal **x-axis** and a vertical **y-axis** <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Their intersection is the **origin**, considered the center of space and the root of all vectors <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Tick marks on each axis, representing a chosen unit length, help define distances <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. When depicting 2D space, these tick marks extend into grid lines <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

The **coordinates** of a vector are a pair of numbers that provide instructions to get from the vector's tail (at the origin) to its tip <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:
*   The first number indicates movement along the x-axis (positive for right, negative for left) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   The second number indicates movement parallel to the y-axis (positive for up, negative for down) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

Vectors are conventionally written as a vertical pair of numbers enclosed in square brackets <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Each pair of numbers uniquely defines a vector, and each vector uniquely corresponds to a pair of numbers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Three-Dimensional Space
In three dimensions, a **z-axis** is added, perpendicular to both the x and y-axes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Each vector is then associated with an ordered triplet of numbers <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>:
*   The first for x-axis movement <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   The second for y-axis parallel movement <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   The third for z-axis parallel movement <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
Similarly, every triplet corresponds to a unique vector, and vice versa <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Fundamental Vector Operations
Every topic in linear algebra centers around two fundamental operations: vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Vector Addition
To add two vectors (e.g., vector A and vector B), conceptually move the second vector (B) so its tail rests at the tip of the first vector (A) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. The sum is a new vector drawn from the tail of the first vector to the tip of the second <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This "tip-to-tail" method is one of the few instances in linear algebra where vectors are allowed to stray from the origin <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

This definition is intuitive when considering vectors as movements <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Taking a step along the first vector, then another along the second, results in the same overall displacement as moving directly along their sum <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Numerically, vector addition involves matching up corresponding terms and adding them together <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, e.g., if vector 1 is (1, 2) and vector 2 is (3, -1), their sum is (1+3, 2-1) = (4, 1) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

### Scalar Multiplication
Multiplying a vector by a number, called a **scalar**, scales the vector <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   Multiplying by a positive scalar (e.g., 2) stretches the vector by that factor <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   Multiplying by a positive fraction (e.g., one-third) squishes it <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   Multiplying by a negative scalar (e.g., -1.8) first flips the vector's direction, then stretches it by the absolute value of the factor <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

Because numbers frequently act to scale vectors in linear algebra, the terms "scalar" and "number" are often used interchangeably <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. Numerically, scalar multiplication means multiplying each component of the vector by the scalar <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>, e.g., 2 multiplied by vector (1, 2) becomes (2*1, 2*2) = (2, 4) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## Interplay of Perspectives
The utility of linear algebra comes from the ability to translate back and forth between the geometric (arrows in space) and numerical (lists of numbers) views <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. This translation allows data analysts to visualize complex data patterns and operations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, while providing physicists and computer graphics programmers a numerical language to describe and manipulate space <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.