---
title: Impact of high throughput on system performance
videoId: AcVshkaqI9I
---

From: [[thepipeline_xyz]] <br/> 

High throughput scenarios, such as 100,000 concurrent users attempting 100 transactions per second, present significant challenges for system stability <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The goal is to handle these extreme loads gracefully without needing to provide excuses for system failures <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Stress Scenarios

Specific events, like an NFT mint where many users simultaneously interact with the system, can serve as super high-stress tests <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The challenge lies in anticipating such events, as seen with Solana's user experience in the fall of 2021, where global users "spam clicking mint buttons" caused unexpected stress <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Symptoms of Performance Degradation

Under severe stress, common issues include:
*   RPC (Remote Procedure Call) failures <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Transactions getting reverted <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

These problems often lead to public complaints on social media platforms like Twitter <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Testing and Optimization

Developers constantly analyze data to further optimize systems to prevent such failures <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While platforms like [[monads_parallel_execution_for_high_throughput | Manad]] are hoped to handle stress gracefully <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, new testing methods are being considered. The combination of AI and [[high_throughput_blockchains_and_infrastructure_challenges | high throughput]] could yield interesting results <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. For instance, incentivizing AI agents to deliberately crash a testnet could help identify system limits and vulnerabilities that human interaction might not reveal <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.