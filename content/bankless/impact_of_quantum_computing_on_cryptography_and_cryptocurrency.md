---
title: Impact of quantum computing on cryptography and cryptocurrency
videoId: 5DRDjeMmOPw
---

From: [[bankless]] <br/> 

Quantum computing stands at the frontier of technology, with its potential impact on [[future_implications_of_quantum_money_and_cryptography | cryptography]] and digital finance being a significant area of discussion within the cryptocurrency space <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. While not an immediate threat, advancements in quantum computing could fundamentally alter the security landscape of digital assets like Bitcoin and Ethereum <a class="yt-timestamp" data-t="01:16:50">[01:16:50]</a>.

## Quantum Computing Fundamentals

Quantum computers harness the laws of quantum mechanics to perform computations in fundamentally new ways <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. Unlike classical computers that use bits (0 or 1), quantum computers use "qubits" which can exist in "superposition states" – a combination of 0 and 1 simultaneously <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>. This allows for an exponential increase in amplitudes (numbers closely related to probabilities) as more qubits are added, leading to a vast "scratch paper" for nature to store information <a class="yt-timestamp" data-t="02:52:02">[02:52:02]</a>.

A key challenge for quantum computers is dealing with noise, as physical qubits are extremely susceptible to errors <a class="yt-timestamp" data-t="03:57:10">[03:57:10]</a>. This necessitates "quantum error-correcting codes" to protect "logical qubits" (the pure computational units) from environmental interference <a class="yt-timestamp" data-t="02:49:09">[02:49:09]</a>.

### Google's Willow Chip Milestone
In late 2023, Google announced its Willow chip, a state-of-the-art quantum computing chip capable of exponentially reducing errors as it scales up <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. This represents an engineering milestone, experimentally demonstrating predictions made by theorists in the 1990s <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. The Willow chip utilizes 103 physical superconducting qubits in a roughly 10x10 grid to implement a "surface code" for quantum error correction <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. For the first time, as they scaled to larger surface codes, they observed encoded qubits being preserved for longer durations, indicating they've passed a critical threshold where larger codes yield a net win <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. This success validates theoretical predictions and refutes skeptics who doubted the feasibility of quantum fault tolerance <a class="yt-timestamp" data-t="11:40:00">[01:21:40]</a>.

### Quantum vs. Classical Computers
Unlike classical computers, quantum computers are not simply faster versions of existing machines <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. They excel at specific tasks where they can exploit the complex nature of amplitudes to choreograph interference patterns <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. This allows them to concentrate probability on correct answers while wrong answers cancel each other out <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>. For most daily computing tasks (like checking email or playing Candy Crush), a quantum computer would offer little to no advantage and be highly inefficient <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

## Quantum Algorithms and Cryptography

The primary concern for cryptocurrencies stems from specific quantum algorithms that can break widely used cryptographic schemes.

### Shor's Algorithm
Discovered in 1994 by Peter Shor, this algorithm can efficiently find the prime factors of huge numbers <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. This is critical because the security of a large fraction of the internet's current encryption, including RSA and Diffie-Hellman, relies on the assumption that factoring large numbers is computationally hard for classical computers <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Shor's algorithm provides an exponential speedup for this problem <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. It can also break elliptic curve encryption <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

Shor's algorithm works by exploiting the underlying mathematical structure of these problems (specifically, "abelian groups" and their periodicity) using a "Quantum Fourier Transform" <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. It is not simply trying every possible solution in parallel <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

To break cryptographic codes like RSA, millions of physical qubits would be required, potentially spread across hundreds or thousands of dilution refrigerators <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. Estimates suggest that breaking a 2048-bit key could take a quantum computer about a week <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. However, this time could decrease significantly as technology advances <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

### Grover's Algorithm
This algorithm provides a more modest, non-exponential speedup for generic search problems <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. It can solve almost any search problem in roughly the square root of the steps a classical computer would need <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. While not as dramatic as Shor's, it has wider applicability <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.

For "proof of work" tasks that involve inverting hash functions (like in Bitcoin mining), Grover's algorithm could provide an advantage <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. However, the enormous overhead of quantum error correction means a quantum computer would only provide a net win for very large problem sizes (e.g., if the search space `N` is trillions) <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

## Impact on Cryptocurrencies

The [[quantum_computings_potential_to_break_bitcoin_and_ethereum | potential impact of quantum computing on cryptocurrencies]] primarily revolves around two cryptographic functions: digital signatures and proof of work <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Bitcoin's Quantum Threat
Bitcoin faces vulnerabilities in two key areas:
1.  **Digital Signatures (ECDSA)**: Bitcoin uses Elliptic Curve Digital Signature Algorithm (ECDSA) for securing account balances <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. Shor's algorithm can break ECDSA, meaning a quantum computer could potentially derive a private key from a public key, allowing an attacker to forge signatures and steal funds <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. Attackers would likely prioritize high-value accounts <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.
    *   **"Lost Coins" and Satoshi's Bitcoin**: An estimated 1 to 4 million Bitcoin, including Satoshi's original 1 million coins, are vulnerable because their public keys were exposed on-chain in early transactions <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. These "stagnant" coins would not be able to migrate to a quantum-secure address without being moved, creating a massive "societal bounty" for whoever first builds a sufficiently powerful quantum computer <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.
    *   **Social and Technical Challenges**: Bitcoin's immutability principle makes it difficult to implement a hard fork to introduce quantum-resistant cryptography, which would be necessary to protect existing coins <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. A decision on how to handle the vulnerable coins would require a significant social consensus, potentially leading to a split in the network <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
    *   **Quantum Issuance**: If the quantum attack against older coins happens gradually (e.g., 50 Bitcoin per day from early blocks), it could ironically provide a new form of "issuance" that incentivizes mining and secures the network for a few years, as attackers would pay for quantum hardware and electricity <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

