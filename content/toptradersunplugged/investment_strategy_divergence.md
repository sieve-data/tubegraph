---
title: Investment Strategy Divergence
videoId: 9_8VMOB-gzI
---

From: [[toptradersunplugged]] <br/> 

In the world of [[systematic_investment_strategies | systematic investing]], various approaches exist, leading to different interpretations and applications of core concepts like [[Trend Following Investment Strategies | trend following]]. This can result in significant [[Investment Strategies and Risks | strategy divergence]] among practitioners.

## Defining [[Trend Following Investment Strategies | Trend Following]]

Richard Brennan highlights that the definition of [[Trend Following Investment Strategies | trend following]] itself can lead to different implementation strategies <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. For instance, a selective process, where one chooses only a handful of top-performing markets based on recent performance, is distinct from a broader, more diversified approach <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Richard classifies this selective method as "cross-sectional momentum trading," which differs from his definition of [[diversification_in_investment_strategies | diversified systematic trend following]] <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Niels Kaastrup-Larsen agrees, defining [[Trend Following Investment Strategies | trend following]] as having a fixed portfolio of markets where signals are consistently calculated across all assets, relying on a high level of [[diversification_in_investment_strategies | diversification]] rather than optimization to select markets <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

## System Design and Flexibility

While a common theme in [[systematic_investment_strategies | systematic trading]] is "keeping it simple" with one entry, one stop, and one stop-loss, practitioners often incorporate "bells and whistles" <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>.

### Regime Filters
Richard often applies a regime filter in his [[Trend Following Investment Strategies | trend following]] models <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. This can involve using a long-term look-back for breakouts, ensuring that price movements are significant before an entry is considered <a class="yt-timestamp" data-t="00:51:45">[00:51:45]</a>. Filters like a 200-day simple moving average can also be used to identify suitable market regimes for breakouts <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>. The aim is to target "tail regions" of the return distribution by being selective about the types of trends to participate in <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>.

Niels cautions against over-optimizing with too many filters, which can lead to an artificially low number of losing trades and small drawdowns in backtests <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>. While one filter might be acceptable, he advises staying as close as possible to classic, simple [[Trend Following Investment Strategies | trend following]] <a class="yt-timestamp" data-t="00:53:57">[00:53:57]</a>.

### Stop-Loss Methodologies and Look-Back Periods
The choice of stop-loss methodology and position sizing is crucial <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>. While there are various trailing stop mechanisms (e.g., Donchian channel, moving average, chandelier exits), the Average True Range (ATR) based trailing stop is a popular choice <a class="yt-timestamp" data-t="00:55:20">[00:55:20]</a>. ATR is favored because it helps normalize different market structures (like cryptocurrencies, commodities, and forex), allowing the same model to be applied across diverse assets <a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>.

