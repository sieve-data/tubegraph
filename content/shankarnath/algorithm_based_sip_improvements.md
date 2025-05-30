---
title: Algorithm based SIP improvements
videoId: WT8_9-ll7XU
---

From: [[shankarnath]] <br/> 

A [[Systematic Investment Plans SIP overview | Systematic Investment Plan (SIP)]] is a popular and effective investment strategy that helps investors manage market fluctuations by averaging performance over time [00:00:38]. While traditional [[Systematic Investment Plans SIP overview | SIPs]] involve investing a fixed amount regularly, newer approaches and strategies aim to visibly improve returns by layering intelligence over the basic [[Systematic Investment Plans SIP overview | SIP]] structure [00:01:00].

## The Flaw in Traditional SIPs
Traditional [[Systematic Investment Plans SIPs for Longterm Growth | SIPs]], by investing a fixed amount monthly, do not account for additional market information, such as significant drops in market indices [00:02:46]. For example, if the Nifty were to drop by 15%, a traditional [[Systematic Investment Plans SIP overview | SIP]] would not prompt an investor to invest more, missing out on potential opportunities [00:03:00]. This perceived flaw has led to the development of algorithm-based solutions.

## Algorithm-Based SIPs (Commercial Offerings)
Various fund houses and platforms offer enhanced [[Systematic Investment Plans SIP overview | SIP]] options, often referred to as [[Value SIP and market timing | Value SIP]], Alpha [[Value SIP and market timing | SIP]], Smart [[Value SIP and market timing | SIP]], Flex [[Value SIP and market timing | SIP]], or Booster [[Value SIP and market timing | SIP]] [00:02:21]. The core principle of these strategies is to invest more when markets are undervalued and reduce investments when markets are expensive [00:03:32]. This process is typically supported by an underlying model or algorithm [00:03:39].

### ICICI Prudential Booster SIP
ICICI Prudential's Booster [[Value SIP and market timing | SIP]] adds two layers over a traditional [[Systematic Investment Plans SIP overview | SIP]] [00:03:38]:
1.  **Proprietary Equity Valuation Index (EVI) Model**: This model informs the [[Systematic Investment Plans SIP overview | SIP]] when equities are considered expensive or cheap [00:03:43].
2.  **Variable Amount Setup**: Based on the EVI model's input, the amount transferred can range from 10% to 1,000% of the base [[Systematic Investment Plans SIP overview | SIP]] amount [00:03:53]. For instance, if equities are super cheap and the base [[Systematic Investment Plans SIP overview | SIP]] is 10,000 rupees, the fund house might invest up to 100,000 rupees (1,000%) [00:04:03]. If equities are super expensive, the investment might be pruned to 1,000 rupees (10%) [00:04:16].

The Booster [[Value SIP and market timing | SIP]] operates on a source fund/target fund concept [00:04:22]. Funds are first transferred to a source fund (often a short-duration debt fund) and then transferred to a chosen equity or hybrid target fund, on which the EVI model is applied [00:04:25]. ICICI Prudential's back-testing of the Booster [[Value SIP and market timing | SIP]] over the Nifty 50, Midcap 150, and Small Cap 250 indices for 17 years showed a 1% to 2% increase in CAGR [00:04:40].

### Kotak Mutual Fund Smart SIP
Kotak Mutual Fund's Smart [[Value SIP and market timing | SIP]] functions similarly, with the monthly [[Systematic Investment Plans SIP overview | SIP]] amount determined by Kotak's Baff net Equity Allocation Model, which classifies the market as cheap, neutral, or expensive [00:04:56]. While Kotak applies default min/max values of 50% and 200% of the [[Systematic Investment Plans SIP overview | SIP]] amount, investors can modify these limits [00:05:11]. The key difference from ICICI's offering is that Kotak directly changes the actual [[Systematic Investment Plans SIP overview | SIP]] amount, rather than using a source and target fund [00:05:18].

### Other Offerings
Other fund houses and platforms also provide similar enhanced [[Systematic Investment Plans SIP overview | SIP]] options:
*   HDFC Mutual Fund offers a Flex [[Value SIP and market timing | SIP]] [00:05:35].
*   Rankmf.com provides a Smart [[Value SIP and market timing | SIP]] that can buy, sell, and even skip [[Systematic Investment Plans SIP overview | SIP]] installments [00:05:41].
*   Php.com has an Alpha [[Value SIP and market timing | SIP]] [00:05:49].

