---
title: Postquantum cryptography and latticebased encryption
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 

## The Quantum Threat to Current Encryption

Currently, nation-states and individual actors are intercepting and storing large amounts of encrypted data, including passwords, bank details, and social security numbers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. They cannot open these files yet <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> but believe that within 10 to 20 years, they will have access to a [[quantum_computing_and_encryption|quantum computer]] capable of breaking the encryption in minutes <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This procedure is known as Store Now, Decrypt Later (SNDL) <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Information such as industrial and pharmaceutical research or top-secret government intelligence will remain valuable in a decade <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

The National Security Administration (NSA) states that a sufficiently large [[quantum_computing_and_encryption|quantum computer]], if built, could undermine all widely deployed [[public_key_cryptography_and_rsa|public key algorithms]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Experts suggest that within a five to ten-year timeframe, [[quantum_computing_and_encryption|quantum computing]] will break encryption as it is known today <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Despite powerful [[quantum_computing_and_encryption|quantum computers]] still being years away, they pose an immediate threat due to SNDL <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The US Congress has passed legislation mandating all agencies begin transitioning to new methods of cryptography that [[quantum_computing_and_encryption|quantum computers]] cannot break <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Current Encryption: [[Public key cryptography and RSA|RSA]]

Current encryption schemes have been highly successful for over 40 years <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Before the 1970s, sharing private information required meeting in person to exchange a secret key <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This "symmetric key algorithm" uses the same key for encryption and decryption <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

The challenge arose when sending information to someone never met, as sharing a key over an unsecured channel (like phone or mail) could lead to interception <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This led to a breakthrough in 1977 by Ronald Rivest, Adi Shamir, and Leonard Adelman, known today as [[public_key_cryptography_and_rsa|RSA]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### How [[Public key cryptography and RSA|RSA]] Works

[[Public key cryptography and RSA|RSA]] works as follows:
1.  Each person has two very large secret prime numbers <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  These primes are multiplied together to get an even larger number, which is made public <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
3.  To send a private message, the sender uses the recipient's public number to "garble" the message <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
4.  This garbling makes it impossible to ungarble without knowing the two secret prime factors that made the public number <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
5.  This is an "asymmetric key system" because different keys are used for encryption and decryption <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. It's easy for the intended recipient to decode but impossible for others unless they can factor the large public number <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Currently, factoring a product of two primes that are around 313 digits long, even with a supercomputer using the General Number Field Sieve algorithm, would take about 16 million years <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. However, this is not the case for a [[quantum_computing_and_encryption|quantum computer]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## How [[Quantum Computing and Encryption|Quantum Computers]] Threaten Encryption

Classical computers use bits that are either a zero or a one <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Two bits can be in one of four states (00, 01, 10, 11) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. A classical computer performs calculations on one state at a time <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

[[Quantum_computing_and_encryption|Quantum computers]] use qubits, which can be in a [[Superposition and entanglement|superposition]] of both zero and one simultaneously <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Two qubits can exist simultaneously in a [[Superposition and entanglement|superposition]] of four states <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This allows a [[quantum_computing_and_encryption|quantum computer]] to perform calculations for all possible numbers (states) at the same time, resulting in a [[Superposition and entanglement|superposition]] of all answers <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

Adding more qubits doubles the number of possible states <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Three qubits can represent eight states <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   Twenty qubits can represent over a million states <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   Three hundred qubits can represent more states than there are particles in the observable universe <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### The Measurement Problem

Despite this power, there's a catch: all answers are embedded in a [[Superposition and entanglement|superposition]] of states, but measuring it only yields a single random value, losing all other information <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. To harness a [[quantum_computing_and_encryption|quantum computer]]'s power, a smart way is needed to convert a [[Superposition and entanglement|superposition]] of states into one containing only the desired information <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This is difficult, making [[quantum_computing_and_encryption|quantum computers]] useless for most applications <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. However, the few problems where this is possible form the foundation of nearly all [[public_key_cryptography and RSA|public key cryptography]] used today <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Shor's Algorithm: The Quantum Breakthrough

In 1994, Peter Shor and Don Coppersmith discovered how to perform a [[quantum_fourier_transform|quantum Fourier transform]] <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Like a classical Fourier transform, it returns the frequencies present in a periodic signal <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. If a [[Superposition and entanglement|superposition]] of states is periodic (terms separated by a regular amount), applying the [[quantum_fourier_transform|quantum Fourier transform]] leaves states containing the signal's frequency, which can then be measured <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This ability to extract frequency information from a periodic [[Superposition and entanglement|superposition]] is crucial for factoring <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### How Shor's Algorithm Factors Numbers

To factor a number N (product of two primes p and q), using N=77 as an example:
1.  **Pick a number G** that doesn't share factors with N (e.g., G=8 for N=77) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
2.  **Find the exponent R:** Multiply G by itself repeatedly (G^1, G^2, G^3...) and find the remainder when divided by N. The goal is to find an exponent R where G^R is one more than a multiple of N (i.e., G^R mod N = 1) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   For G=8 and N=77, the remainders are 8, 64, 50, 15, 43, 36, 57, 71, 29, and finally 1 at G^10 <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. So, R=10 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
    *   This sequence of remainders is periodic <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The exponent R (period) is the spacing between occurrences of the same remainder <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
3.  **Use the exponent R:** Rearrange the equation G^R - 1 = multiple of N, which can be factored into (G^(R/2) - 1)(G^(R/2) + 1) = multiple of N <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. As long as R is even, these two terms likely share factors with N <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
    *   For R=10, the terms are (8^5 - 1) = 32,767 and (8^5 + 1) = 32,769 <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
4.  **Find shared factors with Euclid's algorithm:** Use Euclid's algorithm to find the greatest common divisor (GCD) between N and each of these two terms <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   GCD(32769, 77) = 11 <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
    *   Dividing 77 by 11 gives the other factor, 7 <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Thus, the prime factors of 77 are 7 and 11 <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

While these steps can be done classically, [[quantum_computing_and_encryption|quantum computers]] dramatically speed up step two: finding the exponent R <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

### Quantum Acceleration of Shor's Algorithm

1.  **Prepare qubits:** Split qubits into two sets. The first set is prepared in a [[Superposition and entanglement|superposition]] of all possible exponents from 0 up to a very large number (e.g., 10^1234), requiring thousands of qubits <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. The second set is left in the zero state <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
2.  **Perform calculation and entangle:** Raise G to the power of the first set of qubits (which are in [[Superposition and entanglement|superposition]]), divide by N, and store the remainder in the second set of qubits <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. This operation [[Superposition and entanglement|entangles]] the two sets of qubits, creating a [[Superposition and entanglement|superposition]] of all possible (exponent, remainder) pairs <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
3.  **Measure remainder:** Instead of measuring the entire [[Superposition and entanglement|superposition]], only the remainder part is measured <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. This yields a random remainder, but crucially, this remainder will have occurred multiple times throughout the cycle <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. For example, if the remainder 15 was measured, the original exponents would be 4, 14, 24, 34, etc., all separated by 10 (which is R) <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
4.  **Isolate periodic [[Superposition and entanglement|superposition]]:** After measuring the remainder, the quantum system is left with a [[Superposition and entanglement|superposition]] of states where all exponents share the same remainder and are separated by the desired value R <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. This creates a periodic [[Superposition and entanglement|superposition]] <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
5.  **Apply [[quantum_fourier_transform|Quantum Fourier Transform]]:** Applying the [[quantum_fourier_transform|quantum Fourier transform]] to this periodic [[Superposition and entanglement|superposition]] transforms the states to contain information about one over R (1/R) <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
6.  **Measure and Invert:** A final measurement yields R by inverting the measured value <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. This R is then used in the classical steps (3 and 4) to find the prime factors <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

### Progress in Qubit Technology

Breaking [[public_key_cryptography_and_rsa|RSA]] encryption would require several thousand "perfect" qubits <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. However, current qubits are imperfect, necessitating additional qubits for error correction <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.
*   In 2012, it was estimated that a billion physical qubits would be needed <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   By 2017, this estimate dropped to 230 million <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   In 2019, after more technological breakthroughs, the estimate plummeted to just 20 million physical qubits <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

While current [[quantum_computing_and_encryption|quantum computers]] (like IBM's) are far from this number, progress appears to be exponential, meaning the ability to break current encryption could arrive rapidly <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## The Race for Post-Quantum Cryptography

Given the known threat, scientists have been seeking new ways to encrypt data that can withstand attacks from both classical and [[quantum_computing_and_encryption|quantum computers]] <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. In 2016, the National Institute of Standards and Technology (NIST) launched a competition to find such algorithms <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. Out of 82 proposals, NIST selected four algorithms on July 5, 2022, to be part of their post-quantum cryptographic standard <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

## Lattice-Based Encryption: A New Approach

Three of the four NIST-selected algorithms are based on the mathematics of lattices <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

### Understanding Lattices and the Closest Vector Problem

A lattice is formed by taking integer combinations of a set of basis vectors (e.g., r1 and r2 in 2D) <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. The "closest vector problem" asks to find the lattice point closest to a given target point C <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

The difficulty of this problem depends on the chosen basis vectors <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. If the vectors are "good" (e.g., nearly orthogonal), finding the closest point is easy <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. However, if the vectors are "bad" (e.g., highly skewed), each step in one direction might move you off course in others, making the problem much harder <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

The problem becomes exponentially harder with increasing dimensions <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. In proposed future encryption schemes, around a thousand dimensions will be used <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. In such high dimensions, finding the closest point is extremely difficult even for the most powerful computers, unless one knows a "good" set of vectors <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

### Lattice Encryption in Practice

1.  **Key Generation:** Each person has a "good" (secret) set of vectors that describes a lattice <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. They then share their lattice publicly using a "bad" (hard-to-work-with) set of vectors <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
2.  **Encryption:** To send a message (e.g., the number seven), the sender picks a point on the recipient's lattice corresponding to that message <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. They then add some random noise to this point, so the sent message is close to, but not exactly at, a lattice point <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.
3.  **Decryption:** The recipient must figure out which lattice point is closest to the noisy message point <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. In a thousand dimensions, this is extremely difficult unless the recipient has their "nice" set of secret vectors <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.

This makes it easy for the recipient (who has the good vectors) but hard for everyone else <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>. As far as current knowledge indicates, this problem is extremely difficult to solve for both classical and [[quantum_computing_and_encryption|quantum computers]] <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.

These new cryptographic methods are crucial for ensuring the security of data, protecting critical infrastructure, and maintaining privacy in a future with powerful [[quantum_computing_and_encryption|quantum computers]] <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.