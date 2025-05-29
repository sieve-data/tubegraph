---
title: Calculus and exponential functions
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

Calculus provides a framework for understanding the unique properties and widespread appearance of [[properties_of_the_exponential_function | exponential functions]] and natural logarithms in mathematics and natural phenomena <a class="yt-timestamp" data-t="03:01:04">[03:01:04]</a>. The number *e*, the base of the natural logarithm, holds a special significance due to its relationship with rates of change <a class="yt-timestamp" data-t="03:02:51">[03:02:51]</a>.

## The Natural Logarithm and Prime Numbers

The density of prime numbers near a very large value, such as a trillion, is approximately the natural logarithm of that value <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. For example, around a trillion (10^12), the natural logarithm is approximately 27 <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. This means that roughly 1 out of every 27 numbers in that range is prime <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

The natural logarithm, denoted as ln(x) or log base e of x, answers the question "e to what power equals x?" <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. For instance, the natural log of 10 is about 2.3, meaning e^2.3 equals 10 <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>. The frequent appearance of the natural logarithm in seemingly unrelated mathematical contexts, such as prime number density, contributes to its designation as "natural" <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Infinite Series and Natural Logarithms

The natural logarithm is intrinsically linked to several infinite series:

*   **Harmonic Series**: The sum of reciprocals of positive integers (1 + 1/2 + 1/3 + 1/4 + ...) is known as the harmonic series. This series does not converge to a finite number; it eventually grows larger than any chosen value, no matter how small the terms become <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>. The sum of the first *n* terms of the harmonic series is approximately equal to [[natural_logarithms_and_exponential_growth | the natural log of *n*]] <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>. More precisely, it's approximately ln(n) plus Euler's constant (γ), which is about 0.577 <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This approximation is intuitive given that the integral of 1/x from 1 to *n* is ln(n) <a class="yt-timestamp" data-t="01:01:39">[01:01:39]</a>.

    ```
    S_n = 1 + 1/2 + 1/3 + ... + 1/n ≈ ln(n) <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>
    ```
    To reach a sum of a million, *n* must be approximately 10^400,000 <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>.

*   **Alternating Harmonic Series**: The alternating sum of reciprocals of positive integers (1 - 1/2 + 1/3 - 1/4 + ...) converges to the natural log of 2 <a class="yt-timestamp" data-t="01:12:51">[01:12:51]</a>. This can be shown by considering the integral of 1/(1+x) from 0 to 1 <a class="yt-timestamp" data-t="01:08:48">[01:08:48]</a>, which is ln(1+x) evaluated at the bounds, resulting in ln(2) - ln(1) = ln(2) <a class="yt-timestamp" data-t="01:10:47">[01:10:47]</a>.

*   **Basel Problem**: The sum of the reciprocals of squares (1/1^2 + 1/2^2 + 1/3^2 + ...) equals pi^2/6 <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. A peculiar "game" involving only prime numbers or powers of primes (scaled down by their exponent) in this series results in the natural logarithm of pi^2/6 <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>.

*   **Leibniz Formula for Pi/4**: The alternating sum of reciprocals of odd numbers (1 - 1/3 + 1/5 - 1/7 + ...) equals pi/4 <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>. Applying the same "prime number game" to this series yields the natural logarithm of pi/4 <a class="yt-timestamp" data-t="01:11:09">[01:11:09]</a>.

## The Significance of Euler's Number (*e*)

The number *e* (approximately 2.718) is the standard base for [[exponential_growth_and_decay | exponential growth]] and [[derivatives_of_exponential_functions | decay]] in physics, engineering, and mathematics <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. While any exponential function `a^x` can be rewritten as `e^(rx)` for some constant `r` (where `r = ln(a)`) <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>, the choice of *e* as the base is driven by its unique [[proportionality_constants_in_exponential_functions | rate of change]] property <a class="yt-timestamp" data-t="03:02:51">[03:02:51]</a>.

### Derivatives of Exponential Functions

The defining characteristic of `e^t` is that its derivative with respect to `t` is itself <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>:

```
d/dt (e^t) = e^t <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>
```
This means that at any point on the graph of `e^t`, the slope (rate of increase) is exactly equal to its height <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.

For a more general exponential function `e^(r*t)`, its derivative is `r * e^(r*t)` <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. The constant *r* represents the proportionality constant between the function's value and its rate of growth <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

For any base *a*, the derivative of `a^x` is `ln(a) * a^x` <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. This is derived by first converting `a^x` to `e^(ln(a) * x)` and then applying the chain rule <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. The factor `ln(a)` accounts for the "naturalness" of *e* in calculus. For example, the derivative of 2^x is `ln(2) * 2^x`, where `ln(2)` is approximately 0.69 <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.

### Complex Exponentials and Transformations

In the [[complex_plane_and_exponential_functions | complex plane]], `e^(i*t)` (where *i* is the imaginary unit and *t* is a real number) describes a point moving around the unit circle <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. This is because the derivative of `e^(i*t)` is `i * e^(i*t)` <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. Multiplying a complex number by *i* corresponds to a 90-degree rotation <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. This means the velocity vector (rate of change) is always 90 degrees to the position vector, causing circular motion <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

While other bases like `2^(i*t)` also produce circular motion, they simply "rescale time" <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. The `ln(2)` factor means `2^(i*t)` moves at a slower rate than `e^(i*t)` <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. The choice of *e* makes the angular distance traversed on the unit circle directly equal to *t* radians <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

### Defining *e* and its Properties

The number *e* can be defined in several ways:

1.  **Limit Definition**: *e* is the unique number for which the limit of `(a^h - 1) / h` as `h` approaches 0 is equal to 1 <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. This directly leads to `e^x` being its own derivative <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.
2.  **Taylor Series (Polynomial Definition)**: The exponential function, often denoted as `exp(x)`, can be defined by the infinite series:
    ```
    exp(x) = 1 + x + x^2/2! + x^3/3! + ... <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>
    ```
    Taking the derivative of each term in this series remarkably yields the exact same series, thus proving that `exp(x)` is its own derivative <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>. The number *e* is then `exp(1)` <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. This definition is particularly useful for [[complex_functions_and_transformations | complex functions]] and extending the concept of exponentiation beyond real numbers <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.

## Derivatives and Integrals of Natural Logarithms

The derivative of the natural logarithm `ln(x)` is `1/x` <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>:

```
d/dx (ln(x)) = 1/x <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>
```
This can be derived using implicit differentiation from the definition `e^y = x` (where `y = ln(x)`) <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

Conversely, the integral of `1/x` is the natural logarithm `ln(x)` <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>. This antiderivative relationship highlights the close connection between [[natural_logarithms_and_exponential_growth | natural logarithms]] and the growth properties of the harmonic series <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>. When comparing the harmonic sum `S` (sum of 1/n) and the integral `I` (integral of 1/x), the sum *S* is always greater than the integral *I* <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>, as visualized by rectangles (the sum) extending above the curve (the integral) <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.