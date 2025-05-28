---
title: Quantum computing and public key algorithms
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 

## The Threat of [[Quantum computers and encryption | Quantum Computers]] to Encryption

Currently, some nation states and individual actors are intercepting and storing large amounts of encrypted data, including passwords, bank details, and social security numbers, even though they cannot yet access these files <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This practice is known as Store Now, Decrypt Later (SNDL) <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. They believe that within the next 10 to 20 years, they will possess a [[Quantum computers and encryption | quantum computer]] capable of breaking existing encryption in minutes <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This is effective because information valuable today, such as industrial and pharmaceutical research or top-secret government intelligence, will still hold value in a decade <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The threat posed by [[Quantum computers and encryption | quantum computers]] is widely recognized. The National Security Administration (NSA) has stated that a sufficiently large [[Quantum computers and encryption | quantum computer]], if built, could undermine all widely deployed public key algorithms <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Experts predict that [[Quantum computers and encryption | quantum computing]] will break encryption as we know it today within a five to ten year timeframe <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Due to this looming threat, the U.S. Congress has passed legislation mandating that all agencies begin transitioning to new methods of cryptography that are resistant to [[Quantum computers and encryption | quantum computer]] attacks <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Evolution of Encryption Schemes

Current encryption schemes have been remarkably successful for over 40 years <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Symmetric Key Algorithms
Prior to the 1970s, exchanging private information required an in-person meeting to share a secret key <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This single key was used for both encrypting and decrypting messages, making it a symmetric key algorithm <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Messages remained secure as long as the key remained secret <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, this method proved impractical for sending information to unknown recipients or over unsecured channels like phone lines or mail, where the key could be intercepted <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Asymmetric Key Algorithms (RSA)
In 1977, scientists Ron Rivest, Adi Shamir, and Leonard Adleman developed a breakthrough in encryption, now known as RSA, named after their initials <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. RSA is an asymmetric key system, using different keys for encryption and decryption <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

#### How RSA Works
Each person generates two very large, secret prime numbers <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. They then multiply these primes to create an even larger number, which is made public <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. To send a private message, the sender uses the recipient's large public number to garble the message <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The message is garbled in a way that makes it impossible to ungarble without knowing the two original prime factors <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This system allows the intended recipient, who possesses the secret prime factors, to easily decode the message, while making it practically impossible for anyone else unless they can factor that large public number <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

