---
title: Valuation of L1 tokens
videoId: qNqZgp2fNug
---

From: [[bankless]] <br/> 

Every Layer 1 (L1) blockchain features a native token, commonly referred to as an L1 token. Understanding how to value these tokens is crucial for investors to evaluate risks and potential returns for any asset, particularly given that L1 tokens constitute the vast majority—around 95%—of the current crypto market capitalization, which sits north of $3 trillion [01:41:40]. Key examples include [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Bitcoin]] (approximately 63% of total crypto market cap), [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Ethereum]], [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Solana]], Sui, and Bit Tensor [02:07:00]. This valuation question is essentially a "trillion-dollar question" [02:56:00].

## Historical Valuation Approaches

Historically, various methods have been proposed to value L1 tokens:

*   **MV=PQ (Quantity Theory of Money)**: Popularized around 2016-2017, this monetary theory centers the valuation of money on its velocity (rate of spending), stating that velocity must equal price times output or nominal GDP [03:51:00]. This approach has largely fallen out of favor for valuing L1 tokens [04:24:00].
*   **Stock-to-Flow**: Popularized by Bitcoiners, this model assumes that scarcity, measured by the ratio of existing supply to annual issuance, directly drives value [04:31:00]. While highly comparable to gold due to its supply inelasticity, stock-to-flow primarily focuses on the supply side and assumes infinite persistent demand, leading to its decline in popularity as a primary valuation method [05:20:00].
*   **Relative Valuation to Gold**: A more recent approach for [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Bitcoin]] involves comparing its market capitalization to that of gold (an $18 trillion market) and estimating what percentage of gold's "store of value" status Bitcoin can capture [05:51:00]. This thinking also extends to other digital assets, positing that a digital disruptor rarely remains smaller than its analog incumbent [07:01:00].

## Current Consensus and its Critique

As of May 2025, the consensus view among many analysts is that [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Bitcoin]] is a "special snowflake" and can be valued like gold, as a monetary reserve asset [07:35:00]. However, other L1 assets are often valued differently, typically through a [[Valuation models for blockchain networks | Discounted Cash Flow (DCF)]] model based on a metric called [[Real Economic Value REV in crypto | Real Economic Value (REV)]] [07:51:00].

### Understanding [[Real Economic Value REV in crypto | REV]] and [[Valuation models for blockchain networks | DCF]]

*   **[[Real Economic Value REV in crypto | REV]]**: This metric measures the total fees users pay to L1 validators, representing the value validators capture from transaction activity on the chain [08:33:00].
*   **[[Valuation models for blockchain networks | Discounted Cash Flow (DCF)]]**: A traditional financial model where the present value of an asset is the sum of all future cash flows, incorporating a discount rate [09:11:00]. For companies, this model makes sense because they compound or grow a balance sheet of fiat currencies, and share ownership provides a pro-rata claim on these non-native cash flows [09:53:00].

### Critique of [[Real Economic Value REV in crypto | REV]]/[[Valuation models for blockchain networks | DCF]] for L1 Tokens

Applying [[Valuation models for blockchain networks | DCF]] to L1 tokens is problematic because L1 tokens are not company shares and do not accrue value like them [10:47:00].
Validators earn rewards in the native token (e.g., more ETH, more SOL), not a non-native currency like USDC [11:22:00]. This creates a "circular reference" [11:51:00]. A non-circular, fundamental driver is needed for dollar valuation [11:54:00].

A key thought experiment highlights this: if one person owned the entire supply of a company's shares (like Apple), the company's value wouldn't change. But if one person owned the entire supply of ETH, SOL, or BTC, the value would be zero because there would be no network activity, no one paying fees, and no communication or transactions [14:48:00]. This illustrates that money is a network asset, and its value is relational, not solely based on internal cash flows [15:23:00]. While [[Real Economic Value REV in crypto | REV]] is a "pure metric" measuring the aggregate dollar value users pay for transactions [12:13:00], its conversion to dollars for DCF inputs muddies the waters, as the payments are originally denominated in the native token [12:40:00].

