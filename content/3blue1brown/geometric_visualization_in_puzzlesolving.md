---
title: Geometric visualization in puzzlesolving
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

[[puzzles_and_geometric_problemsolving | Geometric visualization]] can transform complex problems, such as [[the_impossible_chessboard_puzzle | the impossible chessboard puzzle]], into more intuitive geometric challenges like coloring the corners of a high-dimensional cube. This approach simplifies the understanding of problem constraints and potential solutions, often revealing deeper mathematical truths [00:10:05].

## The Impossible Chessboard Puzzle
The [[the_impossible_chessboard_puzzle | impossible chessboard puzzle]] involves a chessboard with 64 squares, each having a coin [00:00:03]. A warden sets the coins to heads or tails in any pattern and places a key in one of the squares [00:00:23]. The first prisoner must flip exactly one coin [00:00:48]. The second prisoner then enters the room and, based solely on the coin pattern, must deduce the key's location [00:00:56]. Both prisoners can strategize beforehand but won't know the initial coin arrangement or key location, and the warden can choose an adversarial setup [00:01:09].

### Transforming the Puzzle: From Coins to Coordinates
To facilitate analysis, the coins can be thought of as ones and zeros instead of heads and tails [00:04:38]. Each unique arrangement of coins then becomes a set of coordinates [00:04:44].

For instance, with two squares and two coins:
*   The four possible states of the board (e.g., HH, HT, TH, TT) can be represented as coordinates that sit at the corners of a unit square [00:04:47].
*   Flipping one coin corresponds to moving along an edge of this square, as only one coordinate changes [00:05:02].

Extending this to three squares and three coins:
*   There are eight possible states for the coins [00:05:56].
*   These states can be interpreted as coordinates in three-dimensional space, with each state representing a corner of a unit cube [00:06:00].
*   Turning over a coin is vividly represented as walking along the edge of this cube [00:06:13].

### Strategy as Cube Coloring
Devising a strategy for the puzzle is equivalent to coloring each corner of the cube (or hypercube in higher dimensions) with different colors, where each color represents a possible location for the key [00:06:48]. For the three-square case, if the key can be in one of three squares (e.g., square 0, 1, or 2), the corners of the cube would be colored red, green, or blue, respectively [00:06:39].

The total number of possible strategies is enormous: for a 64-square chessboard, there are 64 (possible key locations) to the power of 2^64 (total coin configurations) strategies [00:07:36].

### Geometric Interpretation of a Winning Strategy
A successful strategy requires that from any starting coin configuration (any corner of the cube), the first prisoner can make one flip (move along one edge) to reach a configuration that unambiguously communicates the key's location to the second prisoner [00:05:31], [00:11:32]. In the cube coloring analogy, this means that from any given vertex, its neighbors must represent all possible key locations (i.e., all required colors) [00:10:08], [00:11:32].

An example of a failed strategy in the 3-square case shows a corner where two neighbors share the same color, meaning there's no way to reach a third color (key location) [00:09:02]. An adversarial warden could then place the key in the unreachable square to thwart the strategy [00:09:31].

### The Impossibility Proof Through Coloring
This [[geometric_reasoning_in_higher_dimensions | geometric reasoning in higher dimensions]] offers a powerful way to prove why certain variations of the puzzle are impossible, regardless of the chosen strategy [00:03:20].

#### The Counting Argument
For a puzzle with *N* squares:
1.  **Number of vertices**: There are 2<sup>N</sup> possible coin configurations, each represented by a vertex in an N-dimensional hypercube [00:14:43].
2.  **Number of neighbors**: Each vertex has *N* distinct neighbors, corresponding to flipping one of the *N* coins [00:14:38].
3.  **Coloring requirement**: For a solution to exist, each vertex must have *k* (where *k* is the number of possible key locations) neighbors that cover all *k* colors [00:10:08].
4.  **Symmetry**: If a solution exists, a symmetric property is implied: there must be an equal number of vertices for each color [00:13:30]. For instance, if there are *k* key locations, then 2<sup>N</sup> / *k* vertices must be assigned to each color.
5.  **The Proof**: By counting how many times a particular color (e.g., red) appears as a neighbor:
    *   If a solution exists, every corner would have exactly one red neighbor. Thus, the total count of red neighbors across all 2<sup>N</sup> vertices would be 2<sup>N</sup> [00:15:02].
    *   Alternatively, each red corner is counted *N* times (once for each of its *N* neighbors). So, the total count is *N* times the number of red corners [00:15:04].
    *   Therefore, *N* multiplied by the number of red corners must equal 2<sup>N</sup>. This implies that *N* must be a power of two for a solution to be possible [00:15:14].

This argument demonstrates that if the number of squares (N) is not a power of two (e.g., 3, 6, 64-1), a solution is impossible [00:12:20], [00:15:52]. This means removing even a single square from a 64-square board makes the task "hopeless" [00:01:47], [00:16:06].

### Connection to Other Fields
[[Geometric reasoning in higher dimensions | Thinking about binary strings as vertices of a high-dimensional cube]], with bit flips corresponding to edges, is a common approach in various fields [00:10:44]. This is particularly true in [[coding_theory]] and information theory, where it's used to analyze concepts like error correction [00:02:09], [00:10:47]. The intuition behind solving [[the_impossible_chessboard_puzzle | this puzzle]] is essentially the same as that behind Hamming codes, an early example of efficient error correction [00:02:39].

The process of coloring corners of a cube is also used in other mathematical problems, such as those related to [[Ramsey theory]] and incredibly large numbers like Graham's constant [00:11:03].