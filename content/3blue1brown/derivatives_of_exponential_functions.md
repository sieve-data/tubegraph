---
title: Derivatives of Exponential Functions
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

Exponential functions, such as 2^x or 7^x, are a crucial topic in the study of [[derivatives and integrals | derivatives]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Among these, the [[exponential functions and their properties | exponential function]] e^x holds particular significance <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Intuition with 2^t (Pie Creature Population)

To understand the [[derivatives of trigonometric and exponential functions | derivative of exponential functions]], consider the function 2^t, where 't' represents time in days and '2^t' represents the total mass of a population of "pie creatures" that doubles daily <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This continuous mass representation is preferred over discrete population size for clarity when discussing tiny changes <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

*   At t=0 days, the mass is 2^0 = 1 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   At t=1 day, the mass is 2^1 = 2 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   At t=2 days, the mass is 2^2 = 4 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The derivative, dm/dt, represents the rate at which this population mass is growing <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Growth over a Full Day

Observing the growth over a full day:
*   Between day 3 and day 4, the mass grows from 8 to 16, an addition of 8 new creature masses <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This rate of growth (8 per day) equals the population size at the start of day 3 <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   Between day 4 and day 5, it grows from 16 to 32, a rate of 16 new creature masses per day, which equals the population size at the start of day 4 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

This pattern suggests that the rate of growth over a full day equals the population size at the start of that day <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. It might be tempting to conclude that the derivative of 2^t is 2^t itself <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. However, this is based on comparing changes over a full day (2^(t+1) versus 2^t), whereas a true derivative requires considering infinitesimally small changes (dt) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## Algebraic Derivation

To find the derivative of 2^t, we want to evaluate the limit as dt approaches 0 of the expression:
$$ \frac{2^{t+dt} - 2^t}{dt} $$ <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>

A key property of [[exponential functions and their properties | exponentials]] is that `2^(t+dt)` can be broken down as `2^t * 2^dt` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This property connects additive changes in the exponent (like tiny steps in time) to multiplicative changes in the output (like rates) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Substituting this into the expression, we can factor out 2^t:
$$ 2^t \times \frac{2^{dt} - 1}{dt} $$ <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

As dt approaches 0, the term `(2^dt - 1) / dt` approaches a specific constant value, approximately 0.6931 <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This constant is independent of 't' <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

Therefore, the derivative of 2^t is `2^t` multiplied by this constant <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This means the rate of change of 2^t is not exactly equal to itself, but proportional to itself <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Generalization and the Constant *e*

This pattern holds for other bases as well:
*   The derivative of 3^t is proportional to 3^t, with a constant of approximately 1.0986 <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   The derivative of 8^t is proportional to 8^t, with a constant of approximately 2.079 <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### The Special Case of *e*

A critical question arises: Is there a base for which this proportionality constant is exactly 1? <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>

Yes, this special base is the constant *e*, approximately 2.71828 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. The property that its derivative is equal to itself (i.e., the proportionality constant is 1) defines *e* <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

This means:
$$ \frac{d}{dt}(e^t) = e^t $$ <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>

Graphically, the slope of the tangent line to the graph of e^t at any point equals the height of that point above the horizontal axis <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Explaining the Mystery Constants with the [[Chain Rule and Exponential Functions | Chain Rule]]

The existence of *e* helps explain the mystery constants seen earlier. This involves using the [[chain_rule_and_exponential_functions | chain rule]] <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

For example, to find the derivative of e^(3t):
1.  Take the derivative of the outermost function (e^u), which is itself: e^(3t) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
2.  Multiply by the derivative of the inner function (3t), which is the constant 3 <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

So, `d/dt(e^(3t)) = 3 * e^(3t)` <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. In general, `d/dt(e^(kt)) = k * e^(kt)`.

Now, we can relate any exponential function to *e*:
The number 2 can be written as `e^(ln 2)` by definition of the natural logarithm <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
Therefore, the function 2^t can be rewritten as `(e^(ln 2))^t = e^(ln 2 * t)` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

Using the [[chain_rule_and_exponential_functions | chain rule]] on `e^(ln 2 * t)`:
$$ \frac{d}{dt}(e^{(\ln 2)t}) = (\ln 2) \times e^{(\ln 2)t} = (\ln 2) \times 2^t $$ <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>

If you calculate ln 2, it is approximately 0.6931, which is exactly the mystery constant we found earlier for the derivative of 2^t <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

Thus, for any base 'b', the derivative of b^t is `(ln b) * b^t` <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. The proportionality constant is simply the natural logarithm of the base <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Significance in Applications

In calculus applications, exponentials are typically written in the form `e^(kt)` rather than `b^t` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This is because the constant 'k' in the exponent `e^(kt)` has a direct and readable meaning: it is the proportionality constant between the changing variable and its rate of change <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

This form is especially useful for phenomena where the rate of change is proportional to the quantity itself, which is characteristic of [[exponential growth and decay | exponential growth and decay]]. Examples include:
*   Population growth where resources are not limited <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   The cooling rate of hot water in a cooler room, proportional to the temperature difference <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   The growth rate of invested money, proportional to the current amount <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

In all such cases, the function describing the variable over time will be an exponential, and expressing it as `e^(kt)` clearly shows the proportionality constant 'k' that governs its growth or decay <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.