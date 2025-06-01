---
title: Limitations of traditional forecasting methods
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

Traditional forecasting methods, particularly those focusing on "super forecasting" and binary outcomes, face significant limitations when applied to complex, real-world phenomena characterized by [[the_impact_of_fat_tails_on_prediction_and_option_value | fat tails]] and non-standard distributions <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The core disagreement often revolves around binary versus continuous payoffs in prediction <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Binary vs. Continuous Payoffs

A fundamental flaw in traditional forecasting is the reliance on binary outcomes (e.g., yes/no questions) rather than considering continuous payoffs <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### The Impact of Fat Tails

In financial contexts, an out-of-the-money binary option paradoxically decreases in value when [[the_impact_of_fat_tails_on_prediction_and_option_value | fat tails]] are present <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This is because the binary outcome represents a probability <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. When tails are fattened, the probability of falling within a standard deviation (e.g., +/- one Sigma in a Gaussian curve) actually drops, as variance is more explained by rare events <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

This implies that traditional forecasters, including those in economics, who express their bets using binary methods are making the wrong bet, particularly when the payoff structure clips upside <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Seasoned option traders understand this dynamic, often selling such options to less experienced individuals <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

> "There's a difference between making a bet where you get paid $1 and making a bet where you get paid a lot" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## The Problem of Sub-Selected Events and "Typical Events"

Traditional forecasting often relies on sub-selecting events that are predictable but ultimately inconsequential <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. They tend to focus on "small, restricted questions" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### No Standard Deviation in Extremistan

A key insight from [[mandelbrots_influence_on_understanding_extreme_events | Mandelbrot's influence on understanding extreme events]] is that there is "no such thing as a standard deviation in Extremistan" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This means one cannot judge an event by its occurrence alone without considering its magnitude <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. For example, a "war" could kill two people or 600,000 people <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Similarly, a pandemic's impact isn't just "yes/no," but depends on its scale <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

In scale-free distributions, there is no "typical event" <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The expected deviation above a certain point does not shrink as it does in a Gaussian distribution <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This implies that the scale of events, such as company size or the number of people killed in a pandemic, does not "shrink" proportionally as values increase; in absolute terms, they can explode <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This "explosion" indicates the absence of a standard large deviation <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

This concept of "no characteristic scale" is central to understanding [[the_impact_of_fat_tails_on_prediction_and_option_value | fat tails]] and the limitations of forecasting <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This framework, developed with [[mandelbrots_influence_on_understanding_extreme_events | Mandelbrot's influence on understanding extreme events]], highlights the sterility of forecasting when characteristic scales are assumed <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### The Folly of Point Forecasts

For fat-tailed variables, making a "point forecast" is considered foolish <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. It is equally foolish to critique someone's forecast as "missed" when 95% of observations might fall below the mean, as is common in distributions with [[the_impact_of_fat_tails_on_prediction_and_option_value | fat tails]] <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This is analogous to a trader who loses money 98% of the time but makes significant profits from rare, large events <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

## Frequency Space vs. Payoff Space

A critical distinction is between forecasting in "frequency space" (how often something happens) and "payoff space" (the actual monetary or consequential outcome) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

> "You're paid in dollars and cents" <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

A good forecaster might be right frequently on small, inconsequential matters, but wrong on the critical, high-payoff events. For example, Winston Churchill was often wrong on minor policy calls but correct on the major, high-consequence question of Hitler's intentions <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. Conversely, Napoleon was excellent at winning battles but ultimately lost the war, highlighting a mismatch between frequent small wins and large overall losses <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

This explains the phenomenon of being "bullish" in terms of [[probability_and_prediction_in_finance_and_economics | probability]] of going up, but "short" in terms of expected payoff <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. There is a disconnect between accurate predictions of rates of growth (e.g., COVID-19) and translating that into the actual number of people killed, because the latter involves an exponential transformation that can lead to a [[the_impact_of_fat_tails_on_prediction_and_option_value | fat-tailed]] outcome <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

## The Inadequacy of Value-at-Risk (VaR)

The problem extends to financial risk measures like Value-at-Risk (VaR), which aims to predict the maximum loss within a certain confidence interval (e.g., 95% confidence that losses won't exceed a million) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This approach is flawed because the "remaining 5% is where the action was" <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. Conditional on losing more than the VaR, the actual loss can be significantly higher, demonstrating the importance of extreme events. The transformation from bounded probabilities to unbounded real-world outcomes is explosive, particularly for non-Gaussian distributions <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

## Probability as a Kernel, Not a Standalone Product

A true understanding of [[probability_and_prediction_in_finance_and_economics | probability]] recognizes that it is not a standalone "product" but a "kernel" that adds up to one <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. This means a [[probability_and_prediction_in_finance_and_economics | probability]] `P(X)` by itself has no inherent meaning; it must be considered within an integral with some function `G(X)` (the payoff function) <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

For binary outcomes, `G(X)` is an indicator function (0 or 1), while for continuous outcomes, it can take various convex or concave shapes <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. The inability to separate `P(X)` from `G(X)` is a critical oversight in many traditional forecasting approaches <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. Option traders, for instance, focus on the value of the option (which inherently includes the payoff function) rather than just raw probabilities <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

### Lack of Practical Application

Forecasting, particularly "super forecasting," often fails to translate into tangible financial success <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Individuals who are good at forecasting in banks are rarely rich, as their role is often to communicate forecasts to customers <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The true test of a forecasting method lies in its ability to generate wealth, which requires accounting for non-linear payoff functions <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. The effectiveness of forecasting cannot be isolated from the payoff function <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.