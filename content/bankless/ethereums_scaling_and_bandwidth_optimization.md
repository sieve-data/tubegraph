---
title: Ethereums Scaling and Bandwidth Optimization
videoId: WpjcPPrrN2E
---

From: [[bankless]] <br/> 

Ethereum is an evolving organism that constantly adapts through debate, deliberation, and rough consensus, primarily within the Ethereum All Core Devs (ACD) calls where priorities are set and Ethereum Improvement Proposals (EIPs) are considered <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>. A key theme of the past year has been [[challenges_and_solutions_in_ethereum_scaling | scaling]], affecting both the execution and consensus layers <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## Core Philosophy: Security First

Ethereum's development prioritizes security above all else <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This robust approach is what differentiates Ethereum, ensuring the chain has never gone down <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. While this focus may lead to slower upgrades, taking between six and twelve months instead of weeks, it ensures thorough testing and robustness, as there's no off-chain legal system to resolve issues like centralized banks can <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>, <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. The bar for social intervention on Ethereum, such as reversing transactions, is extremely high, as seen with historical events like the DAO hack <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. If security were disregarded, [[challenges_and_solutions_in_ethereum_scaling | scalability]] could be achieved quickly, but at the cost of stability, potentially leading to chain restarts or syncing issues <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

## Current and Future Upgrades: Petra & Fusaka

Ethereum upgrades come in "hard forks" named after a combination of a star and a Devcon city <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>, <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

### Petra Hard Fork

The next significant upgrade is **Petra** (Prague + Electra), currently in its testnet phase <a class="yt-timestamp" data-t="00:50:02">[00:50:02]</a>, aiming for a mainnet activation around May <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>. Key features include:

*   **Maximum Effective Balance (Max EB):** This feature allows validators to consolidate their staked Ether from discrete 32 ETH chunks into larger units of up to 2048 ETH <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
    *   **Bandwidth Optimization:** Large operators, like Lido, can combine their validators to significantly reduce bandwidth usage on the network, freeing up bandwidth for other scaling efforts like blobs <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>, <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. Instead of sending multiple messages for many validators, a single message representing a higher weight is sent <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
    *   **Compounding for Small Stakers:** Smaller validators (e.g., 32 ETH stakers) can auto-compound their rewards, as their effective balance automatically increases with earned rewards up to 2048 ETH <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.
*   **Increased Blob Space:** Petra will double the average number of blobs per block from three to six (with a maximum of nine) <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. This directly translates to [[ethereums_layer_2_rollup_strategy | more data availability for L2s]], which rely on blobs for cost-effective, ephemeral data storage <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. The bandwidth savings from Max EB contribute to making this increase possible <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
*   **EIP-7702 (Account Abstraction):** This EIP introduces the first in-protocol version of account abstraction, allowing Externally Owned Accounts (EOAs) to delegate functionality to smart contracts <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>. Users can effectively "plugin" smart contract features (like multi-sig, auto-approvals, or social recovery) to their existing EOAs, and change these delegations over time while retaining their original address and private key <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>, <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>. This enhances user experience and maintains security by preventing cross-chain asset draining from faulty delegations <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>. While not a silver bullet, it addresses most user needs in the short term <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>.

### Fusaka Hard Fork

**Fusaka** (Fulu + Osaka) is the subsequent hard fork, targeted for 2025 <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>. Its primary goal is a significant increase in blob data, ideally aiming for 48 blobs per block on average <a class="yt-timestamp" data-t="00:38:35">[00:38:35]</a>, <a class="yt-timestamp" data-t="00:03:00">[00:00:03]</a>. The two main features are:

