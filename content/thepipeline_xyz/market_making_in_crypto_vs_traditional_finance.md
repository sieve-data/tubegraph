---
title: Market making in crypto vs traditional finance
videoId: DS796z6QLVI
---

From: [[thepipeline_xyz]] <br/> 

Market making in the crypto space operates fundamentally differently from its counterpart in traditional finance (TradFi) <a class="yt-timestamp" data-t="00:02:06">00:02:06</a>. While both aim to provide liquidity and facilitate trading, the underlying profit mechanisms, operational transparency, and technological considerations diverge significantly.

## Profit Centers and Strategies

In **traditional finance**, the primary profit center for market-making firms lies directly in the profit and loss (P&L) derived from their trading activities in the market <a class="yt-timestamp" data-t="00:02:08">00:02:08</a>. What they earn from market movements and spreads is what they take home <a class="yt-timestamp" data-t="00:02:14">00:02:14</a>.

In **crypto**, this is often not the case <a class="yt-timestamp" data-t="00:02:16">00:02:16</a>. Many crypto market makers engage in very basic operations, sometimes just running simple scripts to deploy liquidity on order books <a class="yt-timestamp" data-t="00:02:22">00:02:22</a>. Their actual profit center does not typically come from the performance of their trading algorithms, which often break even <a class="yt-timestamp" data-t="00:02:28">00:02:28</a>. Instead, they earn money by charging exchanges and protocols for access to their market-making services <a class="yt-timestamp" data-t="00:02:35">00:02:35</a>.

This difference in profit motivation led to the inspiration behind projects like Elixir, which aims to demonstrate that a decentralized, trustless protocol could perform the same market-making function <a class="yt-timestamp" data-t="00:02:46">00:02:46</a>. Elixir builds a modular DPOS Network to power order book liquidity, allowing anyone to supply liquidity to order books <a class="yt-timestamp" data-t="00:02:52">00:02:52</a>. The protocol algorithmically deploys this liquidity to tighten bid-ask spreads and deepen order book liquidity <a class="yt-timestamp" data-t="00:03:00">00:03:00</a>. Liquidity providers (LPs) on Elixir experience a risk-return profile nearly identical to those on Uniswap V2, by design, as the goal is to simplify the complex space of market making for users <a class="yt-timestamp" data-t="00:03:10">00:03:10</a>.

## Transparency and Infrastructure

Market making on-chain introduces unique transparency considerations compared to centralized exchanges. On both a decentralized order book and a centralized exchange's order book, users can see where orders are placed and query the state of the order book to place their own orders accordingly <a class="yt-timestamp" data-t="00:23:37">00:23:37</a>.

However, additional transparency on-chain can reveal information like a market maker's leverage, which could expose their liquidation levels and be valuable information for other traders <a class="yt-timestamp" data-t="00:24:04">00:24:04</a>.

When considering an on-chain Central Limit Order Book (CLOB), there are key differences:
*   **Off-chain CLOBs settling on-chain:** Most large decentralized exchanges (DEXs) like dYdX, Vertex, RabbitX, Hyperliquid, and Aevo utilize off-chain modules that settle transactions on-chain <a class="yt-timestamp" data-t="00:25:27">00:25:27</a>. This approach is recommended because it avoids high gas fees for updating orders, which would force market makers to update less frequently and quote wider spreads <a class="yt-timestamp" data-t="00:25:45">00:25:45</a>. It also mitigates manipulation attempts, such as spamming transactions to prevent liquidations <a class="yt-timestamp" data-t="00:30:26">00:30:26</a>. These off-chain models offer faster, cheaper order updates and allow for gasless operations for LPs <a class="yt-timestamp" data-t="00:29:57">00:29:57</a>, <a class="yt-timestamp" data-t="00:33:05">00:33:05</a>.
*   **Fully on-chain CLOBs:** While possible, fully on-chain order books, even on fast chains like Solana, tend to have wider spreads and less optimal execution because of the cost and latency associated with on-chain order updates <a class="yt-timestamp" data-t="00:26:50">00:26:50</a>. This makes it difficult for market makers to achieve tight spreads and frequent updates (e.g., 10-30 times a second) typical of high-frequency trading (HFT) firms <a class="yt-timestamp" data-t="00:27:10">00:27:10</a>.

Even with on-chain transparency, protocols like Elixir incorporate mechanisms such as provable randomness to prevent predictable order placement and deter adversarial trading <a class="yt-timestamp" data-t="00:28:21">00:28:21</a>. For example, a variable that fluctuates between 0 and 1 determines the algorithm's focus (balancing books vs. optimizing P&L), and a random percentage of orders might not make it to the exchange, making it unprofitable for others to trade against Elixir's algorithm <a class="yt-timestamp" data-t="00:28:57">00:28:57</a>.

## Benefits for the User

For users, especially those new to crypto, on-chain CLOBs offer several significant advantages over centralized exchanges:
*   **Custody:** Users retain custody of their assets at all times <a class="yt-timestamp" data-t="00:35:42">00:35:42</a>. This eliminates the need to trust a third party with funds, as seen with past exchange hacks or collapses <a class="yt-timestamp" data-t="00:35:56">00:35:56</a>.
*   **Fairness:** The transparent nature of on-chain operations means the exchange itself cannot trade against its users, preventing predatory practices like liquidating users for profit <a class="yt-timestamp" data-t="00:36:18">00:36:18</a>.
*   **Deeper Liquidity:** Protocols like Elixir contribute to deeper liquidity on decentralized exchanges by allowing passive liquidity provision, which makes trading more efficient <a class="yt-timestamp" data-t="00:36:24">00:36:24</a>.
*   **Improved User Experience:** On high-throughput, low-gas chains like Monad, CLOBs can enable features like one-click trading by using signatures for approvals, eliminating the need for multiple approvals for every trade <a class="yt-timestamp" data-t="00:37:51">00:37:51</a>. This allows users to keep funds in their own wallets (e.g., MetaMask, Ledger) while still trading seamlessly <a class="yt-timestamp" data-t="00:38:16">00:38:16</a>.

The evolution of crypto markets is increasingly seeing [[the_evolution_of_crypto_markets_and_technologies | AMMs]] moving towards order book models (e.g., Uniswap V3's concentrated liquidity, V4's hooks for limit orders) <a class="yt-timestamp" data-t="00:11:37">00:11:37</a>. The ability to passively supply liquidity, a key strength of AMMs, is now being adapted for order books, bridging the gap between the two models <a class="yt-timestamp" data-t="00:12:05">00:12:05</a>. This signifies a push towards more efficient, decentralized trading environments for end-users <a class="yt-timestamp" data-t="00:09:50">00:09:50</a>.