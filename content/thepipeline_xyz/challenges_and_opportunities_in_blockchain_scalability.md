---
title: Challenges and opportunities in blockchain scalability
videoId: rXMlv51Mmsc
---

From: [[thepipeline_xyz]] <br/> 

Blockchain scalability refers to the ability of a blockchain to handle a growing number of transactions and users without compromising its core principles of decentralization and security <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. As the cryptocurrency space matures, addressing scalability concerns becomes paramount for mass adoption and the realization of blockchain's full potential <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.

## Current Landscape and Challenges

At the beginning of 2022, and continuing today, a significant challenge in the blockchain space has been the lack of focus on the core execution stack of virtual machines, particularly the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. While much attention has been directed towards [[scaling_blockchain_ecosystems | Layer 2 solutions]] like rollups, zero-knowledge proofs, and data availability improvements <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, the underlying performance of EVM execution has remained a less explored area <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Bottlenecks in Current EVM Infrastructure

The EVM, despite being the dominant standard for smart contracts with 98% of all TVL in crypto <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, faces several [[challenges_in_current_blockchain_infrastructure | fundamental bottlenecks]] that limit its composability and broader applicability:
*   **Sequential Execution:** The EVM historically processes transactions sequentially, meaning one after another, which creates a bottleneck for throughput <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **State Database Limitations:** The underlying state database, which stores all data in a Merkel tree, struggles to support many parallel reads and writes efficiently <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Gas Costs:** High gas costs practically limit the extent of composability envisioned by the original Ethereum developers <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Many ideas and applications become cost-prohibitive due to these fees <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Limited Composability:** While the EVM theoretically allows for deep cross-contract calls (up to 1,024 calls deep), practical gas limits make extensive composition expensive <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a> <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. For example, Solana's cross-program invocation depth is only three <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Security Trade-offs:** High gas costs force developers to make trade-offs, sometimes omitting additional defensive assertions or checks in smart contracts to save on fees, potentially reducing security <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.
*   **Mass Adoption Hurdles:** Current applications, while good for early adopters, cannot scale to the level of normal adoption due to high costs <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. User onboarding in crypto also faces significant hurdles, including learning about browser wallets, moving funds, and securing private keys <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>.

## Monad's Approach to Scalability

Monad Labs aims to address these [[challenges_in_blockchain_system_design | fundamental challenges]] by revamping the EVM's execution stack <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Their approach focuses on low-level systems engineering and first principles to introduce significant [[technical_challenges_and_solutions_in_blockchain_performance | performance optimizations]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Key Innovations

*   **[[Parallelization in blockchain technologies | Parallel Execution]]:** Monad introduces parallel execution, enabling the EVM to process multiple transactions concurrently <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This is supported by a high-performance state database designed for parallel reads and writes <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **EVM Compatibility:** By focusing on improving the EVM directly, Monad leverages the existing ecosystem of developers, tools, and research <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. This allows them to scale the base layer while benefiting from a rich research community and existing developer tooling <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.
*   **Reduced Gas Costs:** Substantially reducing gas costs allows for greater composability and enables developers to include more defensive assertions for enhanced security without cost penalty <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.
*   **Enhanced Composability:** Monad aims to enable infinite composition, allowing applications to build deeply on top of existing smart contracts without hitting practical gas limits <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Flexibility for New Features:** As an L1, Monad has the flexibility to add new opcodes or pre-compiles (e.g., for BLS or ZK-related functions) that can unlock new use cases like private smart contracts, without breaking backward compatibility <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Opportunities for Application Development

The performance and cost improvements brought by Monad create significant [[opportunities_for_application_development_on_highperformance_blockchains | opportunities for application development]] that were previously unfeasible <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

### Unleashing Blockchains' Potential

*   **True Composability:** The concept of "money Legos," where different DeFi protocols could seamlessly interoperate, can now flourish <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. This means developers can build complex applications by combining existing, tested smart contract primitives <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   **New NFT Standards:** More advanced NFT standards that include features like in-protocol royalty enforcement or loyalty program tracking, which were previously too expensive to implement, become viable <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **Consumer-Facing Apps:** The reduced costs make everyday applications feasible on-chain, such as event ticketing (e.g., concert tickets as NFTs) <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>, sports betting <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>, on-chain casinos <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>, and social applications <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.
*   **Data Sovereignty and Context-Aware Experiences:** Users can have their data stored securely in their wallets, enabling context-aware applications that service content based on wallet holdings, similar to personalized web2 experiences but with cryptographic security <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. This requires high throughput and low fees due to the large amount of data <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.
*   **Scalable Financial Products:** DeFi applications like money markets, decentralized exchanges, derivatives, and high-fidelity oracles can scale to millions of users, potentially replacing existing incumbent financial systems with open markets and lower fees <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.

## Future Potential and Adoption

The vision for Monad is not to compete with or replace Ethereum, but to expand the overall "pie" of blockchain usage by bringing in new users and enabling new use cases <a class="yt-timestamp" data-t="00:42:16">[00:42:16]</a>.

### Mass Adoption Strategy

*   **New User Acquisition:** A primary goal is to acquire new users from web2 by delivering compelling use cases and killer apps that drive adoption of decentralized technology <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>.
*   **Seamless UX/UI:** The aim is to create user experiences and user interfaces that are as intuitive as web2 applications, making it easy for web2 developers to transition and build on blockchain without immediately realizing they are using one <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
*   **Converging Ideals:** Monad seeks to bridge the gap between crypto natives, who are motivated by idealistic values, and web2 developers, who primarily want to build functional apps, by providing a platform where building is seamless <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.
*   **Continuous Innovation:** While performance is a key differentiator now, the long-term vision is for Monad to continuously push the limits of what's possible in terms of new behaviors, opcodes, and integrations, maintaining decentralization <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>. The combination of community, killer apps, research, and commitment to technological advancement will set Monad apart in the future <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.
*   **Industry Maturation:** As the industry matures, the focus will shift from attracting builders to ensuring the infrastructure can support sustained growth and enable applications to scale to many users while remaining decentralized <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>.
*   **Global Accessibility:** Efforts are needed to address challenges like funding for international builders and overall security practices in the adversarial crypto environment <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.

### Measuring Performance

Measuring blockchain performance, particularly Transactions Per Second (TPS), is often a source of confusion due to non-uniform definitions <a class="yt-timestamp" data-t="00:49:24">[00:49:24]</a>.

*   **True TPS:** It's important to distinguish between "real" transactions (smart contract interactions, transfers) and "voting transactions" (validator votes on each block) <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>. Monad will only count real transactions in its reported TPS <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>.
*   **Standardized Benchmarks:** To provide clarity, reproducible benchmarks with public GitHub repositories detailing the testing procedure are crucial <a class="yt-timestamp" data-t="00:50:49">[00:50:49]</a>. This allows for fair comparison of maximum possible transaction throughput across different systems <a class="yt-timestamp" data-t="00:49:49">[00:49:49]</a>.
*   **Beyond TPS:** A more accurate measure for real-world activity, especially considering varied transaction sizes, might be raw bytes per second propagated through the system, as this abstracts away conditional transaction definitions <a class="yt-timestamp" data-t="00:52:36">[00:52:36]</a>. The historical Ethereum transaction history can serve as a benchmark for real-life transaction composition <a class="yt-timestamp" data-t="00:52:56">[00:52:56]</a>.

The [[future_of_high_performance_and_scalable_blockchains | future potential of blockchain applications and adoption]] hinges on overcoming these scalability challenges, transforming the EVM into a much more performant and accessible platform <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.