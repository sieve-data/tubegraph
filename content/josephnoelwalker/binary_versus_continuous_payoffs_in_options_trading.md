---
title: Binary versus continuous payoffs in options trading
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

A core disagreement in forecasting, particularly when dealing with [[understanding_fat_tails_in_probability_distributions | fat-tailed]] distributions, lies in the distinction between binary and continuous payoffs <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This distinction is crucial for understanding how financial bets, especially in options trading, generate value <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Binary Payoffs and Their Limitations

Binary options, or "yes/no" bets, pay out a fixed amount (e.g., $1) if a specific event occurs and nothing otherwise <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### The Problem with Fat Tails
*   **Counter-intuitive behavior**: A common misconception among those not familiar with options trading is that an out-of-the-money binary option will *increase* in value when the [[understanding_fat_tails_in_probability_distributions | tail fattens]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. In reality, they *decrease* in value <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Reason**: When tails are fatter, the variance of the distribution is more explained by rare events <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This causes the main body of the distribution to go up and the shoulders to narrow, meaning there are more ordinary events, but deviations that occur are much more pronounced <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Risk**: Engaging with binary options or any financial instrument that "clips your upside" can lead to making the "wrong bet" <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Seasoned option traders are aware of this, but rookies or those in economics sometimes express their bets this way <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Inadequacy in Forecasting
*   **Sub-selection of events**: Forecasters often sub-select events that are inconsequential and restricted in scope, making them easier to forecast but irrelevant to real-world outcomes <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Undefined event size**: There's no such thing as a "standard event" in [[understanding_fat_tails_in_probability_distributions | extremist]] statistics <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. For example, forecasting a war as "yes" or "no" ignores whether it kills two people or 600,000 <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Similarly, a pandemic's size is a random variable, making a simple "yes/no" forecast of a pandemic meaningless <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **No typical event**: In [[understanding_fat_tails_on_prediction_and_option_value | scale-free distributions]], there is no "typical event" or standard large deviation <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The expected deviation above 3 Sigma in a Gaussian distribution is slightly more than 3 Sigma, but for [[understanding_fat_tails_in_probability_distributions | extremist]] distributions (like [[understanding_fat_tails_in_probability_distributions | Pareto]]), the scale of deviations remains proportionally the same, yet explodes in absolute terms <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **[[probability_and_prediction_in_finance_and_economics | Point forecasts]] for [[understanding_fat_tails_in_probability_distributions | fat-tailed variables]]**: Such forecasts are inherently inadequate <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. If 95% of observations fall below the mean in a [[understanding_fat_tails_in_probability_distributions | fat-tailed]] distribution, critiquing a forecast for missing the mean is foolish and meaningless <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Transformation issue**: Forecasting a growth rate (R) for COVID-19 cannot be directly translated into the number of people killed (W), because if W = W0 * e^(Rt), W can follow a [[understanding_fat_tails_in_probability_distributions | Pareto]] distribution. This can lead to an infinite expectation for W even if R has a finite expectation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **VaR vs. CVaR**: The concept of Value-at-Risk (VaR), which gives a loss threshold within a certain confidence interval (e.g., 95%), is flawed because the conditional loss beyond that threshold (Conditional VaR or CVaR) can be dramatically higher, especially with [[understanding_fat_tails_in_probability_distributions | fat tails]] <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. The "action" lies in the extreme 5% <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

> "Probability is not a product; it's a kernel... P of X by itself has no meaning." <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a> <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>
>
> --- *From the transcript*

## Continuous Payoffs and Real-World Value

Unlike binary outcomes, continuous payoffs reflect the actual magnitude of gains or losses.

*   **Payoff space vs. frequency space**: One can be "bullish" in the sense of having a higher probability of the market going up (frequency space), yet be "short" overall because the expected payoff (payoff space) is negative due to potential large losses <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a> <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Churchill vs. Napoleon**: Winston Churchill, despite being "wrong on all these [small] questions" (frequency space), was "right on the big question of Hitler's intentions" (payoff space) <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. Conversely, Napoleon won many battles (frequency space) but lost the war (payoff space) <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This highlights that success in the real world is measured by payoff, not mere frequency of correct predictions <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Option traders' perspective**: Option traders focus on the *value* of an option and its continuous payoff, not just probabilities <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. The [[understanding_fat_tails_in_probability_distributions | Pareto distribution]] is valuable in this context because it allows for a continuous payoff <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>.

## Implications for Forecasting

*   **Sterile forecasting**: Relying solely on binary forecasts leads to "sterile" predictions because the magnitude of the outcome (e.g., higher than 10 million vs. 100 million) carries significant meaning that binary forecasts ignore <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Forecasters' wealth**: People who are good at forecasting in traditional roles, such as in banks, are rarely wealthy themselves <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. This suggests that the ability to forecast does not directly translate to generating real-world financial gain, unless it's applied through a beneficial payoff function <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Non-linear payoffs**: When betting against a convex function, for example, predicting volatility steadily when it arrives in lumps, one can lose significantly, even if their overall prediction of volatility is an overestimate <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This is because the payoff function is non-linear <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

> "You cannot isolate the forecasting from the payoff function." <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>
>
> --- *From the transcript*

The fundamental distinction lies in how the outcome is measured and compensated. In finance, where payoffs are typically continuous and potentially unbounded, understanding the nature of these payoffs in relation to the underlying distribution, especially those with [[understanding_fat_tails_in_probability_distributions | fat tails]], is paramount.