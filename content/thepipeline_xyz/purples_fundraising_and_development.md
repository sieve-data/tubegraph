---
title: Purples Fundraising and Development
videoId: ijERsyZzWxs
---

From: [[thepipeline_xyz]] <br/> 

Purple, a perpetual exchange built natively on Monad, recently announced the close of a significant funding round and continues to develop its ambitious product [01:28:01].

## Fundraising Success
Purple has successfully closed a funding round, raising $9.25 million [02:02:02, 02:46:00]. The round was led by Dragonfly and Argonia [02:14:16]. Additional funds involved include Brevin Howard, L1 Digital, and Hash King [02:19:07].

A crucial aspect of the funding round was the involvement of angel investors from well-known trading firms such as HRT, Jump, Barbellos, and Galwa [02:30:00]. The round also saw participation from influential founder angels like Kane, James, Eugene, and Jarry [02:38:00]. The fundraising process, while exciting for investors due to the "obvious and exciting idea" of a perpetual exchange on Monad, required substantial effort to finalize and dot all the i's [02:22:00, 02:26:00, 02:28:00].

## Team and Building Philosophy
Purple's co-founders, PBJ and AC, are engineers by trade, with previous experience building AMMs on Ethereum [06:02:05, 06:05:05, 06:34:02]. They quit their jobs around 2016 from AMD Xilinx, an FPGA hardware company used in defense, space, telecom, HFT, and early crypto mining [29:09:00, 29:12:00, 29:18:00]. They later found their way into crypto through hackathons, eventually focusing on low-level EVM programming [30:06:00, 30:23:00].

The idea for Purple originated when they were approached by the trading team Argonia, who suggested building a perps exchange on Monad, recognizing the chain's speed for market making [06:19:00, 06:27:00, 06:31:00]. Argonia's extensive experience across various perps exchanges and centralized exchanges provided critical insights into effective and ineffective strategies [06:44:00, 06:49:00].

Purple's team of approximately 10 people is based in London, operating hyper-locally rather than in a distributed manner [04:38:00, 04:41:00, 05:07:00]. This approach is intentional, as the team believes that building ambitious startups requires the ability to physically collaborate, whiteboard ideas, dissect, and rebuild them efficiently [04:48:00, 04:51:00, 04:54:00, 04:56:00, 04:58:00]. The focus is on delivering the product and fulfilling the promise to users, rather than expanding the team extensively [05:11:00, 05:13:00].

## Ambitious Product and Differentiation
Purple's core product is a fully on-chain perpetual exchange built on EVM [07:21:00, 07:25:00, 07:29:00]. This endeavor is considered ambitious because a fully on-chain CLOB (Central Limit Order Book) perps exchange on a generalized EVM L1 has not been successfully achieved [07:35:00, 08:01:00]. Historically, perps exchanges on Ethereum often became AMMs due to limitations in properly market-making on-chain, while successful CLOBs like dYdX and Hyperliquid operate as app chains on Cosmos, not generalized EVM L1s [07:40:00, 07:43:00, 07:50:00, 07:55:00, 07:58:00].

### Challenges and Solutions
Building on a generalized L1 like Monad presents unique challenges compared to app chains:
*   **Custom Op Codes & Gas Control:** App chains like Hyperliquid can implement custom op codes for functionalities like collecting funding without gas fees, controlling gas, and prioritizing orders (e.g., cancel orders always going to the top of the block) [15:02:00, 15:13:00, 15:15:00, 15:17:00, 15:29:00].
*   **Purple's Approach:** Since Purple cannot control the chain, it implements "time enforced orders" [16:22:00, 16:23:00, 16:27:00]. Market makers can set orders to be active for only a few blocks (e.g., two to three), automatically expiring without needing a separate cancel order [16:33:00, 16:35:00, 16:37:00, 16:39:00, 16:41:00].

