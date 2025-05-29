---
title: Proportionality constants in exponential functions
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

In the study of [[calculus_and_exponential_functions | calculus]], understanding [[derivatives_of_exponential_functions | derivatives of exponential functions]] is crucial <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This article explores the concept of proportionality constants that arise when differentiating exponential functions like `2^x` or `7^x`, and explains why `e^x` holds a special significance <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Intuition Behind Growth

To build an [[intuition_behind_the_growth_of_exponential_functions | intuition]], consider the function `2^t`, where `t` represents time in days and `2^t` represents the total mass of a population of pie creatures that doubles every day <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This continuous mass better reflects the function's continuity compared to discrete population counts <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

*   At `t = 0`, the mass is `2^0 = 1` creature mass <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   At `t = 1` day, it grows to `2^1 = 2` creature masses <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   At `t = 2` days, it's `2^2 = 4` creature masses, continuing to double daily <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

When observing the rate of change over a full day (e.g., from day 3 to day 4, where mass grows from 8 to 16), the growth rate is 8 new creature masses per day, which equals the population size at the start of that day <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This pattern holds true for any full-day interval <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This might lead one to *tentatively* conclude that the derivative of `2^t` is `2^t` itself, meaning its rate of change equals its current value <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. However, this is not entirely accurate <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## The True Rate of Change

For a precise derivative, we need to consider infinitesimally small changes in time (`dt`), not full-day intervals <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The derivative `dm/dt` requires evaluating the limit of `(2^(t+dt) - 2^t) / dt` as `dt` approaches zero <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

A core [[properties_of_the_exponential_function | property of exponentials]] allows `2^(t+dt)` to be broken down as `2^t * 2^dt` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This factorization is key because it allows the term `2^t` to be factored out from the numerator <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, resulting in:

`2^t * (2^dt - 1) / dt` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>

As `dt` approaches 0, the term `(2^dt - 1) / dt` approaches a specific constant value, approximately `0.6931` <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This constant is independent of `t` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Therefore, the derivative of `2^t` is `2^t` multiplied by this constant:

`d/dt (2^t) = 0.6931 * 2^t` <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>

This means the rate of change for `2^t` is proportional to itself, with `0.6931` as the proportionality constant <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Generalization and the Special Number `e`

This principle applies to any exponential function `a^t`. For example:

*   The derivative of `3^t` is `1.0986 * 3^t` <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   The derivative of `8^t` is `2.079 * 8^t` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

These proportionality constants are not random; they follow a pattern <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. For instance, the constant for `8^t` (2.079) is exactly three times the constant for `2^t` (0.6931) <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

A crucial question then arises: Is there a base `a` for which this proportionality constant is exactly 1? <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>

### The Role of `e`

The answer is yes: the special constant `e`, approximately `2.71828` <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. The number `e` is *defined* by this property <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

> All exponential functions are proportional to their own derivative, but e alone is the special number so that proportionality constant is 1, meaning e to the t actually equals its own derivative. <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>

Graphically, this means that for `e^t`, the slope of the tangent line at any point equals the height of that point above the horizontal axis <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Explaining the Mystery Constants

The existence of `e` helps explain the other constants through the [[calculus_and_exponential_functions | chain rule]]:

1.  **Chain Rule Example**: The derivative of `e^(3t)` is `e^(3t)` (derivative of the outer function) multiplied by `3` (derivative of the inner function, `3t`) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. So, `d/dt (e^(3t)) = 3 * e^(3t)` <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. This shows that `e` raised to `constant * t` results in that same `constant` times itself <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

2.  **Rewriting Bases with `e`**: Any number, such as 2, can be written as `e` raised to the [[natural_logarithms_and_exponential_growth | natural logarithm]] of that number <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. For example:
    *   `2 = e^(ln 2)` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
    *   Therefore, `2^t = (e^(ln 2))^t = e^((ln 2) * t)` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

    Applying the chain rule to `e^((ln 2) * t)`, the derivative is `ln(2) * e^((ln 2) * t)`. Since `e^((ln 2) * t)` is equal to `2^t`, the derivative of `2^t` is `ln(2) * 2^t` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

    If you calculate `ln(2)`, you get approximately `0.6931` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. This confirms that the "mystery proportionality constant" for any base `a` is simply the [[natural_logarithms_and_exponential_growth | natural logarithm]] of that base (`ln a`) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Significance in Applications

In practical applications of [[calculus_and_exponential_functions | calculus]], [[exponential_growth_and_decay | exponential functions]] are almost always written in the form `e^(kt)` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. While `2^t` can be written as `e^((ln 2) * t)`, using `e` makes the constant `k` more meaningful <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

Many [[natural_phenomena_and_their_relationship_with_exponentials | natural phenomena]] involve a rate of change directly proportional to the quantity changing <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. Examples include:

*   **Population Growth**: The rate of growth of a population is proportional to its current size <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Cooling**: The rate at which an object cools is proportional to the temperature difference between the object and its surroundings <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Investments**: The rate at which money grows is proportional to the amount invested <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

In all these cases, the variable over time will be described by some kind of [[exponential_growth_and_decay | exponential function]] <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. By expressing these functions as `e^(kt)`, the constant `k` directly represents the proportionality constant between the changing variable's size and its rate of change <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.