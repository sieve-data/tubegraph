---
title: Coordination and governance in Ethereums rollup roadmap
videoId: 0TOnHHnB6Ro
---

From: [[bankless]] <br/> 

## The Challenge of Decentralized Scaling

[[ethereum_roadmap|Ethereum]]'s approach to scaling involves rollups, which has led to a landscape where its [[Ethereums Layer 2 Rollup Strategy|scaling strategy]] was "exported" to independent Layer 2 teams <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These teams developed their own rollup code, resulting in a "non-homogenated" ecosystem <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. While [[ethereum_roadmap|Ethereum]] has scaled with many different rollups, these rollups are not closely integrated with [[ethereum_roadmap|Ethereum]] itself <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. They possess different code, varying [[security_and_interoperability_of_ethereum_rollups|security assumptions]], and create competing standards <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This heterogeneity has fostered a perception that Layer 2s are distinct from [[ethereum_roadmap|Ethereum]], leading to numerous downstream problems <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

A core issue highlighted is that all of [[ethereum_roadmap|Ethereum]]'s problems ultimately "collapse back down to human coordination" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Outsourcing Scalability and Its Consequences

In 2020, [[ethereum_roadmap|Ethereum]] adopted its rollup-centric roadmap due to technological limitations at Layer 1 <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. This strategy involved outsourcing scalability research and development to VC-backed teams, which greatly benefited the ecosystem through investment in projects like Arbitrum and Optimism <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

However, this model introduced new challenges:
*   **Competing Standards:** Each organization developed its own solution, leading to multiple competing standards rather than a unified one <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Loss of Credible Neutrality:** The pursuit of individual dominance by rollups (e.g., Base wanting everything to settle on Base, Arbitrum on Arbitrum) risks eroding the credible neutrality of the [[ethereum_roadmap|Ethereum]] Layer 1 <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Centralized Sequencers:** Current rollups often rely on centralized sequencers, which creates a centralization vector and contributes to interoperability issues <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Proof System Diversity:** Every rollup independently develops its own state transition function and proof system to validate its validity to Layer 1, introducing security concerns and a lack of shared standards <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Security Councils:** Many rollups rely on security councils (multisigs) to govern upgrades to their proof systems, which acts as a single point of failure with significant responsibility <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Limited ETH Value Accrual:** The initial flexible and high-tolerance rollup constructions allowed Layer 2s to capture significant value without much accrual back to [[ethereum_roadmap|Ethereum]] Layer 1 <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.

## Native Rollups: A Strategic Shift

