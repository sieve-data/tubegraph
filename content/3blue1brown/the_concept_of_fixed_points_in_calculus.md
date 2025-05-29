---
title: The Concept of Fixed Points in Calculus
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

The study of [[fundamental_concepts_of_calculus | calculus]] involves various concepts, including [[introduction_to_derivatives_and_calculus_concepts | derivatives]] and integrals. While initial [[visual_intuition_in_calculus | visual intuition]] in [[fundamental_concepts_of_calculus | calculus]] is often based on graphs <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>, this perspective can become limited when generalizing [[fundamental_concepts_of_calculus | calculus]] beyond functions with simple numerical inputs and outputs <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>. A deeper understanding, particularly for advanced topics like [[multivariable_calculus_and_complex_analysis | multivariable calculus]] and [[multivariable_calculus_and_complex_analysis | complex analysis]], can be achieved through a "transformational view" of [[introduction_to_derivatives_and_calculus_concepts | derivatives]] <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This perspective is particularly helpful for understanding fixed points and their stability.

## What is a Fixed Point?

A fixed point of a function is an input value that, when put through the function, returns itself as the output <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>. If a function is denoted as `f(x)`, a fixed point `x` satisfies the equation `f(x) = x` <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>.

### Example: The Infinite Continued Fraction

Consider the infinite continued fraction: 1 + 1 / (1 + 1 / (1 + ...)) <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.
To find its value, one method is to set the entire expression equal to `x` <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. Since a copy of the expression appears within itself, we can write:
`x = 1 + 1/x` <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>
This equation means we are looking for the fixed points of the function `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.

Solving for `x`:
1.  Multiply by `x`: `x² = x + 1`
2.  Rearrange: `x² - x - 1 = 0`
Using the quadratic formula, the two solutions (fixed points) are:
*   The golden ratio, phi (approximately 1.618) <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>
*   Negative 1 divided by phi (approximately -0.618) <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>

## Repeated Application of Functions

When evaluating an infinite expression like the continued fraction, one common interpretation is to think of it as a [[introduction_to_limits_in_calculus | limiting]] process: starting with an initial value and repeatedly applying the function `f(x) = 1 + 1/x`, then observing what value the sequence approaches <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.

### Graphical Approach (Spiderweb Diagram)

Traditionally, repeated function application can be visualized using a graph:
1.  Start with an `x` input. Its `y` value is the output.
2.  To feed this output back into the function as a new input, move horizontally to the line `y = x`. This point's `x` coordinate now matches the previous output's `y` coordinate <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
3.  From `y = x`, move vertically to the function graph to find the next output <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.
4.  Repeat the process, creating a "spiderweb" pattern <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

> "Personally, I think this is kind of an awkward way to think about repeatedly applying a function... you kind of have to pause and think about it to remember which way to draw the lines." <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>

### Transformational View

An alternative, more intuitive [[visualization_in_calculus | visualization]] involves thinking of the function as mapping points from an input number line to an output number line <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. The [[introduction_to_derivatives and calculus concepts | derivative]] then indicates how much the input space gets "stretched or squished" in various regions <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.

When repeatedly applying a function in this view, you map the input points to outputs, then consider those outputs as the new inputs and map them again <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.

## Stability of Fixed Points

When observing the repeated application of `f(x) = 1 + 1/x`, numerical experimentation shows that regardless of the starting value (except for the negative fixed point itself), the sequence converges to the golden ratio (phi) <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>. The other fixed point, negative 0.618, is rarely seen in such numerical play <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>. This difference is explained by the stability of the fixed points, which is determined by the magnitude of the function's [[introduction_to_derivatives_and_calculus_concepts | derivative]] at that fixed point <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

### Derivative as Stretching/Squishing

In the transformational view, the [[introduction_to_derivatives_and_calculus_concepts | derivative]] at a given input measures how much a small neighborhood of points around that input is stretched or contracted after the function's mapping <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

*   If the magnitude of the [[introduction_to_derivatives_and_calculus_concepts | derivative]] at a fixed point is **less than 1**, points in the neighborhood get contracted. This creates a "gravitational pull" towards the fixed point <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. Such a point is called a **stable fixed point** <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>.
*   If the magnitude of the [[introduction_to_derivatives_and_calculus_concepts | derivative]] at a fixed point is **greater than 1**, points near the fixed point are repelled away from it <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. This is an **unstable fixed point** <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.

### Applying to the Example

For the function `f(x) = 1 + 1/x`, the derivative `f'(x) = -1/x²`.

*   **At phi (approx. 1.618)**:
    `f'(phi) = -1 / (phi)²` ≈ -1 / (1.618)² ≈ -0.38 <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>.
    Since `|-0.38| < 1`, phi is a **stable fixed point**. Each iteration "scrunches" the neighborhood around phi, pulling values closer to it <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>. This is why the infinite fraction converges to phi.

*   **At negative 0.618**:
    `f'(-0.618) = -1 / (-0.618)²` ≈ -1 / (0.38) ≈ -2.618 <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
    Since `|-2.618| > 1`, this is an **unstable fixed point**. Points near this fixed point are stretched and repelled away from it with each iteration <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>. The negative sign also indicates a flip in direction <a class="yt-timestamp" data-t="12:14:00">[12:14:00]</a>.

## Conclusion

The "transformational view" of [[introduction_to_derivatives_and_calculus_concepts | derivatives]], which conceptualizes them as measures of stretching or squishing in the input space, provides a powerful and intuitive understanding of fixed point stability <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>. While graphical [[visualization_in_calculus | visualizations]] are useful, this alternative perspective offers a more flexible foundation, especially as one progresses to more generalized and complex topics in [[fundamental_concepts_of_calculus | calculus]] <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.