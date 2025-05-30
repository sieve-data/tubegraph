---
title: Automated Trading Systems
videoId: VNSu5Pt8at0
---

From: [[toptradersunplugged]] <br/> 

An automated trading system is a type of [[systematic_trading_systems | systematic trading system]] that relies on algorithms and predefined rules to execute trades, often with minimal human intervention <a class="yt-timestamp" data-t="00:00:05">00:00:05</a>. These systems are designed to operate efficiently and consistently, processing market data and making trading decisions automatically <a class="yt-timestamp" data-t="00:00:08">00:00:08</a>.

## Efficiency and Time Commitment

One of the primary benefits of an [[The Role of Automation in Trading | automated]] trading system is the reduced time commitment required from the trader <a class="yt-timestamp" data-t="00:00:06">00:00:06</a>. For a fully automated system, a trader might spend as little as five minutes per month per market, utilizing price data and automatic filters to catch bad prices <a class="yt-timestamp" data-t="00:00:08">00:00:08</a>. This efficiency allows for diversification across many markets; for instance, trading 100 or 150 liquid futures markets would be feasible if capital allows, as even marginal gains from additional markets justify the minimal time investment <a class="yt-timestamp" data-t="00:00:28">00:00:28</a>.

## Risk Management in Automated Trading

Effective risk management is crucial for [[systematic_trading_strategies | systematic trading strategies]]. Risk is understood to have two components: predictable and unpredictable <a class="yt-timestamp" data-t="00:05:40">00:05:40</a>. The main challenge arises when unpredictable risk is ignored or assumed not to exist <a class="yt-timestamp" data-t="00:05:48">00:05:48</a>.

### Modeling Risk

Most trading models rely on assumptions about how returns appear, often using concepts like standard deviation and correlation structure <a class="yt-timestamp" data-t="00:06:10">00:06:10</a>. While these models can be made more sophisticated by including higher moments (skew, kurtosis) and complex correlations, increasing complexity also increases the need for calibration <a class="yt-timestamp" data-t="00:06:47">00:06:47</a>. There is a risk that sophisticated models may lead to the false assumption that expected risk is fully captured, leaving less room for unexpected risk <a class="yt-timestamp" data-t="00:07:30">00:07:30</a>.

A simpler approach advocates for using the most basic risk model (standard deviation and correlation only) while consciously acknowledging exposure to errors <a class="yt-timestamp" data-t="00:08:15">00:08:15</a>. This involves mentally considering scenarios where correlations might be completely wrong (e.g., all 1 or -1, whichever is worse for the position) and setting limits based on potential losses in such scenarios, leading to automatic position cuts if exposure exceeds these limits <a class="yt-timestamp" data-t="00:08:31">00:08:31</a>. Simple, robust models help ensure traders do not over-rely on potentially flawed assumptions <a class="yt-timestamp" data-t="00:09:05">00:09:05</a>.

### Position Sizing and Stop Losses

The framework for managing positions, including initial sizing and subsequent adjustments, is critical <a class="yt-timestamp" data-t="00:09:49">00:09:49</a>. If this aspect is managed correctly, the exact entry point of a trade becomes less significant <a class="yt-timestamp" data-t="00:10:11">00:10:11</a>.

Traditional trading advice sometimes conflates different aspects of risk management, such as setting a stop-loss based on a percentage of capital <a class="yt-timestamp" data-t="00:11:10">00:11:10</a>. However, the market's volatility and the appropriate holding period for a trade are independent of an individual's capital <a class="yt-timestamp" data-t="00:12:44">00:12:44</a>. Therefore, stop-loss calculations should be based on market volatility (wider stop for more volatile markets) and the desired holding period (wider stop for longer holding periods if trading costs are high) <a class="yt-timestamp" data-t="00:12:59">00:12:59</a>. Only after determining the stop-loss should the amount of capital and desired risk be factored in to determine the position size <a class="yt-timestamp" data-t="00:13:39">00:13:39</a>. The amount of risk taken on capital depends on multiple factors, including the expected profitability and properties of the system, such as whether it's a divergent or convergent system <a class="yt-timestamp" data-t="00:14:02">00:14:02</a>.

### Continuous vs. Discrete Position Management

