---
title: Risk management and drawdowns
videoId: RQER5heyq2M
---

From: [[toptradersunplugged]] <br/> 
The following article is based on a discussion from the Systematic Investor Series featuring Niels Kaastrup-Larsen and Jerry Parker.


[[risk_management_and_drawdown_handling | Risk management and drawdown handling]] are crucial aspects of systematic investing, particularly within the realm of trend following. The discussions presented here explore various facets of [[risk_management_in_trading | risk management]], from defining trade risk to managing market exposure and evaluating performance metrics.

## Defining Risk in Systematic Trading

In systematic trading, defining risk is fundamental. According to Jerry Parker, a core principle involves allocating a "unit" of risk per market and then dividing that unit across multiple independent systems <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. For example, a single market's risk might be split into four systems, each taking a quarter of a unit <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Pyramiding Misconception
The term "pyramiding" is often misunderstood in systematic trend following. It's not about increasing risk based on open profit <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. Instead, the systems operate independently, each with its own entry and exit rules. While multiple breakouts (e.g., 20-day, 40-day, 60-day, 80-day) might occur on the same day for a single market, they are treated as distinct trades with predefined risk <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Minor attempts to micromanage trades, such as spreading entries for a small profit, have actually been shown to underperform the simple, systematic approach <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

## Diversification and Risk Control

Diversification is a cornerstone of effective [[risk_management_strategies | risk management]] in systematic investing.

### Single Stocks vs. Indices
While single stocks can be used, a diversified portfolio often handles risk better. For instance, in January 2020, a portfolio diversified across all stocks, currencies, commodities, and bonds saw everything go down simultaneously <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. However, in other periods, a mixed bag of long and short single stocks, along with short indices (like country ETFs), can offer better [[risk_management_in_trading | risk control]] and diversification than focusing solely on indices <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

### Multi-Market Approach
Applying the exact same four breakout systems across every liquid market is generally considered optimal for long-term trend following due to the need for a requisite sample size <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. There isn't enough historical data to customize parameters for individual markets like crypto <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
Richard Dennis suggested an "in-sample and out-of-sample" test, where parameters are optimized for an initial period and then applied to subsequent data to see if they remain consistent <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. His contention was that global, non-optimized parameters tend to be more robust for the future <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

Niels suggests that while generally keeping rules simple and universal is best <a class="yt-timestamp" data-t="00:28:25">[00:28:25]</a>, a nuanced approach could involve:
1.  Using universal parameter settings for a portion of the risk budget <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.
2.  Optimizing parameters based on sectors (e.g., metals vs. softs) for another portion <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.
3.  Applying individual market optimization for a very small, cautious part of the total risk budget <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

However, Jerry counters that these variations can compromise the system's robustness, emphasizing that diversification should not come at the cost of fundamentally sound and positively skewed strategies <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>. He stresses that "it has to be very close to being robust and safe and positively skewed" <a class="yt-timestamp" data-t="00:31:03">[00:31:03]</a>.

### Managing Extreme Outliers
When faced with extreme market movements, like a 95% drop in a single day (e.g., Luna crypto), the question arises whether to manually close a position or let the system run <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.
*   Systematic traders typically define risk using Average True Range (ATR) based on daily volatility, not dollar value <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>.
*   Historically, large short trades don't necessarily show a consistent pattern of volatility decreasing <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.
*   Shorts provide diversification, especially when other markets are not trending <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>.
*   Over-analyzing shorts or creating special rules for every situation is generally counterproductive; a simple "one entry, one exit, a stop loss" rule for all markets is preferred <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a>.

However, in extremely rare, outlier situations (e.g., a 500 ATR profit), a discretionary decision to take some profit or exit a position can be more robust than rigid, non-robust rules applied daily <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>. Jerry cites his experience with the Russian stock ETF, where he exited a short position manually when it was near zero, realizing the risk/reward of staying in was unfavorable <a class="yt-timestamp" data-t="00:40:21">[00:40:21]</a>.

## Consistency vs. Outliers

