---
title: Probability distribution functions
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

[[Random Variables in Probability | Random variables]] can be categorized into two main types: discrete and continuous <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Their associated probability distribution functions differ in how they represent and calculate probabilities.

## Discrete Probability Distributions

[[Discrete Random Variables | Discrete random variables]] take on a finite number of values <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These values don't always have to be integers <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. For a discrete random variable, the sum of all possible probabilities must equal 1 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Example: Coin Toss
Consider a coin toss where the [[Random Variables in Probability | random variable]] `x` is 1 for heads and 0 for tails <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. If the probability of heads is 0.5, then the probability of tails must also be 0.5, adding up to 1 <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. If one probability was 0.6, the other would necessarily be 0.4, ensuring their sum is 1 <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. Having 60% chance for heads and 60% chance for tails would make no sense, as it sums to 120% <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## Continuous Probability Density Functions

Continuous [[Random Variables in Probability | random variables]] can take on an infinite number of values within an interval <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. For these, we use a [[Probability density functions and calculus integration | probability density function]] (PDF) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Probability of an Exact Value
For a continuous [[Random Variables in Probability | random variable]], the [[Calculating probability of an event | probability of an event]] occurring at an *exact* value is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
For example, the [[Calculating probability of an event | probability]] of exactly 2 inches of rain tomorrow is virtually zero <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This is because there are infinite possibilities between any two points (e.g., 2.000001 inches vs. 2 inches) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Our measurement tools cannot even confirm exactness down to an infinite decimal point <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
Conceptually, this is similar to asking for the [[Area under probability curves | area of a line]], which has no width and thus no area <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Calculating Probability Over an Interval
Instead, for continuous [[Random Variables in Probability | random variables]], we [[Calculating probability of an event | calculate probability]] over an *interval* <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The [[Area under probability curves | area]] under the [[Probability density functions and calculus integration | probability density function]] curve within a specified range represents the [[Calculating probability of an event | probability]] of the [[Random Variables in Probability | random variable]] falling within that range <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

#### Example: Rain Amount
Let Y be the exact amount of rain tomorrow, represented by a [[Probability density functions and calculus integration | probability density function]] `f(x)` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
If we want the [[Calculating probability of an event | probability]] that Y is between 1.9 and 2.1 inches of rain, this corresponds to the [[Area under probability curves | area]] under the curve between `x = 1.9` and `x = 2.1` <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Using [[Probability density functions and calculus integration | calculus integration]], this [[Calculating probability of an event | probability]] is given by the definite integral of the PDF `f(x)` from 1.9 to 2.1:
`P(1.9 < Y < 2.1) = ∫₁․₉²․¹ f(x) dx` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>, <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

Similarly, to find the [[Calculating probability of an event | probability]] of less than 0.1 inches of rain, you would calculate the [[Area under probability curves | area]] from 0 to 0.1 <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. For more than 4 inches of rain, you would calculate the [[Area under probability curves | area]] from 4 to infinity <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### Total Probability Rule for Continuous Variables
For a continuous [[Random Variables in Probability | random variable]], the total [[Area under probability curves | area]] under its [[Probability density functions and calculus integration | probability density function]] curve must be equal to 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This is because the sum of all possible [[Calculating probability of an event | probabilities]] of all events that might occur cannot exceed 100% or 1 <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

In calculus terms, the integral of `f(x)` from negative infinity (or 0, if the variable cannot be negative) to positive infinity must equal 1:
`∫₀^∞ f(x) dx = 1` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.