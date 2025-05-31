---
title: Challenges and strategies for scaling cryptocurrency protocols
videoId: z7sGoUXw4NE
---

From: [[when-shift-happens]] <br/> 

The cryptocurrency ecosystem, despite its aim to undermine existing traditional financial systems, often finds its most important instruments reliant on the very banking infrastructure it seeks to replace <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This reliance highlights a core [[Cryptocurrency and blockchain ecosystem challenges | challenge]] in crypto: the need to create truly crypto-native forms of money <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Athena's Synthetic Dollar Protocol

Guy Young, the founder of Athena Labs, describes Athena as a synthetic dollar protocol built on Ethereum that aims to provide a crypto-native solution for money, free from reliance on traditional banking infrastructure <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Building Anticlockwise
According to Young, those who do best in building something often work "antic cyclical" to the market <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This means starting to build when the market is at its lows, experiencing "peak pessimism" <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Athena, for instance, launched a protocol worth over $10 billion within a year, but a year prior, market conditions were not favorable <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Addressing Past Failures: The Luna and FTX Context
Launching a new stablecoin design after the failures of Luna and FTX was considered an "outrageous idea" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Athena’s product design, which involves centralized exchanges and infrastructure, initially faced skepticism, with many viewing it as potentially "the next ponzi scheme" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. However, Young believes a good idea must be contrarian to the prevailing market sentiment <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Previous projects like LMA on Ethereum and UXD on Solana also attempted similar designs but failed <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The key difference for Athena was focusing on scalability rather than rigid decentralization <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### Prioritizing Scalability Over Decentralization
Young argues that people generally "care less about decentralization than we want them to" <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Choosing decentralization often means trading off scalability, efficiency, or cost <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Athena made an explicit trade-off for scale with centralized venues <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

This pragmatic approach, shared by other "OG Builders" like Kane from Synthetix, involves building products that people actually want to use, rather than solely adhering to purist decentralized ideals <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

Young differentiates the importance of decentralization by layers:
*   **Base Layer (Bitcoin, Ethereum):** Incredibly important for decentralization <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Application Layer:** Often resembles traditional businesses and prioritizing decentralization too early can be unhelpful <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Founders should focus on product-market fit first, then consider decentralization later <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### Innovation and Market Structure
The perceived lack of innovation in crypto, beyond stablecoins and speculation, may have contributed to the "meme coin mania" <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>, <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. Young sees meme coins as a response not only to a lack of innovation in more serious projects but also to changes in market structure and VC funding <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. It has become difficult for retail investors to gain early exposure to projects before they become multi-billion dollar entities on centralized venues <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. Meme coins offer a way for retail to participate in something early that feels like a more level playing field <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

### Understanding Stablecoins and Synthetic Dollars
Traditionally, fiat-backed stablecoins like USDT and USDC are backed by T-bills or bonds held in banks <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>. The USDC depeg during the banking crisis in 2023 highlighted the custodial risk associated with these, as all other stables traded down in lockstep <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>.

Athena's synthetic dollar (USD) is created by taking crypto assets (currently BTC and ETH) as collateral and immediately hedging them on the other side with a short position <a class="yt-timestamp" data-t="01:22:53">[01:22:53]</a>. This means if the underlying asset's price moves, the two positions perfectly offset each other, allowing for the issuance of a stable asset <a class="yt-timestamp" data-t="01:22:38">[01:22:38]</a>. This strategy captures an interest rate (funding rates) from those who want to long crypto <a class="yt-timestamp" data-t="01:23:03">[01:23:03]</a>.

The **cash and carry trade** involves putting down a spot asset and shorting its future or perpetual contract <a class="yt-timestamp" data-t="01:24:02">[01:24:02]</a>. While common in traditional finance, crypto offers significantly higher interest rates due to imbalances in capital supply <a class="yt-timestamp" data-t="01:24:28">[01:24:28]</a>.

#### [[Challenges and risks in the crypto ecosystem | Risks in the Cash and Carry Trade]]
*   **Leverage:** In traditional finance, this trade is often done with enormous leverage (20-50x), which can lead to issues if the spot and derivative contracts don't interact as expected <a class="yt-timestamp" data-t="01:25:17">[01:25:17]</a>. Athena mitigates this by not using any leverage <a class="yt-timestamp" data-t="01:25:36">[01:25:36]</a>.
*   **Counterparty Risk (ADL Events):** A key risk, especially in extreme market wipeouts, is that the counterparty on the short contract might go fully bankrupt, preventing payouts <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. While exchanges are better capitalized now, this risk hasn't been seen at scale for BTC in five years <a class="yt-timestamp" data-t="01:30:35">[01:30:35]</a>.
*   **Custodial Risk:** The biggest risk for Athena and USD is if there's fraud or loss of the underlying crypto assets held with custodians, similar to the USDC depeg with SVB <a class="yt-timestamp" data-t="01:32:50">[01:32:50]</a>. This is comparable to a smart contract hack in DeFi <a class="yt-timestamp" data-t="01:33:23">[01:33:23]</a>.

#### Avoiding Luna's Pitfalls
A critical difference between Athena and Luna (UST) is that Athena's governance token plays no role in backing USD, unlike Luna which backed UST <a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>. This explicitly separates the asset from the governance token <a class="yt-timestamp" data-t="01:26:41">[01:26:41]</a>.

