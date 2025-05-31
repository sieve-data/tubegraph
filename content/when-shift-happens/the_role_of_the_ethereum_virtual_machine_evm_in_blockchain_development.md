---
title: The role of the Ethereum Virtual Machine EVM in blockchain development
videoId: dUuF9eLoUQo
---

From: [[when-shift-happens]] <br/> 

The [[ethereum_and_smart_contracts | Ethereum Virtual Machine (EVM)]] serves as a foundational technology in the blockchain space, processing the majority of transactions across various networks <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. Approximately 80% to 90% of developers in the crypto industry are currently EVM developers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>, indicating its widespread adoption.

## Origins and Design Philosophy

The EVM was revolutionary as the first blockchain to introduce the concept of a general-purpose virtual machine, a "Turing complete" virtual machine <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>, <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. However, when [[ethereum_development_and_challenges | Ethereum]] was initially built, performance was not a primary design consideration <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. The main objective was to create a functional virtual machine that users could utilize <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>. Early [[ethereum_development_and_challenges | Ethereum development]] faced financial constraints, making it difficult to prioritize performance alongside core functionality <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.

## Current Challenges and Limitations

Despite its widespread use, the EVM faces significant performance limitations <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. Issues such as high transaction costs (e.g., $100 in gas fees) make [[ethereum_development_and_challenges | Ethereum]] inaccessible to many ordinary users <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>. This limitation is a major hurdle, as it is incredibly difficult to transition away from a virtual machine once it has achieved such broad adoption <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>.

## The Need for Scaling the EVM

Recognizing the EVM's established presence and its performance bottlenecks, companies like Say Labs have focused on scaling it <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>, <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. The goal is to solve the fundamental issues of poor EVM performance <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.

### Parallelized EVM (Say V2)

Say Labs' solution, Say V2, is the first parallelized EVM <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>, <a class="yt-timestamp" data-t="01:09:12">[01:09:12]</a>. This innovation addresses the performance limitations by allowing multiple independent transactions to be processed simultaneously <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

**How Parallelization Works:**
Traditional blockchains often process transactions sequentially, even if they are unrelated <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. Parallelization, as explained by analogy, is like baking chicken and chopping vegetables at the same time instead of one after the other <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>. In a blockchain context, if two transactions are completely separate and do not interact with the same "state" (e.g., transferring Ether from person A to B, and person C to D), they can be executed concurrently <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>. This approach significantly speeds up transaction execution and leverages modern hardware with multiple cores <a class="yt-timestamp" data-t="00:56:45">[00:56:45]</a>, resulting in more transactions per second (TPS) <a class="yt-timestamp" data-t="00:56:50">[00:56:50]</a>.

This concept of a parallelized EVM gained significant excitement upon its announcement in November 2023 <a class="yt-timestamp" data-t="00:53:28">[00:53:28]</a>.

## Future Outlook

The trend in blockchain infrastructure is undeniably towards higher performance <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>, <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. As users desire cheap fees and fast infrastructure, the industry will inevitably move towards fast chains, such as those offering 10,000 transactions per second compared to 50 TPS <a class="yt-timestamp" data-t="01:14:15">[01:14:15]</a>. Projects unwilling to adapt to this demand for higher performance will likely see reduced traction and activity <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>.

While [[the_evolving_narrative_and_importance_of_ethereum | Ethereum]]'s Layer 1 may not handle future scaling needs <a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>, its strength lies in having the most Total Value Locked (TVL) and user base <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>. The future of [[the_role_of_layer_2_solutions_in_scaling_ethereum | Ethereum]]'s scalability is envisioned through a "rollup-centric roadmap," where activities occur on layers above Ethereum, using it for settlement and potentially data availability <a class="yt-timestamp" data-t="01:18:28">[01:18:28]</a>. This ensures value continues to accrue to the base layer <a class="yt-timestamp" data-t="01:18:40">[01:18:40]</a>.