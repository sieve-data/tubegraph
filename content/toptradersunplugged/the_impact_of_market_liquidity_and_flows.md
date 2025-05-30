---
title: The impact of market liquidity and flows
videoId: dE_v-aPvyv0
---

From: [[toptradersunplugged]] <br/> 

Understanding [[execution_and_liquidity_in_financial_markets | market liquidity]] and the underlying flows of capital is crucial for investors, as these factors significantly influence asset pricing, volatility, and the effectiveness of trading strategies <a class="yt-timestamp" data-t="00:00:08"></a>. Rather than focusing solely on a "good story" for a trade, it's essential to consider the price and the associated risk premium <a class="yt-timestamp" data-t="00:00:08"></a>.

## Structural Flows and Pricing in Derivatives Markets

In derivatives markets, an asset is often cheap or expensive because of **structural selling or buying** without regard for price <a class="yt-timestamp" data-t="00:21:11"></a>. Recognizing these underlying flow patterns provides valuable insights into market dynamics.

### Equity Index Options

*   **Short-Term Options (e.g., 2-week, 1-month):** There is a very heavy oversupply of short-term options, driven by extensive selling of puts and calls for overwriting, underwriting, or rebalancing programs pitched to pension funds and retail investors (income style programs) <a class="yt-timestamp" data-t="00:21:33"></a>. Consequently, there are very few natural buyers on a systematic basis for these options <a class="yt-timestamp" data-t="00:21:49"></a>. This constant supply helps explain why short-term volatility in the S&P 500 can be as low as 10% or sub-10%, compared to 15% historically, and why the term structure is often very steep <a class="yt-timestamp" data-t="00:25:29"></a>.
*   **Long-Term Options (e.g., 18 months, 2-3 years):** Heavy supply originates from retail structured product businesses <a class="yt-timestamp" data-t="00:22:04"></a>. Retail investors generate yield by selling long-term crash risk in equity indices (e.g., notes with coupons that cease if the S&P drops significantly) <a class="yt-timestamp" data-t="00:22:25"></a>. Banks issuing these products immediately hedge by selling large baskets of out-of-the-money puts, leading to heavy supply at the back end of the curve <a class="yt-timestamp" data-t="00:22:51"></a>.
*   **Mid-Term Options (Belly of the Curve):** The post-COVID environment has seen increased client option demand for hedging and shaping beta views, primarily in the 3-month, 6-month, and 9-month maturities, where liquidity is perceived to be reasonable without constant position rolling <a class="yt-timestamp" data-t="00:23:03"></a>.

### Fixed Income Options

Similar structural flows are observed in fixed income options markets:

*   **Shorter-Term Options:** There's significant supply of shorter-term options (1-3 months) on Eurodollars, Treasury notes, and Treasury bonds, often from very large asset managers <a class="yt-timestamp" data-t="00:57:37"></a>.
*   **Longer-Term Swaption Volatility:** Long-term forward rates volatility is typically inverted at the back end of the curve due to heavy supply from callable bond issuance in Taiwan (Formosa bond issuance), linked to insurance company demand <a class="yt-timestamp" data-t="00:58:00"></a>. This often results in mildly positive carry and tends to be low, spiking during crises but reverting quickly due to supply <a class="yt-timestamp" data-t="00:58:30"></a>.

## [[impact_of_liquidity_on_global_financial_markets | Market Liquidity]] and Volatility Regimes

The nature of [[impact_of_liquidity_on_global_financial_markets | market liquidity]] has changed, contributing to a "jumpy" or bi-modal volatility regime <a class="yt-timestamp" data-t="00:32:35"></a>.

*   **Fragile Liquidity:** [[impact_of_liquidity_on_global_financial_markets | Liquidity conditions]] are much more fragile locally, partly due to the de-risking of banks following regulations like Dodd-Frank and Basel III, which reduced their ability to warehouse and inventory risk <a class="yt-timestamp" data-t="00:35:05"></a>.
*   **Gamma Effect:** Heavy supply of short-dated options from end-users, like call overwriting or cash-secured put selling, creates a **locally stabilizing phenomenon** <a class="yt-timestamp" data-t="00:35:31"></a>. Dealers and volatility arbitrage hedge funds, who often take the other side, become "long gamma" <a class="yt-timestamp" data-t="00:36:26"></a>. This means they are forced to buy stocks when the market goes down and sell when it goes up, dampening close-to-close realized volatility when the market stays within its recent range <a class="yt-timestamp" data-t="00:36:26"></a>.
*   **Jumps and Amplification:** However, the gamma profile of short-term options is very localized <a class="yt-timestamp" data-t="00:36:51"></a>. Once the market breaks out of this range, it moves away from this stabilizing gamma <a class="yt-timestamp" data-t="00:37:03"></a>. This can lead to rapid transitions to much higher volatility or volatility gaps, particularly when combined with feedback effects from systematic sellers (e.g., vol control indexes, CTAs) <a class="yt-timestamp" data-t="00:32:46"></a>. This creates a market where periods of quiet can quickly transition to turbulence when the stabilizing gamma is overcome <a class="yt-timestamp" data-t="00:39:52"></a>.
*   **VIX Spikes in Low Liquidity:** Recent VIX spikes, even with relatively small S&P drawdowns, have been attributed to rapid de-risking by equity investors who buy short-dated puts into low-liquidity environments, especially near year-end <a class="yt-timestamp" data-t="00:43:59"></a>. The lack of supply from banks or other accounts that can quickly absorb large tail risk buying pressure means that such demand can spike volatility significantly <a class="yt-timestamp" data-t="00:44:52"></a>. Volatility then tends to revert quickly once this excess demand passes <a class="yt-timestamp" data-t="00:45:42"></a>.

## Challenges with Naive Strategies

