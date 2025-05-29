---
title: Challenges and strategies in building crypto infrastructure
videoId: DS796z6QLVI
---

From: [[thepipeline_xyz]] <br/> 

Building new primitives in the crypto space presents unique [[challenges and propositions in blockchain technology | challenges]] and opportunities, especially for foundational infrastructure like liquidity protocols and layer-1 blockchains. Elixir Protocol, for example, focuses on providing decentralized liquidity for order books, aiming to address critical gaps in the market making landscape <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Founding Elixir Protocol: Identifying a Market Need

Phillip, the founder of Elixir Protocol, observed a recurring problem in the crypto space: blockchain startups and order-book-based exchanges consistently relied on a few centralized market makers for liquidity <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Traditional finance market making differs significantly from crypto; in traditional finance, profit centers are the P&Ls from market activity <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. In crypto, market makers often break even on algorithmic performance, making money by charging exchanges and protocols for access to their market-making services <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This led to the realization that a decentralized, trustless protocol could fulfill this role <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Elixir's Solution: Decentralized Order Book Liquidity

Elixir is building a modular DPOS (Delegated Proof-of-Stake) network designed to power order book liquidity <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. It allows anyone to supply liquidity, which the protocol then algorithmically builds and deploys on order books to tighten bid-ask spreads and deepen liquidity <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Key features include:
*   **Trustless Liquidity Provision** The protocol itself provisions liquidity on the back end <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Validators come to consensus, sending data to relay infrastructure for signing and transmission to exchanges <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This process is fully trustless, with funds sitting in a smart contract and signatures issued at that level <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **Similar Risk-Return Profile to AMMs** Elixir aims to provide a near-identical risk-return profile to Uniswap V2 for liquidity providers (LPs) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. LPs earn a share of incentives exchanges are already paying out to professional market makers <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Addressing the "Cold Start Problem" for Order Books** Unlike Automated Market Makers (AMMs) which make it easy to bootstrap liquidity for long-tail markets <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>, there wasn't a trustless way to bootstrap liquidity for an order book before Elixir <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Advantages of On-Chain Order Books for User Experience

For users, the transition to on-chain Central Limit Order Books (CLOBs), especially on high-performance chains like Monad, offers significant improvements over traditional or even early DeFi experiences:
*   **Custody** Users retain custody of their assets at all times, reducing counterparty risk <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>. This contrasts with centralized exchanges where funds are held by the exchange <a class="yt-timestamp" data-t="00:35:52">[00:35:52]</a>.
*   **Transparency and Fair Trading** Users can be assured the exchange is not trading against them, as the code is verifiable on-chain <a class="yt-timestamp" data-t="00:36:18">[00:36:18]</a>. This mitigates risks seen with models like FTX/Alameda where exchanges had built-in market makers that could exploit user positions <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>.
*   **Lower Slippage** Order books inherently offer better execution and drastically decrease slippage compared to AMMs, especially with high throughput and low gas fees <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Streamlined Trading Experience** On-chain CLOBs can enable "one-click trading" by issuing a signature for approvals, allowing users to trade without repeated authorizations <a class="yt-timestamp" data-t="00:37:59">[00:37:59]</a>.

## [[challenges and propositions in blockchain technology | Challenges and Solutions]] in Liquidity Provision

### Toxic Flow and Impermanent Loss
One of the biggest complaints in crypto is the lack of liquidity, and a significant issue within DeFi liquidity is "toxic flow" <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This occurs when passive LPs lose money due to arbitrageurs exploiting price discrepancies between a pool and the fair market price <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This is analogous to impermanent loss in AMMs <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

Solutions employed to mitigate toxic flow and improve profitability for LPs:
*   **Dynamic Fee Mechanisms** AMMs like Kyber Swaps and Uniswap V3 have introduced dynamic fee rates for LPs. Pairs with high "toxicity" (volatile, hard-to-price assets) charge higher fees, while less toxic pairs (like stablecoin-to-stablecoin) charge very low fees <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
*   **Spreads in Order Books** For order books, the equivalent is the spread <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. Market makers and protocols like Elixir dynamically adjust spreads: quoting wider during periods of higher volatility to protect LPs from toxic flow <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   **Reduced Costs for Liquidity Providers** Reducing the costs associated with supplying liquidity, such as gas fees for updating orders, makes it more inherently profitable for LPs <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.

