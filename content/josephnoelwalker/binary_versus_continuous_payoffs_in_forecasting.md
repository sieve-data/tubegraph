---
title: Binary versus continuous payoffs in forecasting
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

A substantive disagreement with the [[limitations_of_super_forecasting | super forecasting]] intellectual project centers on the distinction between binary and continuous payoffs <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Binary Payoffs

Binary payoffs, such as "yes or no" questions, are criticized for being inadequate for forecasting real-world phenomena with potentially extreme outcomes <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Limitations and Misconceptions
*   **Misunderstanding of Tail Risk**: A naive person might assume that fattening the tail of a distribution (i.e., increasing the probability of rare, extreme events) would increase the value of an out-of-the-money binary option. However, these options actually go down in value because the binary is a probability, and increased variance in the tails reduces the probability within a fixed range <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   For a Gaussian curve, if you fatten the tail, the probabilities of being above or below a certain standard deviation drop <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This happens because variance is more explained by rare events, and the "body" of the distribution goes up, while the "shoulders" narrow <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Inadequate for Large Deviations**: The concept of a "standard deviation" or a "typical event" is problematic in extremistan distributions, where extreme events contribute significantly to the total variance <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   For example, in scale-free distributions (like a Pareto distribution), the ratio of outcomes remains constant (e.g., 10 million over 5 million is similar to 20 million over 10 million) <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This implies there is no typical event <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   Unlike Gaussian distributions where expected deviation above 3 Sigma is just a little more than 3 Sigma, in extremistan, the scale stays the same, meaning expected life expectancy at 100 could still be significantly higher than expected life expectancy at 0 <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Sub-selection of Events**: [[limitations_of_super_forecasting | Super forecasters]] may select events that are forecastable but inconsequential, such as "will there be a war yes or no," without considering the scale of the war (e.g., two people killed versus 600,000 people killed) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Inadequacy of Point Forecasts**: It is foolish to provide [[challenges_with_standard_deviation_in_forecasting | point forecast]] for fat-tailed variables, such as how many people will be killed in a pandemic <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Critiquing someone's forecast as a "miss" in such scenarios is also misguided, especially if 95% of observations are below the mean <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   The distribution of people killed in pandemics, like wars, has a tail exponent less than one (similar to a Levy infinite mean distribution) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Transformation Issues**: While elections may have binary outcomes, accurately valuing them requires integrating variance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. It's difficult to translate binary outcomes into real-world consequences <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
    *   For example, forecasting the rate of growth of COVID cannot be directly translated into the number of people killed because the exponential transformation leads to a Pareto distribution for the number of people killed, potentially yielding an infinite expectation <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   **Value at Risk (VaR) Dilemma**: A 95% confidence in VaR (e.g., not losing more than a million) is flawed because the remaining 5% can result in significantly larger losses (e.g., 200 million), demonstrating that the "action" is in the tails <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

## Continuous Payoffs

Continuous payoffs, understood by option traders, represent outcomes in dollars and cents rather than simple "yes/no" predictions <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

### Understanding the Payoff Function
*   **The Importance of the Payoff Function**: The value of a forecast is inseparable from its payoff function <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
    *   Winston Churchill, despite being wrong on many smaller issues (e.g., gold standard, India), was "right on the big question of Hitler's intentions" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. He was right in the "payoff space" where it mattered <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    *   Conversely, Napoleon, despite winning many battles, lost the "war" at Waterloo <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   **Nonlinear Payoffs**: Betting against volatility, for example, is nonlinear <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. One can overestimate volatility by 30% and still make money if the volatility comes in lumps rather than steadily <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
*   **"No Rich Forecasters"**: The lack of "fabulously rich" [[limitations_of_super_forecasting | super forecasters]], in contrast to traders who understand and manage risk and payoff structures, is cited as evidence <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### Probability as a Kernel
A fundamental understanding of probability requires recognizing that [[probability_as_a_kernel_not_a_product | probability is a kernel, not a product]] <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   [[Probability as a kernel not a product | Probability density functions]] (P(X)) do not have meaning by themselves; they must be considered within an integral alongside a function G(X) (the payoff function) <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   G(X) can be an indicator function (for binary outcomes), or continuous, convex, or concave, representing various payoff shapes <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   Option traders do not talk about probabilities in isolation but rather the value of the option <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.