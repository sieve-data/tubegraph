---
title: Impact of quantum computing on Bitcoin mining
videoId: 5DRDjeMmOPw
---

From: [[bankless]] <br/> 

The advent of [[Quantum Computing and AI | quantum computing]] raises significant questions about the future of [[Future challenges for Bitcoin with quantum advancements | Bitcoin]] and other cryptocurrencies. While still in early engineering phases, the theoretical understanding of quantum computers suggests they could fundamentally impact existing cryptographic systems, including those underlying Bitcoin's security model <a class="yt-timestamp" data-t="01:02:54">[01:02:54]</a>.

## Understanding Quantum Computing's Edge

Unlike classical computers, quantum computers harness the laws of quantum mechanics to perform computations in fundamentally new ways <a class="yt-timestamp" data-t="02:26:01">[02:26:01]</a>. They exploit phenomena like superposition and interference, where quantum bits (qubits) can exist in multiple states simultaneously <a class="yt-timestamp" data-t="02:16:04">[02:16:04]</a>. The core difference lies in how these amplitudes (numbers attached to possibilities) can be positive, negative, or even complex, allowing for choreographed interference patterns to amplify correct answers and cancel out wrong ones <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

While a universal quantum computer capable of breaking [[Quantum Computing and cryptography | cryptography]] for digital signatures is still in the future, the theory predicts significant advantages for specific problems <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>.

## Impact on Bitcoin's Proof-of-Work

Bitcoin's consensus mechanism, Proof-of-Work (PoW), relies on miners solving a computational puzzle by finding a "golden nonce" through searching a vast space of possible solutions <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a> <a class="yt-timestamp" data-t="01:42:06">[01:42:06]</a>. This process primarily uses hash functions.

