---
title: Vectors in two and three dimensions
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 

The vector is the fundamental building block of [[understanding_vectors_in_linear_algebra | linear algebra]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. There are three distinct, yet related, perspectives on what a vector is: the physics student perspective, the computer science student perspective, and the mathematician's perspective <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Different Perspectives on Vectors

### Physics Student Perspective
From this viewpoint, vectors are arrows pointing in space <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A vector is defined by its length and direction <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. As long as these two properties remain the same, the vector can be moved anywhere in space and still be considered the same vector <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Two-dimensional vectors** live in a flat plane <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   **Three-dimensional vectors** exist in broader space <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Computer Science Student Perspective
In this view, vectors are ordered lists of numbers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, in house price analytics, a house might be modeled with a pair of numbers: square footage and price <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The order of these numbers matters <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. A "two-dimensional vector" in this context is simply a list of two numbers <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Mathematician's Perspective
The mathematician's perspective generalizes both previous views, defining a vector as anything where there's a sensible way to add two vectors and multiply a vector by a number <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This is a more [[abstract_vector_spaces | abstract vector space]] viewpoint, where the specific details of representation are less important than the operations that can be performed <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This perspective highlights the importance of vector addition and scalar multiplication in linear algebra <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Vectors in Linear Algebra: A Geometric Focus
For a geometric understanding of vectors, it's often helpful to think of a vector as an arrow rooted at the origin of a coordinate system <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Unlike the physics student's view, where vectors can freely move, in linear algebra, vectors are typically rooted at the origin <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Coordinate Systems
The bridge between the arrow (geometric) and list of numbers (numerical) perspectives is the coordinate system <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

#### Two Dimensions
In two dimensions:
*   A horizontal line is the **x-axis**, and a vertical line is the **y-axis** <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   Their intersection is the **origin**, considered the center of space and the root of all vectors <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Coordinates** are a pair of numbers that instruct how to get from the origin (tail) to the tip of the vector <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   The first number indicates horizontal movement along the x-axis (positive for right, negative for left) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   The second number indicates vertical movement parallel to the y-axis (positive for up, negative for down) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   Vectors are typically written vertically with square brackets, e.g., `[x, y]` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Every pair of numbers corresponds to a unique vector, and every vector corresponds to a unique pair of numbers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

#### Three Dimensions
In three dimensions:
*   A third axis, the **z-axis**, is added, perpendicular to both the x and y-axes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   Each vector is associated with an ordered triplet of numbers (x, y, z) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   The first number for x-axis movement <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   The second for y-axis movement <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   The third for z-axis movement <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Every triplet defines a unique vector, and every vector has a unique triplet of numbers <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
[[basis_vectors_in_threedimensional_space | Visualizing transformations in three dimensions]] and understanding vectors in this context are crucial.

## Fundamental Vector Operations
Every topic in linear algebra revolves around these two operations: vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Vector Addition
*   **Geometric Definition**: To add two vectors, move the tail of the second vector to the tip of the first vector. The sum is a new vector drawn from the tail of the first to the tip of the second <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This is often conceptualized as taking one step (first vector) then another step (second vector), with the sum representing the overall displacement <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This tip-to-tail method is almost the only time vectors are allowed to stray from the origin in linear algebra <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Numerical Definition**: When vectors are represented as lists of numbers, vector addition is performed by adding their corresponding components together <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, if vector A = [1, 2] and vector B = [3, -1], their sum A + B = [1+3, 2+(-1)] = [4, 1] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Scalar Multiplication
*   **Geometric Definition**: Multiplying a vector by a number (called a **scalar**) stretches or squishes its length, and can reverse its direction.
    *   Multiplying by `2` doubles the vector's length <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   Multiplying by `1/3` reduces its length to one-third <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   Multiplying by a negative number (e.g., `-1.8`) flips the vector's direction and then scales its length <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   This process is known as **scaling** <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Numerical Definition**: To multiply a vector by a scalar, multiply each of its components by that scalar <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. For example, if vector V = [1, 2], then 2V = [2*1, 2*2] = [2, 4] <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## The Utility of Linear Algebra
The power of linear algebra lies in the ability to translate back and forth between the geometric (arrows in space) and numerical (lists of numbers) views of vectors <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   For a [[applications_of_vectors_in_data_analysis_and_computer_graphics | data analyst]], it provides a visual way to conceptualize large lists of numbers, clarifying patterns in data and showing the global effect of operations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   For physicists and [[applications_of_vectors_in_data_analysis_and_computer_graphics | computer graphics]] programmers, it offers a numerical language to describe space and its manipulation <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. For example, creating animations involves thinking about spatial transformations and then representing them numerically for computer processing <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

These vector basics, especially vector addition and scalar multiplication, are central to all concepts in linear algebra <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Upcoming topics will delve into concepts like span, bases, and linear dependence <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.