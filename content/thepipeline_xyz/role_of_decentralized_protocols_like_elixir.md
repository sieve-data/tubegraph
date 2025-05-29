---
title: Role of decentralized protocols like Elixir
videoId: DS796z6QLVI
---

From: [[thepipeline_xyz]] <br/> 

## Introduction
[[Elixir protocol and its founding | Elixir Protocol]], founded by Phillip, is a decentralized protocol aimed at revolutionizing liquidity provision for order book exchanges in the crypto space [00:00:08]. Recognized as one of the earliest builders within the [[Monad Labs and Ecosystem | Monad ecosystem]], Elixir addresses the inefficiencies and centralization prevalent in traditional market making [00:00:42].

## The Problem with Centralized Market Making
Before Elixir, the crypto market saw a concentration of market making services among a few centralized firms [00:01:39]. Blockchain startups and order-book-based exchanges constantly sought these same four or five names for market making services [00:01:27]. It was observed that in crypto, unlike traditional finance, the primary profit center for these market makers wasn't the PnL of their algorithms (which often just broke even), but rather the fees charged to exchanges and protocols for access to their services [00:02:26]. Exchanges were paying over a million dollars per month in liquidity provider incentives, which largely went to just a few large firms [00:03:41]. This bottleneck highlighted a need for a decentralized, trustless solution [00:02:47].

## How Elixir Works
Elixir is building a modular DPOS (Delegated Proof of Stake) Network designed to power order book liquidity [00:02:52].
*   **Accessibility:** It enables anyone to supply liquidity to order books [00:02:57].
*   **Algorithmic Liquidity:** The protocol algorithmically builds and deploys the supplied liquidity on order books, thereby tightening bid-ask spreads and deepening liquidity [00:03:01].
*   **Uniswap V2 Equivalent:** Elixir functions similarly to a Uniswap V2 equivalent for order books, offering liquidity providers (LPs) a near-identical risk-return profile [00:03:10]. This design choice aims to simplify market making, which is generally a complex field, for the average user [00:03:29].
*   **Trustless Operation:** The protocol comes to consensus once per second, with fraud proofs posted on Ethereum mainnet [00:06:58]. The liquidity provision is fully trustless, as the signing happens at the smart contract level, meaning Elixir's team doesn't have access to user funds [00:07:28].
*   **Exchange Integration:** Exchanges can integrate Elixir's protocol to allow their end-users to supply liquidity to their order books and earn a share of existing liquidity incentives [00:03:48]. This effectively "frees" the market for order book liquidity [00:03:59].

## Impact and Integrations
Elixir has demonstrated significant impact:
*   **Increased Efficiency:** After integrating with Elixir, platforms like Vertex saw a "massive increase" in protocol efficiency, traction, and volume [00:05:30].
*   **Extensive Integrations:** Elixir has secured native integrations with major decentralized exchanges including Vertex (via Vertex Fusion), dydx (Rabidex Fusion), Injective, Bluefin, Orderly, Hyperliquid, and Avo [00:04:02].
*   **Significant Market Share:** Elixir powers approximately 30% of the order book liquidity on Vertex [00:04:30], and is projected to power over half of the liquidity on Rabidex, 30-40% on Bluefin and Orderly, and half on Hyperliquid as rollouts continue [00:04:46]. This positions Elixir as crucial underlying infrastructure for bootstrapping liquidity [00:05:04].

