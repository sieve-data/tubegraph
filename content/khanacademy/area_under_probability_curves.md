---
title: Area under probability curves
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

The area under a probability curve, specifically a [[probability_density_functions_and_calculus_integration | probability density function]] (PDF), is fundamental to understanding probabilities for [[random_variables_in_probability | continuous random variables]] <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. This concept contrasts with [[basic_probability_concepts | discrete random variables]], where probabilities are assigned to distinct points <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## Continuous Random Variables

A [[random_variables_in_probability | random variable]] is considered continuous if it can take on an infinite number of values within a given range <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. An example of a continuous [[random_variables_in_probability | random variable]] is the exact amount of rain tomorrow <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Probability of an Exact Value

For a continuous [[random_variables_in_probability | random variable]], the [[calculating_probability_of_an_event | probability]] of it taking on an exact value is essentially zero <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. For instance, the [[calculating_probability_of_an_event | probability]] of having *exactly* 2 inches of rain (not 2.000001 or 1.99999 inches) is negligible <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. This is because there are infinite possible values around any given point <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.

The concept can be likened to finding the area of a single line <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>. A line, as defined, has no width, and thus no area <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>. Similarly, the [[calculating_probability_of_an_event | probability]] of an exact measurement to an infinite decimal point is zero <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

### Probability Over an Interval

Instead of exact values, [[calculating_probability_of_an_event | probability]] for [[random_variables_in_probability | continuous random variables]] is defined over an interval <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. For example, one might ask for the [[calculating_probability_of_an_event | probability]] that the amount of rain tomorrow is between 1.9 and 2.1 inches <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

To find this [[calculating_probability_of_an_event | probability]], one needs to calculate the area under the [[probability_distribution_functions | probability distribution function]] (also known as a [[probability_density_functions_and_calculus_integration | probability density function]]) within that specific interval <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.

> "If you want to know the [[calculating_probability_of_an_event | probability]] of this occurring, you actually want the area under this curve from this point to this point." <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>

For those familiar with calculus, this area is determined by the definite integral of the [[probability_density_functions_and_calculus_integration | probability density function]] (f(x)) over the given interval <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.

```
P(1.9 < Y < 2.1) = ∫[1.9 to 2.1] f(x) dx
```
<a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>

## Total Probability

A fundamental principle of [[basic_overview_of_probability | probability]] is that the total [[calculating_probability_of_an_event | probability]] of all possible events occurring must equal 1 (or 100%) <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>.

### For Continuous Variables

For a [[random_variables_in_probability | continuous random variable]], this means the entire area under its [[probability_density_functions_and_calculus_integration | probability density function]] curve, across all possible values (from 0 to infinity for non-negative values like rain), must equal 1 <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

```
∫[0 to ∞] f(x) dx = 1
```
<a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>

### For Discrete Variables

This principle also applies to [[discrete random variables]] <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>. For a [[discrete random variable]], the sum of all individual probabilities for each possible outcome must equal 1 <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. For example, in a coin toss where heads (x=1) and tails (x=0) are the only outcomes, if the [[calculating_probability_of_an_event | probability]] of heads is 0.6, the [[calculating_probability_of_an_event | probability]] of tails must be 0.4, ensuring their sum is 1 <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.