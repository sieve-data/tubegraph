---
title: Understanding the Ethereum Merge
videoId: uphXlOeJFJo
---

From: [[goingonchain]] <br/> 

The Ethereum Merge marks the end of Proof of Work (PoW) for Ethereum, fully transitioning it to Proof of Stake (PoS) <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The [[differences_between_ethereum_pos_and_pow_chains|Beacon Chain]], which is Ethereum's Proof of Stake chain, has been operational since December 1, 2020 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Staking services offered by platforms like Binance, KuCoin, and Lido already allow users to stake on the [[preparing_for_the_ethereum_merge|Beacon Chain]] <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Currently, the [[differences_between_ethereum_pos_and_pow_chains|Beacon Chain]] is running but not yet producing blocks for the mainnet <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Impact on Gas Fees

Contrary to a common misconception, the Merge will not inherently lower gas fees <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

The technical explanation for this is:
*   A blockchain consists of three layers: the execution layer, the consensus layer, and the data availability layer <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   The Merge primarily changes the *consensus layer* from PoW to PoS <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   Gas fees are paid on the *execution layer*, meaning there will be no direct changes to gas fees from the Merge itself <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   Blockchain gas fees are determined by the supply and demand for block space <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. High demand, similar to surges seen on chains like Fantom during busy periods, leads to higher fees <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Other factors influencing gas fees include Ethereum's block size, which became variable after the London upgrade <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, and the complexity of decentralized applications (DApps) being used, as more complex DApps consume more transactions <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

> [!NOTE]
> The Merge itself will not directly lower gas fees. The changes are at the consensus layer, not the execution layer where gas fees are incurred <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Reasons for the Merge

The Merge is being implemented for several key reasons <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:

### Lower Security Cost
Proof of Work (PoW) mining rigs are expensive to set up and consume significant energy <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. By moving to Proof of Stake (PoS), the security cost is lowered, enabling more participants to become validators with less energy consumption and lower costs <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. For instance, an Ethereum 2.0 validator can run on a Raspberry Pi (with 32 ETH) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. For those with less than 32 ETH, participation is possible through staking pools like Lido or Rocket Pool <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This broadens participation in the network's validation process <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Scalability for the Future
The Merge is crucial for future scalability initiatives, including sharding (EIP-4844) and statelessness <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. While scaling is difficult with PoW, Proof of Stake allows for easier expansion of the blockchain's capabilities <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Clarifications on Common Narratives

Certain narratives circulating, particularly on crypto Twitter, might condense information, leading to misconceptions <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### 99.9% Network Operating Cost Reduction
This figure refers to the reduction in energy and hardware costs associated with moving from PoW to PoS, enabling validators to use less powerful hardware like a Raspberry Pi or participate through staking pools <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### 90% ETH Issuance Reduction
This refers to a significant drop in the daily supply or issuance of Ethereum <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Currently, daily Ethereum issuance from mining is around 13,300 to 13,500 ETH, accounting for about 4.3% of the total supply <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. After the move to Proof of Stake, this issuance is projected to drop to 0.3% to 0.4% <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

This reduction, combined with [[eip1559_and_its_impact_on_ethereum_issuance|EIP1559 and its Impact on Ethereum Issuance]] (which burns the base fee of transactions), can lead to Ethereum becoming deflationary <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. At the peak of NFT hype, the network was burning more ETH than it was producing daily <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. After [[eip1559_and_its_impact_on_ethereum_issuance|EIP1559]] was implemented, approximately 2 million ETH have been burned, with net issuance for that period around 1.2 million ETH, indicating a deflationary effect <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The combination of reduced daily issuance and the burning mechanism aims to make Ethereum deflationary in the long run <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

### 50-100% Staking Yield Increase
Currently, typical staking interest rates on platforms like Lido, KuCoin, or Binance range from 3% to 5% APR <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. After the Merge, the expected staking yield for ETH is projected to increase to around 10% <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Rewards for block validation will be given to stakers instead of miners in the PoS system <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## When is the Merge Coming?

There is no specific date for the Merge, but many narratives suggest Q2 or June <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Key facts to consider:
*   The Merge is already on the Kiln testnet, though there are still implementation issues being addressed by developers <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   After Kiln, there are other testnets like "Glory" that need to be run before the Merge can happen on the mainnet <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   Users can monitor the progress on websites like `whenmerge.com` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

## Impact of Unstaking Locked ETH

The [[differences_between_ethereum_pos_and_pow_chains|Beacon Chain]], launched on December 1, 2020, currently has approximately 10 million ETH staked and locked <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. At the start of the [[differences_between_ethereum_pos_and_pow_chains|Beacon Chain]], ETH price was around $700-$1000, while at the time of discussion, it was about $3,500 <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

Concerns exist about a potential price crash if all locked ETH were to be unstaked and sold post-Merge <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. However, several factors mitigate this risk:
*   Not all 10 million ETH will be unstaked immediately; users have individual decisions to sell or hold <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   There's a built-in queue system that limits the number of validators that can be released daily to a maximum of 1,125 <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. This means only a limited amount of ETH (around 36,000 ETH based on 32 ETH per validator) can be unstaked each day <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
*   The attractive 10% annual staking yield post-Merge provides an incentive for users to continue holding their ETH for staking rewards rather than selling <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   Withdrawals will not be enabled immediately after the Merge. There will be a period of 6 to 8 months between the Merge and the first hard fork that enables withdrawals <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. During this period, no new ETH will be issued <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

## Staking Options for Users

For users who do not possess the 32 ETH required to run a solo validator node, there are pooling options available:
*   **Lido**: Allows users to stake ETH and earn approximately 3.9% interest <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Rocket Pool**: Offers similar staking services with rates around 4% <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

These pooling options allow users to contribute as little as 0.1 ETH <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a> and receive liquid staking tokens (e.g., rETH from Rocket Pool, stETH from Lido) which can then be used in other decentralized finance (DeFi) protocols <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.