---
title: Infinite series and sum computations
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

## The Natural Logarithm and Prime Density
The proportion of prime numbers within a large range, such as between one trillion and one trillion plus one thousand, can be estimated using the natural logarithm <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. For numbers around one trillion (10¹²), the density of primes is approximately one in every `ln(10¹²)`, which is about 27 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This connection between the natural logarithm and prime numbers is considered a remarkable mathematical fact <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

The natural logarithm (log base `e`) is often called "natural" because of its frequent appearance in various mathematical and scientific contexts <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a> <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## Famous Infinite Series
### The Basel Problem
One well-known [[concept_of_infinite_sums_in_mathematics | infinite series]] is the sum of the reciprocals of all natural numbers squared: 1/1² + 1/2² + 1/3² + 1/4² + ... <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This problem, posed in Basel, remained open for some time <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Leonhard Euler famously proved that this sum converges to `π²/6` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. The appearance of `π` in a sum of squares is considered a beautiful result <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

A curious variation of this series involves only prime numbers and their powers:
1/2² + 1/3² + (1/4² * 1/2) + 1/5² + (1/8² * 1/3) + (1/9² * 1/2) + ...
In this modified series, terms for composite numbers are excluded, and terms for powers of primes (like 4=2² or 8=2³) are scaled down by the reciprocal of their exponent (e.g., 1/2 for a square, 1/3 for a cube) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This manipulated series remarkably sums to `ln(π²/6)` <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

### Leibniz Formula for Pi
Another significant alternating series is `1 - 1/3 + 1/5 - 1/7 + 1/9 - ...`, which sums to `π/4` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
Applying a similar prime-based manipulation to this series (excluding composites, scaling prime powers) results in a sum equal to `ln(π/4)` <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. These relationships highlight a profound connection between `e`, `π`, and prime numbers <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### The Alternating Harmonic Series
The series `1 - 1/2 + 1/3 - 1/4 + ...` involves alternating signs with the reciprocals of all natural numbers <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This series converges to `ln(2)` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. This means `e` raised to the power of this sum is equal to 2 <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

The proof for this sum involves a process of generalization and differentiation:
1.  **Generalization**: The problem can be generalized by introducing `x` as a variable: `f(x) = x/1 - x²/2 + x³/3 - x⁴/4 + ...` <a class="yt-timestamp" data-t="01:05:04">[01:05:04]</a>. The original series is `f(1)`.
2.  **Differentiation**: Taking the derivative of `f(x)` with respect to `x` simplifies the series: `f'(x) = 1 - x + x² - x³ + ...` <a class="yt-timestamp" data-t="01:05:39">[01:05:39]</a>.
3.  **Geometric Series**: The simplified series `1 - x + x² - x³ + ...` is a geometric series with a common ratio of `-x` <a class="yt-timestamp" data-t="01:06:20">[01:06:20]</a>. The sum of such a series is `1 / (1 - (-x)) = 1 / (1 + x)` <a class="yt-timestamp" data-t="01:06:44">[01:06:44]</a>.
4.  **Integration**: Since `f'(x) = 1 / (1 + x)`, integrating `f'(x)` gives `f(x)` back. The integral of `1 / (1 + x)` is `ln(1 + x)` <a class="yt-timestamp" data-t="01:08:17">[01:08:17]</a> <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>.
5.  **Evaluation**: Therefore, `f(x) = ln(1 + x)`. Plugging in `x = 1` yields `f(1) = ln(1 + 1) = ln(2)` <a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a>.

This method highlights the elegance of using calculus to solve problems in [[concept_of_infinite_sums_in_mathematics | infinite series]] by transforming a difficult sum into a more manageable derivative, then integrating it back <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>.

### The Harmonic Series
The harmonic series `1 + 1/2 + 1/3 + 1/4 + ...` (sum of reciprocals of natural numbers) does not converge <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. This means no matter how many terms are added, the sum will eventually exceed any chosen finite number <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

This divergence can be proven by grouping terms:
*   (1/3 + 1/4) > (1/4 + 1/4) = 1/2 <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>
*   (1/5 + 1/6 + 1/7 + 1/8) > (1/8 + 1/8 + 1/8 + 1/8) = 4/8 = 1/2 <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>
*   And so on, each group summing to more than 1/2 <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
Since there are infinitely many such groups, and each adds at least 1/2 to the total, the sum grows infinitely large <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

While the harmonic series diverges, its growth rate is logarithmic. The sum of the first `n` terms (denoted as `S_n`) is approximately equal to `ln(n)` <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. More accurately, `S_n ≈ ln(n) + γ`, where `γ` (Euler-Mascheroni constant) is approximately 0.577 <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>.
For example, to find `n` such that the sum is greater than one million, one would solve `ln(n) ≈ 1,000,000`, which implies `n ≈ e^(1,000,000)` <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Since `e ≈ 10^(1/2.3)` <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>, `n` is roughly `10^(1,000,000 / 2.3)`, which is approximately `10^(400,000)` <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. This incredibly large number demonstrates the slow growth of the harmonic series <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

The relationship between the harmonic sum and the natural logarithm can be visualized by comparing the sum of rectangles (each with width 1 and height 1/n) to the area under the curve `y = 1/x` <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>. The integral of `1/x` from 1 to `n` is `ln(n)` <a class="yt-timestamp" data-t="01:01:39">[01:01:39]</a>. By drawing the rectangles such that their upper-left corners touch the `1/x` curve, it becomes clear that the sum of the areas of the rectangles (`S_n`) is greater than the area under the curve (`ln(n)`) <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>. The difference between the sum and the integral approaches Euler's constant <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>.

## The Role of `e` and the Exponential Function
The number `e` is special because the derivative of `e^t` with respect to `t` is `e^t` itself <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. This means the rate of change of the exponential function at any point is equal to its value at that point <a class="yt-timestamp" data-t="00:31:25">[00:31:25]</a>. This property simplifies calculations involving rates of change and is why `e` is often chosen as the base for exponential functions in physics, engineering, and mathematics (e.g., `e^(rt)` instead of `a^t`) <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>. Using `e` makes the proportionality constant `r` directly readable as the continuous growth rate <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>.

For any base `a`, `a^x` can be rewritten as `e^(ln(a) * x)` <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>. The derivative of `a^x` is `ln(a) * a^x` <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>. This confirms that `e` (where `ln(e) = 1`) is the only base for which the function is its own derivative.

The exponential function, `exp(x)` (often written as `e^x`), can also be defined as an [[understanding_taylor_series_convergence | infinite series]] or [[approximating_functions_using_taylor_series | Taylor series]]: `1 + x + x²/2! + x³/3! + ...` <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>. Taking the derivative of this polynomial term by term reveals that it is indeed its own derivative <a class="yt-timestamp" data-t="00:48:58">[00:48:58]</a>. This foundational definition allows for its use with complex numbers, leading to Euler's formula (`e^(ix) = cos(x) + i*sin(x)`) <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>.

## Derivatives and Integrals of Natural Logarithms
The derivative of `ln(x)` is `1/x` <a class="yt-timestamp" data-t="00:53:28">[00:53:28]</a>. This can be derived using implicit differentiation from the definition `y = ln(x)` which means `x = e^y` <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>. Differentiating both sides with respect to `x` gives `1 = e^y * dy/dx` <a class="yt-timestamp" data-t="00:52:33">[00:52:33]</a>, so `dy/dx = 1/e^y = 1/x` <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.

Conversely, the integral of `1/x` is `ln(x)` <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>. This inverse relationship between derivatives and integrals (as formalized by the Fundamental Theorem of Calculus) is crucial for understanding connections between different mathematical concepts <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a>.