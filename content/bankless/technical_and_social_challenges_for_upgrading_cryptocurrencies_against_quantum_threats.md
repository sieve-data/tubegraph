---
title: Technical and social challenges for upgrading cryptocurrencies against quantum threats
videoId: 5DRDjeMmOPw
---

From: [[bankless]] <br/> 

The emergence and development of quantum computing pose significant technical and social challenges for the security and future of cryptocurrencies like Bitcoin and Ethereum. While a direct threat isn't immediate, the long-term implications necessitate proactive measures and potential fundamental shifts in current cryptographic foundations <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

## Understanding Quantum Computing's Impact

### How Quantum Computers Differ

Unlike classical computers that use bits (0s or 1s), quantum computers utilize "qubits" which can exist in "superposition states" – a combination of both 0 and 1 simultaneously <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. This allows them to harness nature to perform computations in a fundamentally new way, potentially changing what is efficiently computable <a class="yt-timestamp" data-t="02:16:16">[02:16:16]</a>.

The ability to perform these complex calculations stems from "amplitudes," which are numbers (positive, negative, or even complex) attached to the possibility of a qubit being in a certain state <a class="yt-timestamp" data-t="02:21:02">[02:21:02]</a>. When dealing with multiple qubits, the number of required amplitudes grows exponentially (e.g., 2 to the 100th power for 100 qubits) <a class="yt-timestamp" data-t="02:49:15">[02:49:15]</a>. This exponentiality, known to chemists and physicists for generations, is what a quantum computer aims to exploit <a class="yt-timestamp" data-t="02:59:15">[02:59:15]</a>.

The challenge lies in orchestrating "interference" patterns where wrong answers cancel out (positive and negative amplitudes) while correct answers reinforce (amplitudes pointing the same way) <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a>. This is how quantum algorithms can achieve significant speedups for specific problems <a class="yt-timestamp" data-t="03:41:03">[03:41:03]</a>.

### Algorithms and Vulnerabilities

Two primary quantum algorithms are relevant to cryptocurrency security:
*   **Shor's Algorithm:** This algorithm offers an exponential speedup for problems like factoring large numbers and discrete logarithms <a class="yt-timestamp" data-t="03:07:08">[03:07:08]</a>. These problems underpin much of modern public-key cryptography, including RSA, Diffie-Hellman, and elliptic curve cryptography (ECC) <a class="yt-timestamp" data-t="03:15:05">[03:15:05]</a>.
*   **Grover's Algorithm:** While not an exponential speedup, Grover's algorithm provides a quadratic speedup (square root of the number of steps) for searching large lists of possible solutions <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>. This is relevant for "proof of work" problems that involve inverting hash functions <a class="yt-timestamp" data-t="00:59:54">[00:59:54]</a>.

> [!WARNING]
> Quantum computers pose a threat primarily to public-key encryption based on Abelian group problems (like factoring or discrete logarithms). This includes elliptic curve cryptography (ECDSA, BLS signatures) widely used in Bitcoin and Ethereum <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.
>
> Symmetric key cryptography (e.g., AES, DES) is not efficiently broken by quantum computers; they only offer a modest speedup <a class="yt-timestamp" data-t="00:53:56">[00:53:56]</a>.

### Current State and Timeline

Quantum computing development has progressed significantly from theoretical predictions to engineering milestones <a class="yt-timestamp" data-t="01:01:43">[01:01:43]</a>. Google's "Willow" chip, featuring 103 physical qubits, demonstrated a breakthrough in quantum error correction by preserving an encoded qubit for longer durations as scale increases <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This validates theories from the 1990s <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a>.

However, a fault-tolerant quantum computer capable of breaking cryptographic codes would require millions of physical qubits, potentially housed in hundreds or thousands of dilution refrigerators (the "upside down wedding cakes" that cool chips to near absolute zero) <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>, connected by a quantum communications network <a class="yt-timestamp" data-t="01:51:56">[01:51:56]</a>. This is still a significant engineering undertaking <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>.

