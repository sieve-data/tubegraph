---
title: Innovation in blockchain technology and applications
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

The public testnet for Monad is going live, marking a significant milestone that is seen not as a finish line, but as a starting line for further innovation and growth in the blockchain space <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This launch showcases the technology that has been built over several years of dedicated work <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

## Monad's Foundational Approach

Monad has taken a unique approach by building its protocol from the ground up, rather than forking existing open-source projects like Ethereum <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. This decision was driven by the need for greater technical control over the product <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. While forking allows leveraging existing work, Monad found that the extent of necessary modifications would negate the benefits of ongoing maintenance and new features from the original project <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. Building from scratch enables precise control over implementations, such as memory allocation and disk interaction, to achieve optimal performance <a class="yt-timestamp" data-t="02:41:00">[02:41:41]</a>.

Historically, other projects haven't prioritized raw execution performance for EVM chains because Ethereum itself is arbitrarily rate-limited to low throughput to maintain low node requirements <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. In contrast, Monad was conceived as a high-performance EVM chain with the primary restriction being 100% EVM compatibility, aiming to maximize network and hardware performance while still targeting consumer-grade nodes costing around $1,000 <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

> [!NOTE] Challenges and skill set
> Building high-performance systems like Monad is exceptionally challenging and requires highly specialized low-level system engineers, who are typically found in large tech companies, silicon manufacturers, or high-frequency trading firms, rather than general web development <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. This unique skill set is crucial for developing such complex infrastructure <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

### [[Technical challenges and solutions in blockchain performance | Technical Challenges and Solutions]]

The main [[Technical challenges and solutions in blockchain performance | technical challenge]] is achieving concurrent execution to leverage modern multi-core machines, as most existing clients are single-core for transaction processing <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>. Dependencies between transactions within a block complicate concurrent processing, making it difficult to pipeline operations <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

A critical area of innovation is in database management, where waiting for disk access (which can take 30 microseconds or more) can severely bottleneck sequential operations <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. Monad's innovations focus on continuously keeping the CPU busy, particularly by optimizing for situations where it would otherwise wait for disk I/O <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>. This approach is likened to a "washing machine" analogy: instead of performing one load (wash, dry, fold) completely before starting the next, Monad pipelines these processes to handle multiple "loads" (transactions) concurrently, significantly increasing throughput <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.

