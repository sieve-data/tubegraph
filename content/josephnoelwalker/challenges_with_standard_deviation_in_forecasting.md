---
title: Challenges with standard deviation in forecasting
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

A core intellectual disagreement with the "super forecasting" project centers on the distinction between [[binary_versus_continuous_payoffs_in_forecasting | binary versus continuous payoffs]] and the applicability of concepts like standard deviation in predicting real-world events <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Binary vs. Continuous Payoffs

A fundamental issue arises when forecasting with binary options, which only provide a "yes" or "no" outcome, rather than considering continuous payoffs where the magnitude of an event matters <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

*   **Counter-intuitive behavior with fat tails**: A naive person might assume that an out-of-the-money binary option would increase in value if the tail of the distribution fattens. However, these options actually go down in value when the tail fattens <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Impact of fat tails on probability**: If you "fatten the tail" of a distribution, the probabilities of being above or below a certain threshold actually *drop*. This is because the variance becomes more explained by rare, extreme events, causing the body of the distribution to go up and the "shoulders" to narrow <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Misleading bets**: Using binary options or any mechanism that "clips your upside" is considered a "wrong bet" by experienced option traders <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Rookies or those from economics backgrounds often express their bets using these methods, which experienced traders exploit <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Example from *Fooled by Randomness***: It's possible to be bullish on a market (higher probability of going up) in frequency space, yet simultaneously "short" (bearish) in payoff space, meaning the expected gain is bigger from being short <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## The Inadequacy of Standard Deviation in Extremistan

The concept of a "standard deviation" or a "typical event" becomes problematic when dealing with phenomena governed by "fat-tailed" distributions, often referred to as "Extremistan" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

*   **Sub-selection of inconsequential events**: Forecasters often select events that are easy to forecast but are "inconsequential," "small," or "restricted" in scope <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **The random nature of "events"**: There is no such thing as a "standard event" because the size or severity of an event is itself a random variable. For instance, a "war" could kill two people or 600,000 <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Similarly, a "pandemic" is not just "yes or no"; its scale is a random variable <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Mandelbrot's insight**: Benoît Mandelbrot famously stated, "there is no such thing as a standard deviation in Extremistan" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This implies there's "no typical event" when dealing with scale-free distributions, unlike Gaussian distributions <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Behavior of large deviations**:
    *   **Gaussian (Thin-tailed)**: For a Gaussian distribution, the expected deviation above, say, three sigma, is only slightly more than three sigma. As you go higher (e.g., five sigma), the expected additional deviation shrinks proportionally <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This is analogous to human life expectancy: expectancy at birth might be 80 years, but at 100 years old, it's only a few more years <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   **Extremistan (Fat-tailed)**: In Extremistan, or for scale-free distributions, this shrinking doesn't occur. The scale stays the same proportionally. For example, if company sizes were fat-tailed, the expected size of a company larger than 10 million in sales might be 15 million, and for a company larger than 100 million, it might be 150 million <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This "explosion" in absolute terms means there's no "standard large deviation" <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Consequences for Forecasting

This fundamental difference has significant implications for forecasting, particularly for [[statistical_consequences_of_fat_tails | fat-tailed variables]].

*   **"No characteristic scale"**: This framework, developed from working with Mandelbrot, posits that there is no characteristic scale for certain phenomena, which makes standard forecasting problematic <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Inadequacy of point forecasts**: For fat-tailed variables, single "point forecasts" are inadequate because the higher an outcome is, the more meaningful it becomes (e.g., "higher than 10 million" versus "higher than 100 million") <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Pandemic example**: Forecasting the rate of growth of COVID-19 cannot be directly translated into the number of people killed. An exponential transformation from growth rate to number of people killed can result in a Pareto (fat-tailed) distribution, leading to potentially infinite expectation even from a finite explanation in the rate <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Foolishness of criticizing forecasts**: If 95% of observations for a fat-tailed variable fall below the mean, it is meaningless to criticize someone's forecast for "missing" the outcome <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Just as a trader who loses money 98% of the time can't be judged as "losing money this year" without considering the large payoff from the rare 2% <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Churchill vs. Napoleon**: Winston Churchill, despite being "wrong on all these calls" (e.g., gold standard, India), was "right on the big question of Hitler's intentions." He was right "in payoff space" when it mattered, winning the war despite losing many battles <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Conversely, Napoleon, who won many battles, ultimately lost the crucial war, demonstrating that frequency of success doesn't always align with payoff <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## Operational and Philosophical Differences

The operational differences in how these concepts are applied highlight a deep philosophical divide.

*   **Forecast payoff mismatch**: While binary forecasts have some limited value (e.g., elections are binary), there's a poor understanding of how to translate binaries into real-world payoffs <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Value at Risk (VaR) vs. Tail Risk**: The "Value at Risk (VaR)" metric, which defines a loss threshold within a certain confidence level (e.g., "95% confidence you won't lose more than a million"), is considered flawed. The critical action lies in the remaining 5%, where losses could be orders of magnitude larger (e.g., 200 million), known as tail risk <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Forecasters vs. Traders**: People "good at forecasting" in banks are rarely wealthy because they are not paid based on the real-world financial consequences of their forecasts <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The profit or loss generated depends on the payoff function, which is often non-linear and explosive in the real world <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. One cannot isolate forecasting from the payoff function <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>.
*   **Probability as a Kernel**: True understanding of probability involves recognizing it as a "kernel" that adds up to one, rather than an isolated product <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Probability density functions (P(x)) themselves have no meaning in isolation; they must be integrated with a function (G(x)) that describes the payoff <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. This is why option traders focus on the value of the option, which provides a continuous payoff, rather than just probabilities <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.