A perceived paradox in trend following is the desire for consistency while aiming to capture infrequent, large outliers.
*   Long-term classical trend following, when implemented without trying to smooth returns, can achieve higher consistency <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.
*   Attempts to manage "smoothness" through [[risk_management_techniques_in_trading | volatility management]] or correlation management often lead to smaller profits and increased volatility, sacrificing consistency <a class="yt-timestamp" data-t="00:56:18">[00:56:18]</a>.
*   Jerry's firm, Chesapeake, experienced 13 consecutive winning years with simpler systems initially <a class="yt-timestamp" data-t="00:56:54">[00:56:54]</a>. A recent backtest from 1977 showed no losing years, though some winning years were minimal <a class="yt-timestamp" data-t="00:57:11">[00:57:11]</a>.
*   This consistency is an accidental byproduct of not trying to smooth returns, and of focusing on one entry, one exit, and a stop loss, allowing outliers to run <a class="yt-timestamp" data-t="00:58:09">[00:58:09]</a>.
*   The inherent "lumpiness" of returns in trend following, with periods of no money followed by large gains, is a consistent *profile* <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>.

### Critique of Traditional Risk Metrics
Metrics like the Sharpe ratio are often used to evaluate performance, but they may not fully capture the essence of [[risk_management_in_systematic_trading | risk management]] in trend following.
*   The Sharpe ratio, a portfolio tool, primarily measures return over volatility, not the actual [[risk_management_in_trading | risk of loss]] or capital preservation <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>.
*   For trend following, allowing outliers to run to their full potential, which can lead to "lumpiness" and higher volatility, actually maximizes compounded annual growth rate and demonstrates robustness <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. A low Sharpe ratio might even indicate this robust approach <a class="yt-timestamp" data-t="01:05:14">[01:05:14]</a>.
*   Famous long-term investments like the S&P 500 or Warren Buffett's performance are rarely analyzed by Sharpe ratio or biggest drawdowns; instead, their long-term staying power is celebrated <a class="yt-timestamp" data-t="01:05:31">[01:05:31]</a>.

### Philosophical Stance on Risk
The philosophy underpinning [[risk_management_in_systematic_trading | risk management]] is crucial.
*   The most significant "no-no" is attempting trend following on a limited number of markets, as diversification across many markets is a "secret sauce" <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>.
*   Overcomplicating trend following is also detrimental; simplicity often leads to long-term success <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>.
*   The power of outliers is so immense that they can "overwhelm that negativity" from drawdowns, meaning they generate enough profit to compensate for periods of loss <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>.
*   Diluting the "core" principle of letting profits run by implementing [[risk_management_strategies | volatility management]] or taking profits prematurely can be detrimental to the long-term compounding effect <a class="yt-timestamp" data-t="01:19:27">[01:19:27]</a>.
*   While some in the industry embrace complexity and "volatility management," classic trend following remains committed to allowing outliers to drive returns, recognizing that this approach provides longevity and superior long-term performance <a class="yt-timestamp" data-t="01:14:15">[01:14:15]</a>. The choice is often between easier short-term management and maximizing long-term returns by enduring inherent volatility <a class="yt-timestamp" data-t="01:16:08">[01:16:08]</a>.

## Succession and Business Continuity in Investment Firms

The long-term viability and [[risk_management_in_investment_firms | risk management]] of a CTA or managed futures firm also involve succession planning and business structure. Unlike many traditional businesses, CTA firms rarely see ownership passed on, with founders often remaining at the helm <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>.

Some firms have successfully transitioned, like Dunn Capital, where Bill Dunn passed ownership to Marty Bergen after a 10-year transition period <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>. This allowed the firm to retain its DNA and intellectual property.

Jerry suggests that larger firms, like AHL, have established sustainable businesses by focusing on proper investments, personnel, and infrastructure from the outset, making succession planning a normal part of their operation <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>. Transitioning from a founder-dominated structure to a more collaborative, corporate model with diverse talent can strengthen an organization and allow it to withstand periods when trading performance might not be "great" <a class="yt-timestamp" data-t="00:51:42">[00:51:42]</a>. Historically, CTA firms bought by large organizations like banks have not often been successful, possibly due to the inherent "quirkiness" and distinct nature of trend following firms compared to corporate shops <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.