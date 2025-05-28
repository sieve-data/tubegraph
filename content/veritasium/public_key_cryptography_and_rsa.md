---
title: Public key cryptography and RSA
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 

Today, nation-states and individual actors are intercepting and storing vast amounts of [[quantum_computing_and_encryption | encrypted]] data, including passwords, bank details, and social security numbers, even though they cannot currently access these files <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This practice, known as Store Now, Decrypt Later (SNDL), is based on the belief that within the next 10 to 20 years, they will possess a [[quantum_computing_and_encryption | quantum computer]] capable of breaking current [[quantum_computing_and_encryption | encryption]] in minutes <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Information like industrial research, pharmaceutical research, and top-secret government intelligence is expected to remain valuable for decades <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

The National Security Administration (NSA) acknowledges that a sufficiently large [[quantum_computing_and_encryption | quantum computer]], if built, could undermine all widely deployed public key algorithms <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Due to this threat, the US Congress has passed legislation mandating that all agencies begin transitioning to new methods of [[quantum_computing_and_encryption | cryptography]] that are resistant to [[quantum_computing_and_encryption | quantum computers]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Evolution of Cryptography

### Symmetric Key Algorithms
Prior to the 1970s, exchanging private information required meeting in person to share a secret key <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This same key was then used for both encrypting and decrypting messages, a method known as a symmetric key algorithm <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. While secure as long as the key remained secret, it was impractical for communicating with unknown parties or over unsecured channels <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### RSA: The Asymmetric Key Breakthrough
In 1977, three scientists—Rivest, Shamir, and Adelman—developed an [[quantum_computing_and_encryption | encryption]] breakthrough known by their initials, RSA <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This system is based on the concept of asymmetric keys, where different keys are used for [[quantum_computing_and_encryption | encryption]] and decryption <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

The RSA algorithm works as follows:
1.  Each person generates two very large [[mathematical_uniqueness_of_prime_numbers | prime numbers]] and keeps them secret <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  These two [[mathematical_uniqueness_of_prime_numbers | prime numbers]] are multiplied together to produce an even larger number, which is made public <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
3.  To send a private message, the sender uses the recipient's public number to "garble" the message <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
4.  The message is garbled in a way that makes it impossible to ungarble without knowing the two secret [[mathematical_uniqueness_of_prime_numbers | prime factors]] that created the public number <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
5.  The intended recipient can easily decode the message using their secret [[mathematical_uniqueness_of_prime_numbers | prime numbers]], but anyone else would need to factor the large public number <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Current [[quantum_computing_and_encryption | cryptography]] utilizes [[mathematical_uniqueness_of_prime_numbers | prime numbers]] that are approximately 313 digits long <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Factoring a product of two such large [[mathematical_uniqueness_of_prime_numbers | primes]] using the best-known classical algorithm (General Number Field Sieve) with a supercomputer would take around 16 million years <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## The Quantum Threat to RSA

### How Quantum Computers Work
Unlike classical computers that use bits (0 or 1), [[quantum_computing_and_encryption | quantum computers]] use qubits, which can exist in a superposition of both 0 and 1 simultaneously <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   Two bits can be in one of four states (00, 01, 10, 11) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   Two qubits can simultaneously exist in a superposition of all four states <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   This allows [[quantum_computing_and_encryption | quantum computers]] to perform calculations for all possible states at once <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Adding more qubits exponentially increases the number of states that can be represented and computed simultaneously <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. For example, 20 qubits can represent over a million states, allowing for over a million simultaneous computations <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. 300 qubits can represent more states than there are particles in the observable universe <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

>[!WARNING] The Catch with Quantum Measurement
>The major limitation is that when a measurement is made on a superposition, only a single random value is obtained, and all other information is lost <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. To harness the power of a [[quantum_computing_and_encryption | quantum computer]], a clever method is needed to transform a superposition into one that contains only the desired information <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This is why for most applications, [[quantum_computing_and_encryption | quantum computers]] are currently useless <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. However, factoring large numbers, which underpins modern public key [[quantum_computing_and_encryption | cryptography]], is one of the few problems for which a solution has been identified <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Shor's Algorithm and Quantum Fourier Transform
In 1994, Peter Shor and Don Coppersmith discovered how to use the quantum Fourier transform to factor large numbers <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. A quantum Fourier transform can extract frequency information from a periodic superposition <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

#### Factoring N (Example N=77)
The method for factoring a number N (product of two [[mathematical_uniqueness_of_prime_numbers | primes]] p and q) using a [[quantum_computing_and_encryption | quantum computer]] builds upon a classical approach:
1.  **Choose a guess (g)**: Pick a number `g` that does not share any factors with N (e.g., N=77, g=8) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
2.  **Find the exponent (r)**: Determine the exponent `r` such that `g^r` is one more than a multiple of N (i.e., `g^r mod N = 1`) <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   This step involves repeatedly multiplying `g` by itself and finding the remainder when divided by N. The remainders cycle periodically <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The period of this cycle is the exponent `r` <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    *   For N=77 and g=8, `8^10 mod 77 = 1`, so r=10 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
3.  **Calculate two new numbers**: If `r` is even, use the exponent to calculate `g^(r/2) + 1` and `g^(r/2) - 1` <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. These numbers will likely share factors with N <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
    *   For r=10, the numbers are `8^5 + 1` (32,769) and `8^5 - 1` (32,767) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
4.  **Find shared factors with Euclid's Algorithm**: Use Euclid's algorithm to find the greatest common divisor (GCD) between these two new numbers and N <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This will yield the [[mathematical_uniqueness_of_prime_numbers | prime factors]] of N <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
    *   GCD(32769, 77) = 11, and GCD(32767, 77) = 7 <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. Thus, the [[mathematical_uniqueness_of_prime_numbers | prime factors]] of 77 are 11 and 7 <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

#### Quantum Speed-up (Step 2)
The key process that a [[quantum_computing_and_encryption | quantum computer]] accelerates is step 2: finding the exponent `r` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
1.  Initialize qubits in a massive superposition representing all possible exponents <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
2.  Perform the calculation `g^x mod N` for all these exponents `x` simultaneously, storing the remainders in a second set of qubits, entangling the two sets <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
3.  Measure only the remainder part of the superposition. This yields a random remainder, but the remaining superposition of exponent states will be periodic, with each term separated by `r` (the exponent we are looking for) <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
4.  Apply the quantum Fourier transform to this periodic superposition. This converts the states to contain `1/R` (where R is the period), which can then be measured to find `R` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This `R` is the desired exponent `r` <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

This process allows a [[quantum_computing_and_encryption | quantum computer]] to find `r` for very large numbers in a short period <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

### Qubit Requirements
While Shor's algorithm only requires several thousand "perfect" qubits, today's qubits are imperfect, necessitating additional qubits for redundant information and error correction <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   In 2012, an estimated one billion physical qubits were needed to break RSA [[quantum_computing_and_encryption | encryption]] <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   By 2017, this estimate dropped to 230 million <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   In 2019, after technological advancements, the estimate plummeted to just 20 million physical qubits <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.
Progress in [[quantum_computing_and_encryption | quantum computer]] development appears to be exponential <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

## Post-Quantum Cryptography

Recognizing the impending threat, scientists have been developing new [[quantum_computing_and_encryption | encryption]] methods resilient to both classical and [[quantum_computing_and_encryption | quantum computer]] attacks <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
In 2016, the National Institute of Standards and Technology (NIST) launched a competition to identify such algorithms <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. After rigorous testing of 82 proposals, NIST selected four algorithms on July 5, 2022, to be part of their [[postquantum_cryptography_and_latticebased_encryption | post-quantum cryptographic]] standard <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

### Lattice-Based Encryption
Three of the selected algorithms are based on the mathematics of [[postquantum_cryptography_and_latticebased_encryption | lattices]] <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
*   A [[postquantum_cryptography_and_latticebased_encryption | lattice]] is a collection of points generated by adding together integer combinations of basis vectors <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   The security of [[postquantum_cryptography_and_latticebased_encryption | lattice-based encryption]] relies on the "closest vector problem" (CVP): finding the lattice point closest to a given target point <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   While easy in low dimensions with "good" (orthogonal-like) basis vectors, CVP becomes extremely difficult in high dimensions, especially when given "bad" (non-orthogonal) basis vectors <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
*   The difficulty increases exponentially with dimensions. For instance, in a thousand dimensions, a single step in the correct direction can result in wrong steps across 999 other dimensions <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

#### Lattice-Based Encryption Scheme:
1.  Each user has a "good" (secret) set of vectors that define a [[postquantum_cryptography_and_latticebased_encryption | lattice]] <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.
2.  They publicly share their [[postquantum_cryptography_and_latticebased_encryption | lattice]] using a "bad" (hard-to-work-with) set of vectors <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
3.  To send a message (e.g., a number corresponding to a [[postquantum_cryptography_and_latticebased_encryption | lattice]] point), the sender picks that [[postquantum_cryptography_and_latticebased_encryption | lattice]] point and adds random noise to it <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
4.  The recipient, possessing the "good" vectors, can easily determine which [[postquantum_cryptography_and_latticebased_encryption | lattice]] point is closest to the received message point, thus decoding it <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.
5.  Without the "good" vectors, finding the closest point in a thousand dimensions is extremely difficult for even the most powerful classical or [[quantum_computing_and_encryption | quantum computers]] <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

This ongoing research and development by cryptographers and mathematicians are crucial for ensuring data privacy, protecting critical infrastructure, and preventing mass surveillance in a future with powerful [[quantum_computing_and_encryption | quantum computers]] <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.