*   **Proto-Danksharding (Pure DAS):** This is a cryptographic step-function change in data availability strategy <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>. Currently, every node on Ethereum stores all blob data for a few weeks <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>. With Pure DAS, nodes will only store a *subset* of the data but use cryptography to probabilistically ensure that other nodes collectively hold all the data <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>. This qualitative leap could lead to a 10x increase in data availability for the same amount of bandwidth <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   **Ethereum Object Format (EOF):** EOF aims to modernize the Ethereum Virtual Machine (EVM), moving it from a "1950s computer" to a "1990s computer" <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>. This upgrade primarily benefits developers and toolings by separating code and data within smart contracts, introducing specific opcodes, and allowing the deprecation of certain problematic functionalities <a class="yt-timestamp" data-t="00:57:06">[00:57:06]</a>, <a class="yt-timestamp" data-t="00:58:31">[00:58:31]</a>. EOF is an opt-in versioned EVM type, not forcing changes on existing contracts <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

## Glamsterdam and Beyond

**Glamsterdam** is the hard fork planned after Fusaka, but its scope is currently undefined, serving as a placeholder name for future upgrades <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>. The aim is to finalize its scope shortly after Fusaka goes live to allow teams to begin work in parallel <a class="yt-timestamp" data-t="01:02:29">[01:02:29]</a>.

[[adapting_ethereums_roadmap_for_growth | Adapting Ethereum's roadmap for growth]] includes a renewed and aggressive focus on scaling <a class="yt-timestamp" data-t="01:03:22">[01:03:22]</a>, aiming to remove process-related slack in the development system <a class="yt-timestamp" data-t="01:04:17">[01:04:17]</a>. While the pace of upgrades is dictated by thorough R&D and complex engineering issues, the goal is to formalize processes to ensure continuous progress without unnecessary delays <a class="yt-timestamp" data-t="01:04:22">[01:04:22]</a>.

## [[ethereum_scaling_and_gas_limits | Layer 1 Scaling]]

[[ethereums_strategic_pivot_and_scaling_layer_1_efforts | Scaling the Ethereum Layer 1]] (execution layer) is a complex challenge due to its multivariate nature <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>, <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>. Unlike scaling blob space which has a clear "North Star" like Proto-Danksharding and blob targets <a class="yt-timestamp" data-t="01:10:45">[01:10:45]</a>, Layer 1 scaling involves many interconnected inputs, such as state growth, historical data, and opcode pricing <a class="yt-timestamp" data-t="01:09:26">[01:09:26]</a>.

Efforts are underway to:
*   Better understand and address bottlenecks, such as state growth, which was previously thought to be a greater short-term issue <a class="yt-timestamp" data-t="01:09:27">[01:09:27]</a>.
*   Consider repricing opcodes to make certain operations cheaper without increasing the overall gas limit, effectively increasing throughput <a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.
*   Optimize block verification in light of MEV (Maximal Extractable Value) strategies, where builders want to finalize blocks at the last possible second <a class="yt-timestamp" data-t="01:12:17">[01:12:17]</a>.

## Interoperability and Future Direction

Interoperability and fragmentation among [[ethereums_layer_2_rollup_strategy | Layer 2s]] are primarily application-layer concerns <a class="yt-timestamp" data-t="01:13:33">[01:13:33]</a>. While core protocol efforts like [[ethereums_scaling_strategy_with_native_rollups | native rollups]] (common pre-compiles on L1 that allow L2s to interoperate with L1 guarantees) are long-term goals, they are extremely complex and would take years to ship <a class="yt-timestamp" data-t="01:14:09">[01:14:09]</a>. Therefore, the short-term focus remains on application and wallet-level standardization <a class="yt-timestamp" data-t="01:15:53">[01:15:53]</a>.

## Summer of Protocols

Initiatives like "Summer of Protocols" (returning in 2025) aim to deepen the understanding of protocols, an analogy for Ethereum itself <a class="yt-timestamp" data-t="01:16:37">[01:16:37]</a>. By funding researchers and educators across diverse domains, the program seeks to formalize best practices for working with protocols, drawing parallels between Ethereum's challenges and those in other complex systems <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>, <a class="yt-timestamp" data-t="01:18:01">[01:18:01]</a>. This meta-level research helps to frame Ethereum's challenges more effectively and learn from different perspectives <a class="yt-timestamp" data-t="01:18:57">[01:18:57]</a>.