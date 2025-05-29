---
title: Upgrading blockchain systems for quantum resistance
videoId: 5DRDjeMmOPw
---

From: [[bankless]] <br/> 
## Upgrading Blockchain Systems for Quantum Resistance

Quantum computing advancements pose significant [[Future challenges for Bitcoin with quantum advancements | challenges]] to the security and consensus mechanisms of existing blockchain systems like Bitcoin and Ethereum <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. While not an immediate threat, the theoretical groundwork for quantum attacks on current cryptography is established, necessitating future upgrades for quantum resistance <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>.

### Understanding Quantum Computing Threats

Unlike classical computers, [[Quantum computing and cryptography | quantum computers]] harness quantum mechanical phenomena like superposition and interference to perform computations in fundamentally new ways <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. This allows them to tackle specific, complex problems exponentially faster than classical supercomputers <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>.

The core threat to current cryptography stems from two primary quantum algorithms:
*   **Shor's Algorithm**: Discovered by Peter Shor in 1994, this algorithm can efficiently factor large numbers and solve the discrete logarithm problem <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>. These problems underpin the security of widely used public-key encryption schemes such as RSA, Diffie-Hellman, and elliptic curve cryptography (ECC) <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>. If a large-scale quantum computer can run Shor's algorithm, it could break a significant portion of the internet's current encryption, including the digital signatures used in Bitcoin and Ethereum <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>.
*   **Grover's Algorithm**: This algorithm offers a quadratic speedup for searching unsorted databases or inverting hash functions <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>. While not an exponential speedup like Shor's, it means that for a cryptographic hash function, an attacker might need to do only the square root of the work a classical computer would need <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>. This primarily affects [[Impact of quantum computing on Bitcoin mining | proof-of-work]] mining <a class="yt-timestamp" data-t="00:59:41">[00:59:41]</a>.

It is important to note that not all cryptography is equally vulnerable. Symmetric-key cryptography (e.g., AES, DES) and hash functions (for collision resistance) are not efficiently broken by quantum computers, though a quantum computer might reduce the effective key size <a class="yt-timestamp" data-t="00:54:05">[00:54:05]</a>.

### Current State and Future Outlook of Quantum Computing

Recent developments, such as Google's Willow chip announced in December 2023 (paper available since summer), represent significant engineering milestones <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>. The Willow chip features 103 superconducting qubits arranged in a 10x10 grid and successfully demonstrated quantum error correction using the surface code, preserving an encoded qubit for longer durations as the system scaled <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This experimentally confirms theoretical predictions from the 1990s <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

While current quantum computers still require millions of physical qubits to break cryptographic codes, often housed in specialized dilution refrigerators cooled to near absolute zero, the progress indicates that the theoretical underpinnings are sound <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>. Experts predict that a "useful fault-tolerant quantum computer" could emerge within the next decade <a class="yt-timestamp" data-t="00:47:43">[00:47:43]</a>. Breaking a 2048-bit key might initially take a week, but these costs are expected to decrease over time, similar to Moore's Law in classical computing <a class="yt-timestamp" data-t="00:55:37">[00:55:37]</a>.

### Impact on Bitcoin

Bitcoin faces a two-pronged challenge from quantum computing due to its reliance on both elliptic curve digital signatures (ECDSA) for accounts and hash functions for [[Impact of quantum computing on Bitcoin mining | proof-of-work]] mining <a class="yt-timestamp" data-t="01:41:57">[01:41:57]</a>.

#### Signature Vulnerability (ECDSA)

Bitcoin addresses and transactions use ECDSA, which is vulnerable to Shor's algorithm <a class="yt-timestamp" data-t="01:03:58">[01:03:58]</a>. If a quantum computer can derive a private key from a public key, it could forge signatures and steal funds <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>.

*   **Lost/Stagnant Coins**: A significant portion of Bitcoin's supply, estimated between 1 million (Satoshi's coins) and 4 million total, may be particularly vulnerable <a class="yt-timestamp" data-t="01:11:09">[01:11:09]</a>. These coins are often in old addresses where the public key is already exposed on the blockchain <a class="yt-timestamp" data-t="01:08:49">[01:08:49]</a>. If an attacker can quickly crack keys (e.g., in seconds), this could lead to a massive transfer of value, akin to the Ethereum DAO hack <a class="yt-timestamp" data-t="01:45:05">[01:45:05]</a>.
*   **Upgrade Path**: A "hard fork" would be required to introduce a new, quantum-resistant signature scheme (e.g., lattice-based cryptography) <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>. However, this poses a significant social and philosophical challenge for the Bitcoin community, which highly values immutability and resistance to changes in property rights <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
    *   A "soft fork" could potentially freeze vulnerable coins by censoring transactions, but this also requires community consensus <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>.
    *   One proposed mitigation for active users is to only expose their public key for a short period (e.g., during transaction inclusion), but this assumes the quantum attack time is longer than the exposure time <a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>.

#### Proof of Work Vulnerability

