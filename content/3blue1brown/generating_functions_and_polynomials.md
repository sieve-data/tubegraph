---
title: Generating functions and polynomials
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

Generating functions are a powerful mathematical tool used to study discrete sequences by encoding information about them as coefficients of a polynomial or power series <a class="yt-timestamp" data-t="09:30:30">[09:30:30]</a>. The core idea is to transform questions about integer sequences into problems of manipulating and analyzing the properties of these functions <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>, often involving complex numbers <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This approach can reveal surprising insights that are difficult to obtain by direct analysis <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

## Encoding Discrete Problems with Polynomials

A common use of generating functions is to represent combinatorial problems. For instance, consider the puzzle of finding the number of subsets of a given set (e.g., 1 to 2000) whose elements sum to a value divisible by 5 <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

To approach this using generating functions, a specific polynomial is constructed:
$$(1+x)(1+x^2)(1+x^3)...(1+x^N)$$
where N is the largest element in the set <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. For the set 1 to 5, this polynomial is $(1+x)(1+x^2)(1+x^3)(1+x^4)(1+x^5)$ <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.

### The Role of Expansion
When this polynomial is algebraically expanded (similar to [[polynomial_multiplication_and_convolution | polynomial multiplication and convolution]]), each term in the expansion corresponds to a unique subset of the original set <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>. The exponent of 'x' in each term represents the sum of the elements in that corresponding subset <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. For example:
*   Choosing '1' from each parenthetical corresponds to the empty set (sum 0) <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   Choosing 'x' from the first parenthetical and '1' from others corresponds to the subset {1} (sum 1) <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.
*   Choosing 'x' from the first and 'x²' from the second parenthetical, and '1' from others, results in an $x^3$ term, corresponding to the subset {1, 2} (sum 3) <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.

When all like terms are collected, the coefficient of $x^n$ (denoted as $c_n$) represents the number of distinct subsets whose elements sum to 'n' <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. For example, if the coefficient of $x^{10}$ is 3, it means there are 3 distinct subsets whose sum is 10 <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

## Manipulating Generating Functions

Once the problem is encoded in a generating function, `f(x)`, the task shifts to analyzing `f(x)` without full expansion <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.

### Basic Evaluations
*   **`f(0)`**: Plugging in `x=0` into the polynomial `f(x)` (in its expanded form) isolates the constant term, $c_0$ <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>. For the subset sum problem, `f(0) = 1`, which means there is one subset with sum 0 (the empty set) <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.
*   **`f(1)`**: Plugging in `x=1` causes all powers of `x` to become 1, resulting in the sum of all coefficients, $\sum c_n$ <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>. This sum represents the total number of subsets <a class="yt-timestamp" data-t="13:24:00">[13:24:00]</a>. For a set of N elements, there are $2^N$ total subsets <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. For the set 1 to 2000, `f(1) = 2^2000` <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.

### Filtering with Negative One
Evaluating `f(-1)` reveals the alternating sum of coefficients ($c_0 - c_1 + c_2 - ...$) <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>. For the subset sum problem on the set 1 to 2000, `f(-1)` is 0 because the first term $(1+x)$ becomes 0 when $x=-1$, making the entire product 0 <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
This implies that $c_0 + c_2 + c_4 + ... = c_1 + c_3 + c_5 + ...$, meaning half of all subsets have an even sum, and half have an odd sum <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.
Adding `f(1)` and `f(-1)` and dividing by 2 provides the sum of only the even coefficients ($c_0 + c_2 + c_4 + ...$) <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.

## The Role of Complex Numbers

To find the sum of coefficients whose indices are multiples of a specific number (e.g., multiples of 5), complex numbers become "unreasonably useful" <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

### Roots of Unity
The key is to use the **roots of unity**. These are complex numbers that, when raised to a specific power (e.g., 5), result in 1. For the problem involving divisibility by 5, the fifth roots of unity are used <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>.
These roots are located on the unit circle in the complex plane, rotating by equal angles with successive powers <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. The primary root, denoted as $\zeta$ (zeta), is $e^{2\pi i/5}$ <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>. Its powers $\zeta^0, \zeta^1, \zeta^2, \zeta^3, \zeta^4$ cycle through the five roots, with $\zeta^5 = \zeta^0 = 1$ <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>. This cycling behavior is fundamental to their utility <a class="yt-timestamp" data-t="18:37:00">[18:37:00]</a>. [[exponential_functions_and_their_properties | Exponential functions and their properties]], particularly Euler's formula, provide the framework for understanding these rotations.

