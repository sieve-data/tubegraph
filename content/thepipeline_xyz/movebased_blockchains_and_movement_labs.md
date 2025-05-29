---
title: Movebased blockchains and movement Labs
videoId: y9Ac0ybjuHk
---

From: [[thepipeline_xyz]] <br/> 

Movement Labs is building the first network of [[monad_labs_and_blockchain_technology_advancements | Move-based blockchains]], with a focus on [[high performance blockchains | high performance]] and security. Rousi, co-founder of Movement Labs, describes their mission as taking modern tech stacks and blockchains to the next level, addressing the limitations of older technologies like the EVM <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## The Move Concept

The "Move" concept was originally developed by Facebook's Diem (formerly DM) project, which invested over a billion dollars in research <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Facebook chose to completely rewrite the language and infrastructure instead of using Solidity or the standard EVM, a decision that Movement Labs views as a testament to Move's potential <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. The Move language is designed for security and performance <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.

## Movement Labs' Flagship Product: M2

Movement Labs' flagship product is M2, the first Move rollup on Ethereum, powered by Snow consensus <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Architectural Components

M2's architecture is a "mashup" of several technologies, sometimes humorously referred to as an "L1.5" <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>:
*   **Execution Environment**
    *   Utilizes the Move Virtual Machine (DM VM), which was built by the Diem project and adopted by blockchains like Aptos and Sui <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Settlement Layer (Layer 2)**
    *   Settles on Ethereum, leveraging its security and liquidity <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Data Availability (DA)**
    *   Partners with Celestia to handle data availability, avoiding the high gas fees associated with Ethereum's DA <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This allows for performance similar to Layer 1s with extremely low gas fees, while maintaining the security and decentralization of Ethereum mainnet <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Decentralized Sequencer Set**
    *   Movement Labs is developing a decentralized sequencer set that uses Snow consensus (from Avalanche) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   Snow consensus is chosen for its low hardware requirements, high decentralization (allowing anyone to run a validator from home), and instant finality <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   This system addresses the centralization points common in modern rollups <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. Validators are incentivized to maintain network uptime by staking Movement Labs' native token, which also provides value back to the token <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### EVM Compatibility via Fractal

Movement Labs aims for short-term adoption by building backward compatibility for their next-generation technology <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>. They developed "Fractal," a transpiler that allows Solidity code (EVM opcodes) to be mapped to Move opcodes and launched on the Move VM <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. This makes it feel, work, and look like an EVM from a developer's perspective (e.g., Remix IDE, Infura compatibility) while utilizing the Move VM underneath <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>.

Although writing directly in Move code offers the highest security, the transpiler inherits many of the Move VM's proving mechanisms and security benefits, including formal verification <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. This approach aims to prevent the billions of dollars lost annually to smart contract hacks, providing a more secure environment for users and institutions <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

## Addressing Industry Challenges

Movement Labs, alongside other projects like [[monad_labs_and_blockchain_technology | Monad]], is focused on solving critical issues in crypto, particularly infrastructure limitations and scalability <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

### Scaling and Performance

A key value proposition of [[discussion_on_high_throughput_blockchains | high performance blockchains]] is their ability to handle large user bases without prohibitive gas fees or network crashes <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Current EVM-based systems, like Arbitrum, can become unusable with high demand, leading to inconsistent and high gas fees that deter average users <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

Movement Labs believes that infrastructure is now mature enough to support real-world applications <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. Projects like Solana and Movement Labs are pushing boundaries to handle the transactions needed for large-scale applications such as payments and gaming <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

### Collaboration over Competition

Rousi emphasizes the importance of collaboration within the blockchain ecosystem, particularly at the execution layer <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. He notes a shift away from tribalism, with different VM (Virtual Machine) proponents recognizing the value of each other's research and designs <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>, <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>. The common consensus is that the "old EVM needs to burn," fostering a collective goal to move towards next-generation blockchains that can onboard a billion users <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This collaborative mindset, especially in the bear market, aims to grow the overall pie of blockchain users rather than fighting over existing pieces <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.

### Use Cases and Future Outlook

Movement Labs is excited about [[technology_advancements_and_infrastructure_in_blockchain | advancements]] in user experience, such as account abstraction and simplified transaction signing, which remove historical barriers to adoption <a class="yt-timestamp" data-t="00:36:33">[00:36:33]</a>.

They believe that combined with [[high performance blockchains | high-performance]] next-generation chains, this will disrupt industries like payments <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>. Rousi anticipates significant disruption for services like Western Union due to more efficient cross-border payments offered by crypto <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>.

Beyond finance, Movement Labs is interested in how blockchain technology can be used for "social attention" and "social coordination dynamics" <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>. The recent "Friend.tech" application, despite its issues, sparked new thinking about how blockchain can be applied beyond traditional order books and games, particularly in social applications <a class="yt-timestamp" data-t="00:42:47">[00:42:47]</a>. Rousi remains optimistic that among the many new social dApp pitches, some will break through and unlock new use cases <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>. Movement Labs is keen to see [[building_community_within_blockchain_ecosystems | communities]] coalesce around these innovations.