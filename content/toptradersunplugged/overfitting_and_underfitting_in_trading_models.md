---
title: overfitting and underfitting in trading models
videoId: xrNozmQ53ck
---

From: [[toptradersunplugged]] <br/> 

Systematic investing involves analyzing price data to develop and apply trading models. Two critical concepts in this process are [[overfitting_and_strategy_robustness_in_trading | overfitting]] and underfitting, which describe negative system outcomes arising from how models are developed or "trained" and selected [02:11:51].

## Signal vs. Noise in Price Data

When analyzing price data, traders look for patterns that positively correlate with their systems to extract profits [02:26:26]. This pattern is referred to as a "signal" [02:39:42]. For example:
*   **Trend followers** seek a directionally trending or divergent price series as their signal [02:42:45]. They deploy simple trend following models to profit from this signal [02:43:02].
*   **Mean reversion traders** look for signals comprising repeating price oscillations around an equilibrium, a convergent price series [02:43:08]. They use mean reverting models to extract profits from this signal [02:43:19].

A successful trading system must be "optimally fit" to the signal it targets to generate optimal profits [02:54:55]. The definition of a price signal is intricately tied to the nature of the system used to exploit it [02:55:31].

**Noise** refers to all other price patterns that interfere with the primary signal being sought [02:55:46]. This isn't just random patterns; for a trend follower, a convergent price pattern is noise [02:56:11]. When a trend following model is applied to a convergent price pattern, it results in a negative correlation, leading to "whipsaws" [02:56:21]. Conversely, a trend follower's desired signal (divergent price pattern) is considered noise by a mean reverting trader, and vice versa [02:56:57].

The goal is to have a **high signal-to-noise ratio** in the price data, meaning material trending price series are more frequent relative to background noise [02:58:00]. This provides significant opportunities for models to generate more profits than losses [02:58:30]. Conversely, models embedded in noisy price data with few signals will perform poorly due to a low signal-to-noise ratio [02:58:42].

Even when a signal is present, it can be random or a result of an enduring bias like momentum [02:59:55]. Focusing solely on signals reduces the chance of systems participating in price data that is noise, leading to trade outcomes with a higher signal-to-noise ratio [03:10:09]. This process of fitting models to signals aims to extract actual signals from price data, as opposed to accompanying noise [03:10:56].

If there is no exploitable signal in price data, trading systems should degrade or stagnate over time [03:34:00]. If a system produces profitable outcomes when there are no trending price signals, it is highly suspicious that those models are [[overfitting_and_strategy_robustness_in_trading | overfit]] to noise rather than signal [03:34:40]. Long-term profits require an enduring signal that is exploited by trading models [03:34:07].

## Components of Strategy Performance

The performance of any trading strategy is the sum of two components [04:48:51]:
1.  **Edge Extraction:** The ability of the strategy to extract an edge from market data, reflecting its intrinsic power and how optimally fit it is to extract enduring signals [04:49:54].
2.  **Luck:** Performance results attributed to trading noise, which could be good or bad luck [04:51:21]. It is difficult to separate good luck from a real signal, making it hard to determine if a strategy is optimally fit [04:52:12].

## Defining Fit Systems

*   **Optimally Fit Trading System:** A system that preferentially responds to signals in price data and avoids responding to noise [04:52:25]. This leads to greater confidence in exploiting future market signals [04:53:56].
*   **[[overfitting_and_strategy_robustness_in_trading | Overfit]] Trading System:** A system that extracts both signal and noise from a price series, responding to patterns that lead to profitable outcomes, regardless of whether they are real signals or random noise [04:56:58]. This is a common problem in data mining processes where criteria like minimum compound annual growth rate or maximum drawdown are set, and the system trains itself to both noise and signal to meet these objectives [04:56:58]. Such systems quickly degrade when applied to future price series because there is no enduring edge [04:56:58]. Data mining programs that forage for solutions without specific direction in defining signal extraction often lead to [[overfitting_and_strategy_robustness_in_trading | overfit]] outcomes [04:56:58].
*   **Underfit Trading System:** A model in which the trading system fails to optimally extract the signal from a price series, leaving many opportunities unexploited [04:58:56]. While inefficient, an underfit strategy does not necessarily degrade in the future and is generally preferable to an [[overfitting_and_strategy_robustness_in_trading | overfit]] model, especially when targeting unique outliers [04:58:56]. An underfit model is less prescriptive, allowing it to capture a greater variety of trend forms and provide a larger sample size [04:59:50].

