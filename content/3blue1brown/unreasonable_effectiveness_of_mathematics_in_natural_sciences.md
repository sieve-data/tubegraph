---
title: Unreasonable effectiveness of mathematics in natural sciences
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The phrase "the unreasonable effectiveness of mathematics in the natural sciences" was coined by physicist Eugene Wigner, who also wrote a paper on the topic <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Wigner opens his paper with an anecdote about two high school classmates, one of whom became a statistician working on population trends <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The statistician showed a reprint that started with the Gaussian distribution, explaining symbols for actual and average population <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. His classmate, incredulous, asked what a specific symbol was <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The statistician replied, "This is pi" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. When asked what pi was, he explained it as "the ratio of the circumference of a circle to its diameter" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The classmate found this hard to believe, stating that population should have nothing to do with the circumference of a circle <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Wigner's paper discusses the broader phenomenon of pure mathematical concepts finding unexpected applications beyond their initial definitions <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. However, the core question highlighted by the statistician's friend is why a constant related to circles appears in population statistics <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This article explores a proof that explains the presence of pi in the normal distribution formula and seeks to connect it to a deeper understanding of why this specific function is so prevalent in statistics <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## The Role of Pi in the Normal Distribution

The normal distribution, also known as a Gaussian distribution, has a basic bell curve shape described by the function `e^(-x^2)` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The reason pi appears in its final formula is that the area underneath this curve works out to be the square root of pi <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. To interpret it as a probability distribution, the area under the curve must be one, requiring a division by the square root of pi <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This constant originates from the area under `e^(-x^2)` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Calculating the Area Under `e^(-x^2)`

Finding the area under a curve typically involves using an integral <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. An integral approximates the area by summing the areas of many thin rectangles under the curve <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. For the function `e^(-x^2)` from negative infinity to infinity, the usual calculus procedure of finding an antiderivative is not possible; there is no expression for its antiderivative using standard functions like polynomials, trig functions, or exponentials <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This problem requires a "clever trick" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### The Clever Trick: Bumping Up a Dimension

The first step of the trick is to consider a related problem: finding the volume underneath a two-dimensional bell surface defined by `e^-(x^2 + y^2)` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This function can be thought of as `e^(-r^2)`, where `r` is the distance from the origin (`sqrt(x^2 + y^2)`) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This gives the function circular symmetry, meaning all points on a given circle have the same output value <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

#### Method 1: Integrating with Cylindrical Shells

Respecting the circular symmetry, the volume can be computed by integrating thin cylindrical shells <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Each shell has a circumference of `2πr` and a height of `e^(-r^2)` <a class="yt=" yt-timestamp data-t="00:07:08">[00:07:08]</a>. The volume of such a shell with thickness `dr` is `(2πr) * e^(-r^2) * dr` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Integrating this expression from `r = 0` to infinity:

*   The integral becomes `∫(0 to ∞) 2πr * e^(-r^2) dr` <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   Factoring out `π`, we get `π * ∫(0 to ∞) 2r * e^(-r^2) dr` <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   The term `2r * e^(-r^2)` has an antiderivative: `-e^(-r^2)` <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   Evaluating the antiderivative from `0` to `∞`: `0 - (-1) = 1` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   Therefore, the volume underneath the bell surface is `π * 1 = π` <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

It is not surprising that pi appears when using cylindrical coordinates due to the surface's intrinsic circular symmetry <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

#### Method 2: Integrating with Parallel Slices

The volume can also be approached by slicing the surface parallel to an axis, for example, the x-axis <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. The function `e^-(x^2 + y^2)` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="00:09:57">[00:10:00]</a>.

*   For a slice where `y` is constant, the function is `e^(-x^2) * (e^(-y^2))` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   `e^(-y^2)` is just a constant for that slice <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   The area of such a slice is `c * e^(-y^2)`, where `c` is the unknown area under `e^(-x^2)` <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   The total volume is `∫(-∞ to ∞) (area of slice) dy = ∫(-∞ to ∞) c * e^(-y^2) dy` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   Factoring out `c`, this becomes `c * ∫(-∞ to ∞) e^(-y^2) dy` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   The remaining integral is also `c` (the same mystery constant) <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   Therefore, the volume underneath this bell surface is `c * c = c^2` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

Since both methods calculate the same volume, we have `c^2 = π` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. This means the area under the bell curve, `c`, must be `sqrt(π)` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

