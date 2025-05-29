---
title: Quantum computing and cryptography
videoId: 5DRDjeMmOPw
---

From: [[bankless]] <br/> 

[[Quantum computing and AI | Quantum computing]] is poised to significantly impact internet money and finance, raising questions about the security of cryptocurrencies like Bitcoin and Ethereum against advanced computational threats [00:00:27]. Experts like theoretical computer scientist Scott Aaronson and Ethereum Foundation researcher Justin Drake are exploring this frontier, with crypto being seen as a "canary in the coal mine" for how quantum advancements will affect wider society [00:00:44, 00:00:52, 00:03:03].

## Understanding Quantum Computing

A quantum computer is not merely a faster classical computer; it leverages the fundamental laws of quantum mechanics to perform computations in a fundamentally new way [00:20:09, 00:21:24]. It is the first device since Alan Turing's work that changes the basic rules of what is efficiently computable [00:21:32].

Key characteristics:
*   **Superposition States** Quantum bits (qubits) can exist in a superposition of multiple states (e.g., both 0 and 1 simultaneously), unlike classical bits [00:21:50, 00:22:02].
*   **Amplitudes** Each possible state is associated with an "amplitude," which can be positive, negative, or even complex numbers, unlike probabilities [00:22:09, 00:23:15, 02:22:47]. Nature internally uses these vast numbers of parameters to track the states of particles [00:24:52, 02:25:09].
*   **Interference** The core of quantum algorithms is to choreograph patterns of interference. For wrong answers, amplitudes cancel each other out, while for correct answers, they reinforce, boosting the probability of seeing the desired outcome upon measurement [00:33:57, 02:22:47]. This is distinct from simply trying every possible solution in parallel [00:32:00].
*   **Specialized Tasks** While quantum computers can do anything a classical computer can, they are only useful for specific tasks where they can achieve a significant advantage [01:13:09, 01:13:34, 01:36:06, 01:36:31]. Most everyday computer tasks would see little to no benefit [01:13:36].

## Quantum Computing Milestones and Timeline

In December, Google announced a breakthrough with its Willow chip, a state-of-the-art [[Quantum Computing and AI | quantum computing]] chip designed to reduce errors exponentially as it scales up with more qubits [00:07:02]. Scott Aaronson described this as an "engineering milestone" rather than a new theoretical discovery, confirming predictions from the 1990s about quantum error-correcting codes [00:07:45, 00:07:56].

*   **Willow Chip Details** The Willow chip uses 103 superconducting physical qubits, arranged in a 10x10 grid, to implement a "surface code" for quantum error correction [00:09:06, 00:09:26]. For the first time, scaling to larger surface codes (e.g., 3x3 to 5x5) has demonstrated the preservation of an encoded qubit for longer periods, passing a critical threshold [00:09:38, 00:09:56].
*   **Current Limitations** While significant, this is not yet a "full scalable, fault-tolerant quantum computation." It currently involves only one encoded qubit [01:00:20, 01:00:27]. Breaking cryptographic codes would require millions of physical qubits, potentially housed in hundreds or thousands of dilution refrigerators, interconnected by a quantum communication network [01:00:50, 01:51:01, 01:52:05].
*   **Physical Appearance** The distinctive "weird" appearance of quantum computers in pictures (like upside-down wedding cakes) is primarily due to the large dilution refrigerators required to cool chips to extremely low temperatures (e.g., 10 millikelvin) to maintain qubit isolation and coherence [01:42:23, 01:42:55].
*   **Progress and Investment** The field has seen incredible progress in qubit fidelity, approaching the 99.8-99.9% accuracy needed for effective quantum error correction [01:16:06, 01:17:04]. Global investment in quantum information research and development is estimated at $40 billion per year [01:49:04].
*   **Timeline Speculation** While precise timelines are uncertain, Aaronson suggests that within the next decade, "useful, fault-tolerant quantum computers" capable of quantum simulations will likely emerge, even if not immediately capable of breaking RSA [01:47:43, 01:48:06]. For breaking cryptographic codes, the cost is currently estimated in the billions of dollars [01:48:39].

## [[Impact of quantum computing on Bitcoin mining | Impact on Cryptography]]

The advent of powerful quantum computers poses a direct threat to many current cryptographic standards.

### Shor's Algorithm

Discovered by Peter Shor in 1994, this algorithm can achieve dramatic, exponential speedups for problems that have specific algebraic structures, particularly those involving "abelian groups" [00:30:02, 00:37:15].
*   **Targets:** Shor's algorithm can efficiently find the prime factors of large numbers. This directly threatens the security of a large fraction of current internet encryption, including:
    *   RSA [00:30:27, 00:36:36]
    *   Diffie-Hellman (based on discrete logarithms) [00:31:22, 00:36:57]
    *   Elliptic Curve Cryptography (ECC) [00:31:30, 00:37:01]
