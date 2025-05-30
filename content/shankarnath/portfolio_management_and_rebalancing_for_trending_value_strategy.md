---
title: Portfolio management and rebalancing for trending value strategy
videoId: g6xanpDdVNI
---

From: [[shankarnath]] <br/> 

The [[trending_value_strategy | trending value strategy]] is an investment approach that combines both momentum and value investing principles to potentially outperform the market <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. A portfolio based on this strategy has shown significant returns, with a 25-stock portfolio delivering an annualized gain of 96.9% over approximately 11 months, compared to the Nifty 50's 30% gain in the same period <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Over 45 years (1964-2009), the strategy delivered annualized returns of 21.1%, significantly higher than the S&P 500's 9.5% <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

## Portfolio Construction Principles

The concept of trending value was introduced by James O'Shaughnessy in his book "What Works on Wall Street" <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. It consists of two key elements: "trending" (momentum) and "value" <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

### Number of Stocks

While the number of stocks in a portfolio can vary, O'Shaughnessy's backtesting experiments suggest that a 25-stock portfolio generally yields the highest risk-adjusted returns <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>. Therefore, sticking to 25 stocks is recommended <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.

### Initial Portfolio Building
The initial [[constructing_a_trending_value_stock_portfolio | construction of a trending value strategy]] involves a detailed multi-step process, leveraging tools like TickerTape for screening and data extraction <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

#### Value Score Calculation
A "value score" is calculated for companies based on six metrics <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>:
1.  **P/E Ratio**: Current market price per share divided by earnings per share (lower is better) <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
2.  **Price-to-Book Ratio**: Useful for capital-intensive businesses (lower is better) <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.
3.  **Price-to-Cash Flow from Operations**: (lower is better) <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
4.  **Price-to-Sales**: O'Shaughnessy's preferred metric (lower is better) <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.
5.  **EV/EBITDA Ratio**: Enterprise Value (market cap + net debt) divided by EBITDA (lower is better) <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
6.  **Dividend Yield**: (higher is better) <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

For each metric, companies are assigned a decile rank based on their values. For example, the lowest 184 entries for a metric (out of 1,840 companies) are allocated Decile 1, receiving 1 point <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. The cumulative value score is the sum of these decile scores across all six metrics <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>. A lower cumulative score indicates a more undervalued company <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

#### Momentum Score (Trending)
Momentum refers to stocks already showing an upward price movement, indicating market attention <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. For the [[trending_value_strategy | trending value strategy]], companies are assessed based on their stock price performance over the past six months <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.

## Portfolio Rebalancing

[[Rebalancing and switching strategies in mutual funds | Rebalancing]] is crucial for maintaining the desired characteristics of the [[trending_value_strategy | trending value strategy]] portfolio.

### Rebalancing Frequency
Ideally, portfolio rebalancing should be done on a semi-annual basis <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. For a more aggressive approach, quarterly rebalancing can also be effective <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.

### Rebalancing Process
The rebalancing process involves repeating the stock selection exercise:
1.  **Define Universe**: Start with a list of companies with a market cap of over 500 crores (or a chosen threshold) <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.
2.  **Extract Metrics**: Pull out the six value metrics (P/E, P/B, Price-to-Cash Flow from Operations, Price-to-Sales, EV/EBITDA, Dividend Yield) <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>.
3.  **Compute Value Score**: Calculate the combined value score for each company as done previously <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.
4.  **Filter by Value Decile**: Reduce the universe to only those companies within the top decile (lowest combined value scores) <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>. For 1,840 companies, this would be the top 180-190 companies with value scores ranging from 6 to 18 <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
5.  **Combine with Momentum**: Sort this truncated list in descending order based on their 6-month price returns <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.
6.  **Select Top Stocks**: Choose the top 25 stocks from this sorted list to form the [[trending_value_strategy | trending value portfolio]] <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.
7.  **Sell and Replace**: Sell underperforming stocks from the older list that have fallen out of the top decile or no longer meet the criteria <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>. Replace them with the newly identified top-ranking stocks <a class="yt-timestamp" data-t="14:39:00">[14:39:00]</a>.
8.  **Equal Weighting**: All investments should be made with equal weighting. For example, if investing 25,000 rupees, allocate 1,000 rupees per stock <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>.

## Characteristics and Considerations

### Company Type and ROC
The [[trending_value_strategy | trending value strategy]] typically identifies companies at the lower end of valuation metrics <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>. Many of these stocks also exhibit a Return on Capital Employed (ROCE) of over 18%, indicating efficient capital usage and strong profit generation <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>. This helps in avoiding "value traps" <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>.

### Volatility
One known characteristic of the [[trending_value_strategy | trending value strategy]], especially with Indian stocks, is a higher level of portfolio volatility <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>. This is primarily due to the high exposure to small-cap and micro-cap companies often identified by the strategy <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.

### Performance Validation
Studies have shown the [[trending_value_strategy | trending value strategy]] consistently outperforms broader market indices. A backtest on Indian stocks from 2007-2023 showed a CAGR of 20.6%, providing a 10% alpha over the Nifty 50's 9.9% during the same period <a class="yt-timestamp" data-t="16:19:00">[16:19:00]</a>. This outperformance was consistent across 10-year rolling returns <a class="yt-timestamp" data-t="16:56:00">[16:56:00]</a>.