---
title: Performance optimizations in Ethereum Virtual Machine EVM
videoId: rXMlv51Mmsc
---

From: [[thepipeline_xyz]] <br/> 

Monad is building a blockchain focused on revamping the [[evm_compatibility_and_innovation | EVM]] to introduce significant performance optimizations [00:01:35](<a class="yt-timestamp" data-t="00:01:35">00:01:35</a>). The team believes that someone needs to focus on the execution stack to make [[ethereum_virtual_machine_optimizations | EVM execution]] much more performant [00:02:02](<a class="yt-timestamp" data-t="00:02:02">00:02:02</a>). This effort aims to address bottlenecks within the [[ethereum_virtual_machine_optimizations | Ethereum Virtual Machine]] [00:03:33](<a class="yt-timestamp" data-t="00:03:33">00:03:33</a>) and enable new possibilities previously constrained by gas costs [00:13:59](<a class="yt-timestamp" data-t="00:13:59">00:13:59</a>).

## Key Optimization Strategies

Monad's approach involves several fundamental changes and [[optimization_strategies_for_blockchain_clients | optimization strategies]]:

*   **[[Parallel EVM and its impact on performance | Parallel Execution]]**
    The introduction of [[parallel_evm_and_its_impact_on_performance | parallel execution]] is a core optimization [00:09:12](<a class="yt-timestamp" data-t="00:09:12">00:09:12</a>). This is enabled by underlying components that support high-performance parallel processing [00:02:17](<a class="yt-timestamp" data-t="00:02:17">00:02:17</a>).
*   **High-Performance State Database**
    A [[importance_of_custom_databases_for_evm_optimization | high-performance state database]] is crucial for storing data in a Merkel tree while simultaneously supporting access for many reads and writes in parallel [00:02:22](<a class="yt-timestamp" data-t="00:02:22">00:02:22</a>). This includes dealing with storage on disk and keeping the right data in cache for fast reads [00:08:07](<a class="yt-timestamp" data-t="00:08:07">00:08:07</a>). Monad is building a database as part of its blockchain [00:07:47](<a class="yt-timestamp" data-t="00:07:47">00:07:47</a>), drawing on expertise in designing performant systems like MySQL or Postgres [00:07:53](<a class="yt-timestamp" data-t="00:07:53">00:07:53</a>).
*   **Addressing EVM Bottlenecks**
    Beyond [[parallel_evm_and_its_impact_on_performance | parallel execution]], Monad addresses other bottlenecks within the [[ethereum_virtual_machine_optimizations | EVM]] [00:02:31](<a class="yt-timestamp" data-t="00:02:31">00:02:31</a>).
*   **Low-Level Systems Engineering**
    The team applies a "fundamentals first principles approach" to the problem, utilizing best practices from 30 years of high-performance computing [00:04:03](<a class="yt-timestamp" data-t="00:04:03">00:04:03</a>). This involves expertise over the performance of the entire system, sometimes delving into kernel-level optimizations [00:07:32](<a class="yt-timestamp" data-t="00:07:32">00:07:32</a>).

## Impact of Optimizations

These optimizations are designed to enable new functionalities and enhance existing ones:

*   **Enhanced Composability**
    The [[ethereum_virtual_machine_optimizations | EVM]] theoretically allows for deep call stacks (e.g., 1,024 calls deep) [00:11:29](<a class="yt-timestamp" data-t="00:11:29">00:11:29</a>). However, practical limitations like gas costs have restricted this [00:09:45](<a class="yt-timestamp" data-t="00:09:45">00:09:45</a>). Monad aims to remove these gas constraints, allowing for much greater composability [00:10:09](<a class="yt-timestamp" data-t="00:10:09">00:10:09</a>). This will enable developers to build on "money Legos" and existing, tested [[ethereum_virtual_machine_optimizations | EVM]] code without hitting prohibitive gas limits [00:15:06](<a class="yt-timestamp" data-t="00:15:06">00:15:06</a>).
*   **Enabling New Use Cases**
    By reducing gas costs substantially, Monad can enable use cases previously impractical on Ethereum, such as event ticketing NFTs with rich metadata like in-protocol royalty enforcement or loyalty tracking [00:17:03](<a class="yt-timestamp" data-t="00:17:03">00:17:03</a>).
*   **Scaling Existing Business Models**
    The ability to scale existing applications to many more users will make many business models more viable [00:19:16](<a class="yt-timestamp" data-t="00:19:16">00:19:16</a>). This is critical for moving beyond "dog-fooding" crypto products to mass adoption [00:18:41](<a class="yt-timestamp" data-t="00:18:41">00:18:41</a>).
*   **Improved Security**
    Lower gas costs will allow developers to include more defensive assertions and invariant checks in their smart contracts without incurring prohibitively high fees, thus improving application security [00:34:03](<a class="yt-timestamp" data-t="00:34:03">00:34:03</a>).
*   **Better Developer and User Experience**
    Monad aims to provide a user experience akin to Web2 applications, making blockchain development accessible to Web2 developers [00:36:06](<a class="yt-timestamp" data-t="00:36:06">00:36:06</a>). The goal is for users not to even notice they are on a blockchain [00:37:19](<a class="yt-timestamp" data-t="00:37:19">00:37:19</a>).

## Monad's Stance on L2s and Solana

