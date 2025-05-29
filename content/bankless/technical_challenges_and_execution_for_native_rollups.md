---
title: Technical challenges and execution for native rollups
videoId: 0TOnHHnB6Ro
---

From: [[bankless]] <br/> 

Native rollups represent a design construction for an [[Ethereums Layer 2 Rollup Strategy | Ethereum]] rollup that aims to address the current heterogeneity and centralization issues within the rollup landscape <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. The core idea is to bake the security of [[Security and interoperability of Ethereum rollups | Ethereum]] rollups directly into the Layer 1 (L1) itself <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

## Current Problems in the Rollup Landscape

Before the concept of native rollups, [[Ethereum]]'s scaling strategy involved exporting the process to independent Layer 2 (L2) teams, each developing their own rollup code <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. This led to several issues:
*   **Heterogeneity**: Rollups possess different codebases, security assumptions, and compete to establish their own standards <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>. This creates a perception that L2s are distinct from [[Ethereum]] L1 <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   **Interoperability**: Different rollups, such as Optimism, Arbitrum, and Base, often have 7-day withdrawal windows due to their fault proof systems, making it difficult to transfer assets between chains <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Centralized Sequencers**: Many current rollups operate with centralized sequencers, posing a centralization risk and contributing to interoperability problems <a class="yt-timestamp" data-t="09:01:00">[09:01:01]</a>.
*   **Proof Systems and Security Councils**: Each rollup typically develops its own state transition function (STF) and proof system for validity to L1, which can lead to security vulnerabilities and lack of shared standards <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>. This also necessitates security councils, often multi-sigs, that govern upgrades and validity, introducing a single point of failure and potential for catastrophic events like chain drains <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

## Introducing Native Rollups

Native rollups aim to tackle the issue of non-homogeneous rollups by embedding their security directly into the L1 <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   **EVM Pre-compile**: The core mechanism involves an EVM pre-compile, specifically an "execute pre-compile" <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. A pre-compile is a complex instruction for the EVM that allows for "introspection"—the system having visibility into itself <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. This concept, initially proposed by Vitalik Buterin in 2017 as "EVM inside EVM," was meant to simplify Plasma designs and is now being revisited for rollups <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   **L1 Verification**: Instead of individual rollups (like Arbitrum, Optimism, Base) maintaining their own fraud proofs and security councils, the [[Ethereum]] L1 would directly verify the validity of its native rollups using this pre-compile <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. This allows L2s to discard their own proof code and security councils, leveraging L1-level security <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.

### How ZK Proofs Enable Scaling

While adding an execute pre-compile allows for L1 verification, it doesn't inherently scale [[Ethereum]] due to the block gas limit <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This is where ZK (Zero-Knowledge) proofs become crucial:
*   **Overcoming Gas Limits**: With ZK proofs, L1 validators don't need to re-execute all transactions within the pre-compile. Instead, they verify a ZK proof of the correct execution <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. This dramatically increases the effective L1 gas limit, potentially by 10x or 1000x, allowing for significant scaling <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.
*   **Real-time Proving**: The goal is to achieve "next-slot real-time proving," meaning proofs are generated fast enough to be verified within a 12-second slot <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. Current ZK VM technology shows promising progress, with proof generation costs in cents and latencies in minutes on single GPUs <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. Multi-machine proving with GPU clusters is expected to further reduce latency, aiming for 20-30 seconds, bringing it very close to the 12-second benchmark <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

## Transitioning to Native Rollups

### Technical Hurdles for Existing L2s
For existing rollups to become native, they face a significant technical challenge:
*   **Code Refactoring**: Current rollup designs often intertwine the user state transition function (EVM STF) with system-level code (blob handling, sequencer, governance) <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. To leverage the L1 execute pre-compile, L2s must refactor their code to achieve a clean decoupling of these layers <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

