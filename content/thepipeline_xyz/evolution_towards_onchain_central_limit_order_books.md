---
title: Evolution towards onchain central limit order books
videoId: DS796z6QLVI
---

From: [[thepipeline_xyz]] <br/> 

The cryptocurrency market has seen a significant shift from traditional automated market makers (AMMs) to more efficient central limit order books (CLOBs) [00:10:45]. This evolution aims to provide a better user experience by drastically decreasing slippage and transaction costs [00:09:55]. Elixir Protocol, founded by Phillip, is a key player in this transition, working closely with chains like [[discussion_on_high_throughput_blockchains | Monad]] to enable decentralized and efficient market making [00:11:10].

## The Role of Elixir Protocol

Elixir Protocol emerged from the observation that many blockchain startups and orderbook-based exchanges relied on a few centralized market-making firms [00:01:27]. Unlike traditional finance where market makers profit from their algorithms, in crypto, these firms often break even on their trading and generate revenue by charging exchanges for access to their services [00:02:28].

Elixir's mission is to decentralize and democratize market making. It operates as a modular DPOS Network, enabling anyone to supply liquidity to order books [00:02:52]. The protocol then algorithmically builds and deploys this liquidity, which helps to tighten bid-ask spreads and deepen liquidity on exchanges [00:03:01]. This model is designed to be similar to Uniswap V2 in terms of risk-return profile for liquidity providers (LPs), making market making accessible without requiring complex strategies [00:03:10].

Major decentralized exchanges (DEXs) like Vertex (via Vertex Fusion), Rabbid X Fusion, Injective, Blue Fin, Orderly, Hyper Liquid, and Avo are natively integrating Elixir into their infrastructure [00:04:02]. Elixir currently powers approximately 30% of Vertex's order book liquidity and aims to significantly increase its presence across other major platforms [00:04:30]. This integration allows end-users to supply liquidity to order books in a trustless manner and earn a share of liquidity provider incentives that exchanges are already paying out [00:03:48].

### AMM vs. CLOB and Elixir's Contribution

While AMMs, like Uniswap, revolutionized token swaps by offering a decentralized trading method, they are not without their limitations, such as slippage [00:09:40]. Order books, conversely, offer the potential for much greater efficiency [00:09:50]. The industry has seen AMMs, like Uniswap V3 and V4, evolve to incorporate features that resemble order books, such as concentrated liquidity bands and hooks for limit orders [00:11:40].

The primary advantage of AMMs traditionally has been their ability to passively bootstrap liquidity, especially for long-tail markets [00:12:05]. However, order books have "reigned supreme" for large perpetual DEXs and centralized exchanges due to their ability to update orders near-zero cost via APIs, allowing for faster infrastructure and adaptation to market changes [00:12:46].

Elixir bridges the gap by enabling passive liquidity provision for order books, a feature traditionally unique to AMMs [00:12:05]. It essentially helps facilitate the transition from AMMs to efficient, decentralized CLOBs by allowing anyone to participate in market making, rather than just a few large firms [00:11:03].

### Addressing Liquidity Issues in DeFi

A significant challenge in DeFi has been the lack of sufficient liquidity [00:14:10]. For LPs, supplying liquidity is a profit-driven endeavor, often subsidized by exchanges through rebates or incentives [00:14:40]. A major detractor for LPs is "toxic flow" or impermanent loss, where passive LPs can lose money due to arbitrage opportunities exploited by others [00:15:11].

To mitigate toxic flow, AMMs have implemented dynamic fee mechanisms, charging higher fees for more volatile or "toxic" pairs [00:15:50]. The equivalent for order books is the bid-ask spread [00:17:13]. Elixir's algorithm automatically adjusts spreads based on volatility, quoting wider during high-volatility periods to protect LPs from toxic flow [00:17:24]. This ensures that each dollar of rewards paid out by an exchange brings in more liquidity, as the venue becomes more profitable for LPs [00:18:12].

## Onchain Central Limit Order Books: Benefits and Challenges

### Benefits for Users

For users, the primary advantages of an onchain CLOB include:
*   **Custody**: Users maintain custody of their assets at all times, eliminating counterparty risk associated with centralized exchanges [00:35:42].
*   **Transparency**: The exchange cannot trade against its users, as the code is visible and malicious activities would be quickly revealed [00:36:18].
*   **Deeper Liquidity**: Protocols like Elixir contribute to deeper liquidity by enabling broader participation in market making [00:36:24].
*   **Improved User Experience**: Onchain CLOBs, especially on high-throughput chains like [[discussion_on_high_throughput_blockchains | Monad]], can offer one-click trading, reduced gas fees, and lower slippage, making trading much more efficient and user-friendly [00:09:50].

