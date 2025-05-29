---
title: Monads parallel execution for high throughput
videoId: wMa6GXjDyH4
---

From: [[thepipeline_xyz]] <br/> 

[[introduction_to_monad_and_its_capabilities | Monad]], with its fully bytecode EVM compatibility and underlying architectural changes, is designed to enable new types of applications that require high performance <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>. The core of its innovation lies in its approach to [[parallel_execution_methods | parallel execution]] and its custom-built database, which together achieve significantly higher throughput <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>.

## The Problem of State Access in Blockchains

The original vision for Monad was to create a more performant version of Ethereum's execution and consensus layers to build a superior engine for decentralized smart contracts <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>. Upon profiling existing Ethereum clients and other blockchain clients, it became evident that the single biggest bottleneck to performance was "State access" <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>.

Existing Ethereum clients, such as Go Ethereum (Geth), rely on inefficient commodity key-value stores like LevelDB for storing Merkle tree data <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>. While Merkle roots are crucial for commitments to global state and composability <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>, the storage method requires many lookups just to retrieve one piece of state, making it extremely inefficient <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. This inefficiency means that even if a hundred virtual machines (VMs) were running in parallel, they would still be bottlenecked by a single "pipe" for database access, limiting the benefits of parallelization <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.

## Monad's Solution: A Custom Database and Parallel Execution

To address the state access bottleneck, the Monad team embarked on a nearly year-long journey to build a new custom database <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. This database is designed with two key properties:
1.  **Natively Optimized Merkle Tree Storage**: It stores Merkle tree data in a custom data structure specifically optimized for that kind of data <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.
2.  **Asynchronous Reads and Writes**: The database supports asynchronous operations, which is crucial for parallel execution <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

With this custom database, Monad enables [[parallel_execution_methods | parallel access]] to different regions of the Merkle tree, allowing multiple virtual machines to progress much more efficiently and achieve significantly higher performance <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>. The approach is rooted in benchmarking and identifying bottlenecks to engineer specific solutions for performance <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>.

## Impact and Future Outlook

Monad's architecture, particularly its [[parallel_execution_methods | parallel EVM]], is poised to deliver a throughput of 10,000 transactions per second (TPS) <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. This high performance can enable applications that are not feasible elsewhere, such as:
*   Fully on-chain order book trading <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.
*   Highly interactive social applications and games <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.
*   Decentralized finance (DeFi) becoming the standard for personal finance <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

High throughput is critical for crypto to compete with traditional financial systems, especially in areas like payments and personal finance <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Reducing transaction costs and slippage (currently common at 1-5% in DeFi) to single-digit basis points requires a performant environment where market makers can quote tightly and compete the spread down, leading to better execution for users <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

The goal is to shift user and developer expectations, normalizing extremely low transaction costs (e.g., $0.00001 per trade like on Solana) <a class="yt-timestamp" data-t="00:49:29">[00:49:29]</a>. This change in "normalcy" will not only attract more users but also allow developers to build more robust protocols without fine-tuning for gas costs, potentially mitigating security risks <a class="yt-timestamp" data-t="00:50:28">[00:50:28]</a>. This renormalization will pave the way for a new wave of applications and users to fully leverage decentralized technology <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>.