### Limitations for Non-EVM Chains
Native rollups are designed specifically for EVM-equivalent chains:
*   **VM Compatibility**: If a rollup uses a fundamentally different virtual machine (e.g., SVM, Move, Cairo, WASM), it is impossible for it to become native <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   **Trade-off with Customizability**: While native rollups offer enhanced security, they tie EVM-equivalent L2s to the L1 EVM's upgrade cycle <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. Historically, L1 EVM upgrades can be slow (e.g., Account Abstraction took years) <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. However, many L2s prioritize EVM equivalence and often correct course if they deviate, focusing customizability on non-EVM aspects like tokenomics, governance, or specialized sequencing (e.g., Uni Chain's flash blocks) <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

## Benefits and Incentives

The incentives for existing L2s to become native are substantial:
*   **Enhanced Security and Property Rights**: Native rollups extend [[Ethereum]] L1 security to the L2, eliminating reliance on security councils and reducing bug risks from EVM emulation <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. This provides "[[security_and_interoperability_of_ethereum_rollups | shared security]]" and stronger property right assurances, comparable to L1 <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. This can dramatically increase Total Value Locked (TVL) on rollups, as users would feel more comfortable holding assets there for extended periods <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   **Simplicity**: It collapses complex ancillary infrastructure like proving networks, watchtowers, and security councils into a single line of code that calls the pre-compile <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.
*   **Network Effects**: Native rollups foster network effects of security and composability, leading to more "money Legos" being built that are designed for maximum security and neutrality <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   **Quantum Security**: By removing the need for L2s to generate their own elliptic-curve-based proofs on-chain, native rollups inherently become post-quantum secure when the L1 validators upgrade their setup <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.
*   **Proof Aggregation**: Native rollups enable the aggregation of proofs across all native rollups by L1 validators, potentially leading to significantly lower gas costs for L2s to settle on L1 <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.
*   **[[Economic impact of native rollups on Ethereum | Value Accrual for ETH]]**: Native rollups are expected to increase demand for [[Ethereum]]'s data availability (DA) layer, as using the execute pre-compile requires using [[Ethereum]] DA. This stronger "lock-in" to [[Ethereum]]'s core services can significantly help ETH value accrual <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

## Timeline and Execution Challenges

The path to widespread adoption of native rollups involves significant [[Coordination and governance in Ethereums rollup roadmap | coordination and governance]] challenges:
*   **Lack of a Coordinator**: A major bottleneck is the absence of a dedicated champion to take full responsibility for the work, similar to how Tim Beiko championed EIP-1559 <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Hard Fork Process**: Implementing the execute pre-compile requires a hard fork, involving EIP (Ethereum Improvement Proposal) writing, discussion among all-core developers, and extensive testing on Devnets and Testnets. This process alone takes at least 12 to 18 months <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
*   **Accelerating Forks**: While [[Ethereum]] historically conducts one hard fork per year, there's an ambitious goal to shift to two forks per year to accelerate progress <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Phased Rollout**:
    *   **End of 2026 (Potential)**: Introduction of a "naive" execute pre-compile backed by re-execution. This version would have a small gas limit but could immediately benefit optimistic rollups in their fraud proof games <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.
    *   **Three Years Post-Naive Version**: A more advanced pre-compile, backed by SNARKs, is envisioned to dramatically increase the gas limit <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. This depends on several ingredients:
        *   Delayed state roots <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>
        *   A strong diversity of mature and real-time ZK VMs <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>
        *   Proposer-builder separation <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>

## [[Coordination and governance in Ethereums rollup roadmap | Social Coordination as a Bottleneck]]
The overarching challenge for [[Challenges in Ethereums upgrade processes | Ethereum]]'s progress, including native rollups, is consistently social coordination <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. While research and engineering capabilities are present, the decentralized nature of [[Ethereum]] means that delivering major upgrades to mainnet is bottlenecked by the need for consensus and coordination among various entities: L2 teams, execution layer clients, and researchers <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. New coordination efforts and strategies, such as the "beam chain" concept (focusing on R&D for years before entering the expensive social layer of governance), aim to address this fundamental issue <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.