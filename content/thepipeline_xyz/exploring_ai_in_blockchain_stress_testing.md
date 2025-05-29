---
title: Exploring AI in blockchain stress testing
videoId: AcVshkaqI9I
---

From: [[thepipeline_xyz]] <br/> 

Blockchain systems, particularly those aiming for [[discussion_on_high_throughput_blockchains | high throughput]], require robust stress testing to ensure stability under extreme loads <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The goal is to simulate scenarios such as 100,000 concurrent users attempting to send 100 transactions per second or a massive NFT mint where "everyone slams an NFT at the same time" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Current Stress Testing Challenges
Past experiences highlight the unpredictability of user behavior during high-demand events. For instance, the Solana network in fall 2021 experienced issues due to "people from across the globe absolutely spam clicking mint buttons" <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, a scenario that was difficult to anticipate <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Common problems that emerge under stress, often reported on Twitter, include:
*   RPC failures <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Transaction getting reverted <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

The objective for new systems is to avoid making excuses when performance issues arise during high-stress situations <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Addressing these challenges is part of [[dealing_with_blockchain_system_failures | dealing with blockchain system failures]].

## Potential Role of AI Agents in Stress Testing
There is a growing interest in leveraging [[AI and blockchain potential intersections | AI agents]] for stress testing on blockchain testnets <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The combination of [[AI and blockchain potential intersections | AI]] and [[discussion_on_high_throughput_blockchains | high throughput]] could yield "interesting results" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Instead of human users, "robots clicking" could be utilized <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. One proposed approach involves incentivizing these AI agents to intentionally try and crash the testnet <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, thereby pushing the system to its limits in ways human-driven tests might not achieve. This proactive approach aims to identify weaknesses and optimize the system for unforeseen loads <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.