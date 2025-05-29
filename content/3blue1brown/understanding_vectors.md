---
title: Understanding vectors
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 

The fundamental building block for linear algebra is the [[definition_and_nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. To fully grasp linear algebra, it's essential to understand what a [[definition_and_nature_of_vectors | vector]] is <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Broadly speaking, there are three distinct but related perspectives on [[definition_and_nature_of_vectors | vectors]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>: the physics student perspective, the computer science student perspective, and the mathematician's perspective <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Perspectives on Vectors

### Physics Student Perspective
From a physics student's viewpoint, [[vectors_in_physics_and_computer_science | vectors]] are arrows pointing in space <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A [[definition_and_nature_of_vectors | vector]] is defined by its length and direction <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. As long as these two properties remain the same, the [[definition_and_nature_of_vectors | vector]] can be moved anywhere in space and still be considered the same [[definition_and_nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. [[definition_and_nature_of_vectors | Vectors]] can be two-dimensional (living in a flat plane) or three-dimensional (in broader space) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Computer Science Student Perspective
The computer science perspective views [[vectors_in_physics_and_computer_science | vectors]] as ordered lists of numbers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, in analyzing house prices, a house could be modeled as a pair of numbers, with the first representing square footage and the second representing price <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The order of these numbers matters <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. In this context, "[[definition_and_nature_of_vectors | vector]]" is a term for a list, and its "dimensionality" is determined by the length of that list <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Mathematician's Perspective
Mathematicians generalize these views, defining a [[definition_and_nature_of_vectors | vector]] as anything for which there is a sensible way to add two [[definition_and_nature_of_vectors | vectors]] and multiply a [[definition_and_nature_of_vectors | vector]] by a number <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This abstract view highlights the importance of [[definition_and_nature_of_vectors | vector]] addition and multiplication by numbers throughout linear algebra <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. While abstract, it underscores the centrality of these operations <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Geometric Focus in Linear Algebra
For a geometric understanding of [[definition_and_nature_of_vectors | vectors]], especially in linear algebra, it's helpful to primarily think of them as arrows within a coordinate system <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Crucially, these arrows should be imagined with their tail sitting at the origin <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This differs from the physics perspective, where [[definition_and_nature_of_vectors | vectors]] can be freely moved <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>; in linear algebra, [[definition_and_nature_of_vectors | vectors]] are almost always rooted at the origin <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Once a concept is understood geometrically with arrows, it can be translated to the list of numbers perspective by considering the [[definition_and_nature_of_vectors | vector]]'s coordinates <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This back-and-forth translation is crucial for understanding linear algebra <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Coordinate Systems
*   **Two Dimensions (2D)**: In two dimensions, there is a horizontal x-axis and a vertical y-axis <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Their intersection is the origin, considered the center of space and the root of all [[definition_and_nature_of_vectors | vectors]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Tick marks on each axis represent chosen unit lengths <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Coordinates**: The coordinates of a [[definition_and_nature_of_vectors | vector]] are a pair of numbers that instruct how to get from its tail (at the origin) to its tip <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   The first number indicates movement along the x-axis (positive for right, negative for left) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   The second number indicates movement parallel to the y-axis (positive for up, negative for down) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Notation**: To distinguish [[definition_and_nature_of_vectors | vectors]] from points, coordinates are conventionally written vertically with square brackets <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Each pair of numbers uniquely defines a [[definition_and_nature_of_vectors | vector]], and each [[definition_and_nature_of_vectors | vector]] corresponds to a unique pair of numbers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Three Dimensions (3D)**: In three dimensions, a third z-axis is added, perpendicular to both the x and y-axes <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Each [[definition_and_nature_of_vectors | vector]] is then associated with an ordered triplet of numbers <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, representing movement along x, then parallel to y, then parallel to z <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Every triplet uniquely defines a [[definition_and_nature_of_vectors | vector]], and vice-versa <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Fundamental Vector Operations
Every topic in linear algebra revolves around two fundamental [[definition_and_nature_of_vectors | vector]] operations: [[definition_and_nature_of_vectors | vector]] addition and multiplication by a number (scalar multiplication) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Vector Addition
*   **Geometric Definition**: To add two [[definition_and_nature_of_vectors | vectors]], move the second [[definition_and_nature_of_vectors | vector]] so its tail sits at the tip of the first <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. The sum is a new [[definition_and_nature_of_vectors | vector]] drawn from the tail of the first to the tip of the second <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This "tip-to-tail" method is one of the few times [[definition_and_nature_of_vectors | vectors]] are allowed to stray from the origin in linear algebra <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Interpretation**: Each [[definition_and_nature_of_vectors | vector]] represents a movement <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Adding [[definition_and_nature_of_vectors | vectors]] is like taking consecutive steps; the sum represents the overall effect <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Numerical Definition**: Numerically, [[definition_and_nature_of_vectors | vector]] addition is performed by matching up the corresponding terms (components) of the [[definition_and_nature_of_vectors | vectors]] and adding them together <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, if vector A = [1, 2] and vector B = [3, -1], their sum is [1+3, 2+(-1)] = [4, 1] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Scalar Multiplication
*   **Geometric Definition**: Multiplying a [[definition_and_nature_of_vectors | vector]] by a number (called a *scalar*) stretches or squishes its length <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. For example, multiplying by 2 makes the [[definition_and_nature_of_vectors | vector]] twice as long <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>; multiplying by one-third squishes it to one-third its original length <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. If the scalar is negative, the [[definition_and_nature_of_vectors | vector]] also reverses direction before being stretched <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This process is called **scaling** <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, and the number used for multiplication is called a **scalar** <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Numerical Definition**: Numerically, multiplying a [[definition_and_nature_of_vectors | vector]] by a scalar means multiplying each of its components by that scalar <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## The Power of Translation
The usefulness of linear algebra comes from its ability to translate between the geometric (arrows in space) and numerical (lists of numbers) views of [[definition_and_nature_of_vectors | vectors]] <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

*   For data analysts, it provides a visual way to conceptualize lists of numbers, clarifying patterns and providing a global view of operations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   For physicists and computer graphics programmers, it offers a language to describe space and its manipulation using numbers that computers can process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

For example, creating mathematical animations involves thinking geometrically about what's happening in space and then using linear algebra to numerically represent those actions for computer processing <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

Subsequent videos will delve into concepts such as [[span_of_vectors_in_different_dimensions | span]], bases, and linear dependence <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.