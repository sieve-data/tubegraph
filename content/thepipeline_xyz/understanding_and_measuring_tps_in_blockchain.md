---
title: Understanding and measuring TPS in blockchain
videoId: E3vwu96YzJ8
---

From: [[thepipeline_xyz]] <br/> 

Transactions per second (TPS) is a common metric used to measure [[performance_gains_in_blockchain_transactions | blockchain performance]] <a class="yt-timestamp" data-t="03:55:53">[03:55:53]</a>. However, the definition and measurement of TPS can be confusing and misleading due to the lack of a universal standard <a class="yt-timestamp" data-t="03:24:19">[03:24:19]</a>.

## Challenges in Defining TPS
There is no standardized way to measure TPS across different blockchains, similar to how there are universal units of measurement like inches or centimeters <a class="yt-timestamp" data-t="03:28:13">[03:28:13]</a>. This absence of a standard allows for the metric to be artificially boosted using simplified environments or transaction data <a class="yt-timestamp" data-t="03:40:24">[03:40:24]</a>.

### Transaction Complexity
Transactions on a blockchain can vary significantly in their complexity <a class="yt-timestamp" data-t="04:01:21">[04:01:21]</a>. Some transactions can be extremely complex, time-consuming, and computation-intensive, while others are very quick <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.

An example of a simple transaction is a "transfer," which involves exchanging digital asset balances from one wallet address to another <a class="yt-timestamp" data-t="04:10:48">[04:10:48]</a>. If TPS is measured solely based on these simple transfer transactions, it can result in a high, artificial number <a class="yt-timestamp" data-t="04:27:14">[04:27:14]</a>.

### Theoretical vs. Real TPS
The concept of a "theoretical TPS" or "maximum TPS" refers to the highest number of transactions a chain could potentially produce under ideal scenarios, such as transfer-only scenarios <a class="yt-timestamp" data-t="04:40:24">[04:40:24]</a>. However, transfer-only scenarios do not accurately reflect real-world data <a class="yt-timestamp" data-t="04:55:20">[04:55:20]</a>. Modern blockchains host numerous applications and smart contracts that require much more complex transactions than simple transfers <a class="yt-timestamp" data-t="04:57:48">[04:57:48]</a>.

> [!WARNING] Artificial TPS
> Relying on theoretical TPS figures based on simple transactions can be misleading, as they do not represent the actual [[differences_in_blockchain_transaction_metrics | performance gains in blockchain transactions]] or the complexity of real-world blockchain activity <a class="yt-timestamp" data-t="04:27:14">[04:27:14]</a>.

## Monad's Approach to Measuring TPS
Monad aims to provide a "real TPS" metric that is in direct opposition to theoretical TPS <a class="yt-timestamp" data-t="05:15:20">[05:15:20]</a>. To achieve this, Monad defines and measures TPS by using:
*   **Real Historic Data**: This provides a more realistic and accurate view into true [[performance_gains_in_blockchain_transactions | blockchain performance]] and what users can expect <a class="yt-timestamp" data-t="05:22:04">[05:22:04]</a>.
*   **Recent Ethereum Data**: Monad replays real and recent Ethereum data that has been published on-chain <a class="yt-timestamp" data-t="05:46:42">[05:46:42]</a>. This is possible because Monad is an EVM (Ethereum Virtual Machine) compatible chain, allowing applications deployed on Ethereum to also run on Monad <a class="yt-timestamp" data-t="05:56:06">[05:56:06]</a>.
*   **Emulating Current Environments**: Using recent Ethereum transactions helps emulate what a current blockchain environment looks like, contrasting with the early days of Ethereum which predominantly saw simple transfer transactions <a class="yt-timestamp" data-t="06:14:02">[06:14:02]</a>.

This methodology provides a more usable and accurate expectation of Monad's TPS <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. The goal is to demonstrate the True Performance Optimization that Monad brings to an EVM environment by replaying current user activity from the most active environment directly on Monad <a class="yt-timestamp" data-t="07:15:05">[07:15:05]</a>.

> [!INFO] Monad Devnet
> Monad's devnet, a fully functioning blockchain environment, signifies the unification of all four optimizations of its tech stack: the consensus engine (MonadBFT), the execution engine (parallelized execution), and their interactions through Monad DB <a class="yt-timestamp" data-t="02:01:21">[02:01:21]</a>. The devnet currently achieves 10,000 TPS on the EVM <a class="yt-timestamp" data-t="03:00:15">[03:00:15]</a>.
>
> Devnet is currently an internal core team environment <a class="yt-timestamp" data-t="02:40:48">[02:40:48]</a>. The next milestone will be a phased testnet, which will be accessible to the public <a class="yt-timestamp" data-t="02:49:03">[02:49:03]</a>.