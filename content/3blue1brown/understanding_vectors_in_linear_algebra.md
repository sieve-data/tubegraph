---
title: Understanding vectors in linear algebra
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 

The fundamental building block for [[Linear algebra foundations | linear algebra]] is the vector <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It is crucial to understand what a vector is to grasp broader concepts in [[Linear algebra foundations | linear algebra]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Perspectives on Vectors

There are three distinct but related ideas about vectors <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>:

### Physics Student Perspective
For a physics student, vectors are arrows pointing in space <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A vector is defined by its length and direction <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. As long as these two properties remain the same, a vector can be moved around and still be considered the same vector <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Vectors in a flat plane are two-dimensional, while those in three-dimensional space are three-dimensional <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Computer Science Student Perspective
From a computer science viewpoint, vectors are ordered lists of numbers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, if analyzing house prices based on square footage and price, each house could be modeled as a pair of numbers where the order matters <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. In this context, "vector" is a term for a list, and its dimensionality is determined by the length of that list <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Mathematician's Perspective
Mathematicians generalize both views, defining a vector as anything for which there's a sensible notion of adding two vectors and multiplying a vector by a number <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This perspective is more [[abstract_vector_spaces | abstract]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, but it highlights the importance of vector addition and scalar multiplication in [[Linear algebra foundations | linear algebra]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Preferred Perspective in Linear Algebra
For a geometric understanding of [[Linear algebra foundations | linear algebra]], it is helpful to think of a vector as an arrow <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Specifically, visualize this arrow inside a [[coordinate_systems_in_linear_algebra | coordinate system]], such as the XY-plane, with its tail rooted at the origin <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This differs from the physics view, where vectors can freely sit anywhere <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>; in [[Linear algebra foundations | linear algebra]], vectors are almost always rooted at the origin <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Once a concept is understood geometrically, it can be translated to the list of numbers perspective by considering the vector's coordinates <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This back-and-forth translation is crucial in [[Linear algebra foundations | linear algebra]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Coordinate Systems
*   **Two Dimensions**: A [[coordinate_systems_in_linear_algebra | coordinate system]] in 2D consists of a horizontal x-axis and a vertical y-axis <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Their intersection is the origin, which acts as the center of space and the root for all vectors <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
    *   Tick marks on each axis represent arbitrary units <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    *   The coordinates of a vector are a pair of numbers providing instructions to get from the origin (tail) to the vector's tip <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The first number indicates horizontal movement (right for positive, left for negative), and the second indicates vertical movement (up for positive, down for negative) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   Vectors are conventionally written vertically with square brackets <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   Each pair of numbers corresponds to one unique vector, and each vector corresponds to one unique pair of numbers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Three Dimensions**: A third axis, the z-axis, is added perpendicular to both x and y-axes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. In 3D, each vector is associated with an ordered triplet of numbers <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. The numbers indicate movement along the x-axis, parallel to the y-axis, and parallel to the z-axis, respectively <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Similar to 2D, there's a unique mapping between triplets and vectors in 3D space <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Fundamental Vector Operations
Every topic in [[Linear algebra foundations | linear algebra]] revolves around vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Vector Addition
*   **Geometric Definition**: To add two vectors, move the second vector so its tail sits at the tip of the first one <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. The sum is a new vector drawn from the tail of the first to the tip of the second <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This "tip-to-tail" method is almost the only time vectors are allowed to stray from the origin in [[Linear algebra foundations | linear algebra]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   This definition is intuitive because vectors represent movements: taking a step along the first vector and then along the second results in the same overall effect as moving directly along their sum <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Numerical Definition**: When vectors are represented as lists of numbers, vector addition is performed by matching up their corresponding terms and adding each one together <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, if vector 1 is [1, 2] and vector 2 is [3, -1], their sum is [1+3, 2+(-1)] = [4, 1] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Scalar Multiplication
*   **Geometric Definition**: Multiplying a vector by a number (a "scalar") scales its length and potentially its direction <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   Multiplying by 2 stretches the vector to be twice as long <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   Multiplying by 1/3 squishes it to one-third its original length <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   Multiplying by a negative number (e.g., -1.8) first flips the vector's direction, then stretches it by the absolute value of the scalar <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   This process is called "scaling" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The number used for scaling is called a "scalar," often used interchangeably with the word "number" in [[Linear algebra foundations | linear algebra]] <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Numerical Definition**: To multiply a vector by a scalar, multiply each of its components by that scalar <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## Interplay of Perspectives
While it doesn't matter whether one fundamentally thinks of vectors as arrows or lists of numbers, the usefulness of [[Linear algebra foundations | linear algebra]] lies in the ability to translate back and forth between these views <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

*   This translation provides data analysts with a visual way to conceptualize lists of numbers, clarifying patterns and providing a global view of operations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   Conversely, it gives physicists and computer graphics programmers a numerical language to describe space and its manipulation <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. For example, creating math animations often involves thinking about spatial changes and then numerically representing them for computer processing <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

The next steps in [[Linear algebra foundations | linear algebra]] will delve into concepts like span, bases, and linear dependence <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.