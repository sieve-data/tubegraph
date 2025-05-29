---
title: Challenges with RPC failures and transaction reverts
videoId: AcVshkaqI9I
---

From: [[thepipeline_xyz]] <br/> 

## The Problem of System Instability

When a blockchain system experiences issues, common problems observed include Remote Procedure Call (RPC) failures and transactions getting reverted <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. These issues frequently lead to explanations and excuses appearing on platforms like Twitter when something goes wrong <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The goal is to avoid having to make such excuses when things fail <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Impact on User Experience

These [[challenges_in_current_blockchain_infrastructure | challenges in current blockchain infrastructure]] significantly impact the user experience. The speaker recounts that RPC failures and transaction reverts comprised the entirety of their user experience on Solana in the fall of 2021 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Causes and Unforeseen Stresses

Such system failures often arise under conditions of extreme stress, which can be difficult to anticipate in advance <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Examples of high-stress scenarios include:

*   **NFT mints:** A large number of concurrent users trying to send transactions simultaneously, such as 100,000 people attempting 100 transactions per second, can slam the system <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This includes scenarios where people from across the globe are "spam clicking mint buttons" <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **High throughput:** The combination of AI agents and high throughput could yield interesting results, potentially by incentivizing AI to intentionally crash a testnet <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Addressing [[technical_challenges_and_solutions_in_blockchain_performance | Technical Challenges and Solutions]]

The aim for a system like Manad is to handle these extreme stress events gracefully <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This involves continuously looking at data and trying to further optimize performance <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The ultimate goal is to see a system stand up under high stress, such as an NFT mint where everybody is slamming the system, without the need to make excuses for its failure <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Future testing may involve observing AI agents on the testnet to see how they interact with high throughput scenarios <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.