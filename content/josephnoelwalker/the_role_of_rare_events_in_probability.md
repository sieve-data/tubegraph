---
title: The role of rare events in probability
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

A substantive disagreement in intellectual projects like "super forecasting" centers on the distinction between [[binary_versus_continuous_payoffs_in_forecasting | binary versus continuous payoffs]] and the treatment of rare events, particularly in the context of [[statistical_consequences_of_fat_tails | fat-tailed distributions]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Naive individuals might assume an out-of-the-money binary option increases in value when the tail of a distribution is fattened, but in reality, they decrease in value because the binary option is a probability <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Impact of [[Statistical consequences of fat tails | Fat Tails]] on Probabilities

When a distribution's tail is "fattened," the probabilities of being above or below a certain standard deviation (e.g., plus or minus one Sigma in a Gaussian curve) actually drop <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This occurs because rare events explain more of the variance, causing the body of the distribution to go up and the shoulders to narrow <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Consequently, there are more ordinary events, but deviations that do occur are far more pronounced <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This means that using binary options or anything that clips upside can lead to wrong bets, a concept well-understood by option traders but often missed by others, including some academics <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Frequency Space vs. Payoff Space
There is a critical difference between making a bet with a fixed payout (e.g., $1) and one with a potentially large payout <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This distinction is exemplified by being "bullish" in terms of market probability (frequency space) but "short" in terms of expected payoff (payoff space) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. These concepts do not easily translate outside of option trading <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## The Problem with Sub-selecting Events

Forecasting projects often sub-select events that are consequential, but these tend to be small, restricted questions <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Moreover, there is no such thing as a "standard event" <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. For instance, a war can kill two people or 600,000 <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### "No Standard Deviation in Extremistan"
Benoît Mandelbrot frequently emphasized that "there is no such thing as a standard deviation in Extremistan" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This means one cannot judge an event (e.g., a pandemic) by merely its occurrence because its size is a random variable <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

[!NOTE]
In distributions with [[statistical_consequences_of_fat_tails | fat tails]] (like scale-free or Pareto distributions), the ratio of magnitudes remains constant across scales (e.g., 10 million over 5 million is similar to 20 million over 10 million) <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This implies there is "no typical event" and "no standard large deviation" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Unlike a Gaussian distribution where expected deviations above a certain sigma shrink as the sigma increases, in Extremistan, the scale stays the same proportionally, leading to an explosion in absolute terms for large values <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This concept of "no characteristic scale" makes forecasting problematic <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Implications for Forecasting

The insights from Mandelbrot's characteristic scale idea, which formed the basis for *The Black Swan*, highlight a fundamental problem with forecasting <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
A paper was written on "the inadequacy" of "point forecasts for a [[statistical_consequences_of_fat_tails | fat-tailed]] variable" <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This paper, co-authored by Taleb, Cherou, and Bar-Yam, used data on people killed in pandemics, showing a tail exponent of less than one (like a Levy infinite mean distribution) <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This applies to wars as well, where the number of fatalities is a [[statistical_consequences_of_fat_tails | fat-tailed]] variable <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

[!WARNING]
It is "foolish to forecast" and even "more foolish to critique someone's forecast" if they miss a forecast because 95% of observations in a [[statistical_consequences_of_fat_tails | fat-tailed]] distribution will be below the mean <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Similarly, in a trading strategy where 98% of the time losses occur, stating that forecasting will lose money is meaningless <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

Winston Churchill, despite being wrong on many smaller issues (e.g., gold standard, India), was famously right on the "big question of Hitler's intentions" <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. This demonstrates that success is measured in "payoff space" where the consequences of being right on a rare, high-impact event outweigh many small errors <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This contrasts with Napoleon, who was good at winning numerous battles but lost the war <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## The Var-Sear Dilemma

The "Var-Sear dilemma" illustrates another aspect of misinterpreting rare events <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. Value at Risk (VaR) typically states, for example, that there's a 95% confidence that losses won't exceed a million <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. However, the flaw lies in neglecting the remaining 5%—the tail where "the action was" <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. Conditional on losing more than a million, the actual loss could be 200 million <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

Even though probabilities are bounded between zero and one and can be [[statistical_consequences_of_fat_tails | fat-tailed]], the transformation from probability to actual outcome (e.g., number of people killed) can be explosive, especially with exponential growth <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. A small error in a growth rate can lead to a Pareto distribution for the outcome, potentially an infinite expectation for the outcome from a finite expectation in the rate <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

## [[Probability as a kernel not a product | Probability as a Kernel]]

A key insight into understanding probability, particularly in the context of rare events, is recognizing that [[probability_as_a_kernel_not_a_product | probability is not a product; it's a kernel]] <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. It is something that adds up to one <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

[!NOTE]
This means what is "inside" a probability distribution cannot be isolated <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Probability densities are not probabilities themselves, but they function within a continuum <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. Smart people understand that negative probabilities, as used in quantum mechanics, are possible because probability is a kernel, and constraints apply to the summation, not necessarily to individual elements <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

When performing an integral with a probability distribution `P(X)` multiplied by a function `G(X)`, `P(X)` by itself has no meaning <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>. `G(X)`, however, has meaning <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. If `G(X)` is an indicator function (binary outcome), it's one thing; if it's continuous, convex, or concave, it's another <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. One cannot separate `P(X)` and discuss it in isolation <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. This is why option traders focus on the value of the option (continuous payoff) rather than just isolated probabilities <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.