This trend of adding features to [[Systematic Investment Plans SIP overview | SIPs]] is expected to continue, even though the classical premise of an [[Systematic Investment Plans SIP overview | SIP]] was to invest irrespective of market conditions [00:05:57]. Investing is an evolutionary process, and staying informed about new developments is beneficial [00:06:10].

## DIY Algorithm-Based SIP Strategies
It is possible to implement "smart [[Value SIP and market timing | SIP]]" strategies oneself [00:06:24]. Two DIY strategies discussed include [[DIY SIP strategies and market valuation | strategies based on relative valuation and market valuation using the P/E ratio]].

### Strategy 1: Relative Valuation
This strategy involves comparing the monthly closing values of indices like the Nifty Smallcap 250 TR and the Nifty50 TR to derive a "relative score" [00:06:42]. By setting up scenarios based on this score, it has been shown to generate "good Alpha" on a post-tax basis [00:07:00]. However, attempts to replicate this process with the Nifty Midcap 150 index yielded less consistent results [00:07:18].

### Strategy 2: Market Valuation (P/E Ratio)
The P/E ratio is considered a primary basis for many commercial smart [[Value SIP and market timing | SIPs]] [00:07:56]. This DIY strategy involves adjusting monthly [[Systematic Investment Plans SIP overview | SIP]] investments based on the Nifty 50 P/E ratio [00:08:06].

**Base Scenario**: A regular monthly [[Systematic Investment Plans SIP overview | SIP]] of 10,000 rupees in the Nifty 50 from January 2007 to December 2022 (16 years) yielded a CAGR of 13% [00:08:14]. This 13% serves as the benchmark to beat [00:08:42].

**P/E Ratio Bands**:
The strategy defines bands for the Nifty's P/E ratio [00:08:52]:
*   **Normal (18-24 P/E)**: If the Nifty P/E is within this range (around the long-term average of 21), the investor continues the regular 10,000 rupee [[Systematic Investment Plans SIP overview | SIP]] without changes [00:09:07].
*   **Outside Bands**: When the P/E goes above 24 or drops below 18, different buy and sell actions are activated [00:09:28]. This essentially involves investing more when the market seems undervalued and redeeming units when it appears overvalued [00:09:39].

**Scenarios Tested**:
Five scenarios were tested over the 16-year period [00:10:01]:
1.  **Scenario 1 (Base Case)**: Invest 10,000 rupees every month, irrespective of P/E ratio, resulting in a 13% return [00:10:06].
2.  **Scenario 2**: Invest 10,000 rupees only in months where the P/E ratio is 22 or lower (holding [[Systematic Investment Plans SIP overview | SIP]] when the market is expensive) [00:10:14].
3.  **Scenario 3**: Invest in all P/E bands, but increase investment on an accelerated basis when the P/E ratio falls below 18 [00:10:28]. For example, an additional 10,000 rupees might be invested when P/E is between 16 and 18, with higher investments as P/E goes lower [00:10:37].
4.  **Scenario 4**: Invest 10,000 rupees when P/E is 22 or less, but redeem 10,000 rupees worth of units when P/E goes above 22 [00:10:57].
5.  **Scenario 5**: Employ an accelerated buying and selling structure across different P/E bands [00:11:13]. For instance, committing 50,000 rupees when P/E is 11 (very cheap) and withdrawing 40,000 rupees when P/E is 30 (super expensive) [00:11:21].

All four advanced scenarios (2, 3, 4, and 5) outperformed the 13% base case [00:11:59]. This suggests that adding an intelligence layer to an [[Systematic Investment Plans SIP overview | SIP]] can significantly improve returns [00:12:06].

### DIY Implementation
Implementing this DIY strategy requires a few steps each month, taking approximately 6 minutes [00:13:02]:
1.  **Monthly Reminder**: A calendar notification to check the Nifty P/E ratio [00:13:32].
2.  **P/E Data Retrieval**: Obtain the previous month's closing P/E ratio from reliable sources like Niftyindices.com [00:12:43].
3.  **Action Determination**: Consult a pre-defined table of P/E ratio bands to determine the required action (buy, sell, or continue regular [[Systematic Investment Plans SIP overview | SIP]]) [00:12:51].
4.  **Execution**: Log into a trading account and buy or sell the corresponding number of Nifty ETF units [00:12:56].

This small investment of time can lead to a potential gain of 1% or 2% in returns, which can make a significant difference over the long term [00:13:09]. Even a small commitment, like 1,000 rupees a month, can be used to test this approach in the real world [00:13:39].