---
title: Quantum computing and encryption
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 

## The Looming Threat: Store Now, Decrypt Later (SNDL)

Currently, some nation-states and individual actors are intercepting and storing large amounts of encrypted data, such as passwords, bank details, and social security numbers <a class="yt-timestamp" data-t="00:00:00">00:00:00</a>. While they cannot open these files now, they believe that within the next 10 to 20 years, they will have access to a quantum computer capable of breaking this encryption in minutes <a class="yt-timestamp" data-t="00:00:15">00:00:15</a>. This procedure is known as Store Now, Decrypt Later (SNDL) <a class="yt-timestamp" data-t="00:00:23">00:00:23</a>. This strategy works because information collected today, like industrial research, pharmaceutical research, and top-secret government intelligence, will still be valuable in a decade <a class="yt-timestamp" data-t="00:00:29">00:00:29</a>.

The National Security Administration (NSA) has stated that a sufficiently large quantum computer, if built, could undermine all widely deployed [[public_key_cryptography_and_rsa | public key algorithms]] <a class="yt-timestamp" data-t="00:00:42">00:00:42</a>. Experts predict that within a five to ten-year timeframe, quantum computing will break encryption as we know it today <a class="yt-timestamp" data-t="00:00:52">00:00:52</a>. Due to the threat of SNDL, the U.S. Congress has passed legislation mandating all agencies begin transitioning to new methods of cryptography that cannot be broken by quantum computers <a class="yt-timestamp" data-t="00:01:05">00:01:05</a>.

## Current Encryption Schemes: [[Public key cryptography and RSA | RSA]]

Our current encryption schemes have been highly successful for over 40 years <a class="yt-timestamp" data-t="00:01:17">00:01:17</a>.

### Symmetric Key Algorithms

Before the 1970s, exchanging private information required meeting in person to share a secret key <a class="yt-timestamp" data-t="00:01:23">00:01:23</a>. This same key was used for both encrypting and decrypting messages, making it a symmetric key algorithm <a class="yt-timestamp" data-t="00:01:33">00:01:33</a>. As long as the key remained secret, messages were safe <a class="yt-timestamp" data-t="00:01:41">00:01:41</a>. However, sharing a key over unsecured channels like phone lines or mail risked interception <a class="yt-timestamp" data-t="00:01:53">00:01:53</a>.

### Asymmetric Key Algorithms: [[Public key cryptography and RSA | RSA]]

This challenge led to an encryption breakthrough in 1977 by scientists Rivest, Shamir, and Adleman, now known by their initials, [[public_key_cryptography_and_rsa | RSA]] <a class="yt-timestamp" data-t="00:02:00">00:02:00</a>.

[[public_key_cryptography_and_rsa | RSA]] works as follows:
*   Each person has two very large, secret prime numbers <a class="yt-timestamp" data-t="00:02:14">00:02:14</a>.
*   These primes are multiplied together to get an even larger number, which is made public <a class="yt-timestamp" data-t="00:02:20">00:02:20</a>.
*   To send a private message, one uses the recipient's public number to encrypt the message <a class="yt-timestamp" data-t="00:02:27">00:02:27</a>.
*   The message is encrypted in a way that makes it impossible to decrypt without knowing the two secret prime factors that created the public number <a class="yt-timestamp" data-t="00:02:34">00:02:34</a>.
*   This is an asymmetric key system because different keys are used for encryption and decryption <a class="yt-timestamp" data-t="00:02:42">00:02:42</a>. It's easy for the intended recipient to decode but impossible for others, unless they can factor that large public number <a class="yt-timestamp" data-t="00:02:49">00:02:49</a>.

Modern cryptography uses prime numbers that are about 313 digits long <a class="yt-timestamp" data-t="00:03:06">00:03:06</a>. Factoring a product of two such large primes, even with a supercomputer using the best-known factoring algorithm (General Number Field Sieve), would take approximately 16 million years <a class="yt-timestamp" data-t="00:02:59">00:02:59</a>. However, this is not the case for a quantum computer <a class="yt-timestamp" data-t="00:03:17">00:03:17</a>.

## How Quantum Computers Break Encryption

### Classical Bits vs. Qubits

In normal computers, a bit can only be in one state at a time (0 or 1) <a class="yt-timestamp" data-t="00:03:21">00:03:21</a>. Two bits can be in one of four possible states: 00, 01, 10, or 11 <a class="yt-timestamp" data-t="00:03:27">00:03:27</a>. If a calculation is performed, it can only be done for one state at a time <a class="yt-timestamp" data-t="00:03:41">00:03:41</a>.

