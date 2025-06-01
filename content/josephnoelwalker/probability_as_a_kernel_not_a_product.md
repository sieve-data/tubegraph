---
title: Probability as a kernel not a product
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

A fundamental disagreement exists with the intellectual project of "Superforecasting" regarding the nature of probability itself, particularly its application in forecasting outcomes. The core assertion is that probability should be understood as a "kernel" that integrates with a payoff function, rather than a standalone product or frequency <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>.

## Distinction from Superforecasting

The primary disagreement with superforecasting lies in its focus on [[binary_versus_continuous_payoffs_in_forecasting | binary versus continuous payoffs]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. A naive person might assume that an out-of-the-money binary option would increase in value if the tail of the distribution becomes fatter; however, they actually decrease because a binary option represents a probability <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>. When tails are fattened, the probabilities of being above or below a certain threshold actually drop, as the variance is more explained by [[the_role_of_rare_events_in_probability | rare events]] <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

Furthermore, superforecasting often sub-selects events that are forecastable but ultimately inconsequential <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. These are typically "small, restricted questions" <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

## Implications of Fat Tails

For phenomena described by [[statistical_consequences_of_fat_tails | fat-tailed distributions]], such as pandemics or wars, there is [[challenges_with_standard_deviation_in_forecasting | no such thing as a standard deviation in Extremistan]] <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.

> "You can't judge the event...by saying oh there's a pandemic or no pandemic because the the size is a random variable" <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

In fat-tailed distributions, there is no "typical event" or "standard large deviation" <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. This means a point forecast for a fat-tailed variable is inherently problematic <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. The ratio of outcomes remains constant across scales, meaning the relative impact of events does not shrink as they become larger, unlike in thin-tailed (e.g., Gaussian) distributions <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>. This concept of a "characteristic scale" was a central idea to Benoit Mandelbrot, to whom *The Black Swan* was dedicated, and explains why forecasting becomes challenging <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>.

For instance, forecasting the growth rate of a phenomenon like COVID cannot be directly translated into the number of people killed if the payoff function is exponential <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>. An exponential growth will lead to a [[statistical_consequences_of_fat_tails | Pareto distribution]] for the total number of people killed, potentially having an infinite expectation, even if the growth rate itself has a finite expectation <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>. This illustrates why simply forecasting a binary outcome or a rate of growth is insufficient. This also relates to the Value at Risk (VaR) dilemma, where knowing the 95% confidence interval doesn't account for the conditional expectation beyond that threshold, which is where "the action" lies <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>.

## The Payoff Function: Frequency vs. Payoff Space

A crucial distinction lies between frequency space (how often something occurs) and payoff space (what the outcome is worth) <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.

*   A trader can be bullish on the market (higher probability of going up in frequency space) but simultaneously short in payoff space, meaning the expected value of being short is greater <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. This means they expect to lose often but gain significantly when right.
*   Winston Churchill, for example, was often wrong on smaller matters (low [[evaluating_success_and_failure_rates | success rate]] in frequency space) but was right on the critical big question (high payoff in payoff space), like Hitler's intentions <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>. Conversely, Napoleon won many battles (high frequency) but lost the war (low payoff) <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

This leads to the observation that financially successful forecasters are rare:

> "I've never seen a rich forecaster" <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>.
> "People good at forecasting like in banks they're never rich" <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.

The ability to forecast does not automatically translate to financial success because the payoff function (how one gets paid) is not linear or simple <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>. For instance, if predicting volatility, even overestimating it by 30% can lead to profit if the actual volatility arrives in "lumps" rather than steadily, due to the non-linear nature of the bet <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.

## The Kernel Concept of Probability

Understanding probability as a kernel means recognizing that it is not a standalone product but "something that adds up to one" <a class="yt-timestamp" data-t="19:44:00">[19:44:00]</a>.

> "Whatever is inside, okay, cannot be isolated. It's a kernel" <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>.

Therefore, the probability density function P(x) has no meaning by itself <a class="yt-timestamp" data-t="20:45:00">[20:45:00]</a>. It must be multiplied within an integral by some function G(x), which represents the payoff <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>.

*   In [[binary_versus_continuous_payoffs_in_forecasting | binary forecasting]], G(x) is an indicator function (0 or 1) <a class="yt-timestamp" data-t="20:51:00">[20:51:00]</a>.
*   In real-world applications, G(x) can be continuous, convex, or concave, and these different shapes drastically alter the implications <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>.

Option traders, for example, do not talk about probabilities in isolation but rather the value of an option, which inherently incorporates a continuous payoff <a class="yt-timestamp" data-t="21:51:00">[21:51:00]</a>.