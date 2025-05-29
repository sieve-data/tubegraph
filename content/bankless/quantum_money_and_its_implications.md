---
title: Quantum money and its implications
videoId: 5DRDjeMmOPw
---

From: [[bankless]] <br/> 

Quantum money is a conceptual form of digital cash that leverages the principles of quantum mechanics to ensure its security and prevent counterfeiting <a class="yt-timestamp" data-t="02:12:53">[02:12:53]</a>. Unlike traditional cryptocurrencies that rely on a network-wide consensus to prevent double-spending, quantum money could function much like physical cash, where a transfer between two parties does not require global knowledge or validation <a class="yt-timestamp" data-t="02:14:43">[02:14:43]</a>.

## How it Works

The core principle behind quantum money is the "no cloning theorem" of quantum mechanics <a class="yt-timestamp" data-t="02:15:15">[02:15:15]</a>. This fundamental fact states that it is impossible to create an exact copy of an unknown quantum state <a class="yt-timestamp" data-t="02:15:17">[02:15:17]</a>. In the context of quantum money:
*   The private keys are themselves quantum objects, existing in a "private superposition" <a class="yt-timestamp" data-t="02:24:56">[02:24:56]</a>.
*   When a message is signed with a quantum key, the private key is effectively destroyed, preventing it from being used again for double-spending <a class="yt-timestamp" data-t="02:25:05">[02:25:05]</a>.
*   Measuring old qubits to copy them would destroy the original copy <a class="yt-timestamp" data-t="02:25:40">[02:25:40]</a>.

### Historical Context

The idea of using the no cloning theorem to create physically unclonable cash dates back to the 1960s with Stephen Wiesner <a class="yt-timestamp" data-t="02:15:56">[02:15:56]</a>. Wiesner's scheme, while offering provable security, had the drawback that a bill had to be returned to the issuing bank for verification <a class="yt-timestamp" data-t="02:16:22">[02:16:22]</a>.

In 2009, theoretical computer scientist Scott Aaronson revitalized interest in quantum money by proposing schemes for "publicly verifiable quantum money," where anyone could verify a bill's genuineness, not just the bank <a class="yt-timestamp" data-t="02:16:48">[02:16:48]</a>. Although some initial proposals were later broken, current proposals appear to be secure, based on accepted cryptographic assumptions like indistinguishability obfuscation <a class="yt-timestamp" data-t="02:17:03">[02:17:03]</a>.

Interestingly, Aaronson first heard about [[bitcoin]] around 2010 or 2011 while giving talks about his new quantum money ideas <a class="yt-timestamp" data-t="02:18:33">[02:18:33]</a>. He noted that [[bitcoin]] required a "distributed process over the internet" and a blockchain that would "grow without bound," leading him to believe quantum money could someday be a superior solution <a class="yt-timestamp" data-t="02:29:05">[02:29:05]</a>.

## Implications and Feasibility

Quantum money's potential lies in its ability to function like cash without the need for a global consensus mechanism <a class="yt-timestamp" data-t="02:17:02">[02:17:02]</a>. This means no proof-of-work or proof-of-stake, and potentially no need for a continuously growing blockchain <a class="yt-timestamp" data-t="02:27:28">[02:27:28]</a>. It would leverage "nature's notepad," similar to how gold is considered "nature's ledger" <a class="yt-timestamp" data-t="02:27:32">[02:27:32]</a>.

However, the main drawback remains technological <a class="yt-timestamp" data-t="02:17:34">[02:17:34]</a>. Quantum money would require [[Quantum Computing and AI | quantum computers]] capable of preserving quantum states (coherence) for arbitrary amounts of time (weeks, months, years) <a class="yt-timestamp" data-t="02:18:03">[02:18:03]</a>. Additionally, many schemes would necessitate a [[Quantum Communications Network | quantum communications network]] or [[Quantum Communications Network | quantum internet]] to send these states between parties <a class="yt-timestamp" data-t="02:18:19">[02:18:19]</a>. These are capabilities imagined for some future era, likely decades away <a class="yt-timestamp" data-t="02:16:15">[02:16:15]</a>.

### Comparison to Existing Cryptocurrencies

*   **For [[bitcoin]]**: Quantum money is seen as a significant improvement because it eliminates the need for continuous security through fees or issuance <a class="yt-timestamp" data-t="02:27:03">[02:27:03]</a>. It could be the "gold" standard of digital money, with [[bitcoin]] potentially being more akin to "silver" <a class="yt-timestamp" data-t="02:28:41">[02:28:41]</a>.
*   **For Ethereum**: Quantum money, in its pure form, would not be an improvement for Ethereum, as it cannot support smart contracts <a class="yt-timestamp" data-t="02:26:52">[02:26:52]</a>.

It is predicted that the development of quantum money will likely occur after breakthroughs in [[Quantum Computing and AI | Grover's]] and [[Quantum Computing and AI | Shor's algorithms]] <a class="yt-timestamp" data-t="02:27:56">[02:27:56]</a>. This suggests it's a "third generation of applications" for [[Quantum Computing and AI | quantum computers]] <a class="yt-timestamp" data-t="02:27:56">[02:27:56]</a>.

### One-Shot Signatures

A related concept, "one-shot signatures," is highly dependent on [[Quantum Computing and AI | quantum computing]] and could potentially upgrade Ethereum <a class="yt-timestamp" data-t="02:21:19">[02:21:19]</a>. These signatures allow for "perfect finality" by making it physically impossible for a validator to sign two inconsistent messages <a class="yt-timestamp" data-t="02:22:01">[02:22:01]</a>. With one-shot signatures, the private key destroys itself after a single message <a class="yt-timestamp" data-t="02:22:24">[02:22:24]</a>. This could significantly reduce the need for trust in operators and simplify [[role_of_cryptocurrencies_as_money_and_store_of_value | delegated staking]] <a class="yt-timestamp" data-t="02:23:55">[02:23:55]</a>.