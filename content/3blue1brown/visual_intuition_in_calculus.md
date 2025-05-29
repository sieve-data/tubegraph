---
title: Visual Intuition in Calculus
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

Learning calculus involves hard work, memorizing formulas, and encountering moments of struggle, but also beautiful connections and moments of insight. A crucial aspect of learning calculus is developing [[mathematical_intuition_versus_analysis | mathematical intuition]], particularly through visualization <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Traditional Graph-Based Intuition
Most introductory calculus courses primarily rely on graph-based visual intuitions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   The derivative is understood as the slope of a graph <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   The integral is conceptualized as a certain area under that graph <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

This standard visual understanding defines the derivative as a new function that, for every input `x`, returns the slope of the graph at that point <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. However, it's more fundamentally about how sensitive the function is to tiny nudges around the input, with slope being just one way to view this sensitivity in the context of graphs <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. For more information, refer to the [[introduction_to_calculus_series | introduction to calculus series]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Limitations of Graph-Based Intuition
A significant limitation arises when generalizing calculus beyond functions where inputs and outputs are simply numbers <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. In such cases, it's not always possible to graph the function being analyzed <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. If one's intuitions about fundamental ideas like derivatives are too rigidly rooted in graphs, it can create a substantial conceptual hurdle when approaching more advanced topics such as [[Multivariable Calculus and Complex Analysis | multivariable calculus and complex analysis]] or differential geometry <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The Transformational View of Derivatives
An alternative way to think about derivatives, referred to as the "transformational view," generalizes more seamlessly into broader contexts where calculus is applied <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Core Idea
The basic idea behind this alternate visual is to think of a function as mapping input points on one number line to their corresponding outputs on a different number line <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. In this context, the derivative measures how much the input space gets stretched or squished in various regions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. If you zoom in on a specific input, the derivative tells you how spread out or contracted evenly spaced points around that input become after the mapping <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Examples
Consider the function `x^2` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>:
*   **At input 1:** A small cluster of points around input 1 gets stretched out, roughly by a factor of 2. This is what it means for the derivative of `x^2` at `x=1` to be 2 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **At input 3:** A neighborhood of points around input 3 gets stretched out by a factor of 6. This means the derivative of `x^2` at `x=3` is 6 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **At input 1/4:** A small region tends to get contracted by a factor of 1/2. This illustrates what it looks like for a derivative to be smaller than 1 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **At input 0:** As you zoom in closer and closer, a small neighborhood of points around 0 appears to collapse into 0 itself. This visualizes a derivative of 0, where the local behavior looks like multiplying the entire number line by 0 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This is determined by the limiting behavior as you zoom in infinitely closer <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **At negative inputs:** For example, around negative 2, inputs not only get stretched out but also get flipped around. The action on such a neighborhood increasingly resembles multiplication by -4 as you zoom in. This is what it looks like for a derivative to be negative <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

> [!NOTE] Local Behavior
> For derivatives, only the local behavior—what happens in a small range around a given input—is relevant <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## Application: Stability of Fixed Points in Infinite Fractions
The transformational view is particularly useful in solving problems related to fixed points of functions, such as those found in infinite continued fractions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

Consider the infinite fraction `1 + 1/(1 + 1/(1 + ...))` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
This expression can be evaluated by setting it equal to `x` and noticing that it contains a copy of itself, leading to the equation `x = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This means `x` is a fixed point of the function `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

Solving `x = 1 + 1/x` (which simplifies to `x^2 - x - 1 = 0`) yields two solutions:
1.  The golden ratio, phi (approximately 1.618) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  Negative 0.618, which is -1/phi <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

This raises the question of whether the infinite fraction could also equal the negative value. While the terms in the fraction are positive, if interpreted as a repeated application of the function `f(x) = 1 + 1/x` starting from some initial value, the outcome might not be immediately obvious <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Numerical Experiment
If you repeatedly plug any random number into `1 + 1/x` on a calculator, the result consistently converges to phi (1.618) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Even starting with a number very close to -0.618, it eventually moves away from it and converges to phi <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This suggests that phi is a "favored" fixed point.

### Graphical Approach to Stability (Spiderweb Diagram)
A common way to visualize repeated function application using graphs involves a "spiderweb diagram" <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Start with an input `x` on the x-axis, move vertically to the graph of `y=f(x)` to find the output `y`.
*   Move horizontally from `(x,y)` to the line `y=x`. This new point `(y,y)` provides the output as the new input.
*   Move vertically from `(y,y)` to the graph of `y=f(x)` again to find the next output.
*   Repeating this process creates a "spiderweb" pattern that either converges to a fixed point (where `f(x)=x`) or diverges away from it <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

While this method makes sense, it can be awkward to visualize repeated application, and determining convergence relies on understanding the slopes involved <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Transformational Approach to Stability
Viewing the function `f(x) = 1 + 1/x` as a transformation provides a more satisfying understanding of fixed point stability <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Repeated application:** Imagine dots representing sample points on the number line. Each application of the function moves these dots to their output positions. If this process is repeated, all dots quickly clump around 1.618 (phi) <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

*   **Stability at phi (1.618):** When zooming in on a neighborhood around phi, points in that region get *contracted* around phi during each application of the function <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This indicates that the derivative of `1 + 1/x` at phi has a magnitude less than 1 (approximately -0.38) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This repeated scrunching acts like a gravitational pull towards phi <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. Phi is therefore a **stable fixed point** <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

*   **Instability at -0.618:** In contrast, in the neighborhood of -0.618, the derivative of the function has a magnitude larger than 1 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. Points near this fixed point are *repelled* away from it, stretched by more than a factor of 2 in each iteration <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Although they also get flipped around (due to the negative derivative), the key for stability is the magnitude. This makes -0.618 an **unstable fixed point** <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

> [!NOTE] Fixed Point Stability
> The stability of a fixed point is determined by whether the magnitude of its derivative is bigger or smaller than 1 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. A stable fixed point tends to return to its original value if perturbed, while an unstable one moves away <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

This explains why phi consistently appears in numerical calculations, while its "little brother" never does <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

## Conclusion on Visual Intuition
While picturing an entire function through the transformational view can sometimes be clunky compared to graphs <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>, this perspective deserves more emphasis in [[introduction_to_calculus_series | introductory calculus courses]]. It helps make a student's understanding of the derivative more flexible <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. The true value of this perspective lies not just in single-variable calculus, but in how it prepares learners for more advanced topics <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. Developing [[converting_analytic_reasoning_to_geometric_intuition | geometric intuition]] alongside analytic reasoning is a key aspect of [[importance_of_visual_intuition_for_learning_linear_algebra | learning linear algebra]] and other advanced mathematical subjects.