Monad's founders started in early 2022, opting not to build an L2 because they believed the execution stack needed focus [00:01:47](<a class="yt-timestamp" data-t="00:01:47">00:01:47</a>). While L2s and ZK proofs received significant attention, core [[ethereum_virtual_machine_optimizations | EVM execution]] was less prioritized [00:02:46](<a class="yt-timestamp" data-t="00:02:46">00:02:46</a>). Monad sees itself as solving a different, but equally needed, area of [[blockchain_performance_optimization | blockchain scaling]] [00:03:03](<a class="yt-timestamp" data-t="00:03:03">00:03:03</a>).

Regarding Solana, Monad acknowledges its "awesome tech" for enabling financial products with fractions of a cent fees and scaling to millions of users [00:22:34](<a class="yt-timestamp" data-t="00:22:34">00:22:34</a>). However, Solana's developer experience can be tricky due to its lack of [[evm_compatibility and innovation | EVM compatibility]] [00:22:50](<a class="yt-timestamp" data-t="00:22:50">00:22:50</a>). Monad aims to combine Solana-like performance with the familiar [[evm_compatibility_and_innovation | EVM compatibility]] that developers prefer [00:28:34](<a class="yt-timestamp" data-t="00:28:34">00:28:34</a>).

Monad's mission is not to threaten or replace Ethereum, but to complement it by enabling new modes of transactions that are much more plentiful and cheaper [00:42:16](<a class="yt-timestamp" data-t="00:42:16">00:42:16</a>). The goal is to grow the overall "pie" of crypto users rather than split existing users [00:45:34](<a class="yt-timestamp" data-t="00:45:34">00:45:34</a>).

## Team and Expertise

Monad Labs has a team of about 25 people, prioritizing a laser focus on core problems [00:06:10](<a class="yt-timestamp" data-t="00:06:10">00:06:10</a>). The engineering team primarily consists of individuals with extensive experience in building high-performance, low-latency systems, particularly in areas like high-frequency trading and low-level systems engineering [00:07:16](<a class="yt-timestamp" data-t="00:07:16">00:07:16</a>). This background is crucial for tackling the "really fundamental problems at a system level for the [[ethereum_virtual_machine_optimizations | EVM]]" [00:04:37](<a class="yt-timestamp" data-t="00:04:37">00:04:37</a>).

## Measuring Performance (TPS)

TPS (Transactions Per Second) is often a confusing metric in the blockchain space [00:48:52](<a class="yt-timestamp" data-t="00:48:52">00:48:52</a>):

*   **Voting Transactions**: In chains like Solana, reported TPS often includes validator votes, which are technically transactions but not user-initiated smart contract interactions [00:47:37](<a class="yt-timestamp" data-t="00:47:37">00:47:37</a>). Solana's "true TPS" for user activity is around 500 transactions per second, with votes making up an additional 2,500 or more [00:47:59](<a class="yt-timestamp" data-t="00:47:59">00:47:59</a>). Monad will only count real smart contract interactions and transfers in its reported TPS [00:48:21](<a class="yt-timestamp" data-t="00:48:21">00:48:21</a>).
*   **Instruction vs. Transaction**: Some chains, like Aptos or Sui, may count individual instructions as transactions, artificially inflating their TPS figures [00:48:57](<a class="yt-timestamp" data-t="00:48:57">00:48:57</a>).
*   **Capacity vs. Demand**: Observed TPS reflects current demand, not necessarily the system's maximum capacity [00:49:39](<a class="yt-timestamp" data-t="00:49:39">00:49:39</a>).
*   **Transaction Size and Complexity**: Transactions vary greatly in size and computational intensity. A better metric might be raw bytes per second for throughput, as it abstracts away the "conditionally defined" nature of a "transaction" across different blockchains [00:52:36](<a class="yt-timestamp" data-t="00:52:36">00:52:36</a>).

Monad advocates for reproducible benchmarks with publicly available GitHub repositories and scripts that define server deployments and transaction loads to ensure transparency and comparability [00:50:49](<a class="yt-timestamp" data-t="00:50:49">00:50:49</a>). For Monad, the benchmark is the historical Ethereum transaction history, as it represents real-life activity [00:52:56](<a class="yt-timestamp" data-t="00:52:56">00:52:56</a>).

## Long-Term Vision

While performance is Monad's unique edge now, the team acknowledges that all blockchains will likely become more performant over time through improvements and cross-pollination of ideas [00:38:52](<a class="yt-timestamp" data-t="00:38:52">00:38:52</a>). In 10 years, Monad's differentiation will come from:
*   Its community [00:40:12](<a class="yt-timestamp" data-t="00:40:12">00:40:12</a>)
*   Killer apps built on the platform [00:40:15](<a class="yt-timestamp" data-t="00:40:15">00:40:15</a>)
*   The evolving research community [00:40:18](<a class="yt-timestamp" data-t="00:40:18">00:40:18</a>)
*   A commitment to pushing technological limits [00:40:21](<a class="yt-timestamp" data-t="00:40:21">00:40:21</a>)
*   Maintaining a high degree of decentralization [00:40:26](<a class="yt-timestamp" data-t="00:40:26">00:40:26</a>)

Monad's immediate focus is to deliver "really performant, really accelerated, [[parallel_evm_and_its_impact_on_performance | parallel pipelined Ethereum Virtual Machine]]" [00:54:07](<a class="yt-timestamp" data-t="00:54:07">00:54:07</a>).