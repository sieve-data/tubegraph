---
title: Chain Rule and Exponential Functions
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

Calculus involves understanding the rate of change of functions, and among these, [[Derivatives of Exponential Functions | exponential functions]] like `2^x` or `7^x` are particularly important <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. A key aspect is understanding why Euler's number, `e`, is considered the most significant base for exponentials <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Intuition: The Derivative of an Exponential Function

To build intuition, consider the function `2^t`, where `t` represents time in days and `2^t` represents the total mass of a population of "pie creatures" that doubles daily <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Using mass helps reflect the continuity of the function, unlike discrete population counts <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

At `t=0` days, the mass is `2^0 = 1` unit <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. At `t=1` day, it grows to `2^1 = 2` units <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, and at `t=2` days, it's `2^2 = 4` units <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The derivative, `dm/dt`, represents the rate at which this population mass is growing <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
Over a full day, for instance, between day 3 and day 4, the mass grows from 8 to 16, representing a growth of 8 new units per day <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This rate equals the population size at the start of the day <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Similarly, between day 4 and day 5, it grows from 16 to 32, a rate of 16 new units per day, again equal to the starting population size <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

It might be tempting to conclude that the derivative of `2^t` is simply `2^t` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, meaning the rate of change is equal to the function's value <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. However, this observation is based on changes over a full day (`2^(t+1)` vs `2^t`) <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. For a true derivative, we must consider increasingly small changes in time, `dt` <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The derivative is defined by the limit of `(2^(t+dt) - 2^t) / dt` as `dt` approaches `0` <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Key Property of Exponentials

A core property of [[Exponential functions and their properties | exponentials]] is that `a^(x+y) = a^x * a^y` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This allows us to rewrite `2^(t+dt)` as `2^t * 2^dt` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This property links additive concepts (tiny time steps) to multiplicative concepts (rates and ratios) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

Applying this, the derivative expression becomes:
`lim (dt→0) [ (2^t * 2^dt - 2^t) / dt ]`
`= lim (dt→0) [ 2^t * (2^dt - 1) / dt ]` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

Crucially, the term `(2^dt - 1) / dt` is separate from `t`; it only depends on `dt` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. As `dt` approaches `0`, this term approaches a constant value, approximately `0.6931` <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

Therefore, the derivative of `2^t` is `2^t` multiplied by this constant: `d/dt (2^t) = 0.6931 * 2^t` <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>, <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. This shows that the rate of change is proportional to the function's value itself <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

For other bases, like `3^t`, the derivative is `1.0986 * 3^t` <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>, <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>, <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. For `8^t`, the constant is `2.079` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. Notably, `2.079` is approximately `3` times `0.6931` <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## The Special Constant `e`

A natural question arises: Is there a base `a` for which the proportionality constant is exactly `1`, meaning `d/dt (a^t) = a^t`? <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

Yes, there is such a number: `e`, approximately `2.71828` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This is precisely what defines `e`: it is the unique number such that the derivative of `e^t` is `e^t` itself <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>, <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>, <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Geometrically, for the graph of `e^t`, the slope of the tangent line at any point equals the height of that point above the horizontal axis <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>, <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## The Chain Rule and Proportionality Constants

The existence of `e` helps explain the mystery constants for other exponential bases. This involves the [[Chain rule application in machine learning | chain rule]] <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>, <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

Consider the derivative of `e^(3t)`:
1.  Take the derivative of the outermost function (`e^u`), which is itself: `e^(3t)` <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>, <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
2.  Multiply by the derivative of the inner function (`3t`), which is `3` <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
So, `d/dt (e^(3t)) = 3 * e^(3t)` <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

In general, `d/dt (e^(ct)) = c * e^(ct)` <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>, <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

The connection to other bases comes from algebraic manipulation. Any positive number `a` can be written as `e^(ln(a))` by definition of the natural logarithm (where `ln(a)` is the power to which `e` must be raised to equal `a`) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>, <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>, <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

Thus, `2^t` can be rewritten as `(e^(ln(2)))^t = e^(ln(2) * t)` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
Using the [[Chain rule application in machine learning | chain rule]] and the property of `e^t`, the derivative of `2^t` is `ln(2) * e^(ln(2) * t)`, which simplifies to `ln(2) * 2^t` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>, <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
Indeed, `ln(2)` is approximately `0.6931`, the constant found earlier <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>, <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

This pattern holds for all bases: the proportionality constant when taking the derivative of `a^t` is simply `ln(a)` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>, <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>, <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>, <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

### Practical Significance

In calculus applications, [[Exponential functions and their properties | exponential functions]] are almost always written as `e^(ct)` instead of `a^t` <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>, <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>, <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. While `a^t` and `e^(ln(a)t)` are mathematically equivalent ways to express the same [[exponential growth and decay | exponential growth]] function <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>, <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>, using `e` provides a "readable meaning" to the constant `c` in the exponent <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>, <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

Many natural phenomena exhibit a rate of change proportional to the quantity itself <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>, <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Examples include:
*   Population growth (when resources are unlimited) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>, <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>, <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
*   Cooling of a hot object (rate of temperature difference change is proportional to the difference itself) <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>, <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>, <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   Investment growth (rate of growth proportional to current amount) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>, <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>, <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

In all these cases, the function describing the variable over time will be an exponential <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>, <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>, <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. Choosing to express these functions as `e^(ct)` means that the constant `c` directly represents the proportionality constant between the variable's size and its rate of change <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>, <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>, <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>, <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.