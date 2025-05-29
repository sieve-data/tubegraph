---
title: Use of flashbots in privacypreserving MEV extraction
videoId: w9SHvQNKqEM
---

From: [[goingonchain]] <br/> 

Flashbots play a role in managing [[maximal_extractable_value_mev_on_ethereum | MEV]] (Maximal Extractable Value) by connecting participants in a private pool, which aims to mitigate the negative impact of [[mev_extraction_strategies_like_gas_sniffing_and_front_running | MEV extraction]] on the public <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. When [[maximal_extractable_value_mev_on_ethereum | MEV]] occurs in a public pool, it can lead to increased gas prices, affecting general users <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

## How Flashbots Work

Flashbots facilitate a private channel for transactions, involving several steps:
1.  **Searchers Identify Opportunities**: Searchers actively monitor the mempool for profitable [[mev_extraction_strategies_like_gas_sniffing_and_front_running | MEV opportunities]] <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
2.  **Bundling**: Identified opportunities are bundled together <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
3.  **Sending to Flashbots Frontier**: These bundles are sent to a Flashbots Frontier <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
4.  **Block Building**: From the Frontier, block builders construct blocks <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.
5.  **Relay to Validators**: The built blocks are then sent to a relay <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
6.  **Selection by Validators**: The most profitable block is ultimately sent to the validators for inclusion in the blockchain <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

This private communication aims to allow for [[mev_extraction_strategies_like_gas_sniffing_and_front_running | MEV extraction]] without impacting the broader public network through artificially inflated gas prices <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>, <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

## Resources
*   Flashbots documentation <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>
*   Flashbots GitHub, which provides more insights into interesting use cases <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>