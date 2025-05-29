---
title: scaling blockchain ecosystems
videoId: iyn1RngsvZc
---

From: [[thepipeline_xyz]] <br/> 

[[Challenges in current blockchain infrastructure | Challenges]] in blockchain ecosystems often revolve around [[challenges_and_opportunities_in_blockchain_scalability | scalability]], [[decentralization_in_blockchain | decentralization]], and usability. Engineers, such as MT from Helus Labs, emphasize a "bottoms-up" approach to building efficient systems, comparing it to designing a race car by optimizing the engine first [00:10:33]. This philosophy suggests that the foundational layer of a blockchain, the "engine," needs to be as performant as possible to avoid fragmentation and "duct tape" solutions at higher layers [00:11:42].

## Core Issues and Solutions in Blockchain Scaling

A primary [[challenges_in_current_blockchain_infrastructure | inefficiency]] in the Ethereum Virtual Machine (EVM) is its single-thread execution model [00:13:37]. This means transactions must be processed sequentially, even if they are unrelated [00:13:39]. Monad addresses this with [[parallelization_in_blockchain_technologies | parallel execution]] and deferred execution, allowing transactions to be processed concurrently [00:12:26].

Other [[challenges_in_current_blockchain_infrastructure | challenges]] include state growth problems, state access issues, and inefficient code on the EVM [00:14:02]. Monad aims to solve these by optimizing the base layer, which allows builders to focus on product development rather than underlying [[challenges_and_opportunities_in_blockchain_scalability | scalability]] concerns [00:14:46].

## [[Comparison between different blockchain platforms | Platform Comparisons]]: Solana, Ethereum, and Monad

### Solana (SVM)

Solana learned from Ethereum's early challenges, designing its base layer for speed from the outset [00:11:24]. It focuses on optimizing the software to leverage hardware efficiently [00:11:48]. Solana's design enables applications like order books, which are difficult to implement on other chains [00:17:50]. Solana also hosts numerous hackathons to foster its developer community [00:09:12].

### Ethereum (EVM)

Ethereum prioritizes making its nodes accessible to run for anyone globally [00:20:22], which aligns with a focus on [[decentralization in blockchain | decentralization]] [00:08:47]. However, this design choice can impact its raw throughput and cost [00:20:56]. Ethereum's validator profitability model also differs, with a focus on deflationary aspects of its token and early experimentation [00:23:44].

### Monad

Monad, while EVM-compatible, adopts a different approach by revamping the EVM to significantly enhance performance [00:13:09]. Its key innovations include:
*   **[[Parallelization in blockchain technologies | Parallel execution]]**: Allows non-overlapping transactions to run concurrently [00:12:26].
*   **Deferred execution**: Separates transaction ordering from execution, enabling optimizations [00:14:19].
*   **EVM compatibility**: Offers a high-performance EVM that allows developers to easily migrate or build decentralized applications (dApps) using familiar tools like Solidity [00:12:54], potentially providing performance advantages to existing Ethereum applications [00:36:33].

Monad's decision to launch as a Layer 1 (L1) rather than a Layer 2 (L2) is based on the principle of building a robust, decentralized, and scalable foundation from the ground up [00:30:40]. This approach allows developers to build high-performance products without waiting for future L2 scaling solutions like sharding [00:31:09].

## The Role of Layer 2s (L2s)

Layer 2s (L2s) are seen as viable solutions for specific use cases, particularly where global state is not needed or finality requirements are less strict, such as small games [00:27:33]. However, some critics argue against the narrative that L2s are the only way forward or that they solve all problems [00:27:57], especially when they become overly complex with "L3s" [00:30:06] or lead to fragmentation [00:30:01]. While L2s address Ethereum's bottlenecks, scalable L1s like Solana and Monad also offer efficient alternatives [00:29:10].

## Coexistence and the [[Future of blockchain cooperation and multichain ecosystems | Future of Blockchain Ecosystems]]

The [[future_of_blockchain_cooperation_and_multichain_ecosystems | coexistence]] of different blockchain platforms like EVM and SVM is inevitable, similar to how multiple tech stacks or console platforms exist in other industries (e.g., iOS/Android, Xbox/PlayStation, AWS/Google Cloud) [00:16:39]. Developers will choose platforms that best suit their needs [00:17:16].

While Solana and Monad are not simply Ethereum forks, they optimize for distinct functionalities [00:17:32]. The notion that [[future of high performance and scalable blockchains | high-performance blockchains]] only increase hardware requirements is a misconception; they also enable fundamentally different applications, such as on-chain order books [00:17:42].

The long-term vision for blockchain, as described by Vitalik Buterin, involves block production by high-hardware machines and verification by lighter machines using light clients [00:25:32]. Both Solana and Ethereum are moving towards this endgame, albeit through different paths [00:26:00]. This suggests that the current "trade-offs" regarding validator costs and throughput are short-term considerations in the broader [[development stages in blockchain networks | development stages]].

## Attracting Developers and Real-World Applications

Attracting and retaining developers is crucial for any blockchain ecosystem [00:15:19]. While the EVM benefits from a large existing developer base familiar with Solidity [00:33:16], newer chains like Solana (SVM) and Move are seeing increasing adoption [00:34:02]. Solidity is generally easier to write compared to Rust and functional programming used in Solana development [00:34:24]. Platforms like Helus aim to simplify the developer experience on high-performance L1s, allowing them to focus on product rather than infrastructure complexities [00:50:56].

The ability to "copy and paste" existing EVM applications onto Monad could significantly boost its adoption by bringing performance advantages to existing dApps [00:36:33].

The [[future of high performance and scalable blockchains | future of crypto]] will focus on building useful applications that solve real-world problems for users [00:45:08]. Key areas for growth include:
*   **Decentralized Finance (DeFi)**: Improving security and achieving greater efficiency closer to traditional finance [00:44:53]. Monad aims to enable better on-chain order books for enhanced capital efficiency [00:49:07].
*   **Payments**: Crypto offers a significantly easier way to send money globally, especially stablecoins like USDC [00:48:21].
*   **Real World Assets (RWAs)**: Tokenizing assets for more efficient and accessible finance [00:47:00].
*   **Decentralized Physical Infrastructure Networks (DePINs)**: Using tokens to bootstrap physical networks, enabling projects like decentralized mobile networks (Helium) or mapping services (Hivemapper) [00:47:34].
*   **Digital Identity** [00:48:55].

The growth of the ecosystem depends not just on technical advancements but also on social and economic factors, including community building, shared values, and market timing [00:38:28].