---
title: Applications of polynomial rootfinding in computer graphics
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

Finding the roots of polynomials – the values where a polynomial equals zero – is a fundamental problem in mathematics with significant applications in engineering, particularly within [[applications_in_computer_graphics_and_robotics | computer graphics]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. These equations are "littered all over the place" in computer graphics <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Often, determining how a pixel should be colored on screen involves solving equations that utilize polynomials <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Examples in Computer Graphics

### Font Rendering (Bezier Curves)
When computers render text, fonts are typically defined not by pixel values, but as collections of polynomial curves known as Bezier curves <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. To display these curves, such as for stroke width or filling a region they enclose, every pixel on the screen needs to determine if it should be colored <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Determining stroke width, for instance, requires understanding the distance of a given pixel from the pure mathematical curve <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While sampling points on the curve is possible, a more efficient and precise method involves mathematics <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The square of the distance from a pixel to the curve is itself a polynomial, which is convenient to work with <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Finding the minimum of this distance function – and thus determining if a pixel should be filled – becomes a classic calculus problem <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This requires calculating the function's [[derivative_of_polynomial_functions_using_geometric_visualization | derivative]] (also a polynomial) and finding where it equals zero <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Therefore, a systematic way to find polynomial roots is crucial for displaying curves <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Pixar Animation Studios
The quadratic formula, used for finding roots of degree 2 polynomials, is extensively applied in computer graphics <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. A Pixar engineer estimated that the quadratic formula was used "easily multiple trillions of times" during the production of the movie *Coco*. This was due to the large number of lights in scenes and per-pixel calculations involving polynomially defined objects like spheres <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Methods for Finding Polynomial Roots

While direct formulas exist for quadratic, cubic, and quartic (degree 4) polynomials <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, no such general formula exists for polynomials of degree 5 or more <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This concept is known as the [[history_and_implications_of_unsolvability_in_higher_order_polynomials | unsolvability of the quintic]] <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### Iterative Algorithms
In practice, algorithms are used to approximate solutions to these higher-order equations with desired precision <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. A common and important algorithm is [[newtons_method_for_solving_polynomials | Newton's method]] (or Newton-Raphson method) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

#### Newton's Method
[[newtons_method_for_solving_polynomials | Newton's method]] starts with an initial guess ($x_0$) for a root <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. It then finds a linear approximation (tangent line) of the polynomial at that point and determines where this tangent line crosses the x-axis <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This intersection point becomes the next, improved guess <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. The process is repeated iteratively, leading closer to a true root <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The step size for each iteration is computed using the function's value and its [[derivative_of_polynomial_functions_using_geometric_visualization | derivative]] at the current guess <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

While effective, [[newtons_method_for_solving_polynomials | Newton's method]] can exhibit complex behavior, especially when initial guesses are far from a root or when extended to the complex plane <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This complexity leads to the formation of fractals, known as Newton's fractals, which illustrate the sensitivity of the method to initial conditions <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. Despite its visual intricacy, the underlying logic of using a linear approximation remains the same <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.