---
title: The impossible chessboard prisoner puzzle
videoId: wTJI_WuZSwE
---

From: [[3blue1brown]] <br/> 

The Chessboard Prisoner Puzzle is one of those classic [[problemsolving_strategies_in_mathematical_puzzles | prisoner puzzles]] where a math-obsessed warden offers two inmates a chance for freedom if they solve an elaborate scheme [00:00:10]. The setup involves a chessboard with 64 squares, each having a coin on top [00:00:07]. The warden arranges the coins (heads or tails) in any pattern they choose [00:00:23]. A key is then placed inside one of the 64 secret compartments, one for each square [00:00:32].

## The Goal

The first prisoner (P1) enters the room, sees the coin arrangement and the key's location [00:00:35]. P1 is allowed to perform one and only one action: turn over one coin [00:00:44]. After this, P1 leaves, and the second prisoner (P2) enters [00:00:53]. P2, with no information other than the final coin arrangement, must deduce the key's hidden location to win freedom for both [00:00:56].

## Strategy and Adversarial Conditions

Before the puzzle begins, the two prisoners can strategize together [00:01:09]. However, they will not know the specific initial layout of heads and tails, and the warden can listen to their strategy, aiming to thwart it with an adversarial arrangement of coins and the key [00:01:13].

## Underlying Mathematical Concepts

This puzzle leads to deep mathematical insights, particularly in [[information_theory_in_gamesolving | information theory]] and geometry.

### Rabbit Holes of Discovery

The puzzle's solution led to two surprisingly interesting "rabbit holes" [00:01:43]:
1.  **Proof of Impossibility**: Demonstrating that the challenge becomes impossible if the setup is slightly varied, such as making it a 6x6 chessboard or removing one of the squares [00:01:47]. This exploration culminates in understanding "an especially pleasing way to paint the corners of a 4-dimensional cube" [00:02:00].
2.  **Error Correction Connection**: The puzzle's solution is closely related to error correction, a "super important topic in computer science and [[information_theory_in_gamesolving | information theory]]" [00:02:05]. Error correcting codes add a "shockingly small amount of information" to a message, making it possible for the receiver to identify when there's an error and precisely how to fix it, even if "the messiness of the real world inevitably flips a bit now and then" [00:02:26]. The intuition behind solving this puzzle is essentially the same as that for Hamming codes, which are "one of the earliest examples of highly efficient error correction" [00:02:39].

## Visualizing the Puzzle: High-Dimensional Cubes

To understand the puzzle's mechanics and potential strategies, it's helpful to visualize the coin arrangements as points in a geometric space.

### From Coins to Binary Strings

Instead of heads and tails, coins can be thought of as ones and zeros, which is "much easier to do math with" [00:03:38]. Each possible arrangement of coins then becomes a binary string [00:10:44].

### The Simplest Case: 2 Squares, 2 Coins

For two squares and two coins, there are four possible states for the board [00:04:11]. These can be thought of as "a set of coordinates," where each of the four possible states sits "at the corners of a unit square" [00:04:44]. Flipping one of the coins corresponds to moving along an edge of the square, since it's "only changing one of the coordinates" [00:05:02]. A strategy could involve associating the bottom two corners (y-coordinate is 0) with the key being under square zero, and the top two corners (y-coordinate is 1) with the key being under square one [00:05:10]. This ensures P1 can always guarantee ending up in the desired region by flipping one coin [00:05:31].

### Expanding to 3 Squares, 3 Coins

With three squares and three coins, there are eight possible states that the coins can be in [00:05:50]. Interpreting these states as coordinates brings the representation "up into three-dimensional space, with each state sitting at the corner of a unit cube" [00:06:00]. The usefulness of this picture is that it gives a "very vivid meaning to the idea of turning over one of the coins": "Every time you flip a coin, you're walking along the edge of a cube" [00:06:10].

### Strategies as Coloring the Cube

A strategy for the puzzle is equivalent to "coloring each of the eight corners of the cube" with a color representing the key's location (e.g., red for square zero, green for square one, blue for square two) [00:06:48].

