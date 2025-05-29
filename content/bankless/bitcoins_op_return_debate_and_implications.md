---
title: Bitcoins Op Return debate and implications
videoId: KgDlTfKM8DA
---

From: [[bankless]] <br/> 

The Bitcoin community is currently engaged in a heated debate surrounding a potential upgrade concerning the `OP_RETURN` output, which mirrors some of the scaling discussions seen in the Ethereum ecosystem regarding block and blob space. <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>, <a class="yt-timestamp" data-t="00:57:56">[00:57:56]</a>

## What is OP_RETURN?

`OP_RETURN` functions as a dedicated space within Bitcoin transactions, similar to "call data" or "blob space" in Ethereum, allowing for the inclusion of arbitrary data. <a class="yt-timestamp" data-t="00:58:02">[00:58:02]</a>, <a class="yt-timestamp" data-t="00:58:07">[00:58:07]</a> Currently, this space has an 80-byte size limit. <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>

## The Debate

A significant part of the Bitcoin community is pushing to remove this 80-byte cap limit. <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>

### Arguments for Removing the Cap (Proponents)

Proponents of removing the `OP_RETURN` cap argue that the storage of arbitrary data on Bitcoin is inevitable. <a class="yt-timestamp" data-t="00:59:14">[00:59:14]</a> They believe that attempting to suppress it only leads to more harmful workarounds, such as securing data in other, less efficient ways or engaging in private deals with miners. <a class="yt-timestamp" data-t="00:59:18">[00:59:18]</a>
They assert that `OP_RETURN` is the "least damaging method" for data storage, as it is a small, provably unspendable location for data and helps avoid polluting the UTXO set. <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a> Other methods of embedding data in Bitcoin typically involve creating UTXOs (Unspent Transaction Outputs) with data in them. <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a> Essentially, they argue that since people will find ways to embed data regardless, it's better to formalize it. <a class="yt-timestamp" data-t="00:59:45">[00:59:45]</a>

### Arguments Against Removing the Cap (Critics)

Critics argue that removing the `OP_RETURN` limits would invite more "spam" and "non-monetary data" (often referred to as "graffiti") onto the Bitcoin blockchain. <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a> They contend that this would crowd out financial transactions and burden nodes. <a class="yt-timestamp" data-t="00:59:56">[00:59:56]</a>
This side of the debate often operates from a perspective that the network itself is a "burden," and its "only purpose" is to serve the Bitcoin asset. <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a> They view anything not directly using Bitcoin as money as a "burden and a distraction," hindering the progress of "hyperbitcoinization." <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a> They believe that if they could eliminate the network's ancillary uses, a large cohort of the Bitcoin community would. <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>

### Defining "Legitimate" Transactions

A core point of contention revolves around the definition of "legitimate" versus "illegitimate" Bitcoin transactions. <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>
The non-subjective way to interpret a legitimate transaction, according to the software, is if the fee is paid. <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>

## Implications

### Impact on Bitcoin Layer 2s

Eliminating the cap on `OP_RETURN` and allowing unconstrained arbitrary data would be "very good for [[bitcoins_security_budget_and_roadmap_challenges | Bitcoin Layer 2s]]". <a class="yt-timestamp" data-t="01:00:41">[01:00:41]</a>

### Philosophical Divide

There is a true lack of consensus on this issue, leading to a split within the Bitcoin community. <a class="yt-timestamp" data-t="01:00:36">[01:00:36]</a> This highlights a fundamental philosophical difference: whether the network should only facilitate monetary transactions or allow broader data applications.

### Comparison to Ethereum

The debate in Bitcoin parallels the "block versus blob size" discussions in Ethereum, where there is a tension between increasing data throughput for Layer 2s and maintaining the integrity and efficiency of the Layer 1 blockchain. <a class="yt-timestamp" data-t="00:57:50">[00:57:50]</a>