*   **Mechanism:** Shor's algorithm's core is period finding, which is accomplished using a "Quantum Fourier Transform" that manipulates amplitudes to create interference patterns [00:38:18, 00:38:41].
*   **General Purpose:** Once a quantum computer can break one type of elliptic curve cryptography, it will likely be a programmable device capable of breaking other public-key encryption schemes like RSA and Diffie-Hellman as well [00:53:20].

### Grover's Algorithm

This algorithm offers a more modest "quadratic" speedup (square root of the number of steps) for general search problems [01:01:00, 01:01:07].
*   **Targets:** It applies to almost any problem involving searching a giant list of possible solutions, including hash functions used in Proof of Work [01:00:42, 01:00:57].
*   **Limitations:** Due to the enormous overhead of quantum error correction (possibly a million-fold factor), Grover's algorithm might not offer a net win for mining problems until the problem size (N) reaches a trillion, meaning it would likely not be a win for cryptocurrency mining immediately after fault-tolerant quantum computers emerge [01:01:39, 01:02:18, 01:02:40, 01:02:54].

### Quantum-Resistant Cryptography

Not all cryptography is vulnerable to quantum attacks.
*   **Symmetric Key Cryptography:** Algorithms like DES and AES are not efficiently breakable by quantum computers; they only see a modest difference [00:54:07, 00:54:13, 01:00:10].
*   **Lattice-Based Cryptography:** This is a leading candidate for "post-quantum" or "quantum-resistant" encryption standards, already being urged by NIST (National Institute of Standards and Technology) for transition [00:54:01, 01:34:32, 01:34:40, 01:34:51]. Google is reportedly already implementing this transition [01:34:51].

## [[Future challenges for Bitcoin with quantum advancements | Impact on Bitcoin]]

Bitcoin faces a "doubly screwed" situation, as its security relies on both elliptic curves for digital signatures and hash functions for [[Impact of quantum computing on Bitcoin mining | Proof of Work]] [01:41:57, 01:42:21].

### Account Security (ECDSA)
*   Bitcoin's accounts (UTXOs) use ECDSA (Elliptic Curve Digital Signature Algorithm) for digital signatures, which is vulnerable to Shor's algorithm [01:04:38].
*   An attacker with a sufficiently fast quantum computer could forge signatures and steal funds, potentially prioritizing high-value accounts [01:04:01, 01:04:18].
*   Initial estimates for breaking a 2048-bit key might take a week, but this could decrease significantly to seconds in the future [01:08:02, 01:05:01, 01:05:22].
*   **Mitigation Strategy:** Users can expose only the hash of their public key, delaying the exposure of the public key until just before a transaction is included in a block [01:07:40, 01:07:51]. This makes the time window for an attack very short.
*   **Unupgradable Coins:** Between 1 to 4 million Bitcoin, including Satoshi's early coins, are vulnerable because their public keys were exposed on-chain at creation and cannot be upgraded with a soft fork [01:08:44, 01:10:58, 01:11:25, 01:15:16]. These "lost" or stagnant coins represent a potential bounty for the first entity to build a sufficiently powerful quantum computer [01:09:07, 01:11:50, 01:42:55].
*   **Social Conundrum:** Dealing with these unupgradable coins presents a major social challenge for Bitcoin, as it would require a hard fork to alter property rights, going against Bitcoin's core principles of immutability [01:14:17, 01:43:52, 01:46:59]. This could lead to a split in the community or even threaten the system's integrity [01:48:00, 01:49:14].

### Proof of Work
*   Bitcoin's Proof of Work (PoW) relies on hash functions, which are susceptible to Grover's algorithm [01:00:57, 01:57:00].
*   In a world with a few entities possessing scalable quantum computers, those entities could mine significantly more Bitcoin than others, leading to centralization of hash power [01:00:06, 01:18:21, 01:54:45].
*   If quantum computing becomes widespread, the difficulty adjustment mechanism would automatically make the Proof of Work harder, bringing everyone back to parity, but the transition period could be highly problematic due to performance discrepancies [01:18:47, 01:54:50, 01:59:57, 02:00:07].
*   A single dominant quantum miner could acquire control of the network, potentially setting high fees or even attempting to "kill" Bitcoin by shorting it in perp markets [01:55:12, 01:56:06, 01:57:08].
*   While quantum-resistant PoW algorithms or Proof of Space protocols exist, implementing them would require a hard fork, presenting another social upheaval for Bitcoin [02:01:16, 02:01:45, 02:02:16, 02:02:26].

## [[Upgrading blockchain systems for quantum resistance | Impact on Ethereum]]

Ethereum is considered better positioned to handle [[Quantum Computing and AI | quantum computing]] advancements due to its architecture and a history of successful network upgrades.

