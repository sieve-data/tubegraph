---
title: Newtons Method for solving polynomials
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

Newton's Method is a powerful algorithm used to find approximate solutions, or "roots," for equations, particularly polynomials. While the method itself appears innocent, its application to finding complex roots of polynomials gives rise to intricate, infinitely detailed [[Newtons Fractal and Rational Functions | fractal]] shapes known as Newton's fractals <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Understanding these fractals provides insight into the algorithm's behavior and unpredictability <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## The Problem: Finding Polynomial Roots

A fundamental problem in mathematics and engineering is determining when a [[generating_functions_and_polynomials | polynomial]] equals zero <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These points are called the "roots" of the polynomial <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Practical Applications
While seemingly abstract, finding polynomial roots is crucial in many engineering fields <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. One significant area is [[applications_of_polynomial_rootfinding_in_computer_graphics | computer graphics]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:
*   **Pixel Coloring**: Determining how a pixel should be colored often involves solving equations that use polynomials <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Font Rendering**: Digital fonts are typically defined by [[generating_functions_and_polynomials | polynomial]] curves, specifically [[generating_functions_and_polynomials | Bezier curves]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. To display these on a screen, each pixel must be evaluated to see if it should be colored in <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   **Stroke Width**: Calculating the distance of a pixel from a mathematical curve (which has zero width) is often required <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The square of this distance can be expressed as a [[generating_functions_and_polynomials | polynomial]] <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Finding the minimum of this distance (and thus whether a pixel is within the stroke) involves taking its derivative (another [[generating_functions_and_polynomials | polynomial]]) and finding where it equals zero <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Limitations of Exact Formulas
For lower-degree polynomials, exact formulas exist:
*   **Quadratic Formula**: Solves degree 2 polynomials (e.g., $ax^2 + bx + c = 0$) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This formula is used trillions of times in [[applications_of_polynomial_rootfinding_in_computer_graphics | computer graphics]] for complex scenes, such as in the movie *Coco* <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Cubic Formula**: Solves degree 3 polynomials <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Quartic Formula**: Solves degree 4 polynomials, but is too complex for practical use <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

However, for polynomials of degree 5 or higher (quintic and above), there is no general algebraic formula that can express their roots using standard functions (addition, subtraction, multiplication, division, and root extraction) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This is known as the "unsolvability of the quintic" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This limitation necessitates the use of approximation algorithms <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, of which Newton's Method is a common example <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Newton's Method Explained (Real Numbers)

Newton's Method is an iterative numerical technique for finding increasingly better approximations to the roots of a real-valued function.

### The Algorithm
The process begins with an initial guess, $x_0$ <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Since $P(x_0)$ is likely not zero, the goal is to improve this guess <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
1.  **Linear Approximation**: At $x_0$, a tangent line to the polynomial's graph $P(x)$ is drawn <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This tangent line serves as a linear approximation of the function around $x_0$.
2.  **Next Guess**: The point where this tangent line crosses the x-axis is taken as the next, improved guess, $x_1$ <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The assumption is that if the tangent line is a good approximation, its root will be closer to the true root of $P(x)$ <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
3.  **Iteration**: This process is repeated with $x_1$ to find $x_2$, and so on, until the guesses converge to a root with the desired precision <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### The Formula
The slope of the tangent line at $x_0$ is given by the derivative of the polynomial, $P'(x_0)$ <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Using the rise-over-run concept for the slope:
$P'(x_0) = \frac{P(x_0) - 0}{\text{step size}}$ <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

Rearranging for the step size, we get:
$\text{step size} = \frac{P(x_0)}{P'(x_0)}$ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>

The next guess, $x_1$, is then calculated as:
$x_1 = x_0 - \frac{P(x_0)}{P'(x_0)}$ <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>

This generalizes to the iterative update rule:
$x_{n+1} = x_n - \frac{P(x_n)}{P'(x_n)}$

### Intuition Behind the Formula
*   If $P(x)$ is large (graph is high), a bigger step is needed to reach the x-axis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   If $P'(x)$ is large (graph is steep), the step size should be smaller, as the function quickly approaches the x-axis <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### History
This method is also known as the Newton-Raphson method, as Joseph Raphson published a simpler version than Newton's original formulation <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. It is a common topic in [[numerical_methods_for_solving_differential_equations | calculus]] classes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a> and can be used to approximate square roots <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### Limitations in Real Numbers
While generally effective when starting near a root, Newton's Method can exhibit "foibles" if the initial guess is far from a root <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. For example, the sequence of guesses might bounce around a local minimum above the x-axis, providing no useful information about a distant true root <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Convergence to the root only occurs by chance if a new guess happens to fall sufficiently close to it <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Newton's Method in the Complex Plane

The true complexity and fascinating behavior of Newton's Method emerge when applied to finding roots in the complex plane <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Fundamental Theorem of Algebra
A key concept in complex numbers is the [[eulers_formula | Fundamental Theorem of Algebra]], which states that any non-constant [[generating_functions_and_polynomials | polynomial]] with complex coefficients has at least one complex root. More specifically, a [[generating_functions_and_polynomials | polynomial]] of degree $n$ will always have exactly $n$ complex roots (counting multiplicity) <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Applying the Formula
Even though the visual interpretation of tangent lines and graphs doesn't apply to complex inputs and outputs, the iterative formula for Newton's Method remains valid in the complex plane <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>:
$z_{n+1} = z_n - \frac{P(z_n)}{P'(z_n)}$
where $z$ is a complex number. The underlying logic of using a linear approximation to find the next guess still holds <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

When many different initial complex guesses are simultaneously tracked, most quickly converge to one of the polynomial's roots <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. However, some "stragglers" spend a while bouncing around, similar to the real-number case <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

## The Newton's Fractal

To visualize the behavior of Newton's Method in the complex plane, each initial guess (represented as a pixel) is colored based on which of the polynomial's roots it ultimately converges to <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. When this is done for every pixel in a region of the complex plane, the resulting image is a Newton's fractal <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

### Characteristics
*   **Infinite Detail**: Newton's fractals exhibit infinite detail, meaning no matter how far one zooms in, new intricate patterns and complexity are revealed <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   **Sensitivity to Initial Conditions**: The fractal illustrates regions where a minuscule change in the initial guess can lead to convergence to a completely different root <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This highlights the inherent unpredictability of the root-finding algorithm in certain areas of the complex plane <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Root Influence**: Regions immediately surrounding a specific root will consistently lead to that root, as the linear approximation works well in that vicinity <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   **Variability**: The fractal pattern changes depending on the specific [[generating_functions_and_polynomials | polynomial]] and the placement of its roots <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. However, the fractal boundaries are consistently present regardless of root placement for polynomials of degree 3 or higher <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
*   **Iterations**: The intricacy of the fractal increases with the number of iterations of Newton's Method applied <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The "true" fractal is the limit as an arbitrarily large number of iterations is allowed <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
    *   **Voronoi Diagram**: If zero steps of Newton's Method are taken, and pixels are colored based on their closest root, the result is a Voronoi diagram, which has straight-line boundaries and lacks fractal complexity <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

## Why the Complexity? The Boundary Property

The unexpected complexity of Newton's fractals, particularly the endlessly complicated boundaries between convergence regions, stems from a peculiar mathematical property <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.

### The Shared Boundary Property
For polynomials with three or more roots, a surprising property emerges: the boundary of any one colored region (representing convergence to a specific root) is precisely the same set as the boundary of all other colored regions <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

Mathematically, a point is on the "boundary" of a set if any arbitrarily small circle centered at that point contains points both inside and outside the set <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.
*   This property implies that if you draw any small circle on the complex plane, it either contains only points that converge to a single root (if it's in the interior of a region) or it contains points that converge to *all* possible roots (if it intersects the shared boundary) <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   Crucially, you should never be able to find a circle that contains points converging to *just two* of the colors/roots <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

### Implications for the Fractal Shape
This shared boundary property explains the fractal nature:
*   **No Smooth Boundaries**: If a boundary segment were smooth, it would only be touching two colors <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. Since the boundary must touch all colors (for 3+ roots), it must consist entirely of "sharp corners" and intricate, self-similar structures <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. This means the boundary remains rough at any zoom level <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.
*   **Unpredictability**: Near a "sensitive point" on this boundary, a slight adjustment to the initial guess means that every possible root is accessible within that small neighborhood <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **"Blobs on Blobs"**: The visual appearance of the fractal, with its nested "blobs on blobs" pattern, is a direct consequence of this property, as the method tries to "correct" boundaries to include all colors <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

### The Quadratic Case
Quadratic polynomials, with only two roots, behave differently <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. In this case, each initial guess typically tends towards whichever root it is closest to <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. The resulting diagram is much simpler, with a smooth boundary between the two regions, because the shared boundary property (touching *all* roots) is satisfied by simply touching the only two roots available <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>. The complexity only arises when jumping from two to three or more roots <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

The mathematical field that studies these kinds of questions is called holomorphic dynamics <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.

## Future Explorations

While known as "Newton's fractal," Isaac Newton himself had no knowledge of these complex images, as they require modern computational technology <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. This highlights how simple mathematical ideas, even centuries old, can contain hidden complexity and new domains of relevance waiting to be discovered <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.

Further questions about Newton's Method, such as whether the iterative process can ever get trapped in a cycle, lead to surprising connections with other famous fractals like the Mandelbrot set <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.