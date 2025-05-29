---
title: Evaluating crypto with traditional finance models
videoId: qNqZgp2fNug
---

From: [[bankless]] <br/> 

The question of how to value Layer 1 (L1) blockchain tokens is paramount for investors to understand potential returns and risks [00:46:46]. It is critical to have a framework that provides a perspective on whether an asset is over or undervalued and allows for apple-to-apples comparisons between blockchains like Solana, Bitcoin, and Ethereum [01:00:59]. This question is especially important given that L1 tokens constitute the vast majority—around 95%—of the total crypto market capitalization, which currently stands north of $3 trillion [01:53:00].

Despite its importance, the valuation of L1 tokens remains a mysterious and debated question within the industry [03:17:00].

## Historical Valuation Attempts

Historically, various methods have been attempted to value L1 tokens, with varying degrees of success:

### MV=PQ (Quantity Theory of Money)
This monetary theory centers the valuation of money on its velocity (rate of spending), stating that money supply (M) times velocity (V) must equal price (P) times output (Q), or nominal GDP [03:54:00]. While once exciting to apply in the crypto context around 2016-2017, it has largely fallen out of favor as a way to value L1 tokens [04:18:00].

### Stock-to-Flow
Popularized by Bitcoiners, this model assumes that scarcity, measured by the ratio of existing supply to annual Bitcoin issuance, directly drives value [04:31:00]. It drew comparisons to gold, where demand is not met with an increasing flow, making it price-sensitive [04:51:00]. However, critics argue that stock-to-flow assumes infinite, persistent demand and is a very supply-side focused metric that doesn't fully account for the demand picture [05:20:00]. Its regression lines have not held up well [05:41:00].

### Relative Valuation (Bitcoin vs. Gold)
Currently, a more prevalent approach for Bitcoin valuation involves comparing it to gold. This method looks at gold's total addressable market (TAM) – around $18 trillion – and attempts to determine what percentage of this "non-nation state store of value" Bitcoin can capture [05:52:00]. Proponents argue that digital versions should eventually exceed their analog counterparts in value [06:40:00]. This line of thinking can be extended to other L1 assets as well [07:12:00].

## Current Consensus and its Critique

As of May 2025, a common consensus among analysts is that Bitcoin is a "special snowflake" that can be valued similarly to gold, as a monetary store of value [07:35:00]. However, all other L1 assets are typically valued based on a different methodology, often using [[real_economic_value_rev_in_crypto | Real Economic Value (REV)]] in a Discounted Cash Flow (DCF) model [07:49:00].

### Defining [[real_economic_value_rev_in_crypto | REV]]
[[real_economic_value_rev_in_crypto | REV]] is a metric that measures the total fees users pay to L1 validators, or the value validators capture from transaction activity on the chain [08:33:00]. Analysts often interpret this metric as analogous to company cash flows and use it to feed a DCF model, arguing that L1 tokens can be valued like traditional companies [08:52:00].

A DCF model calculates the present value of an asset as the sum of all its future cash flows, incorporating a discount rate [09:08:00]. This method, popularized in the 1930s for valuing equity assets, makes sense for companies that compound a balance sheet of fiat currencies [09:53:00].

### Critique of DCF for L1 Tokens
The issue with applying DCF to L1 tokens is that these tokens are not company shares and do not accrue value in the same way [10:45:00]. Validators do not collect revenue in a non-native currency (e.g., USDC); they earn more of the native token (e.g., ETH or SOL) [11:22:00]. This creates a circular reference: valuing an asset based on its ability to generate more of itself [11:46:00].

A key "mental test" reveals this flaw: if one wallet owned the entire supply of a company's shares (e.g., Apple), the company's value wouldn't change. However, if one wallet owned the entire supply of ETH or SOL, its value would drop to zero because no one would be paying fees or transacting [14:46:00]. This demonstrates that L1 tokens function more like a network where value is derived from interaction and distributed ownership, a concept akin to Metcalfe's Law (e.g., the value of a telephone network is zero if only one person owns all endpoints) [15:20:00].

