---
title: Quantum computers and encryption
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 

[[quantum_computing_and_public_key_algorithms | Quantum computers]] pose a significant threat to current encryption methods, leading to efforts in developing new cryptographic standards. <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>

## Store Now, Decrypt Later (SNDL)
Some nation states and individual actors are currently intercepting and storing large amounts of encrypted data, such as passwords, bank details, and social security numbers. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> They are doing this because they anticipate that within the next 10 to 20 years, they will have access to a quantum computer capable of breaking this encryption in minutes. <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a> This practice is known as Store Now, Decrypt Later (SNDL). <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>

SNDL is effective because information stored today, such as industrial and pharmaceutical research or top-secret government intelligence, will remain valuable in a decade. <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a> The National Security Administration (NSA) has stated that a sufficiently large quantum computer, if built, could undermine all widely deployed [[quantum_computing_and_public_key_algorithms | public key algorithms]]. <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> In a five to ten year timeframe, quantum computing is expected to break current encryption. <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> Despite powerful quantum computers being years away, they are already a threat due to SNDL. <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> Consequently, the U.S. Congress has passed legislation mandating all agencies begin transitioning to new, quantum-resistant cryptography methods. <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

## Current Encryption Schemes

Current encryption schemes have been remarkably successful for over 40 years. <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

### Symmetric Key Algorithms
Up until the 1970s, exchanging private information required meeting in person to share a secret key. <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> This same key was used for both encryption and decryption, hence it's known as a symmetric key algorithm. <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> Messages remain safe as long as the key is not compromised. <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> However, this method is impractical for sending information to someone never met, as a key cannot be shared over unsecured channels like phone lines or mail without risk of interception. <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>

### Asymmetric Key Algorithms (RSA)
In 1977, scientists Rivest, Shamir, and Adelman developed an encryption breakthrough known today by their initials, RSA. <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>

#### How RSA Works
RSA works as follows:
1.  Each person has two large, secret prime numbers. <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>
2.  These primes are multiplied together to get an even larger number, which is then made public. <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
3.  To send a private message, the sender uses the recipient's large public number to garble the message. <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>
4.  The garbled message is impossible to ungarble without knowing the two prime factors that made the public number. <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>

This is an asymmetric key system, as different keys are used for encryption and decryption. <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a> It's easy for the intended recipient to decode but impossible for others, unless they can factor the large public number. <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>

#### Difficulty of Breaking RSA Classically
While someone could attempt to factor the number using a supercomputer with the General Number Field Sieve algorithm, modern cryptography uses prime numbers that are around 313 digits long. <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a> Factoring a product of two such large primes, even with a supercomputer, would take approximately 16 million years. <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> However, this is not the case for a quantum computer. <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>

## Quantum Computers: How They Differ from Classical Computers

### Bits vs. Qubits
In classical computers, a bit can only be in one state at a time (0 or 1). <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a> Two bits can be in one of four possible states (00, 01, 10, or 11). <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> A classical computer performs calculations for one state at a time. <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>

Quantum computers consist of qubits, which also have two states (0 or 1). <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> Unlike classical bits, a qubit can exist in an arbitrary combination of these states, a "superposition" of 0 and 1. <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>

### Parallel Computation
With two qubits, they can exist simultaneously in a superposition of multiple states (e.g., 0, 1, 2, and 3). <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a> When a calculation is performed, it's executed for all these numbers simultaneously, resulting in a superposition of different answers. <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a> Adding another qubit doubles the number of possible states. <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a> For instance, 20 qubits can represent over a million states and simultaneously compute over a million different answers. <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> With 300 qubits, it's possible to represent more states than there are particles in the observable universe. <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>

### The Measurement Problem
Despite their incredible power, quantum computers have a significant limitation: the answers to a computation are embedded in a superposition of states, but this superposition cannot be simply read out. <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a> When a measurement is made, only a single value from the superposition is obtained randomly, and all other information is lost. <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>

### Need for Smart Algorithms
To harness the power of a quantum computer, a "smart way" is needed to convert a superposition of states into one that contains only the desired information. <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a> This is an incredibly difficult task, making quantum computers useless for most applications. <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a> However, a few problems have been identified where this can be done, and these problems form the foundation of nearly all current [[quantum_computing_and_public_key_algorithms | public key cryptography]]. <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>

## Quantum Algorithms for Breaking Encryption

In 1994, Peter Shor and Don Coppersmith developed a way to perform a [[quantum_fourier_transform_and_shors_algorithm | quantum Fourier transform]]. <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a> Similar to a normal Fourier transform, it takes a periodic signal and returns its frequencies. <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a> If a superposition of states is periodic, the [[quantum_fourier_transform_and_shors_algorithm | quantum Fourier transform]] can extract the frequency of the signal, which can then be measured. <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a> This ability to extract frequency information from a periodic superposition is crucial for quantum computers to factor large numbers. <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>

### How a Quantum Computer Factors Numbers
To explain how a quantum computer factors the product of two primes faster than a conventional computer, consider the following method:

#### Classical Example (N=77)
1.  **Given:** A number N that is the product of two primes, p and q. Let N = 77. <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
2.  **Make a "Bad Guess":** Pick a number 'g' that doesn't share any factors with N. Let g = 8. <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>
3.  **Find the Exponent 'r':** Multiply 'g' by itself repeatedly, finding the remainder when divided by N. The goal is to find an exponent 'r' such that g^r is one more than a multiple of N (i.e., g^r mod N = 1). <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>
    *   For g=8, N=77:
        *   8^1 mod 77 = 8
        *   8^2 mod 77 = 64
        *   8^3 mod 77 = 50
        *   ...
        *   8^10 mod 77 = 1 <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>
    *   Thus, r = 10. <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>