Quantum computers use qubits, which also have two states (0 or 1) <a class="yt-timestamp" data-t="00:03:53">00:03:53</a>. However, unlike classical bits, a qubit can exist in an arbitrary combination of those states, known as a [[superposition and entanglement | superposition]] of 0 and 1 <a class="yt-timestamp" data-t="00:03:58">00:03:58</a>. Two qubits can simultaneously exist in a [[superposition and entanglement | superposition]] of 0, 1, 2, and 3 <a class="yt-timestamp" data-t="00:04:10">00:04:10</a>. This allows a quantum computer to perform a calculation for all possible numbers in a [[superposition and entanglement | superposition]] at the same time, resulting in a [[superposition and entanglement | superposition]] of different answers <a class="yt-timestamp" data-t="00:04:20">00:04:20</a>. Adding a qubit doubles the number of possible states and calculations <a class="yt-timestamp" data-t="00:04:35">00:04:35</a>. Just 20 qubits can represent over a million different states, enabling simultaneous computation of over a million answers <a class="yt-timestamp" data-t="00:04:46">00:04:46</a>. With 300 qubits, one can represent more states than there are particles in the observable universe <a class="yt-timestamp" data-t="00:04:57">00:04:57</a>.

### The Measurement Problem

Despite this immense power, there's a significant catch: all the answers to the computation are embedded in a [[superposition and entanglement | superposition]] of states, but this [[superposition and entanglement | superposition]] cannot be directly read out <a class="yt-timestamp" data-t="00:05:11">00:05:11</a>. When a measurement is made, only a single value is obtained from the [[superposition and entanglement | superposition]], essentially at random, and all other information is lost <a class="yt-timestamp" data-t="00:05:19">00:05:19</a>.

To harness the power of a quantum computer, a "smart way" is needed to convert a [[superposition and entanglement | superposition]] of states into one that contains only the desired information <a class="yt-timestamp" data-t="00:05:27">00:05:27</a>. This is an incredibly difficult task, making quantum computers useless for most applications <a class="yt-timestamp" data-t="00:05:37">00:05:37</a>. However, the few problems identified where this can be done are precisely the problems that form the foundation of nearly all [[public_key_cryptography_and_rsa | public key cryptography]] used today <a class="yt-timestamp" data-t="00:05:43">00:05:43</a>.

### Shor's Algorithm and the [[Quantum Fourier transform | Quantum Fourier Transform]]

In 1994, Peter Shor and Don Coppersmith discovered how to perform a [[Quantum Fourier transform | quantum Fourier transform]] <a class="yt-timestamp" data-t="00:05:56">00:05:56</a>. Similar to a normal Fourier transform, it takes a periodic signal and returns its frequencies <a class="yt-timestamp" data-t="00:06:03">00:06:03</a>. If a [[superposition and entanglement | superposition]] of states is periodic (terms are separated by a regular amount), applying the [[Quantum Fourier transform | quantum Fourier transform]] results in states containing the signal's frequency, which can then be measured <a class="yt-timestamp" data-t="00:06:14">00:06:14</a>. The [[Quantum Fourier transform | quantum Fourier transform]] allows the extraction of frequency information from a periodic [[superposition and entanglement | superposition]], which is crucial for factoring <a class="yt-timestamp" data-t="00:06:30">00:06:30</a>.

### Factoring Primes with Quantum Computers (Shor's Algorithm)

To understand how a quantum computer factors the product of two primes much faster than a conventional computer, consider the following steps, demonstrated with a simple example:

1.  **Identify the Period (r)**: Pick a number `g` that does not share any factors with `N` (the number to be factored, product of two primes `p` and `q`) <a class="yt-timestamp" data-t="00:07:23">00:07:23</a>. When `g` is multiplied by itself repeatedly, it will eventually reach a multiple of `N` plus one. This means there's an exponent `r` such that `g^r` is a multiple of `N` plus one <a class="yt-timestamp" data-t="00:07:32">00:07:32</a>.
    *   *Example:* For `N=77`, choosing `g=8`. The remainders of `8^x / 77` are `8, 64, 50, 15, 43, 36, 57, 71, 29`, and finally `1` at `x=10` <a class="yt-timestamp" data-t="00:08:27">00:08:27</a>. So, `r=10` <a class="yt-timestamp" data-t="00:08:49">00:08:49</a>.
    *   The sequence of remainders is periodic. For `g=8` and `N=77`, the sequence `8, 64, 50, 15, 43, 36, 57, 71, 29, 1` repeats every 10 exponents <a class="yt-timestamp" data-t="00:12:05">00:12:05</a>. The exponent `r` (10 in this case) is the period of this sequence <a class="yt-timestamp" data-t="00:13:11">00:13:11</a>. This periodicity is crucial.

