---
title: Risk management and drawdown handling
videoId: 32S8s9CwfOQ
---

From: [[toptradersunplugged]] <br/> 

Systematic Alpha Management, co-founded by Peter Campolin, emphasizes a robust approach to [[risk_management_in_trading | risk management]] and handling [[risk_management and drawdowns | drawdowns]]. The firm's strategies are designed to navigate volatile markets while aiming for uncorrelated returns through extensive diversification and dynamic adjustments <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Investment Philosophy and General Risk

Investors should be aware of the significant [[risk_management and drawdowns | risk]] of financial loss inherent in all investment strategies. It is crucial to request and understand the specific [[risk_management and drawdowns | risks]] associated with any investment product from the investment manager before making decisions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Diversification and Trade Mechanics

The firm trades approximately 20 to 25 different markets, including major global equity indices, major currencies, and a few commodities used for hedging <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This broad market exposure is combined with diversification across strategies and timeframes:
*   **Spread Combinations**: 20 to 30 different spread combinations are traded <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Sub-Models**: Each spread is traded in up to 20 different sub-models <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Holding Times**: Models exploit short-term and longer-term mean-reverting moves within a day and a half to two days by applying different logic and rules based on varying holding periods (e.g., three hours, ten hours, or somewhat longer) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This diversification of holding time results in often uncorrelated returns between models, even for the same spread <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Intraday Seasonality**: The firm's models account for intraday seasonality of spread volatility, which is elevated during specific times like early European trading hours, late US trading hours, and around 9:30-10:00 AM New York time when significant price action and news occur <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This focus on intraday moves is crucial for strategies holding positions for hours, unlike long-term CTAs <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Total Signals**: Approximately 200 individual signals are monitored and traded <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. On average, around 20 trades are executed per day <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Most models remain in cash if no trading opportunity is detected <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

## Position Sizing and Risk Allocation

[[Risk management strategies | Position sizing]] is managed from a top-down perspective <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>:
1.  **Overall Exposure**: A maximum exposure target is set based on overall assets under management, ensuring this limit is not breached even if all models trade in the same direction <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
2.  **Geographical Regions**: Risk is broken down among three geographical regions (Asia, Europe against US, US against US/Canada) based on historical returns, expected returns, and quality of returns <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Historically, 55-70% has been allocated to European spreads, 0-10% to Asia, and the balance to North America <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This review occurs roughly every three months <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
3.  **Country-Level Risk**: Within each geographical zone, individual risk levels are assigned to each country (e.g., UK, Switzerland, France, Germany, Eurostoxx in Europe) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This is based on historical P&L, backtests, and other tools <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The firm prefers US and UK spreads due to their stability and high correlation <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
4.  **Signal-Level Allocation**: Within each country, risk is allocated among individual signals/spreads (up to 20-30 per country) using a proprietary optimizer <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This optimizer analyzes one-minute real returns over the last 4-5 years, assigning more [[risk management in trading strategies | risk]] to models that produce the best returns and are uncorrelated to others in the portfolio <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This leads to an uneven risk allocation <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Open Risk and Stop Losses
The average notional exposure for the single-leverage share class (with ~7% annualized standard deviation) is 60% long and 60% short <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This translates to an average margin-to-equity ratio of about 12% <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. Stop-loss levels are typically set around 2% from the entry price for a particular spread, not the entire portfolio <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

The worst daily P&L experienced in the last 14 years was minus 2.2% in 2008, during a period when the S&P moved 40 points in a minute <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Drawdown Management

