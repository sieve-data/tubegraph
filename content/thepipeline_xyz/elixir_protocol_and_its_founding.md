---
title: Elixir protocol and its founding
videoId: DS796z6QLVI
---

From: [[thepipeline_xyz]] <br/> 

Elixir Protocol is a modular Delegated Proof-of-Stake (DPoS) network designed to power order book liquidity for decentralized exchanges (DEXs) <a class="yt-timestamp" data-t="02:52:43">[02:52:43]</a>. It allows anyone to supply liquidity to order books, which the protocol then algorithmically builds and deploys to tighten bid-ask spreads and deepen liquidity <a class="yt-timestamp" data-t="02:57:02">[02:57:02]</a>.

## Founding Story

Phillip, the founder of Elixir Protocol, began his journey in crypto in 2016 when he started the Carnegie Mellon Blockchain Group, serving as its president until graduation <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. He then ran a company called Block Venture for about two to three years <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

During his time at Block Venture, Phillip observed a significant gap in the market: every blockchain startup he encountered needed a market maker for their centralized exchange pairs <a class="yt-timestamp" data-t="01:27:07">[01:27:07]</a>. Similarly, order-book based decentralized exchanges and concentrated liquidity AMMs (Automated Market Makers) were relying on a few centralized firms for market-making services <a class="yt-timestamp" data-t="01:34:06">[01:34:06]</a>.

Phillip realized that market making in crypto fundamentally differed from traditional finance. In crypto, the actual profit center for these firms wasn't the performance of their trading algorithms, which often just broke even, but rather the fees they charged exchanges and protocols for access to their services <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>. This observation led him to question why a decentralized, trustless protocol couldn't perform the same function <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. This insight became the inspiration for Elixir Protocol <a class="yt-timestamp" data-t="02:51:08">[02:51:08]</a>.

## Elixir Protocol Explained

Elixir functions by allowing liquidity providers (LPs) to supply assets to a pair, similar to an AMM <a class="yt-timestamp" data-t="06:48:06">[06:48:06]</a>. The protocol then provisions that liquidity on the back end <a class="yt-timestamp" data-t="06:54:02">[06:54:02]</a>. Elixir's validators come to consensus once a second, pull the state of the order book, and send it to relay infrastructure for signing and transmission to the exchange <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. This process is fully trustless; the funds sit in a smart contract, and signatures are issued based on those held funds, meaning Elixir doesn't have access to the user's funds <a class="yt-timestamp" data-t="07:28:03">[07:28:03]</a>.

The protocol aims to be the trustless way for an order book to bootstrap liquidity, a capability that previously didn't exist <a class="yt-timestamp" data-t="07:54:08">[07:54:08]</a>. It quotes four or five orders on each side of the book, updating them once per second <a class="yt-timestamp" data-t="08:24:08">[08:24:08]</a>. LPs receive a reward APR, similar to providing liquidity to Uniswap, where the goal isn't proprietary strategies but rather earning incentives for enabling market access <a class="yt-timestamp" data-t="08:33:04">[08:33:04]</a>.

Elixir's approach means that while an LP's principal might fluctuate slightly, the main draw is the high APR earned from providing liquidity to these markets, which would otherwise be exclusive to large market-making firms <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.

## Impact and Integrations

Elixir has seen significant success, with its impact on platforms like Vertex being evident in increased traction and volume post-integration <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. The protocol facilitates native integrations with various exchanges, allowing their end-users to supply liquidity and earn a share of existing liquidity provider incentives <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

Current and planned integrations include:
*   Vertex (via Vertex Fusion, powering roughly 30% of order book liquidity) <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>
*   dYdX <a class="yt-timestamp" data-t="04:07:05">[04:07:05]</a>
*   RabidX (via RabidX Fusion, launching soon) <a class="yt-timestamp" data-t="04:08:08">[04:08:08]</a>
*   Injective <a class="yt-timestamp" data-t="04:12:08">[04:12:08]</a>
*   Bluefin <a class="yt-timestamp" data-t="04:12:08">[04:12:08]</a>
*   Orderly <a class="yt-timestamp" data-t="04:12:08">[04:12:08]</a>
*   Hyperliquid <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>
*   Aevo <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>