While [[real_economic_value_rev_in_crypto | REV]] is a "naturally pure metric" for measuring the aggregate dollar value users pay for transactions [12:10:00], its conversion into dollars for DCF models is seen as "muddying the waters" [13:07:00]. Furthermore, [[real_economic_value_rev_in_crypto | REV]] only measures the use of the L1 token for payments, missing other crucial areas of demand [14:04:00]. The costs of transactions tend to deflate as blockchains scale, potentially negating growth from payment usage in terms of value accrual [29:31:00].

Nonetheless, [[real_economic_value_rev_in_crypto | REV]] and DCF models are still valuable for non-L1 assets, such as DeFi protocols and applications that generate cash flows [22:25:00]. For these assets, the "litmus test" of single-wallet ownership still holds: if one account owned all shares of a DeFi protocol like Aave, it would still generate revenue in non-native assets, making DCF a sound valuation metric [22:47:00].

## The "Money" Framework: L1 Tokens as Money

The core thesis for L1 token valuation posits that these tokens are money, not like stocks [23:27:00].

### Definition of Money
Money is defined as any asset primarily used for payments and as a store of value [23:57:00]. This definition is expansive; if people start hoarding and using copper for payments, copper becomes money [24:04:00]. Fiat currencies explicitly fit this definition, used for payments and as a store of wealth in bonds and bank deposits [24:18:00].

### L1 Tokens as Money
L1 tokens similarly fulfill this definition:
*   **Payments:** All transactions on L1 blockchains are paid for in the native token [24:41:00]. No other token can confirm transactions on the L1 itself [24:56:00].
*   **Store of Value:** L1 tokens are used for staking (taking duration risk for yield) and as a deposit asset in DeFi [25:02:00].

L1 tokens, especially smart contract networks like Ethereum, represent a hybrid between nation-state fiat money and commodity money (like gold or copper) [25:55:00]. They have an economy and a "GDP," where users "pay taxes" (fees) in the native unit of account to process transactions [26:09:00]. This "ground truth" of actual usage constitutes them as money [26:39:00].

### Store of Value vs. Payments Use Case
While L1 tokens are used for both payments and as a store of value, the latter is argued to be the primary driver of value accrual for these assets [28:04:00]. For instance, the US dollar's strength as a world reserve currency is driven by people storing wealth in dollar-denominated assets, not just its use for payments [28:16:00].

For L1 tokens, the payments use case is generally discounted because the cost of transactions (the primary service) continually deflates due to rapid blockchain scaling (e.g., 100x expansion of block space), which is "the enemy of price" [29:12:00]. In contrast, for the store of value use case, demand growth is not met with proportional supply increases (e.g., ETH supply inflates by a very small percentage or is deflationary), leading to price appreciation [29:50:00].

Some argue that [[real_economic_value_rev_in_crypto | REV]] will approach zero over time due to fee compression as networks scale [30:40:00]. However, some aspects of [[real_economic_value_rev_in_crypto | REV]], such as priority fees from transaction ordering, might be more durable due to fundamental supply constraints (e.g., time itself) [31:31:00]. Regardless, [[real_economic_value_rev_in_crypto | REV]] needs to be understood in a monetary context: it represents a native yield paid in the native asset [32:25:00].

## Introducing Realized Store of Value ([[real_economic_value_rev_in_crypto | RSOV]])

To measure the long-term drivers of value for L1 tokens, a new metric, [[real_economic_value_rev_in_crypto | Realized Store of Value (RSOV)]], is proposed [45:52:00].

[[real_economic_value_rev_in_crypto | RSOV]] is inspired by Bitcoin's "realized cap" metric, which measures the aggregate cost basis of the network by valuing each unit of Bitcoin at the price it last moved on-chain [46:48:00]. [[real_economic_value_rev_in_crypto | RSOV]] is an adapted version for smart contract platforms, focusing on two primary drivers of store of value demand:
1.  **Realized value of L1 tokens staked:** The dollar value of tokens committed to staking at their purchase price [46:50:00].
2.  **Realized value of L1 tokens in DeFi:** The dollar value of tokens deposited into DeFi protocols at their purchase price [46:50:00].

