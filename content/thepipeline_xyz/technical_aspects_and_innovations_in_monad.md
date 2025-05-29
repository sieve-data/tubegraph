---
title: Technical Aspects and Innovations in Monad
videoId: d4Yj8lkPgPM
---

From: [[thepipeline_xyz]] <br/> 

The [[What is Monad | Monad]] project has been built on a foundation of specific technical design choices and innovations aimed at achieving high performance and compatibility within the cryptocurrency ecosystem <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Core Design Principles

### Layer 1 Blockchain Choice
While many projects were focused on creating Layer 2 blockchains in late 2021 and early 2022, the founders of [[What is Monad | Monad]], Keon and James, opted to develop a Layer 1 blockchain <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This decision was a deliberate choice for a better fit for their specific design goals, going "Upstream" against the prevailing trend <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### 100% EVM Compatibility
A key design choice, made in January 2023, was to achieve 100% EVM (Ethereum Virtual Machine) compatibility <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. Unlike some scaling solutions, such as ZK sync, which were only slightly EVM compatible and required code changes <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, Monad aimed for full compatibility down to the bytecode level <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This was considered important to allow seamless leverage of the extensive resources and collateral already built for the Ethereum ecosystem and other EVM chains <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. The initial proposal was 97% EVM compatible, but it was pushed to 100%, which was a relatively simple change, more of an "idea play" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a> <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Performance Benchmarks

### 10,000 TPS
A significant performance benchmark for [[What is Monad | Monad]] is its target of 10,000 Transactions Per Second (TPS) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This number was part of the initial pitch, aiming to be 10,000 times faster than Ethereum (which processes about 10 TPS) on similar hardware requirements <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This ambitious goal was conceptualized by proposing a thousand-fold increase in speed, achieved by a "10x at four different layers" approach <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a> <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. The focus is on achieving this performance across the full range of real Ethereum history transactions, while also maintaining a high degree of decentralization <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a> <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Parallel Execution on the EVM
One of the original and core innovations of Monad, frequently discussed since its inception, is parallel execution on the EVM <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a> <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>. This feature is fundamental to its ability to achieve high transaction throughput. The initial concept for the "parallel EVM" was humorously alluded to as being conceived while an "intern locked in the bathroom" <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a> <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>.