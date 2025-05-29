---
title: Connection between Gaussian distribution and probability
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The phrase "the unreasonable effectiveness of mathematics in the natural sciences" was the title of a paper by physicist Eugene Wigner <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Wigner opens his paper with an anecdote about a statistician explaining the [[Normal distribution and its properties | Gaussian distribution]] to a former high school classmate <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. When the statistician mentions "pi" in the formula, the classmate is incredulous, questioning what the ratio of a circle's circumference to its diameter has to do with population trends <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

This article delves into that specific question: how does [[explaining_pi_in_the_normal_distribution_formula | pi appear in the normal distribution formula]]?

## The Normal Distribution and Pi

The basic function that describes the bell curve shape of a [[Normal distribution and its properties | normal distribution]] (also known as a [[Normal distribution and its properties | Gaussian distribution]]) is `e` to the negative `x` squared (`e^(-x^2)`) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Pi shows up in the final formula because the area underneath this curve works out to be the square root of pi (√π) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. To interpret the curve as a [[Probability density and distribution | probability distribution]], its total area must equal one <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Therefore, the function needs to be divided by √π to normalize its area <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

The core questions then become:
1.  How is the area under `e^(-x^2)` calculated to be √π?
2.  Why is the function `e^(-x^2)` itself so special in statistics? <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

## Classic Proof: Calculating the Area

Finding the area under `e^(-x^2)` involves an integral from negative infinity to infinity <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. However, it's provably not possible to find a closed-form antiderivative for this specific function using standard mathematical tools (polynomials, trig functions, exponentials) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This requires a clever trick.

### The "Trick": Bumping Up a Dimension

The first step is to consider a two-dimensional version of the function: `f(x, y) = e^(-(x^2 + y^2))` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This function describes a bell-shaped surface with [[Probability in Geometry | circular symmetry]] about the z-axis <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. The value of `f(x, y)` depends only on the distance `r` from the origin (`r = sqrt(x^2 + y^2)`) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

#### Method 1: Integration in Polar Coordinates

Due to the [[Probability in Geometry | circular symmetry]], the volume under this surface can be calculated by integrating thin cylindrical shells <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   The circumference of a shell at radius `r` is `2πr` <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   The height of the surface at radius `r` is `e^(-r^2)` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   The volume of a thin shell with thickness `dr` is `(2πr) * e^(-r^2) * dr` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Integrating this expression from `r = 0` to infinity:
∫(from 0 to ∞) `2πr * e^(-r^2) dr` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>

This integral can be solved using standard calculus (e.g., u-substitution where `u = -r^2`, `du = -2r dr`) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. The antiderivative of `2r * e^(-r^2)` is `-e^(-r^2)` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
Evaluating the definite integral:
`π * [-e^(-r^2)] (from 0 to ∞)`
`π * (lim(r→∞) (-e^(-r^2)) - (-e^(-0^2)))`
`π * (0 - (-1))`
`π * 1 = π` <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>

Thus, the volume under the 2D bell surface `e^(-(x^2+y^2))` is **π** <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

#### Method 2: Integration in Cartesian Coordinates

The same volume can also be calculated by slicing the surface parallel to an axis <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
The function `f(x, y) = e^(-(x^2 + y^2))` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
Consider slices along the x-axis for different `y` values. For a given `y`, the slice function is `e^(-x^2) * e^(-y^2)`. The term `e^(-y^2)` is a constant for that slice, so the area of the slice is `e^(-y^2)` multiplied by the area under `e^(-x^2)` <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
Let `C` be the unknown area under `e^(-x^2)` (i.e., `C = ∫(from -∞ to ∞) e^(-x^2) dx`) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
The volume is then the integral of the area of these slices:
Volume = ∫(from -∞ to ∞) `(C * e^(-y^2)) dy` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>
Since `C` is a constant, it can be factored out:
Volume = `C * ∫(from -∞ to ∞) e^(-y^2) dy` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
The integral `∫(from -∞ to ∞) e^(-y^2) dy` is also `C` (just with `y` instead of `x`).
So, Volume = `C * C = C^2` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Conclusion of the Classic Proof

Equating the two ways of calculating the volume:
`C^2 = π` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>
Therefore, `C = √π` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

This proves that the area under the curve `e^(-x^2)` is √π. For a [[Probability density and distribution | probability density function]], the total area must be 1. Hence, the `e^(-x^2)` function is scaled by `1/√π` (or `1/√(2πσ^2)` in its full form, where `σ` relates to the spread of the distribution) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Herschel-Maxwell Derivation

