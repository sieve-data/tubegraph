---
title: Tips for building effective stock screener queries
videoId: qmCFsAxVF2E
---

From: [[shankarnath]] <br/> 

A screener is a tool used to filter thousands of stocks based on specific financial metrics <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. These metrics can originate from financial statements like the balance sheet, P&L, and cash flow statements <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. They also include price-based information such as share price, return, market cap, moving averages, and RSI <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Users can filter by ratios like dividend yield, P/E multiple, book value, asset turnover, and non-standard variables such as credit rating, Proski score, and analyst recommendations <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

Popular [[stock_screening_platforms_and_financial_metrics | stock screening platforms]] mentioned include screener.in, ticker tape, trend line, and stock edge, with some even being AI-powered <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Defining Your Screening Objective

Before formulating queries, it's crucial to understand the objective and the insights you aim to extract <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. A common, but too broad, request is simply "a list of 10 multi-bagger stocks" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Instead, it's more effective to break down the objective into manageable sub-goals using a "divide and conquer" approach <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Screening for Specific Company Situations

Screeners can identify companies undergoing potentially profitable situations for investors <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Rapid Capacity Expansion
Companies that are rapidly expanding their capacity might experience increased orders and sales <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This can be identified using the gross block or net block functionality <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Query Example**: "Gross block (current year) is at least two times the preceding year" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   *Real-world example*: Sky Gold, which saw a significant jump in sales and profits after moving to a facility three times its previous size, increasing capacity <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Turnaround Stories
A turnaround occurs when a company posts two or three consecutive quarters of profits after struggling for several quarters <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   *Real-world example*: Sami Hotels, which delivered four quarters of profits after years of losses <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Efficiency Improvement
Efficiency can be measured by metrics like Return on Capital Employed (ROCE), which indicates how effectively a company generates profits from its total capital (debt and equity) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Consistent ROCE over many years (e.g., 10 years) is a positive sign <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   Operating margins (EBITDA divided by sales) also indicate efficiency; visible growth in margins is generally positive, though sectoral cyclicity should be considered <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Other Situational Variations
Screeners can also help identify:
*   Price breakouts using moving averages, RSI, and volumes <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   Changes in promoter holdings, indicating insider buying or selling <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   Analyst upgrades <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
Hundreds of variables are available within a screener <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

## Applying Investment Strategies Through Screeners

[[investment_strategies_using_stock_screeners | Investment strategies]] can be translated into screener queries.

### Growth Investing
This strategy focuses on companies with strong revenue growth, earnings growth, and business expansion <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

*   **Growth at a Reasonable Price (GARP)**: Uses a mix of revenue growth, EPS, and PEG ratio to identify potential stocks <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. A common issue with PEG ratio on most platforms is that the denominator often uses a 5-year profit growth rate instead of the expected EPS growth rate, which requires more analytical work <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Small Cap Hypergrowth**: Queries can look for sub-5,000 crore companies with high quarterly earnings growth and significant capital expenditure (CapEx) in the past year <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Earnings growth might be excluded as growing companies can be volatile <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Disruptive/Innovative Companies**: An advanced query for these companies would seek high revenue growth, R&D expenses at least 10% of sales, customer growth over 50%, recurring revenue 70% or more, high gross margins, heavy insider ownership (especially institutional), and rapidly rising market share <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Value Investing
This classical style involves buying undervalued companies with strong fundamentals <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

*   **Benjamin Graham's NCAV (Net Current Asset Value) Rule**: NCAV is current assets minus all debt <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
    *   **Query Example**: "Market cap is less than 2/3 of the net current assets" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This identifies undervalued companies as per Benjamin Graham <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   **Warren Buffett Method**: A screener query includes a mix of current asset ratio, debt ratios, return metrics (ROE, ROC), sales and earnings growth, free cash flow, and a relatively low price-to-earnings (P/E) multiple <a class="yt-timestamp" data-t="00:09:57">[00:10:05]</a>.
*   **James O'Shaughnessy's [[constructing_a_trending_value_stock_portfolio | Trending Value Strategy]]**: Uses a combination of variables like P/E ratio, price-to-book, price-to-sales, EV/EBITDA, to arrive at a combined score <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Other [[investment_strategies_using_stock_screeners | Investment strategies]]

*   **Coffee Can Portfolio**: Built using a combination of sales growth and return on capital employed <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Price Momentum**: Queries use moving averages, 52-week highs, three-month returns, volumes, and RSI to find companies with accelerating stock prices <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Earnings Momentum**: Queries use profit-related variables with some sales growth and price momentum <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Contrarian Strategy (Losers Portfolio)**: Involves a combination of falling stock prices, a low relative P/E ratio, but companies showing rising revenues and profits <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

The speaker personally uses growth strategies and situational queries focusing on year-on-year quarterly sales growth, increases in gross block, and visible changes in operating margin <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

## Key Tips for Building Effective Screener Queries

1.  **Avoid Too Many Variables**: A large number of variables often leads to unworkable results <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. Instead, select only those variables that perfectly align with your chosen strategy <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
2.  **Use a Screener as a "Screener," Not a "Picker"**: The primary function of a screener is to filter, not to select the final investment <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. Always research the companies found in the results <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
    *   **Post-Screening Research**: Conduct due diligence on both quantitative factors (order book, new products, demand, supply) <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a> and qualitative factors ([[management_analysis_for_stock_investment | management]], competitive advantages, sector tailwinds) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. Screening is just the first step; significant work is required before investing <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
3.  **Beware of False Positives**: A stock might look attractive on paper but could be a result of sector cyclicity, a value trap, or the stock price/demand/margins being at their peak, leading to downward mean reversion <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
4.  **Acknowledge Strategy Cycles**: Every strategy or query will experience good and bad periods <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. Strategies like growth, value, and momentum go through tough times <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
    *   Regularly running queries will likely show a new set of companies <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. It's crucial to rigorously examine what enters and exits your shortlist <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

There is no magical formula within a screener that will automatically provide a list of future multi-bagger stocks <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. Screening is merely the starting point, the "first gear" <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. Picking the right company from the filtered list is a more challenging skill <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. It is recommended to use a screening platform, understand its variables, start with simple queries, and always follow up with a seasoned examination of the company <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.