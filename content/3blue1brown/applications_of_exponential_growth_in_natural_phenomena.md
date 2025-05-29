---
title: Applications of Exponential Growth in Natural Phenomena
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

[[exponential growth and decay | Exponential functions]], such as 2^x or 7^x, are crucial in describing various natural phenomena where the rate of change of a quantity is proportional to the quantity itself <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

## Intuition from Population Growth
Consider a function where the input is time (t) in days and the output is a population mass, like a "fertile band of pie creatures" that doubles every day <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Using mass instead of discrete population size better reflects the continuity of [[exponential functions and their properties | this function]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

For example:
*   At t=0, mass = 2^0 = 1 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   At t=1 day, mass = 2^1 = 2 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   At t=2 days, mass = 2^2 = 4 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
The population mass doubles every day <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Rate of Change (Derivative)
The derivative (dm/dt) represents the rate at which this population mass grows <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
If we observe the growth over a full day (e.g., between day 3 and day 4), the mass grows from 8 to 16, adding 8 new creature masses. This rate of growth (8 per day) equals the population size at the start of that day <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Similarly, between day 4 and day 5, it grows from 16 to 32, a rate of 16 new masses per day, which again matches the starting population size <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

This observation suggests that the derivative of 2^t might be equal to itself <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. However, for a true derivative, we must consider infinitesimally small changes (dt), not full-day increments <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Derivatives of Exponential Functions
The core property of exponentials, a^(t+dt) = a^t * a^dt, allows us to analyze the derivative <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
The derivative of a function like 2^t is found by evaluating the limit of (2^(t+dt) - 2^t) / dt as dt approaches 0 <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
This can be simplified to:
`2^t * ((2^dt - 1) / dt)` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

As dt approaches 0, the term `(2^dt - 1) / dt` approaches a specific constant value, approximately 0.6931 <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
Therefore, the [[Derivatives of Exponential Functions | derivative of 2^t]] is 2^t multiplied by this constant <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This means the rate of change is proportional to the function's value itself <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

Similarly, for 3^t, the [[Natural Logarithm and Proportionality Constants | proportionality constant]] is approximately 1.0986 <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>, <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### The Special Constant 'e'
A key question is whether there's a base `a` for which the [[Natural Logarithm and Proportionality Constants | proportionality constant]] is exactly 1, meaning the derivative of a^t is simply a^t <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This special number is **e**, approximately 2.71828 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

This property defines `e`: it is the only number for which the [[Derivatives of Exponential Functions | derivative of e^t]] is equal to e^t <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>, <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Geometrically, the slope of the tangent line to the graph of e^t at any point equals the height of that point above the horizontal axis <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

### Connecting to Natural Logarithms
The mystery of the [[Natural Logarithm and Proportionality Constants | proportionality constants]] is resolved by the [[Chain Rule and Exponential Functions | chain rule]] and the natural logarithm. Any base `a` can be written as e^(ln a) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
So, a function like 2^t can be expressed as e^(ln 2 * t) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
Using the [[Chain Rule and Exponential Functions | chain rule]], the derivative of e^(kt) is k * e^(kt) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
Therefore, the derivative of 2^t (or e^(ln 2 * t)) is (ln 2) * e^(ln 2 * t), which simplifies to (ln 2) * 2^t <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. The constant (ln 2) is indeed approximately 0.6931 <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>, <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This means the [[Natural Logarithm and Proportionality Constants | proportionality constant]] for any base is simply the natural log of that base <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>, <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Why 'e' is Preferred in Applications
In calculus applications, [[exponential functions and their properties | exponentials]] are almost always written as e^(kt), where 'k' is a constant <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>, <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. While any exponential function can be written in this form, this choice gives the constant 'k' a clear and natural meaning <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>, <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

It represents the [[Natural Logarithm and Proportionality Constants | proportionality constant]] between the size of the changing variable and its rate of change <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

### Examples in Natural Phenomena
Many natural phenomena are characterized by a rate of change proportional to the quantity itself <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>, <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>, <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. The functions describing these variables over time are always exponential <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

*   **Population Growth**: The rate of growth of a population tends to be proportional to its current size, assuming no resource limitations <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>, <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This is a common application in [[mathematical modeling of epidemics | mathematical modeling of epidemics]] and biological growth.
*   **Cooling/Heating**: The rate at which a hot object cools in a cooler room is proportional to the temperature difference between the object and the room <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>, <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **Financial Investment**: The rate at which invested money grows is proportional to the amount of money present at any given time <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>, <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

The consistent appearance of exponential functions in describing such diverse phenomena highlights the [[the_unreasonable_effectiveness_of_mathematics_in_the_natural_sciences | unreasonable effectiveness of mathematics in the natural sciences]].