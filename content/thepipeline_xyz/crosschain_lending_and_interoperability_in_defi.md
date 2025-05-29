---
title: Crosschain lending and interoperability in DeFi
videoId: 7KlUOAaQglQ
---

From: [[thepipeline_xyz]] <br/> 

Pike Finance is a decentralized finance (DeFi) protocol designed as a cross-chain lending market <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. Developed by the Nuts Finance team <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, Pike allows users to deposit assets on one blockchain (chain A) and borrow against them on a different blockchain (chain B) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Its core vision is to unify liquidity across the entire DeFi ecosystem, encompassing both EVM (Ethereum, Optimism, Base, Monad) and non-EVM (Solana, IBC/Cosmos, Move chains like Aptos and Sui, and Polkadot parachains) environments <a class="yt-timestamp" data-t="00:06:48">[00:07:07]</a>, embodying its tagline as a "Universal Liquidity Protocol" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Interoperability Approach

Unlike many cross-chain solutions, Pike Finance does not utilize traditional bridges to enable its functionality <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Instead, it relies on [[future of crosschain communication | cross-chain messaging]] (specifically, Wormhole messaging) <a class="yt-timestamp" data-t="00:07:36">[00:08:10]</a>. This means that when a user deposits assets on one chain (e.g., Optimism) and wishes to borrow on another (e.g., Base), the assets themselves are not sent between chains <a class="yt-timestamp" data-t="00:07:47">[00:07:51]</a>. A message is sent to confirm the deposit and authorize the borrow on the target chain <a class="yt-timestamp" data-t="00:07:51">[00:08:05]</a>.

This approach is driven by a strong focus on security and user experience:
*   **Avoiding Bridges** The team opts out of using bridges due to associated [[challenges_and_strategies_in_defi_product_development | security concerns]] <a class="yt-timestamp" data-t="00:08:17">[00:08:21]</a>.
*   **Native Assets Only** Pike exclusively deals with native assets, steering clear of wrapped or bridged assets <a class="yt-timestamp" data-t="00:08:25">[00:08:28]</a>. This simplifies the user experience by eliminating the need for complex token prefixes and suffixes (e.g., 'wETH', 'stETH'), which can be overwhelming for new users <a class="yt-timestamp" data-t="00:08:30">[00:09:07]</a>.

## Why Monad?

Pike Finance has made an early commitment to supporting Monad, largely due to its high performance and low transaction fees within an EVM environment <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This combines the benefits of a high-performance chain like Solana with the familiarity and existing liquidity of the EVM ecosystem <a class="yt-timestamp" data-t="00:13:43">[00:14:08]</a>. The ability to offer a smooth, fast, and cost-effective user experience while remaining EVM-compatible (requiring no new wallets or ecosystem familiarity) was a key factor in Pike's decision to support Monad <a class="yt-timestamp" data-t="00:14:05">[00:14:22]</a>.

## Mainnet Launch and Initial Metrics

Pike Finance officially went live on its mainnet on February 1st <a class="yt-timestamp" data-t="00:16:03">[00:16:07]</a>. The initial launch is capped, meaning there's a limit on supply per wallet, allowing the team to stress-test the system and ensure performance and reliability as the underlying arbitrary message bridges (AMBs) are still very new <a class="yt-timestamp" data-t="00:16:10">[00:16:53]</a>.

Key metrics since the launch:
*   Over 4,000 unique wallet accounts <a class="yt-timestamp" data-t="00:17:02">[00:17:07]</a>.
*   Pike operates on a hub-and-spoke model, with spokes on Ethereum mainnet, Arbitrum, Optimism, and Base <a class="yt-timestamp" data-t="00:17:49">[00:18:07]</a>.
*   Arbitrum has seen the most [[interoperability_and_blockchain_communication | cross-chain communication]], followed by Optimism and Base <a class="yt-timestamp" data-t="00:18:10">[00:18:21]</a>.
*   The launch demonstrates [[innovative_solutions_for_decentralized_finance_liquidity | liquidity flowing]] between different chains (e.g., Arbitrum to Optimism, Optimism to Base) <a class="yt-timestamp" data-t="00:19:00">[00:19:04]</a>, validating Pike's universal liquidity thesis <a class="yt-timestamp" data-t="00:18:42">[00:18:48]</a>.

## Roadmap and Future Use Cases

Pike Finance has a clear roadmap for future development:
*   **Uncapped Launch**: The immediate next milestone is to uncapped the mainnet, which is anticipated around March <a class="yt-timestamp" data-t="00:43:50">[00:44:06]</a>.
*   **New Asset Support**: The team plans to support new asset types like Liquid Staking Tokens (LSTs) and Liquid Restaking Tokens (LRTs) <a class="yt-timestamp" data-t="00:44:48">[00:45:07]</a>. This is partly enabled by Monad's high performance as a potential hub for connecting liquidity <a class="yt-timestamp" data-t="00:45:17">[00:45:31]</a>.
*   **Cross-chain Governance**: A longer-term goal is to implement cross-chain governance <a class="yt-timestamp" data-t="00:46:02">[00:46:09]</a>. As applications increasingly live across multiple chains, managing governance becomes complex. Pike aims to minimize the overhead for builders while maximizing participation across all deployed chains, fostering a "Melting Pot" concept for liquidity, community, and governance <a class="yt-timestamp" data-t="00:46:26">[00:47:40]</a>.

<br>

<div class="callout">
<div class="callout-emoji">💡</div>
<div class="callout-title">The Power of Community</div>
<div class="callout-content">
Pike Finance places significant emphasis on [[the_role_of_community_in_defi_project_success | community building]], drawing inspiration from projects like Monad. The team believes that a strong, organic community is crucial for long-term success <a class="yt-timestamp" data-t="00:29:39">[00:29:42]</a>. This involves:
<ul>
<li>**Meaningful Engagement**: Fostering genuine conversations instead of superficial interactions <a class="yt-timestamp" data-t="00:28:44">[00:29:17]</a>.</li>
<li>**Quality Over Quantity**: Prioritizing a smaller group of passionate members over large, inactive numbers <a class="yt-timestamp" data-t="00:30:32">[00:30:36]</a>.</li>
<li>**Community-Driven Content**: Encouraging members to create content (memes, art, music, NFTs) about the project, which organically maintains presence in users' minds without official "spamming" <a class="yt-timestamp" data-t="00:30:51">[00:32:57]</a>.</li>
</ul>
A notable example is the "Pikneans" NFT collection, which was entirely community-driven from its ideation to creation, with no team involvement except for amplification <a class="yt-timestamp" data-t="00:20:53">[00:21:16]</a>, <a class="yt-timestamp" data-t="00:21:40">[00:21:59]</a>. This initiative became a symbol of belonging and identity for the community members <a class="yt-timestamp" data-t="00:23:29">[00:23:51]</a>, showcasing the team's commitment to prioritizing [[challenges_and_strategies_in_improving_liquidity_in_defi | community safety]] and long-term vision over short-term vanity metrics <a class="yt-timestamp" data-t="00:30:25">[00:30:36]</a>, <a class="yt-timestamp" data-t="00:32:57">[00:33:02]</a>.
</div>
</div>