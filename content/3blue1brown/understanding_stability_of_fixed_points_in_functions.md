---
title: Understanding stability of fixed points in functions
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

In calculus, the concept of a derivative is often introduced visually as the slope of a graph <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. While this graphical intuition is valuable for functions with simple numerical inputs and outputs, it can become less applicable when generalizing calculus to more complex domains, such as multivariable calculus or [[holomorphic_dynamics_and_complex_functions | complex analysis]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. An alternative "transformational view" of derivatives offers a more flexible perspective, viewing a function as mapping input points to output points <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This view helps understand how the input space gets stretched or squished, and it is particularly useful for analyzing the stability of fixed points in iterated functions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

## Derivatives: Graphical vs. Transformational View

Traditionally, the derivative is understood as the slope of a graph <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. However, a more fundamental understanding is that the derivative measures how sensitive a function is to tiny nudges around an input <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

The transformational view conceptualizes a function as mapping points from an input number line to a different output number line <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. In this context, the derivative at a specific input measures how much a small neighborhood of points around that input gets stretched or squished after the function's mapping <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. For example:
*   For the function $x^2$, zooming in around the input $x=1$ shows points stretching by a factor of 2, indicating a derivative of 2 at $x=1$ <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   Around $x=3$, points stretch by a factor of 6, meaning the derivative is 6 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   Around $x=1/4$, points contract by a factor of $1/2$, so the derivative is $1/2$ <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   Around $x=0$, points collapse towards $0$, indicating a derivative of $0$ <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   For negative inputs, like $x=-2$, points not only stretch (by a factor of 4) but also flip around, meaning the derivative is negative (e.g., -4) <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

The derivative represents the limiting behavior as you zoom in closer and closer to an input <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This perspective is crucial for understanding how functions behave under repeated application.

## Fixed Points and Function Iteration

A "fixed point" of a function $f(x)$ is a value $x$ such that $f(x) = x$ <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. These points are significant when considering functions applied repeatedly, i.e., iterating the function.

### Example: The Infinite Fraction

Consider the infinite fraction:
$1 + \frac{1}{1 + \frac{1}{1 + \dots}}$ <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>

This expression can be evaluated by setting it equal to $x$ and recognizing that the entire fraction appears within itself, leading to the equation $x = 1 + \frac{1}{x}$ <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This means we are looking for a fixed point of the function $f(x) = 1 + \frac{1}{x}$ <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

Solving $x = 1 + \frac{1}{x}$ (which simplifies to $x^2 - x - 1 = 0$) yields two solutions:
1.  The golden ratio, $\phi \approx 1.618$ <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  $\phi$'s "little brother," approximately $-0.618$, which is equal to $-1/\phi$ <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

The question then arises: if the infinite fraction represents a limiting process, which of these two fixed points does it approach? <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>

### Iterative Process

One way to interpret the infinite fraction is as the limit of a sequence generated by repeatedly applying the function $f(x) = 1 + \frac{1}{x}$ starting with an initial value <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   If you start with $x_0 = 1$, then $x_1 = 1 + 1/1 = 2$, $x_2 = 1 + 1/2 = 1.5$, and so on. This sequence approaches $\phi$ <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   Remarkably, if you start with *any* random number (even a negative one or one close to $-1/\phi$), repeatedly applying $f(x)$ will eventually converge to $\phi \approx 1.618$ <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The value $-1/\phi$ is a fixed point, but it's not a stable one; even if you start very close to it, the iterations "shy away" from it <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### Graphical Interpretation of Iteration (Spiderweb Diagram)

The traditional way to visualize function iteration involves a "spiderweb diagram" <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>:
1.  Start with an input $x_0$ on the x-axis.
2.  Move vertically to the graph of $y=f(x)$ to find the output $y_0 = f(x_0)$ <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
3.  Move horizontally from $y_0$ to the line $y=x$. This transfers the output value back to the x-axis as the new input $x_1 = y_0$ <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
4.  Repeat the process: move vertically from $x_1$ to $y=f(x)$, then horizontally to $y=x$, and so on <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
Fixed points are where the graph of $f(x)$ intersects the line $y=x$. The "spiderweb" path will either converge to a fixed point or diverge away from it, depending on the slope of $f(x)$ at the fixed point <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. While insightful, this method can be visually awkward <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

## Stability of Fixed Points with the Transformational View

The transformational view offers a more intuitive understanding of fixed point stability <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. When repeatedly applying a function like $f(x) = 1 + \frac{1}{x}$:
*   Points near $\phi$ (the golden ratio) tend to clump around it <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This happens because, under the function's mapping, points in a neighborhood around $\phi$ get *contracted* towards $\phi$ <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. This contraction implies that the magnitude of the function's derivative at $\phi$ is less than 1 (specifically, around -0.38 for $f(x) = 1 + 1/x$ at $\phi$) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This creates a "gravitational pull" towards $\phi$ <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

*   Conversely, points near $\phi$'s "little brother" ($-1/\phi$) are *repelled* away from it <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This is because the derivative at this fixed point has a magnitude greater than 1 (it stretches points by more than a factor of 2, and also flips them, as the derivative is negative) <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Stable vs. Unstable Fixed Points

*   A fixed point is considered **stable** if, when perturbed slightly, iterations of the function tend to return to that fixed point <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. This occurs when the **magnitude of the derivative** at the fixed point is **less than 1** ($|f'(x)| < 1$) <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Such fixed points act as attractors.
*   A fixed point is considered **unstable** if, when perturbed slightly, iterations of the function tend to move away from that fixed point <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. This occurs when the **magnitude of the derivative** at the fixed point is **greater than 1** ($|f'(x)| > 1$) <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Such fixed points act as repellors.

This principle explains why $\phi$ consistently appears in numerical iterations of $f(x) = 1 + \frac{1}{x}$, while $-1/\phi$ does not <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. The stability of fixed points is determined by the local stretching or squishing factor, which is precisely what the derivative in the transformational view describes.

This perspective enhances a student's understanding of derivatives, making it more flexible for advanced topics in mathematics beyond simple graphing <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.