---
title: The concept and importance of parallelization in blockchain technology
videoId: dUuF9eLoUQo
---

From: [[when-shift-happens]] <br/> 

Parallelization is a critical innovation addressing [[challenges_and_strategies_for_scaling_cryptocurrency_protocols | scalability challenges]] in blockchain technology, particularly for the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. It allows for more efficient processing of transactions, leading to higher performance and lower costs <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>.

## Understanding Parallelization

The core idea of parallelization in blockchains is to process multiple independent transactions simultaneously <a class="yt-timestamp" data-t="00:56:03">[00:56:03]</a>. Jay, co-founder and CEO at Say Labs (the company behind the Say Protocol), explains this with a cooking analogy:
> "If you have let's say that you're cooking something and there's three different things you want to cook... one way that you could do it is you could first get the vegetables ready... and then afterwards you start cooking the chicken... Now the other way that you could do it is you could put the chicken into the oven at the same time that you start cutting the vegetables and that way you're able to cut the vegetables while the chicken is cooking so that's the core idea around paralyzation which is that you can do two things at the same time" <a class="yt-timestamp" data-t="00:55:19">[00:55:19]</a>.

In a blockchain context, if two transactions are completely separate and do not involve overlapping states (e.g., me sending ether to you and Mike sending ether to Chia), they can be executed concurrently <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>. This significantly speeds up transaction execution and allows for processing more transactions per second by utilizing modern hardware with multiple cores <a class="yt-timestamp" data-t="00:56:37">[00:56:37]</a>.

## Issues with Traditional EVM and the Need for Parallelization

Around 80% to 90% of developers in crypto currently use the EVM <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. While the [[the_role_of_the_ethereum_virtual_machine_evm_in_blockchain_development | Ethereum Virtual Machine (EVM)]] was a groundbreaking innovation, being the first general-purpose virtual machine for blockchains <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, it was not built with performance in mind <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This fundamental limitation leads to issues like high transaction costs (e.g., $100 gas fees), making Ethereum inaccessible to ordinary users <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

The EVM's widespread adoption makes it incredibly difficult to move away from <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. This highlights the need to *scale* the EVM by improving its performance, rather than replacing it entirely <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Say Protocol and Parallelized EVM

Say Protocol, developed by Say Labs, is a Layer 1 blockchain that is the first parallelized EVM <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Say V1, launched in August 2023, was already the fastest chain in existence at the time, with 390-millisecond block times, making it roughly 10x faster than Solana and many other chains <a class="yt-timestamp" data-t="00:52:40">[00:52:40]</a>. However, it lacked developer activity due to not supporting the EVM <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

Recognizing the EVM's dominance, Say Labs developed Say V2 to be the first parallelized EVM, directly addressing the performance limitations of the EVM <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This innovation sparked significant excitement, creating a new "vertical" for parallelized EVMs in the blockchain space <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>.

## Industry Trends and Future Impact

The blockchain industry is rapidly moving towards higher-performance blockchains, with a significant focus on parallelization <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>. This trend is driven by the universal desire for cheap fees and fast infrastructure <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>.

Key implications of this trend include:
*   **Increased Performance**: Blockchains will offer significantly higher transactions per second (TPS), for example, moving from 50 TPS to 10,000 TPS <a class="yt-timestamp" data-t="01:34:16">[01:34:16]</a>.
*   **Adoption of Smaller Validator Sets**: While controversial, smaller validator sets can lead to better performance and more sustainable network operation by reducing redundancy and enabling higher hardware requirements for nodes <a class="yt-timestamp" data-t="01:32:48">[01:32:48]</a>.
*   **Shift Away from Legacy Systems**: Projects unwilling to adapt to higher-performance infrastructures, such as vanilla EVMs, may see decreased traction and relevance over time <a class="yt-timestamp" data-t="01:34:47">[01:34:47]</a>.

Ultimately, the drive for higher performance and efficiency through parallelization is expected to be a major force shaping the future of blockchain [[vision_and_innovation_in_blockchain_technology | technology]] in the coming years <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>.