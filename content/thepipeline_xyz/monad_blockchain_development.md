---
title: Monad blockchain development
videoId: rXMlv51Mmsc
---

From: [[thepipeline_xyz]] <br/> 

Monad is a new layer-1 blockchain being developed by Monad Labs, aiming to significantly enhance the performance and capabilities of the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The project began in early 2022 with a core mission to address fundamental execution stack challenges that other [[scaling_blockchain_ecosystems | scaling blockchain ecosystems]] had not prioritized <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Core Mission and Approach

Keone, CEO of Monad Labs, emphasizes that the primary goal is to make EVM execution much more [[need_for_performant_blockchain | performant]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This involves:
*   Introducing optimizations like [[parallelization_in_blockchain_technologies | parallel execution]] <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   Developing a [[high_throughput_blockchains_and_infrastructure_challenges | high-performance state database]] that stores data in a Merkel tree, supporting many parallel reads and writes <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   Addressing other bottlenecks within the Ethereum Virtual Machine <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

At the time of Monad's inception, there was a relative lack of focus on the execution stack compared to efforts in rollups, zero-knowledge proofs, or data availability <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Monad believes that improving this aspect of [[scaling_blockchain_ecosystems | blockchain scaling]] is crucial, especially for the EVM, which remains the dominant standard for smart contracts, holding 98% of total value locked (TVL) in crypto <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The challenge of making the EVM more performant is also seen as an "interesting and challenging problem" akin to climbing a mountain "because it was there" <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

Kevin G, leading developer relations at Monad Labs, found Monad exciting because it takes a "fundamentals first principles approach" to the problem <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Many of Monad's strategies apply "best practices" from 30 years of high-performance computing to a blockchain, unlike other areas still in theoretical stages <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Team and Expertise

Monad Labs comprises approximately 25 people, a size that might surprise some for a layer-1 project <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This lean structure reflects a commitment to staying incredibly laser-focused on core problems <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. The engineering team predominantly consists of individuals with extensive experience [[building_blockchain_technology_from_scratch | building high-performance, low-latency systems]] <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Building a performant base layer system like a database (which the Monad blockchain partly is) requires expertise across the entire system's performance, sometimes necessitating kernel-level optimizations <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

Keone's background in high-frequency trading and Kevin's in low-level systems engineering (from companies like Qualcomm and Apple) provide foundational experience in optimizing systems for speed and efficiency <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Value Propositions for Builders

Monad offers compelling advantages for developers:

*   **Enhanced Composability**: Monad enables deep composability, significantly beyond limitations seen in other blockchains (e.g., Solana's CPI depth of three) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. The EVM's design allows for nearly infinite call depth, and Monad removes practical gas-related limits that hinder features like account abstraction <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Cost Efficiency**: By reducing gas costs, Monad eliminates cost-prohibitive barriers for complex dApps, allowing developers to implement richer functionality without worrying about excessive fees <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **EVM Flexibility**: As an L1, Monad has the flexibility to introduce new opcodes (e.g., for BLS pre-compiles) and other features that enable new use cases like base-layer privacy or private smart contracts, without breaking backward compatibility <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Unlocking Untapped Design Space**: The EVM ecosystem has a wealth of proven, solid existing code and products (e.g., ERC standards) that Monad's performance allows developers to compose and build upon, enabling "money Legos" to truly flourish <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. This opens up new possibilities for NFTs with in-protocol royalty enforcement or loyalty tracking, which are currently too expensive to implement broadly on existing chains <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **New Use Cases**: Monad envisions applications like event ticketing (where tickets are NFTs) <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>, mass-adopted DeFi products (money markets, decentralized exchanges, high-fidelity oracles) that can replace centralized incumbents <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>, and consumer-facing apps like sports betting, on-chain casinos, and social applications <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.
*   **Data Sovereignty**: Kevin G is excited about the potential for context-aware internet experiences where user data resides securely in their wallet. This enables personalized app experiences (like Amazon showing relevant products based on history) but on-chain, requiring [[high_throughput_blockchains_and_infrastructure_challenges | high throughput]] and low fees due to the large amount of data involved <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

Monad is essentially an acceleration of Ethereum's original concept, enabling anyone to truly build anything without the practical gas constraints that have limited the EVM for over a decade <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

## Comparison to Solana and EVM Focus

Monad's team has prior experience in the Solana ecosystem <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. While Solana offers impressive performance and low fees, its non-EVM compatibility creates a trickier developer experience <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. Monad chose the EVM route to support the highest number of developers by going where they already are and solving their pressing problems <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.

Kevin G highlights that Monad offers a path for the ideals of the EVM and Ethereum community to reach "product scale" <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. Monad aims to allow EVM apps to sit side-by-side with Solana apps, offering similar user experiences, making developer choice dependent on system needs rather than a limited set of options <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.

Monad benefits from the robust EVM research community, particularly in ZK research <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>. By scaling the base layer, Monad can leverage existing developer tooling and quickly adopt innovations like fully stateless blockchains if they emerge from research, without needing to rebuild everything from scratch <a class="yt-timestamp" data-t="00:31:47">[00:31:47]</a>.

## Challenges for Builders and Monad's Solutions

Current challenges for builders in the EVM environment include:
*   **Funding**: It remains challenging to attract funding, especially for international builders due to a US-biased investor community <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.
*   **Security**: [[building_blockchain_technology_from_scratch | Building decentralized applications]] is inherently more challenging from a security perspective due to constant probing by black-hat hackers <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>.
*   **Gas Costs vs. Security**: Developers currently face a trade-off between including additional defensive assertions (which cost more gas) and saving on fees <a class="yt-timestamp" data-t="00:34:11">[00:34:11]</a>. Monad's reduced gas costs will allow developers to prioritize security without prohibitive expenses <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.

Monad acknowledges the strength of the crypto community, which provides eager early adopters, unlike traditional tech startups <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>. To encourage Web2 developers, Monad aims to present examples of real use cases with UI/UX similar to Web2 applications, demonstrating that the technology has matured <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. The goal is to make blockchain development feel like "just building an app" <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>, allowing developers to focus on unique experiences and value propositions.

## Future Vision and User Acquisition

Monad believes that the next bull market will bring a surge of new builders <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>. The key is to have the right infrastructure to support these builders in creating apps that can scale to many users while remaining decentralized <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>.

Initially, [[monads_unique_approach_to_blockchain_performance | Monad's unique approach to blockchain performance]] will differentiate it <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>. Over time, as other systems improve, Monad will continue to push the limits of what's possible by introducing new behaviors, pre-compiles, opcodes, and integrations <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>. In 5-10 years, Monad's differentiation will stem from its [[Monad community and ecosystem | community]], killer apps, evolving research community, and unwavering commitment to technological advancement while maintaining a high degree of decentralization <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.

Monad's primary focus for user acquisition is on bringing *new* users into crypto, rather than simply attracting existing users from Ethereum <a class="yt-timestamp" data-t="00:42:43">[00:42:43]</a>. The team believes that growing the overall pie of blockchain users is essential for any [[high_throughput_blockchains_and_infrastructure_challenges | high-performance blockchain]] to achieve full block utilization <a class="yt-timestamp" data-t="00:42:52">[00:42:52]</a>. This requires delivering compelling use cases with killer apps and collaborating with other teams on better wallets, user experiences, and fiat on-ramps to ease the onboarding process <a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>.

## TPS Measurement and Performance Benchmarking

The discussion around Transactions Per Second (TPS) can be confusing due to non-uniform measurement practices across different blockchains <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>. Keone clarifies that Solana's advertised TPS often includes validator votes (about 2500 per second) in addition to actual user transactions (around 500 per second) <a class="yt-timestamp" data-t="00:47:16">[00:47:16]</a>.

Monad's approach to TPS measurement will focus solely on "real" transactions, such as smart contract interactions and transfers, excluding votes <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>. Other systems, like Aptos, might count a single smart contract invocation with multiple sub-instructions as many transactions, further distorting figures <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>.

A key challenge in comparing performance is distinguishing between a system's *current* transaction load (demand) and its *maximum possible* throughput (capacity) <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>. Testnet performance can also be misleading if it doesn't accurately reflect production environments <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>.

Monad advocates for reproducible benchmarks with publicly available GitHub repositories, allowing anyone to deploy servers globally and run scripts to verify transaction throughput tests <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>. This scientific approach ensures transparency and verifiability of performance claims <a class="yt-timestamp" data-t="00:51:27">[00:51:27]</a>.

Kevin G adds that transactions themselves can be "sized" differently across systems. While simple transfers are a good benchmark, real-world activities vary greatly. A better, more abstract metric might be "raw bytes per second" to account for varying transaction payloads <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a>. Monad plans to benchmark against historical Ethereum transaction history as a proxy for real-world activity <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>.