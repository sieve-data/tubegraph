---
title: Challenges in blockchain system design
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

The launch of Monad's public testnet marks a significant step in addressing long-standing [[challenges_in_current_blockchain_infrastructure | challenges in current blockchain infrastructure]] and system design, particularly regarding performance and scalability <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While the community often views a testnet or mainnet launch as crossing the finish line, Monad considers it merely the starting line for continuous innovation <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Building from Scratch: A Unique Approach
Monad has adopted a unique strategy of building its protocol entirely from scratch, rather than forking an existing open-source project <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. This decision was driven by the desire for greater technical control over the product <a class="yt-timestamp" data-t="02:04:04">[02:04:04]</a>.

> "We feel that we would have modified so many things in the existing sort of Open Source projects that we wouldn't have leveraged been able to leverage like the ongoing new features or maintenance of those projects for Monad so it just didn't it just didn't really make sense from like an ongoing sort of St maintenance standpoint and new feature development standpoint." <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>
> — James Hunsaker, CEO & CTO at Category Labs

Building from scratch allows for specific implementation choices regarding memory allocation, disk interaction, and other low-level aspects to achieve optimal [[need_for_performant_blockchain | performance]] <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

### Why Others Haven't
Despite the Ethereum Virtual Machine (EVM) being over a decade old, few projects have undertaken a similar ground-up rebuild focused on [[high_throughput_blockchains_and_infrastructure_challenges | high throughput]] <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. Ethereum clients, like Aragon, have improved state sync performance, but not raw execution performance <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This is largely because Ethereum is arbitrarily rate-limited to maintain low node requirements, making a focus on raw throughput less relevant for its original design goals <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

Monad, however, was envisioned as a [[high_throughput_blockchains_and_infrastructure_challenges | high performance]] EVM chain from the outset, with few design restrictions beyond 100% EVM compatibility <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. The goal was to maximize network and hardware performance, while still targeting consumer-grade node requirements (e.g., a $1,000 PC) <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.

A major challenge in this endeavor is the scarcity of low-level system engineers, who typically work in big tech, silicon manufacturing, or high-frequency trading firms, rather than general web development <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

## Core [[Technical challenges and solutions in blockchain performance | Technical Challenges]] and Innovations
The primary [[technical_challenges_and_solutions_in_blockchain_performance | technical challenge]] in blockchain design is achieving concurrent execution <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>. While modern machines have many cores, most existing clients are single-core for transaction execution <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>. Blocks contain transactions with dependencies, meaning they are not a thousand independent tasks <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

Monad's key innovations revolve around:
*   **Pipelining**: Efficiently processing multiple transactions simultaneously, even with dependencies, by working on different stages of different transactions concurrently <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. This is likened to a "washing machine" analogy where washing, drying, and folding different loads happen in parallel <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
*   **Database Optimization**: Minimizing CPU idle time caused by slow disk access <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>. Disk access, even at 30 microseconds, adds up quickly across many transactions, leading to inefficient hardware utilization <a class="yt-timestamp" data-t="07:12:00">[07:12:12]</a>. Monad's custom database is designed to keep the CPU constantly busy <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.

This intense focus on optimization differentiates building a merely functional system from a truly high-performance one <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

## Benchmarking and Misleading Metrics
The blockchain space is rife with misleading marketing and benchmarks <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. Simple token transfers are the easiest for a blockchain to process, and even unoptimized, single-core clients can achieve 50k TPS on such artificial benchmarks <a class="yt-timestamp" data-t="19:51:00">[19:51:00]</a>. Monad rejects claims of high TPS based solely on token transfers because it's "easily achievable" and "not interesting" <a class="yt-timestamp" data-t="22:23:00">[22:23:00]</a>.

> "When somebody publishes like oh we're doing 10K TPS and you look and it's like token transfer it's like that's actually not I mean maybe some people are wild by that but I'm not Wild by that because I've seen it like even under even not so optimize clients or not parallel execution clients do 50k TPS on the sort of artificial benchmarks." <a class="yt-timestamp" data-t="20:22:00">[20:22:00]</a>
> — James Hunsaker, CEO & CTO at Category Labs