### Implied vs. Realized Volatility Screens

Relying on simple screens like implied volatility minus trailing realized volatility for trading signals has become less effective <a class="yt-timestamp" data-t="00:31:55"></a>.

*   **Increased Competition:** [[execution_and_liquidity_in_financial_markets | Market efficiency]] has increased due to more participants analyzing these metrics <a class="yt-timestamp" data-t="00:32:05"></a>.
*   **Predictability:** Simple trailing realized volatility metrics are particularly uninformative in the current jumpy volatility regime, where there's an elevated probability of sudden spikes <a class="yt-timestamp" data-t="00:33:02"></a>.

### ETF Products for Hedging

ETF products designed for hedging (e.g., tail risk) face significant weaknesses due to [[execution_and_liquidity_in_financial_markets | market liquidity]] and **flow dynamics**:

*   **Poor Cash Efficiency:** These products often hold a large amount of treasury bonds alongside a small amount of options, making them very capital-intensive <a class="yt-timestamp" data-t="00:17:10"></a>. This can defeat the purpose of hedging, as it requires significantly cutting equity exposure to fund the hedge <a class="yt-timestamp" data-t="00:17:55"></a>.
*   **Optics vs. Function:** Investors are sensitive to the long-term performance chart of an ETF, which can lead managers to de-risk portfolios to make them look palatable, even if it means the hedge doesn't provide sufficient protection or balance sheet usage for a client <a class="yt-timestamp" data-t="00:18:16"></a>.
*   **Predictable Flows:** Simple and mechanical strategies, often used in ETFs for transparency, create predictable flows <a class="yt-timestamp" data-t="00:19:01"></a>. When such an ETF grows, its rebalancing acts are known to dealers, leading to front-running and poor performance <a class="yt-timestamp" data-t="00:19:18"></a>.

## Crowded Positioning and Skew

When there is strong dealer positioning in specific strikes (e.g., large client short strike trades), it's reflected in market pricing, making the skew through that strike range very steep <a class="yt-timestamp" data-t="00:41:08"></a>.

*   **Squeeze Risk:** A naive approach of being "short skew" in such an area might seem attractive due to the steep pricing <a class="yt-timestamp" data-t="00:41:28"></a>. However, this steepness exists precisely because dealers are crowded in that short position <a class="yt-timestamp" data-t="00:41:41"></a>. If the underlying asset moves towards that strike close to expiration, there will be massive volatility buying in that range, squeezing dealers and creating a negative expectancy for those betting against it <a class="yt-timestamp" data-t="00:41:49"></a>.
*   **Beyond Naive Views:** A long-term view on spot-volatility covariance might suggest profitability, but the reality is that the expectancy of a scenario where the spot moves to that strike means volatility will spike far more than expected <a class="yt-timestamp" data-t="00:42:25"></a>. Understanding crowded positioning is a crucial layer of analysis <a class="yt-timestamp" data-t="00:42:50"></a>.

## [[Global capital flows and their effects on asset markets | Dispersion]] and [[Global capital flows and their effects on asset markets | Implied Correlation]]

[[Global capital flows and their effects on asset markets | Dispersion]] trading, which benefits from differences in single-name volatility relative to index volatility, has evolved.

*   **Historical Context:** After being huge during the dot-com bubble, dispersion had episodic successes. There was a period (2017-2019) with low and range-bound implied spread, meaning not a lot of excess single-name volatility <a class="yt-timestamp" data-t="00:47:30"></a>. This was due to subdued retail activity and limited option demand in single names <a class="yt-timestamp" data-t="00:47:56"></a>.
*   **Post-March 2020:** The March 2020 crisis dramatically changed this. While initially a high correlation panic, it quickly morphed into massive factor and sector rotation <a class="yt-timestamp" data-t="00:48:17"></a>. This led to incredible single-name volatility, reaching record levels of the single-name versus implied spread in late 2020/early 2021 <a class="yt-timestamp" data-t="00:48:55"></a>.
*   **Retail Impact:** The surge in retail option trading, particularly in names like Tesla and mega-cap tech, significantly pushed option volumes and contributed to this increased single-name volatility <a class="yt-timestamp" data-t="00:49:06"></a>. While it quieted in summer 2021, it reignited in early November, causing spreads to explode again <a class="yt-timestamp" data-t="00:49:20"></a>.
*   **Current Regime:** Currently, there's an elevated volatility regime not just in the index, but also significantly in single names <a class="yt-timestamp" data-t="00:49:34"></a>. Implied correlation levels are relatively low given the overall volatility, reflecting more aggressive trading and continued sector/factor rotation <a class="yt-timestamp" data-t="00:49:40"></a>.
*   **Correlation Myth:** The idea that "in a crisis all correlations go to one" is often untrue <a class="yt-timestamp" data-t="00:50:08"></a>. Correlations are very unstable during crises; some go up, others drop <a class="yt-timestamp" data-t="00:50:19"></a>. For example, a market-neutral dispersion trade (short correlation) was highly profitable in 2008 due to massive sector rotation, even though a theta-neutral correlation trade that was very short overall volatility might have been hit <a class="yt-timestamp" data-t="00:50:26"></a>.

## Conclusion

[[Execution and liquidity in financial markets | Market liquidity]] and structural flows are foundational to understanding derivatives pricing and market behavior. Recognizing patterns of supply and demand, the impact of crowded positioning, and the evolving nature of volatility regimes (like the current "jumpy" environment) is critical for effective trading and risk management. Simple models or "good stories" without a deep understanding of these underlying dynamics and their impact on price and risk premium are often insufficient <a class="yt-timestamp" data-t="00:27:09"></a>. Continuously researching and tracking the flow patterns of large market participants can provide a valuable edge <a class="yt-timestamp" data-t="01:01:10"></a>.