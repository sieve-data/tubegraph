---
title: Riemann hypothesis
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 

The [[riemann_zeta_function|Riemann zeta function]] is a significant object in modern mathematics <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. A substantial prize of one million dollars is offered to anyone who can determine when this function equals zero, a challenge known as the Riemann hypothesis <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## The [[riemann_zeta_function|Riemann Zeta Function]]

The [[riemann_zeta_function|Riemann zeta function]], commonly denoted as `ζ(s)`, is initially defined for a given input `s` as an infinite sum over all natural numbers <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>:
ζ(s) = 1/1^s + 1/2^s + 1/3^s + 1/4^s + ... <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

For example, when `s = 2`, the sum becomes 1 + 1/4 + 1/9 + 1/16 + ... <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. This series converges to π²/6, approximately 1.645 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This sum converges, and the function makes sense, only when the real part of `s` is greater than 1 <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Divergent Sums and the Zeta Function

Some might encounter the [[riemann_zeta_function|Riemann zeta function]] in the context of the divergent sum 1 + 2 + 3 + 4 + ... up to infinity <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. There is a sense in which this sum equals -1/12 <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This seemingly nonsensical result is defined using the [[riemann_zeta_function|Riemann zeta function]] through a concept called analytic continuation <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

If one were to plug `s = -1` into the original infinite sum definition, it would result in 1 + 2 + 3 + 4 + ..., which clearly does not approach -1/12 <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Similarly, for `s = -2`, the sum 1 + 4 + 9 + 16 + ... does not approach zero <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This highlights the need for an extended definition beyond the initial sum.

## Analytic Continuation

Bernard Riemann significantly contributed to complex analysis, the study of functions with complex number inputs and outputs <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. His focus was on understanding the [[riemann_zeta_function|Riemann zeta function]] when `s` is a complex value <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

The process of extending an analytic function beyond its original domain, in a way that preserves its *analyticity*, is called **analytic continuation** <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

### Visualizing Complex Functions

Complex functions can be visualized as transformations, where every possible input point moves to its corresponding output point <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. For the [[riemann_zeta_function|Riemann zeta function]], the initial sum definition is valid for inputs `s` where the real part of `s` is greater than 1 (the right half of the complex plane) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. When visualized, this transformed grid on the right half-plane appears to "beg" for extension <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

### Analyticity: The Angle-Preserving Property

A crucial property of complex functions is their derivative. Functions that have a derivative everywhere are called **analytic** <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. Geometrically, this means that if two lines in the input space intersect at a certain angle, they will still intersect at that same angle after the transformation by the function <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>, <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This can be observed by how grid lines, after transformation, still intersect at right angles <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>, <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

This angle-preserving property is very restrictive <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. The surprising fact is that if an analytic function needs to be extended beyond its initial domain, requiring the new extended function to *still be analytic* forces a unique possible extension, if one exists <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>, <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

The full [[riemann_zeta_function|Riemann zeta function]] is defined in two parts <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>:
1.  For `s` where the real part is greater than 1, it's defined by the converging infinite sum <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
2.  For the rest of the complex plane, it's defined as the unique analytic continuation of that sum <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>, <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

## The Riemann Hypothesis and its Zeros

The Riemann hypothesis concerns the points where the [[riemann_zeta_function|Riemann zeta function]] equals zero, meaning points that get mapped to the origin after the transformation <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>, <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

### Trivial Zeros
One known property of the extended function is that the negative even numbers (`-2`, `-4`, `-6`, ...) are mapped to zero <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. These are referred to as "trivial zeros" <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Non-Trivial Zeros and the Critical Strip
The remaining points that map to zero are located within a vertical region called the **critical strip** <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>, <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. The specific placement of these non-trivial zeros contains surprising information about [[distribution_of_prime_numbers_and_dirichlets_theorem|prime numbers]] <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>, <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

### The Hypothesis
Riemann hypothesized that all of these non-trivial zeros lie precisely on the line where the real part of `s` is one half <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>, <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. This line is known as the **critical line** <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

If this hypothesis is proven true, it would provide a significantly deeper understanding of the pattern of [[distribution_of_prime_numbers_and_dirichlets_theorem|prime numbers]] and impact numerous other mathematical results that depend on its truth <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>, <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>, <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. The transformed critical line passes through zero multiple times <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>, <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.