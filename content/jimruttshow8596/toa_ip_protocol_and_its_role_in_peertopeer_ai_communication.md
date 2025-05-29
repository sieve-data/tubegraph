---
title: TOA IP protocol and its role in peertopeer AI communication
videoId: YywqrGkvqrk
---

From: [[jimruttshow8596]] <br/> 

TOA IP is a network communication protocol specifically designed to facilitate decentralized communications for Artificial Intelligence (AI) [[00:40:40]]. It eliminates the need for third-party intermediaries in communication and value exchange between devices, enabling sub-second transactions crucial for AI applications [[00:01:43]].

## Origin and Naming of TOA IP

The creation of TOA IP was not initially intentional; it emerged from a group of technologists aiming to solve problems related to [[ai_security_and_reducing_dependency_on_third_parties | reducing dependency on a third party]] in communications [[00:01:35]]. The name "TOA" was a placeholder, combining the first names of co-authors Tui Saliba and Dan, the CTO, and coincidentally means "thank you" in Hebrew [[00:02:20]]. The name also references physicist Moratu Toda, who contributed significantly to scientific concepts like the Toda chain and Toda lattice [[00:02:49]].

## Core Functionality: Communication of Value

The primary function of TOA IP is to enable [[economic_transactions_in_ai_applications_and_micropayments | communication of value]] directly between two devices [[00:03:11]]. For AI agents, this means they can instantly exchange value for services without waiting for external validation from traditional financial institutions or ledger-based blockchains [[00:03:31]].

Traditional systems, like banks or ledger-based blockchains, introduce delays that AI agents cannot afford, as they often require responses within 100 milliseconds [[00:06:53]]. The speed of light and network latency mean that relying on a central third party for every transaction, even fast ones like Visa, would exceed these time constraints [[00:07:10]].

TOA IP solves this by integrating cryptographic proof directly into the very first network packet of a handshake between devices [[00:08:29]]. This allows the receiver to instantaneously verify the legitimacy of the sender's claim to value and ensure no double-spending, enabling immediate transaction and service execution [[00:11:03]].

### Addressing Micro-payment Challenges

Beyond speed, TOA IP addresses the challenge of [[economic_transactions_in_ai_applications_and_micropayments | micro-payments]] in AI interactions, where a single transaction might be as low as 0.01 cent [[00:07:55]]. Traditional systems have high transaction costs (e.g., $5-$10 for a simple USDC transaction on blockchain, or 25 cents via Visa) that make such micro-payments economically unfeasible [[00:08:00]].

With TOA IP, the friction of time and cost is eliminated because the computational effort for verification largely rests with the two communicating devices (99% of the effort), with minimal burden on the wider network for witnessing [[00:10:06]]. This design, detailed in the Hypercycle core whitepaper, uses a "merzer" (a decentralized Merkle tree) that allows parallel processing and the formation of a single global hash, providing unique, time-stamped proof of ownership [[00:10:12]].

## Settlement and Onboarding

Value within the Hypercycle network is managed through a "container" called HYPC, which is less than 63 kilobytes in size [[00:13:11]]. This container holds cryptographic proof of ownership for US Dollars, Bitcoin, Ethereum, or USDC [[00:13:30]].

*   **Internal Transactions**: Once value is "deployed" into a HYPC container on a Hypercycle computation node, AI agents can transact in sub-second timeframes with minimal cost [[00:20:00]]. Each HYPC container has a globally unique non-fungible token (NFT) number, ensuring that no two devices can use the exact same file at the same time, verified rapidly via binary search trees [[00:33:38]].
*   **Onboarding/Offboarding**: The system leverages existing ledger-based blockchains (like Ethereum for USDC or Bitcoin for Satoshis) only for initial onboarding or final cash-out by human users [[00:13:20]]. A decentralized smart contract, called CHPC, acts as a bridge, costing approximately $1-$2 per transaction for off-chain transfers [[00:24:33]]. This allows for very inexpensive and fast micro-payments within the AI network, with the slower, more expensive blockchain transactions only occurring when funds need to enter or exit the AI ecosystem for human use [[00:28:47]].

The analogy used is that of a Brinks truck: the HYPC container is the truck, which transports the money (USD, Bitcoin, etc.) [[00:31:26]]. The value itself is the money, and the unique identifier of each container or Satoshi (in Bitcoin) makes it non-fungible, akin to the serial number on paper money [[00:33:15]].