2.  **Proof of Work (PoW)**: Bitcoin's PoW mechanism relies on finding pre-images of hash functions <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. Grover's algorithm could accelerate this process <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
    *   **Centralization Risk**: If only a few entities possess scalable quantum computers, they could gain a disproportionate advantage in mining, leading to centralization of hash rate <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. This could allow a single dominant actor to control the vast majority of the hash rate, potentially setting much higher transaction fees or even shorting Bitcoin on the market <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.
    *   **Automatic Difficulty Adjustment**: In a scenario where many entities have quantum computers, the PoW difficulty would automatically adjust to compensate for Grover's algorithm, maintaining security but at a higher computational cost <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.

### Ethereum's Quantum Readiness
Ethereum is generally considered better positioned than Bitcoin to address quantum threats due to its architecture and willingness to undergo upgrades <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

1.  **Digital Signatures (BLS and ECDSA)**:
    *   **BLS Signatures**: Ethereum's Beacon Chain uses BLS signatures for consensus, which are not post-quantum secure <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. However, quantum-secure aggregation properties already exist in research, offering a plausible upgrade path within the next half-decade <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
    *   **ECDSA Accounts**: Like Bitcoin, Ethereum accounts use ECDSA <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. However, Ethereum has two key advantages:
        *   **Account Abstraction**: This feature allows accounts to define their own signature schemes, meaning users can migrate to post-quantum secure signatures without a hard fork <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
        *   **Hashed Public Keys**: From day one, Ethereum addresses have been based on the hash of the public key, not the public key itself <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This means most "lost" or inactive coins are not directly exposed to quantum attacks, unlike Bitcoin's early transactions <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. The estimated percentage of vulnerable Ether is much smaller (around 0.1%) <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

2.  **Proof of Stake (PoS)**: Ethereum's transition to PoS eliminates the vulnerability to Grover's algorithm for mining, which impacts Bitcoin's PoW <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. PoS is inherently more secure against quantum computers in this regard <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

3.  **Other Upgrades**:
    *   **KCG Blobs**: Used for data availability, KCG blobs are elliptic curve-based and will need upgrading <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This is seen as an opportunity for improvements like "blob abstraction" for developers <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
    *   **Verkle Trees**: A potential future upgrade for the Ethereum state tree, moving towards "binary Merkle trees" with SNARK-friendly hash functions, can offer both efficiency and quantum security <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
    *   **Quantum Canary**: Ethereum could implement a "Quantum Canary" smart contract. This contract would switch to post-quantum cryptography automatically if a small quantum computer provides on-chain proof of quantum capabilities (but not yet strong enough to break existing crypto), providing an immutable and self-triggering upgrade mechanism <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

## [[quantum_computing_development_and_milestones | Timeline and Outlook]]

[[quantum_computing_development_and_milestones | Quantum computing development]] is accelerating, with global spending reaching billions of dollars annually <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. Major tech companies (Google, IBM, Amazon, Quanum, Quera, IonQ, Rigetti, Sqantum) and governments (US, China, Singapore, Australia, UK, EU) are making significant investments <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

While a "useful, fault-tolerant quantum computer" (one that can solve problems beyond basic quantum simulation) is expected within the next decade <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>, the ability to break RSA or ECDSA cryptography is not guaranteed to happen simultaneously <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.

However, the National Institute of Standards and Technology (NIST) held a competition from 2017 to 2022 to standardize post-quantum cryptography, converging on "lattice-based cryptography" as a main quantum-resistant alternative <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. NIST is urging a transition, and companies like Google are already moving to post-quantum crypto <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. NIST has indicated that ECDSA will be deprecated by 2030 and disallowed by 2035 <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

## [[future_implications_of_quantum_money_and_cryptography | Future Implications: Quantum Money]]

Beyond quantum-resistant upgrades, quantum computing could enable entirely new forms of digital currency. The concept of "quantum money" dates back to the 1960s, leveraging the "no-cloning theorem" of quantum mechanics, which states that an unknown quantum state cannot be perfectly copied <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. This allows for physically unclonable cash <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

Later proposals, including some by Scott Aaronson around 2009, introduced "publicly verifiable quantum money," meaning anyone could verify a bill's genuineness without needing to return it to the bank <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. While the technology for quantum money is far off, requiring quantum computers that can preserve quantum states for arbitrary amounts of time and a "Quantum Communications Network" <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>, it could eliminate the need for global consensus mechanisms like blockchains to prevent double-spending <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

A related concept, "one-shot signatures," could bring "perfect finality" to blockchains like Ethereum by physically preventing a validator from signing two inconsistent messages <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. This would enhance security and simplify delegation for staking <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

## Conclusion

While quantum computing poses a significant future challenge for [[technical_and_social_challenges_for_upgrading_cryptocurrencies_against_quantum_threats | existing cryptographic methods]] and cryptocurrencies, it is not an immediate existential threat <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. The [[technical_and_social_challenges_for_upgrading_cryptocurrencies_against_quantum_threats | technical and social challenges for upgrading cryptocurrencies against quantum threats]] vary between networks. Ethereum appears to have a clearer roadmap for upgrades that align with its existing ethos of continuous improvement <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. Bitcoin, with its strong immutability principles, faces more complex social and technical hurdles in addressing quantum vulnerabilities, especially concerning its older, "lost" coins <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. The shift to post-quantum cryptography is already underway in other industries, and cryptocurrencies will need to adapt to remain secure in the long term <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.