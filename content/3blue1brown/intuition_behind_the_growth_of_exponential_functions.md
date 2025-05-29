---
title: Intuition behind the growth of exponential functions
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

This article explores the [[derivatives of exponential functions|derivatives of exponential functions]], specifically focusing on functions like 2^x, 7^x, and explaining why *e*^x is considered the most significant among exponentials <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Understanding Growth: The Pie Creature Analogy

To build intuition, consider the function 2^t, where 't' represents time in days <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Imagine 2^t as the total mass of a population of "pie creatures" that doubles every day <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Thinking of mass, rather than discrete population size, helps reflect the continuity of the function <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

*   At t=0, the mass is 2^0 = 1 (one creature mass) <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   At t=1 day, the mass grows to 2^1 = 2 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   At t=2 days, it's 2^2 = 4, continuing to double daily <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Rate of Change Over a Full Day

The derivative (dm/dt) represents the rate at which this population mass grows <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
Observing changes over a full day:
*   Between day 3 and day 4, the mass grows from 8 to 16, adding 8 creature masses <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This rate (8 per day) equals the population size at the start of day 3 <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   Between day 4 and day 5, it grows from 16 to 32, a rate of 16 new creature masses per day, which again equals the population size at the start of day 4 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

This pattern suggests that the rate of growth over a full day is equal to the population size at the start of that day <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. It might be tempting to conclude that the derivative of 2^t is simply 2^t <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## From Full Days to Tiny Changes

However, this conclusion is based on comparing changes over a full day (2^(t+1) vs. 2^t) <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. For the true derivative, we must consider smaller and smaller changes in time (dt) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This is why thinking of population mass is useful, as it allows for tiny changes in mass over tiny fractions of a day <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

The derivative requires understanding the limit of `(2^(t + dt) - 2^t) / dt` as dt approaches zero <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### The Algebraic Key

A crucial [[properties_of_the_exponential_function|property of exponential functions]] is that `a^(x+y)` can be broken down into `a^x * a^y` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Applying this to 2^t:
1.  `2^(t + dt)` can be rewritten as `2^t * 2^dt` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
2.  The expression for the derivative becomes `(2^t * 2^dt - 2^t) / dt` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
3.  Factoring out 2^t, we get `2^t * ((2^dt - 1) / dt)` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

The remarkable insight here is that the term `((2^dt - 1) / dt)` is entirely separate from 't' <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. As dt approaches 0, this term approaches a specific constant value, approximately 0.6931 <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

This means the derivative of 2^t is `2^t` multiplied by some constant <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. It's proportional to itself, with a unique [[proportionality_constants_in_exponential_functions|proportionality constant]] of 0.6931 <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Other Exponential Bases

This pattern holds for other bases as well <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>:
*   For 3^t, the proportionality constant is approximately 1.0986 <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   For 8^t, the constant is around 2.079 <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Notably, 2.079 is approximately 3 times the constant for base 2 <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## The Significance of 'e'

This leads to a crucial question: Is there a base for which the [[proportionality_constants_in_exponential_functions|proportionality constant]] is exactly 1, meaning the derivative of a^t is precisely equal to a^t? <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>

### The Number 'e'

Yes, that special constant is 'e', approximately 2.71828 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This property, where e^t is its own derivative, is a defining characteristic of 'e' <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Visually, the graph of e^t has the unique characteristic that the slope of a tangent line at any point equals the height of that point above the horizontal axis <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Connecting to Natural Logarithms

The existence of 'e' helps explain the "mystery constants" for other bases <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Using the chain rule from [[calculus_and_exponential_functions|calculus]], the derivative of e^(kt) is `k * e^(kt)` <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

Crucially, any number (like 2) can be written as `e^(natural log of 2)` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This is the definition of the [[natural_logarithms_and_exponential_growth|natural logarithm]]: `ln(x)` answers "e to what power equals x" <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

Therefore, the function 2^t can be expressed as `e^(ln(2) * t)` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
Applying the chain rule, the derivative of `e^(ln(2) * t)` is `ln(2) * e^(ln(2) * t)`, which simplifies to `ln(2) * 2^t` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
If you calculate `ln(2)`, you get approximately 0.6931, the original mystery constant <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

In general, the [[proportionality_constants_in_exponential_functions|proportionality constant]] that appears when taking derivatives of `a^t` is simply the [[natural_logarithms_and_exponential_growth|natural logarithm]] of the base 'a' <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Why 'e' is Preferred in Calculus

While any [[exponential_growth|exponential growth]] function can be written using different bases (e.g., 2^t or 3^t), in [[calculus_and_exponential_functions|calculus]] applications, exponentials are almost always expressed in the form `e^(constant * t)` <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

This choice is made because when an exponential function is written as `e^(kt)`, the constant 'k' in the exponent has a clear, readable meaning <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

### Exponential Functions in Natural Phenomena

Many [[natural_phenomena_and_their_relationship_with_exponentials|natural phenomena]] involve a rate of change that is proportional to the quantity itself <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. Examples include:
*   Population growth (assuming no limited resources) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   The cooling rate of hot water, proportional to the temperature difference <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   The growth of invested money, proportional to the current amount <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

In all these cases, where a variable's rate of change is proportional to itself, the function describing that variable over time will be an [[exponential_growth|exponential function]] <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. By expressing these functions as `e^(kt)`, the constant 'k' directly represents the [[proportionality_constants_in_exponential_functions|proportionality constant]] between the changing variable's size and its rate of change <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.