---
title: Importance of Eulers number e in calculus
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

Euler's number, denoted as `e`, is a fundamental mathematical constant with a value of approximately 2.71828 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Its importance in calculus stems primarily from its unique property regarding derivatives of exponential functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Derivatives of Exponential Functions

When considering the derivative of an exponential function like `a^t` (e.g., `2^t` or `3^t`), it is observed that its rate of change is proportional to the function itself <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

For a function `2^t`, the derivative `dm/dt` (rate of change of mass over time) can be analyzed by considering the expression:
`[2^(t + dt) - 2^t] / dt` <a class="yt-timestamp" data-t="00:3:19">[00:03:19]</a>

Utilizing a core property of exponentials, `a^(x+y) = a^x * a^y` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, this expression can be rewritten as:
`[2^t * 2^dt - 2^t] / dt` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>

Factoring out `2^t` yields:
`2^t * [(2^dt - 1) / dt]` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>

As `dt` approaches 0, the term `[(2^dt - 1) / dt]` approaches a specific constant value, approximately 0.6931 <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Therefore, the derivative of `2^t` is `2^t` multiplied by this constant <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This demonstrates that the derivative of `2^t` is proportional to itself <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

Similarly, for `3^t`, the proportionality constant is approximately 1.0986 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## The Defining Property of `e`

A crucial question in this context is whether there exists a base `a` for which the proportionality constant is exactly 1, meaning the derivative of `a^t` is simply `a^t` <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This special base is Euler's number, `e` <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

The property that the derivative of `e^t` is `e^t` is, in essence, what defines the number `e` itself <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a> <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. While all exponential functions are proportional to their own derivative, `e` is unique because its proportionality constant is 1 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

Graphically, this means that for the function `e^t`, the slope of the tangent line at any point on its graph is equal to the height (value) of that point above the horizontal axis <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

## `e` and the Natural Logarithm

The existence of `e` also explains the "mystery constants" observed with other bases. By applying the chain rule, the derivative of `e^(kt)` (where `k` is a constant) is `k * e^(kt)` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

Any number `a` can be expressed as `e^(ln a)`, where `ln` denotes the natural logarithm (the logarithm with base `e`) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a> <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

Therefore, a function like `2^t` can be rewritten as `e^(ln 2 * t)` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Applying the chain rule, the derivative of `e^(ln 2 * t)` is `ln 2 * e^(ln 2 * t)`, which simplifies to `ln 2 * 2^t` <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. The natural log of 2 is approximately 0.6931 <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>, confirming that the proportionality constant for `2^t` is `ln 2` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

In general, the proportionality constant for the derivative of `a^t` is simply the natural logarithm of the base, `ln a` <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Significance in Applications

Due to this elegant property, exponential functions in calculus applications are almost always expressed in terms of `e`, as `e^(kt)` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a> <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. While any exponential function can be written in multiple ways, using `e` gives the constant `k` in the exponent a clear and direct meaning <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a> <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

Many natural phenomena exhibit a rate of change that is proportional to the quantity itself <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>:
*   Population growth (assuming unlimited resources) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>
*   Cooling rates (proportional to temperature difference) <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>
*   Compound interest (rate of money growth proportional to amount) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>

In all these cases, the function describing the variable over time will be an exponential <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Expressing these functions as `e^(kt)` means that `k` directly represents the proportionality constant between the changing variable's size and its rate of change <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a> <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This makes `e` an indispensable constant for modeling natural processes that exhibit continuous growth or decay.