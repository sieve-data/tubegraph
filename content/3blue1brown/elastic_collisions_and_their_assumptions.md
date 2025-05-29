---
title: Elastic collisions and their assumptions
videoId: 6dTyOl1fmDo
---

From: [[3blue1brown]] <br/> 

In a 2019 video, a puzzle was presented demonstrating how [[colliding_blocks_and_pi_computation | two colliding blocks can compute pi]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The setup involves two blocks on a frictionless plane, with one block initially stationary and the other approaching it at a certain speed <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The objective is to determine the total number of collisions between the blocks and with a wall to their left <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

To achieve the "delightful result" of the number of collisions relating to pi, several idealizing assumptions must be made <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>:

## Assumptions for Idealized Collisions

1.  **Perfectly [[elastic_collisions_in_physics | Elastic Collisions]]**: It is assumed that no energy is lost during the collisions <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Physicists refer to these as perfectly [[elastic_collisions_in_physics | elastic collisions]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This implies that no sound would be produced, a detail which is consciously ignored in the video for artistic and communicative purposes to highlight the density of collisions <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  **Negligible Relativistic Effects**: For very large mass ratios (e.g., a million to one), the smaller block would move at speeds that, in a physically accurate analysis, would require considering relativistic effects. These effects are ignored to simplify the puzzle <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  **Idealized Classical Physics**: The puzzle is treated as a "pure, overly idealized classical physics puzzle," disregarding many other practical realities that would otherwise cause the system to break down completely <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
4.  **Immovable Wall**: When the smaller block collides with the wall, it transfers some of its momentum to the wall <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. It is assumed that the wall is "supermassive or fixed into the earth," rendering any movement it might experience negligible <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## Conservation Laws

Central to the puzzle's solution are two fundamental [[conservation_laws_in_classical_physics | conservation laws in classical physics]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>:

*   **[[conservation_laws_in_classical_physics | Conservation of Energy]]**: The total kinetic energy of the two blocks (½m₁v₁² + ½m₂v₂²) remains constant throughout the experiment, provided no energy is lost to friction or collisions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>, <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **[[conservation_laws_in_classical_physics | Conservation of Momentum]]**: The total momentum of the two blocks (m₁v₁ + m₂v₂) also remains constant, even after the blocks collide with each other <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

By applying these assumptions and laws, the physics problem can be translated into a geometry problem involving a point moving around a circle in an abstract "state space" representing the velocities of the blocks <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. While these assumptions simplify the problem, they allow for the discovery of hidden connections, such as the relationship between [[colliding_blocks_and_pi_computation | colliding blocks and pi computation]] or even [[Grover's Algorithm for Search]] in quantum computing <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.