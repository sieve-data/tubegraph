---
title: Challenges and innovations in blockchain development
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

Monad's public testnet launch marks a significant step forward, showcasing technology built from the ground up to address fundamental [[current_challenges_and_opportunities_in_blockchain_scaling | scaling challenges]] in blockchain [00:00:02] [00:01:23]. This initiative is viewed not as a finish line, but as a starting line for continuous innovation [00:00:26] [00:48:55].

## Building from Scratch

Monad has taken a unique approach by building its protocol entirely from scratch, rather than forking existing open-source projects [00:01:46] [00:01:59]. This decision was driven by the need for greater technical control over the product [00:02:06] [00:02:58].

Advantages of building from scratch include:
*   **Technical Control:** Being able to be very particular about implementation details, such as memory allocation or disk interaction, to optimize performance [00:02:41] [00:03:06].
*   **Avoiding Friction:** Existing open-source projects, like the EVM, would require so many modifications that leveraging their ongoing maintenance or new features would become impractical [00:02:19] [00:02:39].

The historical reason other projects haven't taken this high-performance, ground-up approach for EVM chains is largely due to Ethereum's design, which is "arbitrarily rate limited" for low node requirements [00:04:04] [00:04:15]. Monad, in contrast, was envisioned as a high-performance EVM chain from the outset, with no design restrictions other than 100% EVM compatibility [00:04:21] [00:04:38].

Building such a system is incredibly difficult, requiring highly specialized low-level system engineers who are rare in the crypto space, often working in big tech, silicon manufacturing, or high-frequency trading firms [00:05:12] [00:05:57].

## Technical Challenges and Innovations

The primary [[challenges_in_building_and_adopting_new_blockchain_technologies | challenges in building Monad]] revolved around optimizing for concurrent execution and efficient database interaction [00:06:16] [00:07:05].

### Concurrent Execution and Pipelining
Modern machines feature multiple cores, but most existing blockchain clients are single-core for transaction execution [00:06:22] [00:06:32]. A key innovation in Monad is leveraging these cores for concurrent execution [00:06:34].

Transactions within a block often have dependencies, making true parallel execution complex [00:06:36] [00:06:46]. Monad addresses this through **pipelining**, where multiple steps of different transactions are processed simultaneously, akin to a washing machine, dryer, and folding station working on different loads at once [00:06:47] [00:08:42]. This keeps the CPU constantly busy, minimizing idle time [00:07:50] [00:08:03].

### Database Performance Optimization
One of the most impactful areas of innovation is in [[challenges_in_blockchain_database_performance_optimization | database performance optimization]] [00:07:10] [00:08:10]. Disk access is a significant bottleneck (around 30 microseconds per access), and sequential operations quickly accumulate delays [00:07:12] [00:07:43]. Monad built its own database to ensure the CPU is always active, minimizing waiting for disk access [00:08:06] [00:08:10].

Keone Han uses the analogy of early airplanes (zero to one innovation) versus modern, highly optimized jet planes (one to hundred optimization) to describe Monad's work [00:09:43] [00:11:07]. Ethereum achieved the "zero to one" by enabling smart contracts and permissionless global finance, but with a lot of "slack" in the system [00:11:11] [00:11:49]. Monad focuses on the "one to hundred" by implementing performance engineering to achieve much higher throughput and cheaper transactions [00:11:59] [00:12:06].

## Benchmarking and Industry Misconceptions

There are significant challenges in evaluating blockchain performance due to misleading marketing and varied benchmarking methodologies [00:22:41] [00:25:01].

*   **Misleading TPS Metrics:** Simple native token transfers or ERC-20 contract transfers are easily achievable at high TPS (e.g., 50k TPS on single-core clients with artificial benchmarks) [00:19:51] [00:20:41]. Monad's 10k TPS benchmark, however, is based on replaying real Ethereum history, including complex transactions like AMM trades, lending protocols, and gas-expensive ZK proofs, which are far more taxing on a system [00:16:29] [00:21:26] [00:22:12] [00:22:38].
*   **Hardware and Geographic Location:** Benchmarking can be manipulated by using high-end server machines, having all nodes geographically collocated, or concentrating stake weight in one location, which can artificially boost reported performance by reducing network latency [00:23:02] [00:23:27] [00:24:13] [00:26:40]. Monad intentionally tests with geographically distributed, highly stake-weighted nodes to optimize for worst-case conditions and adhere to the laws of physics [00:25:40] [00:26:31].

Monad rejects these misleading practices, focusing instead on using technology to genuinely push the decentralization-performance trade-off curve forward [00:24:21] [00:24:59].

## Unlocking New Applications and Future Vision

Monad's high-performance EVM chain offers a performant version of shared global state with built-in payment rails and programmability, allowing applications to scale to millions or hundreds of millions of users [00:13:06] [00:13:22].

New application verticals enabled by Monad's performance include:
*   **High Fidelity DeFi:** Enabling personal finance at scale with cheap transaction fees and low slippage, leading to more efficient, fully on-chain markets [00:13:48] [00:14:14].
*   **Consumer-Facing Applications:** Any consumer app needing to scale to hundreds of millions of users and requiring high throughput (e.g., over a billion transactions per day) can leverage Monad's capabilities [00:14:22] [00:14:35].
*   **Decentralized Physical Infrastructure Networks (DePIN):** High performance and low transaction costs make it feasible for applications to sponsor gas fees, enabling business models in areas like health data marketplaces or networks for consumer-contributed compute (CPU/GPU) or camera data [00:37:30] [00:38:46] [00:39:22].
*   **Unpredictable Use Cases:** Just as bandwidth improvements led to YouTube and Instagram on the internet, Monad anticipates new, currently unpredictable applications (e.g., AI agents, NFT mints) that will emerge due to the increased speed and lower cost [00:43:00] [00:43:47] [00:27:35] [00:30:40].

The public testnet is primarily a "showcase of the power of the technology" and the applications built upon it [00:33:38]. It's an opportunity for early testers and infrastructure providers to provide feedback, identify unexpected usage patterns, and help optimize the system further [00:17:19] [00:32:51]. The goal is a system that handles stress gracefully, even when pushed to its limits, avoiding frustrating user experiences like reverted transactions or RPC failures [00:29:05] [00:29:43].

Monad's launch is seen as a starting line, with a massive queue of ideas for future optimizations, rewrites, research, and new features like usability improvements, privacy enhancements, and further decentralization to support thousands of nodes [00:48:59] [00:50:06]. This commitment to continuous innovation is a long-term vision, inspired by years of experience in high-performance system development [00:50:15] [00:51:26]. The project aims to bring real, innovative technologies to market, rather than simply forking existing codebases with minor changes [00:52:35] [00:52:47].