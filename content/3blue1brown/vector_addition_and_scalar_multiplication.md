---
title: Vector addition and scalar multiplication
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 

The vector is the fundamental building block of linear algebra <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. While there are different perspectives on what a vector is (physics student, computer science student, mathematician) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, in linear algebra, vectors are often conceptualized as arrows rooted at the origin of a coordinate system <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. Every vector can be uniquely represented by a list of numbers, known as its coordinates <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

Two fundamental operations in linear algebra that revolve around vectors are vector addition and scalar multiplication <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

## Vector Addition

### Geometric Definition
To add two vectors geometrically, position the tail of the second vector at the tip of the first vector <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. The sum is then a new vector drawn from the tail of the first vector to the tip of the second vector <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. This method is the only time in linear algebra that vectors are typically allowed to move away from the origin <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

This definition is sensible because each vector can be thought of as a movement with a certain distance and direction in space <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Performing one movement followed by another results in an overall displacement that is equivalent to moving along the sum of the two vectors <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.

### Numerical Definition
When adding vectors numerically, you add their corresponding components. For example, if vector `v1` has coordinates `[x1, y1]` and vector `v2` has coordinates `[x2, y2]`, their sum `v1 + v2` will have coordinates `[x1 + x2, y1 + y2]` <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>. This component-wise addition aligns with the geometric "tip-to-tail" method <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

## Scalar Multiplication

### Geometric Definition
Multiplying a vector by a number, or "scalar," involves scaling the vector.
*   **Stretching**: Multiplying a vector by a number greater than 1 (e.g., 2) stretches the vector, making it longer by that factor <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
*   **Squishing**: Multiplying by a number between 0 and 1 (e.g., 1/3) squishes the vector, making it shorter <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.
*   **Reversing Direction**: Multiplying by a negative number (e.g., -1.8) first flips the vector's direction, then stretches it by the absolute value of that factor <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

The process of stretching, squishing, or reversing a vector is called **scaling** <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. The number used for this operation is called a [[vector_coordinates_and_scalar_implications | scalar]] <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. In linear algebra, the terms "scalar" and "number" are often used interchangeably <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.

### Numerical Definition
Numerically, multiplying a vector by a scalar means multiplying each of its components by that scalar <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. For instance, if vector `v` has coordinates `[x, y]`, then `2v` would have coordinates `[2x, 2y]` <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>.

## Significance in Linear Algebra
Vector addition and scalar multiplication are central to all topics in linear algebra <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>. The power of linear algebra lies in its ability to translate between the geometric perspective (arrows in space) and the numerical perspective (lists of numbers) <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>. This translation allows data analysts to visualize patterns in data and understand operations on lists of numbers <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>, while enabling fields like physics and computer graphics to describe spatial manipulations numerically <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.