Two main approaches to position management exist:
*   **Continuous Trading System:** This approach involves a target position implied by forecasts, and trading occurs when the target position changes <a class="yt-timestamp" data-t="00:16:04">00:16:04</a>. There is no concept of a "trade" with a fixed stop-loss; instead, positions might shift from long to flat to short <a class="yt-timestamp" data-t="00:16:20">00:16:20</a>. This is suitable for fully [[systematic_trading_systems | systematic trading systems]] <a class="yt-timestamp" data-t="00:17:08">00:17:08</a>.
*   **Discrete Position Management:** This involves discrete trades that are put on and only taken off when a stop-loss is hit <a class="yt-timestamp" data-t="00:16:50">00:16:50</a>. This method is better for non-[[systematic_trading_strategies | systematic trading rules]] or when trading instruments like options where the premium paid is the maximum loss <a class="yt-timestamp" data-t="00:17:06">00:17:06</a>. It simplifies manual evaluation of positions, making it easier for non-[[systematic_trading_systems | systematic]] traders to manage their risk <a class="yt-timestamp" data-t="00:18:17">00:18:17</a>.

### Portfolio Volatility Target

Many professional managers use a volatility target for their portfolio (e.g., 15-20%) <a class="yt-timestamp" data-t="00:18:52">00:18:52</a>. This target is generally an average they expect to achieve over years, not necessarily on a daily or monthly basis <a class="yt-timestamp" data-t="00:19:56">00:19:56</a>. The actual risk run is driven by the confidence in forecasts: weaker forecasts lead to lower risk, while strong forecasts (e.g., "all lights flashing green") can lead to higher risk, usually capped by a speed limit <a class="yt-timestamp" data-t="00:20:16">00:20:16</a>.

Running a fixed risk target (e.g., always 50 miles an hour) can be dangerous, especially when potential returns are compressed or when many quantitative managers hold similar positions, leading to illiquidity and sudden losses if the market moves against them <a class="yt-timestamp" data-t="00:21:35">00:21:35</a>.

## Team Organization for [[Building and evaluating systematic trading strategies | Systematic Funds]]

When forming a research team for a [[systematic_trading_systems | systematic fund]], three considerations are key: team size, educational attainment/intelligence, and diversity of opinions and backgrounds <a class="yt-timestamp" data-t="00:23:10">00:23:10</a>.

*   **Team Size:** Large numbers of researchers are often unnecessary and can be damaging <a class="yt-timestamp" data-t="00:23:38">00:23:38</a>. Once a system is designed and working, a few people are typically sufficient for maintenance <a class="yt-timestamp" data-t="00:24:00">00:24:00</a>. For a CTA with a $100 million AUM, half a dozen people are probably enough <a class="yt-timestamp" data-t="00:24:25">00:24:25</a>.
*   **Intellect and Education:** While smart people are needed, an entire team of "super geniuses" can be dysfunctional <a class="yt-timestamp" data-t="00:25:07">00:25:07</a>. There isn't necessarily a positive correlation between intelligence (beyond a certain point) or number of degrees and team effectiveness <a class="yt-timestamp" data-t="00:25:21">00:25:21</a>. A team of clever individuals, not necessarily all geniuses, is preferable, as geniuses can be difficult to manage and may avoid "dirty work" <a class="yt-timestamp" data-t="00:25:51">00:25:51</a>.
*   **Diversity:** Teams should have diverse backgrounds to avoid "herding behavior" <a class="yt-timestamp" data-t="00:26:25">00:26:25</a>. The business of [[systematic_trading_systems | systematic trading]] requires varied skills, including IT/computing, economics, financial markets knowledge (ideally with trading experience), and statistical ability <a class="yt-timestamp" data-t="00:27:24">00:27:24</a>. A team with a range of backgrounds will think differently, leading to more robust outcomes <a class="yt-timestamp" data-t="00:28:04">00:28:04</a>.

## Evaluating Historical Track Records

Assessing historical track records, especially for [[longterm_trading_systems | long-term trading systems]], is challenged by statistical uncertainty <a class="yt-timestamp" data-t="00:29:39">00:29:39</a>. Even with decades of data, it's difficult to determine if past performance is due to skill or luck <a class="yt-timestamp" data-t="00:29:50">00:29:50</a>.

