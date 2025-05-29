---
title: high performance blockchains
videoId: y9Ac0ybjuHk
---

From: [[thepipeline_xyz]] <br/> 

[[evolution_and_impact_of_highperformance_blockchain_technology | High-performance blockchain technology]] aims to address critical limitations of earlier blockchain designs, particularly the "slow, clunky, broken" nature of previous Virtual Machines (VMs) like the generic EVM <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. The core objective is to create systems that can handle large user bases and complex applications without prohibitive costs or performance bottlenecks <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

## Key Value Propositions of High Performance Blockchains

The primary value proposition of a [[discussion_on_high_throughput_blockchains | high-performance blockchain]] is its ability to handle a billion users, a goal many projects aim for <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. Current EVM-based systems struggle with even 50,000 users, leading to extremely high gas fees and unusability, often followed by hacks <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. Next-generation [[blockchain_scalability_and_highperformance_systems | blockchain scalability and high-performance systems]] are designed to:
*   **Handle Demand:** Capable of supporting the widespread demand anticipated if everyone were on-chain <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
*   **Support Mass Adoption:** Allow for the onboarding of significantly more users <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.
*   **Enable Complex Applications:** Provide the necessary scale for ambitious "Pie in the Sky" ideas to become reality <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

Current infrastructure is not yet ready for applications, as seen when high volumes on platforms like GMX cause Arbitrum gas fees to skyrocket, making the system unusable <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>. This inconsistency in gas fees can wreck trading strategies for average users <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.

## Movement Labs' Approach to High Performance

Movement Labs is building the first network of Move-based blockchains <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. Their architecture is a "weird mashup" of different technologies <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>:
*   **Move Virtual Machine (MoveVM):** The execution environment is the MoveVM, originally developed by Facebook's Diem project (with over a billion dollars in research) and adopted by Aptos and Sui <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a> <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
*   **Ethereum Layer 2 (L2):** Movement Labs' M2 is the first Move rollup on Ethereum, leveraging Ethereum's security and liquidity <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a> <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   **Celestia for Data Availability (DA):** To overcome the data availability bottleneck seen in traditional rollups like Arbitrum or Optimism, Movement partners with Celestia for DA, achieving performance akin to Layer 1s with extremely low gas fees <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
*   **Snow Consensus:** For its decentralized sequencer set, Movement utilizes Snow Consensus, which has low hardware requirements, is highly decentralized, and offers instant finality <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>. This system incentivizes validators through staking the native token ("move") to secure the network and maintain uptime <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Fractal Transpiler (EVM Compatibility):** To drive adoption, Movement built "Fractal," a transpiler that allows any Solidity code (EVM opcodes) to be mapped to Move opcodes and launched on the MoveVM <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. While not 100% the same as writing in Move, it inherits the MoveVM's formal verification methods, significantly enhancing security <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. The goal is for the experience to feel, work, and look like an EVM, but with the MoveVM underneath <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## [[monads_highperformance_blockchain_features | Monad's High-Performance Blockchain Features]]