## TOA IP vs. Traditional Blockchain

TOA IP is described as a "ledger-less blockchain" [[00:36:56]]. While it incorporates blockchain principles like chaining events and cryptographic proofs, it does not rely on a global ledger for every micro-transaction. This fundamentally differentiates it from conventional blockchains, which often face issues of expense, slowness, and complexity due to their ledger-centric design [[00:34:51]].

However, the Hypercycle team acknowledges the utility of traditional blockchains for specific purposes, such as:
*   **Zero-Knowledge Proofs**: Innovations like ZK-snarks originated in the blockchain world and are valuable [[00:35:54]].
*   **Software Licensing**: Using smart contracts (e.g., ERC721 with ERC1155 tokens) for software licenses is more efficient than traditional paperwork, reducing transaction time from days to seconds [[00:37:50]].
*   **Financial Onboarding**: Leveraging existing financial systems where they are already plugged in, such as Ethereum for USDC, for easier onboarding [[00:30:18]].

## Focus on AI Compute and Services

TOA IP and Hypercycle specifically focus on AI computation and services, rather than general computing [[00:46:00]]. This strategic decision was made to avoid direct competition with established financial institutions and ledger-based blockchain entities that would view peer-to-peer money transfers as a threat [[00:47:07]].

By focusing on AI, which requires sophisticated computation and cannot be easily faked by humans, the system positions itself in a "new territory" where disruption is welcomed [[00:48:44]]. This allows the system to remain specialized in facilitating a "market in results" rather than just a market in raw compute power [[00:56:13]]. The value appreciated in the system is not merely the revenue generated by an AI service, but also the "wealth creation" inherent in the intellectual property and reputation of that service, which belongs to the node operator [[00:52:12]].

## Facilitating AGI

The network is designed to accelerate the development of [[evaluating_ai_understanding_and_capability | AGI]] (Artificial General Intelligence) by allowing AI agents to constantly interact, exchange services, and become "smarter" and earn money in fractions of a second [[00:57:16]]. This interaction fosters a decentralized approach to AGI development, in contrast to a single entity controlling it [[01:00:26]].

This [[decentralized_governance_and_its_impact_on_ai_development | decentralized governance]] approach aims to ensure that AGI is not controlled by a single entity's ethical framework, reducing risks associated with centralized power. Instead, it allows for a diverse, global economic contribution to AGI's evolution, with specialized AI components (e.g., image interpretation, [[the_role_of_language_and_perception_in_ai | language part]] translation) potentially owned and developed by different entities across the globe [[01:03:01]]. This creates a safer path to [[ai_and_human_coexistence | AGI]] where humanity's "weakness" (inability for two people to agree on ethics) becomes its strength, preventing any single, potentially biased, AGI from dominating [[01:06:21]].

## Getting Involved

For developers and individuals interested in participating in the Hypercycle network, there are two main avenues:
*   **Capital**: Nodes can be purchased (e.g., a node for $160, or a "node factory" for about $1,000, which can spawn 1,024 nodes over time) [[01:08:38]]. These nodes can generate revenue, creating a business opportunity [[01:09:20]].
*   **Knowledge**: Individuals can learn to run nodes, which are in high demand [[01:11:00]]. Documentation is available on hypercycle.ai, including whitepapers and hackathon materials that guide users through the process of setting up and operating their own nodes, even for those new to the system [[01:10:35]]. Development on Hypercycle nodes primarily uses Python, though it also supports the Ethereum Virtual Machine (EVM) [[01:12:24]].

## Relationship with SingularityNET

Hypercycle is highly complementary to projects like [[ben_goertzels_perspective_on_ai_architectures_and_projects | SingularityNET]]. While SingularityNET focuses on the AI operating system and the AI node itself, Hypercycle provides the underlying secure network infrastructure that enables any AI agent (whether from SingularityNET, Microsoft, Google, or Tencent) to communicate and transact with any other agent on a micro-agent level securely and efficiently [[01:13:25]]. This acts as an "internet of AI," providing a secure communication layer (like HTTPS or TCP) that allows previously siloed AI clusters to interoperate and compensate each other without fear of being blocked or compromised [[01:14:28]].