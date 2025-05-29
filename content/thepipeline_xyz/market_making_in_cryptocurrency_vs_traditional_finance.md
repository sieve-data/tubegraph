---
title: Market making in cryptocurrency vs traditional finance
videoId: DS796z6QLVI
---

From: [[thepipeline_xyz]] <br/> 

Market making, an essential function in financial markets, involves providing liquidity to exchanges by quoting both buy and sell prices for an asset. While its fundamental purpose remains the same, significant differences exist between market making in traditional finance (TradFi) and the cryptocurrency space <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Profit Models

The primary distinction lies in how market makers generate profit:

*   **Traditional Finance:** In TradFi, the main profit center for market-making firms is their actual profit and loss (P&L) from market activities. What they earn in the market is what they take home <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Cryptocurrency:** In crypto, this is often not the case <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Many crypto market makers run basic scripts to deploy liquidity, like Hummingbot <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   Their algorithms typically aim to break even <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
    *   The primary source of income for these firms is charging exchanges and protocols for access to their market-making services <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Exchanges may pay out millions per month in liquidity provider incentive programs, which often go to just a few large firms <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

This observation led to the founding of Elixir Protocol, which aims to decentralize and democratize market making <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## On-Chain vs. Off-Chain Order Books

The nature of the underlying infrastructure also introduces differences:

*   **Information Transparency:**
    *   On a centralized exchange (like Binance) and an on-chain Central Limit Order Book (CLOB) with APIs, market makers generally receive the same amount of information, such as the order book state, to place orders accordingly <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.
    *   A key difference in on-chain market making is the transparency of leverage. If market makers run with high leverage, and their liquidation levels are visible on-chain, this provides valuable information to other parties <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.
*   **Transaction Costs and Latency:**
    *   For on-chain CLOBs that rely on broadcasting transactions, issues like Miner Extractable Value (MEV) and block execution order become significant <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>.
    *   Updating orders on-chain can incur gas fees, even on Layer 2 solutions. If a market maker has to pay 20 cents per update for multiple orders across many pairs, it quickly becomes too expensive <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. This forces market makers to update less frequently, leading to wider spreads <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
    *   Every additional second of latency requires market makers to quote wider <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.
    *   Most large decentralized exchanges (DEXes) like dYdX, Vertex, and RabbitX utilize off-chain order books that settle on-chain to avoid high gas fees and latency for frequent order updates <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. This allows for faster updates (e.g., Elixir updates every 0.9 seconds gaslessly on integrated exchanges) <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>.
*   **Market Manipulation:**
    *   With fully on-chain order books, there's a risk of manipulation. For instance, parties could spam transactions to fill blocks, preventing liquidations from going through, which can negatively impact users with large positions <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>. This is less of a concern with off-chain matching and on-chain settlement <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.

## Automated Market Makers (AMMs) vs. Order Books

Traditional finance primarily uses order books. In crypto, Automated Market Makers (AMMs) emerged as a decentralized alternative for token swaps:

*   **AMMs:**
    *   Users deposit both sides of a pair into a liquidity pool <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   When trades occur against the pool, LPs collect fees <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
    *   However, LPs face [[challenges_and_strategies_in_crypto_investment | toxic flow]] or impermanent loss if the pool price deviates from the fair market price and gets arbitraged <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
    *   AMMs excel at bootstrapping liquidity for long-tail markets due to their passive liquidity provision model <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
    *   Newer AMM versions (e.g., Uniswap V3 and V4) are evolving to include features like concentrated liquidity and "hooks" that allow for limit order-like functionality, moving closer to an order book model <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **Order Books:**
    *   Offer significantly reduced slippage compared to AMMs, leading to more efficient trading for end-users <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   All major perpetual DEXes and centralized exchanges utilize order books for a reason: the ability to update orders at near-zero cost (off-chain), faster infrastructure via APIs, and better adaptability <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
    *   Market makers on order books can widen their spreads during high volatility to protect LPs from [[challenges_and_strategies_in_crypto_investment | toxic flow]], a mechanism akin to dynamic fees in AMMs <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

Elixir aims to bridge the gap by allowing passive liquidity provision to order books, similar to an AMM, while leveraging the efficiency of order book architecture <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The protocol algorithmically builds and deploys liquidity on order books, tightening bid-ask spreads and deepening liquidity <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## User Experience and Trust

Market making in crypto through decentralized protocols offers unique benefits for users:

*   **Custody:** Users retain custody of their assets at all times, unlike centralized exchanges where funds are held by the exchange <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>.
*   **Fairness:** Users know the exchange is not trading against them, addressing concerns like those highlighted by the FTX/Alameda situation, where an exchange with an integrated market maker could potentially manipulate prices or liquidate users for profit <a class="yt-timestamp" data-t="00:36:18">[00:36:18]</a>.
*   **Transparency:** The code of a decentralized exchange is public, making manipulative practices quickly identifiable <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>.
*   **Efficiency for End Users:** High-performance chains like Monad, supporting efficient CLOBs with high throughput and low gas fees, significantly improve the trading experience by minimizing slippage <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. This allows for features like one-click trading by issuing a signature for approvals, removing the need for repeated approvals for each trade <a class="yt-timestamp" data-t="00:37:59">[00:37:59]</a>.
*   **Building Trust:** Decentralized solutions contribute to [[building_trust_in_the_market_especially_in_crypto | building trust in the market]], particularly by ensuring transparency and reducing reliance on centralized intermediaries <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>.

Ultimately, market making in crypto is evolving rapidly, with protocols like Elixir aiming to [[challenges_and_opportunities_in_cryptocurrency_investment | decentralize and improve the efficiency]] of order book liquidity, making it more accessible and transparent for all participants <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.