### Grover's Algorithm: A Modest Speedup
For problems involving searching a giant list of possible solutions, like those in Bitcoin mining, [[Quantum Computing and cryptography | Grover's algorithm]] offers a speedup <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>. However, this is a *modest* speedup, typically reducing the number of steps required to roughly the square root of what a classical computer would need (e.g., N steps become √N steps) <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. This is not an exponential speedup like Shor's algorithm provides for breaking public-key cryptography <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a> <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

### The Role of Error Correction
Building a fault-tolerant quantum computer requires extensive error correction, which introduces a significant overhead, potentially a factor of a million, compared to ideal quantum computation <a class="yt-timestamp" data-t="01:01:39">[01:01:39]</a>. This means a quantum computer only becomes a net win for mining when the problem size (N) is astronomically large, potentially in the trillions <a class="yt-timestamp" data-t="01:02:30">[01:02:30]</a>.

### Centralization and Transition Risks
If only a few entities possess scalable quantum computers, they could mine significantly more Bitcoin than everyone else, leading to a massive centralization of mining power <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>.

During the transition period from classical to quantum mining, there's a risk of a "first mover" or a small group of dominant actors controlling over 50% of the hash rate <a class="yt-timestamp" data-t="01:19:09">[01:19:09]</a> <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. This could allow them to acquire the Bitcoin network, control transaction fees, and even manipulate the market <a class="yt-timestamp" data-t="01:56:06">[01:56:06]</a>. The gap in performance between the best and second-best quantum miners could be orders of magnitude <a class="yt-timestamp" data-t="02:01:06">[02:01:06]</a>.

However, if [[Quantum Computing and cryptography | quantum computing]] becomes widely accessible, the Bitcoin proof-of-work algorithm would automatically adjust its difficulty to compensate for the increased computing power, returning to a state where competition remains <a class="yt-timestamp" data-t="01:18:47">[01:18:47]</a> <a class="yt-timestamp" data-t="01:58:50">[01:58:50]</a>. This scenario, however, might only apply over the *very* long term <a class="yt-timestamp" data-t="01:19:04">[01:19:04]</a>.

### Potential Solutions for Proof-of-Work
While the current Proof-of-Work is susceptible to Grover's algorithm, alternative proof-of-work tasks that offer more quantum resistance exist <a class="yt-timestamp" data-t="02:10:30">[02:10:30]</a>. For example, "proof of space" protocols could see little to no quantum advantage <a class="yt-timestamp" data-t="02:10:51">[02:10:51]</a>. Implementing such changes would require a hard fork of the Bitcoin blockchain, a significant social and technical undertaking <a class="yt-timestamp" data-t="02:10:51">[02:10:51]</a>.

## Impact on Bitcoin's Digital Signatures

Beyond mining, Bitcoin (and [[Ethereums competitive position against Bitcoin | Ethereum]]) rely on elliptic curve cryptography (ECDSA) for digital signatures, which are used to control account balances <a class="yt-timestamp" data-t="01:04:38">[01:04:38]</a> <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. Shor's algorithm, unlike Grover's, offers an exponential speedup for breaking this type of cryptography <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

A quantum computer capable of breaking elliptic curve cryptography would be a "fully programmable device" and could be reprogrammed to break other widely used encryption methods like RSA and Diffie-Hellman <a class="yt-timestamp" data-t="01:53:20">[01:53:20]</a>. Estimates suggest breaking a 2048-bit key could take a quantum computer about a week <a class="yt-timestamp" data-t="01:55:37">[01:55:37]</a>. While this might initially be used only for "very high value targets," costs are expected to decrease over time <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a> <a class="yt-timestamp" data-t="01:56:46">[01:56:46]</a>.

### The "Lost Coins" Dilemma
A unique challenge for Bitcoin is the existence of "lost coins" or early Bitcoin addresses, including Satoshi Nakamoto's estimated 1 million BTC, where the public key is exposed on-chain <a class="yt-timestamp" data-t="01:08:36">[01:08:36]</a> <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>. These coins cannot be upgraded through a simple hard fork to [[Upgrading blockchain systems for quantum resistance | quantum-resistant]] cryptography <a class="yt-timestamp" data-t="01:11:21">[01:11:21]</a>. This creates a potential "societal bounty" for whoever develops a quantum computer capable of breaking these keys <a class="yt-timestamp" data-t="01:09:10">[01:09:10]</a> <a class="yt-timestamp" data-t="01:52:53">[01:52:53]</a>.

The Bitcoin community faces a significant social conundrum: either intervene to freeze or destroy these vulnerable coins (going against Bitcoin's immutability principle) or risk them being stolen <a class="yt-timestamp" data-t="01:43:52">[01:43:52]</a> <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a> <a class="yt-timestamp" data-t="02:13:16">[02:13:16]</a>. A potential solution could be a soft fork to censor transactions from compromised addresses <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>, but this challenges the network's core tenets <a class="yt-timestamp" data-t="01:47:42">[01:47:42]</a>.

## Timeline and Broader Implications

While the threat is not immediate, experts suggest that within the next decade, quantum simulations could yield interesting new things about nature <a class="yt-timestamp" data-t="04:47:41">[04:47:41]</a>. Breaking RSA or ECDSA could take longer, with estimates for the cost to break ECDSA ranging around $10 billion in R&D <a class="yt-timestamp" data-t="04:39:10">[04:39:10]</a> <a class="yt-timestamp" data-t="04:49:04">[04:49:04]</a>. Current global spending on [[Quantum Computing and AI | quantum information research]] is already in the billions <a class="yt-timestamp" data-t="04:49:04">[04:49:04]</a>.

The challenge for Bitcoin is dual: the vulnerability of its digital signatures and the potential disruption to its Proof-of-Work <a class="yt-timestamp" data-t="01:41:54">[01:41:54]</a>. This "doubly screwed" position contrasts with [[Ethereums competitive position against Bitcoin | Ethereum]]'s transition to Proof-of-Stake and its more flexible [[Upgrading blockchain systems for quantum resistance | upgrade path]] for cryptographic elements <a class="yt-timestamp" data-t="02:11:15">[02:11:15]</a>.

The long-term viability of Bitcoin, particularly in the face of quantum advancements, remains a significant topic for discussion, potentially necessitating difficult social and technical decisions that could alter its fundamental characteristics <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a> <a class="yt-timestamp" data-t="02:13:44">[02:13:44]</a>.