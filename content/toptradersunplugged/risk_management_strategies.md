---
title: Risk management strategies
videoId: dE_v-aPvyv0
---

From: [[toptradersunplugged]] <br/> 

Risk management is a critical component of portfolio construction for investors seeking to analyze and understand the riskiness of their holdings in an increasingly uncertain global environment <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Understanding whether a portfolio is long or short volatility can be the difference between ruin and survival during a crisis <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Pricing and Risk of Loss

When evaluating a trade, it's crucial to consider the price and whether the potential reward justifies the [[risk_management_and_drawdowns | risk of loss]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. A story for why a trade is good, without considering its price component, should raise questions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

For instance, selling a put option with the idea of being a buyer of a stock at a lower price might seem appealing <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. However, if the put is sold for an infinitesimal amount, it gives up all potential upside of the stock while only having downside risk <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The key question is whether the compensation for selling the put is sufficient to justify the [[risk_management_and_drawdowns | risk of loss]] if the stock significantly declines <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

This strategy is often compared to placing a resting limit order to buy at the same price <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>. The difference is significant:
*   **Put Seller**: Faces a mark-to-market loss if the stock falls to the strike price and still has an open position <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>. They cannot buy the stock separately without adding to their exposure and potential losses <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.
*   **Resting Limit Buyer**: Buys the stock at the desired lower price without taking a loss or having a short put position, and profits if it rallies back <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>.

The option writer gives up the right to buy the stock without having lost money, a right the option buyer pays a premium for <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>. The strategy's viability depends on the premium received and the perceived probability of the price move <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>.

## Tail Risk Hedging Programs

Investment firms like QVR Advisors offer bespoke portfolios and solutions, often focusing on [[risk_management_and_drawdowns | tail risk hedging]] programs for large institutions <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. These programs aim to provide a simple, scalable way to offset [[risk_management_and_drawdowns | drawdown risk]] during significant equity market crashes <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

### Weaknesses of ETF Hedging Products

Exchange-Traded Funds (ETFs) designed for hedging often have significant weaknesses:
*   **Poor Cash Efficiency**: Many ETF products require a massive amount of treasury bonds, making them capital-intensive and forcing investors to cut their equity exposure to buy the hedge, defeating its purpose <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Optics and Sizing**: Investors are sensitive to the reported returns of an ETF, leading product managers to de-risk portfolios to look palatable. This results in the hedge not doing enough for the client's balance sheet usage, as it needs to be appropriately sized relative to the portfolio it's protecting <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Predictable Flows**: Simple, mechanical ETF products, designed for maximum transparency, become targets for front-running by dealers once they attract significant assets <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. Large, well-known, and predictable flows lead to bad performance <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

## Market Structure and Volatility

Understanding market flows and structural biases is key to effective [[risk_management_in_trading_strategies | hedging strategies]] <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>. An efficient hedge typically involves buying things that are oversold by structural sellers and potentially selling expensive things to cut the cost of carry <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.

### Evolution of Volatility Regimes
Historically, short-dated options were expensive, and strategies like covered call writing or put selling looked very good in backtests because institutional capital wasn't heavily involved <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>. However, as large asset owners adopted these strategies, the volatility term structure in the front end flattened or became steep <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. This changed the risk premium, as the market isn't large enough to absorb huge capital allocations without changing prices <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

### Jumpiness of Volatility
The structural change in volatility over the last five to seven years is not necessarily higher average volatility, but rather its "jumpiness" or bi-modality <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>. Markets can experience very low realized volatility for weeks or months, followed by a sudden transition to much higher volatility or volatility gaps <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.

This makes simplistic volatility forecasts, such as implied versus trailing realized volatility, particularly uninformative <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. Traditional volatility forecasting models become less useful <a class="yt-timestamp" data-t="00:34:09">[00:34:09]</a>.

Factors contributing to this jumpiness include:
*   **Fragile Liquidity**: Post-Dodd-Frank and Basel III, banks have de-risked, reducing their ability to warehouse and inventory risk <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.
*   **Supply of Short-Dated Options**: Heavy supply from end-users selling short-term options (e.g., call overwriting, cash-secured put selling) creates a locally stabilizing phenomenon <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>. When the market goes down, those who are long gamma (e.g., dealers, vol arbitrage hedge funds) buy stocks, and vice versa when it goes up <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.
    *   This causes lower close-to-close realized volatility when the market is within a certain range <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a>.
    *   However, the gamma profile of short-term options is very localized <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>. Once the market breaks out of this range, these stabilizing effects diminish, leading to rapid acceleration of moves and feedback effects from systematic sellers (e.g., vol control indexes, CTAs) <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>.