Bitcoin's proof-of-work mining relies on hash functions that could be sped up by Grover's algorithm <a class="yt-timestamp" data-t="01:18:02">[01:18:02]</a>.
*   **Centralization Risk**: If a few entities or a single nation-state acquire scalable quantum computers, they could gain a significant advantage in mining, potentially controlling more than 50% of the hash rate <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>. This would allow them to dictate transaction fees, block inclusion, and even engage in 51% attacks <a class="yt-timestamp" data-t="01:56:06">[01:56:06]</a>.
*   **Difficulty Adjustment**: While the proof-of-work difficulty adjusts automatically to compensate for increased hashing power, the transition period, where a single entity might have a disproportionate advantage, is problematic <a class="yt-timestamp" data-t="01:19:39">[01:19:39]</a>.
*   **Hard Fork**: A hard fork to a quantum-resistant proof-of-work algorithm (e.g., one less susceptible to Grover's speedup or a proof-of-space protocol) is theoretically possible but would require immense social consensus <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

### Impact on Ethereum

Ethereum is in a more favorable position regarding quantum resistance than Bitcoin <a class="yt-timestamp" data-t="02:13:05">[02:13:05]</a>.

#### Signature Vulnerability (ECDSA & BLS Signatures)

Ethereum uses ECDSA for accounts (similar to Bitcoin) <a class="yt-timestamp" data-t="01:36:12">[01:36:12]</a> and BLS signatures for its proof-of-stake consensus layer (Beacon Chain) <a class="yt-timestamp" data-t="01:29:59">[01:29:59]</a>. Both are susceptible to Shor's algorithm.

*   **Accounts**: Ethereum has an advantage due to "account abstraction," which allows accounts to define their own signature schemes without a hard fork <a class="yt-timestamp" data-t="01:06:35">[01:06:35]</a>. This means large holders can migrate to quantum-resistant signatures today <a class="yt-timestamp" data-t="02:02:51">[02:02:51]</a>.
    *   Additionally, from day one, Ethereum addresses were typically the hash of the public key, reducing the exposure of vulnerable public keys compared to Bitcoin <a class="yt-timestamp" data-t="02:03:31">[02:03:31]</a>. The percentage of vulnerable lost or stagnant coins is estimated to be much smaller (e.g., 0.1% of Eth supply) <a class="yt-timestamp" data-t="02:06:04">[02:06:04]</a>, making a social intervention less likely or less impactful <a class="yt-timestamp" data-t="02:05:08">[02:05:08]</a>.
    *   A "Quantum Canary" mechanism is being explored, where a smart contract could automatically switch to post-quantum cryptography if a proof of small quantum computers (but not yet capable of breaking crypto) is provided on-chain <a class="yt-timestamp" data-t="02:06:32">[02:06:32]</a>.
*   **Consensus Layer (BLS Signatures)**: While BLS signatures are not quantum-secure, the Ethereum community has a plausible upgrade path to quantum-resistant aggregation signatures, potentially within the next half-decade <a class="yt-timestamp" data-t="01:30:13">[01:30:13]</a>. This would require a hard fork, but Ethereum has a history of successful major upgrades (e.g., The Merge) <a class="yt-timestamp" data-t="00:58:39">[00:58:39]</a>.
*   **Blobs (KCG Commitments)**: Ethereum's data availability layer (blobs) uses KCG commitments, which are elliptic-curve-based and thus not quantum-secure <a class="yt-timestamp" data-t="02:07:43">[02:07:43]</a>. This will require an upgrade, which is seen as an opportunity to implement a more efficient "blob abstraction" design <a class="yt-timestamp" data-t="02:08:24">[02:08:24]</a>.
*   **Merkle Trees**: While the current Patricia Merkle tree is quantum-secure, future plans to switch to more efficient Merkle tree variants (e.g., Verkle trees) might involve non-quantum-secure cryptography <a class="yt-timestamp" data-t="02:09:47">[02:09:47]</a>. The current thinking is to move directly to a binary Merkle tree with SNARK-friendly hash functions (like Poseidon) that are also quantum-secure, avoiding intermediate non-quantum-safe steps <a class="yt-timestamp" data-t="02:10:23">[02:10:23]</a>.

#### Proof of Stake Advantage

Unlike Bitcoin, Ethereum's shift to proof-of-stake removes the [[Impact of quantum computing on Bitcoin mining | proof-of-work]] vulnerability to Grover's algorithm <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>. This makes Ethereum's consensus mechanism inherently more resistant to quantum attacks <a class="yt-timestamp" data-t="01:30:40">[01:30:40]</a>. Furthermore, [[Security and Consensus in Ethereum Upgrades | one-shot signatures]], a concept related to [[Quantum money and its implications | quantum money]], could be implemented to achieve "perfect finality" by making equivocation physically impossible for validators <a class="yt-timestamp" data-t="02:19:55">[02:19:55]</a>.

### Post-Quantum Cryptography and the Future

The National Institute of Standards and Technology (NIST) held a competition from 2017 to 2022 to identify and standardize post-quantum cryptography <a class="yt-timestamp" data-t="01:34:22">[01:34:22]</a>. This effort converged on lattice-based cryptography as the primary quantum-resistant alternative <a class="yt-timestamp" data-t="01:34:32">[01:34:32]</a>, and industries like Google are already beginning the transition <a class="yt-timestamp" data-t="01:34:51">[01:34:51]</a>.

The transition to quantum-resistant cryptography for blockchains is an engineering and social challenge, not a theoretical one <a class="yt-timestamp" data-t="01:30:50">[01:30:50]</a>. While Bitcoin faces significant hurdles due to its historical design choices and community ethos regarding immutability, Ethereum appears to have a clearer roadmap for upgrading its systems to withstand quantum threats <a class="yt-timestamp" data-t="02:13:05">[02:13:05]</a>. The long-term viability of blockchains, especially in a world with advanced quantum computing, might depend on their ability to adapt and implement these quantum-resistant solutions <a class="yt-timestamp" data-t="02:14:48">[02:14:48]</a>.