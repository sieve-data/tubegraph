---
title: Visualization of the Riemann zeta function
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_the_riemann_zeta_function | Riemann zeta function]] is a significant object in modern mathematics, often perceived as difficult to understand despite its widespread recognition <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It's notably associated with a one-million-dollar prize for solving the [[the_riemann_hypothesis_and_trivial_zeros | Riemann hypothesis]], which concerns when the function equals zero <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The function also appears in discussions about the divergent sum `1 + 2 + 3 + 4...` equaling `-1/12`, a concept that utilizes the [[introduction_to_the_riemann_zeta_function | Riemann zeta function]]'s definition <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Understanding the zeta function, particularly its extended definition, often involves the concept of analytic continuation, which can be unintuitive and opaque <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This article aims to visually explain the zeta function and analytic continuation <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Defining the Zeta Function

The [[introduction_to_the_riemann_zeta_function | Riemann zeta function]], denoted as `ζ(s)`, is initially defined as an infinite sum for a given input `s` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>:

`ζ(s) = 1/1^s + 1/2^s + 1/3^s + 1/4^s + ...` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

For example, when `s = 2`, the sum becomes `1 + 1/4 + 1/9 + 1/16 + ...`, which converges to `π²/6`, approximately `1.645` <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This convergence, where smaller and smaller amounts are added to approach a specific number, makes the function seem reasonable for certain inputs <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### The Problem with Divergent Sums

However, difficulties arise when considering inputs like `s = -1`. Plugging this into the sum yields `1 + 2 + 3 + 4 + ...`, which obviously does not approach `-1/12` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Similarly, for `s = -2`, the sum becomes `1 + 4 + 9 + 16 + ...`, which clearly doesn't approach zero, despite [[the_riemann_hypothesis_and_trivial_zeros | trivial zeros]] of the function being stated at negative even numbers like `ζ(-2) = 0` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Initially, the zeta function is only defined for `s > 1`, where the sum converges <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Complex Inputs and Exponents

Bernard Riemann's work focused on understanding the zeta function when `s` is a [[geometric_interpretation_of_complex_numbers | complex number]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Raising a number to a complex power like `n^s` involves splitting it into a real part and an imaginary part <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For example, `(1/2)^(2+i)` is `(1/2)^2 * (1/2)^i` <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

The key takeaway is that `n` raised to a pure imaginary number (e.g., `(1/2)^i`) results in a [[geometric_interpretation_of_complex_numbers | complex number]] on the unit circle in the complex plane <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. This operation rotates a number without changing its magnitude <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

When `s` is a complex number with a real part greater than 1 (e.g., `2 + i`), the terms in the zeta sum `1/n^s` still have decreasing magnitudes, allowing the sum to converge <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The imaginary part of `s` simply rotates each term, causing the sum to converge in a spiral on the complex plane <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This means `ζ(s)` is a well-defined complex function as long as the real part of `s` is greater than 1 <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## Visualizing Complex Functions as Transformations

A powerful way to understand complex functions is to visualize them as transformations <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This involves observing how every possible input point in the complex plane moves to its corresponding output point <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

For instance, consider `f(s) = s^2` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>:
- `s = 2` moves to `4` <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
- `s = -1` moves to `1` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
- `s = i` moves to `-1` <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

When a grid representing the input complex plane is transformed by `f(s) = s^2`, it provides a rich [[visualization_in_calculus | visual]] representation of the function's behavior <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### Visualizing the Zeta Function's Initial Domain

Applying this [[visualization_in_calculus | visualization]] technique to the [[introduction_to_the_riemann_zeta_function | Riemann zeta function]] for inputs where the real part of `s` is greater than 1 reveals a complex and beautiful transformation of the complex plane <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. The lines representing imaginary parts, for example, transform into intricate arcs that abruptly stop at the boundary where the real part of `s` equals 1 <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. This prompts a desire to "continue" these arcs <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

## Analytic Continuation

The concept of "analytic continuation" addresses this desire to extend a function beyond its original domain <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. When the real part of `s` is less than 1, the infinite sum definition of the zeta function no longer makes sense <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. While it might seem possible to extend the function in infinitely many ways <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>, there's a crucial constraint that makes the extension unique: the requirement that the extended function must have a [[derivative_of_polynomial_functions_using_geometric_visualization | derivative]] everywhere <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### The Angle-Preserving Property of Analytic Functions

For complex functions, having a [[derivative_of_polynomial_functions_using_geometric_visualization | derivative]] everywhere (being "analytic") has a strong [[geometric_interpretation_of_complex_numbers | geometric interpretation]] <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. If any two lines in the input space intersect at a certain angle, after the transformation by an analytic function, their corresponding transformed curves will still intersect at the *same* angle <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This "angle-preserving" property is highly restrictive <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

The surprising fact is that if an analytic function (like the zeta function on its initial domain) is to be extended beyond its original definition while remaining analytic, there is only *one possible* way to do it, if an extension exists at all <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. This process of extending an analytic function uniquely while preserving its analytic property is called analytic continuation <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

### The Full Riemann Zeta Function

The full [[introduction_to_the_riemann_zeta_function | Riemann zeta function]] is thus defined in two parts <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>:
1.  For `s` values where the real part is greater than 1, it's defined by the converging infinite sum <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
2.  For the rest of the complex plane, it's defined by the unique analytic continuation of that sum <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

This definition is implicit, relying on the guaranteed uniqueness of the analytic continuation <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.

## The Riemann Hypothesis

The [[the_riemann_hypothesis_and_trivial_zeros | Riemann hypothesis]] is a million-dollar problem concerning the "zeros" of the zeta function—the points that get mapped to zero after the transformation <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

### Trivial Zeros
It is known that the negative even numbers (e.g., `-2, -4, -6...`) are mapped to zero <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. These are called [[the_riemann_hypothesis_and_trivial_zeros | trivial zeros]] <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. The term "trivial" reflects mathematicians' understanding of these points, even if they aren't immediately obvious from the original sum <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

### Non-Trivial Zeros and the Critical Line
All other zeros of the function, known as non-trivial zeros, lie within a vertical region called the "critical strip" <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. The exact placement of these zeros encodes surprising information about [[riemann_hypothesis_and_prime_numbers | prime numbers]] <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.

Riemann hypothesized that all of these non-trivial zeros sit precisely on the line where the real part of `s` is one-half <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. This is known as the "critical line" <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. If proven true, this hypothesis would provide a remarkably tight understanding of the pattern of [[riemann_hypothesis_and_prime_numbers | prime numbers]] and many other mathematical patterns <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

When the critical line is transformed by the zeta function, it is observed to pass through zero many times <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. Proving that all non-trivial zeros lie on this line is the challenge of the [[the_riemann_hypothesis_and_trivial_zeros | Riemann hypothesis]] <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

### Zeta of Negative One

Another consequence of the analytic continuation is that `ζ(-1)` maps to `-1/12` <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. This value arises from the unique solution of the analytic continuation "jigsaw puzzle" across the complex plane, not directly from the divergent sum `1 + 2 + 3 + ...` <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. The uniqueness of this continuation suggests a deep, intrinsic connection between these extended values and the original sum <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.