However, this proof can feel like a "trick" that doesn't fully answer the statistician's friend's question about the connection between circles and population statistics <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Herschel-Maxwell Derivation: Defining the Gaussian

To go deeper, we need to understand why the function `e^(-x^2)` is so special in the first place <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. John Herschel, a 19th-century mathematician and scientist, offered an elegant derivation for the Gaussian distribution in 1850 <a class="yt=" yt-timestamp data-t="00:12:51">[00:12:51]</a>.

Herschel's setup involves describing a probability distribution in two-dimensional space, like hits on a dartboard <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. He showed that if this distribution satisfies two reasonable properties, the function describing it must take the form `e^-(x^2 + y^2)` (up to a scaling constant) <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

### Property 1: Radial Symmetry

The probability density around each point depends only on its distance from the origin, not on its direction <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. Mathematically, the probability distribution function, `f2(x, y)`, can be expressed as a single-variable function of the radius `r`, i.e., `f(r)` where `r = sqrt(x^2 + y^2)` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

### Property 2: Independence of Coordinates

The x and y coordinates of each point are independent <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This means the function `f2(x, y)` can be factored into a part purely dependent on `x` (let's call it `g(x)`) and a part purely dependent on `y` (let's call it `h(y)`) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Due to radial symmetry, the behavior on each axis should be the same, so `h(y)` must be the same function as `g(y)`, making `f2(x, y) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

Combining these two properties, `f(sqrt(x^2 + y^2)) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. If we make the simplifying assumption that `f` and `g` are the same function (up to a constant that can be normalized later) <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>, we get the functional equation:

`f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

#### Solving the Functional Equation

To solve this, a helper function `h(x) = f(sqrt(x))` is introduced <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. This means `f(x) = h(x^2)` <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
The functional equation then becomes:

`h(x^2 + y^2) = h(x^2) * h(y^2)` <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

Let `A = x^2` and `B = y^2`. Since `x` and `y` can be any real numbers, `A` and `B` can be any positive real numbers.
So, `h(A + B) = h(A) * h(B)` <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

This equation implies that for any whole number `n`, `h(n) = (h(1))^n` <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. If we let `b = h(1)`, then `h(n) = b^n` <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. This can be extended to rational inputs (`p/q`), where `h(p/q) = b^(p/q)` <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Assuming `h` is continuous, this forces `h(x)` to be an exponential function, `b^x`, for all positive real `x` <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

Mathematicians often express exponential functions as `e^(cx)` <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.
Since `f(x) = h(x^2)`, this implies `f(x) = e^(c * x^2)` <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
For this to be a valid probability distribution (i.e., for the area/volume under the curve to be finite and normalizable), the constant `c` in the exponent must be a negative number <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. The specific value of `c` determines the spread of the distribution <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

### Maxwell's Independent Discovery

Ten years after Herschel's work, James Clerk Maxwell, known for his work in electromagnetism, independently arrived at the same derivation <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>. Maxwell applied it in three dimensions to derive the distribution of velocities of molecules in a gas within statistical mechanics <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

## Connecting the Proof to the Derivation

Viewing this Herschel-Maxwell derivation as the defining property of a Gaussian makes the appearance of pi less surprising <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. Circular symmetry was an intrinsic part of this definition <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. The "clever trick" of bumping up a dimension in the area calculation then feels less arbitrary <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. It was a way to make the Gaussian's defining properties – radial symmetry and the ability to factor the function – visible and usable in the calculation <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. From this perspective, the proof's steps are not just a trick that happened to work, but an inevitable necessity stemming from the function's fundamental nature <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.

## Unanswered Questions

Even with the Herschel-Maxwell derivation, the connection to real-world population statistics (as per the statistician's friend) is not fully satisfying <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. The derivation assumes a multi-dimensional spatial or geometric situation <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. However, normal distributions commonly arise from the [[Central Limit Theorem]], which is about adding many different independent variables, not inherently a spatial concept <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. The next step is to explain why the function characterized by the Herschel-Maxwell derivation is the same as the function central to the [[Central Limit Theorem]] <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.

### Higher Dimensional Spheres

As a side note, applying the integration trick in higher dimensions allows for the derivation of formulas for volumes of higher-dimensional spheres <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This was shared by mathematician Kevin Ega <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.