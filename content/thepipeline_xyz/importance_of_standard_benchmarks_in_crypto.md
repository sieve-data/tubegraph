---
title: Importance of standard benchmarks in crypto
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

In the crypto industry, accurate and reliable information about performance gains is often lacking amidst marketing hype, particularly concerning concepts like the [[The importance of high throughput blockchains | parallel EVM]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The absence of standardized benchmarks makes it difficult to ascertain true performance and can lead to misleading claims <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.

## The Need for Standardization

Unlike other computer-related fields such as graphics cards or CPUs, which have standard benchmarks <a class="yt-timestamp" data-t="00:44:26">[00:44:26]</a>, the crypto space currently lacks consistent metrics <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. This allows projects to make broad claims without accountability, as there's no standard to hold them to <a class="yt-timestamp" data-t="00:44:58">[00:44:58]</a>.

For instance, Transaction Per Second (TPS) figures can be easily misunderstood. A client not highly optimized can still achieve 50,000 TPS for simple token transfers <a class="yt-timestamp" data-t="00:45:19">[00:45:19]</a>. Therefore, stating "200,000 TPS" without specifying the type of transactions (e.g., Uniswap vs. simple token transfers) provides no meaningful context and can sound deceptively impressive <a class="yt-timestamp" data-t="00:45:45">[00:45:45]</a>. It's akin to comparing someone doing 20 simple math problems a minute to someone doing one complex calculus problem a minute, without specifying the problem difficulty <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>.

## Challenges and Pitfalls in Benchmarking

### Superficial Optimizations
Some claims about performance, like simply implementing a [[The importance of high throughput blockchains | parallel EVM]], might sound impactful but yield little true performance gain on their own <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The actual bottleneck is often state access, which involves reading data from SSDs <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Relying solely on [[The importance of high throughput blockchains | parallel EVM]] without addressing underlying inefficiencies in the state database is like putting a Lamborghini body on a Toyota Corolla engine – it looks good but doesn't deliver significant performance <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Cheating Benchmarks with Hardware
A common shortcut to appear performant is to use excessive amounts of RAM <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. While RAM is faster, it is two orders of magnitude more expensive than SSDs (e.g., 2 terabytes of RAM costs $20,000 compared to $200 for a 2TB NVMe SSD) <a class="yt-timestamp" data-t="00:50:32">[00:50:32]</a>. This approach does not [[future_applications_and_scalability_in_the_crypto_space | scale]] well and undermines [[importance_of_decentralized_trustless_protocol | decentralization]] by increasing hardware requirements for participants <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.

### Invalid Assumptions
Assumptions about certain technologies, like access lists inherently improving [[The importance of high throughput blockchains | parallel execution]], are not always correct <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>. Rigorous measurement and experimentation are necessary to validate hypotheses, and often, intuitive ideas prove to be inaccurate <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

## Monad's Approach to Benchmarks

Monad Labs advocates for and will contribute to establishing industry-wide standardized benchmarks.

*   **Ethereum History as a Benchmark:** Monad uses recent Ethereum history as its internal benchmark to accurately measure performance <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>. This involves replaying real-world transaction data, which can take hours or even days for a full history <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.
*   **Publicly Available Benchmarks:** Monad plans to build a publicly available GitHub repository where others can download and replicate their benchmarks for various chains <a class="yt-timestamp" data-t="00:46:24">[00:46:24]</a>.
*   **Open and Reproducible:** The goal is to provide transparent and reproducible benchmarks, allowing the wider [[importance_of_crypto_community_support | crypto community]] to contribute, suggest improvements, or verify results <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>. This includes standardizing hardware specifications (e.g., 32 GB RAM vs. 256 GB RAM) for fair comparison <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>.

## Benefits of Standardization

Standardized benchmarks will bring much-needed rigor to the blockchain industry <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. They will:

*   **Increase Accountability:** Hold projects to their performance claims and prevent misleading marketing <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.
*   **Provide Context:** Allow for a clear understanding of what performance numbers actually represent <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>.
*   **Drive Progress:** Enable engineers to make informed, scientific decisions by identifying where optimizations are truly effective across different clients <a class="yt-timestamp" data-t="00:48:16">[00:48:16]</a>.
*   **Foster Transparency:** Promote a culture of open experimentation and shared knowledge, moving away from intuition-based marketing claims <a class="yt-timestamp" data-t="00:48:56">[00:48:56]</a>.

Ultimately, establishing robust benchmarks will improve the overall engineering standards of the industry and contribute to the space's advancement <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>.