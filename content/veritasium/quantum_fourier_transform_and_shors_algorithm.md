---
title: Quantum Fourier transform and Shors algorithm
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 

## The Looming Threat of Quantum Computers to Encryption

Currently, some nation-states and individual actors are intercepting and storing large amounts of encrypted data, including passwords, bank details, and social security numbers, even though they cannot decrypt these files yet <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This practice, known as **Store Now, Decrypt Later (SNDL)**, operates on the belief that within the next 10 to 20 years, they will have access to a [[Quantum computing and public key algorithms | quantum computer]] capable of breaking existing encryption in minutes <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Valuable information, such as industrial and pharmaceutical research, and top-secret government intelligence, will still hold significance in a decade <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

The National Security Administration (NSA) acknowledges that a sufficiently large [[Quantum computing and public key algorithms | quantum computer]], if built, could undermine [[Quantum computing and public key algorithms | all widely deployed public key algorithms]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Experts predict that within a five to ten-year timeframe, [[Quantum computers and encryption | quantum computing will break encryption]] as we know it today <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Despite [[Quantum computers and encryption | sufficiently powerful quantum computers]] being years away, the SNDL threat is current, leading the U.S. Congress to mandate that all agencies begin transitioning to [[Quantum computers and encryption | new methods of cryptography that can't be broken by quantum computers]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Current Encryption Schemes: RSA

Our current encryption schemes have been highly successful for over 40 years <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Symmetric Key Algorithms
Up until the 1970s, exchanging private information required meeting in person to share a secret key, which would then be used for both encrypting and decrypting messages <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This is known as a symmetric key algorithm <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Asymmetric Key Algorithms (RSA)
The challenge arose when sending information to someone unknown, without an in-person meeting, or over unsecured channels like phone lines or mail where keys could be intercepted <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This led Rivest, Shamir, and Adelman to develop an encryption breakthrough in 1977, known today as RSA <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

RSA works as follows:
*   Each person has two large, secret prime numbers <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   These primes are multiplied together to get an even bigger number, which is made public <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   To send a private message, the sender uses the recipient's public number to garble the message in a way that makes it impossible to ungarble without knowing the two secret prime factors <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   This is an asymmetric key system, as different keys are used for encryption and decryption <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

It's easy for the intended recipient to decode but impossible for others unless they can factor that large public number <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Modern cryptography uses prime numbers around 313 digits long <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Factoring a product of two such large primes, even with a supercomputer using the General Number Field Sieve, would take approximately 16 million years <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. However, this is [[Quantum computers and encryption | not on a quantum computer]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## How Quantum Computers Work

### Bits vs. Qubits
In normal computers, a bit can only be in one state at a time (0 or 1) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. With two bits, there are four possible states (00, 01, 10, 11) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. A classical computer can perform a calculation for only one state at a time <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

Quantum computers use qubits, which also have two states (0 or 1), but a qubit doesn't have to be in just one state <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. It can be in an arbitrary combination of those states, a superposition of zero and one <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   Two qubits can exist simultaneously in a superposition of four states (0, 1, 2, 3) <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   When a calculation is performed, it acts on all these numbers simultaneously, resulting in a superposition of different answers <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Adding another qubit doubles the number of possible states <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Three qubits can represent eight states, performing eight calculations at once <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   Twenty qubits can represent over a million different states, allowing simultaneous computation of over a million answers <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   Three hundred qubits can represent more states than there are particles in the observable universe <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### The Measurement Problem
Despite this incredible power, there's a catch: all answers are embedded in a superposition of states, but you cannot simply read out this superposition <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. When a measurement is made, only a single value is obtained randomly from the superposition, and all other information is lost <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

To harness the power of a quantum computer, a smart way is needed to convert a superposition of states into one containing only the desired information <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This is incredibly difficult, making quantum computers useless for most applications <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. However, the few problems identified where this can be done are precisely the problems that form the foundation of nearly all public key cryptography today <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## [[Fast Fourier Transform | Quantum Fourier Transform]] (QFT)

In 1994, Peter Shor and Don Coppersmith figured out how to take a [[Fast Fourier Transform | quantum Fourier transform]] <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Like a normal Fourier transform, it applies to a periodic signal and returns the frequencies within that signal <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

If a superposition of states is periodic (terms are separated by a regular amount), applying the [[Fast Fourier Transform | quantum Fourier transform]] leaves states containing the frequency of the signal, which can then be measured <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. The [[Fast Fourier Transform | quantum Fourier transform]] allows the extraction of frequency information from a periodic superposition, which is crucial for Shor's algorithm <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Shor's Algorithm: Factoring Large Numbers

Shor's algorithm enables a [[Quantum computing and public key algorithms | quantum computer]] to factor the product of two primes much faster than a conventional computer <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Classical Factoring Example
Let's consider a number N, the product of two primes p and q. For example, N = 77 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
1.  **Choose a "bad guess" `g`**: Pick a number `g` that doesn't share any factors with N (e.g., g = 8 for N = 77) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
2.  **Find `r`**: Multiply `g` by itself repeatedly, raising `g` to higher powers, and divide each result by N, recording the remainder <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The goal is to find an exponent `r` such that `g^r` is one more than a multiple of N (i.e., `g^r mod N = 1`) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   For N=77, g=8:
        *   8^1 mod 77 = 8
        *   8^2 mod 77 = 64
        *   8^3 mod 77 = 50
        *   ...
        *   8^10 mod 77 = 1 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. So, `r = 10`.
    *   The sequence of remainders (8, 64, 50, 15, 43, 36, 57, 71, 29, 1) is periodic <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The period is `r`, the exponent that yields a remainder of 1 <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
3.  **Calculate new numbers**: Rearrange the equation `g^r = k*N + 1` to `g^r - 1 = k*N`, which can be factored as `(g^(r/2) + 1)(g^(r/2) - 1) = k*N` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. As long as `r` is even, these two terms (`g^(r/2) + 1` and `g^(r/2) - 1`) are likely to share factors with N <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
    *   For N=77, r=10: `g^(r/2) = 8^5 = 32768`.
    *   The two numbers are `32768 + 1 = 32769` and `32768 - 1 = 32767` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
4.  **Find shared factors (Euclid's Algorithm)**: Use Euclid's algorithm to find the greatest common divisor (GCD) between these new numbers and N <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   To find GCD(32769, 77):
        *   32769 / 77 -> remainder 44
        *   77 / 44 -> remainder 33
        *   44 / 33 -> remainder 11
        *   33 / 11 -> remainder 0 <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
    *   The GCD is 11, which is a factor of 77 <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Dividing 77 by 11 yields the other prime factor, 7 <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

This classical method is not faster than other factoring methods <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. The key step a quantum computer speeds up is **step two: finding the exponent `r`** <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

### Quantum Acceleration of Finding `r`
The sequence of remainders `g^x mod N` is periodic <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The period of this sequence is `r` (the exponent that yields a remainder of 1) <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Shor's algorithm leverages this periodicity using the [[Fast Fourier Transform | quantum Fourier transform]].

1.  **Prepare Qubits**: Split qubits into two sets. The first set is prepared in a superposition of all numbers from 0 up to a very large number (e.g., 10^1234), requiring about 4,100 perfect qubits <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. The second set starts in the zero state <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
2.  **Apply `g^x mod N`**: A guess `g` is chosen (unlikely to share factors with N). The quantum computer raises `g` to the power of the first set of qubits and stores the remainder (after dividing by N) in the second set, entangling the two sets <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
3.  **Partial Measurement**: Instead of measuring the entire superposition (which would yield a random, unhelpful value), only the remainder part is measured <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This yields some random remainder (e.g., 15 for N=77, g=8).
4.  **Periodic Superposition**: Since the remainder is now fixed, the first set of qubits collapses into a superposition of only the exponents that produce that specific remainder (e.g., 4, 14, 24, 34 for remainder 15) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. These exponents are periodic, separated by the value `r` (the period of the remainders) <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
5.  **Apply [[Fast Fourier Transform | Quantum Fourier Transform]]**: The [[Fast Fourier Transform | quantum Fourier transform]] is applied to this periodic superposition of exponents <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This operation leaves the states containing information about `1/r` <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.
6.  **Measure `r`**: A final measurement is performed to obtain `r` by inverting the measured value <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.

Once `r` is found (and assuming it's even), the remaining steps of Shor's algorithm are classical, using `r` to find the factors of N via Euclid's algorithm, thus breaking the encryption <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

### Qubit Requirements
Breaking RSA encryption with Shor's algorithm would ideally require several thousand perfect qubits <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. However, current qubits are imperfect, necessitating additional qubits for redundant information <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   In 2012, estimates suggested one billion physical qubits would be needed <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   By 2017, this dropped to 230 million <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   In 2019, after technological breakthroughs, the estimate plummeted to just 20 million physical qubits <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

While current quantum computers (like IBM's) are far from this number, progress is exponential, suggesting a future collision point where existing public key encryption could be broken <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## [[Postquantum cryptography and latticebased encryption | Post-Quantum Cryptography]]

Given the impending threat, scientists have been developing new encryption methods resistant to both normal and quantum computers <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. In 2016, the National Institute of Standards and Technology (NIST) launched a competition to find such algorithms <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. Out of 82 proposals, NIST selected four algorithms on July 5, 2022, to be part of their [[Postquantum cryptography and latticebased encryption | post-quantum cryptographic standard]] <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

### Lattice-Based Encryption
Three of the selected algorithms are based on the [[Postquantum cryptography and latticebased encryption | mathematics of lattices]] <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

A lattice is formed by adding together different integer combinations of a set of basis vectors (e.g., r1 and r2 in 2D) <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

#### The Closest Vector Problem
The core of lattice-based encryption relies on the "Closest Vector Problem": given a lattice and a point C, find the lattice point closest to C <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
*   If given a "good" set of basis vectors (e.g., r1 and r2 that are nearly orthogonal), solving this problem is easy <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.
*   However, if given a "bad" set of basis vectors (e.g., b1 and b2 that are highly non-orthogonal), finding the closest point becomes significantly harder <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

#### Increasing Dimensionality
While easy in 2D or 3D, extending this problem to higher dimensions dramatically increases difficulty:
*   The number of lattice points inside a sphere grows exponentially with the number of dimensions (e.g., proportional to r-squared in 2D, r-cubed in 3D) <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
*   Future encryption schemes propose using around a thousand dimensions <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. In such high dimensions, taking a correct step in one dimension might lead to many wrong steps in others, making it extremely hard to find the closest point even for the most powerful classical or quantum computers, *unless* one knows a good set of vectors <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

#### Encryption Process
1.  **Key Generation**: Each person has a "good" set of vectors describing a lattice, which they keep secret <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. They publicly share their lattice using a "bad" set of vectors that are hard to work with <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
2.  **Encryption**: To send a message (e.g., the number seven), the sender picks a lattice point corresponding to the message and adds some random noise to it, sending a point close to, but not exactly on, a lattice point <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
3.  **Decryption**: The recipient must then figure out which lattice point is closest to the noisy message point <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. In a thousand dimensions, this is extremely hard unless one has the "nice" set of vectors, which the recipient possesses <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.

This problem is believed to be extremely difficult for both normal and [[Quantum computing and public key algorithms | quantum computers]] to solve without the secret "good" vectors, making lattice-based encryption a promising path for securing data in the quantum era <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. An army of researchers, mathematicians, and cryptographers are working to ensure data remains secret, protecting critical infrastructure and privacy from the advancements in [[Quantum computing and public key algorithms | quantum computers]] <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.