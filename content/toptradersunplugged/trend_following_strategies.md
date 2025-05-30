---
title: trend following strategies
videoId: xrNozmQ53ck
---

From: [[toptradersunplugged]] <br/> 

[[trend_following_strategies | Trend following strategies]] are a core component of systematic investing, aiming to identify and capitalize on persistent price movements in financial markets <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This approach involves a rules-based methodology to navigate global markets <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Core Concepts of [[trend_following_strategies | Trend Following Strategies]]

[[trend_following_strategies | Trend following strategies]] inherently deal with market volatility and different trade durations, from long-sided to short-sided trades, and short-term to long-term volatility <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Signal and Noise

When analyzing price data, a "signal" refers to a pattern that positively correlates with a system's ability to extract profits <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. For a [[trend_following_strategies | trend follower]], the signal is a directionally trending or divergent price series <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>.

"Noise," conversely, encompasses all other price patterns that interfere with the primary signal <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>. For a [[trend_following_strategies | trend follower]], noise can include random patterns or convergent price patterns <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>. Applying a [[trend_following_strategies | trend following]] model to a convergent pattern results in a negative correlation, often leading to whipsaws <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

A high signal-to-noise ratio in price data indicates that materially trending price series are more frequent than background noise, providing significant opportunities for [[trend_following_strategies | trend following]] models to generate profits <a class="yt-timestamp" data-t="01:09:10">[01:09:10]</a>. If a [[trend_following_strategies | trend following]] model is applied to a noisy series with few signals, it will underperform <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>. It's crucial to distinguish between signals that are the result of random directional trends and those that are from enduring biases or momentum <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.

### Model Fitting

Successful trading systems must be "optimally fit" to the signal they target to generate optimal profits <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>. This means the system preferentially responds to signals and avoids noise <a class="yt-timestamp" data-t="00:42:28">[00:42:28]</a>.

#### Overfitting

An "overfit" trading system extracts both signal and noise, responding to price patterns that simply lead to profitable outcomes, which could be due to luck <a class="yt-timestamp" data-t="00:42:56">[00:42:56]</a>. This often occurs in data mining processes when models are trained to meet specific criteria (e.g., minimum CAGR, maximum drawdown) without discriminatory guidance, causing them to exploit "luck in the noise" <a class="yt-timestamp" data-t="00:43:36">[00:43:36]</a>. An overfit system applied to future data tends to degrade quickly as it lacks an enduring edge <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.

#### Underfitting

An "underfit" trading system fails to optimally extract the signal from a price series, leaving many opportunities unexploited <a class="yt-timestamp" data-t="00:44:58">[00:44:58]</a>. While inefficient, an underfit model is generally preferable to an overfit model, especially when targeting unique and exotic outliers in the market <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>. Overfitting to historical trends can cause a system to miss future trends if their nature changes <a class="yt-timestamp" data-t="00:46:21">[00:46:21]</a>.

### Selection Bias

Selection bias enters a trading process when choosing from competing alternatives, such as selecting one model over another based on past performance <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>. This bias is unavoidable, as choices must be made, but awareness of it is critical <a class="yt-timestamp" data-t="00:51:03">[00:51:03]</a>. The problem is that the "best" performing strategy could be a result of random noise or luck rather than a truly causative signal <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>.

## Methods for Robust [[trend_following_strategies | Trend Following Strategies]] Development

To reduce the chances of overfitting, especially for [[trend_following_strategies | trend following strategies]] that differ from convergent strategies, several principles are applied:

1.  **Design First Logic**
    *   Emphasizes applying "golden rules" defined by logic, not solely statistics, to define a system capable of exploiting the desired edge (e.g., "cut losses short, let profits run") <a class="yt-timestamp" data-t="00:55:17">[00:55:17]</a>. This eliminates the risk of overfitting from an iterative data mining process that lacks pre-defined principles <a class="yt-timestamp" data-t="00:56:38">[00:56:38]</a>.
2.  **Simple Models with Few Parameters**
    *   Utilizing "loose pants models" that are less over-optimized to historical data <a class="yt-timestamp" data-t="00:58:21">[00:58:21]</a>. Simple models can capture a greater variation in trend forms, providing a larger sample size for analysis, whereas complex, prescriptive models might overfit to specific trend forms and miss others <a class="yt-timestamp" data-t="00:58:40">[00:58:40]</a>.
3.  **Visual Mapping Process**
    *   Instead of relying solely on statistical metrics (e.g., Sharpe ratio, CAGR, profit factor) to select models, visually map the equity curve (trade outcomes) against the time series of the price data <a class="yt-timestamp" data-t="01:01:02">[01:01:02]</a>. This allows direct observation of how the system responds to clear outliers (trending periods) versus periods of stagnation or deterioration (noise), indicating whether it's truly exploiting signals or overfit to noise <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>.
4.  **Multi-Market Testing**
    *   Applying a single [[trend_following_strategies | trend following]] model across a diversified portfolio of markets increases the sample size significantly, as a single market may have few trends over a long history <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a>. This approach ensures the model isn't overfit to the characteristics of a single market but has universal applicability across diverse market histories and regimes <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.
5.  **Using All Data**
    *   Avoid separating data into "in-sample" and "out-of-sample" sets for final testing <a class="yt-timestamp" data-t="01:06:11">[01:06:11]</a>. All available data should be used in the backtesting process to ensure the model has been exposed to as many different market regimes as possible <a class="yt-timestamp" data-t="01:06:35">[01:06:35]</a>. Robustness is less about sample size and more about exposure to variety <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

## Perceived Simplicity vs. Reality

Despite common perceptions, particularly on social media, that [[trend_following_strategies | trend following strategies]] are "super easy" with simple entry, exit, and stop-loss rules <a class="yt-timestamp" data-t="01:08:58">[01:08:58]</a>, the reality for experienced managers and long-term successful firms like DUNN, Aspect Capital, and Graham Capital is that it's a complex and challenging endeavor <a class="yt-timestamp" data-t="01:09:12">[01:09:12]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

It involves:
*   Understanding the dispersion in how "trend" is defined and targeted across the industry <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   The psychological difficulty of applying a strategy that often goes against intuition <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Dealing with varying philosophies (e.g., 100% [[trend_following_strategies | Trend Following Investment Strategy]] vs. multi-strategy approaches) <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>, <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   Considering factors like dynamic position sizing <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   The intricacies of data handling, volatility, and correlations <a class="yt-timestamp" data-t="01:08:18">[01:08:18]</a>.

The idea that [[trend_following_strategies | trend following]] is so simple that it should be free or easily replicated at low cost often misleads investors <a class="yt-timestamp" data-t="01:10:02">[01:10:02]</a>. Comparisons between backtested models (with no fees or modern low commissions) and actual manager track records (with historical fees and operational costs) are often flawed <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>. True long-term success in [[trend_following_strategies | trend following]] requires sophisticated research, execution, and talented professionals <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. The data shows that [[trend_following_strategies | trend following]] is one of the most robust [[trend_following_investment_strategies | investment strategies]] available <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>.