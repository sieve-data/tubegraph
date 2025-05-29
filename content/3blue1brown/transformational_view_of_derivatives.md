---
title: Transformational view of derivatives
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

The initial introduction to calculus often emphasizes [[Visualizing derivatives using graphs | graphical intuition]], where the derivative is primarily understood as the slope of a graph <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. However, this perspective can become a "conceptual hurdle" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a> when calculus is generalized beyond functions where inputs and outputs are simple numbers, making graphing impossible <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

The **transformational view** offers an alternative way to think about [[Understanding what a derivative is | derivatives]] that generalizes more seamlessly into advanced topics like multivariable calculus, complex analysis, and differential geometry <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. While the graphical intuition has its place, the transformational view can make a student's understanding of the derivative more flexible <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

## Graphical Intuition vs. Transformational View

### The Standard Visual: Slope of a Graph
In a standard calculus course, for a function that takes real numbers as inputs and outputs, the derivative is taught as giving the slope of its graph <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The derivative of a function is a new function that returns that slope for every input *x* <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

It is important to note that the "derivative as slope" idea is not the fundamental [[Derivative definitions and their relation to limits | definition of a derivative]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Rather, the derivative is more fundamentally about how sensitive a function is to tiny nudges around the input <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. The slope is merely one way to visualize this sensitivity <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### The Alternate Visual: Stretching and Squishing
The basic idea behind the transformational view is to conceptualize a function as mapping all input points on one number line to their corresponding outputs on a different number line <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. In this context, the derivative measures how much the input space gets stretched or squished in various regions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

If you zoom in around a specific input and observe a cluster of evenly spaced points, the derivative of the function at that input indicates how spread out or contracted those points become after the mapping <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

#### Examples using f(x) = x²
Consider the function f(x) = x², which maps 1 to 1, 2 to 4, 3 to 9, and so on <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

*   **Around Input 1:** A small cluster of points around the input 1 (where the output is also 1) gets stretched out by a factor of approximately 2 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. The closer you zoom in, the more this local behavior resembles multiplication by 2. This is what it means for the derivative of x² at x=1 to be 2 <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Around Input 3:** A neighborhood of points around the input 3 would get stretched out by a factor of 6. This means the derivative of x² at x=3 is 6 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Around Input 1/4:** A small region around 1/4 tends to get contracted by a factor of 1/2. This illustrates what it looks like for a derivative to be smaller than 1 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Around Input 0:** As you zoom in closer and closer (e.g., 100x, 1000x), a small neighborhood of points around 0 increasingly collapses into 0 itself <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This represents a derivative of 0, where the local behavior appears more and more like multiplying the entire number line by 0 <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This is about the limiting behavior as you zoom in <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Around Negative Inputs (e.g., -2):** Points in a neighborhood around -2 not only get stretched out but also get flipped around. Specifically, the action on such a neighborhood increasingly looks like multiplying by -4. This shows what it means for the derivative of a function to be negative <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. A downside of this view is that outputs from positive and negative inputs can collide, but for derivatives, only local behavior matters <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Application: Analyzing Fixed Points of Infinite Fractions

The transformational understanding of derivatives can be particularly useful for analyzing the stability of fixed points for functions, as demonstrated with the infinite fraction:
1 + 1 / (1 + 1 / (1 + 1 / (1 + ...))) <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### Finding Fixed Points
A common way to evaluate such an expression is to set it equal to *x* and observe that the full fraction appears within itself, leading to the equation *x* = 1 + 1/*x* <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This means finding the fixed points of the function f(x) = 1 + 1/x <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

There are two solutions (fixed points) for *x*:
1.  **[[golden_ratio | Phi]] (φ):** Approximately 1.618 <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  **Phi's little brother:** Approximately -0.618, which is equal to -1/φ <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### The Question of Convergence
The question arises: Is the infinite fraction also equal to phi's little brother? <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a> Symbolically, applying the function f(x) = 1 + 1/x repeatedly to any initial number *x*₀ represents the infinite fraction <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Numerically, if you start with almost any random number and repeatedly apply f(x) = 1 + 1/x, the result consistently converges to [[golden_ratio | Phi]] (1.618) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Even starting with a number very close to phi's little brother, the sequence eventually moves away and jumps back to phi <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### Graphical Interpretation of Iteration
The concept of repeatedly applying a function can be visualized using a graph by plotting the function f(x) and the line y=x. Starting with an input *x*₀ on the x-axis, you move vertically to the function's graph to find f(*x*₀), then horizontally to the y=x line to make this output the new input, and then vertically again to the function. This creates a "spiderweb" pattern <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. While this method can show convergence or divergence, it can be an "awkward way to think about repeatedly applying a function" <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>, and requires understanding the conditions related to slopes <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Transformational View of Fixed Point Stability
The transformational view offers a more intuitive understanding of why one fixed point is "favored" over the other <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
When visualizing the function f(x) = 1 + 1/x as a transformation of points on a number line, repeatedly applying the function shows sampled points quickly clumping around [[golden_ratio | Phi]] (1.618) <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

*   **Stable Fixed Point (Phi):** If you zoom in on a neighborhood around phi, points in that region get *contracted* towards phi during the mapping <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This occurs because the function's derivative at phi has a magnitude less than 1 (approximately -0.38) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Each repeated application scrunching the neighborhood makes it act like a "gravitational pull" towards phi <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Unstable Fixed Point (Phi's Little Brother):** In the neighborhood of phi's little brother, the derivative actually has a magnitude larger than 1 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This causes points near this fixed point to be *repelled* away from it and stretched by more than a factor of 2 in each iteration <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. (The derivative is also negative, causing a flip, but the magnitude is key for stability <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>).

#### Stability Rule
Mathematicians define a **stable fixed point** as one where small perturbations tend to return to the starting point <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. A useful fact is that the stability of a fixed point is determined by whether the magnitude of its derivative is **smaller or bigger than 1** <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This explains why phi consistently appears in numerical calculations, while phi's little brother does not <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

The interpretation of the infinite fraction's "value" depends on whether it's viewed as a limiting process (favoring phi) or a purely algebraic object with multiple solutions <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. However, the utility of the transformational view lies in its ability to clarify these behaviors.