Furthermore, the payment use case (measured by [[Real Economic Value REV in crypto | REV]]) tends to deflate over time as blockchains scale and transaction costs decrease [29:22:00]. Fees will compress across all blockchain networks as they scale, meaning [[Real Economic Value REV in crypto | REV]] will trend towards zero as a *proportion* of overall network value [30:54:00]. While priority fees for transaction ordering might be a durable source of [[Real Economic Value REV in crypto | REV]] due to fundamental time constraints [32:12:00], the overall driver of value for L1 tokens needs to encompass more than just payments.

## L1 Tokens as Money: A New Perspective

The argument is that L1 tokens are fundamentally money, not company shares [23:27:00].

### Definition of Money and L1 Tokens
Money is defined as any asset primarily used to make payments and as a store of value [23:57:00].
*   **Payments**: L1 tokens are used for payments for on-chain services and goods, as all transactions on these chains are paid for in the native token [24:36:00].
*   **Store of Value (SOV)**: L1 tokens are used for [[role_of_staking_and_defi_in_crypto_valuation | staking]] (taking duration risk for yield) and as a deposit asset in [[role_of_staking_and_defi_in_crypto_valuation | DeFi]] [25:02:00].

L1 tokens occupy a unique position between nation-state fiat money and commodity money (like gold or copper) [26:01:00]. They have an economy and "GDP" where "taxes" (fees) are paid in the native unit of account [26:09:00]. The value comes from actual usage, not just declaration [26:41:00].

### Primacy of Store of Value
For crypto L1 assets, the store of value use case is generally more significant than the payments use case [28:04:00]. Just as the U.S. dollar's strength is driven by its role as a global reserve currency, L1 tokens accrue value as people convert other currencies into them for long-term holding [28:16:00]. The supply of L1 tokens for SOV (e.g., ETH inflating at ~0.5% per year) is much more constrained than the supply of "blockspace" for payments (which can 100x with scaling solutions like ZK-rollups) [34:35:00]. Demand growth for SOV is not met with proportional supply growth, thus driving price appreciation [30:34:00].

## Realized Store of Value (RSOV)

A proposed metric, **Realized Store of Value ([[Real Economic Value REV in crypto | RSOV]])**, aims to measure the fundamental value driven by the SOV use case of L1 tokens [45:52:00].

### Definition and Components
[[Real Economic Value REV in crypto | RSOV]] tracks the two primary drivers of SOV demand for L1 tokens [46:08:00]:
1.  **Realized value of L1 tokens [[role_of_staking_and_defi_in_crypto_valuation | staked]]** [46:36:00].
2.  **Realized value of L1 tokens in [[role_of_staking_and_defi_in_crypto_valuation | DeFi]]** [46:39:00].

This metric is inspired by Bitcoin's "realized cap" [46:48:00], which represents the aggregate cost basis of the entire network, or the sum of all Bitcoins valued at the price they were last moved on-chain [49:21:00]. [[Real Economic Value REV in crypto | RSOV]] adapts this principle for smart contract platforms, measuring the aggregate cost basis of tokens specifically held in staking contracts and [[role_of_staking_and_defi_in_crypto_valuation | DeFi]] protocols [51:05:00]. An increase in [[Real Economic Value REV in crypto | RSOV]] signifies net inflows of capital, indicating that people are buying and holding the asset for long-term value storage [52:12:00]. This also implies reduced velocity of the token, as it is being "hodled" rather than actively transacted [53:18:00].

### RSOV and [[Real Economic Value REV in crypto | REV]]
[[Real Economic Value REV in crypto | RSOV]] "elegantly captures" [[Real Economic Value REV in crypto | REV]] [01:05:37]. When users pay fees (REV) to validators, and validators compound or hold these earnings, the realized value of the staked tokens increases [01:05:58]. Thus, [[Real Economic Value REV in crypto | REV]] contributes to [[Real Economic Value REV in crypto | RSOV]] by facilitating the transfer of native tokens from spenders to savers (stakers) [01:06:55].
For example, the [[value_surges_of_trump_coin | memecoin mania]] on Solana and NFT mania on Ethereum saw high [[Real Economic Value REV in crypto | REV]] (gas fees), but also significant amounts of SOL and ETH locked up in bonding curves, pools, or project treasuries, which contributes to [[Real Economic Value REV in crypto | RSOV]] [01:07:42].

