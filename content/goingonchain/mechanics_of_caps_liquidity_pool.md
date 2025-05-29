---
title: Mechanics of CAPs Liquidity Pool
videoId: nO-0tcLFEB0
---

From: [[goingonchain]] <br/> 

CAP Finance is a decentralized exchange designed for synthetic assets, currently supporting trading pairs for ETH and BTC <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Users can engage in leveraged trading up to 50x <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The protocol ensures liquidity by having traders interact directly with a central liquidity pool, rather than other traders <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## The Liquidity Pool

The core of CAP Finance's liquidity system is a pool composed of ETH and USDC <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This pool acts as the counterparty for all traders on the platform <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Essentially, liquidity providers become "the house" for the trading operations <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Interaction with Traders

The mechanics of how traders interact with the pool directly influence the pool's assets:
*   **Trader Wins**
    *   If a trader wins, they withdraw profit directly from the ETH and USDC pool <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Trader Losses**
    *   If a trader loses, 100% of their lost position is deposited into the ETH and USDC pool <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Liquidations**
    *   When a trader's position is liquidated, a portion of the liquidated assets also goes into the pool <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

These dynamics mean that yields for [[liquidity_provision_and_its_benefits | liquidity providers]] are primarily generated from trader losses <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Providing Liquidity on CAP Finance

Users can become [[providing_liquidity_through_platforms | liquidity providers]] by depositing ETH or USDC into the respective pools.

### Current Yields
*   **ETH Pool**: Offers approximately 69% yield <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   **USDC Pool**: Offers approximately 34% yield <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **CAP Token Staking**: Staking the native CAP token yields around 11.5% <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

These attractive yields are derived from the aggregate losses of traders on the platform <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Risks and Considerations for Liquidity Providers

While providing liquidity can offer high yields, it is important to note that [[risks_of_investing_in_volatile_liquidity_pools | pooling is not risk-free]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Exposure to Trader Profits**: If a large group of traders makes significant profits, they will withdraw from the pool, potentially impacting a liquidity provider's deposited funds <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. In such a scenario, providers might not recover their full initial deposit <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Dynamic Yields**: The yields offered are dynamic and can decrease as more funds enter the pool <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Withdrawal Fees and Lock-up**:
    *   A 1% fee applies to withdrawals from both the ETH and USDC pools <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   There is a 24-hour lock-up period, meaning funds cannot be withdrawn for the first 24 hours after deposit <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Market Position

CAP Finance has a market cap of approximately $12.5 million <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. It aims to differentiate itself from competitors like GMX and Gains by offering no trading fees, with the goal of attracting more traders and thereby increasing trading volume and liquidity <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This "flywheel" approach intends to continually boost [[incentive_mechanisms_for_liquidity_providers | liquidity incentives]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

For those interested in [[overview_of_cap_finance_protocol | CAP Finance]], the protocol offers opportunities to trade without fees, though it currently lacks a stop-loss feature and has a liquidation threshold at 80% <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Alternatively, users can become liquidity providers and earn yields by acting as the market maker <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.