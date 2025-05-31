---
title: Challenges and strategies in launching and scaling a crypto startup
videoId: aW3KlttN814
---

From: [[when-shift-happens]] <br/> 

The crypto industry, while rapidly evolving, presents unique [[challenges_and_opportunities_in_crypto | challenges and opportunities in crypto]]. Launching and scaling a crypto startup like Monad requires a blend of technological innovation, strategic community building, and disciplined financial management <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Current Landscape and [[challenges_in_the_crypto_industry | Industry Challenges]]

The blockchain space, particularly on-chain operations, is currently "pretty inefficient" <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. This inefficiency manifests in:
*   **High Costs** Decentralized exchanges trading crypto assets are the least efficient, leading to higher costs for end-users compared to centralized crypto exchanges or traditional centralized markets <a class="yt-timestamp" data-t="09:50:52">[09:50:52]</a>. This stems from non-performant technology and higher transaction costs for market maker orders, which limit how frequently market makers can update quotes <a class="yt-timestamp" data-t="10:10:07">[10:10:07]</a>.
*   **Scaling Limitations** Existing EVM Layer 1 blockchains, including Ethereum, are "single-threaded," meaning transactions are processed sequentially <a class="yt-timestamp" data-t="16:35:50">[16:35:50]</a>. This severely limits throughput; for example, an app with a million daily active users and 50 transactions per user per day would generate 50 million transactions daily, equivalent to 500 transactions per second (TPS) <a class="yt-timestamp" data-t="15:14:02">[15:14:02]</a>. No current EVM Layer 1 can offer 500 TPS, meaning one such app would "more than saturate any EVM blockchain right now" <a class="yt-timestamp" data-t="15:25:01">[15:25:01]</a>.
*   **Technological Debt** Ethereum, despite feeling long-established in crypto years, only began seeing "huge amounts of usage" and "meaningful capital on chain" around DeFi Summer in 2020 <a class="yt-timestamp" data-t="17:02:18">[17:02:18]</a>. This meant the stakes only became high "a couple years ago" <a class="yt-timestamp" data-t="17:15:37">[17:15:37]</a>, leaving insufficient time for architectural performance improvements <a class="yt-timestamp" data-t="17:17:28">[17:17:28]</a>.

### Key Bottlenecks
One of the biggest performance bottlenecks identified when analyzing Ethereum transaction history is "state access" <a class="yt-timestamp" data-t="19:47:04">[19:47:04]</a>. Every transaction involves mutating state, whether account balances or smart contract data, which requires expensive access to data stored on a solid-state drive (SSD) <a class="yt-timestamp" data-t="20:05:07">[20:05:07]</a>.

## Strategies for [[challenges_and_strategies_for_scaling_cryptocurrency_protocols | Scaling Cryptocurrency Protocols]]

### Monad's Approach: Parallelism and EVM Compatibility
Monad, a parallel EVM Layer 1 blockchain, aims to solve scaling issues by offering "1000x the throughput of Ethereum" <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. It is designed to achieve "world scale" for decentralized applications <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

Monad's uniqueness lies in its introduction of parallelism to the EVM <a class="yt-timestamp" data-t="14:34:04">[14:34:04]</a>, along with other performance re-architectures <a class="yt-timestamp" data-t="14:44:04">[14:44:04]</a>. Parallelism allows computers to perform multiple operations simultaneously, similar to a modern browser running many tabs <a class="yt-timestamp" data-t="16:05:04">[16:05:04]</a>. This contrasts with Ethereum's single-threaded processing <a class="yt-timestamp" data-t="16:36:44">[16:36:44]</a>.

By addressing the state access bottleneck and other improvements, Monad aims for 10,000 TPS, equivalent to a billion transactions per day, enabling apps to scale to millions of users <a class="yt-timestamp" data-t="15:42:01">[15:42:01]</a>.

Unlike some projects that focused solely on rollups for scaling <a class="yt-timestamp" data-t="18:12:01">[18:12:01]</a>, Monad took an "orthogonal direction" by optimizing the execution stack through low-level systems engineering <a class="yt-timestamp" data-t="18:29:01">[18:29:01]</a>. Monad also chose to support Solidity and maintain EVM compatibility, recognizing the vast developer ecosystem, libraries, tooling, and cryptography research built around the EVM <a class="yt-timestamp" data-t="26:01:01">[26:01:01]</a>. This contrasts with Solana, which rebuilt everything from scratch, changing the language, which "might have been an overreaction" <a class="yt-timestamp" data-t="25:43:01">[25:43:01]</a>.