[[Risk management and drawdowns | Drawdowns]] are a common experience for CTAs, who often spend most of their time in some form of drawdown <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Systematic Alpha Management introduced a de-leveraging mechanism in 2011 to actively manage drawdowns <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>:
*   **5% Drawdown Trigger**: If an intra-month drawdown reaches 5% (peak to trough), the firm starts reducing [[risk management in trading | risk]] by 25% <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This initial de-leveraging is applied to the specific markets or spreads causing the drawdown <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **7.5% Drawdown Trigger**: If the portfolio-level drawdown reaches 7.5%, de-leveraging increases to 50% across all spreads, not just the losing ones <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.
*   **Purpose**: This mechanism helps control the depth of the drawdown by trading less [[risk_management_in_systematic_trading | risk]], especially during "Black Swan" events that are difficult to predict <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Re-leveraging**: The firm does not wait for months to re-establish [[risk management techniques in trading | risk]]. If recovery is observed, they slowly put [[risk management techniques in trading | risk]] back on, with the expectation of a full recovery <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. This re-leveraging process is more "art than science," involving analysis of which countries and spreads are behaving normally and generating positive returns <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

### The 2011 Drawdown Experience
In 2011, the firm experienced a peak drawdown of 19%, although they ended the year at minus 11% due to a strong recovery in the fourth quarter <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This was a critical learning experience:
*   **Sense of Invincibility**: After successfully navigating the 2008 market environment where VIX went to 90 (an out-of-sample environment), the firm had a "sense of invincibility" regarding their models <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   **European Debt Crisis**: The European Debt Crisis introduced a new, unforeseen risk factor—credit defaults—which the models were not designed to prevent <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
*   **Realization and Adjustment**: Initially, the drawdown was seen as a temporary bad streak, but after 2-3 months, it became clear it was "something totally different" <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. It took about two months to develop and implement modifications and de-leveraging rules, which were introduced in early September 2011 <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.
*   **Lessons Learned**: The 2011 experience made the firm stronger and a "better manager," despite having fewer assets under management <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. This highlights the importance of how managers react to and learn from difficult times <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>.

## Research and Model Robustness

The firm focuses on ensuring model robustness to avoid over-optimization, a common criticism of quantitative strategies <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>:
*   **Out-of-Sample Testing**: Parameters are estimated not just on in-sample data but through walk-forward out-of-sample tests and scenarios <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.
*   **Mean Reversion**: They continually monitor statistical tests for mean reversion, which is the core of their strategy <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. They assess how these tests change over various timeframes (e.g., 10 years, 3 years, 6 months) <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>. Any deterioration in mean reversion tests can lead to de-leveraging allocation to a particular country <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.
*   **Dynamic Hedge Ratios**: Hedge ratios are recalculated daily to reflect the most recent relationships between markets <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. If these ratios change rapidly, it indicates a breakdown in correlation, prompting a potential exit from that market <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>. For example, they stopped trading the Nikkei-Japanese Yen-S&P relationship when its correlation to the rest of the world disappeared after new Japanese economic policies <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>.
*   **Data-Driven Decisions**: The firm prioritizes data over fundamental analysis. If data indicates a change, they act on it first and then seek fundamental explanations, rather than the other way around <a class="yt-timestamp" data-t="00:36:11">[00:36:11]</a>.

## Managing Investor Expectations

The biggest challenge as a business owner and manager is convincing clients of the benefit of their uncorrelated strategy, especially during [[risk_management and drawdowns | drawdowns]] when other managers might be doing well <a class="yt-timestamp" data-t="00:39:50">[00:39:50]</a>. Investors often appreciate uncorrelated returns when the firm makes money and others lose, but dislike it when the firm is flat or negative while others are profiting <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>.

During a drawdown, it's natural for investors to doubt the strategy <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>. However, the firm maintains a strong belief in its ability to recover and perform again due to its inside knowledge and understanding of its approach <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>. The best time to invest with a manager who has a long track record and has shown an ability to improve and recover is often during a drawdown <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.

## Biggest Failure

Peter Campolin considers the firm's biggest failure to be their inability to hold assets during the 2011 drawdown <a class="yt-timestamp" data-t="00:54:44">[00:54:44]</a>. In retrospect, they should have intervened earlier by reducing [[risk management techniques in trading | risk]] and been more proactive in communicating with clients <a class="yt-timestamp" data-t="00:54:54">[00:54:54]</a>. However, the subsequent changes and improvements implemented made the firm stronger, despite the asset outflows <a class="yt-timestamp" data-t="00:55:37">[00:55:37]</a>.