The timeline for a quantum computer capable of breaking mainstream cryptography is uncertain. Estimates vary, but a fully functional, fault-tolerant quantum computer useful for quantum simulations is expected within the next decade <a class="yt-timestamp" data-t="00:47:43">[00:47:43]</a>. Breaking RSA specifically, with a 2048-bit key, might take a week on early fault-tolerant quantum computers <a class="yt-timestamp" data-t="00:55:37">[00:55:37]</a>. This time could decrease significantly as technology advances <a class="yt-timestamp" data-t="01:08:13">[01:08:13]</a>.

Current global spending on quantum information research and development is estimated at around $40 billion per year <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a>. Private companies like Google, IBM, QuEra, and IonQ are leading efforts, with less public visibility into government-led initiatives in countries like China <a class="yt-timestamp" data-t="01:09:52">[01:09:52]</a>.

> [!INFO]
> The transition to [[quantum_computing_development_and_milestones | post-quantum cryptography]] standards, particularly those based on lattices, is already being urged by NIST (National Institute of Standards and Technology) and adopted by companies like Google <a class="yt-timestamp" data-t="01:34:46">[01:34:46]</a>. ECDSA, a common cryptographic algorithm in crypto, will be deprecated by NIST in 2030 and disallowed in 2035 <a class="yt-timestamp" data-t="01:33:58">[01:33:58]</a>.

## Challenges for Bitcoin

[[quantum_computings_potential_to_break_bitcoin_and_ethereum | Bitcoin]] faces a two-pronged challenge from quantum computers: account security and its proof-of-work mechanism <a class="yt-timestamp" data-t="01:41:40">[01:41:40]</a>.

### Account Security (ECDSA)

Bitcoin relies on ECDSA (Elliptic Curve Digital Signature Algorithm) for digital signatures, which are vulnerable to quantum attacks <a class="yt-timestamp" data-t="00:57:07">[00:57:07]</a>. A sufficiently fast quantum computer could forge signatures by deriving private keys from public keys, allowing an attacker to steal funds <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.

> [!NOTE]
> One mitigation strategy is to only reveal your public key for a very short period (e.g., minutes) while a transaction is being confirmed <a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>. However, this relies on the assumption that cracking a key takes a significant amount of time (days to a week) <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>. If quantum computers become fast enough to crack keys in seconds, this mitigation would be insufficient <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>.

### Proof of Work (Mining)

Bitcoin's proof-of-work mechanism, which involves miners finding pre-images of a hash function, could be accelerated by Grover's algorithm <a class="yt-timestamp" data-t="00:59:54">[00:59:54]</a>. While this is a modest speedup (square root), it introduces a significant risk during the transition from classical to quantum mining.

> [!WARNING]
> If one entity gains a dominant quantum computing advantage in mining (e.g., controlling over 50% of the hash rate) <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>:
> *   They could acquire all issuance and fees for free by setting the difficulty too high for classical miners <a class="yt-timestamp" data-t="01:55:22">[01:55:22]</a>.
> *   They could gain monopoly power over transaction fees, potentially charging arbitrary percentages like 3% or 30% <a class="yt-timestamp" data-t="01:56:09">[01:56:09]</a>.
> *   They could [[bitcoins_security_budget_and_roadmap_challenges | short Bitcoin on perpetual markets]] while simultaneously attacking the network, potentially leading to a massive financial gain and destabilization <a class="yt-timestamp" data-t="01:57:10">[01:57:10]</a>.

### The Social Dilemma: Immutability vs. Survival

Upgrading Bitcoin's cryptography would require a hard fork, a contentious process in the Bitcoin community due to its emphasis on immutability and resistance to changes in its core protocol or property rights <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>.

A particularly problematic aspect is the existence of "lost coins," including Satoshi's 1 million Bitcoin and an estimated 1 to 4 million more Bitcoin <a class="yt-timestamp" data-t="01:11:09">[01:11:09]</a>. These early coins have public keys exposed on-chain, making them vulnerable to quantum attacks <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>.