### RSOV in Practice: Price to RSOV Ratio

Comparing a token's market cap to its [[Real Economic Value REV in crypto | RSOV]] can reveal its "priced-in" future growth [01:14:10].
For instance, if Ethereum's market cap is $350 billion and its [[Real Economic Value REV in crypto | RSOV]] is $120 billion, the $230 billion difference represents the market's expectation of future inflows and growth [01:13:50].

A comparison of L1 tokens' "Price to [[Real Economic Value REV in crypto | RSOV]]" ratios reveals varying market expectations [01:15:17]:
*   [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Bitcoin]] and [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Ethereum]]: ~2x
*   [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Solana]]: ~6x
*   Tao: ~7x
*   Sui: ~185x [01:15:33]

A very high ratio, like Sui's 185x, suggests the market is pricing in a massive amount of future growth for its store of value usage, implying it's "expensive" relative to current on-chain activity [01:16:02]. Conversely, a lower ratio might indicate undervaluation or less future growth priced in.

### Factors Affecting [[Real Economic Value REV in crypto | RSOV]]
*   **Increases [[Real Economic Value REV in crypto | RSOV]]**:
    *   **Inflows into [[role_of_staking_and_defi_in_crypto_valuation | staking]] and [[role_of_staking_and_defi_in_crypto_valuation | DeFi]]**: Higher staking yields attract more capital, as does increased usage as collateral or liquidity in [[role_of_staking_and_defi_in_crypto_valuation | DeFi]] protocols [01:19:41].
    *   **Market View Changes**: A perceived decrease in risk (e.g., for ETH from 3.5% to 2.2% yield) can attract inflows, growing [[Real Economic Value REV in crypto | RSOV]] [01:20:28].
    *   **Growing Asset Issuance on the Network**: More paired assets (e.g., stablecoins, tokenized BTC) in [[role_of_staking_and_defi_in_crypto_valuation | DeFi]] increase opportunities for the L1 token to be used and accrue value [01:21:12].
    *   **Monetary Attributes**: Reliable issuance policy, hardened protocol rules, and easy-to-verify chains (like transparency and autonomy) enhance an L1's appeal as a store of value [01:21:52].
*   **Decreases [[Real Economic Value REV in crypto | RSOV]]**:
    *   **Outflows**: If capital leaves staking or [[role_of_staking_and_defi_in_crypto_valuation | DeFi]] [01:14:48].
    *   **Censorship**: Centralized control leading to asset freezing (e.g., Sui validators freezing hacker funds) undermines the non-sovereign store of value characteristic, potentially decreasing future demand for the asset as a reliable store of value [01:26:07]. While the asset might still be "money," such actions could deem it "bad money" [01:27:54].

## Conclusion

L1 tokens should be recognized as money that accrues value based on net inflows from users converting other currencies to buy and hold them long-term [03:40:00]. This is driven by their use as a payment rail and, more significantly, as a store of value. The total addressable market for digital non-sovereign money is estimated to be $45 trillion, compared to the current $2.5 trillion in digital crypto money, suggesting substantial upside [03:58:00].

Bitcoin, being the first in this wave of non-government money, has gained credibility as it "changes the least" [01:44:00]. However, other L1s, particularly [[bitcoin_vs_ethereum_vs_other_layer_1_1_tokens | Ethereum]], are increasingly demonstrating similar or even superior monetary attributes like censorship resistance, low inflation ([[EIP1559 and its impact on Ethereum valuation | EIP1559]]), and deep on-chain finance ecosystems [01:40:17].

The [[Real Economic Value REV in crypto | RSOV]] framework provides a fundamental, data-driven way to assess the long-term value drivers of L1 tokens, focusing on the behavior of buying and holding the native asset for staking and [[role_of_staking_and_defi_in_crypto_valuation | DeFi]] use [01:47:00]. This approach contrasts with the [[Valuation models for blockchain networks | DCF]] model, which is better suited for app-layer tokens that compound non-native assets [02:26:00].

The goal is to foster further analysis and improvement of the [[Real Economic Value REV in crypto | RSOV]] metric, encouraging contributions from analysts and data providers to refine this "ground truth" measurement of L1 token value [01:34:39].