### Filtering with Roots of Unity
When evaluating `f(x)` at these roots of unity and summing the results, a powerful filtering effect occurs <a class="yt-timestamp" data-t="22:12:00">[22:12:00]</a>:
*   If the exponent `n` of a term $c_n x^n$ is *not* a multiple of 5, the sum of that term evaluated at all five roots of unity (e.g., $c_n (\zeta^0)^n + c_n (\zeta^1)^n + ... + c_n (\zeta^4)^n$) will cancel out to 0 <a class="yt-timestamp" data-t="22:48:00">[22:48:00]</a>. This is because the sum of the roots of unity themselves (or any permutation of them) is 0 <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>.
*   If the exponent `n` *is* a multiple of 5, each $(\zeta^k)^n$ term will evaluate to 1 (since $n$ is a multiple of 5, $(\zeta^k)^n = (\zeta^n)^k = 1^k = 1$) <a class="yt-timestamp" data-t="22:52:00">[22:52:00]</a>. Thus, the sum for that term will be $c_n \times 5$ <a class="yt-timestamp" data-t="22:55:00">[22:55:00]</a>.

Therefore, the sum $f(\zeta^0) + f(\zeta^1) + f(\zeta^2) + f(\zeta^3) + f(\zeta^4)$ equals $5 \times (c_0 + c_5 + c_{10} + ...)$ <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>. Dividing this sum by 5 directly gives the desired count of subsets whose sums are divisible by 5 <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>.

### Calculating the Roots of Unity Sum
To apply this, one needs to evaluate `f(x)` at each of the roots. For the generating function $(1+x)(1+x^2)...(1+x^{2000})$, evaluating it at a root of unity $\zeta^k$ (where $k \neq 0$) means calculating:
$$f(\zeta^k) = (1+\zeta^k)(1+(\zeta^k)^2)...(1+(\zeta^k)^{2000})$$
Since powers of $\zeta^k$ repeat every 5 terms, this long product can be grouped into 400 repetitions of the product of the first five terms <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>:
$$(1+\zeta^k)(1+\zeta^{2k})(1+\zeta^{3k})(1+\zeta^{4k})(1+\zeta^{5k}) \times ... \times (1+\zeta^k)(1+\zeta^{2k})...$$
The product of the first five terms $(1+x)(1+x^2)(1+x^3)(1+x^4)(1+x^5)$ can be precisely evaluated using the factorization of $z^5 - 1$ <a class="yt-timestamp" data-t="27:25:00">[27:25:00]</a>:
$$z^5 - 1 = (z-\zeta^0)(z-\zeta^1)(z-\zeta^2)(z-\zeta^3)(z-\zeta^4)$$
By dividing by $(z-1)$ and substituting $z = -1$, it can be shown that $(1+\zeta^1)(1+\zeta^2)(1+\zeta^3)(1+\zeta^4)(1+\zeta^0)$ evaluates to $2$ <a class="yt-timestamp" data-t="28:30:00">[28:30:00]</a>.
Consequently, for any $k \in \{1,2,3,4\}$, $f(\zeta^k) = 2^{400}$ <a class="yt-timestamp" data-t="28:55:00">[28:55:00]</a>.
For $\zeta^0=1$, $f(1) = 2^{2000}$ <a class="yt-timestamp" data-t="29:16:00">[29:16:00]</a>.

Summing these up:
$f(1) + f(\zeta) + f(\zeta^2) + f(\zeta^3) + f(\zeta^4) = 2^{2000} + 4 \times 2^{400}$ <a class="yt-timestamp" data-t="29:38:00">[29:38:00]</a>.
The final answer for the number of subsets with sums divisible by 5 is therefore:
$$\frac{1}{5} (2^{2000} + 4 \times 2^{400})$$ <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.

## Broader Implications

The technique of using generating functions and complex analysis to solve discrete problems is widespread and powerful:

*   **Riemann Hypothesis**: The modern understanding of prime number distribution involves studying the Riemann zeta function, which is a Dirichlet series (a type of generating function) whose properties are analyzed using complex-valued inputs <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Questions about primes are often easier to answer by analyzing this complex function than by directly studying primes themselves <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.
*   **Frequency Analysis**: The use of roots of unity to detect "frequency information" is a core idea in [[fourier_transforms | Fourier transforms]] and Fourier series, which are fundamental in signal processing, image analysis, and many other scientific fields <a class="yt-timestamp" data-t="33:52:00">[33:52:00]</a>.
*   **Quantum Computing**: Shor's algorithm for factoring large numbers on quantum computers leverages the use of roots of unity to detect frequency information in a quantum system, allowing for significantly faster computation than classical methods <a class="yt-timestamp" data-t="33:59:00">[33:59:00]</a>.

These examples highlight how extending mathematical domains to include complex numbers offers greater power in making deductions about seemingly unrelated discrete problems <a class="yt-timestamp" data-t="32:22:00">[32:22:00]</a>.

***

> "It's certainly not the only time that complex numbers are unreasonably useful for discrete math, to borrow a phrase." <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>

> "The more math you do, the less crazy that seems, because complex numbers have this bizarre relationship with discrete math, but it really is wonderful, there's no two ways about it." <a class="yt-timestamp" data-t="23:41:00">[23:41:00]</a>

For further reading, "GeneratingFunctionology" by Herbert Wilf is recommended <a class="yt-timestamp" data-t="34:01:00">[34:01:00]</a>.