Elixir is positioned to become crucial underlying infrastructure for exchanges to bootstrap liquidity <a class="yt-timestamp" data-t="05:04:07">[05:04:07]</a>.

### Comparison to AMMs and Order Books

Elixir facilitates the transition from AMMs to efficient Central Limit Order Books (CLOBs) by decentralizing market making, allowing anyone to participate <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>. While AMMs made token swaps decentralized and easy for long-tail markets <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>, order books have reigned supreme for larger exchanges due to near-zero cost order updates and faster infrastructure <a class="yt-timestamp" data-t="12:49:00">[12:49:00]</a>. Elixir essentially brings the passive liquidity provision benefit of AMMs to order books <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.

AMMs like Uniswap are evolving towards order book models (e.g., V3 with concentrated liquidity, V4 with hooks for limit orders) <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>. The main issue with liquidity in DeFi is "toxic flow" (impermanent loss) for passive LPs <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>. Elixir, like traditional market makers, quotes wider spreads during high volatility to protect LPs from toxic flow <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>.

## Technical Details

### On-chain vs. Off-chain Market Making
When considering on-chain market making, a key distinction arises between fully on-chain CLOBs and off-chain CLOBs that settle on-chain <a class="yt-timestamp" data-t="29:38:00">[29:38:00]</a>. Elixir recommends the latter for several reasons:
*   **Speed and Cost**: It's much faster and cheaper to quote prices off-chain <a class="yt-timestamp" data-t="30:01:00">[30:01:00]</a>. Users generally don't want to pay gas to update orders <a class="yt-timestamp" data-t="25:47:00">[25:47:00]</a>. If market makers have to pay gas, they update less frequently, leading to wider spreads and worse execution <a class="yt-timestamp" data-t="25:53:00">[25:53:00]</a>.
*   **Manipulation Prevention**: Fully on-chain order books are susceptible to manipulation, such as spamming transactions to prevent liquidations <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.

