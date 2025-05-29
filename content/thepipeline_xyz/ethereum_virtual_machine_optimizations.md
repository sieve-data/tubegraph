---
title: Ethereum Virtual Machine optimizations
videoId: mee-5mcuvMU
---

From: [[thepipeline_xyz]] <br/> 

The inspiration for [[monads_highperformance_blockchain_features | Monad]] stemmed from a background in developing high-performance trading systems and a recognized need for more [[performance_optimizations_in_ethereum_virtual_machine_evm | performant EVM]] implementations in the blockchain space <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Background in High-Frequency Trading (HFT)

The founders of [[monads_highperformance_blockchain_features | Monad]] met in 2014 while working on a high-frequency trading team at Jump Trading <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Their role involved building complete trading systems from the ground up, designed to process large volumes of data packets from exchanges, make rapid trading decisions, and send orders back out swiftly <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This environment is extremely latency-competitive; the fastest system to decide and send an order wins the trading opportunity <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This competitive pressure led to continuous system improvements, focusing on shaving off latency and building highly [[optimization_strategies_for_blockchain_clients | performant systems]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Identifying the Need for EVM Optimization

In 2021, the team transitioned to Jump's crypto division, where they began working on DeFi projects, including Solana DeFi <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This experience highlighted a significant need for more [[blockchain_performance_optimization | performant blockchain]]s in general <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Crucially, they observed a specific demand for more [[performance_optimizations_in_ethereum_virtual_machine_evm | performant EVM]]s <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

The existing [[performance_optimizations_in_ethereum_virtual_machine_evm | EVM implementations]] were noted as being very inefficient and lacked the level of optimization seen in the high-frequency trading systems they had previously developed <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Their background was deemed ideal for tackling this problem, despite the understanding that it would require significant time and effort to build highly [[optimization_strategies_for_blockchain_clients | performant systems]] from the ground up <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

The direct interaction with both Solana and Ethereum further exposed the performance differences and the extensive [[performance_optimizations_in_ethereum_virtual_machine_evm | optimizations]] that could be made, particularly within the [[performance_optimizations_in_ethereum_virtual_machine_evm | EVM space]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This realization served as the primary inspiration for [[monads_highperformance_blockchain_features | Monad]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.