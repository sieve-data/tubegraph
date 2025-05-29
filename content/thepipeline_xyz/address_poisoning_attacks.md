---
title: Address poisoning attacks
videoId: 18U5V0l5P7w
---

From: [[thepipeline_xyz]] <br/> 

Address poisoning attacks are a type of [[common_cryptocurrency_scams | cryptocurrency scam]] where an attacker exploits user habits by sending a transaction to a target with an address that closely mimics one the target frequently uses, often their own wallet address <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## How it Works

The attack typically begins when a user sends cryptocurrency and observes the transaction in their transaction ledger, such as EtherScan <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. An attacker may be monitoring this activity <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Immediately following the legitimate transaction, the attacker sends a small transaction to the target's wallet <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The sender's address of this small transaction is crafted to look very similar to an address the target recently interacted with, often their own wallet address <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

For example, if a user's address begins with "0x11" and ends in "563FD", the attacker can generate an address that has the same initial and final characters <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. In many interfaces, only the beginning and end of an address are fully visible, obscuring the differing middle characters <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

When the user later intends to send funds, perhaps even to one of their own wallets <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, they might mistakenly copy the attacker's "poisoned" address from their transaction history, believing it to be a legitimate address they had previously used <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Consequences

If the user proceeds to send funds to the copied "poisoned" address, they risk accidentally sending a large amount of money to the attacker <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This has led to significant financial losses for victims <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Prevention

To protect against address poisoning attacks, users should always:
*   Be vigilant and aware of this scam <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   Use the direct, verified source for copy-pasting addresses <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   Before confirming any transaction, rigorously verify that the *entire* address, from start to finish, matches the intended recipient's address <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.