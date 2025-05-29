---
title: The impossible chessboard puzzle
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

The "impossible chessboard puzzle" is a classic [[prisoner_puzzle_and_strategy_development | prisoner puzzle]] involving a chessboard, coins, and a hidden key <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It challenges two inmates to secure their freedom by determining the key's location based on a single action taken by the first prisoner <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Puzzle Setup

The puzzle begins with a chessboard where each of its 64 squares has a coin <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. A math-obsessed warden arranges the coins (heads or tails) in any desired pattern and hides a key in one of the squares, which functions as a secret compartment <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The first prisoner knows the key's location <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

The goal is for the second prisoner to also know where the key is <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The first prisoner's only allowed action is to flip *one and only one* coin before leaving the room <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The second prisoner then enters, and based solely on the coin arrangement (which has been subtly tweaked), must deduce the key's hiding place <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Prisoners can strategize beforehand, but they won't know the initial coin layout, and the warden will try to thwart any strategy with an adversarial arrangement <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Exploring the Puzzle's Depths

This puzzle often leads to deeper mathematical insights:
*   **Proving Impossibility:** One "rabbit hole" involves proving that the challenge becomes impossible if the setup is slightly varied, such as using a 6x6 chessboard or removing a square <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Connection to Error Correction:** Another fascinating aspect is the puzzle's close connection to error correction, a critical topic in computer science and information theory <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. The intuition behind solving this puzzle is similar to that of Hamming codes, an early form of highly efficient error correction <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

Instead of directly solving the puzzle, a deeper analysis involves taking a global view of all possible strategies and demonstrating why certain variations are inherently flawed <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This proof highlights how the solution to the original puzzle is, in a sense, "almost impossible" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## [[Geometric visualization in puzzlesolving | Geometric Visualization]] of Strategies

To understand solving the puzzle, it's helpful to visualize the possible states and actions <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Coins as Binary Strings

First, coins are conceptualized as ones and zeros instead of heads and tails for easier mathematical manipulation <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### The Two-Square Case

Consider the simplest meaningful case: two squares, two coins, and two possible key locations <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   Pairs of coins can be seen as coordinates <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   The four possible states (coin arrangements) correspond to the corners of a unit square <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Flipping a coin moves you along an edge of the square, as it only changes one coordinate <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   A strategy might involve associating different regions of the square with the key's location <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. For a solution to work, from any starting state, flipping one coin must allow the first prisoner to lead the second prisoner to the correct key location <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### The Three-Square Case

Scaling up, for three squares, three coins, and three key possibilities, there are eight possible coin states <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   These states can be interpreted as coordinates in three-dimensional space, with each state at the corner of a unit cube <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   Flipping a coin still means moving along an edge of the cube <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

#### Strategies as Cube Colorings

A strategy for this puzzle means that the second prisoner can associate any coin arrangement (three bits) with one of three possible key squares <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   This can be visualized as coloring each of the cube's eight corners (vertices) with one of three colors (e.g., red for square zero, green for square one, blue for square two) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   The total number of strategies is 3 to the power of 8 (3^8) for three squares <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. For the original 64-square puzzle, there are 64^(2^64) possible strategies <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   For a strategy to be successful, no matter the starting position, flipping one coin must allow the first prisoner to reach a state that communicates the desired key location <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. In terms of coloring, this means that for any given vertex, its neighbors (reached by flipping one coin) must collectively represent all three possible key locations (colors) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

An example strategy for the three-square case, like summing coins modulo 3, fails because it doesn't guarantee access to all three colors (key locations) from every starting point <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This failure is visually apparent when a corner has two neighbors of the same color, meaning there's no way to communicate one of the key locations <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### The Impossibility Proof: Coloring High-Dimensional Cubes

The idea of representing binary strings as vertices of a high-dimensional cube where bit flips correspond to edges is common in coding theory <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

For the three-square case, the question becomes: can you color the eight corners of the cube (representing the 2^3 possible coin arrangements) with three colors (representing the three key locations) such that every vertex has one neighbor of each color? <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a> The answer is no.

**The Argument:**
1.  **Count Neighbors of a Specific Color:** Imagine going through each corner of the cube and counting how many of its neighbors are a specific color, say red. If the desired property (every vertex has a red, green, and blue neighbor) holds, then every corner must have exactly one red neighbor <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
2.  **Total Count from Vertex Perspective:** For an `n`-dimensional cube, there are `2^n` total vertices <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. If each has exactly one red neighbor, the total count of "red neighbors" summed over all vertices would be `2^n * 1 = 2^n` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
3.  **Total Count from Color Perspective:** Every red corner is a neighbor to `n` other vertices (because it has `n` edges leading from it) <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. So, the total count of "red neighbors" is also equal to `n * (the total number of red corners)` <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
4.  **The Contradiction:** Equating these two ways of counting, we get: `2^n = n * (Number of Red Corners)` <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
    *   This implies that `(Number of Red Corners) = 2^n / n`.
    *   For the number of red corners to be an integer, `n` must be a power of 2 <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
    *   In the three-square case, `n=3`. `2^3 / 3 = 8/3`, which is not an integer. This proves it's impossible to color the cube in the required way, meaning no strategy can work for three squares <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

This argument generalizes to any number of squares (`n`). If the number of squares (`n`) is not a power of two, it's impossible to solve the puzzle, because it's impossible to evenly divide the vertices among the different colors under the required conditions <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. This means variations like a 6x6 board or removing squares make the task hopeless <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

However, if `n` *is* a power of two (like the original 64 squares, where 64 = 2^6, or 4 squares, where 4 = 2^2), this mathematical argument doesn't rule out a solution <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The solution to the original puzzle is a particularly symmetric way to color the corners of a high-dimensional cube that is disallowed in most dimensions <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

### Visualizing the Four-Dimensional Cube

While most higher-dimensional cubes are impossible to visualize, it's possible to project a 4-dimensional cube into 3D space to see how its vertices and edges are connected <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. This allows for a "4-dimensional cousin of a sudoku" puzzle, trying to color the 16 vertices such that each of the 4 neighbors of any one vertex represent all 4 different colors <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. This is possible because 4 is a power of 2.

> [!INFO] Solution
> The full solution to the original 64-square chessboard puzzle, and an exploration of how different problem-solvers approached it, can be found on the Stand Up Maths YouTube channel in collaboration with Matt Parker <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. The connection between this puzzle and [[Brilliantorg problemsolving puzzles | Hamming codes]] and [[Geometric visualization in puzzlesolving | error correction]] offers further insight into its mathematical significance <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.