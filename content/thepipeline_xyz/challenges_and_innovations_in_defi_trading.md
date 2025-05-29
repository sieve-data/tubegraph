---
title: Challenges and Innovations in DeFi Trading
videoId: ijERsyZzWxs
---

From: [[thepipeline_xyz]] <br/> 

## Introduction
The realm of [[Challenges and Solutions in Decentralized Finance DeFi | DeFi]] trading, particularly in perpetual exchanges (perps), presents unique challenges and opportunities for innovation. While the core concept of perpetual contracts has gained significant traction, the decentralized nature of blockchain technology introduces complexities not seen in traditional finance or even centralized crypto exchanges <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>. Builders in this space aim to create products that offer a superior user experience while upholding the principles of decentralization and censorship resistance <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## The Ambition of Fully Onchain Perpetual Exchanges
The co-founder of Purple, PBJ, highlights the ambitious nature of their product: building a fully onchain perpetual exchange (PerpDex) on an EVM-compatible generalized Layer 1 (L1) blockchain like Monad <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. Historically, achieving this has been challenging because most successful claw-based PerpDexes, like dYdX and Hyperliquid, operate as app chains on Cosmos-based chains, not generalized EVM L1s <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. This distinction is crucial due to the inherent problems associated with running a high-performance trading venue on a generalized L1 <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.

### Core Product: Purple
Purple is a perpetual exchange built natively on Monad <a class="yt-timestamp" data-t="01:28:09">[01:28:09]</a>. The name "Purple" signifies "Perp on Purple Chain" <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. The idea for Purple originated from a trading team, Argonia, who recognized Monad's potential as a fast chain for market making <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>. This collaboration combines deep engineering expertise with insights from experienced traders who have operated on various perpetual and centralized exchanges <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>. Purple recently closed a $9.25 million funding round led by Dragonfly and Argonia, with participation from other funds and prominent angel investors from trading firms like HRT, Jump, and Barbellos <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

## Challenges in Onchain Trading

### Architectural Limitations
Previous attempts at onchain perpetual exchanges on Ethereum faced limitations due to slow block times (12 seconds), making proper market making difficult <a class="yt-timestamp" data-t="12:58:00">[12:58:00]</a>. This led to Automated Market Makers (AMMs) becoming the de facto solution for onchain perps <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>. Similarly, attempts on Solana faced issues with market makers consistently providing liquidity <a class="yt-timestamp" data-t="13:08:00">[13:08:08]</a>.

### Gas Fees and Order Prioritization
One significant challenge for onchain trading on a generalized L1 is dealing with gas fees <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>. App chains like Hyperliquid can implement custom opcodes to avoid gas fees for certain operations (e.g., collecting funding rates) and can even prioritize specific orders, such as cancel orders <a class="yt-timestamp" data-t="15:05:00">[15:05:05]</a>. This prioritization is crucial for market makers to react quickly to market events and avoid being "run over" by sudden price movements <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>. On a generalized L1, developers cannot control chain-level mechanics to offer such prioritization <a class="yt-timestamp" data-t="16:19:00">[16:19:00]</a>.

### User Experience (UX) Complexity
Perpetual contracts are inherently complex and not always retail-friendly <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. The flashing order book and constant data movement can be intimidating for new users <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>. Designing a UX that caters to both retail traders and professional users (whales) with differing needs is a significant hurdle <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

### Decentralization vs. Control Trade-offs
While centralized exchanges or app chains offer more control (e.g., over chain parameters, order prioritization), they sacrifice decentralization <a class="yt-timestamp" data-t="18:58:00">[18:58:00]</a>. This trade-off became evident during events like the "Jelly Jelly attack," where a centralized system could "rewrite history," undermining the core crypto ethos of "don't trust, verify" <a class="yt-timestamp" data-t="20:04:00">[20:04:00]</a>. For institutions, the lack of true decentralization and the potential for arbitrary changes to rules present a significant barrier to adoption <a class="yt-timestamp" data-t="21:51:00">[21:51:00]</a>.

## Innovations and Solutions

### Leveraging Generalized L1 Advantages (Monad)
Purple addresses many challenges by building on Monad, a generalized EVM L1 designed for high-performance trading <a class="yt-timestamp" data-t="13:36:00">[13:36:06]</a>.
*   **Speed**: Monad's 500-millisecond block time significantly improves the trading experience compared to slower chains <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **Native USDC**: Monad provides native USDC support from day one, eliminating the need for wrapped tokens and associated headaches, which is crucial for a PerpDex <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a> <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. This allows users to easily bridge USDC from other chains and start trading <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.
*   **Composability**: Being on a generalized L1 like Monad allows for greater composability within the broader [[Challenges and Solutions in Decentralized Finance DeFi | DeFi]] ecosystem <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>. Users can park assets like MONI tokens, Bitcoin, or Ethereum in lending protocols (e.g., Euler, Aave) to borrow USDC and then use it for perpetual trading on Purple <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>.
*   **Decentralization**: Purple leans into the decentralization of Monad, offering censorship resistance <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a> <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>. This prevents arbitrary changes to the system, building trust for users and future institutional adoption <a class="yt-timestamp" data-t="22:00:00">[22:00:00]</a>.

### Innovative Solutions for Market Makers
To address the lack of custom order prioritization on a generalized L1, Purple introduces "time-enforced orders" <a class="yt-timestamp" data-t="16:27:00">[16:27:00]</a>. Market makers can place orders that are only active for a specific number of blocks (e.g., two to three blocks), automatically expiring without needing a separate cancel order <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>.

### Enhancing Liquidity and Risk Management
*   **Vaults**: Purple aims to use vaults, potentially integrated with solutions like Fireblocks, to help market makers hedge their risk for certain tokens <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>. This allows market makers to access spot liquidity on Monad, making it easier to list new tokens and deepen liquidity on Purple, while passive participants can still earn yield <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>.
*   **Diverse Liquidity**: Unlike systems that rely on a single large market maker or an HLP (Hyperliquid LP) model, Purple focuses on attracting professional market makers <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>.

### Modular User Experience (UX)
Purple plans a modular approach to its UX, similar to Kraken, offering different interfaces tailored to various user types <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>.
*   **One-Click Trading**: A simplified UX for quick trades <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.
*   **Retail-Friendly**: An interface for general users that avoids overwhelming them with flashing order books and complex charts <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **Professional User**: A comprehensive UX providing all necessary data for experienced traders <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
*   **Open Development**: By building on a generalist L1, Purple encourages other developers to build innovative UX layers on top of its core smart contracts, such as Telegram bots, LLM interfaces, or other unique ways to interact with the exchange <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

## The Future of DeFi Trading
Perpetual exchanges are considered one of the best innovations in the [[Challenges and Solutions in Decentralized Finance DeFi | crypto]] space, serving as a new financial primitive that caters to the strong demand for trading and speculation <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>. The current [[Challenges and Solutions in Decentralized Finance DeFi | DeFi]] market is still nascent, with many iterations and experiments across different ecosystems <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>. However, the continuous innovation, institutional adoption, and the emergence of fast, composable L1s like Monad indicate a promising future for fully onchain [[Adoption and potential of DeFi and decentralized exchanges DEXes | DEXes]] and PerpDexes <a class="yt-timestamp" data-t="27:02:00">[27:02:00]</a>.