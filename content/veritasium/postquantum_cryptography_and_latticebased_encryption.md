---
title: Postquantum cryptography and latticebased encryption
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 

The advent of [[Quantum computers and encryption | quantum computers]] poses a significant threat to current encryption methods, leading to the development of post-quantum cryptography. Nation states and individual actors are currently intercepting and storing vast amounts of encrypted data, such as passwords, bank details, and social security numbers, even though they cannot open these files yet <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This practice is known as **Store Now, Decrypt Later (SNDL)** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The belief is that within the next 10 to 20 years, [[Quantum computers and encryption | quantum computers]] will be powerful enough to break this encryption in minutes <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

Data like industrial and pharmaceutical research, along with top-secret government intelligence, will remain valuable for decades <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The National Security Administration (NSA) has stated that a sufficiently large [[Quantum computers and encryption | quantum computer]], if built, could undermine all widely deployed [[quantum_computing_and_public_key_algorithms | public key algorithms]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Due to this looming threat, the US Congress has passed legislation mandating all agencies begin transitioning to new methods of cryptography that are resistant to [[Quantum computers and encryption | quantum computers]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Current Encryption Schemes (RSA)

Modern encryption schemes have been highly successful for over 40 years <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Before the 1970s, exchanging private information required meeting in person to share a secret, symmetric key, which was used for both encryption and decryption <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

A breakthrough occurred in 1977 when scientists Rivest, Shamir, and Adelman developed the **RSA algorithm** <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This system is an **asymmetric key system**, meaning different keys are used for encryption and decryption <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. RSA works as follows:
*   Each person secretly possesses two very large prime numbers <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   These primes are multiplied together to create an even larger number, which is then made public <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   To send a private message, one uses the recipient's public number to garble the message <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   This garbled message is impossible to ungarble without knowing the two secret prime factors that created the public number <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

The security of RSA relies on the extreme difficulty of factoring very large numbers <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Modern cryptography uses prime numbers that are around 313 digits long <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Factoring a product of two such primes, even with a supercomputer using the General Number Field Sieve, would take approximately 16 million years <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## How Quantum Computers Break RSA

Unlike classical computers that use bits in one state (0 or 1) at a time, [[Quantum computers and encryption | quantum computers]] utilize **qubits** which can exist in a [[concepts_of_superposition and entanglement | superposition]] of both states simultaneously <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This allows [[Quantum computers and encryption | quantum computers]] to perform calculations for multiple states at the same time <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For example, 20 qubits can represent over a million different states, enabling simultaneous computation of over a million answers <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. With 300 qubits, more states can be represented than there are particles in the observable universe <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

However, there's a significant challenge: the answers are embedded in a [[concepts_of_superposition and entanglement | superposition]] of states, which cannot be directly read <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. A measurement yields only a single random value, losing all other information <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. To harness the power of a [[Quantum computers and encryption | quantum computer]], a "smart way" is needed to convert a [[concepts_of_superposition and entanglement | superposition]] into one that contains only the desired information <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This is difficult, making [[Quantum computers and encryption | quantum computers]] useless for most applications <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Fortunately (or unfortunately for current encryption), this specific problem is precisely what underlies most [[quantum_computing_and_public_key_algorithms | public key cryptography]] <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Shor's Algorithm

In 1994, Peter Shor and Don Coppersmith discovered how to utilize the [[Quantum Fourier transform and Shors algorithm | Quantum Fourier transform]] <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This transform can extract frequency information from a periodic [[concepts_of_superposition and entanglement | superposition]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This is crucial because factoring large numbers can be reframed as finding the period of a specific mathematical function.

**How Shor's Algorithm Factors (Simplified):**
1.  **Classical Setup:** To factor a number N (product of two primes p and q), pick a random number 'g' that doesn't share factors with N <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
2.  **Finding Periodicity:** Repeatedly raise 'g' to increasing powers and find the remainder when divided by N (g^x mod N). A remarkable property is that these remainders will eventually repeat periodically <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The goal is to find the smallest exponent 'r' such that g^r mod N = 1 <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
3.  **Factor Derivation:** If 'r' is even, the factors of N can often be found by calculating the greatest common divisor (GCD) of N and (g^(r/2) + 1) or N and (g^(r/2) - 1) using Euclid's algorithm <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

**Quantum Speed-up (Step 2 - Finding 'r'):**
The key acceleration offered by a [[Quantum computers and encryption | quantum computer]] is in finding this period 'r' <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   **Superposition Creation:** The [[Quantum computers and encryption | quantum computer]] prepares a set of qubits in a massive [[concepts_of_superposition and entanglement | superposition]] of all possible exponents <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Modular Exponentiation & Entanglement:** It then performs the g^x mod N operation, storing the remainders in a second set of qubits. This process [[concepts_of_superposition and entanglement | entangles]] the two sets of qubits <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **Partial Measurement:** Instead of measuring the entire [[concepts_of_superposition and entanglement | superposition]] (which would yield a random result), only the remainder part is measured <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. This collapses the system into a [[concepts_of_superposition and entanglement | superposition]] where all states share the same measured remainder, and critically, their exponents are separated by the period 'r' <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **[[Quantum Fourier transform and Shors algorithm | Quantum Fourier transform]] Application:** Applying the [[Quantum Fourier transform and Shors algorithm | Quantum Fourier transform]] to this periodic [[concepts_of_superposition and entanglement | superposition]] reveals states containing information about 1/R <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
*   **Measurement of 'r':** A final measurement then yields 'r', completing the quantum part of the algorithm <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. The rest of the factoring process (Euclid's algorithm) is performed classically.

### Qubit Requirements and Progress

While Shor's algorithm only requires a few thousand perfect qubits, current qubits are imperfect, necessitating additional qubits for error correction <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **2012 Estimate:** 1 billion physical qubits to break RSA encryption <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **2017 Estimate:** Dropped to 230 million <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **2019 Estimate:** Plummeted to just 20 million physical qubits due to technological breakthroughs <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

Although current [[Quantum computers and encryption | quantum computers]] (e.g., IBM's) are far from this number, progress appears to be exponential, indicating a looming collision between [[Quantum computers and encryption | quantum computing]] power and the vulnerability of existing [[quantum_computing_and_public_key_algorithms | public key encryption]] <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.

## Post-Quantum Cryptography: Lattice-Based Encryption

Given the inevitable threat, scientists have been developing new encryption methods resistant to both classical and [[Quantum computers and encryption | quantum computer]] attacks <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. In 2016, the National Institute of Standards and Technology (NIST) launched a competition to find such **post-quantum cryptography algorithms** <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. On July 5th, 2022, NIST selected four algorithms for its post-quantum cryptographic standard <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. Three of these are based on the mathematics of **lattices** <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

### How Lattice-Based Encryption Works

A **lattice** is formed by adding together different integer combinations of a set of basis vectors (e.g., `r1` and `r2` in 2D) <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. The core of lattice-based encryption lies in the **Closest Vector Problem**: finding the lattice point closest to a given target point <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.

*   **The Hard Problem:** While easy to solve with a "good" set of basis vectors, the problem becomes extremely difficult with a "bad" set of vectors, where steps in one dimension might adversely affect progress in others <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   **High Dimensions:** The difficulty of the Closest Vector Problem increases exponentially with the number of dimensions <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. Proposed future encryption schemes will use around a thousand dimensions, making it exceptionally hard for even the most powerful classical or [[Quantum computers and encryption | quantum computers]] to solve <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

**Encryption using Lattices:**
1.  Each person has a secret "good" set of vectors defining a lattice <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.
2.  They publicly share the *same lattice*, but using a "bad" set of vectors that is hard to work with <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.
3.  To send a message, the sender picks a point on the recipient's public lattice corresponding to the message (e.g., number seven) <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
4.  Random "noise" is added to this lattice point, making the sent message slightly off the exact lattice point <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.
5.  To decode, the recipient must find the lattice point closest to the noisy message point <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. This is easy for the recipient who possesses the "good" secret vectors, but extremely hard for anyone else <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

This problem is considered extremely difficult for both normal and [[Quantum computers and encryption | quantum computers]] to solve, making it a robust foundation for future encryption <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. These cryptographic advancements aim to ensure data privacy and protect critical infrastructure, allowing secure communication even with the rise of [[Quantum computers and encryption | quantum computers]] <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.