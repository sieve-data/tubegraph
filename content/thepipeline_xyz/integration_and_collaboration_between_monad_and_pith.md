---
title: Integration and collaboration between Monad and Pith
videoId: UmznS8RrLPE
---

From: [[thepipeline_xyz]] <br/> 

This article details the collaboration between Monad Labs, represented by CEO Keone, and Duralabs (contributor to Pith), represented by CEO Mike Cahill. The discussion highlights the synergy between the two entities, focusing on shared values, technical capabilities, and the future of decentralized finance (DeFi). <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>

## Background and Foundational Synergy

Mike Cahill's professional background includes working with Keone at Jump Crypto, and before that at KCG or Getco, in FX trading/sales and trading roles. <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> Cahill has been contributing to Pith since 2021, and Duralabs was formed in mid-2022 to provide the Jump team with agency to contribute full-time to Pith. <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

There is significant synergy between the [[overview_of_monad_and_its_community | Monad community]] and the Pith community, particularly on the builder side. <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a> The things that excite Mike Cahill about Pith are similar to what excites him about Monad. <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a> Both projects represent the intersection of finance and technology, requiring extensive "hard tech" optimizations and relentless effort to achieve the most efficient systems. <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>

> "I know keone and I know James really well and we work together and I know what they hold themselves to in terms of benchmarking and making things really um really fast and Performing and I know they don't stop." <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>

Keone emphasizes that the collaboration is driven by shared values, including a high regard for decentralization and community. <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a> Both Monad and Pith recognize that community is paramount in crypto, and it is also the most enjoyable aspect to work on. <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>

## Monad's Role in High-Performance DeFi

Keone highlights the critical importance of a high-fidelity oracle like Pith for various DeFi primitives:
*   **Lending Protocols**: Precise pricing is essential for the safety of vaults and to prevent issues like those seen with the Curve token, where large positions borrowing against it could lead to negative value if prices drop. <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>
*   **Derivatives Contracts**: Accurate pricing is fundamental for the settlement of derivatives, especially perpetuals, where mark prices and funding rates are calculated based on precise data. <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>

The goal is to enable DeFi to be more competitive against centralized exchanges by achieving greater efficiency and cheaper execution costs. <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a> High-performance oracles are seen as crucial to overcoming bottlenecks preventing DeFi from scaling. <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a> Monad aims to be one of, if not the most, performant platforms for trading in crypto. <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>

## Pith Network: A New Paradigm for Data Oracles

Pith's mission is to be the "source of truth at T0," constantly striving for instantaneous and accurate data. <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> Mike Cahill rates Pith's current status at "about a six out of a 10" in terms of optimization, acknowledging much room for growth. <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>

### Core Architecture and Business Model

