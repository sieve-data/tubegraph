---
title: Herschel Maxwells derivation and its impact on understanding Gaussian distribution
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The apparent "unreasonable effectiveness of mathematics in the natural sciences," a phrase coined by physicist Eugene Wigner, often leads to curious questions, particularly concerning the prevalence of concepts like pi in seemingly unrelated fields such as population trends <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A story illustrates this point: a statistician explaining the Gaussian distribution to a former classmate, who became incredulous upon learning that the constant pi, related to circles, was part of the formula for population trends <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This article explores a derivation that sheds light on why pi appears in the [[connection_between_gaussian_distribution_and_probability | Gaussian distribution]] and the fundamental properties of this function.

## The Mystery of Pi in the Gaussian Formula

The basic function describing the bell curve shape of a [[connection_between_gaussian_distribution_and_probability | Gaussian distribution]] (also called a normal distribution) is `e^(-x^2)` <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. Pi appears in the final formula because the area underneath this curve works out to be the square root of pi <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. To interpret the curve as a [[probability_density_and_distribution | probability distribution]], its total area must be one, necessitating a division by the square root of pi <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

### The Classic Proof: Integrating `e^(-x^2)`

Finding the area under a curve typically involves an integral <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. However, for the function `e^(-x^2)`, it is provably impossible to find an antiderivative using standard mathematical tools (polynomials, trigonometric functions, exponentials, etc.) <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. This requires a clever approach:

1.  **Bumping to Higher Dimensions**: Instead of finding the area under the 1D bell curve, the trick is to ask for the volume underneath a 2D bell surface defined by `e^-(x^2 + y^2)` <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. This function takes two inputs, `x` and `y`, and its value depends on the distance `r` from the origin (`r^2 = x^2 + y^2`), giving it a circular symmetry <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
2.  **Integration in Polar Coordinates**: By respecting the circular symmetry, the volume can be computed by summing up thin cylindrical shells <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. The area of a cylindrical shell is its circumference (`2πr`) times its height (`e^(-r^2)`), multiplied by a thickness `dr` <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. Integrating `2πr * e^(-r^2) dr` from `0` to `infinity` reveals that the volume underneath this bell surface is exactly `π` <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>. The `2r` term inside the integral allows for an antiderivative (`-e^(-r^2)`) to be found <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
3.  **Integration by Slicing**: Alternatively, the volume can be thought of as chopping the surface into slices parallel to the axes <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. The function `e^-(x^2 + y^2)` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. This means each slice (e.g., `y = constant`) is essentially the 1D bell curve `e^(-x^2)` scaled by `e^(-y^2)`. If `c` is the unknown area of the 1D `e^(-x^2)` curve, then the area of a slice at a given `y` is `c * e^(-y^2)` <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. Integrating these slice areas from `y = -infinity` to `infinity` yields `c * integral(e^(-y^2) dy)`, which simplifies to `c * c`, or `c^2` <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.
4.  **The Conclusion**: Since both methods calculate the same volume, `c^2` must equal `π`. Therefore, the area `c` underneath the 1D bell curve `e^(-x^2)` is `sqrt(π)` <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.

While elegant, this proof feels somewhat like a "trick" and doesn't immediately explain why circles relate to statistics <a class="yt-timestamp" data-t="12:14:00">[12:14:00]</a>.

## The Herschel-Maxwell Derivation

John Herschel, a multifaceted scientist of the 19th century, offered an elegant derivation for the [[connection_between_gaussian_distribution_and_probability | Gaussian distribution]] in 1850 <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. His setup models a probability distribution in two-dimensional space, such as dartboard hits <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>. Herschel showed that if this distribution satisfies two reasonable properties, it is inexorably forced into the `e^-(x^2+y^2)` shape <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.

### Herschel's Two Properties:

1.  **Radial Symmetry**: The probability density around each point depends *only* on its distance from the origin, not its direction <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>. Mathematically, this means the 2D probability function `f2(x, y)` can be expressed as a single-variable function `f(r)` of the radius `r = sqrt(x^2 + y^2)` <a class="yt-timestamp" data-t="14:12:00">[14:12:00]</a>.
2.  **Independence of Coordinates**: The `x` and `y` coordinates of each point are independent from each other <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>. This implies that the 2D probability function can be factored into two separate 1D functions: `f2(x, y) = g(x) * h(y)` <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. Due to radial symmetry, the behavior along each axis should be the same, so `h(y)` must be the same function `g(y)`, leading to `f2(x, y) = g(x) * g(y)` <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>.

Combining these two properties, with an assumption that `f` and `g` are proportional (which can be accounted for by normalization later), leads to the functional equation: `f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>.

### Solving the Functional Equation

To solve `f(sqrt(x^2 + y^2)) = f(x) * f(y)`, a helper function `h(x) = f(sqrt(x))` is introduced <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>. This transforms the equation into `h(x+y) = h(x) * h(y)` <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.

This specific functional equation forces `h(x)` to be an exponential function <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>. For any whole number `n`, `h(n) = h(1)^n`. This extends to rational inputs `p/q`, where `h(p/q) = h(1)^(p/q)`. Assuming the function is continuous, this forces `h(x)` to be of the form `b^x` for some base `b`, or more commonly, `e^(cx)` for some constant `c` <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a>.

Translating back, `f(x)` must therefore be of the form `e^(c*x^2)` <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>. For the function to be normalizable as a [[probability_density_and_distribution | probability distribution]] (i.e., its area does not blow up to infinity), the constant `c` in the exponent must be a negative number <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.

### Impact and Connections

Ten years after Herschel, [[Maxwells equations and electromagnetic waves | James Clerk Maxwell]] independently arrived at the same derivation while working on statistical mechanics to describe the distribution of velocities of molecules in a gas <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>.

This derivation offers a profound insight: if a multi-dimensional probability distribution is defined by radial symmetry and independent coordinates, it *must* take the form of a Gaussian function <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. The appearance of pi in the integral of this function becomes less surprising because circular symmetry is inherent to its defining properties <a class="yt-timestamp" data-t="21:59:00">[21:59:00]</a>. The "trick" of bumping the integration problem to higher dimensions is, in fact, a direct application of these defining properties, making the solution feel more inevitable than arbitrary <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>.

This explanation helps satisfy the statistician's friend's question by showing how the fundamental geometric properties of a distribution naturally lead to a function that involves pi <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>. However, it still doesn't fully connect to how a normal distribution arises from the [[assumptions and limitations of the Central Limit Theorem | Central Limit Theorem]], which is about adding many independent variables rather than spatial properties <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>. This further connection is a topic for subsequent discussion <a class="yt-timestamp" data-t="23:42:00">[23:42:00]</a>.

***

> [!NOTE] Higher Dimensional Spheres
> This integration trick, when applied in higher dimensions, can be used to derive the formulas for the volumes of higher-dimensional spheres <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.