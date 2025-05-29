---
title: Business models for data in the blockchain space
videoId: UmznS8RrLPE
---

From: [[thepipeline_xyz]] <br/> 

The value and monetization of data have undergone significant transformations, particularly with the advent of blockchain technology. Historically, the internet's business model encouraged open data on websites to drive traffic and advertisement revenue <a class="yt-timestamp" data-t="09:37:40">[09:37:40]</a>. However, companies began to put data behind paywalls when advertising revenue was insufficient, a trend observed in news organizations over the last decade <a class="yt-timestamp" data-t="10:02:40">[10:02:40]</a>.

This shift has been exacerbated by the rise of Large Language Models (LLMs), which change how information is requested online and do not typically redirect users to original sources or provide citations <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>. This means data owners might not receive value for their information, leading them to restrict access <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>. The trend of data becoming increasingly protected is expected to continue as its value rises <a class="yt-timestamp" data-t="17:29:00">[17:29:00]</a>. For example, Twitter (now X) implemented rate limiting to prevent AI companies from freely scraping its data <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>. Similarly, Wall Street Journal's paywalled content accessed via ChatGPT has sparked discussions about compensation for data usage <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a>.

While historical data is challenging to monetize once freely accessible, real-time data holds significant value <a class="yt-timestamp" data-t="20:33:00">[20:33:00]</a>. The financial market data industry, for instance, generates approximately $70 billion in real-time revenues, making free data, often delayed, less valuable and usable in smart contracts <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>.

## Pith's Innovative Data Business Model

Pith aims to solve this challenge by establishing a "Universal data primitive" that acts as a singular, consistent source of truth for real-time data at "t0" (time zero) <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>. Its approach borrows from systematic trading backgrounds, focusing on optimizations and continuous improvement for efficient systems <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

Pith's business model is designed to incentivize data owners to publish their "paywall data" to its network <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>.
*   **Direct from Source:** Pith receives information directly from publishers who are creating the data, eliminating intermediary scraping steps and reducing latency <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
*   **PithNet:** The data is aggregated on an application-specific blockchain called PithNet, where over 100 publishers contribute 400 symbols, updating several times per second <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>.
*   **Commercial Model:** When data is delivered to another blockchain for an application to use (currently connected to 50 blockchains and used by ~300 applications), a small fee is collected <a class="yt-timestamp" data-t="27:23:00">[27:23:20]</a>. This fee is then distributed to the data contributors, providing a commercial return for their valuable data assets <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.
*   **Institutional Adoption:** This model has successfully attracted major financial institutions and trading firms, such as Jane Street, Susquehanna, Virtu, DRW, and Cboe (including Bats and VIX options), who were previously unable to monetize their vast data troves <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>. Their engagement in publishing data to a blockchain represents a significant milestone for institutional adoption in crypto <a class="yt-timestamp" data-t="16:22:00">[16:22:20]</a>.

## Contrasting Pith with Traditional Oracle Models

Traditional oracle models, such as Chainlink, often operate as messaging protocols <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. These rely on "automation nodes" that fetch data from the internet based on timers (e.g., every 24 hours) or price changes (e.g., 50 basis points) <a class="yt-timestamp" data-t="28:58:00">[28:58:00]</a>. This approach has several limitations:
*   **Performance:** It limits how performant the data can be <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.
*   **External Payments:** It often requires external payments outside the blockchain to compensate for gas fees and node operations <a class="yt-timestamp" data-t="29:09:00">[29:09:00]</a>.
*   **Bespoke Nature:** These are often bespoke solutions for individual clients, lacking scalability and interoperability between different feeds on various chains <a class="yt-timestamp" data-t="29:38:00">[29:38:00]</a>.
*   **Data Quality:** The need to account for gas fees can incentivize less frequent updates, leading to outdated and gappy data that is "blatantly very bad" for dynamic markets <a class="yt-timestamp" data-t="30:24:00">[30:24:00]</a>.

In contrast, Pith's architecture builds a singular, continuously updating source accessible equally to all connected blockchains and applications <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a>. This creates powerful network effects, benefiting everyone as the source grows <a class="yt-timestamp" data-t="29:50:00">[29:50:00]</a>. PithNet handles millions of updates per day across 50 blockchains <a class="yt-timestamp" data-t="27:52:00">[27:52:00]</a>.

## Impact on Decentralized Finance (DeFi)

High-performance oracles like Pith are crucial for the [[growth and scalability challenges in blockchain ecosystems | growth and scalability]] of decentralized finance (DeFi):
*   **Lending Protocols:** They require precise pricing to maintain the safety of vaults and protocols, preventing issues like those seen with the Curve token where inaccurate pricing could lead to significant financial risks <a class="yt-timestamp" data-t="23:26:00">[23:26:00]</a>.
*   **Derivatives Contracts:** Accurate, up-to-date pricing is essential for the settlement of derivatives, especially perpetuals, which rely on mark prices and funding rates <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>.
*   **Capital Efficiency:** Accurate oracles contribute to greater efficiency in DeFi, making it more competitive against centralized exchanges by reducing execution costs <a class="yt-timestamp" data-t="25:12:00">[25:12:00]</a>.
*   **Sustainable Liquidity Provision:** Pith's precise data can enable more sustainable business models for liquidity providers (LPs) in protocols like Synthetix, where pools can adjust prices based on real-world market conditions, mitigating [[challenges and propositions in blockchain technology | impermanent loss]] typically faced by AMMs <a class="yt-timestamp" data-t="32:53:00">[32:53:00]</a>. This ensures that LPs are not constantly losing money due to adverse selection from arbitrageurs with superior data <a class="yt-timestamp" data-t="33:25:00">[33:25:00]</a>.

## Community and Governance

Pith operates as a decentralized oracle where governance can manage on-chain updates <a class="yt-timestamp" data-t="36:51:00">[36:51:00]</a>. The PITH token, distributed via an airdrop across 27 blockchains to over 100,000 wallets, encourages broad community involvement in governance <a class="yt-timestamp" data-t="37:04:00">[37:04:00]</a>. This active community, with over 110,000 wallets staking (more than many established DeFi protocols), is vital for the network's self-identity and long-term sustainability <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>.

> "People overestimate the effects of technology in the short term and underestimate them in the long term" <a class="yt-timestamp" data-t="41:15:00">[41:15:00]</a>.
> — Amar's Law

The development of robust infrastructure, like Pith's data model, is a critical precursor to the emergence of "killer apps" and significant growth in the blockchain space <a class="yt-timestamp" data-t="41:41:00">[41:41:00]</a>. Just as the iPhone was necessary for the Uber app, underlying blockchain infrastructure enables the next wave of applications <a class="yt-timestamp" data-t="41:50:00">[41:50:00]</a>. This focus on fundamental improvements, even if not immediately apparent, is expected to lead to breakthroughs in the future <a class="yt-timestamp" data-t="42:48:00">[42:48:00]</a>.