## Selection Bias

[[Cognitive biases in trading and investing | Selection bias]] enters a trading process when a choice must be made from competing alternatives [04:58:55]. For example, if two models are developed and tested on unseen data, and one outperforms the other, choosing the better-performing model introduces selection bias [04:58:55]. This bias means that the chosen best-performing strategy might be the result of random noise (luck) rather than a real, causative signal [04:58:55]. It is impossible to avoid this bias entirely, but it is crucial to be aware of it [04:58:55].

## Methods to Reduce [[overfitting_and_strategy_robustness_in_trading | Overfitting]]

Traditional methods like Monte Carlo or walk-forward analysis are often unsuitable for trend following due to the sporadic nature of trends [05:54:10]. Rich Brennan employs several principles to reduce [[overfitting_and_strategy_robustness_in_trading | overfitting]] in his models:

1.  **Design-First Logic:** Apply "golden rules" defined by logic, not statistics, to develop a system capable of exploiting the desired edge (e.g., trends) [05:55:14]. This differs from data mining that assumes no design principles, which can lead to [[overfitting_and_strategy_robustness_in_trading | overfit]] models [05:56:05]. Logic dictates constraints like "cut losses short, let profits run," which implies the need for initial and trailing stops before any statistical assessment [05:58:11]. This approach immediately eliminates the chance of [[overfitting_and_strategy_robustness_in_trading | overfitting]] from the iteration process [05:56:46].

2.  **Simple Models with Few Parameters:** Choose "loose pants models" that are less [[overfitting_and_strategy_robustness_in_trading | overoptimized]] to historic market data [05:58:21]. Simple models can capture opportunities from a greater variation in possible trend forms, especially when targeting diverse outliers [05:58:31]. More precise, complex models with many parameters tend to [[overfitting_and_strategy_robustness_in_trading | overfit]] to a specific form of signal, reducing the sample size of exploitable signals and missing alternative patterns [05:59:16]. It is preferable to "underfit" to any single trend form to capture a wider variety of trends and achieve a larger sample size [05:59:47].

3.  **Visual Mapping Process:** Instead of relying solely on statistical metrics (e.g., Sharpe ratio, CAGR), visually map the equity curve's trade outcomes against the price data's time series [01:00:52]. This allows for direct observation of how the equity curve responds to trends and noisy periods [01:01:22]. If the equity curve rises during non-trending (noisy) periods, it indicates [[overfitting_and_strategy_robustness_in_trading | overfitting]] [01:02:25]. This process, tied to the design-first logic, helps identify the least [[overfitting_and_strategy_robustness_in_trading | overfit]] models [01:03:00].

4.  **Multi-Market Testing:** Apply a single trend following model universally across a diversified portfolio of markets [01:03:50]. This increases the sample size of trades (e.g., 60 markets x 10 trades/market = 600 trades) [01:04:41]. This approach eliminates the chance of [[overfitting_and_strategy_robustness_in_trading | overfitting]] to a single market's characteristics and maximizes the chance of fitting to the characteristics of multiple markets [01:05:07]. It represents an array of alternative possible histories, enhancing robustness [01:05:52].

5.  **Using All Data:** Avoid separating data into "out-of-sample" sets for final testing [01:06:11]. Instead, use all available data for backtesting [01:06:35]. The robustness of a trend following model is less about sample size and more about its exposure to a variety of different market regimes [01:06:57]. The four principles above are used to reduce [[overfitting_and_strategy_robustness_in_trading | overfitting]] [01:07:13].

## The Complexity of Trend Following

Despite narratives suggesting trend following is "super easy" with simple entry, exit, and stop-loss rules, it is not [01:08:55]. Successfully managing significant amounts of money over decades requires complex [[research_and_model_optimization | research and model optimization]], talented people, and careful consideration of many moving parts beyond basic rules [01:09:10]. Misleading comparisons between fee-laden historical track records and fee-free simple backtests, or assumptions about low commission costs across history, fail to appreciate the true complexity and costs involved [01:10:58]. Those who call it simple often do not practice it themselves, as practitioners understand it is "not a simple exercise" [01:12:54]. However, data consistently shows that trend following is one of the most robust investment strategies [01:13:10].