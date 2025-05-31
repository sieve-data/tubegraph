---
title: Blockchain scalability and polkadot
videoId: npnbqnlQtoQ
---

From: [[when-shift-happens]] <br/> 

Gavin Wood, co-founder of Ethereum and creator of Polkadot, is a visionary behind [[the_evolving_landscape_of_web3_and_blockchain_technologies | Web3]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. His work addresses fundamental challenges in [[blockchain_and_coordination | blockchain]] technology, particularly concerning scalability and the creation of a more functional and secure decentralized web <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Polkadot's Core Achievement

Polkadot's greatest achievement to date is delivering a secure sharded blockchain <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>, <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>. This design aims to improve the economics of scale, allowing approximately 100 chains to be secured for the same cost as securing a single chain, which contrasts with designs where each chain must secure itself, such as Cosmos <a class="yt-timestamp" data-t="01:10:45">[01:10:45]</a>.

### The Problem with Sharding

Despite being a key achievement, sharding also represents Polkadot's biggest current problem <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, <a class="yt-timestamp" data-t="01:15:21">[01:15:21]</a>.

Sharding, a concept borrowed from database design, involves splitting a database (or a blockchain) into independent segments called shards <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>. While this allows for parallel operation and scalability, it poses significant challenges for services that require frequent and immediate interaction across these segments <a class="yt-timestamp" data-t="01:18:41">[01:18:41]</a>.

#### Synchronous vs. Asynchronous Composition
The core issue lies in the difference between synchronous and asynchronous composition <a class="yt-timestamp" data-t="01:23:02">[01:23:02]</a>:
*   **Asynchronous Composition:** This involves sending messages between shards, like Polkadot's XCM (cross-consensus message) <a class="yt-timestamp" data-t="01:19:51">[01:19:51]</a>. It works well for tasks like KYC (Know Your Customer) checks, where a slight delay is acceptable <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>.
*   **Synchronous Composition:** This is needed for applications requiring immediate interaction, such as decentralized exchanges (DEXes) <a class="yt-timestamp" data-t="01:22:14">[01:22:14]</a>. The back-and-forth messaging in sharded systems makes real-time, agile interactions "very difficult" or "basically impossible" <a class="yt-timestamp" data-t="01:22:38">[01:22:38]</a>, <a class="yt-timestamp" data-t="01:22:54">[01:22:54]</a>.

Wood uses the analogy of playing tag across different school playgrounds: it's hard to play effectively if players are stuck in separate areas and can only communicate via messages <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>. This highlights the inherent limitation of persistently splitting the blockchain state <a class="yt-timestamp" data-t="01:26:16">[01:26:16]</a>.

## Jam: A Solution for Scalability and Synchronous Composability

Gavin Wood's proposal to solve this complex problem is **Jam**, the Join-Accumulate Machine <a class="yt-timestamp" data-t="01:24:08">[01:24:08]</a>. Jam aims to provide synchronous composability while retaining scalability <a class="yt-timestamp" data-t="01:23:52">[01:23:52]</a>.

Jam's approach can be understood through the "ephemeral playgrounds" analogy <a class="yt-timestamp" data-t="01:24:19">[01:24:19]</a>:
*   Instead of fixed playgrounds (shards), Jam creates a broad play area where specific playgrounds can form and disappear quickly <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>.
*   It partitions players (smart contracts) on the fly, grouping those that need to interact closely <a class="yt-timestamp" data-t="01:26:35">[01:26:35]</a>.
*   These groups can then execute synchronously, allowing for complex, real-time interactions <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
*   Multiple such "constellations of smart contracts" can operate simultaneously in parallel, significantly increasing the number of interactions processed <a class="yt-timestamp" data-t="01:27:58">[01:27:58]</a>.

Essentially, Jam removes the persistent splitting of the blockchain state, allowing for agile, on-the-fly partitioning of smart contracts in a large, shared "crucible" <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. This aims to enable hundreds of times more interactions <a class="yt-timestamp" data-t="01:28:08">[01:28:08]</a>.

### Polkadot as a Native Rollup Host Chain

Polkadot can be characterized as a native rollup host chain <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>. The technology developed for Polkadot, which might be seen as a piece of rollup technology, is not trivial to develop <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>. Jam, which Polkadot will eventually become, aims to evolve Polkadot from a multi-chain model (where parachains interact under a shared security umbrella) <a class="yt-timestamp" data-t="01:13:11">[01:13:11]</a> into a more general computation resource <a class="yt-timestamp" data-t="01:13:34">[01:13:34]</a>. This is analogous to how Ethereum transformed Bitcoin into a more general computation resource <a class="yt-timestamp" data-t="01:13:40">[01:13:40]</a>.

The goal for Jam is to create a "big shared computer that always works exactly how you expect it to" <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. On this shared computer, programs can be uploaded to run services, and crucially, these services can cooperate and coordinate with each other <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>. This unified, non-split architecture is key to achieving optimal interaction and scalability <a class="yt-timestamp" data-t="01:14:41">[01:14:41]</a>.

## Communication and Future Outlook

[[challenges_and_strategies_for_scaling_cryptocurrency_protocols | Blockchain scalability]] is a complex problem, and while Jam offers a potential solution, driving adoption requires effective communication and gaining attention in a competitive landscape <a class="yt-timestamp" data-t="01:28:27">[01:28:27]</a>. Polkadot has historically focused on attracting developers, achieving high developer adoption rates compared to other projects, with the exception of Ethereum <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

Gavin Wood emphasizes that Polkadot is built for the long run, focusing on core technology and adhering to the principles of [[the_evolving_landscape_of_web3_and_blockchain_technologies | Web3]], which prioritize strong, technology-based guarantees like privacy, rather than just short-term financial gains or corporate tie-ins <a class="yt-timestamp" data-t="01:38:09">[01:38:09]</a>. The success of Polkadot, in his view, means becoming the platform that provides [[the_evolving_landscape_of_web3_and_blockchain_technologies | Web3]] to the world <a class="yt-timestamp" data-t="01:38:45">[01:38:45]</a>. This depends on whether the world ultimately desires and recognizes the need for [[the_evolving_landscape_of_web3_and_blockchain_technologies | Web3]] principles, a shift that Wood believes is gaining momentum due to increasing distrust in centralized institutions <a class="yt-timestamp" data-t="01:39:51">[01:39:51]</a>.