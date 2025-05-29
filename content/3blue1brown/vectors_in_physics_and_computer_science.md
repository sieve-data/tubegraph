---
title: Vectors in physics and computer science
videoId: fNk_zzaMoSs
---

From: [[3blue1brown]] <br/> 

The fundamental building block of linear algebra is the [[definition_and_nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. To fully grasp what a [[definition_and_nature_of_vectors | vector]] is, it's helpful to consider three distinct, yet related, perspectives <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>:

*   The physics student perspective <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   The computer science student perspective <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   The mathematician's perspective <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

## Physics Student Perspective

From a physics student's point of view, [[understanding_vectors | vectors]] are conceptualized as arrows pointing in space <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A [[definition_and_nature_of_vectors | vector]] is defined by its length and the direction it points <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. As long as these two properties remain the same, the [[definition_and_nature_of_vectors | vector]] can be moved around in space and still be considered the same [[definition_and_nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

*   [[understanding_vectors | Vectors]] in a flat plane are two-dimensional <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   [[understanding_vectors | Vectors]] in broader space (like the one humans inhabit) are three-dimensional <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Computer Science Student Perspective

For a computer science student, [[understanding_vectors | vectors]] are seen as ordered lists of numbers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For instance, in data analytics concerning house prices, where features might include square footage and price, each house could be modeled as a pair of numbers <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The first number could represent square footage, and the second, price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

In this context, the order of numbers in the list matters <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Houses would be modeled as two-dimensional [[understanding_vectors | vectors]], where "[[definition_and_nature_of_vectors | vector]]" is essentially a synonym for "list," and its two-dimensionality is determined by the list's length of two <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Mathematician's Perspective

The mathematician's view aims to generalize both the physics and computer science perspectives <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. From this abstract viewpoint, a [[definition_and_nature_of_vectors | vector]] is defined as anything for which there's a sensible way to perform two operations: adding two [[definition_and_nature_of_vectors | vectors]] and multiplying a [[definition_and_nature_of_vectors | vector]] by a number (scalar) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. While this view is more abstract, it highlights the importance of [[dot_products_and_vectors | vector addition]] and scalar multiplication throughout [[applications_of_linear_algebra_in_data_analysis_and_computer_graphics | linear algebra]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Core Conceptualization for Linear Algebra

For a geometric focus, it's helpful to primarily think of a [[definition_and_nature_of_vectors | vector]] as an arrow rooted at the origin within a coordinate system <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This differs slightly from the physics perspective, where [[understanding_vectors | vectors]] can float freely <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. In [[applications_of_linear_algebra_in_data_analysis_and_computer_graphics | linear algebra]], [[understanding_vectors | vectors]] are almost always rooted at the origin <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Concepts are first understood geometrically, then translated to the "list of numbers" perspective by considering the [[vector_representation_and_coordinate_systems | coordinates]] of the [[definition_and_nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Coordinate Systems and Vector Representation

Coordinate systems provide the bridge between the geometric and numerical views of [[understanding_vectors | vectors]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

#### Two Dimensions

In two dimensions:
*   A horizontal x-axis and a vertical y-axis intersect at the origin <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. The origin is considered the center of space and the root for all [[understanding_vectors | vectors]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   Tick marks on each axis represent arbitrary unit lengths <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   The [[vector_representation_and_coordinate_systems | coordinates]] of a [[definition_and_nature_of_vectors | vector]] are a pair of numbers that provide instructions to get from the origin (tail) to the tip of the [[definition_and_nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   The first number indicates horizontal movement along the x-axis (positive for right, negative for left) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   The second number indicates vertical movement parallel to the y-axis (positive for up, negative for down) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   Conventionally, this pair of numbers is written vertically with square brackets to distinguish [[understanding_vectors | vectors]] from points <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Every pair of numbers corresponds to one unique [[definition_and_nature_of_vectors | vector]], and vice-versa <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

#### Three Dimensions

In three dimensions:
*   A third axis, the z-axis, is added, perpendicular to both the x and y-axes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   Each [[definition_and_nature_of_vectors | vector]] is associated with an ordered triplet of numbers <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   The first number indicates movement along the x-axis <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   The second number indicates movement parallel to the y-axis <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   The third number indicates movement parallel to the z-axis <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Every triplet of numbers corresponds to one unique [[definition_and_nature_of_vectors | vector]] in space, and vice-versa <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Fundamental Vector Operations

Most topics in [[applications_of_linear_algebra_in_data_analysis_and_computer_graphics | linear algebra]] revolve around two fundamental operations: [[dot_products_and_vectors | vector addition]] and scalar multiplication <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Vector Addition

*   **Geometric Definition:** To add two [[understanding_vectors | vectors]], move the second [[definition_and_nature_of_vectors | vector]] so its tail sits at the tip of the first <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. The sum is a new [[definition_and_nature_of_vectors | vector]] drawn from the tail of the first to the tip of the second <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This "tip-to-tail" method is one of the few times [[understanding_vectors | vectors]] are allowed to stray from the origin in [[applications_of_linear_algebra_in_data_analysis_and_computer_graphics | linear algebra]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This can be conceptualized as combining movements in space <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Numerical Definition:** When [[understanding_vectors | vectors]] are represented as lists of numbers, [[dot_products_and_vectors | vector addition]] involves adding the corresponding components of each [[definition_and_nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, if vector `v` is `[1, 2]` and vector `w` is `[3, -1]`, their sum `v + w` is `[1+3, 2+(-1)] = [4, 1]` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Scalar Multiplication

*   **Geometric Definition:** Multiplying a [[definition_and_nature_of_vectors | vector]] by a number (called a scalar) scales its length and can reverse its direction <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   Multiplying by a positive scalar greater than 1 stretches the [[definition_and_nature_of_vectors | vector]] (e.g., multiplying by 2 makes it twice as long) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   Multiplying by a positive scalar between 0 and 1 squishes the [[definition_and_nature_of_vectors | vector]] (e.g., multiplying by 1/3 makes it one-third the original length) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   Multiplying by a negative scalar flips the [[definition_and_nature_of_vectors | vector]]'s direction and then scales its length by the absolute value of the scalar (e.g., multiplying by -1.8 flips it and stretches it by a factor of 1.8) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Numerical Definition:** Numerically, scaling a [[definition_and_nature_of_vectors | vector]] by a scalar involves multiplying each of its components by that scalar <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. For example, if vector `v` is `[1, 2]`, then `2v` is `[2*1, 2*2] = [2, 4]` <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## The Utility of Bridging Perspectives

The power of [[applications_of_linear_algebra_in_data_analysis and computer graphics | linear algebra]] comes from the ability to translate back and forth between the geometric (arrows in space) and numerical (lists of numbers) views of [[understanding_vectors | vectors]] <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

*   For data analysts, it offers a visual way to conceptualize lists of numbers, clarifying patterns in data and providing a global view of operations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   For physicists and computer graphics programmers, it provides a numerical language to describe and manipulate space, which can be processed by computers <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. For instance, creating mathematical animations often involves first conceptualizing spatial movements and then using [[applications_of_linear_algebra_in_data_analysis_and_computer_graphics | linear algebra]] to numerically represent them for pixel placement <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.