The total number of possible strategies for the 3-square case is 3 to the power of 8 (3 choices for the color of each of 8 vertices) [00:07:22]. For the original 64-square puzzle, there are "64 to the 2 to the 64 total possible strategies" [00:07:32].

For a strategy to work, P1 must be able to change the state to any desired "color" (key location) by flipping just one coin [00:06:24]. This means that from any given corner, its neighbors (the states reachable by one coin flip) "always represent red, green, and blue" [00:10:08]. If a corner has two neighbors of the same color, the warden can thwart the strategy by placing the key in the color that cannot be reached [00:09:47].

## The Impossibility Proof: Why Some Boards Don't Work

This problem can be reframed as an "interesting [[combinatorial_puzzles_and_strategy_development | combinatorial question]]": can you paint a high-dimensional cube so that the neighbors of any given vertex always represent all possible key locations? [00:10:05]

### The Coloring Argument

Consider the 3-square case with 8 corners and 3 key locations (colors: red, green, blue) [00:06:52]. For a strategy to work, every corner must have exactly one red, one green, and one blue neighbor [00:13:20].

A "lovely little argument" explains "not only why this will never work in three dimensions, but also why it can't work in any dimension that's not a power of two" [00:12:20]. The idea is that the symmetry implies there have to be an equal number of red, green, and blue vertices [00:13:30]. This would mean "eight-thirds of each, which is not possible" [00:13:38].

To solidify this intuition, imagine a process where you go through each corner and count how many of its neighbors are a particular color, say red [00:12:57].
1.  If the desired property holds (every corner has exactly one red neighbor), the total count of "red neighbors seen" from all 8 corners would be 8 [00:13:20].
2.  Conversely, every red corner is counted exactly three times (once for each instance where it's somebody's neighbor) [00:13:27].
3.  Therefore, the final tally has to be three times the total number of red corners [00:13:34].
4.  Equating these, if the property holds, the number of red corners must be 8/3 [00:13:40].
5.  Since it's impossible to have 8/3 corners, this strategy is impossible in three dimensions [00:13:40].

### Generalization to Higher Dimensions

This argument "immediately generalizes to higher dimensions" [00:13:56]. For `n` squares, the puzzle involves a cube in `n` dimensions.
*   The total number of vertices (coin arrangements) is `2^n` [00:14:43].
*   If you're standing at one of these vertices, you have `n` distinct neighbors (flipping one of `n` coins) [00:14:38].
*   If a strategy is to work with `n` possible key locations, each vertex must have exactly one neighbor corresponding to each of the `n` locations [00:14:12].

Applying the same counting logic:
1.  Summing up the count of "red neighbors seen" from each of the `2^n` vertices would yield `2^n` [00:14:53].
2.  Each red corner is counted `n` times (once for each of its `n` neighbors) [00:15:04].
3.  Therefore, `n` times the total number of red corners must equal `2^n` [00:15:10].
4.  For this equation to hold with integer numbers of corners, `n` (the number of squares) "could only ever happen if n itself is some smaller power of 2" [00:15:14].

This proves that "no possible strategy, no matter how clever you are, can work in all of the cases for this chessboard puzzle, if the number of squares isn't a power of 2" [00:15:52]. This means that "even though it might seem to make it easier if you knock off a couple squares or reduce the size of the board, it actually makes the task hopeless" [00:16:06]. For dimensions like 4 or 64 (powers of 2), there is "no contradiction" and it is "at the very least possible" to evenly divide the vertices among colors [00:15:24].

## The Original Puzzle's "Almost Impossible" Nature

The fact that the solution to the original 64-square puzzle exists means it can be viewed as "a particularly symmetric way to color the corners of a high dimensional cube in a way that's disallowed in most dimensions" [00:16:14]. This perspective highlights how the original puzzle is, in a sense, "almost impossible" [00:03:48].

## Solution and Further Exploration

The explicit solution to the 64-square chessboard puzzle is explored in a video on the Stand Up Maths channel with Matt Parker [00:02:58]. Both the thought processes and multiple ways of looking at the solution are discussed there [00:03:07].

The connection between this puzzle and [[information_theory_in_gamesolving | Hamming codes]] and error correction is a fascinating area for further video exploration [00:17:55].