2.  **Derive Factors**: Rearrange the equation `g^r` = `k*N + 1` to `g^r - 1` = `k*N` <a class="yt-timestamp" data-t="00:09:03">00:09:03</a>. If `r` is even, this can be factored as `(g^(r/2) + 1) * (g^(r/2) - 1)` = `k*N` <a class="yt-timestamp" data-t="00:09:08">00:09:08</a>. Since `N = p * q`, the terms `(g^(r/2) + 1)` and `(g^(r/2) - 1)` likely share factors with `N` <a class="yt-timestamp" data-t="00:09:50">00:09:50</a>.
    *   *Example:* With `r=10`, the terms are `(8^5 + 1)` and `(8^5 - 1)`, which are `32,769` and `32,767` <a class="yt-timestamp" data-t="00:09:50">00:09:50</a>.

3.  **Find Shared Factors (Euclid's Algorithm)**: Use Euclid's algorithm to find the greatest common divisor (GCD) between one of these derived numbers and `N` <a class="yt-timestamp" data-t="00:10:09">00:10:09</a>. This will give one of the prime factors. The other factor can be found by dividing `N` by the first factor <a class="yt-timestamp" data-t="00:11:05">00:11:05</a>.
    *   *Example:* GCD(32,769, 77) = 11 <a class="yt-timestamp" data-t="00:10:13">00:10:13</a>. Dividing 77 by 11 gives 7 <a class="yt-timestamp" data-t="00:11:05">00:11:05</a>. Thus, the prime factors are 11 and 7.

### The Quantum Speed-up

The critical step that a quantum computer speeds up is finding the exponent `r` (step 2) <a class="yt-timestamp" data-t="00:11:49">00:11:49</a>.

Here's how a quantum computer performs this:
1.  **Prepare Qubits**: Split qubits into two sets. The first set is prepared in a massive [[superposition and entanglement | superposition]] of numbers from 0 up to 10^1234 <a class="yt-timestamp" data-t="00:13:54">00:13:54</a>. The second set starts in the zero state <a class="yt-timestamp" data-t="00:14:19">00:14:19</a>.
2.  **Perform `g^x mod N`**: A guess `G` is chosen. `G` is raised to the power of the first set of qubits (representing `x` values in [[superposition and entanglement | superposition]]), then divided by `N`, and the remainder is stored in the second set of qubits <a class="yt-timestamp" data-t="00:14:31">00:14:31</a>. This operation creates [[superposition and entanglement | entanglement]] between the two sets of qubits <a class="yt-timestamp" data-t="00:14:52">00:14:52</a>.
3.  **Measure Remainder**: Instead of measuring the entire [[superposition and entanglement | superposition]], only the remainder part (second set of qubits) is measured <a class="yt-timestamp" data-t="00:15:06">00:15:06</a>. This yields a random remainder. However, this remainder will appear multiple times within the [[superposition and entanglement | superposition]] because of the periodicity of the remainders <a class="yt-timestamp" data-t="00:15:14">00:15:14</a>.
    *   Measuring the remainder effectively "collapses" the first set of qubits into a [[superposition and entanglement | superposition]] of *only those exponents* that yield the measured remainder <a class="yt-timestamp" data-t="00:15:52">00:15:52</a>. Crucially, these exponents are all separated by the desired value `r` <a class="yt-timestamp" data-t="00:15:59">00:15:59</a>.
4.  **Apply [[Quantum Fourier transform | Quantum Fourier Transform]]**: With the remainder now uniform, the first set of qubits forms a periodic [[superposition and entanglement | superposition]] <a class="yt-timestamp" data-t="00:16:06">00:16:06</a>. Applying the [[Quantum Fourier transform | quantum Fourier transform]] to this [[superposition and entanglement | superposition]] will result in states containing information about `1/r` <a class="yt-timestamp" data-t="00:16:18">00:16:18</a>.
5.  **Measure `r`**: A final measurement yields `r` by inverting the `1/r` value <a class="yt-timestamp" data-t="00:16:28">00:16:28</a>.

Once `r` is found, the rest of the factoring process (using Euclid's algorithm) is performed on a classical computer <a class="yt-timestamp" data-t="00:16:36">00:16:36</a>. This significantly reduces the time it takes to break [[public_key_cryptography_and_rsa | RSA]] encryption.

## Progress in Quantum Computing

Breaking [[public_key_cryptography_and_rsa | RSA]] encryption with Shor's algorithm would require several thousand "perfect" qubits <a class="yt-timestamp" data-t="00:16:51">00:16:51</a>. Because current qubits are imperfect, additional qubits are needed for error correction <a class="yt-timestamp" data-t="00:16:58">00:16:58</a>.
*   In 2012, it was estimated that a billion physical qubits would be needed to break [[public_key_cryptography_and_rsa | RSA]] encryption <a class="yt-timestamp" data-t="00:17:02">00:17:02</a>.
*   By 2017, that estimate dropped to 230 million <a class="yt-timestamp" data-t="00:17:08">00:17:08</a>.
*   In 2019, after further technological breakthroughs, the estimate plummeted to just 20 million physical qubits <a class="yt-timestamp" data-t="00:17:12">00:17:12</a>.

While current quantum computers, such as IBM's, are nowhere near that number of qubits, progress appears to be exponential <a class="yt-timestamp" data-t="00:17:23">00:17:23</a>. This raises the question of when the capabilities of quantum computers will meet the requirements to break existing [[public_key_cryptography_and_rsa | public key encryption]] <a class="yt-timestamp" data-t="00:17:32">00:17:32</a>.

## [[Postquantum cryptography and latticebased encryption | Post-Quantum Cryptography]]

Knowing that this threat is coming, scientists have been developing new encryption methods resistant to both normal and quantum computers <a class="yt-timestamp" data-t="00:17:42">00:17:42</a>. In 2016, the National Institute of Standards and Technology (NIST) launched a competition to find such algorithms <a class="yt-timestamp" data-t="00:17:51">00:17:51</a>. Out of 82 proposals, NIST selected four algorithms on July 5th, 2022, to be part of their [[postquantum_cryptography_and_latticebased_encryption | post-quantum cryptographic standard]] <a class="yt-timestamp" data-t="00:17:58">00:17:58</a>.

### [[Postquantum cryptography and latticebased encryption | Lattice-Based Encryption]]

Three of the selected algorithms are based on the mathematics of lattices <a class="yt-timestamp" data-t="00:18:17">00:18:17</a>.

A lattice is formed by adding together different integer combinations of base vectors (e.g., `r1` and `r2` in 2D) to generate points <a class="yt-timestamp" data-t="00:18:24">00:18:24</a>. The challenge in [[postquantum_cryptography_and_latticebased_encryption | lattice-based encryption]] is the "closest vector problem": given a point `C` and a set of basis vectors (e.g., `b1` and `b2`) that define a lattice, find the lattice point closest to `C` <a class="yt-timestamp" data-t="00:18:42">00:18:42</a>.

While easy in 2D with "good" vectors, it becomes much harder with "bad" vectors where steps in one direction negatively affect progress in others <a class="yt-timestamp" data-t="00:19:01">00:19:01</a>. This difficulty rapidly increases with the number of dimensions <a class="yt-timestamp" data-t="00:19:55">00:19:55</a>. The number of lattice points within a given radius grows exponentially with dimensions (e.g., `r^2` in 2D, `r^3` in 3D) <a class="yt-timestamp" data-t="00:20:14">00:20:14</a>. Proposed future encryption schemes will use around a thousand dimensions, making it extremely difficult to find the closest point even for the most powerful computers, unless one possesses a "good" set of vectors <a class="yt-timestamp" data-t="00:20:41">00:20:41</a>.

To encrypt data using lattices:
1.  Each person has a secret "good" set of vectors that describes a lattice <a class="yt-timestamp" data-t="00:21:16">00:21:16</a>.
2.  They publicly share their lattice using a set of "hard" vectors <a class="yt-timestamp" data-t="00:21:22">00:21:22</a>.
3.  To send a message, one picks a point on the recipient's lattice corresponding to the message (e.g., a number) <a class="yt-timestamp" data-t="00:21:27">00:21:27</a>.
4.  Random noise is added to this lattice point, so the transmitted message is near, but not precisely at, the lattice point <a class="yt-timestamp" data-t="00:21:39">00:21:39</a>.
5.  To decode, the recipient must figure out which lattice point is closest to the noisy message point <a class="yt-timestamp" data-t="00:21:47">00:21:47</a>. This is extremely hard in high dimensions unless one has the "nice" (secret) set of vectors, which the recipient does <a class="yt-timestamp" data-t="00:21:53">00:21:53</a>.

This problem is considered extremely difficult to solve for both normal and quantum computers <a class="yt-timestamp" data-t="00:22:07">00:22:07</a>.

## Conclusion

Researchers, mathematicians, and cryptographers are working to ensure that secret data remains secret in the quantum age <a class="yt-timestamp" data-t="00:22:15">00:22:15</a>. Their efforts aim to avoid mass surveillance, protect critical infrastructure, and allow users to live as if quantum computers were never invented <a class="yt-timestamp" data-t="00:22:27">00:22:27</a>.

### Learning Resources

For those interested in [[Quantum mechanics and wave function | quantum mechanics]] and quantum algorithms, resources like Brilliant offer courses on quantum algorithms (co-developed with Microsoft and Alphabet X), which allow users to simulate quantum gates and execute real quantum algorithms <a class="yt-timestamp" data-t="00:23:04">00:23:04</a>. For deeper dives into cryptography, understanding statistics and data analysis is crucial, as making and breaking codes often involves statistical reasoning <a class="yt-timestamp" data-t="00:23:20">00:23:20</a>.