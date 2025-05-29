---
title: Quantum computing development and milestones
videoId: 5DRDjeMmOPw
---

From: [[bankless]] <br/> 

Quantum computing is a rapidly advancing field exploring the frontier of how computation can be performed, particularly its effects on "internet money" such as cryptocurrencies <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Experts like theoretical computer scientist Scott Aaronson are at the forefront of understanding its [[Impact of quantum computing on cryptography and cryptocurrency | impact on cryptography and cryptocurrency]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The progression of quantum computing is seen as a "microcosm" for its broader impact on society <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Recent Engineering Milestones

A significant recent development was the announcement by Google's CEO Sundar about their new state-of-the-art quantum computing chip, "Willow" <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Willow claims a breakthrough in reducing errors exponentially as more qubits are scaled <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

Scott Aaronson describes Willow as an "engineering milestone" rather than a new discovery, as the underlying theory of quantum error correcting codes dates back to the 1990s <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The excitement stems from experimentally demonstrating these 30-year-old predictions <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

The Willow chip uses 103 superconducting physical qubits arranged in a 10x10 grid to implement a "surface code," a quantum error correcting code known since 1997 <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This marks the first time that scaling to larger surface codes (e.g., from 3x3 to 5x5) has resulted in preserving an encoded qubit for progressively longer periods <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This is an important threshold, akin to the Fermi pile in 1942, where a larger code yields a net win <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## Quantum Computing vs. Classical Computing

A quantum computer is not merely a faster classical computer <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. It harnesses nature to perform computations in a fundamentally new way, changing the basic rules of what is efficiently computable <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

### Superposition and Amplitudes

Quantum mechanics dictates that systems can exist in "superposition states" <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. A qubit can be in a superposition of the zero and one states, each with an associated "amplitude" <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>. These amplitudes are not probabilities; they can be positive, negative, or even complex numbers <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>. While actual measurements yield definite answers (zero or one), the probabilities of these outcomes are derived from the square of the amplitudes <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.

For multiple qubits, the number of amplitudes grows exponentially (e.g., 2 to the power of 100 for 100 qubits) <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. Nature implicitly stores this vast "scratch paper" of amplitudes to track the states of even small numbers of particles <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

### Harnessing Quantum Mechanics for Computation

The idea of building a computer to take advantage of this exponentiality, rather than being hindered by it (as in simulating quantum systems classically), was proposed by physicists Richard Feynman and David Deutsch in the early 1980s <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>.

Initially, quantum computers were primarily envisioned for simulating quantum mechanics itself <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>. However, the discovery by Peter Shor in the mid-1990s that a quantum computer could dramatically speed up "purely classical problems" like factoring large numbers brought quantum computing to wider attention <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>. Shor's algorithm could factor an N-digit number in steps scaling roughly like N squared, an exponential speedup over classical methods <a class="yt-timestamp" data-t="00:30:55">[00:30:55]</a>.

### Interference as the Key

The common misconception is that quantum computers work by trying every possible solution in parallel <a class="yt-timestamp" data-t="00:31:59">[00:31:59]</a>. While they can create a superposition of all possible solutions, simply measuring this would yield a random answer <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. The true power lies in exploiting the complex nature of amplitudes to choreograph an "interference pattern" <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>. This causes contributions to amplitudes for wrong answers to cancel each other out (destructive interference), while contributions for the right answer reinforce each other (constructive interference), thereby boosting the probability of seeing the correct result <a class="yt-timestamp" data-t="00:34:19">[00:34:19]</a>.

This interference mechanism makes quantum computing applications specialized <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>. For example, Shor's algorithm exploits specific algebraic structures in problems like factoring and discrete logarithms (which underlie RSA, Diffie-Hellman, and elliptic curve encryption) <a class="yt-timestamp" data-t="00:36:57">[00:36:57]</a>. The core of Shor's algorithm is period finding, which it solves with an exponential speedup using a "Quantum Fourier Transform" <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.

## Current State and Future Outlook

Quantum computing is currently in an inflection point, transitioning from research and theory into practicality <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>. It's a matter of time, willpower, and expense <a class="yt-timestamp" data-t="00:39:42">[00:39:42]</a>.

### Hardware Challenges

Modern quantum computers, especially superconducting qubit-based ones, appear unusual due to the need for dilution refrigerators that cool chips to extreme temperatures (e.g., 10 millikelvin, a hundredth of a degree above absolute zero) <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>. This super-cold environment ensures qubits remain isolated from their environment, maintaining their superposition states for long enough to perform computations (e.g., 50 microseconds) <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>. The "wedding cake" structure of these refrigerators facilitates progressive cooling layers <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>. Additionally, extensive wiring connects classical computers, controlled by human operators, to the quantum chip to send commands and choreograph qubit operations <a class="yt-timestamp" data-t="00:44:33">[00:44:33]</a>.

### Scalability and Cost

While progress has been immense (from 50% qubit fidelity in the 1990s to 99.8% today), achieving fault-tolerant quantum computation for tasks like breaking cryptographic codes requires millions of physical qubits <a class="yt-timestamp" data-t="00:50:59">[00:50:59]</a>. This would necessitate hundreds or thousands of dilution refrigerators, all interconnected by a quantum communications network, potentially filling an entire building <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>. This level of scaling has not yet been demonstrated <a class="yt-timestamp" data-t="00:52:34">[00:52:34]</a>.

Current global spending on quantum information research and development is estimated at $40 billion per year <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a>. Scott Aaronson suggests it's plausible that "useful quantum advantages" could emerge within the next decade if sufficient resources are allocated <a class="yt-timestamp" data-t="00:51:52">[00:51:52]</a>. This mirrors historical parallels, such as the Manhattan Project, where immense resources rapidly advanced nuclear technology <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

### The Role of Logical Qubits

To perform digital computation that can break cryptography, "logical qubits" are needed <a class="yt-timestamp" data-t="01:36:56">[01:36:56]</a>. These are built from multiple "physical qubits," which are inherently noisy <a class="yt-timestamp" data-t="01:37:05">[01:37:05]</a>. Error correction mechanisms are necessary to extract pure digital signals from the noisy physical qubits <a class="yt-timestamp" data-t="01:37:12">[01:37:12]</a>. The Willow breakthrough represents the first successful demonstration of a single logical qubit, constructed from 101 physical qubits using a lattice structure for error correction <a class="yt-timestamp" data-t="01:37:34">[01:37:34]</a>. To break cryptography, thousands to hundreds of thousands of logical qubits would be required <a class="yt-timestamp" data-t="01:37:56">[01:37:56]</a>.

### Speed of Progress

There is an "equivalent of Moore's Law" for quantum computing, and it may even be faster than Moore's Law due to simultaneous improvements across multiple layers of the technology stack <a class="yt-timestamp" data-t="01:39:40">[01:39:40]</a>. This includes improvements in physical qubit fidelity, error correction methods (like new surface codes), and algorithms <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>. This multi-layered progress, similar to the rapid advancements in SNARKs (which improve by a factor of five annually), suggests that quantum computing is on an S-curve, indicating exponential growth <a class="yt-timestamp" data-t="01:40:18">[01:40:18]</a>.

While a full-scale fault-tolerant quantum computer is not yet available, the consensus is that the field is rapidly advancing, and quantum advantages are likely to emerge within the next decade, initially for quantum simulations, and then for more complex tasks like breaking cryptography <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>.