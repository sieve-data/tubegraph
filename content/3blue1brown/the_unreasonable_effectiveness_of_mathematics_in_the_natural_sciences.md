---
title: The unreasonable effectiveness of mathematics in the natural sciences
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The phrase "the unreasonable effectiveness of mathematics in the natural sciences" was the title of a paper by physicist Eugene Wigner <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Wigner's paper opens with an anecdote about two high school classmates <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. One became a statistician working on population trends <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The statistician showed a reprint that started with the Gaussian distribution, explaining the symbols for actual and average population <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The former classmate was incredulous, asking, "How can you know that?" <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a> When the statistician identified a symbol as pi, the ratio of a circle's circumference to its diameter, the classmate retorted, "Surely the population has nothing to do with the circumference of a circle" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

In his paper, Wigner discusses the broader phenomenon of pure mathematical concepts finding applications unexpectedly beyond their definitions <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The central question posed by the statistician's friend is why circles relate to population statistics <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Pi in the Normal Distribution

The reason pi appears in the formula for a normal (or Gaussian) distribution lies in the area underneath its characteristic bell curve <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. When parameters and constants are stripped away, the basic function describing the bell curve is `e^(-x^2)` <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The area under this curve works out to be the square root of pi <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This requires dividing by the square root of pi to normalize the area to one, a requirement for it to be interpreted as a probability distribution <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The origin of pi in the full formula stems from this area <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The challenge is to explain not only this area but also why the function `e^(-x^2)` is so special in statistics, given that many formulas could produce a similar bell shape <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The goal is to connect the proof for pi's appearance with the [[central_limit_theorem | central limit theorem]], which explains when a normal distribution arises in nature <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### The Classic Proof for the Area Under the Bell Curve

To find the area under a curve, the tool used is an integral <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The area under `e^(-x^2)` from negative infinity to infinity is represented by an integral <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. However, for this specific function, it is provably impossible to find an antiderivative using usual mathematical tools like polynomial expressions, trig functions, or exponentials <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. Thus, calculating this area requires a clever trick <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

The trick begins by "bumping things up one dimension" <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Instead of finding the area under a bell curve (a 2D problem), the problem becomes finding the volume underneath a bell surface (a 3D problem) <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This higher-dimensional function is defined as `e^(-(x^2 + y^2))` where `r = sqrt(x^2 + y^2)` is the distance from the origin <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This function exhibits circular symmetry, meaning all inputs on a given circle have the same output <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

To compute the volume under this surface, its rotational symmetry is utilized by imagining integrating thin cylindrical shells <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The volume of a cylindrical shell with radius `r` and thickness `dr` is its circumference (`2 * pi * r`) times its height (`e^(-r^2)`) times `dr` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Integrating this expression from `r=0` to `infinity`:

```
Volume = ∫[0,∞] 2πr * e^(-r^2) dr
```
By factoring `pi` out and noting that `2r * e^(-r^2)` has an antiderivative of `-e^(-r^2)` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, the integral evaluates to `1` <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Thus, the volume underneath this bell surface is `pi` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. The appearance of pi here is not surprising due to the surface's intrinsic circular symmetry <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

Next, the volume is analyzed in a second way, by chopping it into slices parallel to one of the axes, e.g., the x-axis <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Each slice, like `y=0`, looks like a bell curve (`e^(-x^2)`) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This is because the function `e^(-(x^2 + y^2))` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. If the area of the slice `y=0` is `c` (the mystery constant we seek) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, then any other slice `y=k` will have an area of `c * e^(-k^2)` <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

The total volume can then be expressed as the integral of the areas of these slices multiplied by a thickness `dy`:

```
Volume = ∫[-∞,∞] (c * e^(-y^2)) dy
```
Factoring out `c`, the integral becomes `c * ∫[-∞,∞] e^(-y^2) dy` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. The remaining integral is exactly the mystery constant `c` <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. Therefore, the volume under the bell surface is `c^2` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

Since we previously found the volume to be `pi` <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, it follows that `c^2 = pi`, and thus `c = sqrt(pi)` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. This elegantly proves that the area under `e^(-x^2)` is the square root of pi <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

While beautiful, this proof can feel like a trick and doesn't fully answer why circles relate to population statistics <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Herschel-Maxwell Derivation of the Gaussian Distribution

In 1850, John Herschel, a 19th-century mathematician, scientist, and inventor, provided an elegant derivation for the Gaussian distribution <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. His setup imagines describing a probability distribution in two-dimensional space, such as the probability density for hits on a dartboard <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

Herschel showed that if this distribution satisfies two reasonable properties, the form of the function is surprisingly constrained to `e^(-(x^2 + y^2))` (up to a scaling constant) <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

The two properties are:
1.  **Radial Symmetry:** The probability density around each point depends only on its distance from the origin (`r`), not its direction <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. Mathematically, `f2(x, y)` (the 2D probability distribution function) can be expressed as `f(r)`, where `r = sqrt(x^2 + y^2)` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
2.  **Independence of Coordinates:** The x and y coordinates of each point are independent <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This means the probability density `f2(x, y)` can be factored into a function purely of `x`, `g(x)`, and a function purely of `y`, `h(y)` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Due to radial symmetry, `g` and `h` must be the same function, so `f2(x,y) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

Combining these properties:
Since `f2(x, y) = f(r)` and `f2(x, y) = g(x) * g(y)`, and `f` and `g` are basically the same function (up to a constant) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>, we can derive a functional equation:
`f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

To solve this functional equation, a helper function `h(x) = f(sqrt(x))` is introduced <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. This means `h(x^2) = f(x)` <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. The key property for `f` then translates to `h(x + y) = h(x) * h(y)` for arbitrary positive numbers `x` and `y` <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. This type of equation implies that `h(x)` must be an exponential function, `b^x` for some base `b` <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. For mathematical convenience in calculus, this is written as `e^(c*x)` for some constant `c` <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.

Substituting back to `f(x)`, we find that `f(x)` must look like `e^(c*x^2)` <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. For the function to represent a probability distribution that can be normalized (i.e., its integral doesn't blow up to infinity), the constant `c` in the exponent must be a negative number <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>. This constant determines the spread of the distribution <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

Ten years after Herschel, James Clerk Maxwell independently derived the same result while working on statistical mechanics, deriving a formula for the distribution of molecular velocities in a gas in three dimensions <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

This Herschel-Maxwell derivation clarifies why pi might appear in a Gaussian: circular symmetry is a defining property of the distribution itself <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. The "trick" of bumping the problem to higher dimensions in the classic proof (finding the area under the curve) then feels less arbitrary, as it directly leverages this underlying circular symmetry and the ability to factor the function <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

## Connecting to the Central Limit Theorem

Despite these derivations, the explanation still doesn't fully satisfy the statistician's friend because it assumes a multi-dimensional spatial situation <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. More commonly, the normal distribution arises from the [[central_limit_theorem | central limit theorem]], which involves adding many independent variables, a process that doesn't feel inherently spatial or geometric <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. The final step is to explain why the function characterized by the Herschel-Maxwell derivation is the same as the function central to the [[central_limit_theorem | central limit theorem]] <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.

### Footnote: Higher Dimensional Spheres

Applying this integration trick in higher dimensions allows for the derivation of formulas for the volumes of higher dimensional spheres <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This insight was shared by mathematician Kevin Ega <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.