Pith is designed as a universal data primitive, differing from other oracles that typically function as messaging protocols. <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>
*   **Source vs. Messenger**: Unlike systems that "fetch" data from the internet (e.g., Chainlink's messenger nodes), Pith creates a singular, constant source of truth. <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>
*   **Incentivizing Data Owners**: Pith directly incentivizes data owners to publish their data, including "paywalled data," to its source. <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a> This innovative economic model rewards publishers based on the utility of their data on-chain, moving away from reliance on advertising revenue. <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>
    *   This addresses the trend of data moving behind paywalls due to changing internet business models, exacerbated by large language models not routing traffic back to data sources. <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>
*   **Direct from Source**: Pith allows information to be accessed directly from its source, eliminating intermediate scraping steps and reducing latency. <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a> This brings Pith closer to its T0 goal. <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>
*   **PithNet**: Pith operates its own application-specific blockchain called PithNet. <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>
    *   Currently, 100 big institutions, including major trading firms (e.g., Jane Street, Susquehanna, Virtu, DRW) and crypto exchanges, publish their data to PithNet. <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a> This includes Cboe, the third-largest US equity exchange. <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>
    *   These firms, which traditionally haven't monetized their vast data troves, are now able to commercialize these assets. <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>
    *   PithNet is connected to 50 blockchains and serves about 300 applications. <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a> It handles approximately 4 million transaction updates per day. <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>
*   **User Experience**: For an end-user on a perpetuals exchange on Monad, they would see prices updated directly from PithNet. When they execute a trade, the price is pulled onto the local chain (via Wormhole), and the contract executes transparently on Monad. <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a> A small fee is paid to the Pith application, which is then distributed to data contributors, creating a sustainable business model. <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>

### Pith vs. Other Oracles: A Fundamental Difference

The standard model for other oracles involves messenger nodes setting timers to fetch prices from various websites, requiring off-chain payments and bespoke contracts. <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a> This approach leads to:
*   **Limited Scalability**: Each data feed is often tailored, preventing seamless interoperability across different chains. <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>
*   **Detrimental to Data Quality**: Profit maximization incentivizes reducing updates (e.g., 24 hours or 50 basis points), which is inadequate for real-time market data. <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>
*   **Adverse Selection**: Gappy or incremental data leads to issues like impermanent loss and adverse selection for liquidity providers (LPs). <a class="yt-timestamp" data-t="00:31:12">[00:31:12]</a>

Pith, by contrast, builds a singular source that benefits everyone equally, leading to powerful network effects. <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a> This aims to solve the problem of market data quality, shifting from arbitrage opportunities to building a new financial system accessible to everyone globally. <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>

> [!EXAMPLE] LP Profitability
> Pith's model allows for a more sustainable business for LPs. Unlike AMMs where LPs might be adversely selected due to static curves, Pith-powered protocols can adjust prices based on real-world market conditions, ensuring LPs are always pricing at a reasonable rate plus spread. <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>

### Pith Token and Governance

Pith recently completed a retrospective airdrop in November, involving 27 blockchains and making the token eligible to users of applications on those chains. <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>
*   Over 100,000 wallets are currently staking in the Pith protocol, more than double the number of wallets that claimed the airdrop. <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>
*   This staking number is significant in DeFi, comparing favorably to Aave (15,000 wallets), GMX (20,000), and Synthetix (40,000). <a class="yt-timestamp" data-t="00:38:43">[00:38:43]</a>
*   A vote for the Constitution will be the first step in arming governance to manage the network and foster community involvement. <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>

## Insights from Industry Leaders

### Focus on Infrastructure and Long-Term Optimism
Mike Cahill shares that a key insight, inspired by "The Coming Wave" book, is that people tend to overestimate technology's short-term effects and underestimate its long-term impact. <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a> The most crucial aspect of technological advancement is **infrastructure**. <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a> Just as Uber needed the iPhone's GPS and pocket computing power, killer applications in crypto require robust infrastructure. <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>

> [!TIP] Optimism for Infrastructure
> "People just need to stay optimistic that things are being built and get excited about infrastructure and think about what those things potentially can unlock... The use cases are actually coming and seeing the improvements of infrastructure are going to lead to that overnight success around the corner." <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>

### Trading Alpha: Cut Up Your Trades
Keone's trading advice is to "cut up your trades" rather than making one large trade at once. <a class="yt-timestamp" data-t="00:44:16">[00:44:16]</a> Using strategies like Time-Weighted Average Price (TWAP) or Volume-Weighted Average Price (VWAP) helps reduce price impact. <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a> While current crypto gas fees often make frequent small submissions impractical, high-performance blockchains like Monad will enable much better execution. <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>

> [!CAUTION] Avoid Adverse Selection
> Placing a large order on any exchange can lead to deep crossings of the spread, paying a lot, or if left in the book, it signals to others, reducing the likelihood of the order getting filled and causing adverse selection. <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>

## Conclusion

The collaboration between Monad and Pith signifies a powerful alignment of technical expertise and community vision to build robust, high-performance infrastructure for the future of DeFi. Their shared commitment to efficiency, decentralization, and sustainable models for data provision aims to address critical bottlenecks and unlock new possibilities in the crypto ecosystem. <a class="yt-timestamp" data-t="00:45:57">[00:45:57]</a>