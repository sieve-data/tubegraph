---
title: Graphical intuition versus transformational understanding in calculus
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

Learning [[introduction_to_calculus|calculus]] often involves a significant amount of hard work, memorizing formulas, and encountering moments of struggle alongside "aha" moments <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. A common approach to [[visualizing_mathematical_concepts|visualizing mathematical concepts]] in introductory courses relies heavily on graphical intuition <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. However, an alternative perspective, the [[transformational_view_of_derivatives|transformational view]], can greatly accelerate learning by offering a more generalized understanding <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Standard Graphical Intuition of Derivatives

In a typical [[introduction_to_calculus|calculus]] course, the primary visual intuitions are based on graphs <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For functions with numerical inputs and outputs, the derivative is commonly introduced as the slope of a graph <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This means the derivative of a function is a new function that returns the slope for every input `x` <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Similarly, the integral is often explained as a certain area under a graph <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

While the "derivative as slope" concept is useful for [[visualizing_derivatives_using_graphs|visualizing derivatives using graphs]], it's important not to consider it the fundamental definition of a derivative <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. More fundamentally, the derivative relates to how sensitive a function is to tiny nudges around the input <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. The slope is merely one way to conceptualize this sensitivity, relevant specifically to the graphical representation <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Limitations of Graphical Intuition

A rigid adherence to graphical intuition for fundamental concepts like derivatives can create a significant conceptual hurdle when generalizing [[calculus]] beyond functions whose inputs and outputs are simple numbers <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. In advanced topics such as multivariable [[calculus]], complex analysis, or differential geometry, it's not always possible to graph the function being analyzed <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Transformational View of Derivatives

An alternative [[visualizing_derivatives_beyond_graphs|visualizing derivatives beyond graphs]] is the [[transformational_view_of_derivatives|transformational view]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This perspective conceptualizes a function as mapping all input points on a number line to their corresponding outputs on a different number line <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

In this context, the derivative measures how much the input space gets stretched or squished in various regions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. If one zooms in on a specific input and observes evenly spaced points around it, the derivative of the function at that input indicates how spread out or contracted those points become after the mapping <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Examples of the Transformational View

Consider the function `x^2`:
*   **Around input 1**: A small cluster of points around input 1 gets stretched out, roughly by a factor of 2. This signifies that the derivative of `x^2` at `x=1` is 2 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. The closer one zooms in, the more this local behavior resembles multiplication by 2 <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Around input 3**: Points near input 3 would be stretched out by a factor of 6, indicating the derivative is 6 at `x=3` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Around input 1/4**: A small region around input 1/4 gets contracted by a factor of 1/2, illustrating a derivative smaller than 1 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Around input 0**: As one zooms closer to 0, a small neighborhood of points around 0 increasingly appears to collapse into 0 itself. This is what it looks like for the derivative to be 0, as the local behavior resembles multiplying the entire number line by 0 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This is about the limiting behavior as one zooms in infinitely close <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Negative inputs (e.g., -2)**: Points in a neighborhood around negative 2 not only get stretched out but also get flipped around. This local action increasingly looks like multiplying by -4, which indicates a negative derivative <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

While thinking of entire functions as transformations can be clunky, for derivatives, only the local behavior around a given input matters <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## Application: Stability of Fixed Points in Infinite Fractions

The [[transformational_view_of_derivatives|transformational view]] can be particularly useful in understanding the stability of fixed points, as seen in the example of the infinite fraction `1 + 1/(1 + 1/(1 + ...))` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This expression can be represented as finding a fixed point `x` of the function `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

Algebraically, this function has two fixed points:
1.  The golden ratio, phi (approximately 1.618) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  Negative 1 divided by phi (approximately -0.618), sometimes referred to as phi's "little brother" <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

The question arises whether the infinite fraction could also equal the negative value <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. One way to interpret the infinite fraction is as a limiting process: starting with a constant (e.g., 1) and repeatedly applying the function `1 + 1/x` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Contrasting Graphical and Transformational Approaches

Traditionally, repeatedly applying a function can be visualized using a "spiderweb diagram" on a graph, by moving horizontally to the `y=x` line and then vertically to the function graph <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. This method can feel awkward, but the conditions for the spiderweb to narrow in on or propagate away from a fixed point relate to slopes <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

The [[transformational_view_of_derivatives|transformational view]] offers a more intuitive understanding <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. When repeatedly applying the function `1 + 1/x` in this view:
*   **Around phi (1.618)**: Points in a neighborhood around phi get contracted towards it during the mapping <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This occurs because the magnitude of the derivative of `1 + 1/x` at phi is less than 1 (approximately -0.38) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Each application "scrunches" the neighborhood smaller, acting like a gravitational pull <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This makes phi a **stable fixed point** <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   **Around phi's little brother (-0.618)**: The derivative at this point has a magnitude greater than 1 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. Points near this fixed point are repelled away from it, being stretched by more than a factor of 2 in each iteration (and also flipped due to the negative derivative) <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This makes it an **unstable fixed point** <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

The stability of a fixed point is determined by whether the magnitude of its derivative is greater or smaller than 1 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This explains why, when iteratively plugging numbers into a calculator, the process always converges to phi, regardless of the starting number (unless it's phi's little brother itself) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

This demonstrates how [[mathematical_intuition_and_counterintuitive_results|mathematical intuition]] derived from the transformational view provides a clear explanation for why one fixed point is numerically favored over the other, even if both are algebraically valid solutions <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## Conclusion

While [[visualizing_derivatives_using_graphs|graphical intuition]] is valuable, the [[transformational_view_of_derivatives|transformational view]] of derivatives, focusing on stretching and squishing of input spaces, offers a more flexible understanding that generalizes seamlessly into advanced [[calculus]] topics <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. It deserves more attention in [[introduction_to_calculus|introductory calculus]] courses because it enhances a student's [[intuition_behind_calculus_rules|understanding of the derivative]] and better prepares them for future concepts <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.