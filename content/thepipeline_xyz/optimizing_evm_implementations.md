---
title: optimizing EVM implementations
videoId: mee-5mcuvMU
---

From: [[thepipeline_xyz]] <br/> 

The inspiration to build Monad stemmed from a background in developing highly performant systems and identifying a significant [[need_for_performant_blockchain | need for performant blockchain]] technology, particularly within the Ethereum Virtual Machine (EVM) space <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Background in High-Frequency Trading
The founders, James and another individual, met in 2014 while working on a high-frequency trading team at Jump Trading <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Their role involved building a complete trading system from scratch <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This system processed packets from exchanges, made rapid trading decisions, and sent orders back to the exchange <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

The high-frequency trading environment is extremely competitive regarding latency <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. In this space, the participant who can decide and send an order faster wins the opportunity to either take liquidity or secure a queue position for an order <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This intense competition spurred continuous iterations of system improvements, focusing on shaving off latency and building exceptionally performant systems <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Transition to Blockchain and DeFi
By 2021, James and the team transitioned to the crypto division at Jump, where they began working on DeFi projects <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. James, specifically, spent about six months working on Solana DeFi <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Identifying the Need for EVM Optimization
During their work in DeFi, they recognized a substantial [[need_for_performant_blockchain | need for more performant blockchain]] technology in general <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Crucially, they identified a significant [[need_for_performant_blockchain | need for more performant EVM]] implementations <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

Existing EVM implementations were found to be very inefficient and lacked the level of optimization that the team had previously applied to high-frequency trading systems <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Their extensive background in building highly [[performance_gains_in_blockchain_transactions | performant systems]] from the ground up made them uniquely suited to address this challenge <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. They understood that achieving these [[optimizing_ethereum_virtual_machine_performance | optimizations]] would require a significant, long-term effort involving a complete [[blockchain_redesign_for_high_performance | redesign for high performance]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Monad's Inspiration
The initial inspiration for Monad was a combination of their experience in building performant systems for trading and their direct interaction with both Solana and Ethereum <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. While Solana had undergone many [[optimizing_ethereum_virtual_machine_performance | optimizations]], the EVM space still presented a vast opportunity for significant performance improvements <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The realization that there were "a ton of optimizations" to be made in the EVM space served as the primary driving force behind Monad's creation <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.