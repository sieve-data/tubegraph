---
title: Bitcoins OPRETURN debate and implications
videoId: KgDlTfKM8DA
---

From: [[bankless]] <br/> 

A significant debate is underway within the [[Bitcoin]] community regarding the "OP_RETURN" function, which allows arbitrary data to be embedded in [[Bitcoin]] transactions <a class="yt-timestamp" data-t="00:57:56">[00:57:56]</a>. This discussion draws parallels to the "block vs. blob size" debates seen in the [[Ethereum]] community <a class="yt-timestamp" data-t="00:57:50">[00:57:50]</a>.

## What is OP_RETURN?
OP_RETURN is a function in [[Bitcoin]] that enables the inclusion of arbitrary data within transactions <a class="yt-timestamp" data-t="00:58:22">[00:58:22]</a>. It is described as similar to [[Ethereum]]'s "call data" or "blob space" <a class="yt-timestamp" data-t="00:58:02">[00:58:02]</a>. Currently, there is an 80-byte size limit on OP_RETURN data <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>. Notably, this is where "ordinals" data is being stored <a class="yt-timestamp" data-t="00:58:26">[00:58:26]</a>.

## Proponents for Removing the Cap
Supporters of removing the 80-byte cap on OP_RETURN argue that arbitrary data storage on [[Bitcoin]] is inevitable <a class="yt-timestamp" data-t="00:59:14">[00:59:14]</a>. They believe that attempting to suppress it only leads to more harmful workarounds, such as securing data in other ways or making private deals with miners <a class="yt-timestamp" data-t="00:59:18">[00:59:18]</a>. Proponents suggest that OP_RETURN is the "least damaging method" for data storage, as it is a small, provably unspendable space that avoids polluting the UTXO set <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a>.

## Critics Against Removing the Cap
Critics argue that removing the limits on OP_RETURN would invite more "spam" and "non-monetary data" into the [[Bitcoin]] blockchain <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>. They describe this as "graffiti" that could crowd out financial transactions and burden nodes <a class="yt-timestamp" data-t="00:59:56">[00:59:56]</a>. This perspective introduces a notion of "legitimate" versus "illegitimate" [[Bitcoin]] transactions <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>.
*   **Legitimate transactions**: Defined as those made for commerce, using [[Bitcoin]] as money <a class="yt-timestamp" data-t="01:00:06">[01:00:06]</a>.
*   **Illegitimate transactions**: Those containing arbitrary data <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.

However, it is noted that the definition of a "legitimate" [[Bitcoin]] transaction, according to the [[Bitcoin]] core code, is simply one for which a fee is paid <a class="yt-timestamp" data-t="01:00:24">[01:00:24]</a>.

## Implications and Broader Philosophy
There is currently a significant lack of consensus on this issue within the [[Bitcoin]] community <a class="yt-timestamp" data-t="01:00:36">[01:00:36]</a>. Eliminating the cap on OP_RETURN and allowing unconstrained arbitrary data would be beneficial for [[Bitcoins_Rollupcentric_Roadmap_and_Comparison_with_Ethereum | Bitcoin Layer 2s]] <a class="yt-timestamp" data-t="01:00:48">[01:00:48]</a>.

Some observers suggest that a segment of the [[Bitcoin]] community would prefer not to have a network at all, as the network is seen as a "burden" whose only purpose is to support the [[Bitcoin]] asset itself <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>. Everything else is considered "graffiti" or a "means to an end" <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>. This perspective views activities not directly related to [[Bitcoin]]'s function as a financial asset as a "burden and a distraction" that slows down the progress of "hyperbitcoinization" <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a>. The debates are described as very "hardcore" <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>.