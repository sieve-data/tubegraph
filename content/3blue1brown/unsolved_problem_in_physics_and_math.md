---
title: Unsolved problem in physics and math
videoId: 6dTyOl1fmDo
---

From: [[3blue1brown]] <br/> 

The phenomenon where two colliding blocks can compute the digits of pi is, surprisingly, a technically [[Unsolved problem in physics and math | unsolved problem]] in mathematics <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. While the block collision process itself can be understood and calculated precisely <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>, the rigorous proof for its connection to pi remains elusive <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.

## The Colliding Blocks Puzzle

The puzzle involves two blocks on a frictionless plane with a wall on the left <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The left block is initially stationary and smaller (e.g., 1 kilogram), while the right block approaches with some speed <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The goal is to determine the total number of collisions between the blocks and with the wall <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

- For a mass ratio of 1:1, there are 3 collisions <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
- For a mass ratio of 100:1, there are 31 collisions <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
- For a mass ratio of 10,000:1, there are 314 collisions <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
- For a mass ratio of 1,000,000:1, there are 3,141 collisions <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The pattern reveals that as the mass ratio grows by powers of 100, the total number of collisions consistently displays the digits of pi <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### Idealized Physics Assumptions

To achieve this result, the puzzle relies on several [[idealized_physics_in_theoretical_simulations | idealizing assumptions]]:
- **Perfectly Elastic Collisions**: No energy is lost during collisions <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
- **Frictionless Plane**: Blocks move without resistance <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
- **Supermassive Wall**: The wall is assumed to be infinitely massive or fixed, so it doesn't move or absorb significant momentum <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
- **Classical Physics**: Relativistic effects are ignored, despite high velocities at large mass ratios <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Translation to Geometry

The solution involves translating the physics problem into a [[mathematical_exercises_and_problemsolving_in_geometry | pure geometry question]] by using [[vectors_in_physics_and_computer_science | a state space]] <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>, <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

### Conservation Laws and State Space
The core of the problem lies in the [[differential_equations_in_physics | conservation of energy]] and [[differential_equations_in_physics | momentum]] <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. By defining new coordinates (`x = sqrt(m1)*v1` and `y = sqrt(m2)*v2`), the conservation of energy equation transforms into `x^2 + y^2 = constant`, which is the equation for a circle <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

In this circular state space:
- Collisions between blocks correspond to moving along a diagonal line (representing conserved momentum) to another point on the circle <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. The slope of this line is related to the negative square root of the mass ratio <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
- Collisions with the wall correspond to reflecting the y-coordinate across the x-axis, moving straight up or down the circle <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

The process of collisions translates into a sequence of "zigs and zags" around the circle <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. Each "zig" (block-block collision) and "zag" (block-wall collision) corresponds to traversing an arc of `2*theta` radians on the circle, where `theta` is related to the slope of the momentum lines <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. The total number of lines drawn (and thus collisions) is the largest integer `N` such that `N * theta` is less than pi <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

## The Unsolved Aspect: Small Angle Approximations

The reason for the "unsolved" status stems from the reliance on the [[small_angle_approximation | small angle approximation]] <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
The key relationship is `tan(theta) = sqrt(m2/m1)` <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. This means `theta = arctan(sqrt(m2/m1))` <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.
For large mass ratios (e.g., 100:1), `sqrt(m2/m1)` becomes a small number (e.g., 0.1) <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

The [[small_angle_approximation | small angle approximation]] states that for small angles, `arctan(x)` is approximately `x` <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. This means `theta` is approximately `sqrt(m2/m1)`, which for mass ratios like 100:1, 10000:1, etc., results in `theta` being approximately 0.1, 0.01, etc., respectively <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.

When `theta` is a small power of 10 (or very close to it), the division of pi by `theta` yields a number whose digits are those of pi <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

However, the approximation `arctan(x) ≈ x` has an error term, specifically on the order of `x^3` (from Taylor's approximation) <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. While this error is very small for small angles (e.g., 1 millionth for `theta = 0.01`) <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>, it could theoretically lead to an "off-by-one" error in the final integer count if pi's digits exhibit a specific pattern (e.g., a long string of nines) that causes the approximation to cross an integer boundary <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

> "If at any point when you're looking at all the digits of pi, and you consider the first n of those digits, if it ever happens that the next n digits are all nines, then you get this off by one error." <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>

While this scenario seems "absurdly unlikely" given the number of known digits of pi <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>, rigorously proving that it *never* happens is beyond current mathematical capabilities <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>. Thus, the exact connection between these block collisions and the digits of pi remains technically an [[Unsolved problem in physics and math | unsolved problem]] <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.

## Significance of Idealization in Problem Solving

The "messiness" of the real world is often stripped away in physics and mathematics for several reasons:
1.  **Simplification**: Starting with the simplest variant of a problem provides a first approximation of reality, which can then be incrementally modified to account for real-world complexities <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>. For example, energy loss in collisions could be modeled by a shrinking circle in the state space <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
2.  **Exposing Hidden Connections**: Purity and idealization can reveal surprising analogies and deep mathematical structures that are obscured by real-world complexities <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>. This puzzle itself demonstrates a connection between classical mechanics and a fundamental mathematical constant (pi) <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>, and even a secret link to [[TarskiPlanck problem solving | quantum computing]] (specifically, Grover's Algorithm for Search) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Such connections are crucial for making progress in mathematics, as they allow insights from one domain to illuminate problems in another <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.