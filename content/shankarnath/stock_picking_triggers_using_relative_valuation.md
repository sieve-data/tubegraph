---
title: Stock picking triggers using relative valuation
videoId: ppxnjQ86T-Q
---

From: [[shankarnath]] <br/> 

Investing in a blend of large-cap and small-cap indices can yield significantly higher returns than investing in either category in isolation. Since 2007, a monthly investment in a large-cap index would have returned 12.8%, while a small-cap index would have returned 13.8% <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. However, combining these two indices could potentially deliver a return of 16.3% <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, aiming for an extra two to three percent on capital <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This article explores how to achieve this through [[relative_valuation_and_price_earning_multiples | relative valuation]] as a [[stock_selection_criteria_inspired_by_peter_lynch | stock picking trigger]].

## The Role of Relative Valuation

External events and their perception heavily influence investor interest, causing shifts between large-cap and small-cap preferences over time <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. For instance, investors who favored large caps during uncertain periods (2009, 2013, 2020) were often the same individuals who predominantly invested in small caps in different years (2007, 2017) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This dynamic highlights why a [[relative_valuation_and_price_earning_multiples | relative valuation]] range of 0.9 to 1.1 becomes a crucial [[valuation_metrics_in_stock_selection | stock picking trigger]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Data Collection for Analysis

To develop an investment model based on [[relative_valuation_and_price_earning_multiples | relative valuation]], the first step is to collect month-closing values for the Nifty 50 and Nifty Small Cap 250 indices <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This data can be obtained from the NSC India website by navigating to "products," then "equities," and clicking on "historical index data" <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. From there, select "total returns index value" and specify the desired time period <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. While the daily values displayed require conversion to monthly figures, a Google Sheet compiling monthly Nifty 50 and Small Cap 250 closing values for the past 15 years is available via a link in the video's description <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This sheet also contains the various investment scenarios discussed below <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Investment Scenarios

Using the compiled data, several investment scenarios can be analyzed to understand the impact of different strategies on returns.

### Scenario 1: Individual Index Performance

Investing a 10,000 rupee monthly SIP (Systematic Investment Plan) over 15 years would have resulted in:
*   **Nifty 50 TRI:** An annualized return of 12.8%, growing the investment to 55.5 lakhs <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Nifty Small Cap 250 TRI:** A CAGR of 13.8%, growing the investment to a little over 60 lakhs <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### Scenario 2: Pausing SIPs in Overvalued Periods

This [[methodology_for_identifying_undervalued_and_high_momentum_stocks | methodology for identifying undervalued and high momentum stocks]] involves setting a guard rail: if the [[relative_valuation_and_price_earning_multiples | relative valuation]] of small caps to large caps exceeds 1.1 (indicating small caps are overvalued) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, SIPs in small caps are paused. Over the 15-year period, this meant pausing investments for 23 months <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This exclusion led to a slight improvement, with annualized returns of 14.1% <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Scenario 3: Selling When Overvalued

Beyond pausing SIPs, a more proactive [[valuation_indicators_and_selling_strategies | selling strategy]] is to redeem (sell) units when small caps become expensive. By selling 10,000 rupees worth of units every time the small cap level crosses 1.1, the annual return could increase to 14.4% <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Scenario 4: Buy Low, Sell High (Tiered Approach)

This advanced [[methodology_for_identifying_undervalued_and_high_momentum_stocks | methodology for identifying undervalued and high momentum stocks]] not only sells when small caps are expensive but also strategically buys when they are relatively cheaper. The strategy involves a tiered approach for both selling and buying based on [[relative_valuation_and_price_earning_multiples | relative valuation]]:

*   **Selling (When Small Caps are Expensive):**
    *   Crosses 1.1: Sell 10,000 rupees <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
    *   Crosses 1.15: Sell an additional 10,000 (total 20,000 rupees) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   Crosses 1.2: Sell a total of 30,000 rupees <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

*   **Buying (When Small Caps are Cheaper):**
    *   Goes below 0.9: Invest an additional 10,000 rupees <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   Goes below 0.85: Invest an additional 20,000 rupees <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   Goes below 0.8: Invest an additional 30,000 rupees <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

These additional investments are *over and above* the regular 10,000 rupee monthly SIP <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This strategy, which defines both the action and the quantum of investment/redemption based on [[relative_valuation_and_price_earning_multiples | relative valuation]], delivered an impressive 16.3% annual return <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

> [!success] Significant Improvement
> This "Buy Low, Sell High" strategy resulted in a significant jump in annual returns to 16.3% from the initial 12.8% (Nifty 50) and 13.8% (Small Cap 250) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Scenario 5: Long-Short Opportunity (Selling Small Caps to Buy Large Caps)

A further refinement of this [[constructing_a_trending_value_stock_portfolio | constructing a trending value stock portfolio]] is to leverage the relationship between small and large caps. If small caps are relatively inexpensive, it implies that large caps are also relatively cheap at those same points <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This opens up a "long-short" opportunity: use the money redeemed from selling small cap units when they are overvalued to buy units in a Nifty 50 Index Fund when large caps are comparatively cheaper <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This [[relative_valuation_and_price_earning_multiples | relative valuation]] driven approach not only helps achieve a respectable return of 16% over 15 years but also aids in accumulating a larger portfolio corpus by remaining generally invested in the market <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

## Additional Considerations

While the returns are compelling, certain practicalities must be considered when [[improving_stock_and_mutual_fund_selection | improving stock and mutual fund selection]]:

*   **Taxes:** Capital gains taxes are unavoidable <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. However, given that a larger portion of gains will likely be long-term and the typical 5% difference between short-term capital gains (STCG) and long-term capital gains (LTCG) may not be a major concern for investors <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Liquidity:** The strategy requires additional funds (10,000, 20,000, 30,000 rupees) for investment when small caps are cheap <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. If these funds are not readily available, some "slippages" in execution may occur <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Conclusion

The analysis of these five scenarios demonstrates that while individual large-cap and small-cap investments offer decent returns, a tactical approach using [[relative_valuation_and_price_earning_multiples | relative valuation]] can significantly enhance performance <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Small-cap investing is inherently more tactical than large-cap or mid-cap investing <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. By advocating for SIPs even in small caps and fully leveraging their volatility through a "Buy Low, Sell High" strategy, investors can maximize returns <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This systematic application of [[significance_of_valuation_in_stock_investments | significance of valuation in stock investments]] and [[evaluating_stock_market_metrics_for_investment_decisions | evaluating stock market metrics for investment decisions]] provides a robust framework for [[improving_stock_and_mutual_fund_selection | improving stock and mutual fund selection]].