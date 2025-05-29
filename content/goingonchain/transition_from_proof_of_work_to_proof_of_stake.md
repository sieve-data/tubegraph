---
title: Transition from Proof of Work to Proof of Stake
videoId: uphXlOeJFJo
---

From: [[goingonchain]] <br/> 

The Ethereum Merge represents a pivotal shift for the Ethereum network, marking the end of its [[proof_of_work_vs_proof_of_stake | Proof of Work]] (PoW) consensus mechanism and its full transition to [[proof_of_work_vs_proof_of_stake | Proof of Stake]] (PoS) <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This transition effectively merges the current Ethereum mainnet with the Beacon Chain <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## What is The Merge?

The Beacon Chain, which functions as the Ethereum [[proof_of_work_vs_proof_of_stake | Proof of Stake]] chain, has been operational since December 1, 2020 <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Platforms like Binance, KuCoin, and Lido have already allowed users to participate in [[staking_on_snowbank | staking]] on the Ethereum Beacon Chain <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. While running, the Beacon Chain is not yet producing blocks <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Impact on Gas Fees

A common question regarding The Merge is whether it will lead to lower gas fees <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Technically, The Merge will not lower gas fees <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

Blockchains operate with three primary layers:
*   **Execution Layer** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>
*   **Consensus Layer** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>
*   **Data Availability Layer** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>

The Merge specifically alters the Consensus Layer, shifting from [[proof_of_work_vs_proof_of_stake | Proof of Work]] to [[proof_of_work_vs_proof_of_stake | Proof of Stake]] <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. However, gas fees are incurred on the Execution Layer, which remains unchanged by The Merge <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Gas fees are primarily influenced by supply and demand for block space <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For instance, high demand for block space, such as during periods of increased activity in decentralized applications (dApps), leads to higher gas fees <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

While the Ethereum block size was expanded after the London upgrade in August 2021, and dApp complexity also affects gas usage, these factors are distinct from the consensus mechanism change <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Reasons for The Merge

The Merge is being implemented for several strategic reasons:

### Lower Security Costs
The current [[proof_of_work_vs_proof_of_stake | Proof of Work]] system for Ethereum requires expensive mining rigs and consumes significant energy <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. By transitioning to [[proof_of_work_vs_proof_of_stake | Proof of Stake]], the cost and energy required to achieve network consensus are substantially reduced <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This allows more individuals to become validators, potentially even using a Raspberry Pi, provided they have 32 ETH <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. For those with less than 32 ETH, participation is possible through [[staking_on_snowbank | staking pools]] like Lido or Rocket Pool <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Scalability for the Future
The Merge is a foundational step for future scalability enhancements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Upcoming plans include EIP 484 (sharding) and statelessness <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. [[proof_of_work_vs_proof_of_stake | Proof of Stake]] makes it significantly easier to extend the blockchain's capabilities compared to [[proof_of_work_vs_proof_of_stake | Proof of Work]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Clarifying Common Narratives

Many narratives surrounding The Merge circulate, especially on platforms like Crypto Twitter, which can sometimes lead to misconceptions <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Here are clarifications on some key points:

### 99.9% Network Operating Cost Reduction
This refers to the reduction in energy and hardware costs associated with moving from mining rigs to a [[proof_of_work_vs_proof_of_stake | Proof of Stake]] system, enabling validation with less intensive hardware like a Raspberry Pi <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### 90% ETH Issuance Reduction
Currently, approximately 13,500 ETH are issued daily through mining, contributing to about 4.3% of the total supply <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. Post-Merge, with [[proof_of_work_vs_proof_of_stake | Proof of Stake]], daily issuance is projected to drop dramatically to between 0.3% and 0.4% <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

This reduction is amplified by EIP-1559, which burns the base fee component of transaction fees <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. During peak periods, such as the NFT boom, the burning mechanism led to Ethereum becoming deflationary, meaning more ETH was burned than produced daily <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The combination of EIP-1559 and the reduced daily issuance post-Merge is expected to make ETH deflationary in the long run, leading to a decreased supply in the market <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

### 50-100% Staking Yield Increase
Current [[staking_on_snowbank | staking]] yields on platforms like Lido, KuCoin, or Binance typically range from 3% to 5% APR <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. Post-Merge, the expected [[staking_on_snowbank | staking]] yield is projected to increase to around 10% APR <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Rewards, previously distributed to miners, will now be given to stakers <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## When is The Merge Coming?

While there's no specific date, with narratives suggesting Q2 or June <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>, key developments are underway. The Merge is already implemented on the Kiln testnet <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>, though some implementation issues are being addressed <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Users can monitor progress via websites like "whenmerged.com" <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

The Beacon Chain, which began running on December 1, 2020, currently has about 10 million ETH staked <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

### Concerns About ETH Unlocking

A significant concern is the potential for a sell-off when the staked ETH from the Beacon Chain becomes unlockable <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. When the Beacon Chain launched, ETH was priced around $700-$1000 <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

However, several factors mitigate this concern:
1.  **Not all 10 million ETH will be immediately sold** <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
2.  **Built-in Queue System**: There's a maximum daily release of 1,125 validators, equating to approximately 36,000 ETH per day <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
3.  **Incentive to Hold**: With an expected 10% [[staking_on_snowbank | staking]] yield post-Merge, many holders may choose to continue staking rather than selling <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
4.  **Withdrawal Delay**: There will be a period of six to eight months between The Merge and the first hard fork that enables withdrawals <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. During this period, no new ETH will be issued <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>, potentially leading to price implications if supply tightens <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Staking Options for Users

For users who wish to participate in [[staking_on_snowbank | staking]] but do not possess the required 32 ETH <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>, pooling options are available:
*   **Lido**: Offers an APR of approximately 3.9% <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Rocket Pool**: Offers rates around 4% <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

These platforms allow users to contribute as little as 0.1 ETH and receive liquid [[decentralized_finance_options_and_liquid_staking | liquid staking]] tokens (e.g., rETH from Rocket Pool), which can then be used in other decentralized finance (DeFi) protocols <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.