[[real_economic_value_rev_in_crypto | RSOV]] effectively measures net daily inflows of dollars into the network that are "staying in the network" by being held for long-term use cases like staking or DeFi [46:58:00]. It represents the net cumulative inflows in dollar terms, accumulating over time for these specific use cases [48:50:00].

The idea is that buying and staking, or buying and putting tokens into DeFi (e.g., for collateral or liquidity), indicates a "buy and hold" behavior, signifying their use as a store of value [49:02:00]. For instance, if 10% of Ethereum's supply is staked at a higher price, [[real_economic_value_rev_in_crypto | RSOV]] for ETH increases, reflecting new capital inflows [51:54:00].

### Relationship between [[real_economic_value_rev_in_crypto | REV]] and [[real_economic_value_rev_in_crypto | RSOV]]
[[real_economic_value_rev_in_crypto | REV]] (transaction fees) is elegantly captured within [[real_economic_value_rev_in_crypto | RSOV]] [01:05:37]. When validators receive [[real_economic_value_rev_in_crypto | REV]] (native token yield) and hold it to compound returns, the realized value of staked tokens increases [01:05:54]. Thus, [[real_economic_value_rev_in_crypto | REV]] contributes to [[real_economic_value_rev_in_crypto | RSOV]] by facilitating the transfer of native tokens from spenders to savers/stakers [01:06:16].

High [[real_economic_value_rev_in_crypto | REV]] often correlates with high prices (e.g., ETH during NFT mania, SOL during memecoin mania) [01:03:31]. This is because high transaction activity generates more fees, which, when compounded by stakers, directly feeds into [[real_economic_value_rev_in_crypto | RSOV]] [01:06:14]. Additionally, memecoin economies and NFT markets create inherent "supply sinks" of the base L1 token (e.g., SOL locked in bonding curves, ETH in NFT treasuries), further contributing to [[real_economic_value_rev_in_crypto | RSOV]] by increasing the demand to buy and hold the asset [01:08:06].

## Implications and Application of [[real_economic_value_rev_in_crypto | RSOV]]

[[real_economic_value_rev_in_crypto | RSOV]] offers a fundamental measure of net inflows for L1 tokens, allowing investors to develop a forward view on potential investments [47:17:00].

### Price to [[real_economic_value_rev_in_crypto | RSOV]] Ratio
Comparing an L1 token's market cap to its [[real_economic_value_rev_in_crypto | RSOV]] reveals how much future growth the market has priced in [01:14:10]. A higher ratio indicates a larger premium, implying significant growth expectations for the asset's store of value usage [01:15:59]. For example, Sui's price to [[real_economic_value_rev_in_crypto | RSOV]] ratio of 185x suggests a massive bet by investors on its future growth in store of value usage within its DeFi and staking applications, making it seem "expensive" from an [[real_economic_value_rev_in_crypto | RSOV]] perspective compared to Bitcoin or Ethereum [01:15:33].

### Factors Affecting [[real_economic_value_rev_in_crypto | RSOV]]
Factors that help increase [[real_economic_value_rev_in_crypto | RSOV]]:
*   **Inflows into staking:** Driven by higher staking yields or a change in market perception (lower perceived risk, higher demand for the yield) [01:19:41].
*   **Inflows into DeFi:** More usage of the asset as a deposit for collateral or liquidity [01:20:51].
*   **Growing asset issuance across the network:** More non-native assets (e.g., stablecoins, wrapped BTC) available on-chain for pairing with the L1 token in DeFi [01:21:10].
*   **Monetary attributes:** Reliable issuance policy, hardened protocol rules, and an easy-to-verify chain, highlighting strengths relative to analog government money [01:21:52].

