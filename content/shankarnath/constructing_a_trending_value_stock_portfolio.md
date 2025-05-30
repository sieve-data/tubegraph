---
title: Constructing a trending value stock portfolio
videoId: g6xanpDdVNI
---

From: [[shankarnath]] <br/> 

The [[trending_value_strategy | trending value strategy]] is an investment approach that combines the principles of both momentum and value investing to potentially achieve significant outperformance in the market <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This strategy has shown remarkable results, with a portfolio of 25 stocks delivering an annualized gain of 96.9% over 11 months, compared to the Nifty 50's 30% gain and the Midcap 150 index's 52% increase during the same period <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Historically, the [[trending_value_strategy | trending value strategy]] has outperformed market indices for over 45 years <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Origin and Core Concept

The concept of trending value was first introduced by James O'Shaughnessy in his book *What Works on Wall Street* <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The strategy has two key elements: "trending" and "value" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

*   **Trending**: This refers to momentum, identifying stocks that are already showing an upward price movement and attracting market attention <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Value**: This involves identifying fundamentally strong yet undervalued companies that the market has not yet fully recognized <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

The objective of the strategy is to maximize the potential of both momentum and value investing <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. O'Shaughnessy's backtesting over 45 years showed that while an S&P index investment yielded 11.2% annual returns, a [[construction_of_a_momentum_stocks_portfolio | momentum]]-only strategy yielded 14.5%, and buying only undervalued stocks (using his value composite 2 indicator) resulted in 17.3% <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. However, a combination of value and [[construction_of_a_momentum_stocks_portfolio | momentum]], the [[trending_value_strategy | trending value strategy]], achieved an average yearly return of 21.2% <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Constructing a Trending Value Portfolio

[[investment_strategies_using_stock_screeners | Constructing a trending value strategy]] involves several steps, primarily using a stock analysis platform like Ticker Tape, which offers tools such as a powerful screener <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### Part 1: Calculating the Value Score

The value score is a combination of six different metrics <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

1.  **Price-to-Earnings (P/E) Ratio**: Current market price per share divided by earnings per share. Lower is better <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
2.  **Price-to-Book (P/B) Ratio**: Useful for capital-intensive businesses. Lower is better <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
3.  **Price-to-Cash Flow from Operations (P/CF)**: A low number makes the business more attractive <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
4.  **Price-to-Sales (P/S)**: O'Shaughnessy's favorite metric. Lower is better <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
5.  **Enterprise Value to EBITDA (EV/EBITDA)**: Enterprise Value (market cap plus net debt) divided by EBITDA (earnings before interest, taxes, depreciation, and amortization). Lower is preferable <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
6.  **Dividend Yield**: A higher number is more favorable <a class="yt-timestamp" data-t="00:05:58">[00:06:03]</a>.

#### Steps for Calculating the Value Composite Score:

1.  **Define the Universe**: Select companies with at least 500 crores in market cap. This initially yielded about 1,860 companies, narrowing down to 1,840 after removing ETF entries <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
2.  **Extract Metrics**: Obtain the six valuation metrics using a screener's valuation filter <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
3.  **Download Information**: Export the data to a CSV or Excel sheet <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
4.  **Allocate Deciles**: For each metric, assign a decile rank to every company <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. With 1,840 entries, each decile contains 184 companies <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. For metrics where lower is better (P/E, P/B, P/CF, P/S, EV/EBITDA), the lowest 184 entries get decile 1 (1 point), the next 184 get decile 2 (2 points), and so on <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. For dividend yield, the highest values receive decile 1. Companies with negative P/E or missing data points are typically assigned decile 10 (10 points) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. A score of 1 means the company is undervalued on that parameter, while higher scores (7, 8, 9, 10) indicate it's getting more expensive <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
5.  **Replicate**: Apply the decile allocation across all five remaining variables <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
6.  **Sum Scores**: Add up the decile scores across all six metrics to get a cumulative value score for every company <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. A total of 6 is the lowest possible score (meaning undervalued on all metrics), while a score of 60 would be the highest (overvalued on all metrics) <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

### Part 2: Arriving at the Momentum Score

The momentum score identifies companies whose stock prices have performed well recently <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

1.  **Filter by Value**: Reduce the universe to only those companies that are in the top decile based on their combined value scores (e.g., companies with a value score ranging from 6 to 18) <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
2.  **Extract 6-Month Returns**: Use a screener to filter for 6-month returns under the price and volume category <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. While 6 months is used here, 3 or 4-month cycles can also be tried <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
3.  **Sort and Select**: Sort this truncated list in descending order based on the 6-month price return. The top 25 stocks from this sorted list comprise the final [[trending_value_strategy | trending value portfolio]] <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

For example, the October 2024 portfolio includes companies like Nava Limited, Nandan Den, Vedanta, Ran Holdings, Padam Paper Products, and Rattanindia Power Limited <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. These selected stocks often display a balance of value characteristics (low P/E, P/B, etc.) and strong recent momentum <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

## Implementation Considerations

When [[methods_for_analyzing_and_managing_stock_portfolios | implementing the trending value strategy]], several practical aspects should be considered:

*   **Number of Stocks**: A 25-stock portfolio generally provides the highest risk-adjusted portfolio returns, as identified through backtesting <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Rebalancing Frequency**: Instead of focusing on "when to sell," the question is "when to rebalance" <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. Ideally, this activity should occur on a semi-annual basis <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. For a more aggressive approach, quarterly rebalancing can also be effective <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   **Rebalancing Process**: The rebalancing involves repeating the entire construction process:
    1.  Pull a list of companies with market cap over 500 crores <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    2.  Extract values for the six metrics (P/E, P/B, P/CF, P/S, EV/EBITDA, dividend yield) <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
    3.  Compute the combined value score <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
    4.  Extract a subset of companies from the first deciles <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
    5.  Combine this with momentum metrics <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
    6.  Finalize a list of 25 stocks <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
    7.  Sell underperformers from the older list (stocks that have fallen out of the top decile) <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
    8.  Replace them with new top-ranking stocks <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
    9.  Ensure equal weighting across all stocks (e.g., 1,000 rupees per stock if investing 25,000 rupees) <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   **Company Characteristics**: The [[trending_value_strategy | trending value strategy]] often identifies companies at the lower end of valuation metrics <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. Many of these stocks exhibit a Return on Capital Employed (ROCE) of over 18%, indicating efficient capital use for profit generation, reducing the risk of a "value trap" <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. The strategy tends to be more of a small-cap strategy, with almost 90% of the identified stocks being small or micro-cap in terms of market capitalization <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
*   **Volatility**: While the strategy consistently shows outperformance, it may involve a higher level of portfolio volatility due to its exposure to small and micro-cap companies <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

## Performance Validation

Backtesting of the [[trending_value_strategy | trending value strategy]] on Indian stocks over a 16-year period (2007-2023) by Capital Mind showed a Compound Annual Growth Rate (CAGR) of 20.6%, significantly outperforming the Nifty 50's 9.9% CAGR during the same period, generating a 10% alpha <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. This consistent outperformance in rolling returns further validates the strategy's effectiveness across various markets globally <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.