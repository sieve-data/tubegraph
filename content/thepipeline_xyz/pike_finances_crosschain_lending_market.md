---
title: Pike Finances crosschain lending market
videoId: 7KlUOAaQglQ
---

From: [[thepipeline_xyz]] <br/> 

Pike Finance operates as a cross-chain lending market, allowing users to deposit assets on one blockchain ("chain A") and borrow against them on another ("chain B") <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The core aim of Pike is to unify liquidity across the entire [[decentralized_finance_and_personal_finance | DeFi]] ecosystem <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, embodying its tagline as a "universal liquidity protocol" <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Core Mechanism: Cross-Chain Messaging

A key distinction of Pike Finance is that it does not utilize bridges to facilitate cross-chain functionality <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Instead, it relies on cross-chain messaging <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This means that assets are not sent directly from one chain to another to enable a borrow <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. For example, if a user deposits assets on Optimism and borrows on Base, Pike sends a message from Optimism to Base confirming the deposit, which then allows the user to borrow a corresponding amount of native assets like USDC or ETH on Base <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This cross-chain lending is specifically facilitated by [[Pith Network and its role in decentralized finance | Wormhole]] messaging <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

Pike's avoidance of bridges stems from concerns about security <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Consequently, Pike only deals with native assets, not bridged assets <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

## Vision and User Experience

Beyond unifying liquidity, Pike Finance aims to simplify the user experience by eliminating the complex prefixes and suffixes often associated with derivative or receipt tokens (e.g., LP tokens) <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. This simplification is intended to make [[decentralized_finance_and_personal_finance | DeFi]] more accessible for a broader audience, including millions of future users who might find the current complexity overwhelming <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Supported Ecosystems

Pike Finance is working to unify liquidity across various ecosystems, including:
*   **EVM ecosystems**: Ethereum, Optimism, and soon Monad <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Non-EVM ecosystems**: Solana, IBC (Cosmos), and Move-powered chains like Aptos and Sui <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

Pike's mainnet launched with a capped supply, allowing stress testing of the system <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. Building on arbitrary message bridges (AMBs) is a new and challenging endeavor that requires ensuring performance and reliability <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. As of February 2024, Pike is deployed using a hub-and-spoke model, with spoke chains including Ethereum mainnet, Arbitrum, Optimism, and Base <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. Arbitrum has seen the most cross-chain messages, followed by Optimism and Base, which aligns with existing [[decentralized_finance_defi_advancements | DeFi]] activity <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This demonstrates liquidity flowing between various chains <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.