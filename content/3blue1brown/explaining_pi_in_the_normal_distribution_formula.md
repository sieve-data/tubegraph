---
title: Explaining pi in the normal distribution formula
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The appearance of the mathematical constant pi in the formula for the [[normal_distribution_and_its_properties | normal distribution]] often puzzles people, as it seems disconnected from its typical definition as the ratio of a circle's circumference to its diameter <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This phenomenon highlights what physicist Eugene Wigner called "the unreasonable effectiveness of mathematics in the natural sciences" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

Wigner opens his paper with an anecdote about a statistician explaining the [[normal_distribution_and_its_properties | Gaussian distribution]] to a former classmate <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. When the statistician points to the symbol for pi, the classmate incredulously asks, "Surely the population has nothing to do with the circumference of a circle" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## The Origin of Pi in the Formula

The basic function describing the bell curve shape of the [[normal_distribution_and_its_properties | normal distribution]] is `e^(-x^2)` <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Pi shows up in the formula because the area underneath this curve works out to be the square root of pi <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This factor of `sqrt(pi)` must be divided out to ensure the total area under the curve is one, a requirement for any probability distribution <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Thus, the pi in the full formula originates from the area under `e^(-x^2)` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## The Classic Proof: The Gaussian Integral

Calculating the area under `e^(-x^2)` requires an integral from negative infinity to infinity <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. However, it's provably impossible to find a simple antiderivative for this function using standard mathematical tools <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This necessitates a "cleverness" or "new trick" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Step 1: Bumping to a Higher Dimension

The first step of the proof is to move from a two-dimensional area problem to a three-dimensional volume problem <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Instead of the area under `e^(-x^2)`, we consider the volume under the surface `e^(-(x^2+y^2))` <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This function takes two inputs, x and y, and its height is `e^(-r^2)` where `r` is the distance from the origin (`sqrt(x^2+y^2)`) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This definition gives the function a circular symmetry about the z-axis <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Calculating Volume with Circular Symmetry

To compute this volume, we can integrate thin cylindrical shells <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   The circumference of a shell at radius `r` is `2 * pi * r` <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   The height of the shell at radius `r` is `e^(-r^2)` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   With a small thickness `dr`, the volume of each shell is `(2 * pi * r * e^(-r^2)) * dr` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Integrating this expression from `r = 0` to infinity:
`Volume = ∫ (0 to ∞) 2 * pi * r * e^(-r^2) dr` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>
By factoring out `pi` and recognizing that `2r * e^(-r^2)` has an antiderivative of `-e^(-r^2)` <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>, the integral evaluates to `pi * [ -e^(-r^2) ] (from 0 to ∞)` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   At `r = ∞`, `e^(-r^2)` approaches `0` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   At `r = 0`, `e^(-r^2)` is `1` <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
So, the total volume is `pi * (0 - (-1)) = pi` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
Thus, the volume under this bell surface is pi <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

### Calculating Volume with Cartesian Slices

Alternatively, the volume can be computed by integrating slices parallel to one of the axes <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. The function `e^(-(x^2+y^2))` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   Consider a slice at `y = constant`. The shape of this slice is `e^(-x^2) * e^(-y_constant^2)` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   The area of this slice is the integral of `e^(-x^2) * e^(-y_constant^2) dx` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   Since `e^(-y_constant^2)` is a constant for a given slice, this area is `e^(-y_constant^2)` times the integral of `e^(-x^2) dx` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
Let `C` be the unknown area we are trying to find: `C = ∫ (-∞ to ∞) e^(-x^2) dx` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
So, the area of a slice is `C * e^(-y^2)` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

To find the total volume, we integrate these slice areas with respect to `y`:
`Volume = ∫ (-∞ to ∞) (C * e^(-y^2)) dy` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>
Factoring out `C`, we get `Volume = C * ∫ (-∞ to ∞) e^(-y^2) dy` <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
The integral `∫ (-∞ to ∞) e^(-y^2) dy` is also equal to `C`, the mystery constant <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
Therefore, the volume underneath the bell surface works out to be `C^2` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Conclusion of the Proof