## Comparison with AMMs and Centralized Market Making
Elixir facilitates the transition from Automated Market Makers (AMMs) to more efficient Central Limit Order Books (CLOBs) [00:11:03].
*   **Addressing Slippage:** While AMMs revolutionized token swapping in a decentralized way, CLOBs offer significantly reduced slippage for end-users [00:09:50].
*   **Passive Liquidity Provision:** AMMs' "secret weapon" is the ability for people to passively supply liquidity, making it easy to bootstrap liquidity for long-tail markets [00:12:05]. Elixir aims to bring this passive liquidity provision to order books [00:12:05].
*   **Market Dynamics:** Elixir accounts for "toxic flow" (impermanent loss) by dynamically widening spreads during volatility, similar to how AMMs adjust fees for riskier pairs [00:17:20].
*   **On-Chain vs. Off-Chain:** While fully on-chain CLOBs face challenges like high gas costs and slower updates, Elixir generally recommends off-chain order books that settle on-chain [00:25:21]. This approach is used by most large decentralized exchanges (e.g., dydx, Vertex, Rabidex) to ensure faster, cheaper order updates and prevent manipulation via transaction spamming [00:25:27]. [[Monad Labs and Ecosystem | Monad's]] high throughput and low gas fees would make on-chain market making more profitable, leading to tighter spreads [00:32:14].

## User Experience of On-Chain CLOBs
For new crypto users, the benefits of using an on-chain CLOB powered by protocols like Elixir include:
*   **Custody:** Users retain custody of their assets at all times, eliminating the need to trust a centralized exchange with funds [00:35:42].
*   **Transparency & Fairness:** The exchange cannot trade against its users, and potential manipulations, like those seen with FTX and Alameda, are quickly revealed due to on-chain transparency [00:36:18].
*   **Deeper Liquidity:** Protocols like Elixir bring deeper liquidity to decentralized exchanges [00:36:24].
*   **Seamless Trading:** On-chain CLOBs on platforms like [[Monad Labs and Ecosystem | Monad]] can enable one-click trading by allowing users to issue a signature for approvals, streamlining the buy/sell process [00:37:57].

## Synergy with Monad
Elixir's early commitment to [[Monad Labs and Ecosystem | Monad]] stems from several factors:
*   **Technical Alignment:** [[Monad Labs and Ecosystem | Monad's]] strong technology, including increased throughput and native EVM (Ethereum Virtual Machine) support, is a major differentiator [00:19:38].
*   **EVM Compatibility:** The EVM compatibility simplifies development for Elixir, as it avoids the burden of rebuilding their entire stack and smart contracts in different languages (e.g., CosmWasm Rust) and undergoing new audits [00:19:52]. This reduces the cold start problem for new ecosystems [00:21:18].
*   **Community:** [[Monad Labs and Ecosystem | Monad]] has a strong and supportive community, which has significantly benefited Elixir [00:21:35].
*   **Shared Vision:** Both Elixir and [[Monad Labs and Ecosystem | Monad]] share a vision for an efficient trading atmosphere powered by central limit order books, aiming to provide a superior user experience in DeFi within an EVM environment [00:10:03].

## Challenges and Future Plans
Elixir has faced typical challenges of a startup in the crypto space:
*   **Hiring:** Attracting top-tier talent, especially Solidity engineers, is crucial for building new primitives [00:39:44].
*   **Product Framing:** Initially, conveying Elixir's complex function as a modular DPOS Network that integrates with exchanges was challenging [00:40:18]. The adoption of white-label products like "Vertex Fusion" helped simplify this, allowing exchanges to frame Elixir's offering as their own core feature for users [00:40:40].
*   **Regulation:** Operating with a US presence in New York City necessitates significant investment in ensuring regulatory compliance [00:42:57].
*   **Community Growth:** While Elixir initially focused on B2B2C (business-to-business-to-consumer) by integrating with exchanges, building a direct community and public perception is an ongoing focus [00:45:59]. Elixir's community is considered its biggest asset [00:45:44].
*   **Future Initiatives:** Elixir plans to launch the "Elixir Apothecary" soon [00:43:12], and aims for a mainnet launch in June/July, which will enable a fully decentralized network with validators [00:46:52]. Currently, the foundation runs validators as a trusted version for existing implementations [00:47:12]. At present, Elixir's testnet already has over 13,000 validators [00:47:05].

## Final Alpha
Phillip's advice for those building in the crypto space is to "take on early stage risk" and be "ruthless in your pursuit" of a big idea [00:49:06]. Despite facing naysayers, putting your head down and not giving up will bring your vision to life [00:49:51]. This mindset is crucial for pushing the space forward with new and efficient products [00:50:18].