---
title: Proof of work vs proof of stake in Ethereum
videoId: uphXlOeJFJo
---

From: [[goingonchain]] <br/> 

The discussion surrounding [[the_merge_on_ethereum | The Merge]] for Ethereum has generated many narratives and some misconceptions, even in mass media and crypto Twitter <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article condenses information about this significant transition.

## What is [[the_merge_on_ethereum | The Merge]]?
[[the_merge_on_ethereum | The Merge]] officially marks the end of [[proof_of_work_vs_proof_of_stake | Proof of Work]] (PoW) for Ethereum, transitioning it to a full [[proof_of_work_vs_proof_of_stake | Proof of Stake]] (PoS) system <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Currently, [[the_merge_on_ethereum | The Merge]] effectively combines the existing Ethereum mainnet with the Beacon Chain <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## The Beacon Chain
The Beacon Chain is Ethereum's [[proof_of_work_vs_proof_of_stake | Proof of Stake]] component, which has been operational since December 1st, 2020 <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Services like Binance Staking ETH 2.0, KuCoin Staking ETH 2.0, and Lido, among others, facilitate staking on the Ethereum Beacon Chain <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Although running, the Beacon Chain is not yet producing blocks, a function that will be integrated post-[[the_merge_on_ethereum | Merge]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Gas Fees Post-[[the_merge_on_ethereum | Merge]]
A common question is whether [[the_merge_on_ethereum | The Merge]] will lower gas fees <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Technically, it will not <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
Blockchains operate on three layers:
1.  **Execution Layer** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>
2.  **Consensus Layer** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>
3.  **Data Availability Layer** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>

[[the_merge_on_ethereum | The Merge]] specifically changes the consensus layer from [[proof_of_work_vs_proof_of_stake | Proof of Work]] to [[proof_of_work_vs_proof_of_stake | Proof of Stake]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. However, gas fees are paid for usage on the execution layer, which will remain unchanged <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Gas fees are primarily influenced by:
*   **Supply and Demand of Block Space**: Higher demand leads to higher gas fees, similar to how Fantom's gas fees surged during peak activity <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Block Size**: After the London upgrade (August 2021), Ethereum's block size became variable <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Complexity of Decentralized Applications (dApps)**: More complex dApps require more transactions, increasing gas usage <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Reasons for [[ethereums_transition_from_pow_to_pos | Ethereum's transition from POW to POS]]
Despite not reducing gas fees, [[the_merge_on_ethereum | The Merge]] offers significant benefits:

### 1. Lower [[security_cost_and_scalability_improvements_in_ethereum | Security Cost]]
[[proof_of_work_vs_proof_of_stake | Proof of Work]] mining rigs are expensive to set up and consume substantial energy <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. By transitioning to [[proof_of_work_vs_proof_of_stake | Proof of Stake]], Ethereum aims to lower the [[security_cost_and_scalability_improvements_in_ethereum | security cost]], making it more accessible for individuals to participate as validators with less energy and cost <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For instance, in ETH 2.0, one could run a validator node on a Raspberry Pi, provided they have 32 ETH <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. For those with less than 32 ETH, participation is possible through staking pools like Lido or Rocket Pool, which aggregate ETH for validation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### 2. Scalability
[[the_merge_on_ethereum | The Merge]] is a foundational step for future scalability enhancements. It paves the way for initiatives like EIP-4844 (sharding) and statelessness <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Extending the blockchain's capabilities is significantly easier under [[proof_of_work_vs_proof_of_stake | Proof of Stake]] compared to [[proof_of_work_vs_proof_of_stake | Proof of Work]] <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## Impact on Ethereum's Supply and Staking Yield

### 90% ETH Issuance Reduction
This refers to a drastic reduction in the daily supply of ETH. Under [[proof_of_work_vs_proof_of_stake | Proof of Work]], Ethereum's daily issuance was approximately 13,300 to 13,500 ETH, representing about 4.3% of the total supply <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Post-[[the_merge_on_ethereum | Merge]] to [[proof_of_work_vs_proof_of_stake | Proof of Stake]], daily issuance is projected to drop to 0.3% to 0.4% <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

This reduction, combined with EIP-1559, which burns the base fee of transactions, can lead to a deflationary environment for ETH <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. For example, at the peak of the NFT craze, Ethereum was already deflationary, burning more ETH than it produced daily <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Since EIP-1559's implementation, over 2 million ETH have been burned, with net issuance for that period being only 1.2 million ETH <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. The combination of reduced daily issuance and the burning mechanism is expected to make ETH deflationary in the long run <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### [[staking_and_yield_changes_post_ethereum_merge | 50-100% Staking Yield Increase]]
Currently, staking ETH on platforms like Lido, KuCoin, or Binance yields an APR of 3% to 5% <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. After [[the_merge_on_ethereum | The Merge]], the [[staking_and_yield_changes_post_ethereum_merge | staking yield]] is expected to increase significantly, potentially reaching around 10% <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This higher yield could incentivize more users to stake their ETH, similar to how [[choosing_validators_for_luna_staking | LUNA staking]] offered 7% to 8% <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. In a [[proof_of_work_vs_proof_of_stake | Proof of Stake]] system, rewards are distributed to [[role_of_liquidity_providers_and_stakers_in_dex_token_systems | stakers]] instead of miners <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## When is [[the_merge_on_ethereum | The Merge]] Coming?
While narratives often point to Q2 or June, there is no specific date <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   [[the_merge_on_ethereum | The Merge]] is already live on the Kiln testnet, though there are still implementation issues being addressed <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   More testnets (like Gorli) are planned before the mainnet launch <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   Users can monitor progress on websites like `whenmerged.com` <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Unlocking Staked ETH Post-[[the_merge_on_ethereum | Merge]]
Currently, about 10 million ETH are staked on the Beacon Chain, locked in <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Concerns exist about a potential price crash if all staked ETH (originally locked at ETH prices of around $700-$1,000) were to be unlocked and sold <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. However, several factors mitigate this risk:
*   Not all 10 million ETH will be immediately sold; individual users will make their own decisions <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   A built-in queue system limits daily withdrawals to a maximum of 1,125 validators (approximately 36,000 ETH) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   The anticipated 10% [[staking_and_yield_changes_post_ethereum_merge | staking yield]] may incentivize [[role_of_liquidity_providers_and_stakers_in_dex_token_systems | stakers]] to continue holding and earning rewards rather than selling <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   Between [[the_merge_on_ethereum | The Merge]] and the first hard fork (which will enable withdrawals), no new ETH will be issued for approximately six to eight months <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. This period of limited supply could lead to interesting price dynamics <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

## How to Participate in Staking
For those without 32 ETH, pooling options allow participation with smaller amounts (e.g., 0.1 ETH) <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Lido**: Offers liquid staking, currently yielding around 3.9% APR <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Participants receive a receipt token (stETH).
*   **Rocket Pool**: Another pooling option, with rates around 4% APR <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. Participants receive rETH as a liquid staking token.

These liquid staking tokens allow users to earn [[staking_and_yield_changes_post_ethereum_merge | staking rewards]] while also using their staked assets in other decentralized finance (DeFi) applications <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.