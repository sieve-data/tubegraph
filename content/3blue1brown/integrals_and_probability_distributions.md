---
title: Integrals and probability distributions
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The effectiveness of mathematics in natural sciences is a recurring theme, exemplified by Eugene Wigner's paper, "The unreasonable effectiveness of mathematics in the natural sciences" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. A notable anecdote from his paper involves a statistician whose friend questions the appearance of pi in the formula for a Gaussian distribution, used for population trends <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. The core of this inquiry centers on understanding why a concept related to circles (pi) would be relevant to population statistics <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

The fundamental shape of the bell curve in a normal distribution, also known as a Gaussian distribution, is described by the function `e^(-x^2)` <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. The presence of pi in the full formula originates from the fact that the area underneath this `e^(-x^2)` curve works out to be the square root of pi <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. This value, the square root of pi, is then used to normalize the function by dividing it out, ensuring that the total area under the curve is one. This normalization is a crucial requirement for interpreting it as a [[Probability density function PDF | probability distribution]] <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

Our goal is to explain this area calculation and elucidate why this specific function, `e^(-x^2)`, holds such a significant place in statistics <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.

## Calculating the Area Under the Gaussian Curve

To find the area underneath a curve, the primary mathematical tool used is an [[Integrals and derivatives | integral]] <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. The notation for an integral represents the sum of the areas of infinitely many infinitesimally thin rectangles under the curve, where the height is `f(x)` and the width is `dx`, summed from negative infinity to infinity <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

Normally, computing an integral involves finding an antiderivative of the function <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. However, for `e^(-x^2)`, it is provably impossible to express its antiderivative using standard mathematical tools like polynomial expressions, trigonometric functions, or exponentials <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. This necessitates a clever trick to determine its area.

### The Clever Trick: Bumping Up a Dimension

The first step in this trick is to conceptualize the problem in a higher dimension <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. Instead of finding the area under a 2D bell curve `e^(-x^2)`, we seek the volume underneath a 3D bell surface defined by `e^-(x^2 + y^2)` <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

This function possesses a natural circular symmetry because `x^2 + y^2` is equivalent to `r^2` (the square of the distance from the origin) by the Pythagorean theorem <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>. Thus, the function can be expressed as `e^(-r^2)`, where `r` is the radius <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. This means all points on a given circle have the same output value, resulting in a rotational symmetry about the z-axis when graphed in three dimensions <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.

To compute this volume, we can integrate concentric thin cylindrical shells <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>. The volume of such a shell is approximately its circumference (`2 * pi * r`) times its height (`e^(-r^2)`) times its infinitesimal thickness (`dr`) <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>. Integrating this expression from `r = 0` to `r = infinity`:

`Volume = Integral(from 0 to infinity) [2 * pi * r * e^(-r^2) dr]` <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>

We can factor out `pi` from the integral:

`Volume = pi * Integral(from 0 to infinity) [2 * r * e^(-r^2) dr]` <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>

The term `2 * r * e^(-r^2)` *does* have an antiderivative: `-e^(-r^2)` <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>.
Evaluating this antiderivative from 0 to infinity:
As `r` approaches infinity, `-e^(-r^2)` approaches 0 <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.
At `r = 0`, `-e^(-0^2)` equals `-1` <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
So, `[0 - (-1)] = 1` <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>.

Thus, the volume under the bell surface is `pi * 1 = pi` <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>.

### Relating the 3D Volume Back to the 2D Area

We can also compute the volume under the surface by slicing it parallel to one of the axes, say the x-axis <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. The original function `e^-(x^2 + y^2)` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

If we take a slice at a specific `y` value, `e^(-y^2)` becomes a constant. The area of that slice is the integral of `e^(-x^2)` with respect to `x`, multiplied by this constant `e^(-y^2)` <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. Let `c` be the unknown area we are looking for: `c = Integral(from -infinity to infinity) [e^(-x^2) dx]` <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.

So, the area of a slice at `y` is `c * e^(-y^2)` <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>. To get the total volume, we integrate these slice areas over all `y` values:

`Volume = Integral(from -infinity to infinity) [c * e^(-y^2) dy]` <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>

Since `c` is a constant, we can factor it out:

`Volume = c * Integral(from -infinity to infinity) [e^(-y^2) dy]` <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>

Notice that the remaining integral is also equal to `c` (it's the same form as the integral for `x`) <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
Therefore, the volume is `c * c = c^2` <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>.

Since we previously found the volume to be `pi` <a class="yt-timestamp" data-t="08:59:00">[08:59:00]</a>, we can equate the two expressions for the volume:

`c^2 = pi` <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>

This implies that the mystery constant `c`, which is the area under the bell curve `e^(-x^2)`, must be the square root of pi (`sqrt(pi)`) <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.

## Why `e^(-x^2)`? The Herschel-Maxwell Derivation

While the integral trick explains *how* pi appears, it doesn't fully satisfy the statistician's friend's question about the *why* <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>. The deeper explanation comes from a derivation by John Herschel in 1850, and independently by James Clerk Maxwell years later <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.

Herschel showed that if a 2D [[Probability density function PDF | probability distribution]] (e.g., dartboard hits) satisfies two reasonable properties, it is inexorably forced into the shape `e^(-x^2 + y^2)` <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.

### Property 1: Radial Symmetry

The probability density around any point depends only on its distance from the origin, not its direction <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>. Mathematically, this means the 2D probability function `f2(x, y)` can be expressed as a single-variable function `f(r)` of the radius `r` (where `r = sqrt(x^2 + y^2)`) <a class="yt-timestamp" data-t="14:12:00">[14:12:00]</a>.

### Property 2: Independence of Coordinates

The x and y coordinates of each point are independent from each other <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>. This means the joint probability density function `f2(x, y)` can be factored into a product of two functions, one purely of `x` and one purely of `y`: `f2(x, y) = g(x) * h(y)` <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. Due to radial symmetry, `g` and `h` must be the same function, so `f2(x, y) = g(x) * g(y)` <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>.

Combining these properties leads to a functional equation:
`f(sqrt(x^2 + y^2)) = f(x) * f(y)` (assuming `f` and `g` are proportional by a factor of 1 for simplicity, which can be normalized later) <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>.

To solve this, a helper function `h(x) = f(sqrt(x))` is introduced <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>. This transforms the functional equation into:
`h(x^2 + y^2) = h(x^2) * h(y^2)` <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.
Letting `a = x^2` and `b = y^2` (so `a, b >= 0`), we get:
`h(a + b) = h(a) * h(b)` <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.

This equation implies that `h` must be an exponential function <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>. For example, `h(n) = h(1)^n` for whole numbers `n` <a class="yt-timestamp" data-t="18:51:00">[18:51:00]</a>. Extending this to rational and then continuous inputs (assuming continuity), `h(x)` must be of the form `b^x` for some base `b` <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. In calculus, it's convenient to write this as `e^(c*x)` for some constant `c` <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>.

Substituting back `h(x) = f(sqrt(x))`, we have `f(sqrt(x)) = e^(c*x)`.
Therefore, `f(z) = e^(c*z^2)` (by replacing `sqrt(x)` with `z`) <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.

This derivation forces the shape of the function to be `e^(c*r^2)` or `e^(c*(x^2 + y^2))` <a class="yt-timestamp" data-t="20:43:00">[20:43:00]</a>. For this to represent a valid [[Probability density function PDF | probability distribution]] (i.e., its volume doesn't blow up to infinity), the constant `c` in the exponent must be a negative number <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>. This naturally leads to the `e^(-x^2)` form, justifying its appearance from fundamental properties of probability distributions.

This perspective makes the integral trick less "out of the blue." The initial step of "bumping up a dimension" and using circular symmetry is precisely a way to leverage the defining properties of a Gaussian distribution as revealed by the Herschel-Maxwell derivation <a class="yt-timestamp" data-t="22:13:00">[22:13:00]</a>.

## Applications and Further Connections

This understanding also connects to the derivation of volumes of higher-dimensional spheres by applying this integration trick in even higher dimensions <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.

The connection between this derivation and the [[Central Limit Theorem]] (which explains why normal distributions arise in nature from the summation of many independent variables) represents a further, crucial step in fully explaining the ubiquitousness of the Gaussian distribution in statistics <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>.