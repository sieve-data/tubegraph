---
title: Applications of derivatives in solving math puzzles
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

Traditional introductions to calculus often focus on graphical interpretations of derivatives, such as the slope of a curve <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. While this provides a valuable [[Visualizing derivatives using graphs | visual intuition]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, it can become a conceptual hurdle when generalizing calculus beyond functions whose inputs and outputs are simple numbers <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. An alternative "transformational view" of derivatives offers a more flexible way to understand and apply them, particularly in solving complex problems <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## The Transformational View of Derivatives

Instead of viewing a function as a graph, the transformational view conceptualizes it as mapping input points on one number line to output points on another <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. In this context, the derivative measures how much the input space gets stretched or squished in various regions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

For example, for the function `x²`:
*   Around an input of 1, a small cluster of points gets stretched by a factor of approximately 2 <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This means the derivative at `x = 1` is 2 <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   Around an input of 3, points get stretched by a factor of 6 <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>, indicating a derivative of 6 at `x = 3` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Around an input of 1/4, points get contracted by a factor of 1/2 <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. A derivative smaller than 1 signifies this contraction <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   Around an input of 0, a small region collapses into 0 itself as you zoom in, which indicates a derivative of 0 <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   For negative inputs, like -2, points get stretched and flipped. For instance, around -2, the action looks like multiplying by -4, which is what a negative derivative signifies <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

This view emphasizes how sensitive the function is to tiny nudges around the input, which is a more fundamental understanding than just slope <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Solving the Infinite Fraction Puzzle

This transformational view can be applied to solve mathematical puzzles that involve repeated function applications, such as the infinite continued fraction:
`1 + 1 / (1 + 1 / (1 + 1 / ...))` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### Identifying Fixed Points
To evaluate this expression, one common approach is to set it equal to `x` and notice that a copy of the full fraction is contained within itself <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This leads to the equation `x = 1 + 1/x`, which can be rearranged to `x² - x - 1 = 0`. The solutions to this quadratic equation are the "fixed points" of the function `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

There are two solutions for `x`:
1.  **The Golden Ratio (`phi`)**: Approximately 1.618 <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  **Phi's Little Brother**: Approximately -0.618, which is `-1/phi` <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### The Question of Validity and Convergence
The puzzle then arises: Is the infinite fraction also equal to the negative value, given that all terms in its expression are positive <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>?

One way to think about the infinite fraction is as a limiting process: start with an initial constant (e.g., 1) and repeatedly apply the function `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. When this is done numerically, starting with almost any random number, the sequence of outputs consistently converges to `1.618` (phi) <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Even when starting with a number very close to phi's little brother, the sequence eventually shies away from it and jumps to phi <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### Explaining Stability with the Transformational View
The [[paradoxes_in_the_concept_of_derivatives | stability]] of these fixed points can be explained using the transformational view of derivatives:

*   **Traditional (Graphical) Approach**: The "spiderweb diagram" method plots the function `y = f(x)` and the line `y = x`. Iteratively, you move from `(x, f(x))` horizontally to `(f(x), f(x))` on the `y = x` line, then vertically to `(f(x), f(f(x)))` on the function graph, and so on <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. While it can show convergence or divergence, its interpretation can be awkward <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. The conditions for convergence relate to the slope of the function <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

*   **Transformational View Application**: When repeatedly applying `f(x) = 1 + 1/x` as a transformation:
    *   **Near Phi (1.618)**: If you zoom in on a neighborhood around phi, points in that region get *contracted* towards phi with each application <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This occurs because the derivative of `f(x)` at `x = phi` has a magnitude less than 1 (approximately -0.38) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This "scrunching" behavior makes phi a **stable fixed point** <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>, acting like a gravitational pull <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
    *   **Near Phi's Little Brother (-0.618)**: In contrast, the derivative of `f(x)` at `x = -0.618` has a magnitude *larger* than 1 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. Points near this fixed point are *repelled* away from it, being stretched by more than a factor of 2 in each iteration <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This makes it an **unstable fixed point** <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

This directly explains why `phi` is the value that appears when the function is repeatedly applied numerically, while phi's little brother does not <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. A fixed point is considered stable if, when perturbed slightly, it tends to return to its original state <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The stability of a fixed point is determined by whether the magnitude of its derivative is less than or greater than 1 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

While the transformational view can sometimes be clunky for visualizing entire functions compared to graphs <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>, its utility in explaining phenomena like fixed point stability in function iteration makes it a valuable tool for [[calculating_derivatives_and_their_applications | problem-solving strategies in mathematical puzzles]] and understanding more [[computing_derivatives_of_functions | advanced topics]] beyond single-variable calculus <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.