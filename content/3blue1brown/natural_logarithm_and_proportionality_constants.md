---
title: Natural Logarithm and Proportionality Constants
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

The study of [[Derivatives of Exponential Functions | derivatives of exponentials]] reveals a profound connection between the natural logarithm and the proportionality constants that arise when differentiating these functions <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This relationship highlights why the mathematical constant *e* is particularly important among all [[exponential growth and decay | exponential functions]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Derivatives of Exponential Functions

To understand the derivative of a function like 2<sup>x</sup>, consider it as a population mass, `m = 2^t`, where `t` is time <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This mass doubles every day <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The rate of change (`dm/dt`) is desired <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

When observing the growth over a full day, for example, from day 3 to day 4, the mass grows from 8 to 16, meaning 8 new creature masses are added <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This rate of growth is equal to the population size at the start of the day <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Similarly, from day 4 to day 5, it grows from 16 to 32, a rate of 16 new creature masses per day, which again equals the population size at the start <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This pattern suggests the [[Derivatives of Exponential Functions | derivative of 2 to the t]] might be equal to itself <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

However, for a true derivative, one must consider increasingly smaller changes in time (`dt`) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The fundamental property of exponents, `a^(t+dt) = a^t * a^dt`, is crucial here <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Applying this, the difference `2^(t+dt) - 2^t` divided by `dt` can be factored as `2^t * (2^dt - 1) / dt` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

As `dt` approaches 0, the term `(2^dt - 1) / dt` approaches a specific number, approximately **0.6931** <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This constant is independent of `t` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Thus, the derivative of 2<sup>t</sup> is **2<sup>t</sup> multiplied by this constant** <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
For a base of 3, the proportionality constant is approximately **1.0986** <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, and for a base of 8, it's about **2.079** <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. Notice that 2.079 is roughly three times 0.6931 <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## The Special Number *e*

A critical question arises: Is there a base for which this proportionality constant is exactly 1? <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> Yes, there is: the special constant *e*, approximately **2.71828** <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

*   **Definition of *e***: The number *e* is defined by the property that the derivative of *e*<sup>t</sup> is *e*<sup>t</sup> itself <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This means *e* is the only number whose [[exponential growth and decay | exponential function]] is its own derivative <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Geometric Property**: If you look at the graph of *e*<sup>t</sup>, the slope of the tangent line at any point equals the height of that point above the horizontal axis <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Derivatives of *e*<sup>kt</sup>

Using the chain rule, the derivative of *e*<sup>kt</sup> is the derivative of the outermost function (which is *e*<sup>kt</sup> itself) multiplied by the derivative of the inner function `kt` (which is `k`) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Therefore, the derivative of *e*<sup>kt</sup> is `k * e^kt` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This shows that functions proportional to their own derivative can be expressed in terms of *e* <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## The Natural Logarithm and Proportionality Constants

The mystery constants encountered earlier are explained by the [[Natural logarithm and its significance | natural log]]. Any number `a` can be written as `e^(ln a)` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This is simply the definition of the [[Natural logarithm and its significance | natural log]]: `ln a` asks "e to what power equals a?" <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

Therefore, the function 2<sup>t</sup> can be rewritten as *e*<sup>(ln 2 * t)</sup> <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. Based on the chain rule for *e*<sup>kt</sup>, the derivative of *e*<sup>(ln 2 * t)</sup> is proportional to itself, with a proportionality constant equal to **ln 2** <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
Indeed, if you calculate the [[Natural logarithm and its significance | natural log of 2]], it is approximately **0.6931** <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. This confirms the previously mysterious constant <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
In general, for any base `a`, the proportionality constant that appears when taking [[Derivatives of Exponential Functions | derivatives of other functions]] is simply the [[Natural logarithm and its significance | natural log of the base]] `ln a` <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Significance in Applications

In calculus, [[exponential growth and decay | exponential functions]] are almost always expressed as *e* to the power of some constant times `t` (e.g., *e*<sup>kt</sup>), rather than as `a^t` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. While algebraically equivalent <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, writing exponentials in terms of *e* gives the constant in the exponent a clear and readable meaning <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

Many [[Applications of Exponential Growth in Natural Phenomena | natural phenomena]] involve a rate of change that is proportional to the quantity itself <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>:
*   **[[Applications of Exponential Growth in Natural Phenomena | Population growth]]**: The rate of growth tends to be proportional to the population size <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Cooling**: The rate at which hot water cools is proportional to the temperature difference between the water and the room <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Investments**: The [[Applications of Exponential Growth in Natural Phenomena | rate at which it grows]] is proportional to the amount of money invested <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

In all these cases, the function describing the variable over time is an [[exponential growth and decay | exponential function]] <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. By expressing these functions as *e*<sup>kt</sup>, the constant `k` directly represents the **proportionality constant** between the size of the changing variable and its rate of change <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.