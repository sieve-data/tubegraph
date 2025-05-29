---
title: Movebased blockchains and their advantages
videoId: y9Ac0ybjuHk
---

From: [[thepipeline_xyz]] <br/> 

Move-based blockchains represent a new generation of blockchain technology, emphasizing performance, security, and developer experience. Movement Labs is a key player in this space, building the first network of Move-based blockchains, including M2, the first Move Rollup on Ethereum <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>.

## Origin and Vision of Move

The Move concept was originally developed by Facebook through the Diem (formerly Libra) project <a class="yt-timestamp" data-t="01:27:14">[01:27:14]</a>. This project invested over a billion dollars in research to create a novel programming language and virtual machine, as the existing Ethereum Virtual Machine (EVM) was perceived as "slow, clunky, and broken" <a class="yt-timestamp" data-t="01:13:35">[01:13:35]</a>. The vision for Move-based blockchains is to bring this advanced concept to networks like Ethereum, leveraging their liquidity and user bases <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.

## Key Advantages of Move-based Blockchains

Move-based blockchains offer several significant advantages over older architectures, directly addressing [[challenges_in_current_blockchain_infrastructure | challenges in current blockchain infrastructure]]:

### 1. Performance and Scalability
High-performance blockchains, like those based on Move, are designed to handle a billion users, unlike older EVM chains that struggle with 50,000 users due to prohibitive gas fees and instability <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. These next-generation blockchains can actually meet the demands of a world where everyone is on-chain <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. They enable [[performance_gains_in_blockchain_transactions | performance gains in blockchain transactions]] necessary for widespread adoption.

### 2. Enhanced Security
A critical advantage of Move-based blockchains is their focus on security through formal verification <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. The MoveVM has built-in provers, inheriting formal verification methods <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This directly combats the billions of dollars lost annually to smart contract hacks <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. The language's typed bytecode allows for checks at execution time, which improves security <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. For Solidity code transpiled to Move, it maps to statistically typed Move opcodes with baked-in security, though not 100% equivalent to native Move code <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

### 3. Developer Experience and Compatibility
While Rust, used by some high-performance chains like Solana, can be difficult for developers <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>, Move-based projects aim to make development more accessible. Movement Labs has developed "Fractal," a transpiler that allows Solidity code (EVM opcodes) to be mapped to Move opcodes and launched on the MoveVM <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. This means developers can bring their existing Solidity code to a next-generation network without needing to hire a new engineering team or learn a new programming language <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. The goal is for it to feel, work, and look like an EVM, but with the MoveVM underneath <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## Movement Labs' Approach (M2)

Movement Labs' M2 is a prime example of a Move-based blockchain leveraging a hybrid architecture:

*   **Execution Environment**: It uses the Move Virtual Machine (MoveVM), originally built by the Diem project and adopted by other Move chains like Aptos and Sui <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
*   **Layer 2 on Ethereum**: M2 is a Layer 2 on Ethereum, inheriting Ethereum's security and liquidity <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   **Data Availability (DA)**: To overcome the data availability bottleneck and high gas fees seen in traditional rollups, M2 partners with Celestia for data availability <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. This combination aims to offer Layer 1-like performance with extremely low gas fees, while maintaining Ethereum mainnet's security and decentralization <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
*   **Decentralized Sequencer**: M2 will feature a decentralized sequencer set that uses Snow Consensus (from the Avalanche ecosystem) <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>. Snow Consensus has low hardware requirements and is highly decentralized, allowing anyone to run a validator from home <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. Validators are incentivized by staking the native token, creating an ecosystem that ensures network uptime <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **"L1.5"**: This unique combination of Move, Avalanche (Snow Consensus), Ethereum, and Celestia has been jokingly referred to as "L1.5," reflecting its mix of Layer 1 and Layer 2 characteristics due to its decentralized sequencer set on Ethereum <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

## Industry Context and Future Outlook

The industry is moving towards a future where [[high_throughput_blockchains_and_infrastructure_challenges | high throughput blockchains and infrastructure challenges]] are being solved <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. There is a general consensus that the "old EVM needs to burn" <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>, and new virtual machines like MoveVM and [[monad_blockchain_development | Monad]]'s approach are seen as crucial next steps <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.

Developers are increasingly recognizing that the [[need_for_performant_blockchain | need for performant blockchain]] systems is paramount for mainstream adoption <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. While infrastructure is becoming more capable, a single app with web2-level users (like Instagram or Facebook) would still break every blockchain today, including Solana <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>. However, there is now "line of sight on the solution" for this scalability challenge <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.

This shift in infrastructure readiness opens up [[opportunities_for_application_development_on_highperformance_blockchains | opportunities for application development on highperformance blockchains]] that were previously impossible <a class="yt-timestamp" data-t="21:14:00">[21:14:00]</a>:

*   **Payments**: Ready for disruption, enabling efficient cross-border transactions with stablecoins and improved user experiences via account abstraction <a class="yt-timestamp" data-t="35:54:00">[35:54:00]</a>.
*   **Retail Trading**: On-chain order books with reasonable slippages are becoming viable <a class="yt-timestamp" data-t="37:19:00">[37:19:00]</a>.
*   **Gaming**: Building fun games with on-chain asset and state tracking is now feasible, moving beyond "Ponzi games" towards sustainable economics and unique social coordination experiences <a class="yt-timestamp" data-t="37:45:00">[37:45:00]</a>.

The blockchain space is also seeing a breakdown of tribalism, with different ecosystems showing more collaboration and respect for each other's technical advancements <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>. This collaborative mindset, especially among execution layer teams, aims to expand the overall market ("grow the pie") rather than just competing for existing users <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>. The focus is on solving specific problems and providing developers with choices tailored to their needs <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>. This represents a significant shift from past cycles, fostering a more cohesive community to achieve the [[future_of_high_performance_and_scalable_blockchains | Future of high performance and scalable blockchains]] where users can truly benefit from next-generation blockchain technology <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.