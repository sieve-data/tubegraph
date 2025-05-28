---
title: Quantum Fourier transform
videoId: -UrdExQW0cs
---

From: [[veritasium]] <br/> 
The [[quantum_mechanics_and_wave_function | Quantum Fourier Transform]] (QFT) is a critical component in [[quantum_computing_and_encryption | quantum computing]], particularly for tasks such as breaking encryption algorithms.

## Overview
The [[quantum_mechanics_and_wave_function | Quantum Fourier Transform]] is a quantum analogue of the classical Fourier transform <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. It was first conceived by Peter Shor and Don Coppersmith in 1994 <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. Its primary function is to extract frequencies from periodic signals <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

## How it Works
When applied to a periodic superposition of states—where the terms in the superposition are separated by a regular amount—the [[quantum_mechanics_and_wave_function | Quantum Fourier Transform]] returns states that contain the frequency of that signal <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. This allows for the measurement and extraction of frequency information from the periodic superposition <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.

## Application in Factoring (Shor's Algorithm)
The [[quantum_mechanics_and_wave_function | Quantum Fourier Transform]] plays a key role in the ability of [[quantum_computing_and_encryption | quantum computers]] to factor large products of two primes, a problem that is computationally intensive for classical computers <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.

The core of factoring in this context involves finding an exponent 'r' such that a chosen number 'g' raised to the power of 'r' (g^r) is one more than a multiple of the number 'N' to be factored (g^r = 1 mod N) <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>. The remainders of g^x when divided by N exhibit a periodic pattern <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>. The period of this pattern is the exponent 'r' <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.

On a [[quantum_computing_and_encryption | quantum computer]], this process is significantly accelerated:
1.  **Superposition Preparation:** Two sets of qubits are prepared. The first set is put into a superposition of a vast range of numbers <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.
2.  **Calculation and Entanglement:** A chosen guess 'g' is raised to the power of the numbers represented by the first set of qubits, and the remainder when divided by 'N' is stored in the second set of qubits. This action entangles the two sets <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.
3.  **Measurement and Periodic Superposition:** By measuring only the remainder part of the entangled superposition, a random remainder is obtained <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>. Crucially, this measurement collapses the first set of qubits into a periodic superposition of states, where all the exponents correspond to the chosen remainder, and they are all separated by the desired value 'r' <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>.
4.  **Application of QFT:** With the remainder put aside, the periodic superposition of exponents remains <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>. Applying the [[quantum_mechanics_and_wave_function | Quantum Fourier Transform]] to this superposition results in states containing information about '1/r' <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>.
5.  **Extraction of 'r':** A final measurement extracts 'r' by inverting the measured value <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.

Once 'r' is found, and if it is an even number, it can be used with classical algorithms like Euclid's algorithm to efficiently find the prime factors of 'N' and break the encryption <a class="yt-timestamp" data-t="16:36:00">[16:36:00]</a>. This capability makes current [[quantum_computing_and_encryption | public key encryption schemes]] vulnerable, necessitating the development of [[postquantum_cryptography_and_latticebased_encryption | post-quantum cryptography]] <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.