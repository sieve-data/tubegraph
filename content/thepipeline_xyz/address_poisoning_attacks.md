---
title: Address poisoning attacks
videoId: 18U5V0l5P7w
---

From: [[thepipeline_xyz]] <br/> 

Address poisoning is a type of attack in the crypto space where malicious actors exploit the way cryptocurrency addresses are displayed and how users interact with their transaction histories <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## What is an Address Poisoning Attack?

An address poisoning attack occurs when an attacker monitors an individual's crypto transactions <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Upon detecting an incoming or outgoing transaction, the attacker immediately sends a small transaction to the victim's wallet <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The crucial element of this attack is that the address used by the attacker is crafted to look very similar to a legitimate address the victim has previously interacted with, such as their own second wallet or a frequently used recipient's address <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## How it Works

1.  **Monitoring Transactions** <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>: Attackers observe public transaction ledgers, like EtherScan, to identify users and their transaction patterns <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
2.  **Crafting a Similar Address** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>: The attacker creates an address that closely mimics a legitimate one used by the victim. This often involves ensuring the fake address has the same initial and final characters as the genuine address (e.g., both start with "0x11" and end in "563FD") <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This tactic exploits the fact that many block explorers or wallet interfaces truncate the middle part of long addresses, showing only the beginning and end <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
3.  **Sending a "Poisoning" Transaction** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>: The attacker sends a minimal amount of crypto (e.g., 0 ETH) from this similar-looking address to the victim's wallet. This transaction then appears in the victim's transaction history <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.
4.  **Victim's Mistake** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>: If the victim is not paying close attention, they might scroll through their transaction history to find an address they want to send money to. Seeing the similar-looking address from the attacker's poisoning transaction, and possibly mistaking it for their own or a trusted recipient's address, they might inadvertently copy it <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
5.  **Fund Loss** <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>: The victim then sends a large amount of money to this copied, fraudulent address, unknowingly sending their funds directly to the attacker <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Consequences

Many individuals have fallen victim to these attacks, resulting in the loss of substantial amounts of cryptocurrency <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Prevention

To protect against address poisoning attacks:

*   **Be Aware** <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>: Understand that these types of [[Fraudulent transaction tactics | fraudulent transaction tactics]] exist.
*   **Verify Directly** <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>: Always copy and paste addresses from their direct, original source (e.g., your wallet's send function for your own address, or a trusted contact's direct communication). Do not rely on past transaction history for copying addresses, especially if you have had multiple small transactions <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Exact Match Verification** <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>: Before confirming any transaction, meticulously verify that the *entire* address you are sending to is the exact address you intend <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It's recommended to check not just the first and last few characters, but several characters throughout the address.