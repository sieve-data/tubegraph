---
title: Vector addition and scalar multiplication
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 
The fundamental building block for linear algebra is the [[understanding_vectors_in_linear_algebra|vector]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. While there are different perspectives on what a vector is, in the context of linear algebra, it's often best to think of it as an arrow rooted at the origin of a coordinate system <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The coordinates of a vector provide instructions on how to get from its tail at the origin to its tip <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. For example, in two dimensions, a vector's coordinates tell you how far to move along the x-axis and then parallel to the y-axis <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. In three dimensions, a third coordinate specifies movement along the z-axis <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Every pair (or triplet) of numbers uniquely defines a vector, and vice versa <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

Vector addition and scalar multiplication are the two fundamental operations around which all topics in linear algebra revolve <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Vector Addition

### Geometric Definition
To add two vectors, conceptually move the second vector so that its tail sits at the tip of the first one <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. The sum is a new vector drawn from the tail of the first to the tip of the second <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This is typically the only time in linear algebra where vectors are allowed to stray from the origin <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

This definition is intuitive if you consider vectors as representing movements: taking a step along the first vector, then a step along the second, results in the same overall displacement as moving along their sum <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Numerical Definition
Numerically, vector addition is performed by adding the corresponding components of each vector <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. For example, if vector A has coordinates (1, 2) and vector B has coordinates (3, -1), their sum will have coordinates (1+3, 2-1) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Scalar Multiplication

### Geometric Definition
Multiplying a vector by a number (called a scalar) scales its length <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   Multiplying by a number greater than 1 stretches the vector, making it longer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   Multiplying by a number between 0 and 1 squishes it, making it shorter <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   Multiplying by a negative number flips the vector's direction before stretching or squishing it <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

The term "scalar" is used interchangeably with "number" in linear algebra, as scaling vectors is one of the main functions of numbers in this context <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Numerical Definition
Numerically, multiplying a vector by a scalar means multiplying each of its components by that scalar <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. For instance, multiplying a vector with coordinates (1, 2) by 2 results in a new vector with coordinates (2*1, 2*2) <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## Significance in Linear Algebra
The ability to translate between the geometric (arrows in space) and numerical (lists of numbers) views of vectors, along with understanding these fundamental operations, is key to the usefulness of linear algebra <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. This translation allows data analysts to visualize patterns in data and gives programmers a numerical language to describe and manipulate space <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.