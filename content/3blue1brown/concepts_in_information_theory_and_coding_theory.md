---
title: Concepts in information theory and coding theory
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

This article explores fundamental concepts in [[Information theory and entropy | information theory]] and [[Error correction and Hamming codes | error correction]], often illustrated through the lens of a classic chessboard puzzle. The puzzle serves as a practical, engaging model to understand how information is encoded, transmitted, and protected against errors.

## The Chessboard Puzzle: An Introduction
The puzzle involves a chessboard with 64 squares, each containing a coin set to either heads or tails in a pattern determined by a "math-obsessed warden" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. A key is hidden in one of these squares <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. One prisoner is shown the key's location and the coin pattern, and is allowed to flip exactly one coin before leaving <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A second prisoner then enters, and based solely on the coins' arrangement, must deduce the key's location <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Both prisoners can strategize beforehand <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

The solution to this puzzle provides intuition for understanding [[Error correction and Hamming codes | Hamming codes]], an early and efficient form of [[Error correction and Hamming codes | error correction]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Representing the Puzzle: Coins as Bits, Boards as Cubes
To analyze the puzzle, coins are best thought of as ones and zeros <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This allows for mathematical treatment and geometric representation.

### Simplest Case: Two Squares
Consider a simplified version with two squares, two coins, and two possible key locations <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Coordinates:** The state of the two coins (e.g., heads/tails or 0/1) can be represented as a pair of coordinates <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Geometric Representation:** Each of the four possible states (00, 01, 10, 11) sits at the corners of a unit square <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Flipping a coin moves you along an edge of this square, changing only one coordinate <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Solution Strategy:** A strategy might associate the bottom two corners (y-coordinate 0) with the key being in square zero, and the top two corners (y-coordinate 1) with the key in square one <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. The first prisoner must be able to move to a desired region (key location) by flipping one coin <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Generalization: Higher Dimensions
For a larger board with 'n' squares, the `2^n` possible coin arrangements correspond to the vertices of an 'n'-dimensional unit cube <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. Flipping a coin corresponds to moving along an edge of this hypercube <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Strategies as Colorings
A strategy for the puzzle is equivalent to "coloring" each vertex (coin arrangement) of the cube with a specific color, where each color represents a possible key location <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   For the 3-square case, with 8 possible coin states, a strategy is to color each of the 8 corners of a 3D cube either red, green, or blue (representing squares 0, 1, or 2) <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   The goal is that from any starting corner, flipping one coin allows the first prisoner to reach a corner of any desired color (representing the key's location) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. If a corner has two neighbors of the same color, it signifies a flaw in the strategy because the prisoner cannot reach all target colors <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

> [!INFO] Total Possible Strategies
> For the original 64-square puzzle, there are `64^(2^64)` total possible strategies <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## The Impossibility Proof: Why Certain Variations Fail
A fascinating insight arises from proving that certain variations of the puzzle are impossible to solve <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### The Counting Argument (for 3-squares)
For the 3-square case, the question becomes: can you color the 8 corners of a cube with 3 colors (red, green, blue) such that the three neighbors of any given vertex always represent red, green, and blue? <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>

This problem can be proven impossible using a counting argument:
1.  Imagine counting how many neighbors of each corner are red. If the desired property holds, each of the 8 corners must have exactly one red neighbor <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>, summing to a total of 8 "red neighbors" <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
2.  Conversely, every red corner is counted exactly three times (once for each of its three neighbors) <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
3.  Therefore, `3 * (number of red corners) = 8`. This implies the number of red corners must be `8/3`, which is impossible for an integer number of corners <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

### Generalization to N Dimensions
This argument generalizes to any 'n'-dimensional cube (n squares in the puzzle):
*   An 'n'-dimensional cube has `2^n` vertices <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   Each vertex has 'n' distinct neighbors <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   If a solution exists, and there are 'n' possible key locations (colors), then by the same counting argument: `n * (number of red corners) = 2^n` <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   For the number of red corners to be an integer, 'n' must be a power of two <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

### Implications for the Puzzle
This proof demonstrates that the chessboard puzzle cannot be solved if the number of squares ('n') is not a power of two <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   For example, a 6x6 chessboard (36 squares) would be impossible to solve, even though it seems simpler than a 64-square board <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   The original 64-square puzzle (`n=64`, which is `2^6`) *is* a power of two, meaning a solution is not ruled out by this argument <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

> [!NOTE] Higher Dimensional Visualization
> While visualizing high-dimensional cubes is difficult, the concept of their vertices (bitstrings) and edges (bit flips) is crucial in fields like [[Error correction and Hamming codes | coding theory]] <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Connection to Error Correction
The intuition behind solving the chessboard puzzle is deeply connected to [[Error correction and Hamming codes | error correction]].

### What is Error Correction?
When computers send or store data, errors (like a bit flip) can occur due to real-world "messiness" <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. [[Error correction and Hamming codes | Error correcting codes]] add a small amount of extra information to a message, allowing the receiver to not only detect an error but also precisely identify and fix it <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Hamming Codes and the Puzzle's Intuition
The solution to the chessboard puzzle shares the same underlying intuition as [[Error correction and Hamming codes | Hamming codes]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. [[Error correction and Hamming codes | Hamming codes]] are notable for being one of the earliest examples of highly efficient [[Error correction and Hamming codes | error correction]] schemes <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This means that the problem-solving skills applied to the puzzle are directly applicable to understanding practical aspects of [[Information theory and entropy | information theory]] and computer science.

## Further Exploration
For an explicit solution to the 64-square chessboard puzzle, a collaboration with Matt Parker on Stand Up Maths explores the thought processes and multiple ways of approaching the problem <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. The connection between the puzzle and [[Error correction and Hamming codes | Hamming codes]] is also a topic of interest for future discussion <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.