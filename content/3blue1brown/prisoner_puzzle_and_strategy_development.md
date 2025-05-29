---
title: Prisoner puzzle and strategy development
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

The classic prisoner puzzle scenario often involves a math-obsessed warden offering freedom to inmates if they can solve an elaborate scheme <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. One such variant features a chessboard with coins and a hidden key <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## The Chessboard Key Puzzle

In this particular puzzle, a chessboard has 64 squares, each with a coin (either heads or tails) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The warden arranges the coins in any pattern they choose <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, then places a key inside a secret compartment under one of the squares <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

The first prisoner (you) knows where the key is <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The goal is to convey the key's location to a second prisoner <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The only action allowed is to turn over one, and only one, of the coins before leaving the room <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The second prisoner then enters, and with no other information besides the coin arrangement, must deduce the key's location to win freedom for both <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Players can strategize beforehand, but they won't know the specific initial coin layout <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The warden can also listen to their strategy and create an adversarial arrangement of coins and the key to thwart it <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Core Insights and Rabbit Holes

Solving this puzzle can lead to deeper mathematical explorations <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>:
*   **Proof of Impossibility:** Investigating why the challenge becomes impossible if the setup is slightly varied, such as using a 6x6 chessboard or removing a square <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This rabbit hole can lead to discussions about coloring corners of a 4-dimensional cube <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **[[relation_between_the_puzzle_and_error_correction | Connection to Error Correction]]:** The solution to this puzzle is closely linked to the intuition behind Hamming codes, an early example of efficient error correction <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Error correction is vital in computer science, allowing receivers to identify and fix data bit-flips caused by real-world "messiness" <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Geometric Visualization of Strategies

To understand possible strategies, it's helpful to visualize the puzzle geometrically <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### The Simplest Case: Two Squares

Consider a simplified version with two squares, two coins, and two possible key locations <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   Coins can be thought of as ones and zeros instead of heads and tails for easier mathematical manipulation <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   Pairs of coins represent a set of coordinates, where each of the four possible board states sits at the corners of a unit square <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   Flipping one coin moves you along an edge of this square, changing only one coordinate <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   A strategy, like letting the second coin encode the key's location (tails for left square, heads for right), means associating regions of the square with key locations <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. The goal is to ensure that by flipping one coin, you can always reach the desired region <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Expanding to Three Squares

For three squares, three coins, and three key locations, there are eight possible states for the coins <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Interpreting these states as coordinates leads to a three-dimensional space, with each state at the corner of a unit cube <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Flipping a coin corresponds to walking along an edge of this cube <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

A strategy involves associating each of the eight cube corners (coin states) with one of the three key locations (e.g., red for square zero, green for square one, blue for square two) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. So, creating a strategy is equivalent to coloring each of the cube's eight corners <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. The total number of possible strategies is immense: for three squares, it's 3<sup>8</sup> <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>; for the original 64-square puzzle, it's 64<sup>2<sup>64</sup></sup> <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

A successful strategy requires that from any given corner (initial coin state), by flipping one coin (moving along an edge), you can always reach a corner of the desired color (key location) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. If a corner has two neighbors of the same color, an adversarial warden could trap you, making it impossible to reach a specific key location <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### The Combinatorial Question

The core question becomes: can you paint the corners of the cube so that the three neighbors of any given vertex always represent red, green, and blue (or all possible key locations)? <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a> This problem resembles a three-dimensional Sudoku <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

Thinking about binary strings as vertices of a high-dimensional cube, where bit flips correspond to edges, is a common concept in coding theory and [[relation_between_the_puzzle_and_error_correction | error correction]] <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Coloring in mathematics often describes partitioning items into distinct sets <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

## Proof of Impossibility for Non-Power-of-Two Dimensions

An elegant argument demonstrates why this coloring is impossible in three dimensions, and more generally, in any dimension that is not a power of two <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

The argument relies on counting:
1.  Assume a valid coloring where every corner has exactly one neighbor of each color (e.g., one red, one green, one blue).
2.  If this property holds, then the total count of "red neighbors" across all corners should equal the total number of corners <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. In three dimensions, this means 8 (total corners).
3.  However, every red corner is counted exactly three times (once for each of its three neighbors) <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. Therefore, the total count of red neighbors must also be three times the total number of red corners.
4.  This leads to the conclusion that the number of red corners must be 8/3, which is not possible as corners must be whole numbers <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

This argument generalizes to 'n' squares (an n-dimensional cube) <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>:
*   There are 'n' distinct neighbors for each vertex <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   The total number of vertices is 2<sup>n</sup> <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   If a solution exists, the sum of "red neighbors" across all vertices must be 2<sup>n</sup>.
*   Also, this sum must equal 'n' times the total number of red corners <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   For these two sums to be equal (2<sup>n</sup> = n * number of red corners), 'n' must be a power of two <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

This proves that no possible strategy can work if the number of squares 'n' is not a power of two <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Thus, even seemingly simpler setups like a 6x6 board or one with a removed square (which changes 'n' to 35) become hopeless <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Solutions for Power-of-Two Cases

While this argument rules out many dimensions, it does not preclude solutions when 'n' is a power of two, such as 4 or 64 dimensions <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The solution for the original 64-square puzzle involves a particularly symmetric way to color the corners of a high-dimensional cube <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. For example, a solution for the 4-square case can be explicitly visualized as coloring a 4-dimensional cube such that each of its four neighbors represents a different color <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

The actual solution to the chessboard puzzle, along with a detailed walkthrough of thought processes and multiple approaches, is demonstrated in a collaborative video with Matt Parker on the Stand Up Maths channel <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. The connection between this puzzle and [[relation_between_the_puzzle_and_error_correction | Hamming codes]] and [[wordle_solving_strategies_and_information_theory | information theory]] can also be explored further <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.