### Account Security (ECDSA)
*   Ethereum also uses ECDSA for accounts, making them vulnerable [01:04:38, 02:03:36].
*   **Advantages:**
    *   **Account Abstraction:** Ethereum's account abstraction allows users to define their own signature schemes, enabling migration to post-quantum secure signatures without a hard fork [01:06:35, 02:02:45].
    *   **Public Key Hashing:** From day one, Ethereum addresses have been the hash of the public key, reducing the exposure of keys on-chain compared to Bitcoin and limiting the number of passively vulnerable "lost coins" to a much smaller percentage (e.g., ~0.1% of ETH supply) [02:03:31, 02:03:50, 02:05:07, 02:05:59, 02:06:04].
    *   **Quantum Canary:** Ethereum could implement a "Quantum Canary" smart contract. This would allow a proof of concept of a small quantum computer to automatically trigger a switch to post-quantum cryptography on-chain, ensuring security while maintaining efficiency in the interim [02:06:34].

### Consensus Layer (BLS Signatures)
*   Ethereum's Beacon Chain currently uses BLS (Boneh-Lynn-Shacham) signatures for consensus, which are not post-quantum secure [01:30:00].
*   **Upgrade Path:** Researchers are working on new cryptography that offers the same aggregation properties as BLS but is quantum-resistant [01:30:13, 01:30:20]. This migration is plausible within the next half-decade [02:02:26, 02:02:54].
*   **Trade-offs:** Post-quantum signatures tend to be about 10 times larger, potentially increasing gas costs for transactions [01:06:59, 01:31:54]. However, optimizations like SNARKs for batching signatures can mitigate this [01:07:16].
*   **Proof of Stake:** Ethereum's move to Proof of Stake makes it more resilient to the mining-related issues that Bitcoin faces with Grover's algorithm [01:30:40, 01:57:00].

### Other Components
*   **Blobs (KCG):** Ethereum's blobs, which use elliptic curve-based KCG technology for data availability, will need to be upgraded to be post-quantum secure [02:07:40, 02:07:43]. This presents an opportunity to improve blob design (e.g., variable size, blob abstraction) [02:07:54, 02:08:24].
*   **Merkle Trees:** While the current Patricia Merkle Tree is post-quantum secure, future upgrades like Verkle trees (potentially using non-quantum-secure cryptography for efficiency) would need to be carefully designed to ensure long-term quantum resistance (e.g., by moving directly to SNARK-friendly binary Merkle trees) [02:09:32, 02:09:47, 02:10:09, 02:10:30].

## [[Emerging trends in AI and crypto | Future Concepts and Overall Outlook]]

### [[Quantum money and its implications | Quantum Money]]
[[Quantum money and its implications | Quantum money]] is an older concept (from the 1960s, revived by Aaronson in 2009) that leverages the "no-cloning theorem" of quantum mechanics to create physically unclonable digital cash [01:25:10, 01:25:17, 01:26:00, 01:26:31].
*   **How it Works:** Private keys are quantum objects (superpositions) that are destroyed upon signing a message, preventing double-spending without needing a central ledger or consensus [01:24:52, 01:25:03, 01:27:01].
*   **Challenges:** Requires quantum computers that can preserve quantum states for arbitrary amounts of time and a [[Quantum Computing and AI | quantum communications]] network [01:27:31, 01:28:06].
*   **Comparison to Bitcoin:** While it could be a "better Bitcoin" by eliminating the need for consensus, it's not an improvement for Ethereum because it can't support smart contracts [02:16:50, 02:17:02].

### One-Shot Signatures
Related to [[Quantum money and its implications | quantum money]], one-shot signatures are a futuristic concept where a private key can only sign a single message before destroying itself [02:20:19].
*   **Application to Ethereum:** This could enable "perfect finality" on Ethereum by physically preventing validators from equivocating (voting for inconsistent chains), enhancing security beyond economic finality [02:19:27, 02:20:01]. It could also simplify delegation for liquid staking tokens (LSTs) by removing the need for trust in operators regarding slashing faults [02:21:26].
*   **Prerequisites:** Requires advanced quantum computing, specifically the ability to run Grover's and Shor's algorithms [02:22:56, 02:23:05].

### Conclusion
The overall outlook is that the threat from [[Quantum Computing and AI | quantum computers]] to cryptography is a "solvable problem" and a "survivable headache," akin to Y2K rather than an existential doom for cryptocurrency [00:59:06, 01:35:50, 01:56:06]. Ethereum appears to have a clearer roadmap for [[upgrading_blockchain_systems_for_quantum_resistance | upgrading its systems]] to be quantum-resistant within the next 5-7 years, with less social friction due to its adaptable nature [02:11:15, 02:13:05, 02:14:10, 02:14:30]. Bitcoin faces more significant social and technical challenges due to its rigidity and the issue of unupgradable early coins [02:13:16, 02:14:10]. The market is not yet pricing in these long-term quantum threats, but that could change as quantum capabilities advance [02:15:01, 02:15:11].