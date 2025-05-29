---
title: highfrequency trading systems
videoId: mee-5mcuvMU
---

From: [[thepipeline_xyz]] <br/> 

High-frequency trading (HFT) systems are highly performant setups designed to execute trades at extreme speeds in competitive financial markets <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The core job of such a system is to build a full trading infrastructure from scratch <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## System Mechanics and Operation

An HFT system operates by:
*   Ingesting large volumes of data packets from exchanges <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   Making rapid trading decisions <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   Sending orders back out to the exchange <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Competitive Landscape

The HFT space is characterized by intense competition <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Success hinges on being faster than competitors; if a packet arrives from an exchange and multiple parties react simultaneously, the entity that decides faster and sends the order first wins the opportunity <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This opportunity can involve:
*   Taking liquidity for an aggressive order <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   Getting into the queue for a passive order <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

This environment is "super latency competitive" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, driving continuous improvements to shave off latency and build a highly [[impact_of_high_throughput_on_system_performance | performant system]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Origins and Evolution

The foundational inspiration for building highly performant systems, such as Monad, stemmed from experience with high-frequency trading <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Key team members met in 2014 while working on a high-frequency trading team at [[market_making_in_crypto_vs_traditional_finance | Jump trading]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This experience of building from the ground up for performance was directly transferable to addressing inefficiencies found in existing blockchain environments, particularly the EVM <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

[!INFO] The expertise gained from optimizing traditional HFT systems, including the focus on low-latency and high-[[impact_of_high_throughput_on_system_performance | performance]] architectures, was later applied to solving challenges in the blockchain space <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This background was considered perfect for tackling the problem of building very [[impact_of_high_throughput_on_system_performance | performant systems]] from the ground up in the crypto domain <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.