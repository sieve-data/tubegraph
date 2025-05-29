---
title: Ethereums ZK scaling developments
videoId: NJIkUCJZwZg
---

From: [[bankless]] <br/> 

Ethereum is on the cusp of significant scaling advancements through Zero-Knowledge (ZK) cryptography, which could accelerate its Layer 1 (L1) throughput by a factor of 100x <a class="yt-timestamp" data-t="01:27:27">[01:27:27]</a>. This breakthrough, referred to as an "Ethereum ZK Miracle," is anticipated to revolutionize the network's capacity and interoperability <a class="yt-timestamp" data-t="02:22:31">[02:22:31]</a>.

## The ZK Proving Mechanism

At its core, ZK proving allows for the verification of computation without needing to re-execute the entire process <a class="yt-timestamp" data-t="03:44:39">[03:44:39]</a>. Currently, all blockchain nodes, including those on Ethereum, Bitcoin, and Solana, must re-execute every block to check its validity, which is a bottleneck for speed and scalability <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. With a ZK proof, only one computer needs to perform the complex computation (like solving a Sudoku puzzle), and then other nodes simply verify the correctness of the proof, which is a much easier task <a class="yt-timestamp" data-t="03:49:50">[03:49:50]</a>.

## Real-Time Proving

The key to this scaling leap is "real-time proving," meaning ZK proofs can be generated in sub-block time <a class="yt-timestamp" data-t="03:13:50">[03:13:50]</a>. For Ethereum's L1, with its 12-second block times, this means proofs must be created faster than 12 seconds <a class="yt-timestamp" data-t="03:22:46">[03:22:46]</a>. As of current observations, 99% of Ethereum L1 blocks are already proved in less than 13 seconds, indicating the technology is very close to enabling this real-time capability <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. The cost and time for ZK proofs are on an exponential decline, happening faster than previously expected <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

## Impact on Ethereum Layer 1

The advent of real-time ZK proving unlocks two main benefits for Ethereum:

*   **Enhanced Cross-Chain Composability**: If Layer 2 (L2) ecosystems can generate proofs in real-time, the state of one L2 can be referenced by another, fostering stronger interoperability <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   **Enshrined ZK Rollup L1**: The Ethereum L1 itself can be transformed into an enshrined ZK rollup <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. This means decoupling the execution layer from the [[ethereums_consensus_layer_and_validator_changes | consensus layer]], allowing the L1 to achieve a 100x increase in throughput <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>. While block times will remain 12 seconds, block sizes could become hundreds or thousands of times larger <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. As ZK proving times continue to decrease, further reductions in block times are also possible <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. This [[ethereums_scaling_strategy_with_native_rollups | Ethereums scaling strategy with native rollups]] acts as a "gravity well," encouraging other rollups to become native to Ethereum for better interoperability, leading to a "United Chains of Ethereum" <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

[!NOTE]
This development provides a credible path to [[ethereums_scaling_and_bandwidth_optimization | scale the Ethereum L1]] to 10,000 transactions per second <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This is part of [[ethereums_strategic_pivot_and_scaling_layer_1_efforts | Ethereum's strategic pivot and scaling layer 1 efforts]].

## Timelines and Outlook

Opinions on the exact timeline for these advancements vary among developers. Justin Drake is highly optimistic, suggesting it could happen within 3 years <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. Donrad estimates around 6 years <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>. A middle-ground estimate suggests approximately four and a half years for the full 10,000 transactions per second capability to be realized <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. The ability to achieve a 3x annual increase in [[ethereum_scaling_and_gas_limits | Ethereum scaling and gas limits]] means significant progress will compound rapidly <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. Overall, this is seen as highly bullish, potentially "saving Ethereum" and validating its long-term [[ethereum_development_priorities | roadmap and potential upside]] <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. This is part of [[ethereums_strategic_pivot_and_ongoing_developments | Ethereums strategic pivot and ongoing developments]] that prioritizes long-term solutions.

## Key Players and Challenges

The [[challenges_and_solutions_in_ethereum_scaling | Ethereum Foundation]] has been investing in ZK technology for years, making this progress possible <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. One key player in this space is Succinct, which is launching a decentralized prover network and its PRO token this week <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>. This network is crucial for generating the "Sudoku puzzles" (ZK proofs) and ensuring a decentralized set of provers <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.

### Remaining Hurdles
While progress is rapid, challenges remain:
*   **Formal Verification**: Vitalik Buterin has emphasized the need for formal verification of ZK systems, though companies like Succinct are reportedly close to achieving this within months <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   **Bugs**: The complexity of ZK tech means potential for bugs that need to be ironed out <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Hardware and Energy**: Currently, proving requires GPUs, demanding energy equivalent to 10 Teslas plugged in simultaneously <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. The goal is to reduce this to one Tesla's worth of energy, making it feasible for hobbyist stakers to run provers at home using marketable ZK prover ASICs that the Ethereum Foundation is investing in <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.