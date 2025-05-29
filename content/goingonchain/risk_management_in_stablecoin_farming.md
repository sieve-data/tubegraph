---
title: Risk management in stablecoin farming
videoId: LelKwA_0CpA
---

From: [[goingonchain]] <br/> 

Given the uncertainty in the market, strategies to optimize [[earning_interest_on_stablecoins | stablecoin]] yields while managing associated risks become a key consideration <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While yield optimization protocols can be an interesting consideration during market volatility, it is crucial to understand that they are not risk-free <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Grow Protocol's Approach to Risk Balancing

Grow Protocol is a DeFi yield optimizer designed to balance risk and offer leverage on stablecoins <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The protocol has two primary products that work closely together to manage risk and return:

*   **Powered** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>: This product functions similarly to a fixed deposit for stablecoins, offering returns superior to traditional finance ("TradFi") and providing deposit protection <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Vault** <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>: This product offers [[stablecoin_leveraged_yield_farming | leveraged yield]] on stablecoins <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The Vault leverages assets from the Powered saving pool; consequently, when there are more deposits in Powered, the returns for the Vault increase <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Critically, any protocol losses incurred are first covered by the Vault <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Automated Leverage Yield ("Labs") and Risk Rebalancing

Grow Protocol has extended its expertise to Avalanche, introducing two active "Labs": the USDC Leverage Yield and the USDT Leverage Yield <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

The Labs operate by leveraging farms from Alpha Homora v2, a [[stablecoin_leveraged_yield_farming | leveraged yield farming]] platform on Avalanche <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Funds from the Labs are used as collateral to borrow AVAX, and stablecoins are leveraged at 2x to open new positions <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

Key risk management features of the Labs include:
*   **Automated Strategy Execution** <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>: The Labs execute strategies automatically based on market conditions <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Each time a position is opened and closed, it's considered a "strategy cycle" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Continuous Risk Rebalancing** <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>: The risks within the Labs are continuously rebalanced <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Performance Resilience Example** <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>: A test conducted from December 3rd to December 6th, during which AVAX dropped approximately 20% (from $104 to $83), showed the Lab strategy yielding a 0.5% gain despite the significant market decline <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. During this period, the Lab opened and closed positions 13 times <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

While some individual strategy cycles may show negative returns, the average return for the Labs is approximately 17% <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The Lab UI provides transparency by showing Total Value Locked (TVL), reserves (funds not yet deployed), and AVAX exposure <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Important Considerations for Investors

Despite the risk balancing mechanisms, investors are advised that these protocols are not risk-free <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Given that DeFi is a nascent and rapidly evolving space, it is crucial to perform your own research and make independent investment decisions <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. For more information on [[evaluating_and_managing_yield_farming_risks | evaluating and managing yield farming risks]] and using stablecoins to earn yield, resources such as Grow Protocol's website and Twitter can be consulted <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.