### On-Chain vs. Off-Chain Order Books with On-Chain Settlement
While full on-chain CLOBs exist, many leading DEXes, including dYdX, Vertex, and RabbitX, use an off-chain order book that settles on-chain <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

*   **Speed and Cost** The main advantage of off-chain order books with on-chain settlement is significantly faster and cheaper price quoting <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Constantly updating orders on a fully on-chain CLOB, even with low gas fees, can become prohibitively expensive for market makers <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **MEV and Manipulation** Fully on-chain order books can be susceptible to manipulation via transaction spamming or MEV (Miner Extractable Value) tactics, affecting liquidations or order execution <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>. Off-chain order books with on-chain settlement mitigate some of these risks <a class="yt-timestamp" data-t="00:30:45">[00:30:45]</a>.
*   **Latency vs. Spread** Every additional second of latency in updating orders necessitates wider quotes from market makers to compensate <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. Off-chain systems allow for near-zero cost, sub-second updates, leading to tighter spreads <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.

### Mitigating Market Making Information Leakage
Even with transparency, on-chain market making has unique challenges. While the order book itself is transparent (similar to centralized exchanges via APIs) <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>, additional transparency comes from visible leverage positions <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. If an attacker can see a market maker's liquidation level, it creates an exploitable vulnerability <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

Elixir addresses this with:
*   **Provable Randomness** The protocol incorporates provable randomness to prevent predictability of future orders <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>. A variable, fluctuating between 0 and 1, influences the algorithm's behavior (e.g., optimizing for 50/50 book balance vs. P&L) <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>. This randomness is verifiable retrospectively but unpredictable in real-time <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.
*   **Random Order Cancellation** Randomly, one out of every five orders will not make it to the exchange <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>. This makes it economically unfavorable for bots to attempt to trade against Elixir's algorithms <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.

## Broader [[challenges_and_strategies_for_crypto_startups | Challenges for Crypto Projects]]

### Hiring and Talent Acquisition
Hiring top-quality, trustworthy individuals is often the biggest [[challenges_and_strategies_for_crypto_startups | challenge for crypto startups]] <a class="yt-timestamp" data-t="00:39:44">[00:39:44]</a>. Early on, projects may need to use headhunters to access specialized talent like Solidity Engineers <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>. As a project gains traction, inbound interest from candidates increases, alleviating this challenge <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>.

### Marketing and Branding for New Primitives
Explaining and positioning a new, complex primitive can be difficult <a class="yt-timestamp" data-t="00:40:18">[00:40:18]</a>. Elixir tackled this by shifting its branding from a direct "powered by Elixir" model to a white-label "Fusion" product (e.g., Vertex Fusion) <a class="yt-timestamp" data-t="00:41:04">[00:41:04]</a>. This allows exchanges to present Elixir's functionality as their own core feature, enhancing their offerings without external branding clutter <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.

### Regulatory Compliance
Operating with a U.S. presence, particularly in New York City, requires significant investment in ensuring regulatory compliance <a class="yt-timestamp" data-t="00:43:39">[00:43:39]</a>. This is a substantial cost and focus area for many U.S.-based crypto projects to avoid legal crosshairs <a class="yt-timestamp" data-t="00:43:10">[00:43:10]</a>.

### Community Building
A strong community is a vital asset for any crypto project <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. While Elixir focuses on B2B2C, providing infrastructure to exchanges, fostering community engagement is crucial for long-term recognition and adoption <a class="yt-timestamp" data-t="00:45:59">[00:45:59]</a>. A strong community attracts future partners and validators, as demonstrated by Elixir's testnet with over 13,000 validators <a class="yt-timestamp" data-t="00:47:05">[00:47:05]</a>.

> "Take on early stage risk and... be ruthless in your pursuit of it. Don't give up when you're pursuing it and it will come to life." <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>

This ethos encourages builders to persist despite naysayers and challenges, a fundamental principle for pushing the crypto space forward <a class="yt-timestamp" data-t="00:50:18">[00:50:18]</a>.