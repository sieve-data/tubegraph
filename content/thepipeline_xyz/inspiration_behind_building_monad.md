---
title: inspiration behind building Monad
videoId: mee-5mcuvMU
---

From: [[thepipeline_xyz]] <br/> 

The initial inspiration to build [[what_is_monad | Monad]] stemmed from the founders' extensive background in building highly performant systems and their subsequent observations within the blockchain space, particularly regarding the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Background in High-Frequency Trading

The co-founders, James and the speaker, first met in 2014 while working on a high-frequency trading team at Jump Trading <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Their role involved building a complete trading system from the ground up <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This system would process incoming data packets from exchanges, make rapid trading decisions, and then transmit orders back to the exchange <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The high-frequency trading environment is intensely competitive <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Success depends on the ability to decide and send orders faster than competitors to capture opportunities <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This competitive pressure, driven by latency, necessitated continuous iterations of system improvement to shave off milliseconds and build a highly performant architecture <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This experience honed their skills in building extremely optimized, ground-up systems <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Transition to Crypto and DeFi

By 2021, James and the team transitioned to the crypto division at Jump, where they began focusing on decentralized finance (DeFi) projects <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. James, in particular, spent about six months working on Pyth, which involved interacting with Solana DeFi <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

During this period, they identified a significant need for more performant blockchains generally <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, and specifically, a critical demand for a more performant EVM <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. They observed that existing EVM implementations were inefficient and lacked the level of optimization they had applied to their previous trading systems <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## The Confluence of Experience and Need

The founders recognized that their background in building highly optimized systems from the ground up was perfectly suited to address the performance challenges in the blockchain space <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. They understood the long-term commitment required for such optimizations <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

The initial inspiration for [[what_is_monad | Monad]] was thus a combination of their experience building performant systems for different tasks and their direct interaction with platforms like Solana and Ethereum <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. They noted the performance differences and the extensive optimization potential within the EVM space <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This realization that there were a "ton of optimizations" to be made in the EVM space became the primary driver for creating [[what_is_monad | Monad]] <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.