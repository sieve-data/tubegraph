---
title: Probability and prediction in finance and economics
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

A significant intellectual disagreement exists concerning the broad project of "super forecasting," particularly regarding the distinction between [[binary_versus_continuous_payoffs_in_options_trading | binary versus continuous payoffs]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This disagreement stems from fundamental misunderstandings of probability and the nature of events, especially in financial markets.

## The Problem with Binary Payoffs and Fat Tails

When dealing with [[understanding_fat_tails_in_probability_distributions | fat tails in probability distributions]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, a naive person might assume that an out-of-the-money binary option would increase in value <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. However, such options actually decrease in value when the tail is fattened, because a binary option represents a probability <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

The intuition behind this is observed when comparing a Gaussian curve to a fat-tailed distribution:
*   In a Gaussian curve, the probability within plus or minus one standard deviation is about 68% <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   When the tail is fattened, the probabilities of being above or below certain thresholds *drop* <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This occurs because the variance is more explained by rare events, causing the body of the distribution to go up while the "shoulders" narrow <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   This implies a higher concentration of ordinary events and more pronounced deviations from the norm <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Rookies or individuals not experienced in option trading, including some in economics, often express their bets using binary options or methods that clip their upside, which experienced option traders avoid <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This is because there's a critical difference between making a bet for a fixed payoff (e.g., $1) and one where the payoff can be substantial (e.g., a lot) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This concept was previously explained by being "bullish" on the market (higher probability of going up) while simultaneously "short" in expectation (the payoff from being short is bigger) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## The Inconsequentiality of Forecastable Events

Forecasting efforts often fall short because they tend to sub-select events that are inconsequential or very small and restricted in scope <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. There is no such thing as a "standard event" when dealing with phenomena that exhibit [[the_impact_of_fat_tails_on_prediction_and_option_value | fat tails]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

For instance:
*   A war could kill two people or 600,000 people; its "size" is a random variable <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   Similarly, a pandemic's impact is not a binary yes/no event, as its severity (size) is also a random variable <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

This concept is rooted in the idea that for fat-tailed distributions, there is no "typical event" or "standard large deviation" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. As Benoit Mandelbrot famously stated, "there is no such thing as a standard deviation in extremistan" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. While the expected deviation in a Gaussian distribution shrinks as you go higher in standard deviations (e.g., 3 Sigma vs. 5 Sigma) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, in extremistan, the scale stays the same proportionally, but explodes in absolute terms <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This characteristic scale idea was central to *The Black Swan* <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

## The Inadequacy of Point Forecasts

Given the nature of fat-tailed variables, "point forecasts" (single predictions of a future value) are inherently inadequate <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. A paper co-authored on the subject highlights this inadequacy <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

The distribution of people killed in pandemics, for example, has a tail exponent of less than one, similar to a Lévy infinite mean distribution <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This means:
*   It is foolish to forecast the number of people killed in a pandemic <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   It is even more foolish to critique someone's forecast as incorrect simply because 95% of observations might fall below the mean <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. This is akin to a trader who loses money 98% of the time, yet profits overall from rare, large gains <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

Winston Churchill serves as an anecdotal example: he was often wrong on many specific questions (e.g., gold standard, India) <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a> but was profoundly correct on the critical "big question" (Hitler's intentions) <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. He was "right in payoff space" where it mattered, illustrating that frequency of being right doesn't equate to payoff <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### The VaR-Sear Dilemma

Another illustration of this problem is the "VaR-Sear dilemma" <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. While Value at Risk (VaR) might state that within 95% confidence, one won't lose more than a million, the flaw lies in ignoring what happens in the remaining 5% <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. Conditional on losing more than a million, one might lose 200 million <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This exponential transformation (e.g., predicting the *rate of growth* of COVID vs. the *number of people killed*) shows that a small error in the input (rate) can lead to a Pareto distribution of the output (deaths) with infinite expectation <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## Forecasting Cannot Be Isolated from Payoff

The central problem with traditional forecasting, including super forecasting, is its inability to isolate forecasting from the payoff function <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

*   People good at forecasting in banks are rarely rich <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   If you're betting against a convex function, and volatility comes in lumps instead of steadily, you lose significantly <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. For example, overestimating volatility by 30% can still lead to making money if your bet is structured non-linearly <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. This highlights that forecasting accuracy (being "right" on average) doesn't necessarily translate to profit in the real world <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

The idea that "probability by itself has no meaning" <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a> is crucial. Probability is a "kernel" that adds up to one, meaning whatever is inside cannot be isolated <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. When using probability P(X), it must be multiplied by some function G(X) (the payoff function) within an integral <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>. If G(X) is an indicator function (0 or 1 for binary outcomes), or a continuous/convex/concave function, the consequences for the payoff can be dramatically different. Option traders, therefore, focus on the value of the option (continuous payoff) rather than just probabilities <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.