### Key Differentiators
Purple aims to stand out by leveraging Monad's architecture and ecosystem:
*   **Generalized L1 with a Strong Ecosystem:** Purple benefits from building on a generalized L1 that fosters a strong community and ecosystem [13:36:00, 13:38:00, 17:00:00].
*   **Composability:** Monad enables composability, providing advantages such as:
    *   **Native USDC Support:** Monad will have USDC on day one, allowing users to trade instantly with one click, unlike solutions that rely on wrapped tokens or bridging from other chains [00:18:00, 00:20:00, 14:17:00, 14:19:00, 14:23:00, 14:25:00]. This addresses a problem seen with Hyperliquid, which needs Arbitrum for USDC flow [14:07:00, 14:09:00, 14:11:00].
    *   **Protocol Integration:** Users can take tokens (like bridged Bitcoin or Ethereum) on Monad, deposit them into lending protocols like Euler or Aave to borrow USDC, and then use that USDC to trade on Purple [14:30:00, 14:32:00, 14:34:00, 14:36:00, 14:39:00, 14:41:00, 14:45:00, 14:48:00].
    *   **Fireblocks Integration:** This will aid Purple's vaults, providing a solution for market makers to hedge risk for certain tokens using Monad's liquidity, while passive participants can earn yield [17:03:00, 17:06:00, 17:08:00, 17:10:00, 17:53:00, 17:56:00, 17:58:00, 18:00:00, 18:04:00].
*   **User Experience (UX):** Purple aims for a modular UX design, similar to Kraken, offering different interfaces for one-click trading, retail traders (without overwhelming data), and professional users (with full data) [09:53:00, 09:55:00, 09:58:00, 10:00:00, 10:01:00, 10:04:00, 10:06:00, 10:09:00, 10:12:00, 10:13:00, 10:15:00, 10:17:00, 10:20:00]. The goal is to provide familiar UXs (like Hyperliquid) alongside simpler options and to encourage external developers to build innovative interfaces like Telegram bots or LLM interfaces on top of Purple's core smart contracts [10:24:00, 10:25:00, 10:27:00, 10:36:00, 10:39:00, 10:40:00, 10:42:00, 10:45:00, 10:48:00, 10:51:00, 10:54:00, 10:56:00, 10:58:00, 11:01:00, 11:03:00, 11:05:00, 11:08:00, 11:10:00, 11:13:00].

## Commitment to Decentralization
Purple's decision to build on a decentralized L1 like Monad, despite it being a harder path, stems from a strong belief in decentralization [18:58:00, 19:00:00, 19:02:00, 19:04:00, 19:07:00, 19:13:00]. PBJ emphasizes that decentralization is not just a buzzword but provides crucial censorship resistance, a lesson highlighted by incidents like the "Jelly Jelly attack" where a closed system could arbitrarily rewrite history [19:13:00, 19:15:00, 19:17:00, 20:04:00, 20:06:00, 20:09:00, 21:02:00, 21:05:00].

For institutions, trusting a system where rules can be changed arbitrarily is a non-starter [21:51:00, 21:55:00, 21:57:00, 21:58:00, 22:00:00, 22:03:00, 22:06:00, 22:08:00, 22:10:00, 22:12:00, 22:15:00]. The long-term vision for crypto, especially for attracting institutional adoption, relies on decentralized, immutable systems like Ethereum and Solana, which have gained notice despite initial growing pains [22:17:00, 22:19:00, 22:22:00, 22:24:00, 22:26:00, 22:27:00, 22:29:00, 22:31:00]. Purple is committed to building for the next five to ten years with this decentralized, long-term mindset [23:37:00, 23:40:00].

## Future Plans and Community Engagement
Purple aims to launch on testnet soon, followed by mainnet, taking advantage of the synchronized launches with Monad's mainnet [25:11:00, 25:14:00, 25:18:00, 25:19:00, 25:22:00]. The team is actively working to bring features like cross margin and cross collateral, acknowledging that building everything on-chain takes time and rigorous security considerations [25:26:00, 25:30:00, 25:33:00, 25:35:00, 25:36:00, 25:39:00, 25:41:00, 25:44:00, 25:46:00, 25:48:00, 25:50:00, 25:54:00, 25:55:00, 25:56:00, 25:58:00, 26:00:00, 26:03:00].