4.  **Derive New Numbers:** Rearrange the equation (g^r mod N = 1) to g^r - 1 = k * N (where k is an integer). This can be split into (g^(r/2) + 1)(g^(r/2) - 1) = k * N. <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>
    *   For r=10, the terms are (8^5 + 1) and (8^5 - 1). <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
    *   (32,769) and (32,767). <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a> These two numbers likely share factors with N. <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>
5.  **Find Shared Factors (Euclid's Algorithm):** Use Euclid's algorithm to find the greatest common divisor (GCD) between N and each of these new numbers. <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>
    *   GCD(32769, 77):
        *   32769 / 77 = 425 remainder 44
        *   77 / 44 = 1 remainder 33
        *   44 / 33 = 1 remainder 11
        *   33 / 11 = 3 remainder 0. <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>
    *   The GCD is 11, which is a factor of 77. <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>
    *   Divide 77 by 11 to get the other prime factor, 7. <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>

The critical step that a quantum computer speeds up is finding the exponent 'r'. <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a> The sequence of remainders (g^x mod N) is periodic. <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a> The exponent 'r' corresponds to the period of this sequence. <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>

#### Quantum Computer Execution
1.  **Prepare Qubits:** Split qubits into two sets. The first set is prepared in a superposition of all possible exponents from 0 up to a very large number (e.g., 10^1234). The second set is initialized to zero. <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>
2.  **Perform Calculation and Entangle:** Choose a guess 'g'. Raise 'g' to the power of the first set of qubits (representing all possible exponents simultaneously), divide by N, and store the remainder in the second set of qubits. This entangles the two sets of qubits, resulting in a superposition of (exponent, remainder) pairs. <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>
3.  **Measure Remainder:** Measure only the remainder part of the superposition. This will yield a random remainder, but crucially, it will "collapse" the first set of qubits into a superposition of only those exponents that produce that specific remainder. <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a> These exponents will all be separated by the period 'r' (the number we are looking for). <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>
4.  **Apply [[quantum_fourier_transform_and_shors_algorithm | Quantum Fourier Transform]]:** Since the resulting superposition of exponents is periodic with period 'r', applying the [[quantum_fourier_transform_and_shors_algorithm | quantum Fourier transform]] to this superposition will leave it with states containing 1/r. <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>
5.  **Measure and Find 'r':** Perform a measurement to find 1/r, then invert it to obtain 'r'. <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>

Once 'r' is found (and assuming 'r' is even), the remaining steps (deriving new numbers and using Euclid's algorithm) are performed classically to find the prime factors and break the encryption. <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>

### Qubit Requirements and Progress
Breaking RSA encryption with this method would require several thousand "perfect" qubits. <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a> However, current qubits are imperfect, necessitating additional "redundant" qubits for error correction. <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>
*   **2012:** Estimated to require 1 billion physical qubits to break RSA encryption. <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>
*   **2017:** Estimate dropped to 230 million. <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>
*   **2019:** Estimate plummeted to just 20 million physical qubits due to technological breakthroughs. <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>

While current quantum computers (e.g., IBM's) are far from these numbers, progress appears exponential, indicating a future collision point where existing [[quantum_computing_and_public_key_algorithms | public key encryption]] could be broken. <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>

## Post-Quantum Cryptography

Scientists have been developing new ways to encrypt data that can withstand attacks from both classical and quantum computers, anticipating the quantum threat. <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>

### NIST Competition
In 2016, the National Institute of Standards and Technology (NIST) launched a competition to find new quantum-resistant encryption algorithms. <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a> Out of 82 proposals rigorously tested by cryptographers worldwide, NIST selected four algorithms on July 5th, 2022, to be part of their [[postquantum_cryptography_and_latticebased_encryption | post-quantum cryptographic standard]]. <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>

### [[postquantum_cryptography_and_latticebased_encryption | Lattice-Based Encryption]]
Three of the selected algorithms are based on the mathematics of lattices. <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>

#### How Lattices Work
A lattice is formed by adding together different integer combinations of a set of "basis" vectors (e.g., r1 and r2 in 2D). <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a> Any point reachable by combining these vectors in different integer ways is part of the lattice. <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>

#### The "Closest Vector Problem"
The core problem in [[postquantum_cryptography_and_latticebased_encryption | lattice-based encryption]] is the "closest vector problem": given a lattice and a point 'C', find the lattice point closest to 'C'. <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>

#### High Dimensions Make it Hard
While finding the closest point in 2D or 3D is relatively easy, it becomes extremely difficult as the number of dimensions increases. <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a> In proposed future encryption schemes, around a thousand dimensions will be used. <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a> In such high dimensions, taking a step in one direction can negatively impact progress in many other dimensions simultaneously, making it incredibly hard to find the closest point even for the most powerful computers, unless one has a "good" set of basis vectors. <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>

#### How it is Used for Encryption
1.  Each person has a "good" (easy to work with) set of vectors describing a lattice, which they keep secret. <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>
2.  They publicly share their lattice using a "bad" (hard to work with) set of vectors. <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>
3.  To send a message (e.g., a number), the sender picks a lattice point corresponding to the message. <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>
4.  Then, some random "noise" is added to the message point, so the sent message is not precisely at a lattice point but close to it. <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>
5.  To decode, the recipient must find which lattice point is closest to the received message point. <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>
6.  In a thousand dimensions, this is extremely hard unless one has the "nice" set of vectors (which the recipient does). <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>

This problem is considered extremely difficult to solve for both classical and quantum computers, making [[postquantum_cryptography_and_latticebased_encryption | lattice-based encryption]] a promising candidate for future secure communication. <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>