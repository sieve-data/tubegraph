---
title: Limitations of super forecasting
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

The intellectual project of "super forecasting" faces substantive disagreements, primarily concerning its reliance on binary outcomes and its inability to properly account for "fat tails" and non-standard events <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Binary vs. Continuous Payoffs
A core disagreement stems from the use of [[binary_versus_continuous_payoffs_in_forecasting | binary versus continuous payoffs]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. A naive person might assume that an out-of-the-money binary option would increase in value when the "tail" of a distribution fattens, but in reality, it decreases <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. When tails fatten, the probabilities of being above or below certain thresholds (like plus or minus one standard deviation from a Gaussian curve) actually drop <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This occurs because the variance is more explained by rare events, causing the body of the distribution to go up while the shoulders narrow <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

> "You're making the wrong bet using binary options or using anything that clips your upside" <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

Option traders understand this, but others, including some economists, often express their bets using binary methods, which are then sold to them <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The distinction between a bet that pays a fixed $1 and one that pays a lot (continuous payoff) is crucial <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For example, one can be "bullish" on the market (expecting a higher probability of going up) yet simultaneously "short" it if the expected payoff from rare, large downward movements is greater <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. These concepts do not translate well outside option trading <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

Binary forecasts have limited value because they assume a lump sum payoff, unlike real-world continuous payoffs <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. There's also a challenge in translating binaries into real-world outcomes <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. For instance, accurately forecasting the growth rate of a disease (like COVID) does not directly translate to forecasting the number of people killed if the growth is exponential, as a small error in the rate can lead to a Pareto distribution for the outcome, potentially with an infinite expectation <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

## Sub-selection of Events and Inconsequential Forecasts
Super forecasting projects often "sub-select events" that are forecastable but ultimately inconsequential, dealing with very small, restricted questions <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Real-world events, like a war, are not binary (yes/no) because their consequences can range from killing two people to 600,000 <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## The Problem of Standard Deviation in Extremistan
A significant critique is that there is no such thing as a [[challenges_with_standard_deviation_in_forecasting | standard deviation]] in "Extremistan" (domains characterized by fat tails) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This means you cannot judge an event (e.g., a pandemic) by simply saying "yes" or "no" because its size is a random variable <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

In scale-free distributions, there is no "standard event" or "typical event" <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Unlike Gaussian distributions where the expected deviation above a certain sigma shrinks as the sigma increases, in Extremistan, the scale stays the same, and deviations can explode <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This "explosion" indicates the absence of a standard large deviation and a characteristic scale <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This framework, which helped explain events like the 1987 market crash, implies a fundamental problem with forecasting <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

## Inadequacy of Point Forecasts
It is inappropriate to use point forecasts for fat-tailed variables <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
A paper co-authored, "On the Inadequacy of Point Forecasts for Fat-Tailed Variables," argues against this <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. For example, the distribution of people killed in pandemics has a tail exponent less than one (like a Levy infinite mean distribution), making it foolish to forecast specific numbers or critique a forecast for missing the mark, especially since 95% of observations might fall below the mean <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Payoff Space vs. Frequency Space
Forecasting accuracy (frequency space) does not equate to success in "payoff space" (real-world outcomes in dollars and cents) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. Winston Churchill, for instance, was often wrong on many small forecasts (gold standard, India) but was decisively right on the major question of Hitler's intentions, winning in payoff space where it mattered <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Conversely, Napoleon won many battles (frequency) but ultimately lost the war (payoff) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

The ability to consistently generate wealth through forecasting is rare. People good at forecasting in banks are typically not wealthy <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. If one is predicting volatility, and the volatility occurs steadily, they might break even. However, if volatility comes in "lumps" (unsteadily), one can lose significantly, even if they are overestimating volatility <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. The function for expressing a bet against volatility is nonlinear, leading to "explosive" outcomes <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

> "I've never seen a rich forecaster" <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

The core problem is that forecasting cannot be isolated from the payoff function <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

## Misunderstanding Probability
A deeper issue lies in the understanding of probability itself. True understanding of probability implies knowing it is not a standalone product but a "kernel"—something that adds up to one and cannot be isolated <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Probability density functions, for example, are not probabilities by themselves; they work within a continuum <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.

> "P of X by itself has no meaning" <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.

When multiplying P(x) with a function G(x) (e.g., an indicator function for binary outcomes or a continuous/convex/concave function), G(x) has meaning, but P(x) alone does not <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. Option traders, for instance, focus on the value of the option rather than isolated probabilities <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.