### Community Engagement
Purple maintains a very active Discord community, led by Gan, who organizes daily events such as "trading wars," poker nights, and "therapy" sessions [24:36:00, 24:39:00, 24:41:00, 24:44:00, 24:45:00, 24:47:00, 24:49:00, 24:51:00, 24:52:00, 24:55:00].

For new users interested in DeFi or Purple's product, PBJ recommends:
*   **DeFi Workshops:** Join Purple's Discord for workshops on yield farming, spot trading, or perps, taught by professionals [42:14:00, 42:16:00, 42:18:00, 42:21:00, 42:23:00, 42:24:00, 42:27:00, 42:29:00, 42:31:00, 42:34:00, 42:36:00, 42:38:00].
*   **Testnet Exploration:** Try out products on testnets without spending real money. Users can get testnet Monad from Purple's Discord or other apps, and learning by doing is the best way [42:41:00, 42:43:00, 42:44:00, 42:46:00, 42:49:00, 42:52:00, 42:54:00, 42:56:00, 42:59:00, 43:00:00, 43:01:00].
*   **User Feedback:** Provide valuable feedback to builders by trying out new apps and highlighting areas that don't make sense to a new user [43:27:00, 43:30:00, 43:32:00, 43:34:00, 43:36:00, 43:37:00, 43:39:00, 43:41:00, 43:43:00].
*   **Technical Contributions:** For those proficient in programming, write Telegram bots or cool front ends to interact with smart contracts [43:49:00, 43:52:00, 43:54:00, 43:56:00]. Monad, being an EVM chain, allows developers to apply Ethereum tutorials directly [44:00:00, 44:02:00, 44:04:00, 44:06:00, 44:09:00, 44:10:00].

### Outlook on Crypto and DeFi
Despite periods of market slowdown, PBJ remains optimistic about the long-term future of crypto and DeFi [27:02:00, 27:06:00, 27:07:00, 27:09:00, 27:11:00, 27:13:00, 27:14:00]. He points to growing institutional adoption, the boom of stablecoins, and innovations like on-chain stocks (e.g., Superstate, Arbitrum-based Axiom) as indicators of significant progress beyond price charts [27:17:00, 27:19:00, 27:21:00, 27:23:00, 27:25:00, 27:28:00, 27:30:00, 27:32:00, 27:35:00, 27:36:00, 27:39:00, 27:41:00, 27:44:00, 27:47:00]. He expresses excitement for the non-obvious applications that will emerge from EVM as a high-frequency trading chain, citing the immense activity and buzz around the Monad testnet [27:57:00, 27:59:00, 28:02:00, 28:04:00, 28:06:00, 28:10:00, 28:12:00, 28:13:00, 28:15:00, 28:17:00, 28:19:00, 28:22:00].

Perpetual exchanges are seen as one of the best innovations in crypto, a "new financial primitive" with significant product market fit, particularly for speculation and leverage [11:25:00, 11:29:00, 11:31:00, 11:35:00, 11:37:00, 11:41:00, 11:44:00, 11:46:00, 11:49:00, 11:52:00, 11:54:00, 11:56:00, 11:58:00, 12:01:00, 12:04:00, 12:06:00].

## Final Alpha
For builders, PBJ recommends participating in hackathons to find ideas and gain practical experience, especially if they struggle with generating their own problems to solve [48:05:00, 48:07:00, 48:10:00, 48:12:00, 48:15:00, 48:17:00, 48:21:00, 48:23:00, 48:24:00, 48:28:00, 48:30:00, 48:32:00, 48:34:00, 48:37:00, 48:39:00, 48:42:00, 48:44:00].

He also suggests starting a meme contest featuring James, co-founder of Monad, as "Blockchain Larry David" due to his persona and demeanor [48:50:00, 48:54:00, 48:56:00, 48:59:00, 49:03:00, 49:06:00, 49:09:00, 49:11:00].