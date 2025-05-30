---
title: Mean reversion vs trend following strategies
videoId: pVE8sehGzCQ
---

From: [[toptradersunplugged]] <br/> 

Systematic investing often involves exploring different strategies, with [[trend_following_strategies | trend following strategies]] and [[mean_reversion_trading_strategy | mean reversion strategies]] being two prominent approaches. While they are often seen as opposites, they can also complement each other within a diversified portfolio <a class="yt-timestamp" data-t="02:19:58">[02:19:58]</a>.

## Trend Following Strategies

[[trend_following_strategies | Trend following strategies]] capitalize on sustained market movements, assuming that if a price went up last month, it's more likely to go up this month <a class="yt-timestamp" data-t="02:29:27">[02:29:27]</a>. They generally do their own risk management; instead of explicit stop-losses, positions are typically closed when the trend reverses <a class="yt-timestamp" data-t="03:09:07">[03:09:07]</a>.

Historically, [[trend_following_strategies | trend following strategies]] have shown a "sweet spot" for performance around a holding period of approximately one month <a class="yt-timestamp" data-t="02:55:56">[02:55:56]</a>. Performance tends to degrade when going faster than this, especially considering trading costs <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>.

## Mean Reversion Strategies

[[mean_reversion_trading_strategy | Mean reversion strategies]] operate on the principle that prices will eventually revert to their historical average or equilibrium. They often involve "buying fear and selling greed," or short-term tactics <a class="yt-timestamp" data-t="02:35:10">[02:35:10]</a>.

### Types of Mean Reversion

*   **Relative Value Trading**: This involves trading the relationship between two assets that are typically mean-reverting. An example is trading "butterflies" on the yield curve (e.g., 2, 5, and 10-year points), where the relationship between them tends to revert to a mean <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>.
*   **Slow Value Trade**: This is a classic long-term mean reversion approach, where one might buy when a price is significantly below its five-year average (adjusted for volatility) and sell when it's significantly above <a class="yt-timestamp" data-t="02:34:32">[02:34:32]</a>.
*   **Short-term Mean Reversion**: This involves very fast trading horizons, potentially as short as one to two hours or a few days <a class="yt-timestamp" data-t="02:59:22">[02:59:22]</a>. Autocorrelation of futures returns can be strongly negative at these very short horizons, indicating potential for mean reversion <a class="yt-timestamp" data-t="02:59:41">[02:59:41]</a>.

### Challenges of Mean Reversion

*   **Expected Returns**: Slow mean reversion strategies tend to have lower expected returns, possibly a Sharpe ratio of 0.2 compared to 1.0 for a diversified [[trend_following_strategies | trend following]] futures portfolio <a class="yt-timestamp" data-t="02:56:01">[02:56:01]</a>. Such low Sharpe ratios can be statistically insignificant <a class="yt-timestamp" data-t="02:58:11">[02:58:11]</a>.
*   **Risk Management**: Unlike [[trend_following_strategies | trend following]], mean reversion strategies don't inherently manage risk. If a trade moves against the position, the strategy might suggest buying more, which can lead to significant losses if the market continues to move away from the expected mean <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. Explicit stop-losses are often needed, which introduces calibration challenges and complexity in reopening trades <a class="yt-timestamp" data-t="03:40:48">[03:40:48]</a>.
*   **Costs**: Faster mean reversion strategies incur significantly higher trading costs due to increased frequency and the need for aggressive execution (crossing the bid-ask spread) <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. This often limits the universe of tradeable instruments to those with cheaper trading costs, such as equity indices, reducing diversification benefits <a class="yt-timestamp" data-t="02:49:50">[02:49:50]</a>.
*   **Diversification**: The need to manage costs often means mean reversion portfolios cannot be as diversified as [[trend_following_strategies | trend following]] ones, as they might be limited to a smaller number of markets <a class="yt-timestamp" data-t="02:47:50">[02:47:50]</a>.

## Complementary Strategies

While at the same timeframe, a flipped [[trend_following_strategies | trend following]] signal would be perfectly negatively correlated with a mean reversion signal, it would also likely lose money in a backtest if the original [[trend_following_strategies | trend following strategy]] was profitable <a class="yt-timestamp" data-t="02:22:15">[02:22:15]</a>. Therefore, effective mean reversion strategies should target scenarios where [[trend_following_strategies | trend following strategies]] are less effective, such as different time frequencies <a class="yt-timestamp" data-t="02:28:30">[02:28:30]</a>.

One promising application of very short-term mean reversion signals is as an **overlay to execution** for slower systems <a class="yt-timestamp" data-t="03:32:56">[03:32:56]</a>. For example, a daily [[trend_following_strategies | trend following system]] that wants to sell might only execute if the price movement aligns with a short-term mean reversion system, thus reducing costs without actively trading the high-frequency strategy <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

A diversified portfolio can include a mix of strategies. An example given is a portfolio that is roughly 60% [[trend_following_strategies | trend following]] and 40% other signals (which may include elements of mean reversion or value), which helps smooth out overall performance, especially in years when [[trend_following_strategies | trend following]] alone struggles <a class="yt-timestamp" data-t="02:11:02">[02:11:02]</a>. Even with small allocations, long-term value indicators can provide negative correlation benefits despite being weak signals and difficult to risk manage <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

## Overfitting and Robustness

Developing systematic strategies requires guarding against overfitting, which means assuming the future will be too much like the past <a class="yt-timestamp" data-t="04:06:01">[04:06:01]</a>. An example of overfitting is adding overly specific, complex conditions to a strategy based on past data to achieve an unrealistically high in-sample performance <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. The goal is to maximize out-of-sample performance, not just backtested results <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

One technique to detect overfitting and measure robustness is to evaluate strategy performance across different sub-samples of historical data, or using **bootstrapping** or **block bootstrapping** to create alternative histories <a class="yt-timestamp" data-t="04:48:48">[04:48:48]</a>. A robust strategy will perform well across many different alternative histories, rather than being overly dependent on the exact historical sequence <a class="yt-timestamp" data-t="04:49:10">[04:49:10]</a>. This also assesses whether the strategy is robust to changing market conditions <a class="yt-timestamp" data-t="04:52:40">[04:52:40]</a>. As a general rule of thumb, running hundreds of backtests to perfect a strategy almost certainly indicates overfitting <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.