## Community Building as a Core Strategy

In crypto, the "only path to successful marketing" is community building <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a> <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. Monad's success, in part, comes from its incredibly strong community <a class="yt-timestamp" data-t="34:08:00">[34:08:00]</a>.

Key aspects of effective community building:
*   **Start Early:** It's "never too early to start building your community" <a class="yt-timestamp" data-t="35:48:01">[35:48:01]</a>. Monad started in November 2022, just before the FTX collapse, finding that a bear market helped attract "true to crypto" individuals <a class="yt-timestamp" data-t="36:04:01">[36:04:01]</a>.
*   **"Community is the Product":** Instead of waiting for a fully built product, Monad treated its community as the product from day one <a class="yt-timestamp" data-t="48:00:00">[48:00:00]</a>. This meant being intentional about making the community "addictive" and enjoyable, rather than just outsourcing moderation <a class="yt-timestamp" data-t="48:26:01">[48:26:01]</a>.
*   **Authenticity and Fun:** Monad's team is in touch with "the spirit of crypto Twitter" <a class="yt-timestamp" data-t="34:42:01">[34:42:01]</a>, not taking themselves too seriously and leaning into community-driven art, memes, and lore <a class="yt-timestamp" data-t="34:50:01">[34:50:01]</a>.
*   **Beyond Financial Motivation:** While some community members are financially driven, Monad focuses on fostering a fun environment where people make friends through shared experiences and lore, encouraging long-term engagement beyond just an airdrop <a class="yt-timestamp" data-t="41:49:01">[41:49:01]</a>.

## Financial Management and Funding Strategies

Monad raised $225 million <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, a significant sum. While some might see raising too much money as dangerous for a startup <a class="yt-timestamp" data-t="28:37:01">[28:37:01]</a>, Monad views it as a "hedge" and a way to provide ample resources for the ecosystem to succeed <a class="yt-timestamp" data-t="31:15:01">[31:15:01]</a>.

The strategy involves:
*   **Discipline:** Maintaining discipline in spending and focusing on activities with a positive Return on Investment (ROI) <a class="yt-timestamp" data-t="29:14:01">[29:14:01]</a>.
*   **Leveraging Privilege:** Acknowledging the industry's well-capitalized nature and making the most of the opportunity <a class="yt-timestamp" data-t="29:51:01">[29:51:01]</a>.
*   **In-house Operations:** Preferring to do things in-house rather than relying on third-party services for events or marketing, which instills valuable lessons <a class="yt-timestamp" data-t="30:29:01">[30:29:01]</a>.

## Leadership and [[longterm_strategies_and_philosophies_in_crypto_startups | Long-Term Philosophy]]

Effective leadership in a crypto startup is characterized by:
*   **Consistency:** Being "boringly consistent" <a class="yt-timestamp" data-t="52:53:01">[52:53:01]</a>, focusing on daily progress, and trusting the direction even if immediate massive success isn't apparent <a class="yt-timestamp" data-t="55:48:01">[55:48:01]</a>.
*   **Humility:** Avoiding hubris, especially given the discerning nature of the crypto community <a class="yt-timestamp" data-t="57:12:01">[57:12:01]</a>. Making big claims requires the ability to back them up <a class="yt-timestamp" data-t="58:01:01">[58:01:01]</a>.
*   **High Standards:** Setting a very high standard of excellence for the team and paying "attention to detail" without becoming "overly obsessed with the past" or past mistakes <a class="yt-timestamp" data-t="59:11:01">[59:11:01]</a>.
*   **Long-Term Vision:** Prioritizing long-term planning over short-term gains, despite market cycles and investor pressure <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>. A startup founder should be ready to commit for 10 years, which in crypto terms means building to last "multiple cycles" <a class="yt-timestamp" data-t="01:09:03">[01:09:03]</a>. The focus should be on picking "the right idea" that can raise money and prevail, rather than constantly pivoting to hot narratives <a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.
*   **Beyond the Playbook:** For a successful mainnet launch, it's crucial to go beyond "table stakes" features (like a great DEX, lending protocol, NFTs) <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. The goal is to offer "completely new" and unique experiences that drive users to engage <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>. This requires working with ambitious builders who have "out of the box ideas" <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.

Overall, success in the crypto startup landscape depends on solving fundamental technological [[challenges_and_risks_in_the_crypto_ecosystem | challenges and risks in the crypto ecosystem]], cultivating a vibrant community, managing resources wisely, and maintaining a consistent, long-term, and humble approach to leadership.