Factors that can hurt [[real_economic_value_rev_in_crypto | RSOV]]:
*   Net outflows from staking or DeFi.
*   Censorship or centralization risks (e.g., Sui validators freezing funds) can reduce perceived value as a non-sovereign store of value, even if the asset remains a "currency" [01:25:59]. This can cause a decrease in demand for holding the asset as a store of value.

### L2s: Parasitic or Synergistic?
The debate over whether Layer 2s (L2s) are parasitic or synergistic to L1s often arises in the context of [[real_economic_value_rev_in_crypto | REV]] and DCF models, focusing on block space purchases [01:58:47]. However, from an [[real_economic_value_rev_in_crypto | RSOV]] perspective, L2s can be synergistic: if an L2 facilitates the import and use of the L1 token within its DeFi ecosystem (e.g., ETH on Base or Arbitrum), it increases [[real_economic_value_rev_in_crypto | RSOV]] regardless of transaction fees on the L1 [01:59:00]. This means L2s can drive demand for holding the L1 token as a store of value, which is a net positive [01:59:00].

### L1s as "Two Products"
L1 blockchains can be seen as offering two distinct "products":
1.  **Block space:** Valued via [[real_economic_value_rev_in_crypto | REV]] and DCF, with supply expanding rapidly as networks scale [01:24:29].
2.  **Uncensorable, non-state, non-sovereign store of value asset:** Valued via [[real_economic_value_rev_in_crypto | RSOV]], with scarce token supply [01:24:36].

Bitcoin exemplifies this dichotomy, with massive demand for its asset as a store of value, but comparatively small demand for its blockchain's transaction activity [01:24:54]. The "tribal dynamics" in crypto often see Bitcoin maximalists prioritizing [[real_economic_value_rev_in_crypto | RSOV]] (realized cap) and minimizing utility, while other L1 ecosystems prioritize [[real_economic_value_rev_in_crypto | REV]] [01:28:16]. Ethereum attempts to do both, which can complicate simple valuation narratives but aligns with its multifaceted design goals (e.g., the "burn" mechanism benefits both [[real_economic_value_rev_in_crypto | REV]] and [[real_economic_value_rev_in_crypto | RSOV]]) [01:29:13].

### Critique of "Cash Flow, Therefore DCF"
The assertion that "if there's a cash flow, it should be valued based on cash flows" is seen as a lazy argument when applied to L1 tokens [01:32:18]. Validators are paid in the *native* token, not non-native dollars, which fundamentally differentiates it from traditional company cash flows [01:32:46]. Many traditional assets, such as gold, oil, or fiat currencies, cannot be valued using DCF models [01:33:55]. L1 tokens, as commodity-like monies, also fall into this category [01:34:07].

## Conclusion

The [[real_economic_value_rev_in_crypto | RSOV]] framework aims to provide a more holistic and fundamental understanding of L1 token valuation, rooted in their actual usage as money [01:13:13]. It highlights that L1 tokens accrue value similarly: through people selling dollars to buy and hold the token long-term [01:30:04].

The "Total Addressable Market for Digital Non-Sovereign Money" chart illustrates the massive upside potential (20x or more) for L1 tokens if they capture a significant share of analog and government-based money (gold, fiat base money), which currently stands at $45 trillion compared to digital crypto money's $2.5 trillion [01:02:24]. Bitcoin is viewed as a "Trojan horse" in this transition, paving the way for other L1s as people seek diversification from traditional monetary risks [01:40:09].

The development of [[real_economic_value_rev_in_crypto | RSOV]] is a V1 framework that seeks further input from analysts to identify additional measurable store of value usages [01:34:39]. The goal is to improve the quality of the data signal and make it more accessible for broader analysis, moving away from tribal maximalism towards a data-driven and chain-agnostic approach to L1 valuation [01:35:50].

From an [[real_economic_value_rev_in_crypto | RSOV]] lens, Ethereum, relative to Bitcoin (which is 15% of Bitcoin's market cap), appears significantly undervalued due to its strong monetary attributes, low inflation, and central role in on-chain finance [01:39:21]. This suggests that there can be "more than one snowflake" in the digital money landscape [01:40:47].