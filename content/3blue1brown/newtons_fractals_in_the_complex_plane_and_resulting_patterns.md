---
title: Newtons fractals in the complex plane and resulting patterns
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

Newton's fractal refers to an infinite family of [[introduction_to_newtons_fractals_and_its_infinite_complexity | fractals]] that exhibit infinite detail regardless of how far one zooms in <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike many [[understanding_fractals_and_their_definitions | fractals]], this particular set of images has a more pragmatic origin, tied to an algorithm widely used in engineering <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Understanding the complexity of these fractals provides insight into the underlying algorithm <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## The Practical Need for Root Finding

The primary context for these fractals begins with the problem of finding when a polynomial equals zero, also known as finding its "roots" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This is a common requirement in various engineering fields, especially in computer graphics <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Application in Computer Graphics
In computer graphics, polynomials are fundamental <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. For instance, rendering text on a screen involves fonts defined by polynomial curves known as Bezier curves <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. To display these curves, each pixel on the screen must be determined whether it should be colored in <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This often involves calculating the distance from a pixel to the mathematical curve, which can be expressed as a polynomial function <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Finding the minimum of this distance function (or its square) is a classic calculus problem that requires finding where its derivative (also a polynomial) equals zero <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

> "To actually carry out this seemingly simple task of just displaying a curve, wouldn't it be nice if you had a systematic and general way to figure out when a given polynomial equals zero?" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>

Even in a movie like *Coco*, the quadratic formula was used "multiple trillions of times" for per-pixel calculations involving polynomially defined objects like spheres <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Limitations of Direct Formulas
While quadratic, cubic, and quartic polynomials have direct formulas for their roots <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, there is no analogous formula for polynomials of degree five or more <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This is known as the "unsolvability of the quintic" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. In practice, this limitation is overcome by using algorithms to approximate solutions <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Newton's Method: The Algorithm

The core algorithm leading to these fractals is Newton's method (also known as the Newton-Raphson method) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It's a common topic in calculus classes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Procedure for Real Numbers
1.  **Initial Guess (x0):** Start with a random guess for a root <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
2.  **Linear Approximation:** Draw a tangent line to the polynomial's graph at the current guess <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
3.  **New Guess (x1):** The point where this tangent line crosses the x-axis becomes the next, improved guess <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This step size is computed as `P(x) / P'(x)`, where `P(x)` is the polynomial value and `P'(x)` is its derivative (slope) <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
4.  **Iteration:** Repeat the process until the guess is extremely close to a true root <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Foibles of Newton's Method
While efficient when starting near a root, Newton's method can be unpredictable if the initial guess is far from a root <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. For example, a guess can bounce around a local minimum for many iterations before converging to a root, or even diverge <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## Newton's Fractals in the Complex Plane

The true complexity of Newton's method emerges when extended to the [[geometric_interpretation_of_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. According to the fundamental theorem of algebra, any polynomial will have roots in the complex plane <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Generating the Patterns
1.  **Complex Inputs:** Instead of real numbers, initial guesses are points in the [[geometric_interpretation_of_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
2.  **Iterative Process:** The same update rule `x_next = x_prev - P(x_prev) / P'(x_prev)` is applied <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
3.  **Convergence:** Most points quickly converge to one of the true roots <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>, but some "stragglers" bounce around <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>, especially those on the positive real number line for certain polynomials <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
4.  **Coloring:** Each initial guess (pixel) in the complex plane is colored based on which root its iteration sequence converges to <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

### Resulting Patterns and Complexity
The resulting image, when applied to every pixel in the plane and allowing for an arbitrarily large number of iterations, reveals a pattern with "endless complexity" <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. This means that a tiny adjustment to an initial guess can completely change which root it converges to <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, highlighting the unpredictability of the algorithm in certain regions <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

The patterns change depending on the roots of the polynomial being used <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Regions close to a root (where the linear approximation works well) always have the same color <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. All the chaos occurs at the boundaries between these colored regions <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

The number of steps allowed also affects the intricacy. Zero steps result in a Voronoi Diagram <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a> <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>, while more steps lead to a more intricate image that approaches the full fractal <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

### The Peculiar Boundary Property

A key characteristic of Newton's fractals (for polynomials with three or more roots) is a peculiar boundary property <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>:

> "The boundary of one color is the boundary of all of them." <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>

This means if you draw a small circle anywhere on the boundary of one colored region, no matter how tiny, it will always contain points belonging to *all* possible colors (i.e., points that converge to all distinct roots) <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. Conversely, a circle either contains all colors or just one, never just two <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This property explains why the boundary of Newton's fractal must be rough and cannot be smooth <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. It implies that at these sensitive boundary points, every possible root is accessible from within a small neighborhood <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

For the example shown, the [[fractal_dimension_and_its_application_in_nature | fractal dimension]] of the boundary is approximately 1.44 <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.

### Comparison: Quadratic vs. Higher-Degree Polynomials
While cubic and higher-degree polynomials generate these intricate fractal patterns <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>, quadratic polynomials with only two roots behave differently <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. In the quadratic case, each seed value simply tends towards whichever root it is closest to, resulting in a diagram with "decidedly more boring" straight-line boundaries (a Voronoi diagram) <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. This difference suggests that the complexity arises specifically when there are three or more roots <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

## Holomorphic Dynamics
The mathematical field that studies these types of questions and provides explanations for the bizarre boundary property is called holomorphic dynamics <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. Further exploration into this field can reveal surprising connections, such as with the Mandelbrot set, when considering if the iteration process can get trapped in a cycle <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.

Newton's fractal is an example of how even simple, centuries-old mathematical ideas can contain new, complex domains of relevance waiting to be discovered with modern tools <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.