Monad's benchmarks are based on replaying real Ethereum history, which includes complex transactions from AMMs, lending protocols, and computationally expensive ZK proofs <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>. For example, a team simulating an exchange on Monad's devnet sent 3 trillion gas in a few hours, equivalent to about 30 days of Ethereum throughput <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>.

Other deceptive benchmarking practices include:
*   Using high-end, expensive hardware <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>.
*   Geographically co-locating nodes or concentrating stake weight in one area, creating an illusion of [[Decentralization in blockchain | decentralization]] and speed that doesn't hold up in a truly distributed network <a class="yt-timestamp" data-t="23:08:00">[23:08:00]</a>.

Monad, conversely, intentionally tests its algorithm under "worst-case" conditions, such as high stake-weighted nodes located far apart (e.g., Singapore and New York), to optimize for real-world [[security_and_decentralization_in_blockchain | decentralization]] and performance, respecting the laws of physics <a class="yt-timestamp" data-t="25:43:00">[25:43:00]</a>.

## Addressing [[User experience issues on blockchain platforms | User Experience]] and System Robustness
A significant [[challenges_and_opportunities_in_blockchain_scalability | challenge in blockchain scalability]] is ensuring graceful degradation under stress. During high-demand events like NFT mints or AI agent spamming, systems can fail, leading to reverted transactions, RPC errors, and user frustration <a class="yt-timestamp" data-t="28:35:00">[28:35:00]</a>.

> "You always see these sorts of things like oh the RPC thing failed or transaction getting reverted or all you know there's all these sorts of things that pop up on Twitter when something goes wrong and would be nice and not have to make those sort of excuses why things went wrong." <a class="yt-timestamp" data-t="28:47:00">[28:47:00]</a>
> — James Hunsaker, CEO & CTO at Category Labs

Monad aims for a system that, even when pushed to its limits, handles transactions gracefully, perhaps with a slight delay, rather than outright failing <a class="yt-timestamp" data-t="29:05:00">[29:05:05]</a>. This robustness across the entire stack, from RPC to validator and block propagation layers, is crucial for a positive [[user_experience_issues_on_blockchain_platforms | user experience]] <a class="yt-timestamp" data-t="31:25:00">[31:25:00]</a>.

Current blockchain [[user_experience_issues_on_blockchain_platforms | user experience issues]] also stem from fragmented protocols across multiple L2s or mainnets, making interactions painful and hindering general adoption <a class="yt-timestamp" data-t="40:49:00">[40:49:00]</a>. Monad seeks to improve this by providing a high-performance EVM-compatible base that enables seamless, cheaper transactions <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.

## Impact on Applications and Future Vision
Monad's high-performance, EVM-compatible shared global state, with built-in payment rails and programmability, unlocks new possibilities for developers <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

Key application verticals benefiting from Monad's design include:
*   **High-fidelity DeFi**: Enabling personal finance at scale with cheap transaction fees and low slippage due to efficient liquidity provision <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.
*   **Consumer applications**: Scaling to hundreds of millions of users, requiring Monad's capacity of over a billion transactions per day <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.
*   **DePIN (Decentralized Physical Infrastructure Networks)**: Lowering the cost of pushing data to chain to fractions of a cent, enabling new business models for marketplaces involving health data, compute (CPU/GPU), cameras, and other consumer hardware <a class="yt-timestamp" data-t="38:18:00">[38:18:00]</a>.

Simplifying the [[user_experience_issues_on_blockchain_platforms | user experience]] by abstracting away gas fees is also a key goal, which becomes economically viable for application developers when transaction costs are significantly reduced <a class="yt-timestamp" data-t="36:59:00">[36:59:00]</a>.

The Monad team views the public testnet as the start of a long-term commitment to innovation <a class="yt-timestamp" data-t="48:45:00">[48:45:00]</a>. They have a massive "queue of ideas" for optimizations, rewrites, research, new features (like usability and privacy), and further [[security_and_decentralization_in_blockchain | decentralization]] to support thousands of nodes <a class="yt-timestamp" data-t="48:59:00">[48:59:00]</a>. The core goal is to consistently push the [[security_and_decentralization_in_blockchain | decentralization]]-[[need_for_performant_blockchain | performance]] tradeoff curve forward <a class="yt-timestamp" data-t="24:40:00">[24:40:00]</a>.