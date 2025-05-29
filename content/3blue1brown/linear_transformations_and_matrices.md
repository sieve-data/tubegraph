---
title: Linear transformations and matrices
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

When analyzing the shadow of a cube, two distinct problem-solving styles emerge: one favoring detailed calculation (Bob) and another preferring a high-level, generalized overview (Alice) <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Alice's approach highlights the utility of [[linear_transformations]] and their [[matrix_representation_of_linear_transformations | matrix representation]] in solving complex geometry problems.

## Linear Transformations in Shadow Projection

Alice observes that both the rotation of a shape in 3D space and its subsequent flat projection into 2D space are [[linear_transformations]] <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This means that, in principle, each of these operations can be described by a [[matrix_representation_of_linear_transformations | matrix]] <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The combined effect of these transformations would then be represented by the product of their respective matrices <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

A key property of [[linear_transformations]] is their effect on area <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. If a shape's area is transformed by a [[linear_transformations | linear transformation]], the output area will be the original area multiplied by a constant factor <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. This constant is known as the determinant of the transformation <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Intuitively, this means that if you uniformly stretch the original shape in some direction, the output will also uniformly stretch in some direction, causing their areas to scale proportionally <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

For a fixed transformation (rotation plus flat projection), this proportionality constant between the original shape's area and its shadow's area does not depend on the original shape <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. It is solely determined by the transformation itself, which, in this context, depends on the specific rotation applied to the shape <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

## Distinguishing Linear from Non-Linear Projections

It's important to note that the proportionality between the shadow's area and the original shape's area holds true *because* the projection is linear <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. If the light source were closer to the object, the projection would not be linear <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. In such a non-linear scenario, uniformly stretching the original shape might lead to a disproportionate effect on the shadow, particularly if parts of the shape are much closer to the light source <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. Alice emphasizes that the linearity of the transformation is a crucial property for her generalizations <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

## Generalization to Convex Solids

Alice's method relies on the general principle that for any convex solid, the average area of its shadow will be proportional to its surface area <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Crucially, this proportionality constant is the same across all convex solids <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a> <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.

For any flat 2D object, the average shadow area will be equal to some universal proportionality constant multiplied by its own area <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>. This constant does not depend on the specific shape of the 2D object <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>.

> [!NOTE] Universal Proportionality Constant
> Alice's insight shows that the average shadow area of a convex solid is always 1/4th of its surface area <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>. This constant is derived from the sphere, where the shadow area (πr²) is exactly one-fourth of its surface area (4πr²) <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. This same proportionality then applies to any convex solid, including the cube <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.

This generalization, which is supported by concepts of limits and polyhedral approximations of a sphere, is a core strength of Alice's approach, allowing her to solve the problem for a cube without extensive computations specific to the cube's geometry <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>.