[[monads_highperformance_blockchain_features | Monad's high-performance blockchain features]] focus on making the EVM fast while adhering to first engineering principles <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **EVM Optimization:** Monad aims to make the actual EVM fast by changing underlying components like the database and consensus mechanism <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Layer 1 (L1) Architecture:** To provide a viable, full package solution, Monad operates as an L1, allowing deep-seated changes to the system <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
*   **Developer Focus:** Monad aims to be the choice for EVM developers, while Solana attracts SVM developers <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This strategy is seen as market expansion rather than direct competition <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.
*   **Security Improvements:** [[blockchain_performance_optimization | Blockchain performance optimization]] can indirectly improve security by reducing development costs, allowing developers to implement more checks without compromising on gas optimization <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. As an L1, Monad can also add special, low-level instructions to the VM (e.g., marking contracts as non-reentrant) to directly address common security concerns like re-entrancy attacks <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

## Pressing Issues and Solutions in Crypto

The most pressing issue in crypto, beyond gaining more users, is the inadequacy of today's infrastructure, especially execution layers <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.
*   **Developer Experience:** While Solana has performed well, it's difficult to get builders to write in Rust due to the financial disincentive and the dominance of Solidity/EVM for volume and Total Value Locked (TVL) <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. Projects like Movement and Monad allow Solidity developers to bring their code to next-generation networks without hiring new teams or learning new, untested programming languages <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **Scalability:** The current infrastructure cannot handle a Facebook-level user base; every blockchain would fail <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>. Projects are now reaching a "line of sight" on solutions, indicating that while not fully there, the path to massive [[blockchain_scalability_and_highperformance_systems | blockchain scalability and high-performance systems]] is becoming clearer <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
*   **Inconsistent Gas Fees:** [[Parallel Execution in Blockchain | Parallelized runtimes]] and localized fee markets are crucial to guarantee a consistent user experience, as sudden jumps in gas fees can make applications unusable for average users <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.

## Collaboration vs. Competition

Historically, the blockchain space has been characterized by rigid competition and "Twitter Wars" between different Layer 1s, Data Availability (DA) layers, and settlement layers <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>. However, there's a growing sentiment for collaboration, particularly among execution layer projects <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
*   **Shared Goal:** Different VMs (Monad VM, Move VM, Solana VM) are seen as interesting pieces of technology, designed for specific use cases, and built on genuine research <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>. The common consensus is that the old EVM is problematic <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>.
*   **Moving the Space Forward:** The industry is recognizing that fighting between ecosystems (e.g., Ethereum vs. Solana) has not been beneficial <a class="yt-timestamp" data-t="16:41:00">[16:41:00]</a>. Collaboration, learning from each other, and contributing back to the broader ecosystem (e.g., Monad considering EIPs for Ethereum) is seen as a more productive approach <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.
*   **Growing the Pie:** The goal is to "grow the pie" of overall blockchain adoption and use cases, rather than fighting over existing market share <a class="yt-timestamp" data-t="32:27:00">[32:27:00]</a>. Developers should have the choice of where to build, and unique value propositions will attract them <a class="yt-timestamp" data-t="32:49:00">[32:49:00]</a>.

## Ready for Applications

The infrastructure is perceived as "99% there," with significant investments resolving previous issues like expensive DA (Celestia) and inefficient VMs <a class="yt-timestamp" data-t="20:05:00">[20:05:00]</a>. While not ready for a "Facebook-level" user base today, there is a clear "line of sight" on solutions <a class="yt-timestamp" data-t="21:30:00">[21:30:00]</a>.

### Potential Use Cases
*   **Payments:** Cross-border payments are ripe for disruption due to high costs and complexities in traditional systems <a class="yt-timestamp" data-t="35:57:00">[35:57:00]</a>. Advancements in account abstraction and wallet experiences, combined with [[discussion_on_high_throughput_blockchains | high-throughput blockchains]], can enable seamless, low-cost global transactions <a class="yt-timestamp" data-t="36:33:00">[36:33:00]</a>.
*   **Retail Trading:** [[Performance needs in decentralized finance | Performance needs in decentralized finance]] include retail trading, where on-chain order books with reasonable slippages and market maker profitability are becoming feasible <a class="yt-timestamp" data-t="37:19:00">[37:19:00]</a>. High-frequency trading may still be an iteration or cycle away <a class="yt-timestamp" data-t="37:23:00">[37:23:00]</a>.
*   **Gaming:** While previous attempts were hampered by being "Ponzi games" focused on financial speculation rather than fun <a class="yt-timestamp" data-t="40:30:00">[40:30:00]</a>, modern [[performance_needs_in_decentralized_finance | performance needs in decentralized finance]] allow for building good games that use blockchain for asset and state tracking, rather than running the entire game engine on-chain <a class="yt-timestamp" data-t="37:48:00">[37:48:00]</a>. The primary bottleneck is creating a genuinely fun game first, then integrating blockchain components like NFTs for digital ownership <a class="yt-timestamp" data-t="38:21:00">[38:21:00]</a>.

### Unique Database Optimizations
[[unique_database_optimizations_in_blockchains | Unique database optimizations in blockchains]] are crucial for high-performance systems. The challenge is often the [[challenges_of_standard_databases_in_blockchain_performance | challenges of standard databases in blockchain performance]] because they are not designed for the specific needs of blockchain's transactional model.

## Future Outlook

There is growing excitement over the breakdown of "tribalism" in crypto, with core Ethereum developers acknowledging other VMs and DA layers <a class="yt-timestamp" data-t="41:52:00">[41:52:00]</a>. This shift towards a more cohesive community that works together on technology is viewed positively <a class="yt-timestamp" data-t="42:30:00">[42:30:00]</a>. The focus is shifting from infrastructure building to unlocking actual application use cases <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>. Innovations like Friend.tech, despite their flaws, have inspired new ideas for social applications beyond traditional finance or gaming <a class="yt-timestamp" data-t="42:47:00">[42:47:00]</a>.