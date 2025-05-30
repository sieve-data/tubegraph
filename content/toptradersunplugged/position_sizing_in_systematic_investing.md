---
title: Position sizing in systematic investing
videoId: G2xumgdvbKY
---

From: [[toptradersunplugged]] <br/> 

[[systematic_investing | Systematic investing]] involves a raw and honest journey into the world of dependable and consistent investment strategies <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. A key aspect of these strategies is [[position_sizing_and_risk_management_in_trading | position sizing and risk management]], which are considered among the most important elements of the investment process <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.

## Key Principles

Niels Kostrop Larson emphasizes that in [[systematic_investing | systematic investing]], practitioners are primarily [[risk_management_in_systematic_trading | risk managers]] <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. While the performance of systems cannot be controlled, the influence on risk is significant <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This focus on risk is why considerable time is spent on managing different types of risks, especially when dealing with potentially hundreds of positions at any given time <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

## "Pant Sizing" Analogy

The concept of "pant sizing" refers to the flexibility or tightness of parameters in a trading system <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

### Rich Brennan's Approach
Rich Brennan explains that his six [[systematic_trading_strategies | trading systems]], which span different look-back periods (e.g., 50-day to 300-day), each have "loose pants" <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. This means they use a minimal number of parameters (around four to five at most for entry criteria, stops, and trailing stops) <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. Fewer parameters allow for greater responsiveness to price movements, making the system less constrained <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

For shorter-term systems, initial and trailing stops (which are ATR-based for normalization across markets) are typically tighter <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. Conversely, medium to long-term models utilize wider initial and trailing stops <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. This combination of models aims to capture different facets of trends, from short-term momentum to longer, more "wandering" cycles <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.

## Kelly Criterion

The Kelly Criterion is a mathematical formula designed to optimize [[position_sizing_and_risk_management_in_trading | position sizing]] to maximize geometric returns <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>. It considers historical win percentage, loss percentage, and return-to-risk relationship for trades <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.

### Limitations for Trend Following
While aggressive and effective for maximizing returns, the Kelly Criterion relies on underlying assumptions of stable returns and exact knowledge of expected returns <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>. Rich Brennan advises against using the Kelly Criterion for [[systematic_investing_and_trend_following | trend following]] strategies <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>:
*   **Aggressiveness:** It is a very aggressive formula with no room for error <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>.
*   **Volatility and Non-Stationarity:** If win rates or return-to-risk relationships fluctuate (i.e., non-stationarity or regime changes), the formula can lead to significant risk <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.
*   **Tail Events:** Trend followers operate in the "tail region" of return distributions where stability (like a stable mean or standard deviation) doesn't exist, making Kelly inappropriate <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>. Increasing the sample size for Kelly inputs does not account for regime changes, which can lead to "risk of ruin" <a class="yt-timestamp" data-t="00:30:55">[00:30:55]</a>. Markets are not normally distributed and have extreme variations <a class="yt-timestamp" data-t="00:31:33">[00:31:33]</a>.

### Alternative for Convergent Strategies
The Kelly Criterion can be useful for "convergent" trading activities that seek predictable, stable regimes <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>. However, for [[systematic_investing_and_trend_following | trend following]] (divergent strategies), it is not recommended <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>.

### Rich Brennan's Alternative
Instead of Kelly, Rich Brennan uses a standard, very small, equally weighted risk bet for every return stream in his portfolio <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>. He relies on the magnification abilities of the portfolio itself to drive compound annual growth rates over the long term, rather than aggressive [[position_sizing_and_risk_management_in_trading | position sizing]] at the discrete trade level <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.

## System Design and Diversification for Position Sizing

Effective [[systematic_investing | systematic investing]] involves both robust system design and broad diversification to manage [[risk_management_in_systematic_trading | risk]] and capture returns.

### System Design Elements
*   **Targeting Directional Trends:** Systems are specifically configured to capture directional trends <a class="yt-timestamp" data-t="00:50:08">[00:50:08]</a>.
*   **Cutting Losses Short:** A core principle is to cut losses short and let profits run <a class="yt-timestamp" data-t="00:51:55">[00:51:55]</a>. This is achieved through small initial bets, initial stops, and trailing stops <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.
*   **No Profit Targets:** The absence of profit targets, using only trailing exits, allows systems to ride trends for as long as they endure, offering unlimited upside potential <a class="yt-timestamp" data-t="00:52:18">[00:52:18]</a>.
*   **Long and Short Trading:** Trading both long and short positions is crucial, as market tail events can be in either direction. This benefits wealth building and provides correlation benefits at the portfolio level <a class="yt-timestamp" data-t="00:51:33">[00:51:33]</a>.
*   **Positive Skew:** This design produces positive skew in the trade distribution, meaning many small losses are accepted while leaving open the possibility for large, non-linear gains <a class="yt-timestamp" data-t="00:53:02">[00:53:02]</a>. A small percentage of trades (5-10%) are responsible for moving the needle and providing "lifting power" to the portfolio <a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>.

### Diversification for Outlier Capture
[[systematic_investing_strategies | Diversification]] is essential for [[systematic_investing | trend followers]] <a class="yt-timestamp" data-t="00:55:24">[00:55:24]</a>.
*   **Uncorrelated Streams:** It brings together uncorrelated return streams, which smooths the equity curve at the portfolio level by offsetting drawdowns <a class="yt-timestamp" data-t="00:55:39">[00:55:39]</a>.
*   **Frequency of Outliers:** While individual market outliers are infrequent, trading many markets (e.g., 60 markets) increases the frequency of capturing these non-linear anomalies across the portfolio <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.
*   **Distributed Outliers:** The outliers are typically not "coincident" (occurring at the same time in the same location of the portfolio distribution), but rather widely distributed throughout the time series <a class="yt-timestamp" data-t="00:56:57">[00:56:57]</a>. This continuous "lifting power" allows for optimal compound growth over time <a class="yt-timestamp" data-t="00:57:09">[00:57:09]</a>.
*   **CAGR Improvement:** Unlike traditional diversification methods that primarily reduce volatility, [[systematic_investing | trend following]] also improves the compound annual growth rate (CAGR) by actively capturing these non-linear anomalies <a class="yt-timestamp" data-t="01:02:15">[01:02:15]</a>.
*   **Market Behavior and Trend Amplification:** Markets exhibit "leptokurtic" distributions (fat tails) in liquid markets, which is attributed to the behavioral tendencies of participants <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>. During periods of uncertainty or boom, when most "convergent" strategies (e.g., fundamental investing, many technical analysis methods, central bank interventions) fail, participants are forced into "divergent" behavior, amplifying existing trends. [[systematic_investing_and_trend_following | Trend followers]], operating on the divergent side (only about 10% of participants), capitalize on this shift in wealth flow <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>. This explains why [[systematic_investing_and_trend_following | trend following]] performs well during both boom and bust periods, as it benefits from altered trading behavior and the resulting non-linear amplification of trends <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.