### Technical Considerations and Challenges

The choice between a fully onchain CLOB and an offchain CLOB that settles onchain presents trade-offs:
*   **Speed and Cost**: The main advantage of an offchain order book settling onchain is faster and cheaper price quoting [00:30:05]. A fully onchain CLOB incurs gas fees for every order update, which can make frequent updates prohibitively expensive, leading to wider spreads [00:25:51]. For example, even on fast chains like Solana, fully onchain order books tend to have wider spreads and less optimal execution [00:27:00].
*   **Market Manipulation**: Fully onchain order books can be vulnerable to manipulation, where parties might spam transactions to prevent liquidations or exploit other users' positions [00:30:26].
*   **MEV (Maximal Extractable Value)**: Broadcasting transactions onchain exposes orders to MEV, which can affect the execution of trades and impact market makers' profitability [00:25:05].

Most large DEXs, including dYdX, Vertex, Rabbid X, Avo, and Hyperliquid, utilize offchain matching engines that settle onchain to overcome these challenges [00:25:27]. This allows them to avoid gas fees for order updates and maintain tight spreads, as Elixir, for example, can update orders every 0.9 seconds gaslessly [00:32:57].

### [[growth_and_scalability_challenges_in_blockchain_ecosystems | Challenges and Advancements in High-Frequency Trading and Blockchain]]

While onchain CLOBs offer benefits, they face challenges in high-frequency trading (HFT) environments. Market making is competitive, and transparency onchain means all order information is public [00:22:38]. This can potentially expose strategies, such as leverage levels that could lead to liquidation [00:24:02]. Elixir addresses this by incorporating provable randomness within its protocol, making it harder to predict future order placements and deterring arbitrageurs by randomly not broadcasting some orders [00:28:21].

## Monad's Role in the Evolution

[[discussion_on_high_throughput_blockchains | Monad]] aims to support an efficient central limit order book environment through its extremely high throughput and low gas fees [00:10:03]. This capability is crucial for enhancing the trading experience, allowing for much more efficient execution with significantly reduced slippage and gas costs compared to traditional AMMs on other chains [00:10:27].

The native EVM compatibility of [[discussion_on_high_throughput_blockchains | Monad]] is a significant differentiator. Projects like Elixir have already built out their stack, including smart contracts and APIs, in the EVM environment [00:19:52]. Rebuilding this infrastructure for non-EVM compatible chains (e.g., in CosmWasm or Rust) presents a substantial barrier in terms of cost, time, and audit requirements [00:20:11]. [[discussion_on_high_throughput_blockchains | Monad]] removes this burden, making it an attractive platform for established projects and fostering ecosystem growth [00:21:29]. The synergy between [[discussion_on_high_throughput_blockchains | Monad]]'s technical capabilities and Elixir's liquidity solutions is seen as critical for establishing [[discussion_on_high_throughput_blockchains | Monad]]'s prevalence in the Web3 space, particularly for facilitating decentralized, onchain trading [00:13:35].

## Building in the Crypto Space: Challenges and Community

Founding a project like Elixir comes with unique [[growth_and_scalability_challenges_in_blockchain_ecosystems | challenges and advancements in high-frequency trading and blockchain]] [00:39:08]. Key challenges include hiring top-tier talent, defining the project's novel primitive for market understanding, and navigating complex regulatory landscapes, especially for US-based entities [00:39:40]. Elixir has overcome branding challenges by developing white-label products like "Vertex Fusion," allowing exchanges to integrate Elixir's liquidity as their core feature without overtly branding it as an Elixir product [00:40:40].

Community is a vital asset for any crypto project [00:44:54]. While many of Elixir's liquidity providers on platforms like Vertex may not initially realize they are interacting with Elixir, the protocol is gaining momentum through public perception and upcoming initiatives like the "Elixir Apothecary" [00:46:15]. Elixir's testnet already has over 13,000 validators [00:47:03], with a mainnet launch planned for June-July, aiming for a fully decentralized network of validators [00:46:52].

A key piece of advice for builders in the crypto space is to "take on early stage risk" and be "ruthless in your pursuit" of a big idea, even when faced with naysayers [00:49:06]. This commitment and perseverance are crucial for pushing the space forward and bringing innovative products to life [00:50:18].