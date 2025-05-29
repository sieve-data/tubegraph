---
title: Combinatorial puzzles and strategy development
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

## The Chessboard Prisoner Puzzle

The chessboard prisoner puzzle is a classic example of a [[problem_solving_strategies_in_mathematics | combinatorial puzzle]] that involves strategy development under adversarial conditions <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It serves as a strong motivating problem for exploring deeper mathematical concepts like [[information_theory_in_gamesolving | information theory]] and high-dimensional geometry <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Puzzle Setup

In this puzzle, two prisoners are offered a chance for freedom if they solve an elaborate scheme set up by a math-obsessed warden <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The setup involves:
*   A chessboard with 64 squares, each having a coin (heads or tails) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
*   The warden carefully sets the coins to any pattern <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   A key is hidden inside one of the 64 squares <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   Prisoner 1 enters the room, sees the coin configuration and the key's location <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   Prisoner 1's only allowed action is to turn over one and only one coin before leaving the room <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   Prisoner 2 then enters the room and, with no additional information, must deduce the key's location based solely on the final coin configuration <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Strategy Constraints

The prisoners can strategize ahead of time <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. However, they will not know the initial coin layout or key location beforehand, and the warden can listen to their strategy, attempting to thwart it with an adversarial arrangement of coins and the key <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Problem-Solving Approach: Geometric Visualization

A powerful strategy for analyzing such puzzles is to visualize the problem geometrically <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

#### Representing Coin States

Coins can be thought of as ones and zeros instead of heads and tails, making them easier to work with mathematically <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. A configuration of `n` coins can be seen as an `n`-bit binary string <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

#### High-Dimensional Cubes

These binary strings correspond to the vertices of an `n`-dimensional unit cube (a hypercube) <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **2 Squares/Coins:** States are pairs of coins (0,0), (0,1), (1,0), (1,1), which map to the four corners of a unit square <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **3 Squares/Coins:** States are triples of coins (0,0,0) to (1,1,1), mapping to the eight corners of a unit cube in three-dimensional space <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **64 Squares/Coins:** The original puzzle involves a 64-dimensional cube <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

Flipping one coin corresponds to moving along an edge of this `n`-dimensional cube, as it changes only one coordinate (or bit) <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

#### Coloring the Cube: Defining a Strategy

A strategy for the puzzle can be conceptualized as "coloring" each vertex of the `n`-dimensional cube <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Each color represents one of the possible key locations <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Goal of Strategy:** When Prisoner 2 sees the coin configuration, they must know which square the key is under <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This means each state (corner) must be associated with a unique key location (color) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Prisoner 1's Action:** Prisoner 1 must be able to flip one coin to ensure the resulting state (corner) indicates the *actual* key location <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This implies that for any given vertex (initial coin state), its neighbors (states reachable by one flip) must collectively represent all possible key locations (colors) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. For the 3-square case with 3 key locations, this means each vertex must have one red, one green, and one blue neighbor <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

The total number of possible strategies is enormous: for the original 64-square puzzle, there are 64 to the power of 2 to the power of 64 total possible strategies <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Proof of Impossibility (for certain dimensions)

This geometric perspective allows for a proof that the puzzle is impossible for certain board sizes <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

#### The Counting Argument

The argument relies on the properties of counting "colored neighbors" on the cube's vertices <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
1.  **Desired Property:** If a solution exists, every vertex of the `n`-dimensional cube must have exactly one neighbor of each of the `n` colors (representing the `n` key locations, which in this case is `n` itself) <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
2.  **Total Count (Method 1):** Summing how many neighbors of a particular color (e.g., red) each vertex has. If every vertex has exactly one red neighbor, and there are `2^n` total vertices, this sum would be `2^n * 1 = 2^n` <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
3.  **Total Count (Method 2):** Summing how many neighbors *each red vertex* has. Since each red vertex has `n` neighbors, this sum must be `n * (total number of red vertices)` <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
4.  **Equating the Counts:** For a solution to exist, these two sums must be equal: `2^n = n * (total number of red vertices)` <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
5.  **Conclusion:** For this equation to hold, `n` must be a factor of `2^n`. This implies that `n` itself must be a power of two <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

#### Implications

*   **Impossible Cases:** If the number of squares (`n`) is not a power of two (e.g., 3 squares, 6 squares), then no strategy, no matter how clever, can work <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The warden can always thwart the players <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Possible Cases:** If `n` *is* a power of two (like 4 or 64), the argument doesn't rule out a solution, but it doesn't guarantee one either <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The original 64-square puzzle (where 64 is `2^6`) is therefore theoretically solvable <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

This type of combinatorial argument, often involving "coloring" or partitioning, is a common technique in mathematics <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

### Connections to Other Fields

*   **Error Correction:** The intuition behind solving this puzzle is similar to that of [[information_theory_in_gamesolving | Hamming codes]], which are efficient error-correction codes used in computer science <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Error-correcting codes add a small amount of information to a message, allowing the receiver to detect and fix bit flips caused by real-world messiness <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Coding Theory:** The representation of binary strings as vertices of high-dimensional cubes with bit flips as edges is fundamental in coding theory <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

### Solution

The specific solution to [[the_impossible_chessboard_prisoner_puzzle | the impossible chessboard prisoner puzzle]] (for the 64-square case) is not provided in this transcript, but is covered in a collaborative video on the Stand Up Maths channel <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. The solution itself can be viewed as a particularly symmetric way to color the corners of a high-dimensional cube <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.