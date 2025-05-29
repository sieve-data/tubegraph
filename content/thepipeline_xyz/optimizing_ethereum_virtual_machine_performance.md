---
title: Optimizing Ethereum Virtual Machine performance
videoId: rXMlv51Mmsc
---

From: [[thepipeline_xyz]] <br/> 

Monad Labs is dedicated to making [[optimizing_evm_implementations | Ethereum Virtual Machine (EVM) execution]] significantly more performant. This commitment stems from the belief that someone needs to focus on the core execution stack of the EVM, especially given its dominant position as the standard for smart contracts with 98% of total value locked (TVL) in crypto <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

## Why Revamp the EVM?

When Monad Labs began in early 2022, the focus was already on addressing the [[technical_challenges_and_solutions_in_blockchain_performance | execution stack]] and making EVM execution more performant <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. At the time, less attention was paid to this area compared to other [[scaling_solutions_for_the_ethereum_virtual_machine | scaling solutions]] like rollups or zero-knowledge proofs <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

Key areas of focus for [[monads_unique_approach_to_blockchain_performance | Monad's unique approach to blockchain performance]] include:
*   **Introducing [[parallel_evm_and_blockchain_optimizations | parallel execution]]** <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Developing a high-performance state database** for storing data in a Merkle tree, supporting many parallel reads and writes <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
*   **Addressing other bottlenecks** within the [[performance_and_scalability_of_evm_chains | Ethereum Virtual Machine]] <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.

> "I think it's just it's another area of blockchain scaling that's really needed and I think it's really needed in order to help um the ethereum virtual machine which is ultimately the dominant standard for smart contracts with 98% of all tvl um in crypto right now it's just really important for someone to do that." <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>

The challenge of making the EVM more performant is also seen as an "interesting challenging problem" <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

## Engineering Approach

Monad's team largely consists of individuals with extensive experience in building high-performance, low-latency systems <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. The approach involves a "fundamentals first principles" mindset <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>, applying best practices from 30 years of high-performance computing to blockchain <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

The [[blockchain_redesign_for_high_performance | blockchain redesign for high performance]] involves:
*   Expertise over the entire system's performance <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.
*   Delving into kernel-level optimizations <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>.
*   Treating the blockchain as a database, managing multiple threads, data storage on disk, and cache optimization for fast reads <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.

## Impact on Composability and Application Development

[[Performance and scalability of EVM chains | Performance and scalability of EVM chains]] directly impacts composability in the EVM. While the EVM theoretically allows for deep cross-program calls (1,024 calls deep), practical limits exist due to gas costs <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>. Monad aims to remove these practical limitations, enabling true composability <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

This [[performance_gains_in_blockchain_transactions | performance gains in blockchain transactions]] unlocks new possibilities:
*   **Full composability:** Developers can compose smart contracts almost infinitely without hitting gas limits, which is crucial for applications like account abstraction <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **New use cases:** Ability to add new opcodes or pre-compiles (e.g., BLS pre-compiled for privacy) that enhance the EVM without breaking backward compatibility <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.
*   **Expanded design space:** Existing battle-tested EVM code and products (like ERC-20, ERC-721) can be composed in new ways. For instance, advanced NFT standards with in-protocol royalty enforcement or loyalty tracking, currently cost-prohibitive, could become viable <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>.
*   **Reduced gas costs:** Lower gas costs mean developers can include more defensive assertions and security checks in their smart contracts, reducing the trade-off between security and cost <a class="yt-timestamp" data-t="34:03:00">[34:03:00]</a>. This allows for applications like on-chain event ticketing (NFTs as tickets) which are currently too expensive <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>.

Essentially, Monad seeks to accelerate the original Ethereum vision of building "anything" without the practical constraints imposed by existing gas costs <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.

## Focus on User and Developer Adoption

Monad operates as a developer platform, prioritizing going "where the developers are" (EVM community) and solving their pressing problems <a class="yt-timestamp" data-t="25:55:00">[25:55:00]</a>. This includes:
*   Pure EVM compatibility <a class="yt-timestamp" data-t="26:06:00">[26:06:00]</a>.
*   Making cryptographic functions easier and cheaper <a class="yt-timestamp" data-t="26:21:00">[26:21:00]</a>.
*   Increasing application security through VM behavioral changes (e.g., re-entrancy attack defense) <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>.

The **[[need_for_performant_blockchain | need for performant blockchain]]** is not just for existing users but for mass adoption:
*   **Bringing in new users:** The primary KPI is bringing new people into crypto and using decentralized apps, as simply moving existing users won't fill block space sufficiently <a class="yt-timestamp" data-t="42:53:00">[42:53:00]</a>.
*   **Delivering compelling use cases:** With killer apps that drive adoption despite current onboarding hurdles (e.g., wallet usage, funding, private key security) <a class="yt-timestamp" data-t="43:37:00">[43:37:00]</a>.
*   **Bridging Web2 and Web3:** Presenting examples of real use cases with a familiar UX/UI for Web2 developers to realize the potential of blockchain <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>. The goal is to enable a UX/UI experience that makes blockchain development on par with Web2, allowing developers to build apps without immediately hitting blockchain-specific limitations <a class="yt-timestamp" data-t="36:54:00">[36:54:00]</a>.

## Measuring Performance (TPS)

The concept of Transactions Per Second (TPS) as a metric is often debated and can be confusing due to non-uniform definitions across different blockchains <a class="yt-timestamp" data-t="48:50:00">[48:50:00]</a>.

Key considerations for TPS:
*   **Excluding "voting transactions":** In chains like Solana, voting transactions by validators are included in the advertised TPS, alongside actual user transactions (e.g., swaps, NFT mints) <a class="yt-timestamp" data-t="47:16:00">[47:16:00]</a>. Monad believes only real smart contract interactions and transfers should be counted <a class="yt-timestamp" data-t="48:21:00">[48:21:00]</a>.
*   **Defining a "transaction":** Different chains may count a single smart contract invocation that performs multiple sub-instructions as many "transactions," inflating their reported TPS <a class="yt-timestamp" data-t="49:05:00">[49:05:00]</a>.
*   **Capacity vs. Demand:** Current TPS often reflects demand, not the maximum capacity of a system <a class="yt-timestamp" data-t="49:52:00">[49:52:00]</a>.
*   **Reproducible Benchmarks:** The true solution is to establish reproducible benchmarks with publicly available GitHub repositories and full scripts for deploying servers and sending transactions, allowing for transparent comparison <a class="yt-timestamp" data-t="50:49:00">[50:49:00]</a>.
*   **Transaction size:** Transactions on different systems are "sized differently." A better benchmark might be raw bytes per second, as it abstracts away varying transaction complexities and payloads <a class="yt-timestamp" data-t="51:47:00">[51:47:00]</a>.

For Monad, the benchmark for performance comparison is the historical Ethereum transaction history, as it provides a proxy for real-life usage patterns <a class="yt-timestamp" data-t="52:56:00">[52:56:00]</a>.

While performance is a key differentiator for Monad now, the long-term vision is that other systems will also improve. Monad will continue to push the limits of what's possible, introducing new behaviors, pre-compiles, and opcodes, while maintaining a high degree of decentralization <a class="yt-timestamp" data-t="39:36:00">[39:36:00]</a>. In 10 years, Monad's differentiation will be a combination of its community, killer applications built on it, the evolving research community, and its commitment to technological advancement and decentralization <a class="yt-timestamp" data-t="40:06:00">[40:06:00]</a>.