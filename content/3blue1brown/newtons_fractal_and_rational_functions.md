---
title: Newtons Fractal and Rational Functions
videoId: LqbZpur38nw
---

From: [[3blue1brown]] <br/> 

Holomorphic dynamics is a field of mathematics that studies how functions behave when they are repeatedly applied, particularly functions that have complex number inputs and outputs and are differentiable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This field is closely related to iconic shapes like the Mandelbrot set and [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's fractal]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Holomorphic Functions and Dynamics

The term "holomorphic" refers to functions that take complex numbers as inputs and produce complex numbers as outputs, and for which a derivative can be taken <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. In this context, having a derivative means that when one zooms in on how the function behaves near a point, it appears roughly like scaling and rotating (multiplying by a complex constant) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This category includes many common functions such as polynomials, exponentials, and trigonometric functions <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

"Dynamics" refers to the process of repeatedly applying one of these functions: evaluating it on an input, then evaluating it again on the output, and so on <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The patterns emerging from these repeated applications can vary:
*   The sequence of points might get trapped in a cycle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   The sequence might approach a specific limiting point <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   The sequence might grow indefinitely and "fly off to infinity," which mathematicians consider a limit point <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   The sequence might exhibit no discernible pattern, behaving chaotically <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

Surprisingly, visualizing these different behaviors often results in intricate [[understanding_fractals_and_their_definitions | fractal patterns]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Newton's Method and Rational Functions

One example where these fractal patterns emerge is in [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's method]] for finding roots of a polynomial *p* <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The method iteratively applies the expression *x* - *p(x)* / *p'(x)*, where *p'(x)* is the derivative <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. When applied in the complex plane, starting with different initial seed values, each pixel of the plane can be colored based on which root that seed value converges to <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This process generates complex images with rough [[understanding_fractals_and_their_definitions | fractal boundaries]] between the colors <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The function iterated in [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's method]] (e.g., for *z*³ - 1) can be rewritten as one polynomial divided by another <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. These types of functions are called **rational functions** <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Mathematicians Pierre Fatou and Gaston Julia extensively studied the iteration of rational functions in the years following World War I, developing a rich theory without the aid of computers <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Parameter Space vs. Initial Value Space: Mandelbrot and Julia Sets

A widely popularized example of a rational function studied this way is *z*² + *c*, where *c* is a constant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. When the initial value *z* is fixed (e.g., *z* = 0) and the parameter *c* is varied, coloring points black if the iterative process remains bounded, the resulting image is the **Mandelbrot set** <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This is considered a **parameter space**, as the parameter *c* (which defines the function itself) is being changed <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. The Mandelbrot set's regions have specific meanings related to the dynamics: the largest cardioid corresponds to values of *c* where the process converges to a limit, and other circular regions correspond to cycles of specific periods <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

In contrast, [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's fractal]] is constructed by fixing a single function and associating each pixel with a different initial seed value <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. These types of images, where *c* is fixed and different initial *z* values are explored for *z*² + *c*, are often referred to as **[[Julia sets | Julia sets]]** or [[Julia fractals | Julia fractals]] <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. More precisely, the term [[Julia sets | Julia set]] refers to the boundaries of these regions, not the interior <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Analyzing Dynamical Stability

To understand the full dynamics, mathematicians analyze the "stability" of points in the system <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Fixed Points
A **fixed point** is a value *z* where applying the function *f(z)* results in *z* itself (*f(z) = z*) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. For functions derived from [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's method]], the roots of the polynomial *p* are fixed points <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. All rational functions possess fixed points, as finding them translates to finding the roots of a polynomial expression <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Fixed points can be:
*   **Attracting**: Nearby points are drawn towards the fixed point <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This occurs if the absolute value of the function's derivative at the fixed point is less than 1 <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. In [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's map]], roots are super-attracting fixed points, meaning the derivative is 0, causing rapid convergence <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Repelling**: Nearby points are pushed away from the fixed point <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. This occurs if the absolute value of the derivative is greater than 1 <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

### Cycles
Beyond fixed points, points can fall into **cycles** where they return to an initial value after multiple iterations (*f(f(z)) = z* for a two-cycle, or *fⁿ(z) = z* for an *n*-cycle) <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Explicit expressions for *n*-cycles become very complex, but for any rational map, periodic points (points that fall into a cycle) exist and their number grows exponentially with *n* <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

Most periodic points lie on the boundaries between colored regions and are unlikely to be hit in practice <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. What matters for attracting points is if a cycle is itself attracting, meaning a neighborhood of points around values in that cycle would be pulled in <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. For [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's method]], an attracting cycle means an initial guess could get trapped and never find a root <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. An example of an attracting cycle exists for the polynomial *z*³ - 2*z* + 2, where points around zero can get trapped in a cycle between zero and one <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

### Fatou's Theorem and the Mandelbrot Set in Newton's Method Parameter Space

A significant result by Fatou states that if a rational map has an attracting cycle, at least one of the values where the derivative of the iterated function equals zero must fall into that cycle <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This provides a way to test for attracting cycles by checking specific "critical points" where the derivative is zero <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

For cubic polynomials in [[newtons_fractals_in_the_complex_plane_and_resulting_patterns | Newton's method]], if an attracting cycle exists, the seed value located at the average (center of mass) of the three roots will fall into that attracting cycle <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. This "magical fact" simplifies the search for attracting cycles <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.

This principle allows for the visualization of cubic polynomials that have attracting cycles <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. By fixing two roots (e.g., at -1 and 1) and varying a third root (lambda), a parameter space can be created where each pixel corresponds to a unique cubic polynomial <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. Pixels are colored black if the corresponding polynomial has an attracting cycle (as determined by the behavior of the midpoint of its roots) <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. When zoomed in, this black region reveals a shape identical to the Mandelbrot set <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. This suggests that the Mandelbrot shape is not unique to the *z*² + *c* function but is a universal feature of certain parameter spaces in holomorphic dynamics <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

## Why Fractals? Julia and Fatou Sets

The intricate, non-smooth nature of these fractal boundaries can be explained by properties of [[Julia sets | Julia sets]] and [[Fatou sets | Fatou sets]] <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

*   **[[Fatou sets | Fatou set]]**: Contains points that eventually fall into some stable, predictable pattern (e.g., converging to a fixed point or cycle, or diverging to infinity) <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. A small disk around a point in the [[Fatou sets | Fatou set]] will eventually shrink as the process falls into stable behavior <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **[[Julia sets | Julia set]]**: Comprises all other points, which include the rough boundaries between regions of different stable behaviors <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. [[Julia sets | Julia sets]] contain repelling cycles and fixed points <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. Points in the [[Julia sets | Julia set]] tend to behave chaotically, meaning nearby neighbors will eventually exhibit qualitatively different behaviors <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.

A surprising result related to [[Julia sets | Julia sets]] is the "stuff-goes-everywhere principle" (a corollary to Montel's theorem) <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. This principle states that if a small disk is drawn around a point on the [[Julia sets | Julia set]], it will eventually expand to cover every single point on the complex plane (with at most two exceptions) as the iterative process plays out <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.

This principle explains the complex nature of the boundaries: if there are three or more attracting behaviors (colors) in the system, then any tiny circle around a boundary point must contain points that will eventually fall into *all* those attracting behaviors <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. This prevents the boundary from being smooth, as a smooth segment would allow for a small enough circle to touch only two colors <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. This direct link between the chaotic behavior of points in the [[Julia sets | Julia set]] and the resulting intricate [[understanding_fractals_and_their_definitions | fractal]] shapes is a key insight into why chaos and fractals often coincide in mathematics <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.