The maximum market size for USD is limited by the capacity of the crypto derivative market, specifically the demand for leverage to long crypto on perpetuals <a class="yt-timestamp" data-t="01:27:08">[01:27:08]</a>. Currently, this is roughly 30% of open interest, implying a ceiling around $10-20 billion for USD without market movement <a class="yt-timestamp" data-t="01:27:33">[01:27:33]</a>. The protocol has a self-regulating mechanism: as USD grows, it pushes down funding rates, making the product less attractive and naturally limiting its size <a class="yt-timestamp" data-t="01:28:16">[01:28:16]</a>. This avoids the mistake of controlling interest rates, as seen with Anchor protocol and Terra <a class="yt-timestamp" data-t="01:28:50">[01:28:50]</a>.

### Token Launch and Community Engagement
Athena's token launch was notable for being "one of the most successful" in recent years <a class="yt-timestamp" data-t="01:47:47">[01:47:47]</a>. Young emphasizes not "dragging things out" or "farming your users" with prolonged point systems, a common practice in the industry <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>. Instead, Athena aimed to quickly determine product-market fit and rewarded early supporters handsomely <a class="yt-timestamp" data-t="01:51:09">[01:51:09]</a>. This approach is based on the idea that to build a cult following, projects need to make people "really rich" <a class="yt-timestamp" data-t="01:52:16">[01:52:16]</a>.

Young believes there's a strong negative correlation between a team's confidence in their product and how long they drag out points programs <a class="yt-timestamp" data-t="01:53:05">[01:53:05]</a>. Prolonged point systems are often used to generate inorganic traction for fundraising, rather than validating genuine product-market fit <a class="yt-timestamp" data-t="01:53:13">[01:53:13]</a>.

## Founder Mindset and Personal Strategies

### The Importance of Grit
While intellectual horsepower is important, Young believes that "grit" – not taking no for an answer and pushing ahead with aggression – is a more critical skill for success <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. He observes that often the "second smartest guy in the room" does the best because they have a "chip on their shoulders" and constantly strive to improve, unlike those who might become comfortable or lazy if always told they are the best <a class="yt-timestamp" data-t="01:10:19">[01:10:19]</a>.

### The Double-Edged Sword of Ego
Founders need a certain level of "natural arrogance" to start something new, as it means challenging existing worldviews <a class="yt-timestamp" data-t="01:13:39">[01:13:39]</a>. However, there's a fine line before ego becomes destructive, as seen in the "ugly examples" of the last cycle (e.g., Do Kwon) <a class="yt-timestamp" data-t="01:13:08">[01:13:08]</a>.

### Handling Criticism and FUD
Young actively seeks out criticism, viewing it as an opportunity to identify and address issues early <a class="yt-timestamp" data-t="01:43:04">[01:43:04]</a>. While the initial public response to Athena was difficult, he eventually learned to filter valid concerns from unfair criticism <a class="yt-timestamp" data-t="01:44:04">[01:44:04]</a>. He notes that if a founder has the "audacity" to build something that the majority doesn't believe in, they cannot expect universal agreement upon launch <a class="yt-timestamp" data-t="01:45:56">[01:45:56]</a>.

### Personal Routine for Focus
Young maintains a "boring routine" with consistent wake-up times, gym visits, and meals <a class="yt-timestamp" data-t="01:51:44">[01:51:44]</a>. This structure helps reduce "brain power" spent on planning daily tasks, allowing him to focus more on the core work <a class="yt-timestamp" data-t="01:51:14">[01:51:14]</a>. The physical activity is primarily a mental tool for focus and routine <a class="yt-timestamp" data-t="01:57:41">[01:57:41]</a>.

### The Attention Economy
In crypto, "attention is the only scarce thing" <a class="yt-timestamp" data-t="01:38:36">[01:38:36]</a>. Valuations and trading often revolve around "mind share" <a class="yt-timestamp" data-t="01:39:03">[01:39:03]</a>. Athena's controversial and divisive product itself generated significant marketing by forcing people to have an opinion, prompting widespread discussion <a class="yt-timestamp" data-t="01:49:57">[01:49:57]</a>.

## Future Outlook and Predictions
Young believes the BTC ETF was a "huge moment" that this entire cycle is built around <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>. A potential risk is outflows from these ETFs <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>. He anticipates an "interesting time for Athena" when interest rates in the US start to come down, as 90% of on-chain transactions involve a dollar <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>. The ETH ETF approval is also expected to create interesting dynamics for Athena, as it sits on the other side of speculative long trades <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>. The ETH ETF or the EigenLayer token drop could mark the cycle's top <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>.

### Strategies for Bear Markets
For future bear markets, Athena aims to remain "maximally flexible" <a class="yt-timestamp" data-t="02:00:31">[02:00:31]</a>. While Athena's product is sensitive to market cycles, the team wants the option for the community to decide on alternate revenue sources or exposures, such as real-world assets (RWAs) or holding T-bills, if market conditions turn <a class="yt-timestamp" data-t="02:01:01">[02:01:01]</a>. This is about having a "fallback option" if growth contracts <a class="yt-timestamp" data-t="02:01:01">[02:01:01]</a>.

### Notable Projects and Teams
*   **Pendle:** A project that facilitates interest rate trading, allowing users to buy points for a fixed yield or take a speculative view <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>. Young admires Pendle for its team's perseverance and continued "grinding" during the bear market to find product-market fit <a class="yt-timestamp" data-t="01:55:38">[01:55:38]</a>.
*   **Mantle:** A Layer 2 solution for Ethereum <a class="yt-timestamp" data-t="01:56:13">[01:56:13]</a>. Young is impressed by Mantle's "professionalism and thoughtful approach" <a class="yt-timestamp" data-t="01:56:29">[01:56:29]</a>, supporting applications with their large treasury and strategically planning for the types of applications they want on their chain, contrasting with more aggressive, short-cutting teams <a class="yt-timestamp" data-t="01:56:43">[01:56:43]</a>.