The distinction is between building a system that merely "works" (like the Wright brothers' first airplane) and one that is highly "optimized" (a modern jet plane) <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. Ethereum provided the "zero-to-one" innovation of smart contracts and permissionless global finance <a class="yt-timestamp" data-t="11:11:00">[0:11:11]</a>. Monad focuses on the "next step": performance engineering to achieve much higher throughput and cheaper transactions <a class="yt-timestamp" data-t="11:59:00">[0:11:59]</a>.

## Benchmarking and Trust in Performance Metrics

Monad uses real Ethereum history to benchmark its performance, which provides a more accurate simulation of real-world usage compared to artificial benchmarks <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>. Simple native token transfers or ERC-20 transfers are easily achievable even by unoptimized, single-core clients (e.g., 50k TPS for Silkworm on early Ethereum history) <a class="yt-timestamp" data-t="20:12:00">[20:12:00]</a>. Benchmarking with such simple transactions is not considered interesting or indicative of true performance under complex conditions <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>.

Real Ethereum usage involves complex protocols like AMMs, lending protocols, and computationally expensive ZK proofs, which are far more taxing on a system <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>. Monad aims to handle this real, diverse usage <a class="yt-timestamp" data-t="22:34:00">[22:34:00]</a>.

> [!CAUTION] Misleading Marketing in Benchmarking
> There is a lot of misleading marketing in the blockchain space regarding performance <a class="yt-timestamp" data-t="22:41:00">[22:41:00]</a>. Projects can manipulate benchmarks by:
> *   **Transaction Nature**: Using simple, low-cost token transfers <a class="yt-timestamp" data-t="22:56:00">[22:56:00]</a>.
> *   **Hardware**: Using extremely high-end hardware <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>.
> *   **Node Location**: Geographically collocating nodes or centralizing stake weight in one location to reduce latency and bypass true decentralized consensus challenges <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>.

Monad rejects these practices, focusing instead on [[Technology focus and pragmatism in blockchain development | technological innovation]] to push the decentralization-performance tradeoff curve forward <a class="yt-timestamp" data-t="24:25:00">[24:25:00]</a>. They intentionally test under "worst-case" conditions, like having highly stake-weighted nodes geographically dispersed (e.g., Singapore and New York), to optimize for robustness and real-world physics limitations <a class="yt-timestamp" data-t="25:43:00">[25:43:00]</a>. Metrics should be questioned if they appear to violate the laws of physics, indicating a lack of decentralization <a class="yt-timestamp" data-t="26:35:00">[26:35:00]</a>.

## Applications Unlocked by Monad's Performance

Monad offers a performant version of shared global state with built-in payment rails and programmability, allowing developers to build applications for millions or hundreds of millions of users who already have on-chain assets and digital identities <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

Two specific verticals showing traction for [[opportunities_for_application_development_on_highperformance_blockchains | application development]] on Monad include:

1.  **High-Fidelity DeFi**: Enabling personal finance to scale to hundreds of millions of users with extremely cheap transaction fees and low slippage, allowing liquidity providers to create highly efficient, competitive on-chain markets <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.
2.  **[[emerging_consumer_apps_leveraging_blockchain_technology | Consumer-Facing Applications]]**: Any application targeting consumers that needs to scale to tens or hundreds of millions of users, requiring Monad's scale of over a billion transactions per day <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.

Monad represents a bet on [[future_potential_of_blockchain_applications_and_adoption | application builders]] leveraging this performant infrastructure <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>. The adoption of crypto applications and wallets is seen as consistently increasing, providing a strong foundation for future growth <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>.

High performance is also key to simplifying the user experience by enabling applications to sponsor gas fees <a class="yt-timestamp" data-t="37:02:00">[37:02:00]</a>. If gas is cheap, the cost burden on developers is reduced, making business models more sustainable and lowering the cost of entry for new types of applications <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>. Examples include Decentralized Physical Infrastructure Networks (DePINs) and marketplaces for health data or other device data, where consumers can contribute resources like compute or network access <a class="yt-timestamp" data-t="38:18:00">[38:18:00]</a>.

## Public Testnet: Goals and Future Outlook

The devnet phase provided crucial feedback from early testers and infrastructure providers, helping to identify and fix issues and anticipate new use patterns <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>. One team simulated 3 trillion gas of usage over a few hours on devnet, equivalent to approximately 30 days of Ethereum throughput, showcasing Monad's capacity even with complex, chunky transactions <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>.

The public testnet's goal is to:
*   **Exercise the Technology**: Gather real-world usage data to identify strengths, weaknesses, and areas for further optimization <a class="yt-timestamp" data-t="32:45:00">[32:45:00]</a>.
*   **Showcase Technology and Applications**: Demonstrate the power of Monad's technology and the applications built upon it <a class="yt-timestamp" data-t="33:38:00">[33:38:00]</a>.
*   **Generate Excitement**: Foster community engagement and enthusiasm by allowing users to interact with the platform <a class="yt=" data-t="00:33:52">[00:33:52]</a>.
*   **Attract Builders**: Draw in developers who have been waiting for a high-performance EVM-compatible chain to push the limits of what's possible in crypto <a class="yt-timestamp" data-t="35:31:00">[35:31:00]</a>.

The team anticipates encountering unexpected usage patterns, such as high-stress events like NFT mints or spamming by [[diversity_in_blockchain_and_AI_sectors | AI agents]], and aims for the system to degrade gracefully rather than fail completely <a class="yt-timestamp" data-t="28:03:00">[28:03:00]</a>. This includes ensuring all parts of the stack – RPC layer, validator layer, and consensus – are robust <a class="yt-timestamp" data-t="31:25:00">[31:25:00]</a>.

> [!IMPORTANT] Long-Term Vision
> For Monad, the launch of the testnet is not a finish line but a starting line <a class="yt-timestamp" data-t="48:41:00">[48:41:00]</a>. The project has a massive queue of ideas for optimizations, rewrites, new features (e.g., usability, privacy, greater decentralization), and ongoing research <a class="yt-timestamp" data-t="48:59:00">[48:59:00]</a>. The client will initially support hundreds of nodes, with a plan to scale to thousands to match chains like Ethereum and Solana <a class="yt-timestamp" data-t="49:31:00">[49:31:00]</a>. The core goal is to deliver high performance and full backward compatibility for EVM and RPC, which will unlock many use cases and attract builders <a class="yt-timestamp" data-t="51:06:00">[51:06:00]</a>.

The crypto space often undervalues [[Technology focus and pragmatism in blockchain development | technology]], prioritizing go-to-market strategies or minor changes to existing codebases <a class="yt-timestamp" data-t="51:41:00">[51:41:00]</a>. Monad believes that bringing truly [[startup_innovation_in_crypto | innovative technology]] to market is the fundamental starting point for broader impact and [[future_potential_of_blockchain_applications_and_adoption | crypto adoption]] <a class="yt-timestamp" data-t="52:35:00">[52:35:00]</a>. Just as the internet's increased bandwidth led to unpredictable but massive applications like YouTube and Instagram, Monad's faster, cheaper, and more scalable platform is expected to enable entirely new and currently unforeseen applications <a class="yt-timestamp" data-t="43:00:00">[43:00:00]</a>.

## A Call to Action for the Community

The public testnet is an opportunity for the community to get involved, as previous engagement was primarily off-chain through Discord, Telegram, and in-person meetups <a class="yt-timestamp" data-t="45:25:00">[45:25:00]</a>. This launch allows "terminally on-chain" users who focus on trading and using new apps to interact with Monad's innovations <a class="yt-timestamp" data-t="46:55:00">[46:55:00]</a>. The community is encouraged to try out the testnet, provide feedback, and contribute to growing projects and fostering new communities <a class="yt-timestamp" data-t="58:42:00">[58:42:00]</a>. This collaborative effort is essential for Monad to reach new heights and achieve unprecedented advancements in the blockchain space <a class="yt-timestamp" data-t="59:29:00">[59:29:00]</a>.