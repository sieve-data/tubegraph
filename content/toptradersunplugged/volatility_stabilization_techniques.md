---
title: Volatility Stabilization Techniques
videoId: 6myigI5buI4
---

From: [[toptradersunplugged]] <br/> 

[[Volatility stabilization]] is a key concept in systematic investing, aiming to manage risk by maintaining a targeted level of portfolio [[volatility_in_trading_strategies | volatility]] <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This approach was notably refined through the collaboration between Perry Kaufman and Moritz Seibert, with Seibert credited for a significant improvement in Kaufman's work over the past 15 years <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## Core Mechanism

The primary idea behind [[volatility stabilization]] is to target a specific, acceptable [[volatility_in_trading_strategies | volatility]] level for a portfolio <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. The industry standard target is often around 12% <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

The process involves:
1.  **Calculating Portfolio Volatility:** This is typically done by taking the last 20, 30, or 40 days of program returns, expressed as percentages, and calculating their annualized [[volatility_in_trading_strategies | volatility]] <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  **Adjusting Position Size:**
    *   If the portfolio's [[volatility_in_trading_strategies | volatility]] goes above the target (e.g., 12%), the position size is cut to bring it back down <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
    *   If the [[volatility_in_trading_strategies | volatility]] falls below the target, leverage is increased to raise it <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
    *   These adjustments are not made daily; for instance, Perry Kaufman only changes the [[volatility_in_trading_strategies | volatility]] of the portfolio if it moves by 20% from the target (e.g., 12% to 14.4%) <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

This adjustment is generally easier to implement in futures markets than in stocks <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Benefits of Volatility Stabilization

*   **Improved Performance:** The surprising outcome of [[volatility stabilization]] is that most of the improvement comes from *raising* portfolio [[volatility_in_trading_strategies | volatility]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. During periods of low [[volatility_in_trading_strategies | volatility]] in a trend following system, returns can be significantly reduced (e.g., by almost 50%) if positions aren't increased to bring [[volatility_in_trading_strategies | volatility]] back to target <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This ensures that the real performance matches the theoretical expectation in the long run <a class="yt-timestamp" data-t="01:22:21">[01:22:21]</a>.
*   **Enhanced Risk-to-Return Ratio:** When [[volatility_in_trading_strategies | volatility]] is high, and positions are reduced, it not only locks in profits but also improves the return-to-risk ratio <a class="yt-timestamp" data-t="01:12:29">[01:12:29]</a>.
*   **Smoothed Performance:** Utilizing multiple parameters in a system, such as different calculation speeds, helps smooth out performance and makes expected returns more realistic <a class="yt-timestamp" data-t="01:22:15">[01:22:15]</a>.
*   **Risk Management:** It's critical for controlling risk in trading <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>. Traders don't control returns, but they can control risk <a class="yt-timestamp" data-t="01:03:02">[01:03:02]</a>. [[Volatility targeting in trend following | Volatility targeting]] is considered a method of thinking about risk management <a class="yt-timestamp" data-t="01:13:10">[01:13:10]</a>.

## Critiques and Alternative Perspectives

While impactful, strict [[volatility targeting in trend following | volatility targeting]] isn't universally adopted. Moritz Seibert, for example, stepped away from a rigid [[volatility_in_trading_strategies | volatility]] control process for several reasons:

*   **Cost Savings:** Accepting a more dynamic [[volatility_in_trading_strategies | volatility]] (e.g., fluctuating between 12% and 20%) reduces the need for frequent [[Volatility and market mechanics | volatility adjustment]] trades, which saves on commissions, exchange fees, clearing fees, bid-ask spread, and potential slippage <a class="yt-timestamp" data-t="01:13:13">[01:13:13]</a>.
*   **Impact on Average Loss:** Seibert observed that these [[volatility_in_trading_strategies | volatility]] control trades, when separated from core system trades, increased his average loss <a class="yt-timestamp" data-t="01:14:37">[01:14:37]</a>.
*   **Skewed Exposure:** Much of the additional performance from dynamic leveraging in the past was solely due to leveraging the fixed income complex of the portfolio, leading to a skewed exposure that Seibert wished to avoid <a class="yt-timestamp" data-t="01:14:41">[01:14:41]</a>.
*   **Philosophical Choice:** Risk management and position sizing are personal choices <a class="yt-timestamp" data-t="01:15:11">[01:15:11]</a>. Traders must be comfortable with their system's [[Volatility and Market Dynamics | volatility dynamics]] to stick with it long-term and avoid prematurely abandoning a strategy during difficult periods <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>.

Ultimately, whether to implement rigid [[volatility stabilization]] is a decision based on a trader's comfort level with [[volatility_in_trading_strategies | volatility]] fluctuations and their specific [[investment_strategies_for_volatility | investment strategies for volatility]] <a class="yt-timestamp" data-t="01:15:11">[01:15:11]</a>.