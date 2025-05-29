---
title: Understanding TPS Transactions Per Second in blockchain
videoId: E3vwu96YzJ8
---

From: [[thepipeline_xyz]] <br/> 

Transactions Per Second (TPS) is a common metric used to gauge [[Blockchain performance optimization | blockchain performance]] <a class="yt-timestamp" data-t="03:55:08">[03:55:08]</a>. However, the term "TPS" can be misleading and confusing <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a> for several reasons.

## Challenges in Measuring TPS

### Lack of Standardization
There is no universal or standardized way to measure TPS across different blockchain platforms <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. This lack of a consistent metric, unlike units such as an inch or a centimeter, makes it easy to artificially inflate TPS numbers <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

### Transaction Complexity
Transactions on a blockchain can vary significantly in their complexity <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>. Some transactions can be extremely complex, time-consuming, and computation-intensive <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>, while others, like simple transfers, are very quick <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. Transfers, which involve exchanging digital asset balances from one wallet address to another <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>, are the simplest form of transaction <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.

### Theoretical vs. Real TPS
*   **Theoretical TPS (or Maximum TPS)**: This refers to an artificial number representing the highest potential number of transactions a chain could process in ideal scenarios, such as those involving only simple transfers <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. However, transfer-only scenarios do not reflect real-world blockchain activity <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. Modern blockchains host numerous applications and smart contracts that require more complex transactions <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
*   **Real TPS**: This contrasts with theoretical TPS by accounting for the diverse and complex transactions observed in actual blockchain environments, not just simple transfers <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.

## Monad's Approach to Measuring TPS
Monad aims to provide a more accurate and realistic measure of TPS by:
*   **Utilizing Real Historic Data**: Monad measures TPS using real historic data to provide a far more realistic and accurate view of true [[Blockchain performance optimization | blockchain performance]] and what users can expect <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
*   **Replaying Ethereum Transactions**: Monad replays real and recent Ethereum transaction data on its own blockchain <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. This is possible because Monad is an EVM-compatible chain <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>, allowing applications deployed on Ethereum and other EVM environments to also run on Monad <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.
*   **Focusing on Recent Data**: By using more recent Ethereum transactions, Monad emulates what a current blockchain environment looks like <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. Early days of Ethereum primarily saw simple transfers, which contrasts with the complex smart contract interactions common today <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.

This method of using real, recent Ethereum data published on-chain provides a more usable and accurate expectation of Monad's TPS <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. It demonstrates how Monad's optimizations perform when processing the kind of user activity seen on the most active EVM environment <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.

## Monad Devnet
The Monad Devnet is a fully functioning blockchain environment specific to the Monad blockchain <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. It represents a significant milestone for the team, as it unifies all four optimizations of their tech stack, including the consensus engine (MonadBFT) and the execution engine (which enables [[Parallel Execution in Blockchain | parallelized execution]]) <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. Their interactions, through MonadDB, form a cohesive system <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

Devnet is currently an internal core team environment <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. The next milestone for public access will be the phased Testnet <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. One of the headlines for Devnet is its ability to achieve 10,000 TPS on the EVM <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Monad utilizes Devnet to "dog food" the blockchain, internally identifying system strengths and areas for further optimization <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>. This iterative approach is fundamental to software development and ensures continuous improvement <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.