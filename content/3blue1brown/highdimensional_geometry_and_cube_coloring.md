---
title: Highdimensional geometry and cube coloring
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

This article explores how a classic prisoner puzzle involving a chessboard and coins can be translated into a problem of [[higher_dimensions_and_their_relevance | high-dimensional geometry]] and cube coloring, revealing surprising mathematical truths about information theory and error correction.

## The Chessboard Coin Puzzle

The puzzle presents a scenario where a math-obsessed warden offers two prisoners a chance for freedom <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. One prisoner, alone in a room, finds a chessboard with 64 squares, each having a coin (heads or tails) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The warden has arranged the coins in a specific pattern and placed a key inside one of the squares, showing the first prisoner its location <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

The first prisoner's task is to communicate the key's location to the second prisoner <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The only action allowed is to flip exactly one coin on the board <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The second prisoner then enters the room, sees the coin arrangement, and must deduce the key's hidden location to win freedom for both <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Both prisoners can strategize beforehand, but they won't know the initial coin layout, and the warden will try to thwart their plan <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Mathematical Rabbit Holes

Solving this puzzle leads to two "surprisingly interesting rabbit holes" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>:
1.  **Impossibility Proofs**: Proving the challenge is impossible if the setup is slightly varied, such as a 6x6 chessboard or removing a square <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This involves [[exploring_fourdimensional_geometry_and_its_implications | painting the corners of a 4-dimensional cube]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
2.  **Error Correction**: Connecting the puzzle's solution to error correction, a critical topic in computer science and information theory <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Error correcting codes add a small amount of information to a message, allowing receivers to identify and fix flipped bits <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The puzzle's intuition is essentially the same as that behind Hamming codes, an early example of efficient error correction <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Visualizing the Puzzle Geometrically

To understand the puzzle's solution space, coins are re-interpreted as ones and zeros <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This allows for a geometric visualization:

### Two-Square Case
In the simplest case with two squares and two coins, there are four possible states (00, 01, 10, 11) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. These can be thought of as coordinates, representing the corners of a unit square <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Flipping a coin means moving along an edge of the square, as only one coordinate changes <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Three-Square Case
For three squares, three coins, and three possible key locations, there are eight possible states (000 to 111) <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Interpreting these states as coordinates lifts the problem into three-dimensional space, with each state at the corner of a unit cube <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Flipping a coin corresponds to walking along an edge of this cube <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Generalization to Higher Dimensions
The original 64-square chessboard puzzle can be visualized as a 64-dimensional cube, where each vertex represents a unique arrangement of 64 coins, and flipping a coin means moving along an edge <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This approach of thinking about binary strings as vertices of a [[higher_dimensions_and_their_relevance | high-dimensional cube]], with bit flips corresponding to edges, is common in coding theory <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Strategies as Cube Coloring

A strategy for the puzzle means that for any given coin configuration, the second prisoner can deduce the key's location <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This translates to "coloring" each corner of the cube (representing a coin state) with a color corresponding to the key's location (e.g., red for square 0, green for square 1, blue for square 2) <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

For a strategy to work, no matter where the first prisoner starts (a specific vertex color), they must be able to flip one coin (move along an edge) to reach any desired key location (any specific color) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This means every vertex must have neighbors representing all possible key locations <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. For the three-square case, this implies every vertex must have a red, green, and blue neighbor <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

The total number of possible strategies is immense; for the original 64-square puzzle, it is 64 to the power of 2 to the 64 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

## Proof of Impossibility for Non-Power-of-Two Dimensions

The geometric visualization allows for a proof that the puzzle is impossible if the number of squares (n) is not a power of two <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### The Counting Argument
Consider a desired coloring where each vertex has exactly one neighbor of each color (assuming there are `n` possible key locations, and thus `n` colors).
1.  **Count by Vertex**: Go through each of the `2^n` vertices and count how many of its `n` neighbors are, for example, "red" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. If the desired property holds, each vertex would have exactly one red neighbor <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. The total sum would then be `2^n` (one for each vertex) <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
2.  **Count by Color**: Each "red" vertex is counted `n` times (once for each of its `n` neighbors) <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. So, the total sum must also be `n` times the total number of red corners <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

For these two counts to be equal, `2^n` must equal `n * (number of red corners)` <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. Since `2^n` is a power of 2, `n` itself must also be a power of 2 <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

> [!NOTE] Conclusion
> This means that if the number of squares (`n`) is not a power of 2 (e.g., 3 squares or 6 squares), then it's impossible to have an equal distribution of colors that satisfies the puzzle's conditions <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This proves that no possible strategy can work if `n` is not a power of 2, rendering the task hopeless <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

### Example: Three-Square Case
For three squares, `n=3`. The total number of vertices is `2^3 = 8`. If the puzzle were solvable, there would need to be `8/3` red corners, `8/3` green corners, and `8/3` blue corners, which is impossible <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

### Example: Four-Dimensional Cube
While most [[higher_dimensions_and_their_relevance | higher dimensions]] are difficult to visualize, a [[exploring_fourdimensional_geometry_and_its_implications | 4-dimensional cube]] can be projected into 3D space, showing its vertices and edges <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. For `n=4` (a power of 2), the argument doesn't lead to a contradiction, meaning a solution *might* exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The solution to the 4-square case involves a particularly symmetric coloring of the [[exploring_fourdimensional_geometry_and_its_implications | 4-dimensional cube]] <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.

The ability to analyze how to color a [[higher_dimensions_and_their_relevance | high-dimensional cube]] is a valuable and transferable skill, especially in fields like coding theory <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

## Solution and Further Exploration

The actual solution to the 64-square chessboard puzzle (which works because 64 is a power of 2) is discussed in detail on Stand Up Maths with Matt Parker <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. The solution can be viewed as a uniquely symmetric way to color the corners of a [[higher_dimensions_and_their_relevance | high-dimensional cube]] <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

The connection between this puzzle and [[vectors_in_two_and_three_dimensions | Hamming codes]] and error correction is also a topic of interest <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.