---
title: Infinite sums and approximations
videoId: r6sGWTCMz2k
---

From: [[3blue1brown]] <br/> 

The concept of infinite sums is central to understanding how complex functions and shapes can be represented by simpler components, particularly within the framework of Fourier series <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Approximation with Finite Sums
When functions, such as a step function used to model heat distribution, are approximated by a sum of basic waves (like sine waves), these are initially just approximations <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. A finite sum of continuous sine waves can never perfectly replicate features like a flat line (unless it's a constant function) or a discontinuity <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This limitation highlights the necessity of considering infinite sums for accurate representations <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Defining Infinite Sums
An infinite sum involves adding an unending sequence of terms. Its meaning can sometimes seem vague <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. In the context of numbers, an infinite sum implies that as more terms are added, the sequence of partial sums approaches a specific value, getting arbitrarily close and staying that close to it <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. For example, a sum of fractions can equal [[rational_approximations_for_pi | pi divided by 4]], even though each partial sum is rational <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This concept, known as [[concept_of_infinite_sums_and_convergence | convergence]], is abbreviated by simply stating "the infinite sum equals" the limit value <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Infinite Sums in Functions
The principle extends to functions, where an infinite sum of terms can represent a target function across its domain <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. For instance, an infinite sum of scaled cosine functions can approximate a step function, approaching different values depending on the input <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Handling Discontinuities
A significant insight is that while finite sums of continuous functions remain continuous, an infinite sum of continuous functions can result in a discontinuous function <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This qualitative change is only possible through the use of limits <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. For a step function, the infinite sum might dictate a specific value (e.g., 0) at the point of discontinuity, which can be an awkward but necessary prescription for strict mathematical equality <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Application in Fourier Series
The core idea behind Fourier series is to break down any function into a sum of simple oscillations <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This involves determining specific coefficients (constants) for each oscillating term <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. In the context of complex Fourier series, these oscillations are represented by rotating vectors, which are fundamentally linked to complex exponentials <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

The process of finding these coefficients involves [[evaluating_integrals_and_the_role_of_the_convergence_point | integrating]] the function <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. This integration acts as a "continuous average," effectively isolating the desired constant term by canceling out all other oscillating components, as their averages over a full cycle are zero <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. For higher-frequency terms, the function is first multiplied by a complex exponential that "holds still" the target vector, allowing its coefficient to be isolated through integration <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.

When these infinitely many solutions (exponentially decaying cosine waves from the heat equation context) are summed up, they provide an exact solution for how a discontinuous initial condition, like a step function, would evolve over time <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Numerical Approximation
In practice, these infinite sums are approximated by using a finite number of terms. For example, animations of complex Fourier series often use a limited range of rotating vectors (e.g., 101 vectors for n from -50 to 50) <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>. The integrals required to find the coefficients are typically computed numerically, by dividing the input interval into small pieces and summing discrete values <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. As the number of vectors (terms) used approaches infinity, the approximation of the original path or function becomes increasingly accurate <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

This use of [[approximation_of_functions_using_taylor_series | infinite sums to approximate functions]] is a fundamental concept in [[approximating_solutions_using_calculus | calculus]] and [[mathematical_insights_and_elegant_solutions | mathematical analysis]], demonstrating how infinite mathematical constructs can precisely describe complex phenomena <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.