By equating the two ways of calculating the volume:
`C^2 = pi` <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>
Therefore, `C = sqrt(pi)` <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
The area under the bell curve `e^(-x^2)` is `sqrt(pi)`.

## Beyond the Proof: Why `e^(-x^2)` is Special (Herschel-Maxwell Derivation)

The previous proof, while beautiful, feels like a trick <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. The deeper question, posed by the statistician's friend, is why circles (and thus pi) have anything to do with population statistics <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. The answer lies in the fundamental properties that define the [[normal_distribution_and_its_properties | Gaussian distribution]].

In 1850, John Herschel provided an elegant derivation for the [[normal_distribution_and_its_properties | Gaussian distribution]] <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. He showed that if a 2D probability distribution (e.g., hits on a dartboard) satisfies two reasonable properties, it must take the form `e^(-(x^2+y^2))` (up to constants) <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

### Property 1: Radial Symmetry

The probability density around each point depends only on its distance from the origin (`r`), not on its direction <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This means the 2D function `f2(x, y)` can be expressed as a single-variable function `f(r)` <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

### Property 2: Independence of X and Y Coordinates

The x and y coordinates of each point are independent <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. This means the 2D probability density function `f2(x, y)` can be factored into a product of two independent functions, one purely of x (`g(x)`) and one purely of y (`h(y)`) <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. Given radial symmetry, `g(x)` and `h(y)` must be the same function, say `g` <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. So, `f2(x, y) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

Combining these two properties, especially with the assumption that `f` and `g` are proportional (and for simplicity, setting the proportionality constant to 1 for derivation purposes) <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>, leads to a functional equation:
`f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### Solving the Functional Equation

To solve this, a helper function `h(x) = f(sqrt(x))` is introduced <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. This transforms the equation into:
`h(x + y) = h(x) * h(y)` for positive `x` and `y` <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

This equation implies that `h(n) = h(1)^n` for any whole number `n` <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. Further, for rational inputs `p/q`, `h(p/q) = h(1)^(p/q)` <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>. Assuming continuity, `h(x)` must be an exponential function `b^x` for some base `b` <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. This can be rewritten as `e^(c * x)` for some constant `c` <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.

Since `f(x) = h(x^2)` <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>, this means `f(x)` must be of the form `e^(c * x^2)` <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. For the function to represent a probability distribution that can be normalized (i.e., its volume doesn't blow up to infinity), the constant `c` in the exponent must be a negative number <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.

James Clerk Maxwell independently derived the same result ten years after Herschel, applying it to the distribution of molecular velocities in a gas <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

This derivation shows that the specific `e^(-x^2)` shape is a necessary consequence of radial symmetry and coordinate independence <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. Because circular symmetry is a defining property, it becomes less surprising that pi makes an appearance in the function's normalization <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. The "trick" of moving to higher dimensions in the integral proof is simply opening the door to make this defining radial symmetry visible <a class="yt-timestamp" data-t="00:22:39">[00:22:39]</a>.

## Connecting to the Central Limit Theorem

While the Herschel-Maxwell derivation explains why the [[normal_distribution_and_its_properties | Gaussian distribution]] arises in multi-dimensional scenarios, it doesn't immediately clarify its common appearance in non-spatial contexts, particularly via the [[central_limit_theorem | central limit theorem]] <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>. The [[central_limit_theorem | central limit theorem]] describes how the sum of many independent variables tends towards a [[normal_distribution_and_its_properties | normal distribution]] <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>. The [[connection_between_gaussian_distribution_and_probability | connection between the Herschel-Maxwell derivation and the central limit theorem]] is a topic for further exploration <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.

---
[!NOTE] Application to Higher Dimensions
The integration trick used to find the area under `e^(-x^2)` can be applied in higher dimensions to derive formulas for the volumes of higher-dimensional spheres <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>. This was shared by mathematician Kevin Ega <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

```latex
V_n(R) = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)} R^n
```
<a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>
This formula for the volume of an n-dimensional sphere of radius R involves the Gamma function, which is a generalization of the factorial function to real and complex numbers.
The derivation involves integration by parts <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.