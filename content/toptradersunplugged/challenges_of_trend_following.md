---
title: challenges of trend following
videoId: xrNozmQ53ck
---

From: [[toptradersunplugged]] <br/> 

[[Trend following as a trading strategy|Trend following]] is an investment strategy that seeks to capitalize on sustained price movements in markets. While often perceived as straightforward, the implementation and consistent success of [[Trend following as a trading strategy|trend following]] strategies involve significant complexities and challenges, particularly in the areas of model development, data analysis, and psychological application <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.

## Psychological and Perceptual Challenges
[[Trend following as a trading strategy|Trend following]] is psychologically difficult to apply because it often goes against intuitive human tendencies <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>. It's considered "the hardest game in town to apply psychologically" due to the need to act contrary to what one's brain might suggest <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. This difficulty is also what creates a significant edge in the strategy <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.

Despite its complexity, [[Trend following as a trading strategy|trend following]] is often simplistically described on social media, implying it involves only "one entry, one exit, one stop loss" <a class="yt-timestamp" data-t="01:08:58">[01:08:58]</a>. This oversimplification can be misleading to investors, making the strategy appear easy or as a factor that should be "free" <a class="yt-timestamp" data-t="01:09:51">[01:09:51]</a>. However, successfully executing [[Trend following as a trading strategy|trend following]] for decades requires highly intelligent and talented individuals in research and execution <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## Technical Challenges in Model Development

The development of systematic trading models involves carefully analyzing price data to identify patterns and signals while mitigating the impact of noise.

### Signal and Noise
When analyzing price data, traders look for patterns that positively correlate with systems used to extract profits <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>. This identifiable pattern is referred to as a **signal** <a class="yt-timestamp" data-t="00:22:39">[00:22:39]</a>. For a [[Trend following trading strategies|trend following]] system, a signal is a directionally trending or divergent price series <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.

**Noise** refers to all other price patterns that interfere with the primary signal <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>. For a trend follower, noise includes not only random patterns but also convergent price patterns <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. Applying a [[Trend following trading strategies|trend following]] model to a convergent pattern results in a negative correlation, leading to "whipsaw" losses <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. Essentially, one trader's signal (e.g., a mean reversion trader's convergent pattern) can be another's noise (e.g., a trend follower's) <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.

An optimal trading system aims to have a **high signal-to-noise ratio**, meaning signals are more frequent and material relative to background noise <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. If a [[Trend following trading strategies|trend following]] model is applied to a noisy series with few signals, it will perform poorly due to a low signal-to-noise ratio <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>. While a signal might be the result of a random directional trend, ideally, it stems from an enduring bias or momentum that can extend into the future <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.

### Overfitting and Underfitting

Quantitative models must be "fit" to price data to be successful <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

*   **Overfitting** occurs when a trading system extracts both signal and noise from price data, responding to patterns that lead to profitable outcomes by chance <a class="yt-timestamp" data-t="00:42:56">[00:42:56]</a>. This often results from data mining processes that seek specific statistical objectives (e.g., minimum CAGR, maximum drawdown) without logical design principles, leading the model to "train itself to the noise" <a class="yt-timestamp" data-t="00:43:36">[00:43:36]</a>. Overfit systems quickly degrade in the future because there's no enduring edge <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.
*   **Underfitting** describes a model that fails to optimally extract the signal, leaving much of the opportunity unexploited <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a>. While inefficient, an underfit model is generally preferable to an overfit one, especially when targeting unique, unrepeated outliers <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>. An optimally fit system preferentially responds to signals and not noise <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>.

### Selection Bias
[[Challenges and strategies in trend following|Challenges and strategies in trend following]] arise when selecting models. **Selection bias** is introduced as soon as one chooses from competing alternatives, such as picking the best-performing model from a set of backtest results <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>. The problem is that the best-performing strategy might be a result of "100 percent luck" from trading noise rather than an enduring signal <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. It's impossible to completely avoid this bias, but it's crucial to be aware of it <a class="yt-timestamp" data-t="00:51:03">[00:51:03]</a>.

## Strategies to Mitigate Overfitting
To address the [[challenges_and_strategies_in_trend_following|challenges of trend following]], several strategies can be employed to reduce the likelihood of overfitting:

*   **Design-First Logic:** Instead of relying solely on statistical outcomes, apply "golden rules" defined by logical principles, such as "cut losses short" and "let profits run" <a class="yt-timestamp" data-t="00:55:17">[00:55:17]</a>. This establishes logical constraint boundaries before statistical assessment <a class="yt-timestamp" data-t="00:58:07">[00:58:07]</a>.
*   **Simple Models with Few Parameters:** Choosing "loose pants models" with fewer parameters makes them less over-optimized to historical data <a class="yt-timestamp" data-t="00:58:21">[00:58:21]</a>. Simple models can capture a greater variation of trend forms and offer a larger sample size of exploitable signals <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>.
*   **Visual Mapping Process:** Instead of relying on statistical metrics (e.g., Sharpe ratio, CAGR) to select models, visually map the trade outcomes and equity curve against the actual price data <a class="yt-timestamp" data-t="01:01:02">[01:01:02]</a>. This allows direct observation of whether the equity curve responds correctly to trending periods and stagnates/deteriorates during non-trending (noisy) periods <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>.
*   **Multi-Market Testing:** Apply the same [[Trend following trading strategies|trend following]] model across a diversified portfolio of markets <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a>. This increases the sample size of trades (e.g., 60 markets * 10 trades/market = 600 trades) and reduces the chance of overfitting to a single market's characteristics <a class="yt-timestamp" data-t="01:04:41">[01:04:41]</a>. Each market provides an "alternative history" to test the model's robustness <a class="yt-timestamp" data-t="01:05:52">[01:05:52]</a>.
*   **Use All Available Data:** Avoid splitting data into "in-sample" and "out-of-sample" sets for final testing <a class="yt-timestamp" data-t="01:06:11">[01:06:11]</a>. Using all data exposes the model to as many different market regimes as possible, enhancing its robustness against future market changes <a class="yt-timestamp" data-t="01:06:49">[01:06:49]</a>.

## Conclusion: The True Nature of Trend Following

[[Trend following trading strategies|Trend following]] is not a simple undertaking <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>. It requires a deep understanding of market dynamics, sophisticated model development techniques, and rigorous testing processes to avoid common pitfalls like overfitting <a class="yt-timestamp" data-t="01:11:58">[01:11:58]</a>. The consistent, long-term success of [[Trend following trading strategies|trend following]] strategies is a testament to their robustness when properly implemented <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>.