Key considerations for investors:
*   **Contextual Comparison:** A track record should be similar to others in the same strategy <a class="yt-timestamp" data-t="00:31:21">00:31:21</a>. For example, if a [[Systematic trading and trend following strategies | trend-following]] manager lost money in a year when trend-following generally performed poorly, it raises questions about their strategy <a class="yt-timestamp" data-t="00:31:31">00:31:31</a>. Exceptional performance far outside the expected distribution can be a red flag, indicating either extreme skill or a different, potentially riskier, strategy <a class="yt-timestamp" data-t="00:31:56">00:31:56</a>.
*   **Qualitative Judgment:** Qualitative assessment is crucial <a class="yt-timestamp" data-t="00:33:07">00:33:07</a>. Investors should speak to researchers, ensure they can explain their methods and perceived risks, and verify transparency <a class="yt-timestamp" data-t="00:32:51">00:32:51</a>.

## Concerns About Systematized Strategies

Concerns about saturation in [[Systematic trading strategies | systematized strategies]] (e.g., too many people doing [[Systematic trading and trend following strategies | trend following]] or high-frequency trading) depend on factors like the size of [[systematic_trading_systems | systematic traders]] versus others, the trading style, and the likelihood of market condition changes <a class="yt-timestamp" data-t="00:33:54">00:33:54</a>.

*   **High-Frequency Trading (HFT):** HFT is almost entirely systematized, as human speed cannot compete with latency requirements <a class="yt-timestamp" data-t="00:34:21">00:34:21</a>. While the market structure may evolve (e.g., IEX Exchange designed to frustrate HFT), HFT is expected to remain profitable, though individual firm profitability and specific strategy effectiveness may change over time <a class="yt-timestamp" data-t="00:35:51">00:35:51</a>.
*   **Medium-Speed Relative Value Trading:** Strategies like long-short equity trading based on factors (e.g., book value) can see profitability erode if too many market participants adopt the same strategy <a class="yt-timestamp" data-t="00:37:12">00:37:12</a>. Opportunities disappear as prices converge <a class="yt-timestamp" data-t="00:37:31">00:37:31</a>. The profitability of such strategies is cyclical, often picking up after market crashes when mispricings become more pronounced <a class="yt-timestamp" data-t="00:37:59">00:37:59</a>.
*   **Slow-Edge Strategies (e.g., [[Systematic trading and trend following strategies | Trend Following]]):** Unlike relative value, if more people follow [[Systematic trading and trend following strategies | trend following]], it can become self-reinforcing, as buying into rising markets pushes prices higher <a class="yt-timestamp" data-t="00:39:17">00:39:17</a>. However, this creates execution risk: if many traders running the same model rush for the exits during a correction, liquidity problems can arise <a class="yt-timestamp" data-t="00:39:45">00:39:45</a>. While underlying returns of slow [[systematic_trading_and_trend_following_strategies | trend-following strategies]] are expected to persist due to human behavior, periods of crowding may lead to unexpected liquidity issues <a class="yt-timestamp" data-t="00:40:49">00:40:49</a>. The exit strategy is a particularly important factor in these strategies to avoid being caught in crowded trades <a class="yt-timestamp" data-t="00:41:15">00:41:15</a>.

## Key Performance Statistics

When analyzing [[systematic_trading_systems | systematic trading systems]], the Sharpe ratio is a commonly used metric due to its simplicity and intuitive understanding <a class="yt-timestamp" data-t="00:42:19">00:42:19</a>. However, since the Sharpe ratio assumes symmetric returns, it's also important to examine skew <a class="yt-timestamp" data-t="00:42:42">00:42:42</a>.

*   **Positive Skew:** More losing days than winning days, but winning days are larger (characteristic of a [[Systematic trading and trend following strategies | trend following strategy]]) <a class="yt-timestamp" data-t="00:42:50">00:42:50</a>.
*   **Negative Skew:** More winning days than losing days, but losses are larger (characteristic of relative value or carry strategies) <a class="yt-timestamp" data-t="00:43:03">00:43:03</a>.

Higher-order moments like skew can be unreliable and easily distorted by a few data points <a class="yt-timestamp" data-t="00:43:21">00:43:21</a>. Be wary of negatively skewed strategies with high Sharpe ratios that have never experienced a significant loss in backtesting (known as the "peso problem"), as they may be exposed to unquantified risks <a class="yt-timestamp" data-t="00:43:40">00:43:40</a>.

## Personal Automated Trading System

