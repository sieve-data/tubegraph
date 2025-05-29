---
title: Higherdimensional cubes and coloring problems
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

The challenge of understanding and solving a classic prisoner puzzle involving a chessboard with coins naturally leads to the mathematical concepts of higher-dimensional cubes and related coloring problems <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This approach offers a powerful visual and combinatorial framework for analyzing the problem and its limits <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## The Chessboard Puzzle

The puzzle begins with a chessboard (64 squares), each having a coin on it, either heads or tails <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. A math-obsessed warden places a hidden key under one of the 64 squares <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The first prisoner (the "setter") knows the initial coin arrangement and the key's location <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Their only action is to flip exactly one coin <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The second prisoner (the "guesser") then enters, sees the updated coin arrangement, and must deduce the key's location to win freedom for both <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The prisoners can strategize beforehand, but the warden can choose an adversarial coin arrangement and key placement to thwart their plan <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

This puzzle is closely related to [[error_correction | error correction]] and [[hamming_codes | Hamming codes]] in computer science and information theory <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Visualizing States as Higher-Dimensional Cubes

To analyze the puzzle, the first step is to transform the coin states (heads/tails) into binary digits (ones/zeros) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. Each arrangement of coins can then be thought of as a set of coordinates, representing a unique state of the board <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### From 2D to 3D and Beyond

*   **Two squares, two coins:** These configurations can be viewed as the corners of a unit square in two-dimensional space <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Flipping a single coin corresponds to moving along an edge of this square <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Three squares, three coins:** With eight possible states (2^3), these configurations correspond to the corners of a unit cube in three-dimensional space <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Flipping a coin means "walking along the edge of a cube" <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

This concept extends to any number of squares. For *n* squares, there are 2^*n* possible coin arrangements, which represent the vertices of an *n*-dimensional hypercube <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Each vertex has *n* distinct neighbors, corresponding to the *n* possible single-coin flips <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

## Coloring the Cube: Representing Strategies

A strategy for the puzzle can be visualized as coloring each vertex of the hypercube <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Each color corresponds to a specific key location. For example, in the three-square case, if there are three possible key locations (squares zero, one, and two), the vertices of the 3D cube could be colored red, green, or blue <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

The goal of the puzzle (for the setter) is to manipulate the coins (move along an edge) so that the final state (the colored vertex) indicates the correct key location for the guesser <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This means that from any starting vertex, the setter must be able to reach a vertex of the desired color by flipping only one coin <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. In other words, every vertex on the hypercube must have neighbors of all possible colors (representing all possible key locations) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

The total number of possible strategies is enormous: for *k* possible key locations and a hypercube with *V* vertices, there are *k*^*V* total coloring strategies <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. For the original 64-square puzzle, this is 64^(2^64) possible strategies <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### Example of a Failed Strategy (3-square case)

Consider a strategy where the key location is encoded by the sum of the coin values (modulo 3) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. If we start at a particular vertex, say (0,1,0), and it's colored green <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>:
*   Flipping coin 0 (changing 0,1,0 to 1,1,0) might keep it green <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   Flipping coin 1 (changing 0,1,0 to 0,0,0) or coin 2 (changing 0,1,0 to 0,1,1) might take you to a red corner <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

If there's no way to reach a blue corner from the starting vertex (0,1,0) by flipping a single coin, then an adversarial warden could start with this configuration and place the key under the "blue" square, thus thwarting the strategy <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This failure is visually apparent as a corner in the colored cube that has two neighbors of the same color, meaning not all key locations are accessible via a single flip <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

## The Impossibility Proof: Non-Power-of-Two Dimensions

A fascinating insight emerges from this coloring perspective: a solution to the puzzle is only possible if the number of squares (or dimensions, *n*) is a power of two <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

The argument relies on a counting principle:
1.  Assume a successful coloring strategy exists for an *n*-dimensional hypercube, where there are *k* possible key locations (colors).
2.  For the strategy to work, every vertex must have neighbors representing all *k* colors <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. This means each vertex must have exactly one neighbor of each color, or *n* must be a multiple of *k*. For simplicity, assume *k* equals *n* (the number of possible key locations equals the number of dimensions/squares).
3.  Consider one specific color, say "red." The desired property states that every vertex on the cube must have exactly one red neighbor <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
4.  Sum the number of red neighbors for all vertices: If there are 2^*n* vertices in total, and each has one red neighbor, this sum is 2^*n* <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
5.  Alternatively, consider only the red vertices. Each red vertex has *n* neighbors <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. The total count of red neighbors (from step 4) must also equal *n* times the total number of red vertices <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
6.  Therefore, *n* multiplied by the number of red vertices must equal 2^*n* <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
7.  Since 2^*n* is a power of 2, it implies that *n* itself must also be a power of 2 for this equation to hold with an integer number of red vertices <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. For example, in 3 dimensions (3 squares, 3 key locations), this would require 8/3 red vertices, which is impossible <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

This proof demonstrates that if the number of squares (*n*) is not a power of two (e.g., 3 or 6), it is impossible to create a strategy that guarantees a win, regardless of how clever the approach <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. This shows that solutions are "almost impossible" in most dimensions <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Visualizing 4-Dimensional Coloring

While [[geometric_reasoning_in_higher_dimensions | visualizing higher dimensional cubes]] can be challenging, a 4-dimensional cube can be projected into 3D space, showing its vertices and edges <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. For a 4-square puzzle, since 4 is a power of 2, a solution is mathematically possible <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. Such a solution would involve coloring the 16 vertices of the 4D cube with 4 colors, such that each vertex has exactly one neighbor of each of the 4 colors <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.

<figure>
    <img src="https://i.imgur.com/example_4d_cube_coloring.png" alt="A projection of a 4D cube with its vertices colored to demonstrate a solution to the puzzle."/>
    <figcaption>A 4-dimensional cube with its corners painted in a symmetric way to satisfy the puzzle's requirements <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.</figcaption>
</figure>

This problem, especially for 64 squares (2^6), is a classic example of how abstract mathematical [[transformations_between_different_dimensions | transformations between different dimensions]] and [[geometric_reasoning_in_higher_dimensions | geometric reasoning in higher dimensions]] can unlock insights into seemingly unrelated problems <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.