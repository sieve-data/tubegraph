---
title: comparing l1 and l2 solutions
videoId: iyn1RngsvZc
---

From: [[thepipeline_xyz]] <br/> 

The conversation delves into the fundamental differences and philosophies behind Layer 1 (L1) and Layer 2 (L2) blockchain scaling solutions, particularly contrasting them in the context of Ethereum, Solana, and [[manad_labs_execution_and_consensus_separation | Monad]].

## Understanding L1s and L2s
Layer 1 (L1) refers to the base blockchain itself, like Ethereum or Solana, which processes and finalizes transactions directly on its mainnet. Layer 2 (L2) solutions are built on top of L1s to improve their scalability and efficiency, often by processing transactions off-chain and then settling them back on the L1.

Mt emphasizes the importance of optimizing systems from the "bottom up" when building, much like designing a race car by focusing on the best possible engine first before refining other components [10:33:47]. He believes that the base layer (L1) is the "engine" and needs to be optimized as much as possible to efficiently leverage hardware and software [11:39:07]. This approach leads to less fragmentation and avoids "duct-tapy" or subpar scaling solutions [12:01:06].

## The L1 Approach: Solana and [[manad_labs_execution_and_consensus_separation | Monad]]
Solana's and [[manad_labs_execution_and_consensus_separation | Monad]]'s approach aligns with this "bottom-up" philosophy, optimizing the base layer for speed and efficiency [11:37:37].

### Key L1 Optimizations:
*   **Parallel Execution Methods**: Unlike Ethereum's single-thread execution model, which processes transactions sequentially (A then B then C, even if non-overlapping), Solana and [[manad_labs_execution_and_consensus_separation | Monad]] utilize [[parallel_execution_methods | parallel execution methods]] [13:39:07]. This allows multiple independent transactions (A, B, and C) to be processed simultaneously, significantly improving throughput [13:51:06]. This is a technical challenge on EVM chains due to the lack of advanced access lists, but [[manad_labs_execution_and_consensus_separation | Monad]] addresses this [17:19:00].
*   **Deferred Execution**: [[manad_labs_execution_and_consensus_separation | Monad]] specifically implements deferred execution [14:19:20]. Traditionally, Ethereum requires execution before consensus. However, [[manad_labs_execution and consensus separation | Monad]] recognizes that the transaction ordering already determines execution, allowing these processes to occur non-simultaneously and take advantage of the separation [14:26:00].
*   **Focus on Product**: Optimizing the L1 allows builders to focus on the product rather than worrying about underlying scalability or other complexities [12:46:00].

### Comparison with Ethereum's Strategy
Ethereum's scaling strategy has involved building L2s to compensate for its L1's limitations, which Mt likens to "compensating to make the car faster by working on the other parts" instead of optimizing the engine [11:17:00]. He acknowledges Ethereum "has to do it" because [[comparison_between_ethereum_and_solana | Solana]] learned from Ethereum's earlier mistakes regarding speed [11:24:00]. While Ethereum cares more about node accessibility for anyone to run a node, [[comparison_between_ethereum_and_solana | Solana]] optimizes for higher demand benefits, enabling applications like order books that aren't feasible elsewhere [08:50:00].

## Critiques of L2s and Their Marketing
Mt views L2s favorably from a "pure nerd perspective" for addressing bottlenecks in Ethereum's execution and compute [27:21:00]. He acknowledges they work for cases not requiring global state, such as small games where finality requirements aren't strict [27:33:00].

However, his primary concern isn't the L2 technology itself, but the marketing that often portrays L2s as the "only way forward" or a solution for "any and all problems" [27:57:00].

> "What I don't like is not so much l2s as as much as kind of the people who prone al2s who make it seem like al2s are the only way forward and that they will solve any and all problems and and and you know solve world hunger and and and you know save I don't know Universe from heat death" <a class="yt-timestamp" data-t="00:27:52">[27:52:00]</a>

He argues that:
*   **L1s are generally more flexible**: While L1s might be worse in some niche cases, they offer greater flexibility overall [28:19:00].
*   **Misleading narratives**: Public figures sometimes downplay the capabilities of scalable L1s to promote L2s, creating a false impression that L1s are universally slow and expensive [28:51:00].
*   **Stacking layers**: The idea of continually adding L3s on top of L2s raises questions about the efficiency of the initial design [29:32:00].
*   **Unrealistic fragmentation**: The claim that there will be an L2 for every website or thousands of L2s is unrealistic due to fragmentation and Ethereum's inability to handle such a load [29:50:00].

## The Case for [[manad_labs_execution_and_consensus_separation | Monad]] as an L1
Mt sees [[manad_labs_execution_and_consensus_separation | Monad]]'s decision to launch as an L1 as a "no-brainer" from a first-principles perspective [30:42:00]. The goal is to build decentralized applications that solve problems for users, which currently L2s struggle with due to being "quite permissioned and centralized and not very scalable" [30:52:00]. While L2s might eventually scale with sharding in three to five years, that's "a very long time to wait" for builders who want to create the best possible products now [31:07:00].

[[manad_labs_execution_and_consensus_separation | Monad]] offers a solution for developers who prefer the EVM but desire the scalability of an L1, without needing to adopt different programming languages like Rust (used in Solana) [31:36:00]. Furthermore, an L1 like [[manad_labs_execution_and_consensus_separation | Monad]] can always integrate L2s in the future or enable app chains, offering greater flexibility [31:41:00].

A significant advantage for [[manad_labs_execution_and_consensus_separation | Monad]] is the ability for existing EVM applications to be "copy and pasted" from Ethereum or other EVM chains, potentially providing immediate performance advantages [36:33:00]. This could generate momentum and lead the Ethereum community to reconsider scaling the L1 more directly [37:16:00].

## Coexistence of VMs
Mt firmly believes in the mutual existence of different blockchain virtual machines, such as the EVM (Ethereum Virtual Machine) and SVM ([[comparison_between_ethereum_and_solana | Solana]] Virtual Machine), stating it's "inevitable" [36:36:00].

### Why Multiple Tech Stacks are Inevitable:
*   **Historical precedent**: No single tech stack has ever dominated an entire industry (e.g., iOS vs. Android, Xbox vs. PlayStation, AWS vs. Google Cloud) [36:43:00].
*   **Developer choice**: Developers desire different options and tools [37:15:00].
*   **Different optimizations**: The EVM and SVM optimize for distinct aspects in a meaningful way [37:26:00]. For example, [[comparison_between_ethereum and solana | Solana]] enables features like on-chain order books that are not feasible elsewhere [37:50:00].
*   **Continuous evolution**: Technology evolves rapidly, and competition is fierce, especially in dynamic fields like blockchain [38:37:00].
*   **Specialized roles**: A modular future might see different layers handling specific functions (e.g., settlement on Ethereum, execution on Solana, data availability on other layers) [38:52:00].

Mt predicts the emergence of a third VM, possibly a Move VM, alongside the EVM and SVM [38:08:00]. He stresses that L1s will be easier for developers to work with and conceptualize in the long run [36:10:00]. While L2s may still have niche uses, the general proclamation that they are the sole "savior of crypto" is inaccurate [30:06:00].