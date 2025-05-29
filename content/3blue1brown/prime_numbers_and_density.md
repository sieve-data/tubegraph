---
title: Prime numbers and density
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

When considering a large range of numbers, such as those between 1 trillion (10^12) and 1 trillion plus a thousand, one might ask what proportion of these numbers are [[prime_numbers_and_their_regularities | prime numbers]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Density of Primes

As numbers increase in magnitude, [[prime_numbers_and_their_regularities | prime numbers]] generally become sparser <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This is because larger numbers have more potential factors they could be divisible by <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. For instance, checking if a number around a trillion is prime requires checking approximately a million potential prime factors up to its square root <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

A simple program can calculate the actual number of primes in a given range <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. For the range between 1 trillion and 1 trillion plus a thousand, there are 37 primes <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This means the proportion of primes in that 1000-integer range is 0.037, or approximately one in every 27 numbers <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Many might intuitively guess a much lower density, such as one in 250 or even one in a thousand <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Mathematicians can quickly estimate the density of primes in such ranges without extensive calculation <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This is due to a "cute fact" in number theory: the [[Relationship between natural logs and prime numbers | density of prime numbers]] near a given value (N) is approximately the natural logarithm of N (ln(N)) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. For a trillion (10^12), the natural log is approximately 27 <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This means that around a trillion, about one in every 27 numbers is prime <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Natural Logarithms and Primes

The frequent appearance of the natural logarithm (log base *e*) in relation to [[prime_numbers_and_their_regularities | prime numbers]] and other natural phenomena is why it is called the "natural logarithm" <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### Euler's Series and Pi

Euler demonstrated a remarkable connection between infinite series, [[Pi and its formulas involving primes | Pi]], and [[prime_numbers_and_their_regularities | prime numbers]] <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. For example, the sum of the reciprocals of squares (1/1^2 + 1/2^2 + 1/3^2 + ...) equals [[Pi and its formulas involving primes | pi]] squared divided by 6 (π²/6) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

An even more unusual manipulation involves creating a new series by:
*   Excluding non-[[prime_numbers_and_their_regularities | prime numbers]] that are not powers of a prime (e.g., 6, 10, 15, 21) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   Keeping [[prime_numbers_and_their_regularities | prime numbers]] as they are <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   Scaling down terms that are powers of a prime (e.g., 1/4^2 is scaled by 1/2 because 4 = 2^2; 1/8^2 is scaled by 1/3 because 8 = 2^3) <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

When this "strange game" is applied to the sum of reciprocals of squares, the resulting sum equals the natural logarithm of the original sum, i.e., ln(π²/6) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

This pattern extends to other series involving [[Pi and its formulas involving primes | pi]]. For instance, the alternating sum of reciprocals of odd numbers (1 - 1/3 + 1/5 - 1/7 + ...) equals [[Pi and its formulas involving primes | pi]] divided by 4 (π/4) <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. If the same "game" of keeping only [[prime_numbers_and_their_regularities | primes]] and scaled prime powers is applied, the result is the natural logarithm of pi/4 (ln(π/4)) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This suggests a profound connection between *e*, [[Pi and its formulas involving primes | pi]], and [[prime_numbers_and_their_regularities | prime numbers]] <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

### Alternating Harmonic Series

The alternating harmonic series, 1 - 1/2 + 1/3 - 1/4 + ..., converges to the natural logarithm of 2 (ln(2)), which is approximately 0.69 <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This can be derived by generalizing the series using powers of *x* (x - x²/2 + x³/3 - ...) and recognizing its derivative (1 - x + x² - ...) as a geometric series sum (1/(1+x)) <a class="yt-timestamp" data-t="01:04:52">[01:04:52]</a>. Integrating 1/(1+x) from 0 to 1 yields ln(2) <a class="yt-timestamp" data-t="01:09:46">[01:09:46]</a>.

### Harmonic Series

The harmonic series, 1 + 1/2 + 1/3 + 1/4 + ..., does not converge to a finite value; it diverges to infinity <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. This can be shown by grouping terms: (1/3 + 1/4) > 2*(1/4) = 1/2; (1/5 + 1/6 + 1/7 + 1/8) > 4*(1/8) = 1/2, and so on <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. This demonstrates that the sum can be made arbitrarily large by adding enough terms, as it's greater than 1 + 1/2 + 1/2 + 1/2... <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

The sum of the harmonic series up to 1/n is approximately the natural log of n (ln(n)) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. For example, to exceed a sum of a million, *n* must be approximately *e* to the power of a million (e^1,000,000), which is roughly 10^400,000 <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

This relationship between the harmonic sum and the natural log is further illuminated by calculus. The integral of 1/x from 1 to *n* is ln(*n*) <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>. Graphically, the sum of 1/n terms (represented by rectangles with height 1/n) is always slightly greater than the integral of 1/x (the area under the curve) <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>. The constant difference between the harmonic sum and ln(n) as n approaches infinity is known as Euler's constant (or Euler-Macheroni constant), approximately 0.577 <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>.

## The Special Role of *e* in Calculus

The number *e* is special because the derivative of *e*<sup>t</sup> with respect to *t* is *e*<sup>t</sup> itself <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. This property means that the rate of change of the function is always equal to its current value <a class="yt-timestamp" data-t="00:31:25">[00:31:25]</a>. While any exponential function (a<sup>t</sup>) has a derivative proportional to itself, *e*<sup>t</sup> is the only one where the proportionality constant is exactly 1 <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.

This makes *e* the natural choice for describing exponential families in physics, engineering, and mathematics, as it simplifies the interpretation of growth rates (e.g., in *e*<sup>rt</sup>, *r* directly represents the continuous growth rate) <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

Even in contexts like the bell curve in [[applications_of_probability_density | probability density]] functions (often written as *e*<sup>-x²</sup>) or complex exponentials (e.g., *e*<sup>it</sup>, which describes motion around a unit circle), using *e* provides readable meanings for the parameters involved <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. For example, in *e*<sup>it</sup>, *t* directly represents the distance walked in radians <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.

The derivative of the natural logarithm, ln(x), is 1/x <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>. This can be derived using implicit differentiation from the definition of the natural log: if y = ln(x), then x = e<sup>y</sup>. Taking the derivative of both sides with respect to x yields 1 = e<sup>y</sup> * dy/dx, which rearranges to dy/dx = 1/e<sup>y</sup>, or 1/x <a class="yt-timestamp" data-t="00:51:55">[00:51:55]</a>. This demonstrates the inverse relationship between the exponential function and the natural logarithm.