---
title: Understanding Newtons method and its applications
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

[[Newtons_fractal_and_its_relation_to_polynomials | Newton's method]] is an iterative [[numerical_methods_and_chaos_theory_in_differential_equations | numerical method]] primarily used to find successively better approximations to the roots (or zeroes) of a real-valued function. While often associated with intricate fractal shapes, its foundation is pragmatic, addressing the real-world need to solve polynomial equations [00:00:22]. The visual complexity of the resulting fractals reflects the algorithm's behavior, particularly when applied in the complex plane [00:00:33].

## The Problem: Finding Polynomial Roots

The starting point for Newton's method is the desire to find when a [[newtons_fractal_and_roots_of_polynomial_equations | polynomial]] equals zero, known as its roots [00:00:51]. While these can sometimes be eyeballed from a graph [00:00:57], computing them exactly poses a significant challenge [00:01:04].

### Real-World Relevance
Finding polynomial roots is a common problem in engineering [00:01:18]. In computer graphics, polynomials are frequently used to define shapes and curves [00:01:26]. For instance, text fonts are often defined by [[mathematical_concepts_related_to_newtons_fractal | Bezier curves]], which are themselves polynomial curves [00:01:47]. Displaying these curves on a screen requires determining which pixels to color [00:02:02].

One specific example is calculating the stroke width of a curve. This involves finding the distance between a given pixel and the mathematical curve [00:02:27]. The square of this distance can be expressed as a polynomial [00:03:01]. To find the minimum distance, which is crucial for determining if a pixel should be colored, one applies [[calculating_derivatives_and_their_applications | calculus]]: find the [[calculating_derivatives_and_their_applications | derivative]] of this polynomial (which is also a polynomial) and set it to zero [00:03:29]. This leads directly back to the problem of finding polynomial roots [00:03:47].

### Limitations of Exact Formulas
For quadratic functions (degree 2), the quadratic formula provides exact roots [00:04:12]. This formula is extensively used; for example, a Pixar engineer estimated it was used trillions of times in the production of the movie *Coco* [00:04:24]. Cubic (degree 3) and quartic (degree 4) polynomials also have formulas for their roots, though the quartic formula is rarely used in practice due to its complexity [00:04:48].

However, for polynomials of degree 5 or more (quintic), there is no general analogous formula that can express the roots using standard functions and coefficients [00:05:08]. This profound result is known as the [[mathematical_concepts_related_to_newtons_fractal | unsolvability of the quintic]] [00:05:27]. In practice, this limitation doesn't halt progress because algorithms exist to approximate solutions to these equations with high precision [00:05:36]. One such common algorithm is Newton's method [00:05:43].

## Newton's Method Explained (Real Numbers)

The procedure for Newton's method seems straightforward [00:05:49]:
1.  **Initial Guess**: Start with a random guess, `x0` [00:05:55].
2.  **Linear Approximation**: At `x0`, calculate the value of the polynomial `P(x0)` and the slope of the tangent line `P'(x0)` (its [[calculating_derivatives_and_their_applications | derivative]]) [00:06:16].
3.  **New Guess**: Determine where this tangent line crosses the x-axis [00:06:19]. This point, `x1`, becomes the improved guess [00:07:12]. The step size (difference between `x1` and `x0`) is calculated as `-P(x0) / P'(x0)` [00:07:08].
4.  **Iteration**: Repeat the process with `x1` to find `x2`, and so on [00:07:18].
5.  **Convergence**: With each iteration, the guesses typically get closer to a true root [00:07:36].

The formula for the next guess `x_(n+1)` is `x_n - P(x_n) / P'(x_n)` [00:07:12]. This formula makes intuitive sense: a large `P(x)` means a larger step is needed, while a large `P'(x)` (steep slope) means the step should be smaller [00:07:49].

This algorithm is also often called the [[mathematical_concepts_related_to_newtons_fractal | Newton-Rafson method]], as Joseph Rafson published a simpler version than Newton's original [00:08:12]. A simple exercise to understand it is to use it to approximate square roots [00:08:28].

## Foibles and Complexities (Real Numbers)

While [[newtons_fractal_and_roots_of_polynomial_equations | Newton's method]] converges quickly when starting near a root, it can behave unexpectedly when the initial guess is far off [00:08:45]. For example, if the function is shifted upwards, an initial guess might cause the sequence of guesses to bounce around a local minimum without converging to the true root [00:09:07]. This behavior highlights that the linear approximation in one region provides little information about roots in other, distant regions [00:09:19].

## Newton's Method in the Complex Plane

The true complexity of Newton's method emerges when considering roots in the complex plane [00:09:42].
According to the [[mathematical_concepts_related_to_newtons_fractal | Fundamental Theorem of Algebra]], any polynomial can be factored into terms corresponding to its complex roots [00:09:52]. Even if a polynomial only has one real root, it will have other complex roots [00:09:48].

While the visual meaning of tangent lines and graphs is lost in the complex plane, the mathematical formula for Newton's method still applies [00:10:16]. Starting with a complex initial guess, the same iterative rule can be applied to generate new complex guesses that hopefully converge to a complex root [00:10:29]. The logic remains the same: use a linear approximation to find a closer guess [00:10:49]. When observed, many initial guesses quickly converge to one of the true roots, but some "stragglers" bounce around chaotically, especially those on the real number line that mimic the earlier observed behavior [00:11:32].

## The Emergence of Fractals

To visualize the behavior across the complex plane, each pixel (representing an initial complex guess) can be colored based on which of the polynomial's roots it ultimately converges to [00:11:56]. When this process is applied to a fine grid of initial guesses and then rolled back to their starting positions, an infinitely intricate pattern emerges [00:12:13]. This shape, known as [[newtons_fractal_and_its_relation_to_polynomials | Newton's fractal]], possesses infinite detail regardless of how much one zooms in [00:12:46].

This fractal demonstrates extreme sensitivity to initial conditions: a minute adjustment to a starting point can completely change which root it converges to [00:13:04]. This "chaos" is particularly evident at the boundaries between the regions of different colors [00:13:58]. Changing the positions of the polynomial's roots dynamically alters the fractal pattern [00:13:37]. Regions immediately surrounding a root consistently converge to that root, forming solid colored areas where the linear approximation works without issue [00:13:45].

### Voronoi Diagrams and Iterations
If zero steps of Newton's method are taken, and each point is colored by the root it is closest to, the resulting diagram is called a [[mathematical_concepts_related_to_newtons_fractal | Voronoi Diagram]], characterized by straight-line boundaries [00:14:22]. As more steps of Newton's method are allowed, the patterns become increasingly intricate, gradually forming the true fractal, which is the limit as the number of iterations approaches infinity [00:14:50].

## The "Why" of Complexity

The extreme complexity arising from a simple iterative rule is surprising [00:15:40]. A common intuitive guess might be that each seed value simply tends towards the closest root, leading to a simple Voronoi diagram [00:15:50]. The complexity of Newton's fractal is not related to the [[mathematical_concepts_related_to_newtons_fractal | unsolvability of the quintic]] [00:16:12].

A key insight into this complexity lies in a peculiar property of the diagram: **the boundary of any single colored region is precisely the same set as the boundary of all other colored regions** [00:18:17].

### The Boundary Property
A point is defined as being on the boundary of a set if any arbitrarily small circle drawn around it contains points both inside and outside that set [00:18:36]. This implies that if a point is on the boundary of one color region, it must also be on the boundary of all other color regions present in that vicinity [00:19:05]. Consequently, it is impossible to find a small circle that contains points of only two colors, as that would mean a boundary exists between only two regions [00:19:30].

This property forces the fractal to exhibit "blobs on blobs" patterns [00:20:53], meaning the boundaries cannot be smooth or partially smooth, as any smooth segment would only touch two colors [00:21:10]. Instead, the boundary must consist entirely of "sharp corners" [00:21:18], maintaining its rough, infinite detail upon zooming in [00:21:26]. The [[mathematical_concepts_related_to_newtons_fractal | fractal dimension]] of such a boundary can be measured, e.g., around 1.44 [00:21:30].

From a practical perspective, this property means that if a region is sensitive such that initial guesses nearby converge to different roots, then *all* possible roots must be accessible from within that small neighborhood [00:21:48]. There's no in-between state where points tend to only a subset of the roots [00:22:08]. Watching clusters of points "explode outward" during iteration provides intuition for this chaotic behavior [00:22:16].

### Quadratic Polynomials are Different
This boundary property also explains why quadratic polynomials (with only two roots) behave differently [00:22:48]. With only two colors, a smooth boundary is permissible because it only needs to touch two colors [00:22:51]. While a fractal boundary between two colors is possible, Newton's method for quadratics yields a smooth boundary (a straight line) [00:23:01]. The transition from two to three roots (or more) marks a fundamental shift where this peculiar boundary condition comes into play [00:23:32].

The deeper mathematical reasons for this boundary property belong to the field of [[mathematical_concepts_related_to_newtons_fractal | holomorphic dynamics]] [00:23:22].

## Legacy and Future Questions

It is noteworthy that while the fractal is named "Newton's fractal," Isaac Newton himself could not have conceived of or visualized these intricate patterns [00:23:38]. This highlights a common phenomenon in mathematics where initial "simple ideas," even centuries old, hold within them new angles and domains of relevance that are discovered much later [00:24:10].

For example, asking if Newton's method iterations can ever get trapped in a cycle leads to surprising connections with the Mandelbrot set, a topic explored further in subsequent discussions [00:24:46]. This suggests that many more facts about seemingly "old news" mathematical concepts remain undiscovered, waiting for new questions to be asked [00:24:28].