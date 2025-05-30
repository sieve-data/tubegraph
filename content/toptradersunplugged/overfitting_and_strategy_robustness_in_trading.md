---
title: Overfitting and strategy robustness in trading
videoId: pVE8sehGzCQ
---

From: [[toptradersunplugged]] <br/> 

[[overfitting_and_underfitting_in_trading_models | Overfitting]] in trading strategies refers to the assumption that future market conditions will be excessively similar to past data used for backtesting <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>. It occurs when a strategy is overly optimized to specific historical market events, leading to a high "in-sample" (backtested) performance but poor "out-of-sample" (live trading) results <a class="yt-timestamp" data-t="00:47:45">[00:47:45]</a>. The primary goal in strategy development is to maximize out-of-sample performance, as this is where actual profits are made <a class="yt-timestamp" data-t="00:47:53">[00:47:53]</a>.

## Detecting Overfitting

Overfitting can be detected by evaluating a strategy's performance across various historical subsamples <a class="yt-timestamp" data-t="00:48:56">[00:48:56]</a>. This can involve:

*   **Subsample Analysis** <a class="yt-timestamp" data-t="00:48:56">[00:48:56]</a>: Examining how the strategy performs in different decades (e.g., 1970s, 1980s).
*   **Bootstrapping or Block Bootstrapping** <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>: Randomly sampling years, months, or blocks of data to create alternative histories. This technique, particularly block bootstrapping, helps preserve the order of returns within sampled periods, which is crucial for [[systematic_trading_and_trend_following_strategies | trend-following strategies]] <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.
*   **Performance Distribution** <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>: A robust strategy should perform well across many different alternative histories <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>. If performance is highly concentrated and excellent only in histories very similar to the actual past, it suggests overfitting <a class="yt-timestamp" data-t="00:49:26">[00:49:26]</a>.

A general rule of thumb to avoid overfitting is to be wary if a strategy requires hundreds of backtests and intricate adjustments to achieve optimal performance <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>, <a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>. An example of extreme overfitting would be a strategy for gold that incorporates numerous highly specific, arbitrary conditions like "32 and 87-day crossover, with a stop loss of 1.6 times annual volatility, a stop profit of 7.8 times the price, and also closes the position if the third FIB retracement on a Wednesday is a negative value and the moon is full" <a class="yt-timestamp" data-t="00:46:32">[00:46:32]</a>.

## Strategy Robustness

[[challenges_and_strategies_in_improving_trading_systems_without_overoptimization | Strategy robustness]] measures a strategy's ability to maintain performance even when market conditions deviate from historical patterns <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>. To assess robustness, one can analyze the conditional distribution of returns, for instance, by observing how a strategy performs across different interest rate environments (e.g., low, high, rising, or falling interest rates) <a class="yt-timestamp" data-t="00:50:33">[00:50:33]</a>. If performance remains relatively stable across these varying conditions, the strategy is considered robust <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>.

## Timeframes and Costs

The choice of trading frequency and its impact on costs is critical for both [[overfitting_and_underfitting_in_trading_models | overfitting]] and [[challenges_and_strategies_in_improving_trading_systems_without_overoptimization | strategy robustness]].

*   **Slower vs. Faster Trading** <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>: Generally, the slower a strategy trades, the lower its expected returns, as there are fewer trading opportunities <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. However, very fast strategies (e.g., daily or intraday) face significantly higher trading costs due to the need for aggressive execution (crossing the spread) <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>.
*   **Cost Impact** <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>: For very short-term [[systematic_trading_strategies | systematic trading strategies]], trading costs can easily erode potential profits <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>. This often limits profitable short-term strategies to highly liquid markets with lower trading costs, such as equity indices, rather than less liquid commodity markets <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.
*   **Execution Overlays** <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>: Short-term signals can be used as an overlay to a slower, primary [[rulebased trading strategies | rule-based trading strategy]] to improve execution without incurring the high costs of fully trading the faster signal <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>. For example, a daily system might only sell if a short-term mean reversion system indicates a favorable price change in the last day <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.

## Mean Reversion and Risk Management

While [[systematic_trading_and_trend_following_strategies | mean reversion strategies]] offer perfect negative correlation to [[systematic_trading_and_trend_following_strategies | trend-following strategies]] at the same timeframe, making them attractive for diversification <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>, they present unique [[risk_management_in_trading_strategies | risk management]] challenges <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.

*   **Risk Management Difference** <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>: [[systematic_trading_and_trend_following_strategies | Trend-following strategies]] inherently manage risk by closing positions when a trend reverses <a class="yt-timestamp" data-t="00:31:09">[00:31:09]</a>. Mean reversion strategies, however, tend to average down into losing positions, requiring explicit stop losses to prevent significant losses if the market continues to move against the position <a class="yt-timestamp" data-t="00:31:28">[00:31:28]</a>.
*   **Complexity** <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>: Implementing and managing stop losses for mean reversion strategies, especially considering when to re-enter trades, can be complex and lead to over-parameterization <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
*   **Weak Signal** <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>: Long-term value-based mean reversion strategies often have a low Sharpe ratio (around 0.2), making them statistically insignificant as standalone strategies and usually warranting only a small portfolio allocation for diversification benefits <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>, <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>.

## Capacity and Diversification

Account size significantly impacts the ability to build a diversified and robust portfolio, particularly for [[systematic_trading_strategies | systematic trading strategies]] <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>.

*   **Small Accounts** <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>: Very small accounts (e.g., $10,000) may only be able to trade a few instruments due to margin requirements, limiting diversification <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>.
*   **Optimal Range** <a class="yt-timestamp" data-t="00:42:41">[00:42:41]</a>: An optimal account size might be between $50 million and $250 million. In this range, a manager can typically take unconstrained positions in most liquid futures markets, allowing for optimal diversification without significant capacity issues <a class="yt-timestamp" data-t="00:43:15">[00:43:15]</a>.
*   **Large Accounts** <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>: For very large funds (e.g., $30 billion), capacity becomes a major constraint, preventing unconstrained allocation across all markets. This means allocations are often skewed towards highly liquid markets like the S&P 500 rather than smaller markets like cheese futures, purely due to market depth rather than perceived quality <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. This capacity constraint can lead to a degradation in the strategy's Sharpe ratio compared to a smaller, optimally diversified portfolio <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.
*   **Benefits of Larger Funds** <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>: Despite capacity issues, larger funds may have advantages such as the ability to trade OTC markets or employ specialized staff for complex operational needs <a class="yt-timestamp" data-t="00:44:34">[00:44:34]</a>.

Developing a [[building_and_evaluating_systematic_trading_strategies | robust trading strategy]] involves carefully balancing optimization with generalizability, utilizing rigorous testing methods, and understanding the practical implications of trading costs and account capacity.