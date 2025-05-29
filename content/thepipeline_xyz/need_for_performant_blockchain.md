---
title: need for performant blockchain
videoId: mee-5mcuvMU
---

From: [[thepipeline_xyz]] <br/> 

The inspiration to build Monad stemmed from a combination of prior experience in high-performance systems and a direct observation of the limitations within existing blockchain infrastructure <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Background in High-Frequency Trading (HFT)

The founders, James and his colleague, first met in 2014, working together on a high-frequency trading team at Jump Trading <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Their role involved building a complete trading system from the ground up, processing incoming packets from exchanges, making rapid trading decisions, and sending orders back out <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

This environment is extremely competitive and latency-sensitive <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. In HFT, the ability to decide faster and send orders to an exchange determines who secures liquidity or queue position <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This intense competition drove numerous iterations of system improvements, focusing on reducing latency and building highly performant systems <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Transition to Blockchain and DeFi

By 2021, James and the team transitioned to Jump's crypto division, immediately engaging with DeFi projects <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. James, in particular, spent about six months working on Solana DeFi, including Pith <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

This direct involvement quickly highlighted a critical gap:
*   A significant need for a more [[high_throughput_blockchains_and_infrastructure_challenges | performant blockchain]] in general <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   A specific and pressing need for a more performant Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

The existing EVM implementations were found to be very inefficient and lacked the level of optimization seen in the high-frequency trading systems they previously developed <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This highlighted [[challenges_in_current_blockchain_infrastructure | challenges in current blockchain infrastructure]] and [[challenges_in_blockchain_system_design | blockchain system design]].

## Monad's Founding Principle

The team recognized that their background in building highly performant systems from the ground up was uniquely suited to address these [[technical_challenges_and_solutions_in_blockchain_performance | technical challenges and solutions in blockchain performance]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. While understanding that significant optimization work would be required, the clear need for a more performant EVM became the primary driver for Monad <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The initial implementation of a [[parallelization_in_blockchain_technologies | parallel EVM]] was a direct outcome of this realization <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The observed performance differences between Solana and Ethereum further underscored the potential for [[performance_gains_in_blockchain_transactions | optimizations in the EVM space]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.