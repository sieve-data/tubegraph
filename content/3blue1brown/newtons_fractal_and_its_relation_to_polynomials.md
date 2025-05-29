---
title: Newtons fractal and its relation to polynomials
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

[[Newtons fractal and roots of polynomial equations | Newton's fractal]] is an infinite family of intricate shapes that possess infinite detail, revealing complexity no matter how far one zooms in <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While visually stunning, the story behind this fractal has a pragmatic origin, rooted in an algorithm used widely in engineering <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Understanding its underlying principles makes its complicated appearance more meaningful <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Challenge of Finding Polynomial Roots

The primary starting point for [[Newtons fractal and roots of polynomial equations | Newton's fractal]] is the problem of finding when a polynomial equals zero, also known as finding its roots <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. For a graphed polynomial, roots are the points where it crosses the x-axis <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### Practical Applications in Engineering
While seemingly an abstract mathematical question, finding polynomial roots is a common task in engineering <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. For example, in computer graphics, polynomials are ubiquitous <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. When a computer renders text, fonts are often defined by polynomial curves known as Bezier curves <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. To display these curves on a screen, pixels must be colored based on their proximity to the mathematical curve <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Determining this distance often involves solving a polynomial equation where the square of the distance is a polynomial <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Finding the minimum of this distance function, a classic calculus problem, requires finding when its derivative (also a polynomial) equals zero <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### The Limits of Algebraic Formulas
For quadratic functions (degree 2), the quadratic formula provides exact roots <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This formula was used trillions of times in the production of the movie *Coco* for per-pixel calculations involving polynomially defined objects <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Cubic (degree 3) and quartic (degree 4) polynomials also have formulas, though the quartic formula is rarely used due to its complexity <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

However, for polynomials of degree 5 or higher, there is no analogous general formula using standard functions to find the roots <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This is known as the unsolvability of the quintic <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Despite this, algorithms exist to approximate solutions to these equations with high precision <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Newton's Method: An Iterative Approach

[[Newtons fractal and roots of polynomial equations | Newton's method]], also known as the Newton-Raphson method, is a common algorithm for approximating polynomial roots <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### How the Algorithm Works
The method begins with an initial guess, `x0` <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Since the polynomial's output at `x0` is likely not zero, the idea is to find where a linear approximation (a tangent line) of the function at `x0` crosses the x-axis <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This new x-intercept becomes the next, improved guess (`x1`) <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

The step size for each new guess is calculated using the formula:
`step size = P(x) / P'(x)`
where `P(x)` is the polynomial's value at the current guess `x`, and `P'(x)` is its derivative (slope) at `x` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
The next guess, `x_new`, is `x_old - step size` <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
This process is repeated iteratively, with each new guess theoretically bringing the approximation closer to a true root <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

Newton's method converges quickly when the initial guess is close to a root <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. While Newton initially developed a version of this method, Joseph Raphson published a simpler form, leading to its dual name <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. It's a common topic in calculus classes and can be used to approximate square roots <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Limitations in the Real Plane
Despite its effectiveness, [[Newtons fractal and roots of polynomial equations | Newton's method]] can exhibit "foibles" if the initial guess is far from a root <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, a sequence of guesses might bounce around a local minimum of the function, unrelated to the actual root <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. The process only becomes productive if a subsequent guess happens to land closer to the root by chance <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Exploring Newton's Method in the Complex Plane

The true complexity of [[Newtons fractal and roots of polynomial equations | Newton's method]] emerges when applied to the complex plane <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The [[mathematical_concepts_related_to_newtons_fractal | Fundamental Theorem of Algebra]] states that any polynomial of degree 'n' will have 'n' roots if complex numbers are allowed <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

While the tangent line visualization of Newton's method doesn't apply directly to complex numbers, the underlying formula for iteration remains valid <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Starting with a complex initial guess, the same update rule is used to generate new guesses that hopefully converge to one of the polynomial's complex roots <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Visualizing Newton's Fractal

To generate [[Newtons fractal and roots of polynomial equations | Newton's fractal]], many different initial guesses are made across the complex plane <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. Each point in the plane is an initial guess, and [[Newtons fractal and roots of polynomial equations | Newton's method]] is applied to it <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. The point is then colored based on which of the polynomial's true roots it eventually converges to <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. When all points are colored and reset to their starting positions, the resulting image is [[Newtons fractal and roots of polynomial equations | Newton's fractal]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

![[Newton's Fractal Example.png]]

This [[visualization and characteristics of fractal patterns | visualization]] reveals shapes with "endless complexity" <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. Even slight adjustments to an initial seed value (e.g., by a millionth or trillionth) can completely change which root it converges to <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This highlights the inherent unpredictability and chaos of the root-finding algorithm in certain regions <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

The appearance of the fractal changes when the roots of the polynomial are altered <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Regions around a given root always share the same color, as points there are close enough for the method to work consistently <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. All the chaos occurs at the boundaries between these regions <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

The number of iterations used also influences the image <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>:
*   **Zero steps**: The image is a Voronoi diagram, where each point is colored based on which root it is initially closest to <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
*   **One or more steps**: As more iterations are allowed, the patterns become increasingly intricate, approaching the true [[Newtons fractal and roots of polynomial equations | fractal pattern]] which represents the limit of an arbitrarily large number of iterations <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

## The Peculiar Boundary Property

The complexity of [[Newtons fractal and roots of polynomial equations | Newton's fractal]], particularly its "endlessly complicated" nature <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>, stems from a peculiar property of its boundaries.

A point is considered to be on the boundary of a set if any arbitrarily small circle drawn around it contains points both inside and outside that set <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. For [[Newtons fractal and roots of polynomial equations | Newton's fractal]] with three or more roots, a surprising property is observed: the boundary of any one colored region (i.e., the set of points that tend to a particular root) is precisely the same set as the boundary of all other colored regions <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

This means that if a point is on the boundary between two colors, it must also be touching all other colors <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. One cannot find a small circle that contains just two of the colors without also containing all others <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. This "shared boundary" property necessitates an infinite level of detail, leading to a "blobs on blobs on blobs" pattern, because any attempt to draw a smooth boundary between only two colors would immediately violate the rule by leaving out a third <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This explains why the boundary must remain rough and never smooth, no matter how much one zooms in <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.

The [[fractal dimension and its implications | fractal dimension]] of such a boundary can be measured; for the cubic polynomial example, it is approximately 1.44 <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>. In practical terms, this property implies that near any "sensitive point" on the boundary, where initial guesses can lead to different roots, *every* possible root must be accessible from within that tiny neighborhood <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

### The Special Case of Quadratic Polynomials
Unlike polynomials with three or more roots, quadratic polynomials (with only two roots) produce a simpler, non-fractal boundary <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. In this case, each initial guess tends toward whichever root it is closest to, resulting in a diagram resembling a Voronoi diagram with a single straight-line boundary <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. The complexity of the [[Newtons fractal and roots of polynomial equations | fractal]] arises precisely when the number of roots jumps from two to three or more <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

The field of [[mathematical_concepts_related_to_newtons_fractal | holomorphic dynamics]] studies questions related to these complex dynamics and the reasons behind such bizarre boundary properties <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.

## Legacy and Future Discoveries
It is notable that [[Newtons fractal and roots of polynomial equations | Newton's fractal]] is named after Newton, despite him having no knowledge of its [[visualization and characteristics of fractal patterns | fractal patterns]] or the computational tools to explore them <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. This common phenomenon in mathematics reflects how even simple, centuries-old ideas can contain new angles or domains of relevance that await future discovery <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. Further exploration of [[Newtons fractal and roots of polynomial equations | Newton's method]], such as questions about cycles in the iteration process, reveals surprising connections, including with the [[Benoit Mandelbrot and the pragmatic origins of fractal geometry | Mandelbrot set]] <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.