> [!WARNING]
> If these "lost coins" cannot be upgraded or moved by their original owners, they become a massive "bounty" for the first entity to build a sufficiently powerful quantum computer <a class="yt-timestamp" data-t="01:11:50">[01:11:50]</a>. This could be a nation-state or a private company <a class="yt-timestamp" data-t="01:09:35">[01:09:35]</a>.
>
> The community would face a stark choice:
> 1.  **Do nothing:** Allow the vulnerable coins to be stolen, potentially leading to significant centralization of wealth and jeopardizing Bitcoin's fundamental principles <a class="yt-timestamp" data-t="01:51:59">[01:51:59]</a>.
> 2.  **Social intervention:** Implement a hard fork to "burn" or "freeze" these vulnerable coins, which would contradict Bitcoin's ethos of immutable property rights <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.
>
> The 2010 overflow bug, which required a rollback, serves as a historical precedent for protocol changes in Bitcoin's early days, but a similar intervention now would face immense social and ideological hurdles <a class="yt-timestamp" data-t="01:48:17">[01:48:17]</a>.

Some theories suggest Bitcoin's long-term survival might involve the BTC asset decoupling from the chain to live on a more secure platform, or a quantum-induced "issuance" where quantum computers unlock old 50 BTC blocks over time, inadvertently providing security budget <a class="yt-timestamp" data-t="01:43:56">[01:43:56]</a>.

## Challenges and Solutions for Ethereum

Ethereum, particularly after "The Merge" to proof of stake, is in a relatively better position to address quantum threats compared to Bitcoin <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>.

### Consensus Layer (BLS Signatures)

Ethereum's Beacon Chain currently uses BLS signatures for its consensus mechanism, which are not post-quantum secure <a class="yt-timestamp" data-t="01:30:02">[01:30:02]</a>.

> [!NOTE]
> Ethereum researchers are developing [[challenges_in_ethereums_upgrade_processes | post-quantum secure cryptographic solutions]] that offer similar aggregation properties to BLS signatures, with a plausible upgrade path within the next half-decade <a class="yt-timestamp" data-t="01:30:13">[01:30:13]</a>. Proof of stake itself is considered much more secure against quantum attacks than proof of work <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>.

### Account Security (ECDSA)

Ethereum accounts also use ECDSA for digital signatures, similar to Bitcoin <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.

> [!NOTE]
> Ethereum has several advantages:
> *   **Account Abstraction:** This allows accounts to define their own signature schemes, enabling users to migrate to [[impact_of_quantum_computing_on_cryptography_and_cryptocurrency | post-quantum signatures]] without a network-wide hard fork <a class="yt-timestamp" data-t="01:06:33">[01:06:33]</a>.
> *   **Hash of Public Key:** From day one, Ethereum addresses have been the hash of the public key, not the public key itself. This means that even lost coins are generally not exposed to quantum attacks unless their public key is revealed during a transaction <a class="yt-timestamp" data-t="02:03:31">[02:03:31]</a>. This significantly limits the amount of vulnerable "lost" Ether (estimated at 0.1% of supply) <a class="yt-timestamp" data-t="02:05:59">[02:05:59]</a>.

### Data Availability (Blobs)

Ethereum's data availability layer, using "blobs" with KCG (elliptic curve-based) cryptography, will also need to be upgraded for [[impact_of_quantum_computing_on_cryptography_and_cryptocurrency | quantum resistance]] <a class="yt-timestamp" data-t="02:07:40">[02:07:40]</a>.

> [!NOTE]
> Researchers are exploring "blob abstraction," a new design that would make the data availability layer more flexible and efficient, while also integrating post-quantum security <a class="yt-timestamp" data-t="02:08:24">[02:08:24]</a>.

### State Management (Merkle Trees)

Ethereum's current Patricia Merkle Tree for its state is post-quantum secure <a class="yt-timestamp" data-t="02:09:32">[02:09:32]</a>. However, there's a possibility of moving to a different Merkle tree (e.g., Verkle trees) for efficiency gains, which might not be post-quantum secure <a class="yt-timestamp" data-t="02:09:47">[02:09:47]</a>.

> [!NOTE]
> The preferred long-term solution is to move directly to a binary Merkle tree with a "snark-friendly" hash function (like Poseidon), which would offer both efficiency benefits and post-quantum security, avoiding intermediate forks <a class="yt-timestamp" data-t="02:10:30">[02:10:30]</a>.

### Ethereum's Approach to Upgrades