For longer-term [[Trend Following Investment Strategies | trend following]] systems, time-based exits (e.g., exiting if a trade isn't profitable after 'x' days) are generally not recommended <a class="yt-timestamp" data-t="00:56:48">[00:56:48]</a>. This is because [[Trend Following Investment Strategies | trend following]] focuses on capturing sustained movements, and a trend might take time to develop after an entry, making premature exits detrimental <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.

The relationship between the look-back period for entries and the distance to the stop-loss also varies <a class="yt-timestamp" data-t="00:59:16">[00:59:16]</a>. While long look-backs define entry points, the trailing stops can be a combination of different short-term, medium-term, and long-term models, rather than necessarily wide <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>. This layered approach allows for a slow entry into a trend and a measured exit <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>.

### Cross-Sectional Momentum vs. Individual Market Analysis
Richard and Niels express skepticism about cross-sectional momentum models, where markets are ranked by momentum and only the strongest are traded <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>. Niels prefers treating each market individually, sizing positions based solely on that market's strength, without reference to other markets <a class="yt-timestamp" data-t="01:02:36">[01:02:36]</a>.

Richard suggests that while cross-sectional momentum methods (like dual momentum) work for some, they differ from the mechanics of capturing "outliers" (significant, unpredictable movements) <a class="yt-timestamp" data-t="01:03:05">[01:03:05]</a>. Cross-sectional momentum assumes past strength will continue, whereas capturing outliers involves less predictive information and can occur in any liquid market <a class="yt-timestamp" data-t="01:03:48">[01:03:48]</a>. Niels adds that such strategies might lead to buying past winners, potentially missing out on the initial phase of strong momentum <a class="yt-timestamp" data-t="01:04:57">[01:04:57]</a>.

## Comparing [[Trend Following Investment Strategies | Trend Following]] Indices

The differences in [[Investment Strategies and Risks | investment strategies]] are evident when comparing various [[Trend Following Investment Strategies | trend following]] indices:

*   **SG Trend Index:** Focuses on the 10 largest [[Trend Following Investment Strategies | trend following]] CTAs (Commodity Trading Advisors) by AUM, trading primarily futures, broadly diversified, recognized as [[Trend Following Investment Strategies | trend followers]], showing significant correlation to peers, open to new investment, and reporting daily <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>. It's equally weighted and rebalanced/reconstituted annually <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>.
*   **B Top 50 Index:** Aims to track the largest investable trading advisor programs by AUM, with similar criteria to SG Trend, requiring at least three years of operating history and two years of trading activity <a class="yt-timestamp" data-t="01:08:32">[01:08:32]</a>. Despite its name, it currently only includes 20 constituents and represents the broader [[managed futures | managed futures]] industry rather than solely [[Trend Following Investment Strategies | trend followers]] <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>, <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.
*   **TTU [[Trend Following Investment Strategies | Trend Following]] Index:** Created by Niels and Richard, this index does not use size as a criterion but instead focuses on a minimum 15-year unbroken track record <a class="yt-timestamp" data-t="01:10:21">[01:10:21]</a>. Constituents must be geographically diversified, fully systematic, adopt [[Trend Following Investment Strategies | trend following]] as the dominant [[Investment Strategies and Risks | investment strategy]], be currently investable, and report monthly <a class="yt-timestamp" data-t="01:10:55">[01:10:55]</a>. It is equally weighted and rebalanced/reconstituted monthly <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>. As of April 2022, it included 60 programs <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.

The TTU [[Trend Following Investment Strategies | Trend Following]] Index demonstrates superior performance (higher compound annual growth rate and lower drawdown) compared to the SG Trend and B Top 50 indices <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This suggests that a long, validated track record is a robust risk metric, and extensive [[diversification_in_investment_strategies | diversification]] across numerous [[Trend Following Investment Strategies | trend following]] programs (each itself diversified across markets and systems) yields optimal risk-weighted returns <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>. The index's maximum drawdown since 2000 has been 18%, with an 8.57% compound annual growth rate, outperforming the S&P 500's 50% drawdown and 6.5% CAGR over the same period <a class="yt-timestamp" data-t="01:16:03">[01:16:03]</a>.

### Recent Performance (May 2022)
*   B Top 50: Up 0.48% (May), up 15% YTD <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>
*   BarclayHedge CTA Index: Down 0.10% (May), up 19.25% YTD <a class="yt-timestamp" data-t="01:19:26">[01:19:26]</a>
*   SG Trend Index: Down 0.32% (May), up 25.58% YTD <a class="yt-timestamp" data-t="01:19:35">[01:19:35]</a>
*   SG Short-Term Traders Index: Up 0.82% (May), up 9.5% YTD <a class="yt-timestamp" data-t="01:20:11">[01:20:11]</a>
*   MSCI World Index: Down 0.16% (May), down 13.64% YTD <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>
*   World Government Bonds: Down 0.71% (May), down 8.2% YTD <a class="yt-timestamp" data-t="01:20:30">[01:20:30]</a>
*   S&P 500: Flat (May) <a class="yt-timestamp" data-t="01:20:38">[01:20:38]</a>

The differences in monthly returns among these indices can be attributed to their diverse constituents and underlying strategies <a class="yt-timestamp" data-t="01:19:43">[01:19:43]</a>.