### Trading in Jumpy Regimes
In regimes with exaggerated moves but uncertain direction (gamma is an accelerant, not a directional bias), traders should consider:
*   **Aggressive Intraday Delta Hedging**: When expecting significant resistance to intraday rallies or sell-offs due to widespread long gamma <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.
*   **Hedging for the Close**: When in a negative gamma zone, where an initial impetus could lead to large intraday swings, hedging is often left for the close <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

The pricing of options, particularly steep skew in certain strike ranges, often reflects crowded dealer short positioning <a class="yt-timestamp" data-t="00:41:36">[00:41:36]</a>. A naive assumption that steep skew guarantees profitability can be wrong, as dealers will get squeezed, leading to increased volatility buying in that range <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>.

## Volatility Dispersion and Correlation

**Dispersion trading** (the spread between weighted average single-name components and the index) has seen increased popularity <a class="yt-timestamp" data-t="00:46:37">[00:46:37]</a>.

Recent dynamics in correlation and dispersion include:
*   **Pre-2020**: A regime of relatively low and range-bound implied spread, with not much excess single-name volatility relative to the index price. This corresponded to higher implied correlation <a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>.
*   **March 2020 and Beyond**: The COVID-19 crisis led to massive factor and sector rotation dynamics, driving incredible single-name volatility <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>. This resulted in record levels of single-name vs. implied spread <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. Retail investor participation in option trading on single names also contributed significantly <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.
*   **Current Regime**: Generally, an elevated volatility regime, not just in the index but also in single names, leading to relatively low implied correlation levels <a class="yt-timestamp" data-t="00:49:34">[00:49:34]</a>.

The notion that "in a crisis all correlations go to one" is not entirely true <a class="yt-timestamp" data-t="00:50:08">[00:50:08]</a>. Correlations are very unstable during crises, with some going up and others dropping <a class="yt-timestamp" data-t="00:50:19">[00:50:19]</a>. For example, in 2008, a market-neutral dispersion trade (short correlation) was highly profitable due to massive sector rotation <a class="yt-timestamp" data-t="00:50:26">[00:50:26]</a>.

## Relative Value Strategies

Relative value (RV) strategies involve spreading certain options against others. The sizing of positions should be relative to their risk-reward profile and expected co-movement with other positions <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>. Positions with higher basis risk between the long and short legs (and thus more P&L volatility) should be sized smaller if they have the same edge as positions with lower basis risk <a class="yt-timestamp" data-t="00:52:47">[00:52:47]</a>.

A true relative value trade involves material risk reduction in the overall hedged position compared to either leg on a standalone basis <a class="yt-timestamp" data-t="00:53:14">[00:53:14]</a>. Cross-asset class spread trades, such as long interest rate volatility versus short equity volatility, are often not true hedges as their components may not be well-correlated historically and can move in opposite directions <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>.

## Fixed Income Options Market Distortions

Similar to equities, the fixed income options market exhibits persistent distortions:
*   **Short-Term Supply**: There is a very strong supply of shorter-term options (e.g., one to three months) on Eurodollars and Treasury notes, driven by large asset managers <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>.
*   **Long-Term Swaption Ball**: The Formosa bond issuance, linked to insurance company demand, leads to a huge net supply of long-term dollar swaption volatility <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. This means long-term forward rates volatility is usually inverted at the back end of the curve, generally low, and reverts quickly after spikes <a class="yt-timestamp" data-t="00:58:25">[00:58:25]</a>.

Crowded short positioning by dealers in specific strikes and maturities can lead to steep skew in market pricing <a class="yt-timestamp" data-t="00:41:08">[00:41:08]</a>. While this might appear as a cheap selling opportunity, it implies that dealers will be squeezed, causing significant volatility buying as the price approaches that strike <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>. There is "no free lunch" in positions that are cheap and obvious, as their behavioral characteristics involve losses and limited upside due to crowded selling <a class="yt-timestamp" data-t="00:59:15">[00:59:15]</a>.

Understanding the flow patterns of large accounts and whether their trades are information-based or simply a source of supply is a useful, albeit challenging, research project for market participants <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>.