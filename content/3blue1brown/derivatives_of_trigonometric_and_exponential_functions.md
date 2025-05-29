---
title: Derivatives of trigonometric and exponential functions
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

The principles of [[derivatives_and_integrals | derivatives]] can be applied to find the rates of change for both [[exponential_functions_and_their_properties | exponential]] and [[graphing_trigonometric_functions_and_making_predictions | trigonometric functions]]. This involves understanding how these functions change with respect to their inputs.

## [[exponential_functions_and_their_properties | Exponential Functions]]

### Derivative of $e^x$
The derivative of the natural [[exponential_functions_and_their_properties | exponential function]], $e^x$, is uniquely its own function <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
$$ \frac{d}{dx} (e^x) = e^x $$

### Derivative of $ln(x)$
The natural logarithm, $ln(x)$, is the inverse function of $e^x$ <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. Its derivative can be found using a technique called implicit differentiation <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>:
1.  Start with the equation defining the natural logarithm: $y = ln(x)$ <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
2.  Rearrange this equation into its [[exponential_functions_and_their_properties | exponential form]]: $e^y = x$ <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This means "e to the what equals x" <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
3.  Take the derivative of both sides of $e^y = x$ with respect to x. This asks how a tiny step with components $dx$ and $dy$ changes the value of each side <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
    *   The derivative of the left side, $e^y$, with respect to x (using the chain rule) is $e^y \cdot dy$ <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
    *   The derivative of the right side, $x$, with respect to x is $dx$ <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
4.  Equate the derivatives of both sides: $e^y \cdot dy = dx$ <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
5.  Rearrange to solve for $\frac{dy}{dx}$, which represents the slope of the graph and thus the derivative of $ln(x)$: $\frac{dy}{dx} = \frac{1}{e^y}$ <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
6.  Since $e^y = x$ when on the curve of $y = ln(x)$, substitute $x$ back into the expression: $\frac{dy}{dx} = \frac{1}{x}$ <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

Thus, the derivative of $ln(x)$ is:
$$ \frac{d}{dx} (ln(x)) = \frac{1}{x} $$

## [[derivative_of_trigonometric_functions_with_unit_circle_analysis | Trigonometric Functions]]

### Derivative of $sin(x)$
When considering expressions involving [[graphing_trigonometric_functions_and_making_predictions | trigonometric functions]], their [[taking_derivatives_of_complex_combinations_of_functions | derivatives]] are found using standard rules. For example, in an equation like $sin(x) \cdot y^2 = x$, taking the derivative of $sin(x)$ is part of applying the [[taking_derivatives_of_complex_combinations_of_functions | product rule]] <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. The change to $sin(x)$ is $cos(x) \cdot dx$ <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

Thus, the derivative of $sin(x)$ is:
$$ \frac{d}{dx} (sin(x)) = cos(x) $$