#### Classical Factoring Limitations
Modern cryptography uses prime numbers that are approximately 313 digits long <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Even with the best known classical factoring algorithm, the General Number Field Sieve, and a supercomputer, factoring the product of two such large primes would take around 16 million years <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. However, this is not the case for a [[Quantum computers and encryption | quantum computer]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## How [[Quantum computers and encryption | Quantum Computers]] Break Encryption

### Classical Bits vs. Quantum Qubits
In normal computers, a bit exists in one state at a time, either zero or one <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Two bits can be in one of four possible states: 00, 01, 10, or 11 <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Calculations can only be performed for one state at a time <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

[[Quantum computers and encryption | Quantum computers]] use qubits, which also have states of zero or one <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Unlike classical bits, a qubit can exist in an arbitrary combination of these states simultaneously, a concept known as superposition <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Two qubits can exist simultaneously in a superposition of four states (0, 1, 2, and 3) <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. When a calculation is performed, it is executed for all these numbers at the same time, resulting in a superposition of different answers <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

Adding more qubits doubles the number of possible states <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. For example, three qubits can represent eight states and perform eight calculations simultaneously <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Just 20 qubits can represent over a million different states, allowing simultaneous computation of over a million answers <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. With 300 qubits, a [[Quantum computers and encryption | quantum computer]] could represent more states than there are particles in the observable universe <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### The Measurement Problem
Despite this incredible power, there is a significant challenge: the answers to the computation are embedded in a superposition of states, but this superposition cannot be directly read out <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. When a measurement is made, only a single, random value is obtained from the superposition, and all other information is lost <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Therefore, to harness the power of a [[Quantum computers and encryption | quantum computer]], a clever method is needed to convert a superposition of states into one that contains only the desired information <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This is an incredibly difficult task, making [[Quantum computers and encryption | quantum computers]] useless for most applications <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### [[Quantum Fourier transform and Shors algorithm | Shor's Algorithm]]
Fortunately, a few problems have been identified where this conversion is possible, and these problems form the foundation of nearly all public key cryptography used today <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

In 1994, Peter Shor and Don Coppersmith discovered how to use the [[Quantum Fourier transform and Shors algorithm | quantum Fourier transform]] <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Similar to a normal Fourier transform, it can be applied to a periodic signal to return its frequencies <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. If a superposition of states is periodic (terms are separated by a regular amount), applying the [[Quantum Fourier transform and Shors algorithm | quantum Fourier transform]] leaves states containing the signal's frequency, which can then be measured <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This ability to extract frequency information from a periodic superposition is key to factoring large numbers <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

#### Factoring N with a [[Quantum computer and encryption | Quantum Computer]]
The core idea for factoring a number `N` (product of two primes `p` and `q`) using a [[Quantum computer and encryption | quantum computer]] involves finding the period `r` of a modular exponentiation function <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

1.  **Classical Setup:** Pick a random number `g` that does not share factors with `N` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. When `g` is repeatedly multiplied by itself (raised to increasing powers) and divided by `N`, the remainder will eventually be 1 <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This means there is an exponent `r` such that `g^r` is one more than a multiple of `N` <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The sequence of remainders `g^x mod N` is periodic <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The period of this sequence is `r` <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
2.  **Using `r` to find factors:** If `r` is even, the equation `g^r - 1` can be factored into `(g^(r/2) + 1) * (g^(r/2) - 1)` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Since `g^r - 1` is a multiple of `N`, these two terms `(g^(r/2) + 1)` and `(g^(r/2) - 1)` are likely to share factors with `N` <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
3.  **Euclid's Algorithm:** Euclid's algorithm can then be used to find the greatest common divisor (GCD) between `N` and `(g^(r/2) + 1)` or `(g^(r/2) - 1)` <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This GCD will be one of the prime factors of `N` <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

The classical computation of `r` by testing powers of `g` is slow for large `N`. The key process that a [[Quantum computers and encryption | quantum computer]] speeds up is finding this exponent `r` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

#### Quantum Speed-up of Period Finding
1.  **Qubit Preparation:** Two sets of qubits are used. The first set is prepared in a superposition of all numbers from 0 up to a very large number (e.g., 10^1234) <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. The second set is initialized to zero <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
2.  **Quantum Computation:** The `g` value is raised to the power of the first set of qubits, and the remainder when divided by `N` is stored in the second set of qubits, entangling the two sets <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. This creates a superposition of all input numbers and their corresponding remainders <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
3.  **Partial Measurement:** Instead of measuring the entire superposition (which would yield a random, unhelpful value), only the remainder part is measured <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. This measurement will yield a random remainder, but this remainder will correspond to multiple exponents in the superposition that are all separated by `r`, the period we are looking for <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
4.  **[[Quantum Fourier transform and Shors algorithm | Quantum Fourier Transform]]:** This partial measurement leaves a periodic superposition of states, where each term is separated by `r` <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. Applying the [[Quantum Fourier transform and Shors algorithm | quantum Fourier transform]] to this superposition will result in states containing `1/r` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
5.  **Final Measurement:** A final measurement reveals `r` by inverting the measured value <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.
Once `r` is found, the rest of the factoring process (using `r` to generate candidate factors and then Euclid's algorithm) is performed classically <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

### Qubit Requirements for Breaking RSA
To break RSA encryption using [[Quantum computers and encryption | Shor's algorithm]], several thousand *perfect* qubits would be needed <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. However, current qubits are imperfect, requiring additional qubits for error correction (redundant information) <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

Estimates for the number of physical qubits required to break RSA have decreased significantly:
*   **2012:** 1 billion physical qubits <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>
*   **2017:** 230 million physical qubits <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>
*   **2019:** 20 million physical qubits <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>

While current [[Quantum computers and encryption | quantum computers]] (like IBM's) are far from these numbers, progress appears to be exponential, raising concerns about when these capabilities will intersect with the security of existing public key encryption <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

## [[Postquantum cryptography and latticebased encryption | Post-Quantum Cryptography]]

Given the known threat, scientists have been developing new encryption methods resistant to both classical and [[Quantum computers and encryption | quantum computer]] attacks <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

### NIST Competition
In 2016, the National Institute of Standards and Technology (NIST) launched a competition to find new [[Postquantum cryptography and latticebased encryption | post-quantum cryptography]] algorithms <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. Out of 82 proposals, rigorously tested and many broken, NIST selected four algorithms on July 5th, 2022, to be part of their [[Postquantum cryptography and latticebased encryption | post-quantum cryptographic standard]] <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

### [[Postquantum cryptography and latticebased encryption | Lattice-based Encryption]]
Three of the selected algorithms are based on the mathematics of lattices <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

#### How Lattice-based Encryption Works
1.  **Lattice Definition:** A lattice is formed by combining different integer multiples of a set of base vectors (e.g., `r1` and `r2` in 2D) <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
2.  **Hardness Problem:** The security of lattice-based cryptography relies on the "closest vector problem." Given a lattice (defined by a "bad" set of base vectors that are hard to work with) and a point not on the lattice, the challenge is to find the lattice point closest to the given point <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. While easy in low dimensions (like 2D or 3D), this problem becomes extremely difficult in high dimensions <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. Proposed future encryption schemes will use around a thousand dimensions <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.
3.  **Encryption:** Each person generates a "good" (secret) set of vectors that defines a lattice and an equivalent "bad" (public) set of vectors <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. To send a message (e.g., the number seven), the sender picks a lattice point corresponding to the message and adds some random noise to it, sending a point close to, but not precisely on, the lattice <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
4.  **Decryption:** The recipient, possessing the "good" set of vectors, can easily determine which lattice point is closest to the received noisy message point <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. This is easy for the recipient with the good vectors but extremely hard for anyone else, including both classical and [[Quantum computers and encryption | quantum computers]], if they only have the bad vectors <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.

This problem is considered extremely difficult to solve for both normal and [[Quantum computers and encryption | quantum computers]], offering a promising path for future secure communication <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. Researchers, mathematicians, and cryptographers are working to ensure secret data remains secure, protecting against mass surveillance and critical infrastructure attacks, allowing users to interact as if [[Quantum computers and encryption | quantum computers]] were never invented <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.