While the above proof explains *that* pi appears, it doesn't fully answer *why* it appears in a non-spatial context. This leads to the [[herschel_maxwells_derivation_and_its_impact_on_understanding_gaussian_distribution | Herschel-Maxwell derivation]] <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

In 1850, John Herschel provided an elegant derivation for the [[Normal distribution and its properties | Gaussian distribution]] by considering a two-dimensional [[Probability density and distribution | probability distribution]], such as the distribution of hits on a dartboard <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. He showed that if two reasonable properties are met, the distribution must take the form `e^(-(x^2 + y^2))` (up to a scaling factor) <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### Property 1: Radial Symmetry

The [[Probability density and distribution | probability density]] around each point depends only on its distance from the origin (`r`), not its direction <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
Mathematically, `f2(x, y) = f(r)`, where `r = sqrt(x^2 + y^2)` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This means the distribution has an intrinsic [[Probability in Geometry | circular symmetry]] <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

### Property 2: Independence of Coordinates

The `x` and `y` coordinates of each point are independent from each other <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This means the joint [[Probability density and distribution | probability density function]] `f2(x, y)` can be factored into functions of `x` and `y` separately: `f2(x, y) = g(x) * h(y)` <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Due to radial symmetry, `g` and `h` must be the same function, so `f2(x, y) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. Also, `f(r)` (from Property 1) is proportional to `g(r)` <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

Combining these properties (and assuming `f` and `g` are the same function up to a constant factor, which can be handled by normalization later), we get a functional equation:
`f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

### Solving the Functional Equation

To solve `f(sqrt(x^2 + y^2)) = f(x) * f(y)`, introduce a helper function `h(z) = f(sqrt(z))`, so `f(x) = h(x^2)` <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
Substituting this into the equation:
`h(x^2 + y^2) = h(x^2) * h(y^2)` <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
Let `X = x^2` and `Y = y^2`. Then, `h(X + Y) = h(X) * h(Y)` for positive `X` and `Y` <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

This functional equation implies that `h` must be an exponential function <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. If `h(1) = b`, then `h(n) = b^n` for any whole number `n`, and similarly `h(p/q) = b^(p/q)` for rational `p/q` <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. Assuming `h` is continuous, it must be of the form `h(z) = b^z` for all positive real `z` <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. This can be rewritten as `h(z) = e^(cz)` for some constant `c` <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.

Substituting back `f(x) = h(x^2)`, we find that `f(x)` must be of the form `e^(c*x^2)` <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. For this to be a valid [[Probability density and distribution | probability distribution]] (i.e., its area does not "blow up"), the constant `c` must be negative <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. The specific negative value of `c` determines the spread of the distribution <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

### Impact of Herschel-Maxwell Derivation

[[herschel_maxwells_derivation_and_its_impact_on_understanding_gaussian_distribution | James Clerk Maxwell]] independently stumbled upon this same derivation a decade later while deriving a formula for the distribution of velocities of molecules in a gas <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

This derivation explains why the [[Normal distribution and its properties | Gaussian function]] is `e^(-x^2)`: it's the unique function satisfying radial symmetry and coordinate independence. The inherent [[Probability in Geometry | circular symmetry]] in its definition naturally explains the appearance of pi in the normalization constant <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. The "trick" of bumping up a dimension in the classic proof was essentially "opening the door" to reveal this defining property <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

## Unanswered Question: Central Limit Theorem

While the [[herschel_maxwells_derivation_and_its_impact_on_understanding_gaussian_distribution | Herschel-Maxwell derivation]] clarifies the role of [[Probability in Geometry | circular symmetry]], it still assumes a multi-dimensional spatial or geometric situation <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. In practice, the [[Normal distribution and its properties | normal distribution]] most commonly arises from the [[central_limit_theorem | Central Limit Theorem]], which involves adding together many independent variables without an obvious spatial or geometric connection <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. Explaining why the function derived from the Herschel-Maxwell properties is the same as the function at the heart of the [[central_limit_theorem | Central Limit Theorem]] remains a further area of exploration <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.

> [!NOTE] Higher Dimensional Spheres
> The integration trick used to find the area under the Gaussian curve can also be applied in higher dimensions to derive the formulas for volumes of higher-dimensional spheres. This insight was shared by mathematician Kevin Ega <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.