---
title: Tiling in higher dimensions
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

Higher dimensions can provide surprising and delightful insights into solving puzzles in lower dimensions, even those that initially appear to be purely geometric [00:00:08](<a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This concept is explored through various examples, including specific tiling problems.

## Rhombus Tiling and Stacked Cubes

Consider a rhombus shape with internal angles of 60 and 120 degrees [00:00:34](<a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Copies of this rhombus can tile the plane in many distinct, pseudo-hexagonal patterns [00:00:47](<a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. A specific move involves identifying three rhombus shapes forming a small hexagon and rotating them 60 degrees to generate a slightly different tiling [00:01:01](<a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

The puzzle arises when considering tiling a finite hexagon (with side lengths as whole numbers, e.g., 4) with these rhombuses, each having a side length of 1 [00:01:52](<a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The question is whether it's possible to get from any tiling of this finite hexagon to any other using the 60-degree rotation move [00:02:06](<a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. If yes, a follow-up asks about the maximum number of moves required as a function of the hexagon's size [00:02:32](<a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Solution: Projecting 3D Cubes

The solution involves [[Analogy between 2D 3D and higher dimensions | stepping into a higher dimension]] [00:06:42](<a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. By coloring the tiles based on their orientation, the 2D tiling can be thought of as a projection of a stack of 3D cubes [00:04:42](<a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Any stack of cubes within an n by n by n frame corresponds to one of these rhombus tiling patterns, and conversely, any rhombus tiling has a corresponding stack of cubes [00:04:50](<a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The fundamental move of rotating a hexagon is equivalent to adding or removing cubes from this stack [00:05:34](<a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This simplifies the problem significantly [00:05:38](<a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>:
*   It becomes clear that any pattern can be reached from any other by removing all cubes to an empty state and then adding back the necessary cubes for the target pattern [00:05:43](<a class="yt-timestamp" data="00:05:43">[00:05:43]</a>.
*   The maximum number of steps to transform one configuration to another is achieved by going from an empty configuration to a full one [00:06:13](<a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. For an n x n x n stack, this requires `n cubed` different steps, as each move corresponds to adding or removing a single cube [00:06:16](<a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
This demonstrates how a purely 2D problem can be elegantly solved using [[Threedimensional puzzles and fourdimensional insights | three-dimensional thinking]], with the cubic nature of the numerical answer indicating the inherent 3D property of the puzzle itself [00:06:21](<a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Higher-Dimensional Tiling: The "Absurd Puzzle"

Inspired by the rhombus tiling puzzle, a natural question is whether a [[Threedimensional puzzles and fourdimensional insights | three-dimensional puzzle]] can be conceived that requires [[Analogy between 2D 3D and higher dimensions | stepping up into four dimensions]] for its solution [00:19:02](<a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. This leads to the concept of a 3D tiling pattern that a four-dimensional creature could perceive as a stack of four-dimensional hypercubes [00:19:10](<a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

### The Rhombic Dodecahedron

A 4D hypercube, with vertices as combinations of 0s and 1s in four coordinates, can be projected down into a 3D subspace [00:20:21](<a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. By projecting along the diagonal vector (1,1,1,1), the wireframe of a 4D cube appears as a beautiful and symmetric shape in 3D [00:21:56](<a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>. When made solid, this shape is known as a rhombic dodecahedron [00:22:10](<a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.

The rhombic dodecahedron's ability to tessellate 3D space becomes evident when viewed as a projection of a stack of hypercubes [00:22:26](<a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

### Constructing the Puzzle

Similar to how 2D rhombuses correspond to projections of 3D cube faces [00:23:50](<a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>, the "cubical cells" of a hypercube project into squished cube shapes that together form a rhombic dodecahedron [00:23:55](<a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

The "absurd puzzle" is as follows:
1.  Define a "squished cube shape" (a polyhedron formed from six rhombuses) [00:24:59](<a class="yt-timestamp" data-t="00:24:59">[00:24:59]</a>.
2.  Imagine tiling a large rhombic dodecahedron (with integer side length 'n') using many copies of this shape [00:25:11](<a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.
3.  The game involves finding a small 1x1x1 rhombic dodecahedron within the tiling and making a move where each piece slides through the middle [00:25:19](<a class="yt-timestamp" data-t="00:25:19">[00:25:19]</a>. This move is analogous to sliding rhombuses through the origin in the 2D projection [00:24:30](<a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.
4.  The puzzle asks for the maximum number of moves required to get from one tiling to another [00:25:29](<a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

### Solution: [[Higherdimensional cubes and coloring problems | Hypercube]] Stack Analogy

By understanding this puzzle as a projection of a stack of [[higherdimensional_cubes_and_coloring_problems | hypercubes]], the answer is `n to the power 4` [00:25:36](<a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>. This is because each move corresponds to adding or removing a hypercube from the 4D stack, similar to the 3D cube analogy in the first puzzle.

## Broader Implications of Higher Dimensions

These puzzles illustrate a broader mathematical phenomenon where constructs in higher dimensions can be surprisingly relevant to solving problems more easily in lower dimensions, or even non-geometric problems [00:26:01](<a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

Examples include:
*   **[[Quaternion multiplication and fourdimensional geometry | Quaternions]]**: An extension of complex numbers in four dimensions, offering an elegant way to encode and work with three-dimensional rotations and [[Transformations between different dimensions | transformations between different dimensions]] [00:26:15](<a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>. They involve unique "extra rigidity" when rotating a hypersphere [00:26:37](<a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **Sphere Packing**: An unusually elegant way to pack spheres in 24 dimensions is closely related to error correction codes used on Voyager spacecraft [00:26:54](<a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>. See also: [[Understanding higher dimensional spheres and shapes | Understanding higher dimensional spheres and shapes]].
*   **Random Vectors**: In very high dimensions, random vectors have a high chance of being nearly perpendicular [00:27:13](<a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>. This is relevant to [[Highdimensional vector embeddings | high-dimensional vector embeddings]] and compression algorithms, and may explain the performance of large language models [00:27:21](<a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. See also: [[Span of vectors in different dimensions | Span of vectors in different dimensions]].

### The Limits of Intuition

While [[geometric_reasoning_in_higher_dimensions | higher-dimensional reasoning]] provides powerful analytical tools, there's a distinction between analysis and intuition [00:27:37](<a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. Humans can intuitively grasp [[Analogy between 2D 3D and higher dimensions | 2D to 3D analogies]], like seeing a rhombus tiling as stacked cubes or a line as the intersection of two planes [00:27:41](<a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>. However, examples that use even higher dimensions often rely on pure analysis rather than intuitive understanding [00:28:11](<a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

Intuition acts as a guiding light in the vast space of logical moves for a proof [00:28:46](<a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. The "sadness" lies in the thought that some problems in three dimensions might have intuitive solutions accessible only to a four-dimensional (or higher) creature, insights that remain inaccessible to human intuition [00:28:54](<a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.