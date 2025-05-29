---
title: The Riemann hypothesis and trivial zeros
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 
The [[Riemann hypothesis and prime numbers | Riemann zeta function]] is a mathematical object often heard of but difficult to understand <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is central to a [[Riemann hypothesis and prime numbers | million-dollar prize]] offered to anyone who can solve the [[Riemann hypothesis and prime numbers | Riemann hypothesis]], which concerns when the function equals zero <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Initial Definition of the Riemann Zeta Function

The [[Introduction to the Riemann zeta function | Riemann zeta function]], denoted as zeta(s), is initially defined as an infinite sum:
$$ \zeta(s) = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \dots $$
This sum continues indefinitely over all natural numbers <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. For example, if s equals 2, the sum becomes $1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots$, which converges to $\frac{\pi^2}{6}$ (approximately 1.645) <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This initial definition of the function only makes sense when the real part of `s` is greater than 1, as the sum converges in this domain <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Mathematician Bernard Riemann, a pioneer in complex analysis, focused on understanding the function when `s` is a [[Conceptualizing complex numbers | complex number]] <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. When a [[Conceptualizing complex numbers | complex value]] is plugged in for `s`, the terms in the sum are raised to a complex power, which involves rotation but does not change the lengths of the terms, ensuring convergence as long as the real part of `s` is greater than 1 <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Analytic Continuation and the Full Riemann Zeta Function

The infinite sum definition of the [[Introduction to the Riemann zeta function | Riemann zeta function]] is only valid for inputs `s` where the real part is greater than 1 <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. For other values, such as `s = -1`, the sum becomes $1 + 2 + 3 + 4 + \dots$, which obviously diverges <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. However, it is commonly stated that zeta(-1) equals -1/12 <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This seemingly nonsensical result is understood through a concept called analytic continuation <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Analytic continuation is the process of extending the definition of a complex function beyond its original domain where it was defined <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. For a function to be "analytic," it must have a derivative everywhere, which geometrically means it must preserve angles when mapping points from the input space to the output space <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. The surprising property of analytic functions is that if you extend such a function while requiring it to remain analytic, there is only one possible way to do so <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

The [[Introduction to the Riemann zeta function | Riemann zeta function]], defined by its infinite sum for `Re(s) > 1`, is an analytic function <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. Therefore, its definition for the rest of the complex plane is derived from this unique analytic continuation <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. This process explains how values like zeta(-1) = -1/12 are obtained <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

## Trivial Zeros of the Riemann Zeta Function

The "zeros" of the [[Introduction to the Riemann zeta function | Riemann zeta function]] are the points `s` for which $\zeta(s) = 0$ <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. One set of these zeros are the negative even numbers, such as -2, -4, -6, etc. <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. For example, $\zeta(-2) = 0$ <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. These are known as the **trivial zeros** <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

The term "trivial" is used by mathematicians to denote facts that are well-understood, even if they are not immediately obvious <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. Plugging these negative even numbers into the original infinite sum definition would yield wildly divergent results (e.g., $1 + 4 + 9 + 16 + \dots$ for `s = -2`), which certainly do not equal zero <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The fact that they are zeros comes from the analytically continued form of the function.

## The Riemann Hypothesis and Non-Trivial Zeros

Beyond the trivial zeros, the [[Riemann hypothesis and prime numbers | Riemann zeta function]] has other zeros, known as non-trivial zeros <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. These are all located within a vertical band in the complex plane called the **critical strip** <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. The specific placement of these non-trivial zeros contains surprising information about [[riemann_hypothesis_and_prime_numbers | prime numbers]] <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

The [[Riemann hypothesis and prime numbers | Riemann hypothesis]] states that all of these non-trivial zeros lie on a specific line within the critical strip, known as the **critical line**, where the real part of `s` is exactly one half <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. Proving this hypothesis would provide a remarkably tight grasp on the pattern of prime numbers and many other mathematical patterns <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. The critical line itself passes through zero many times under the zeta function transformation <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.