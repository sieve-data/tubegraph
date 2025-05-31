---
title: Different Types of Stablecoins
videoId: 144qHAKjZ24
---

From: [[when-shift-happens]] <br/> 

A [[introduction_to_terra_and_stablecoins | stablecoin]] is a cryptocurrency designed to maintain a stable value against another asset, typically the US dollar <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. While they usually peg to the US dollar, they could technically be stable against assets like gold, a Big Mac's price, or a basket of fiat currencies <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

[[importance_of_stablecoins_in_cryptocurrency | Stablecoins]] are useful because volatile assets like Bitcoin are difficult to use in financial applications, such as paying for a cab ride or denominating a salary, as their value can fluctuate significantly <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. A [[introduction_to_terra_and_stablecoins | stablecoin]] fixes this by allowing familiar fiat-denominated financial transactions to occur within a crypto context <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This enables the layering of complex financial applications while retaining the permissionless and censorship-resistant qualities of cryptocurrencies like Bitcoin and Ethereum <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

In addition to stability, [[the_role_of_stablecoins_in_everyday_transactions | stablecoins]] offer unique benefits in the crypto world: they can earn [[highyield_stablecoin_interest | high yield stablecoin interest]] and can be transacted 24/7 globally <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

## Main Types of Stablecoins

There are largely three different types of [[introduction_to_terra_and_stablecoins | stablecoins]] <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>:

### 1. Fiat-Backed Stablecoins
These are the dominant type of [[introduction_to_terra_and_stablecoins | stablecoin]], with examples including USDT (Tether) and USDC (USD Coin) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Mechanism**: For every [[introduction_to_terra_and_stablecoins | stablecoin]] issued, a dollar's worth of assets is held in a bank account by a centralized custodian <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. If the [[introduction_to_terra_and_stablecoins | stablecoin]]'s price falls, the issuer buys back tokens to maintain the peg <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   **Issues**:
    *   **Centralization Risk**: Users must trust the issuer to maintain sufficient deposits <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. Issuers typically handle redemptions for large amounts, not individual users <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
    *   **Regulatory Risk**: Regulators can exert control over the issuer, potentially impacting decentralized finance (DeFi) applications built on top of these [[introduction_to_terra_and_stablecoins | stablecoins]] <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   **Why they are widely used**: Despite risks, they initially benefited from first-mover advantage and the perception of large backers (like Coinbase for Circle) providing sufficient balance sheet to underwrite risk in early stages <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. However, these risks scale poorly as market capitalization increases <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.

### 2. Crypto-Collateralized Stablecoins
MakerDAO's DAI is the market leader in this category <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Mechanism**: To issue one dollar's worth of [[introduction_to_terra_and_stablecoins | stablecoin]], users must lock up a larger value (e.g., 150%) of a volatile crypto asset like Ether <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. Liquidations and arbitrages are used to maintain the peg if collateral value drops <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Issues**:
    *   **Scalability**: Issuance is driven by demand for leverage on the underlying crypto asset, not directly by demand for the [[introduction_to_terra_and_stablecoins | stablecoin]] itself <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This can lead to the [[introduction_to_terra_and_stablecoins | stablecoin]] trading above its peg during periods of high demand (e.g., DeFi Summer 2020 for DAI) <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
    *   **Decentralization Compromise**: To address scalability, MakerDAO added USDC as a collateral type, meaning over 50% of DAI is now backed by a centralized [[introduction_to_terra_and_stablecoins | stablecoin]], undermining its decentralization <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

### 3. [[algorithmic_stablecoins_and_their_importance | Algorithmic Stablecoins]]
Terra (LUNA/UST) is a prominent example in this category <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   **Mechanism**: These [[introduction_to_terra_and_stablecoins | stablecoins]] hold no traditional collateral. Instead, they use game-theoretic incentives to maintain their peg <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
    *   **Terra's Model (LUNA/UST)**: Users can swap 1 Terra USD (UST) for $1 worth of LUNA, and vice versa <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
        *   If UST trades below $1 (e.g., 90 cents), users can buy UST for 90 cents, burn it for $1 worth of LUNA, and sell the LUNA for a profit, shrinking UST supply and pushing its price up <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
        *   If UST trades above $1 (e.g., $1.10), users can burn $1 worth of LUNA to mint 1 UST, sell the UST for $1.10, capturing arbitrage profit, expanding UST supply and pushing its price down <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
*   **Challenges and "Death Spiral"**: Many [[algorithmic_stablecoins_and_their_importance | algorithmic stablecoins]] have failed <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. The primary challenge isn't the mechanism itself, but rather the "go to market" strategy <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Projects like Iron Finance offered unsustainably high APRs (e.g., 2000%) to attract capital <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This created "ponzi economic" benefits that collapsed when capital exited, leading to the [[introduction_to_terra_and_stablecoins | stablecoin]]'s price going to zero <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This sudden and irreversible collapse is often referred to as a "death spiral."
*   **Terra's Success (Non-Recursive Economy)**: Terra's success lies in building a "non-recursive, robust economy" that drives real user engagement and economic growth for its [[introduction_to_terra_and_stablecoins | stablecoins]] <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. They focused on building applications that make Terra USD (UST) attractive to save and easy to spend <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>:
    *   **Spending**: Built payment services and e-wallets like Chai in Korea, integrated with major e-commerce merchants and offline venues <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. This closed the retail loop, allowing users to buy almost anything with Terra [[introduction_to_terra_and_stablecoins | stablecoins]] <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. This directly supports [[the_role_of_stablecoins_in_commerce | the role of stablecoins in commerce]].
    *   **Saving/Investing**:
        *   **Anchor Protocol**: Allows users to deposit Terra [[introduction_to_terra_and_stablecoins | stablecoins]] and earn a [[highyield_stablecoin_interest | high yield stablecoin interest]] of around 20% by leveraging staking yields from various Proof-of-Stake blockchains <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.
        *   **Mirror Protocol**: Enables investment in global asset classes (e.g., synthetic Apple stock) through price exposure using Terra USD as the gateway <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.
*   **Counter-Cyclicality**: The diverse utility of Terra's applications (payments, savings, synthetic investments) aims to create counter-cyclical demand for UST <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>. For example, in a bear market, users might still need to pay for daily items or might seek the [[highyield_stablecoin_interest | high yield stablecoin interest]] on Anchor while waiting for markets to recover <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>. While some correlation exists early on, it is expected to diminish over time <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

### The Importance of Decentralized Money

The underlying monetary layer of DeFi must be decentralized <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. If [[decentralized_exchanges_and_liquidity_protocols | decentralized exchanges and liquidity protocols]] rely on centralized [[introduction_to_terra_and_stablecoins | stablecoins]] like USDC or Tether, regulators could easily freeze assets, forcing changes to protocols and undermining the purpose of DeFi <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. Terra UST aims to be the best promise for truly decentralized money across the entire DeFi stack <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>.