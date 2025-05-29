---
title: Ethereum compatibility and technology evolution
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

Monad Labs, founded by Keone and James, formerly of Jump Trading and Jump Crypto, is focused on improving the [[performance_and_scalability_of_evm_chains | performance and scalability of EVM chains]]. Monad aims to address the lack of reliable information about [[parallel_evm_and_blockchain_optimizations | parallel EVM]] and other essential optimizations needed for true performance gains in blockchain technology <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Monad's Approach to Parallel EVM and Optimizations

Monad Labs pushed the first [[parallel_evm_and_blockchain_optimizations | parallel EVM]] algorithm over a year and a half ago <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Their optimistic parallel execution algorithm aims to complete transactions in a shorter period while maintaining linear ordering within the block <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
The algorithm involves running transactions in parallel to generate pending results, which are then committed in the original order <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. If an input is invalidated during commitment, the transaction is re-executed, typically a "cheap" process due to cached inputs <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

However, Monad found that [[parallel_evm_and_blockchain_optimizations | parallel execution]] alone offered little improvement over serial execution <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The primary bottleneck was identified as state access, where transaction dependencies on accounts and slots are stored on SSDs <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Existing databases used by Ethereum and other EVM-compatible blockchains do not support parallel access, leading to a single-file execution bottleneck even with multiple virtual machines running <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This realization led Monad to pursue other optimizations, particularly at the state database level <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### The Custom State Database

The most expensive parts of blockchain operations include cryptography functions, hashing, and state access <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. The actual business logic in most smart contracts is relatively cheap compared to these operations <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. A single read from an SSD can take 80 to 100 microseconds or more, which is orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Multiple sequential reads, common in transactions, can lead to significant delays <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

Standard general-purpose databases like Pebble DB, RocksDB, LMDB, and MDBX are not optimized for blockchain state access <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. They often involve embedding one data structure inside another on disk, leading to expensive, multi-traversal requests <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. In contrast, Monad's custom database is designed specifically for how blockchain data is stored and accessed, extracting maximum [[technology_focus_and_pragmatism_in_blockchain_development | performance from hardware]] like modern SSDs <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. For example, a modern SSD can perform 500,000 I/O operations per second <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>, but general-purpose databases often make 10-20 requests for a single lookup, whereas Monad's approach might only require one or two <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

### Separation of Execution and Consensus

Another key optimization by Monad is the separation of execution and consensus <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. By not requiring execution to complete before consensus, these processes can run in parallel, providing more time for both <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
In Ethereum, for example, within a 12-second block time, only about 100 milliseconds are allocated for execution, limiting the gas limit and amount of work that can be done <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. Moving execution out of being a prerequisite for consensus (e.g., running it in parallel to the next consensus round) provides a massive unlock for execution capacity <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. This approach doesn't restrict leaders from executing transactions before proposing a block but allows greater flexibility and budget for others to run them in parallel <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

## "No Shortcuts" Philosophy

Monad's "no shortcuts" philosophy emphasizes building performant systems from the ground up rather than relying on superficial fixes <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. A common shortcut is to "throw a bunch of hardware" at the problem, such as requiring very large amounts of RAM <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. While this might increase performance in the short term, it makes it harder and more expensive for regular people to participate in the network, hindering decentralization <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

Monad aims to run on commodity hardware, like a $200 modern SSD, while still extracting maximum performance <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. This approach, heavily influenced by their background in high-frequency trading (HFT), involves hyper-optimization at a granular level, including analyzing assembly instructions and optimizing low-level hardware interactions <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>.

Monad's development process is characterized by extensive experimentation and quantitative design <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. They avoid assumptions, even seemingly intuitive ones (e.g., that access lists are always beneficial for [[parallel_evm_and_blockchain_optimizations | parallel execution]]), by rigorously measuring and testing hypotheses <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>. This dedication often involves writing and discarding code, prioritizing robust, well-understood solutions over quick fixes <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>.

## EVM Compatibility and VM Differences

Monad is committed to full EVM compatibility down to the bytecode level <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>. This ensures that everything functions exactly the same as in Ethereum, avoiding "hiccups" or differences that can complicate contract deployment or RPC interactions <a class="yt-timestamp" data-t="00:36:28">[00:36:28]</a>.

There's a common misconception that the Virtual Machine (VM) itself (e.g., SVM, WASM vs. EVM) makes a huge difference in performance <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>. However, James notes that the differences between VMs like EVM and Java VM (which is decades old) are minor and don't intrinsically grant special capabilities <a class="yt-timestamp" data-t="00:37:47">[00:37:47]</a>.
Full EVM compatibility is primarily about tooling, developer experience, and seamless portability <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>. When developers don't have to worry about subtle differences, they can focus more on business logic and building for the consumer <a class="yt-timestamp" data-t="00:39:47">[00:39:47]</a>.

Ultimately, users value responsiveness and low latency <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. While there's a trade-off between throughput and latency in computer science, Monad aims to balance these to provide the best user experience <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

## Standardized Benchmarks and Industry Progress

The crypto industry lacks standardized benchmarks, allowing anyone to make performance claims without accountability <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. Claims of "200k TPS" often lack context about the type of transactions (e.g., simple token transfers vs. complex Uniswap or borrowing protocol interactions), making them potentially misleading <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.

Monad uses replaying recent Ethereum history as its internal benchmark <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>. They plan to release a public GitHub repository where others can download and replicate benchmarks for Monad and other chains <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. This initiative aims to improve the overall engineering and scientific rigor of the industry, moving away from intuition and marketing towards validated hypotheses <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>.

A significant "shortcut" that can "cheat" benchmarks is using excessively large amounts of RAM <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. While RAM is faster, it is two orders of magnitude more expensive than SSDs (e.g., 2 terabytes of RAM costs $20,000 compared to $200 for a 2TB high-quality NVMe SSD) <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. Jacking up RAM requirements doesn't scale, isn't decentralized, and would lead to increasing node requirements over time <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.

## Monad's Contribution to the Ethereum Ecosystem

Monad's goal is not to "kill Ethereum" but to meaningfully contribute to and expand the EVM ecosystem <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>. The Ethereum research community increasingly recognizes the value of Monad's unique approach: rebuilding the execution stack from the ground up, researching a custom database, and implementing optimizations like [[parallel_evm_and_blockchain_optimizations | parallel execution]] and asynchronous execution <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.

Ethereum has established a powerful bytecode standard with rich tooling, applications, and applied cryptography research within the EVM context <a class="yt-timestamp" data-t="00:54:20">[00:54:20]</a>. Monad leverages this existing work and explores new, orthogonal directions that aim to push the entire space forward <a class="yt-timestamp" data-t="00:54:42">[00:54:42]</a>. Monad hopes their advancements could even be incorporated into Ethereum itself, further pushing the boundaries of what's possible <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>. This exemplifies a collaborative approach to the [[future_of_blockchain_cooperation_and_multichain_ecosystems | future of blockchain cooperation and multichain ecosystems]].