Many large DEXs, like dydx, Vertex, RabidX, Aevo, and Hyperliquid, use off-chain modules that settle on-chain for these reasons <a class="yt-timestamp" data-t="25:27:00">[25:27:00]</a>. Elixir updates every 0.9 seconds gaslessly for many integrations <a class="yt-timestamp" data-t="32:57:00">[32:57:00]</a>. For fully on-chain exchanges, like NFT Perpetual, Elixir adapts by updating less frequently (e.g., only when there's a trade) and quoting wider spreads <a class="yt-timestamp" data-t="33:16:00">[33:16:00]</a>.

### Transparency and Randomness
While the transparency of order books (where orders sit) is similar on centralized and decentralized exchanges, on-chain market making can reveal additional information like leverage levels, which could lead to liquidation targeting <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.

To mitigate gaming and predictability, Elixir incorporates provable randomness within its protocol <a class="yt-timestamp" data-t="28:21:00">[28:21:00]</a>. A variable, inspired by Von Neumann, fluctuates between 0 and 1:
*   When at 1, the algorithm tries to keep books at 50/50 <a class="yt-timestamp" data-t="28:42:00">[28:42:00]</a>.
*   When at 0, it optimizes for P&L <a class="yt-timestamp" data-t="28:47:00">[28:47:00]</a>.
This random lock in Elixir's enclaves allows verification of honest protocol action retrospectively but prevents prediction of future orders <a class="yt-timestamp" data-t="28:57:00">[28:57:00]</a>. Additionally, one out of every five orders randomly won't make it to the exchange, making it economically negative for arbitrageurs to try and game Elixir's positions <a class="yt-timestamp" data-t="29:16:00">[29:16:00]</a>.

## User Experience Benefits of On-chain CLOBs

For typical users, the main benefits of an on-chain CLOB (especially when supported by infrastructure like Elixir and chains like [[Monad Labs and Ecosystem | Monad]], which enables high throughput and low gas fees <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>) include:
*   **Custody**: Users always custody their assets, removing the counterparty risk associated with centralized exchanges <a class="yt-timestamp" data-t="35:42:00">[35:42:00]</a>.
*   **No Trading Against Users**: The exchange cannot trade against its users, as all activity is transparent and verifiable on-chain <a class="yt-timestamp" data-t="36:18:00">[36:18:00]</a>.
*   **Deeper Liquidity**: Protocols like Elixir bring deeper, trustless liquidity to order books <a class="yt-timestamp" data-t="36:24:00">[36:24:00]</a>.
*   **Improved Efficiency**: Orders can be updated quickly and cheaply, leading to tighter spreads and less slippage <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.
*   **Seamless Trading**: Users can trade directly from their self-custody wallets (e.g., MetaMask, Ledger) without needing to deposit funds to an exchange, and features like one-click trading reduce the need for constant approvals <a class="yt-timestamp" data-t="37:57:00">[37:57:57]</a>.

## Challenges Faced

Elixir has faced several challenges common to projects building new primitives in crypto:
*   **Hiring**: Securing top-tier talent, especially Solidity engineers, is crucial but can be costly, often initially requiring headhunters <a class="yt-timestamp" data-t="39:44:00">[39:44:00]</a>.
*   **Defining the Product**: Initially, it was challenging to communicate Elixir's unique nature as a modular DPoS network that could be white-label integrated by exchanges <a class="yt-timestamp" data-t="40:18:00">[40:18:00]</a>. This was addressed by creating branded integrations like "Vertex Fusion," allowing exchanges to present it as their own core feature <a class="yt-timestamp" data-t="41:04:00">[41:04:00]</a>.
*   **Regulation**: As a U.S.-based team, navigating the regulatory landscape and ensuring compliance is a significant ongoing concern and expenditure <a class="yt-timestamp" data-t="42:57:00">[42:57:00]</a>.

## Community Importance

Elixir recognizes its community as its biggest asset <a class="yt-timestamp" data-t="45:44:00">[45:44:00]</a>. While early focus was B2B2C, providing infrastructure for exchanges to push to their users, the growing public perception of Elixir is crucial <a class="yt-timestamp" data-t="45:57:00">[45:57:00]</a>. Many users interacting with Elixir via exchange interfaces might not initially know it's Elixir, but gaining broader momentum is vital for future growth and for attracting new exchanges <a class="yt-timestamp" data-t="46:15:00">[46:15:00]</a>.

The upcoming "Elixir Apothecary" and partnerships with influential figures like Arthur Hayes are set to increase public engagement, leading up to a mainnet launch around June-July <a class="yt-timestamp" data-t="46:39:00">[46:39:00]</a>. This will enable a truly decentralized network with a large set of validators, moving beyond the current trusted version run by the foundation <a class="yt-timestamp" data-t="46:58:00">[46:58:00]</a>.

### [[Understanding Monad and its community | Synergy with Monad]]
There's significant synergy between the [[Monad Labs and Ecosystem | Monad community]] and The Elixir Community <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. Elixir was among the earliest builders within the [[Monad Labs and Ecosystem | Monad ecosystem]] <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Key reasons for this early excitement and commitment include:
*   **Strong Technology**: [[Overview of Monad Database vs Standard Databases for EVM | Monad's]] increased throughput <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **Native EVM Support**: This is a major differentiator, as Elixir has already built out its stack with EVM compatibility. Rebuilding for non-EVM chains (like Rust or CosmWasm) would be a huge burden, including additional audits and API wiring <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   **Community**: [[History of the Monad Community | Monad's]] community is noted for its engagement <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
*   **Trusted Actors**: The [[Monad Labs and Ecosystem | Monad]] team consists of trusted actors <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

[[Monad Labs and Ecosystem | Monad's]] core value proposition of an efficient trading atmosphere powered by a central limit order book, with extremely high throughput and low gas, aligns perfectly with Elixir's goal of decentralizing and improving order book liquidity <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.

## Final Alpha

Phillip advises those planning to build in the crypto space to "take on early stage risk and like... just own it and then just kind of be ruthless in your pursuit of it" <a class="yt-timestamp" data-t="49:06:00">[49:06:00]</a>. He emphasizes not giving up despite potential naysayers, as perseverance is key to bringing big ideas to life <a class="yt-timestamp" data-t="49:31:00">[49:31:00]</a>.