An example of a personal [[The Role of Automation in Trading | automated]] trading system trades about 40 futures markets, diversified across main asset classes and geographies <a class="yt-timestamp" data-t="00:45:42">00:45:42</a>. The system seeks to add more markets with more capital, as theoretically, there's always a diversification benefit as long as the cost of adding a market doesn't exceed its potential returns <a class="yt-timestamp" data-t="00:45:57">00:45:57</a>.

The system is approximately 40% [[Systematic trading and trend following strategies | trend following]], incorporating different variations of trend following <a class="yt-timestamp" data-t="00:49:01">00:49:01</a>. It also includes a "chunk of carry" strategy, looking at yield curve slopes and roll/contango in various asset classes <a class="yt-timestamp" data-t="00:49:20">00:49:20</a>. While some systems might perform better in specific asset classes (e.g., fast trend following in equity indices), the system uses the same core logic across all markets, adjusting for trading costs (trading more quickly in cheap markets like Nasdaq/S&P 500 than in expensive markets like Australian interest rate futures) <a class="yt-timestamp" data-t="00:49:43">00:49:43</a>.

Additionally, it holds a small (5-10% of total risk) systematic short bias on volatility index markets (VIX and V2X) <a class="yt-timestamp" data-t="00:50:53">00:50:53</a>. This is based on the belief that being short the implied vs. realizable premium is a source of return, acknowledging its high skew and potential for significant losses in extreme events <a class="yt-timestamp" data-t="00:51:04">00:51:04</a>. However, the diversification with trend following and carry strategies mitigates this risk <a class="yt-timestamp" data-t="00:51:52">00:51:52</a>.

Historically, in [[Systematic trading and trend following strategies | trend following]], a disproportionate part of profits has come from the long side of trades, especially in financial markets with long secular bull trends over the past 30 years <a class="yt-timestamp" data-t="00:52:06">00:52:06</a>. However, due to this historical bias, it's difficult to statistically prove if different strategies are truly needed for bull vs. bear markets <a class="yt-timestamp" data-t="00:52:43">00:52:43</a>. A preference for simplicity means strong evidence is required to implement such adjustments <a class="yt-timestamp" data-t="00:53:27">00:53:27</a>.

## Estimating Drawdowns

To gauge a system's potential drawdown, one can use artificial data and run numerous simulations <a class="yt-timestamp" data-t="00:55:45">00:55:45</a>. This avoids the bias of real-world data, where actual drawdowns might be exceptionally small or large due to luck <a class="yt-timestamp" data-t="00:56:00">00:56:00</a>.

By running multiple simulations with random data (assuming a certain Sharpe ratio and skew), the distribution of drawdowns can be analyzed <a class="yt-timestamp" data-t="00:56:24">00:56:24</a>.
*   **Average Drawdown:** For a system with a 20% risk target and 0.5 Sharpe ratio, the average drawdown in any given day across simulations is about 10% <a class="yt-timestamp" data-t="00:57:36">00:57:36</a>.
*   **Worst Drawdown:** Over a 10-year period, the average worst drawdown is typically around 40% (twice the risk target) <a class="yt-timestamp" data-t="00:58:17">00:58:17</a>. However, extreme scenarios can see drawdowns of 80% <a class="yt-timestamp" data-t="00:58:46">00:58:46</a>.

This reinforces the message that investors should be prepared to lose all the money they are trading, even with a strong Sharpe ratio, as extreme unluckiness is always a possibility <a class="yt-timestamp" data-t="00:59:02">00:59:02</a>.

## Investor Diligence Questions

When meeting with [[systematic_trading_systems | systematic fund]] managers, investors should ask questions that are often overlooked:
*   "What can go wrong? What keeps you awake at night?" <a class="yt-timestamp" data-t="01:00:16">01:00:16</a> This helps uncover exposure to severe, rare risks that might not have occurred yet <a class="yt-timestamp" data-t="01:00:44">01:00:44</a>.
*   "How did you fit this particular model? Where did the idea come from?" <a class="yt-timestamp" data-t="01:01:57">01:01:57</a> This helps detect [[building_and_evaluating_systematic_trading_strategies | overfitting]], where a model is too tailored to past data and may not perform well in the future <a class="yt-timestamp" data-t="01:01:01">01:01:01</a>. If the research process involves many iterations, it could be a red flag for overfitting <a class="yt-timestamp" data-t="01:01:50">01:01:50</a>.
*   Questions about trading costs <a class="yt-timestamp" data-t="01:02:29">01:02:29</a>, as these are often underestimated but significantly impact profitability.