[[Ethereums scaling strategy with native rollups|Native rollups]] are a design construction that directly addresses the issue of non-homogenous rollups <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The core idea is to bake the [[security_and_interoperability_of_ethereum_rollups|security of Ethereum rollups]] directly into the Layer 1 itself, using an EVM pre-compile <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This would allow rollups like Arbitrum, Optimism, and Base to shed their own fraud proof code and security councils, instead using the Layer 1 pre-compile for [[security_and_interoperability_of_ethereum_rollups|Ethereum-level security]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

[[Ethereums future strategic direction|Native rollups]] aim to:
*   **Solve Bugs:** By allowing Layer 2s to "peek under the hood" into Layer 1 via introspection, they gain access to Layer 1's client diversity, mitigating emulation-introduced bugs <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Ensure Forward Compatibility:** They provide a pathway to trustless rollups, eliminating the need to trust a security council or governance token for compatibility with EVM upgrades <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Extend Ethereum's Social Consensus:** [[Ethereums scaling strategy with native rollups|Native rollups]] extend [[ethereum_roadmap|Ethereum]]'s social consensus, governance, and [[security_and_interoperability_of_ethereum_rollups|security]] over the critical parts of a rollup's stack <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Increase Network Effects:** They aim to increase network effects for [[ethereum_roadmap|Ethereum]] by providing composability (via based sequencing) and shared security <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.
*   **Enhance Property Rights:** By offering property right assurances equivalent to Layer 1, native rollups aim to increase the amount of ETH bridged and transacted on Layer 2s, which currently stands at only 2% of all ETH <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.
*   **Unlock New Security Levels:** They enable a "bright green" or "stage three" level of [[security_and_interoperability_of_ethereum_rollups|security]] on Layer 2Beat criteria <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.
*   **Simplify Infrastructure:** Much of the ancillary infrastructure (proving networks, watchtowers, security councils) required by current rollups collapses into a single line of code that calls the pre-compile <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.
*   **Quantum Security:** [[Ethereums scaling strategy with native rollups|Native rollups]] inherently offer quantum security because no proofs are put on-chain, automatically inheriting Layer 1's post-quantum upgrades <a class="yt-timestamp" data-t="01:06:10">[01:06:10]</a>.
*   **Proof Aggregation:** They enable aggregation of proofs across all native rollups behind the scenes by Layer 1 validators, dramatically reducing gas costs for Layer 2s to settle <a class="yt-timestamp" data-t="01:07:37">[01:07:37]</a>.

This strategic shift means that Layer 2s will become closer to the heart and economics of [[ethereum_roadmap|Ethereum]], and more technically aligned with it <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

## Implementation: Timelines and Challenges

Implementing [[Ethereums scaling strategy with native rollups|native rollups]] involves significant coordination and technical hurdles:
*   **The EVM Pre-compile:** The core mechanism for [[Ethereums scaling strategy with native rollups|native rollups]] is the EVM execute pre-compile <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. This special instruction allows the EVM to see within itself, facilitating state transition validation by Layer 1 validators <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>.
    *   **Vanilla vs. ZK:** A simple, "naive" re-execution-backed pre-compile can be implemented sooner, potentially by late 2026 <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. However, to truly scale [[ethereum_roadmap|Ethereum]] and dramatically increase the gas limit, [[Ethereums strategic pivot and ongoing developments|ZK proofs]] (snarks) are necessary <a class="yt-timestamp" data-t="00:40:16">[00:40:16]</a>.
    *   **Real-time Proving:** The technology for snark proving is rapidly advancing, with costs already in the order of cents and latencies for proving an [[ethereum_roadmap|Ethereum]] block on a single GPU currently around a few minutes <a class="yt-timestamp" data-t="01:09:41">[01:09:41]</a>. Multi-machine proving is expected to bring latencies much lower, potentially hitting the 12-second "next slot real-time proving" benchmark this year <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>. This will enable the pre-compile to scale Layer 1 throughput by 10x or 100x <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.
*   **Refactoring Existing Rollups:** For current rollups (e.g., Optimism, Arbitrum, Base) to become native, they need to refactor their code to cleanly decouple the execution of user transactions (EVM state transition function) from their system-level code (blob passing, sequencer handling, governance) <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>. This represents a "decent technical hurdle" <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.
*   **Virtual Machine Compatibility:** [[Ethereums scaling strategy with native rollups|Native rollups]] are only possible for EVM-equivalent rollups. Those using different virtual machines (like SVM, Move, Cairo, or WASM) cannot become native <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.
*   **Customizability Trade-off:** While native rollups offer immense security and integration benefits, they tie Layer 2s to the EVM's upgrade cycle, which historically has been slow <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>. However, evidence suggests that most Layer 2s prioritize EVM equivalence, and customizability is increasingly expressed in areas outside the core EVM, such as tokenomics, governance, treasury management, or sequencer features (e.g., flash blocks) <a class="yt-timestamp" data-t="00:54:57">[00:54:57]</a>.

### The Problem of Coordination

The primary bottleneck for this work is the lack of a full-time "coordinator" or "champion" to lead the effort, similar to Tim Beiko's role in shipping EIP-1559 <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. This role would involve coordinating with Layer 2 teams, execution layer clients, and researchers <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>.

The process for an [[Ethereums roadmap and future upgrades|Ethereum upgrade]] involves:
1.  Writing an EIP (Ethereum Improvement Proposal).
2.  Going through All Core Devs calls.
3.  Developing and testing on Dev Nets and Test Nets.
This process typically takes 12 to 18 months <a class="yt-timestamp" data-t="01:00:39">[01:00:39]</a>.

### Strategies for Faster Progress

The [[ethereum_roadmap|Ethereum]] community is implementing two parallel strategies to address coordination and accelerate progress:
1.  **Accelerated Fork Cadence:** Shifting from one hard fork per year to an ambitious goal of two forks per year <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. This allows smaller changes to be pushed with lower latency <a class="yt-timestamp" data-t="01:14:26">[01:14:26]</a>.
2.  **The Beam Chain:** This initiative focuses solely on research and development for a period of years, aiming to batch bold and ambitious upgrades into a single, less frequent but more significant release, thereby optimizing the "social layer" governance process <a class="yt-timestamp" data-t="01:14:51">[01:14:51]</a>. This allows for bigger, more fundamental changes without being constrained by the rapid cadence of smaller forks <a class="yt-timestamp" data-t="01:15:11">[01:15:11]</a>.

These efforts reflect a broader strategy to maintain high conviction in [[ethereums_roadmap_and_potential_upside|Ethereum's future strategic direction]] by tackling fundamental coordination challenges <a class="yt-timestamp" data-t="01:15:38">[01:15:38]</a>.