Ethereum's history of significant upgrades, such as The Merge, demonstrates its capacity for complex protocol changes through social consensus <a class="yt-timestamp" data-t="00:58:39">[00:58:39]</a>. The challenges presented by quantum computing are viewed as opportunities to improve and refine the protocol <a class="yt-timestamp" data-t="02:14:04">[02:14:04]</a>.

> [!NOTE]
>
> **Trade-offs:** Post-quantum signatures tend to be about 10 times larger, leading to increased gas costs for users and higher bandwidth load for validators <a class="yt-timestamp" data-t="01:06:59">[01:06:59]</a>. Researchers are actively working on solutions to manage this, such as improved peer-to-peer network architecture <a class="yt-timestamp" data-t="01:32:30">[01:32:30]</a>.
>
> **Quantum Canary:** Ethereum could implement a "Quantum Canary" mechanism, an immutable smart contract that automatically triggers a migration to post-quantum cryptography once a small, provable quantum computer exists, ensuring timely upgrades without manual governance <a class="yt-timestamp" data-t="02:06:36">[02:06:36]</a>.
>
> The overall goal is to have a post-quantum secure Ethereum within a five-year timescale, well before quantum computers pose a critical threat, with the current roadmap aiming for a system that can last for decades or centuries without further cryptographic changes <a class="yt-timestamp" data-t="02:14:18">[02:14:18]</a>.

## Future Concepts: Quantum Money and One-Shot Signatures

Beyond simply upgrading existing cryptocurrencies, quantum mechanics also offers revolutionary possibilities for the future of digital money.

*   **[[future_implications_of_quantum_money_and_cryptography | Quantum Money]]:** Based on the fundamental "no-cloning theorem" of quantum mechanics (which states an unknown quantum state cannot be copied), quantum money could create physically unclonable digital cash <a class="yt-timestamp" data-t="02:55:51">[02:55:51]</a>. This concept, dating back to the 1960s, would allow for peer-to-peer transactions without the need for a blockchain or global consensus, similar to physical cash <a class="yt-timestamp" data-t="02:42:58">[02:42:58]</a>. Verifying a quantum bill would be possible by anyone, not just a central bank <a class="yt-timestamp" data-t="02:46:58">[02:46:58]</a>. However, this would require quantum computers capable of preserving quantum states for arbitrary amounts of time and a "Quantum Internet" to transmit these states <a class="yt-timestamp" data-t="02:57:31">[02:57:31]</a>.
*   **One-Shot Signatures:** A concept closely related to quantum money, one-shot signatures allow a private key to sign only a single message before destroying itself <a class="yt-timestamp" data-t="02:17:15">[02:17:15]</a>. This could enable "perfect finality" in proof-of-stake systems like Ethereum, preventing validators from voting for inconsistent chains (equivocation) by making it physically impossible to sign two messages with the same epoch number <a class="yt-timestamp" data-t="02:19:55">[02:19:55]</a>. This would enhance trustlessness in delegated staking by eliminating the risk of slashing from operator misbehavior <a class="yt-timestamp" data-t="02:22:58">[02:22:58]</a>. Implementing one-shot signatures would likely occur after the development of sufficiently powerful Grover's and Shor's algorithms <a class="yt-timestamp" data-t="02:23:07">[02:23:07]</a>.

## Conclusion

The [[impact_of_quantum_computing_on_cryptography_and_cryptocurrency | impact of quantum computing on cryptography and cryptocurrency]] is a long-term challenge, measured in decades rather than years <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. While Bitcoin faces significant social and technical hurdles due to its design principles and the issue of vulnerable "lost coins," Ethereum appears better positioned with its adaptable roadmap and historical precedent for protocol upgrades. The ultimate "Rector scale" impact will differ, with Ethereum potentially experiencing a manageable "four" and Bitcoin a more disruptive "five, six, or seven" <a class="yt-timestamp" data-t="02:12:12">[02:12:12]</a>. The shift to quantum-resistant cryptography is already underway in the broader tech industry, and cryptocurrencies will need to adapt to survive this inevitable technological evolution <a class="yt-timestamp" data-t="01:34:57">[01:34:57]</a>.