---
title: Integrations of Elixir with various exchanges
videoId: DS796z6QLVI
---

From: [[thepipeline_xyz]] <br/> 

[[elixir_protocol_and_its_founding | Elixir Protocol]] is a modular DPoS network designed to power order book liquidity, enabling anyone to supply liquidity to order books <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The protocol algorithmically builds and deploys this liquidity on order books, thereby tightening bid-ask spreads and deepening the overall liquidity for a given pair <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Its design is similar to Uniswap V2 in that it offers liquidity providers (LPs) a near-identical risk-return profile <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Addressing Market Making Challenges

Traditionally, market making in crypto has differed from traditional finance, where the P&L of market making firms is the main profit center <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. In crypto, these firms often run basic scripts and their primary profit center isn't the performance of their algorithms (which often break even), but rather the fees they charge exchanges and protocols for access to their market making services <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

Exchanges frequently spend over a million dollars per month on long-term liquidity provider incentive programs, with these funds often going to only a few large firms <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. [[elixir_protocol_and_its_founding | Elixir Protocol]] addresses this by providing a decentralized, trustless protocol that allows end-users to supply liquidity and earn a share of these incentives <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This approach aims to free the market for order book liquidity <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Key Integrations and Impact

[[role_of_decentralized_protocols_like_elixir | Elixir]] has secured native integrations with many large decentralized perpetual exchanges:
*   **Vertex** <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>
*   **dYdX** <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
*   **Rabbidex** <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
*   **Injective** <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>
*   **Bluefin** <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>
*   **Orderly** <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>
*   **Hyperliquid** <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>
*   **Aevo** <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>

These integrations allow the exchanges' end-users to supply liquidity to trading pairs in a trustless manner <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Impact on Vertex
[[role_of_decentralized_protocols_like_elixir | Elixir]] currently powers approximately 30% of the order book liquidity on Vertex <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This integration has led to a "massive increase" in the efficiency of the Vertex protocol, along with significant growth in traction and volume <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Upcoming Integrations and Future Goals
[[role_of_decentralized_protocols_like_elixir | Elixir]] plans to power:
*   More than half of the order book liquidity on Rabbidex <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   30% on Orderly <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   40% on Bluefin <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   Half of the order book liquidity on Hyperliquid <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   NFT perps with NFT Perps Turbine (Elixir's integration) are also launching <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>.

As [[role_of_decentralized_protocols_like_elixir | Elixir]] expands its integrations, it aims to emerge as a crucial underlying infrastructure that exchanges can rely on to bootstrap liquidity to their order books <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Integration Approach and Technology

[[role_of_decentralized_protocols_like_elixir | Elixir]] started by providing market making services to centralized exchanges but pivoted to decentralized exchanges (DEXs) after dYdX and other large exchanges expressed interest in allowing their users to access liquidity provider incentives <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

When an LP deposits into [[role_of_decentralized_protocols_like_elixir | Elixir]], the protocol transparently and trustlessly provisions that liquidity <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The protocol reaches consensus once per second, pulls the state of the order book, and its validators come to consensus before sending the signed data to the exchange via relay infrastructure <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The signing happens at the smart contract level, meaning [[role_of_decentralized_protocols_like_elixir | Elixir]] does not have access to the funds, which remain in a smart contract <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

[[role_of_decentralized_protocols_like_elixir | Elixir]] typically quotes four or five orders on each side of the order book, updating them once per second <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### White-Labeling and User Experience
To foster deeper integration and ownership by exchanges, [[role_of_decentralized_protocols_like_elixir | Elixir]] adopted a white-labeling strategy. For example, the integration with Vertex is branded as "Vertex Fusion," making it a key feature of the exchange rather than an external advertisement <a class="yt-timestamp" data-t="00:41:04">[00:41:04]</a>. This allows exchanges to offer liquidity provision as their own core feature, enabling users to supply liquidity and earn yield (e.g., 20-25% API on stables) <a class="yt-timestamp" data-t="00:41:13">[00:41:13]</a>. Rabbidex Fusion is set to launch next <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### On-Chain vs. Off-Chain Order Books
For optimal performance, [[role_of_decentralized_protocols_like_elixir | Elixir]] recommends that teams building central limit order books (CLOBs) build them off-chain with on-chain settlement, rather than fully on-chain <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>. This approach is adopted by major DEXs like dYdX, Vertex, Rabbidex, Aevo, and Hyperliquid <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

The main advantages of off-chain order books with on-chain settlement include:
*   **Speed and Cost**: It's much faster and cheaper to quote prices off-chain <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. High gas costs on fully on-chain CLOBs force market makers to update orders less frequently, leading to wider spreads <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
*   **Manipulation Prevention**: Fully on-chain order books are susceptible to manipulation, such as spamming transactions to prevent liquidations <a class="yt-timestamp" data-t="00:30:45">[00:30:45]</a>.
*   **Execution Quality**: Even on fast chains like Solana, fully on-chain order books tend to have wider spreads and less optimal execution compared to off-chain models <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.

[[role_of_decentralized_protocols_like_elixir | Elixir]] updates orders every 0.9 seconds in a gasless manner on integrated exchanges like Vertex Fusion, Rabbidex Fusion, Bluefin Nexus, Hyperliquid Aqua <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>.

### Mitigating Toxic Flow and Transparency
To protect LPs from "toxic flow" (where LPs lose money due to arbitrage), [[role_of_decentralized_protocols_like_elixir | Elixir]]'s algorithm adjusts bid-ask spreads <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. In times of higher volatility, the spreads widen to ensure LPs do not take on excessive toxic flow <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

While on-chain market making provides transparency, especially regarding leverage levels that could lead to liquidations <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>, [[role_of_decentralized_protocols_like_elixir | Elixir]] incorporates features to prevent manipulation. It utilizes provable randomness within its protocol, specifically a variable that fluctuates between 0 and 1 <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>. This variable, along with randomly not routing one out of every five orders to the exchange, makes it difficult for arbitrageurs to predict future order placements and trade against [[role_of_decentralized_protocols_like_elixir | Elixir]] profitably <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.