---
title: Overview of CAP Finance Protocol
videoId: nO-0tcLFEB0
---

From: [[goingonchain]] <br/> 

CAP Finance is described as a decentralized exchange (DEX) for synthetic assets, currently supporting trading pairs for ETH and BTC <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. It allows traders to use leverage up to 50x <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Mechanics of CAP Finance

CAP Finance differentiates itself by having no fees for traders, aiming to build a flywheel effect where no fees lead to more traders, more volume, and ultimately more liquidity <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Traders on CAP Finance operate without a stop-loss feature, and liquidation occurs at 80% <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### [[mechanics_of_caps_liquidity_pool | Liquidity Pool]]

On CAP Finance, traders engage in transactions against a [[mechanics_of_caps_liquidity_pool | liquidity pool]] comprised of ETH and USDC <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This [[mechanics_of_caps_liquidity_pool | pool]] acts as the counterparty for traders <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

*   **Trader Wins**: If a trader wins, they take profit directly from the [[mechanics_of_caps_liquidity_pool | pool]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Trader Losses**: If a trader loses, the assets from their position go into the [[mechanics_of_caps_liquidity_pool | ETH and USDC pool]] <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Interestingly, 100% of a losing position's assets are contributed to this [[mechanics_of_caps_liquidity_pool | pool]] <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. In cases of liquidation, a partial amount of the liquidated asset also goes into the [[mechanics_of_caps_liquidity_pool | pool]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Yields

The attractive yields offered by CAP Finance are generated from the losses incurred by traders, effectively positioning the [[mechanics_of_caps_liquidity_pool | liquidity pool]] providers as "the house" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

Current yields include:
*   69% on ETH <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   34% on USDC <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Staking the native CAP token yields around 11.5% <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>

### Tokenomics

The CAP token's primary utility currently is for exposure to the protocol's potential growth, as there is no governance feature associated with the token <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. CAP Finance has a market capitalization of approximately $12.5 million <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Based on current numbers and the total revenue shares to holders, CAP Finance has a Price-to-Earnings (PE) ratio of approximately 9.87 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. For comparison, GMX, another perpetual decentralized exchange, has a PE ratio of roughly 14.5 <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Users can verify these figures using platforms like Token Terminal <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## [[risks_associated_with_cap_finance | Risks Associated with CAP Finance]]

Providing liquidity to the [[mechanics_of_caps_liquidity_pool | pool]] on CAP Finance is not without [[risks_associated_with_cap_finance | risk]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Loss of Deposit**: In a scenario where a group of traders achieves significant wins, [[risks_associated_with_cap_finance | providers may not retrieve their full deposit]] as profits are drawn from the [[mechanics_of_caps_liquidity_pool | pool]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This is particularly true if a large group of traders experiences a "big win" <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Withdrawal Fees and Lock-up**: Withdrawals from the [[mechanics_of_caps_liquidity_pool | pool]] incur a 1% fee for both ETH and USDC pools <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Additionally, there is a 24-hour lock-up period during which funds cannot be withdrawn once deposited <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Dynamic Yields**: The yields offered are dynamic; as more funds flow into the [[mechanics_of_caps_liquidity_pool | pool]], the yield percentage is expected to decrease <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.