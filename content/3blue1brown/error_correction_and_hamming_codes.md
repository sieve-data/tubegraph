---
title: Error correction and Hamming codes
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

The problem of reliable data transmission and storage in the face of inevitable errors is a fundamental challenge in computer science and [[concepts_in_information_theory_and_coding_theory|information theory]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Just as the real world's "messiness" can cause bits to flip when computers send or store data, leading to corrupted information <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>, a similar concept can be explored through a classic mathematical puzzle involving a chessboard and coins.

## The Chessboard Puzzle

This puzzle features a 64-square chessboard, with a coin on each square, facing either heads or tails <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. A key is hidden in a secret compartment beneath one of the squares <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. The goal is for two prisoners, who can strategize beforehand but won't know the initial coin arrangement or key location, to deduce where the key is <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

The first prisoner (you) is shown the board and the key's location, and is allowed to flip one and only one coin before leaving the room <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The second prisoner then enters, sees the final coin arrangement, and must correctly identify the key's location to win freedom for both <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The warden is adversarial and will try to thwart any strategy <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Solving this puzzle leads to insights into [[error_correction]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Error Correction Explained

[[Error correcting codes]] are a method to add a minimal amount of information to a message, enabling the receiver to not only detect an error but also precisely correct it <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The fundamental intuition behind solving the chessboard puzzle is essentially the same as that behind [[Hamming codes]] <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, which are notable as one of the earliest examples of highly efficient [[error_correction]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Visualizing Strategies with High-Dimensional Cubes

To analyze strategies for the chessboard puzzle, it's helpful to translate the problem into a geometric framework:
1.  **Binary Representation**: Think of heads and tails as ones and zeros <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
2.  **Coordinates**: A set of coins (bits) can be seen as a set of coordinates <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
3.  **High-Dimensional Cube**: Each possible state of the coin board (e.g., 64 squares means a 64-bit string) corresponds to a corner (vertex) of a high-dimensional unit cube <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
4.  **Coin Flips as Edges**: Flipping a single coin means moving along an edge of the cube, changing only one coordinate <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

For a three-square (3-coin) board, there are 2^3 = 8 possible states, corresponding to the 8 corners of a 3-dimensional cube <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Coloring the Cube

A strategy for the puzzle can be visualized as "coloring" each vertex of the cube (each coin arrangement) with a color representing the key's deduced location <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. For instance, with three possible key locations, the corners might be colored red, green, or blue <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

For a strategy to work, no matter the starting coin arrangement, the first prisoner must be able to flip one coin (move along one edge) to reach a state that communicates the correct key location. This means that from any given vertex (initial coin state), its neighbors (states reachable by one flip) must collectively represent all possible key locations <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. If a corner has two neighbors of the same color, it means there's no way to communicate one of the key locations from that starting state <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. An adversarial warden could exploit this by setting that initial configuration and placing the key in the color that cannot be reached <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Proof of Impossibility for Non-Power-of-Two Dimensions

The geometric visualization leads to a profound conclusion: a solution to this puzzle cannot exist if the number of squares (n) is not a power of two <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

Consider a general n-dimensional cube (representing n squares). Each vertex has 'n' distinct neighbors <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>, and there are 2^n total vertices <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. For a successful strategy, every vertex must have one neighbor of each of the 'n' possible "key location" colors.

Let's imagine counting how many times each corner has a "red" neighbor. If the property holds, this sum should be 2^n (one for each vertex) <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. However, each red corner itself is counted 'n' times (once for each of its 'n' neighbors) <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. Therefore, 2^n must equal 'n' times the total number of red corners <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

For this equation to hold with an integer number of red corners, 'n' must be a divisor of 2^n. This implies that 'n' itself must be a power of two <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

For example, with a 3-square board (n=3), there are 8 corners. If a solution existed, there would need to be 8/3 red corners, 8/3 green corners, and 8/3 blue corners, which is impossible <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This proves that for n=3, no strategy can work <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

This means that even if a board is "simplified" by having fewer squares (e.g., 3 instead of 64), if the number of squares is not a power of two, the task becomes impossible <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Conversely, if 'n' *is* a power of two (like 4 or 64), the argument doesn't rule out a solution, implying it might be possible <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

The solution to the original 64-square puzzle, therefore, can be seen as a particularly symmetric way to color the corners of a high-dimensional cube, a feat disallowed in most dimensions <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. The connection between binary strings and high-dimensional cubes, where bit flips correspond to edges, is a common concept in [[coding theory]] <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a> and helps in understanding [[basics_of_error_correction_schemes | error correction schemes]].

For an explicit demonstration of the solution and further discussion on its connection to [[Hamming codes]] and the [[practical_implementation_of_error_correction_algorithms | practical implementation of error correction algorithms]] or [[error_correction_in_digital_data_storage | error correction in digital data storage]], further exploration is encouraged <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. The [[history_and_significance_of_hamming_codes | history and significance of Hamming codes]] highlights their early efficiency in this field.