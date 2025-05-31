---
title: Introduction to Terra and Stablecoins
videoId: 144qHAKjZ24
---

From: [[when-shift-happens]] <br/> 

This article provides an introduction to Terra and the fundamental concept of stablecoins, featuring insights from Do Kwon, founder of Terraform Labs.

## Do Kwon's Journey to Crypto and the Genesis of Terra

Do Kwon's journey into cryptocurrency began after college, while working as an NLP engineer in Seattle <a class="yt-timestamp" data-t="01:29:57">01:29:57</a>. Feeling uninspired by his work, he tinkered with side projects, eventually developing a Wi-Fi mesh technology that allowed devices to connect via Wi-Fi Direct or Bluetooth, providing free internet access by hopping through a network of other users <a class="yt-timestamp" data-t="01:41:43">01:41:43</a>. This technology was then packaged into a B2B networking solution, serving amusement parks, shopping malls, and large venues <a class="yt-timestamp" data-t="02:21:00">02:21:00</a>.

During research for distributed mesh networks, Kwon encountered terms like Bitcoin and Ethereum <a class="yt-timestamp" data-t="02:46:00">02:46:00</a>. He spent increasing amounts of time in crypto chat rooms and Discord servers, eventually making the full-time jump into crypto in 2017 by founding Terra <a class="yt-timestamp" data-t="03:00:00">03:00:00</a>.

## Defining Stablecoins and Their Utility

A [[different_types_of_stablecoins | stablecoin]] is a cryptocurrency designed to retain a stable value against another asset, most commonly the US dollar <a class="yt-timestamp" data-t="03:36:00">03:36:00</a>. While typically pegged to the US dollar, a stablecoin could theoretically be stable against the price of gold, a Big Mac, or even other crypto assets <a class="yt-timestamp" data-t="03:43:00">03:43:00</a>. For practical purposes, a stablecoin is understood as an asset with low price volatility against the US dollar <a class="yt-timestamp" data-t="04:05:00">04:05:00</a>.

### Why Stablecoins are the "Killer App" in Crypto
The fixed monetary policy of Bitcoin, while a feature for investment, makes it impractical for financial applications and everyday commerce due to its price volatility <a class="yt-timestamp" data-t="04:27:00">04:27:00</a>. For example, using Bitcoin to pay for a cab ride or denominating a salary in it would expose parties to significant value fluctuations during the transaction or contract term <a class="yt-timestamp" data-t="04:46:00">04:46:00</a>. This volatility adds a transaction cost <a class="yt-timestamp" data-t="05:16:00">05:16:00</a>.

[[the_role_of_stablecoins_in_commerce | Stablecoins]] solve this by allowing familiar financial transactions, traditionally denominated in fiat currencies, to operate within a crypto context <a class="yt-timestamp" data-t="06:07:00">06:07:00</a>. This enables the development of complex financial applications layered on top of price-stable assets <a class="yt-timestamp" data-t="06:25:00">06:25:00</a>. They combine the price stability of fiat with the permissionless and censorship-resistant qualities of cryptocurrencies like Bitcoin and Ethereum <a class="yt-timestamp" data-t="06:44:00">06:44:00</a>.

As the crypto market has grown, stablecoins have proven to be the most useful product, with various markets, DeFi applications, and NFT sales being quoted in and constituting around stablecoin liquidity <a class="yt-timestamp" data-t="09:05:00">09:05:00</a>. They are considered "super useful dollars" that can earn yield and be transacted 24/7 globally <a class="yt-timestamp" data-t="09:43:00">09:43:00</a>.

## Types of Stablecoins

There are three main categories of [[different_types_of_stablecoins | stablecoins]]:

1.  **Fiat-backed Stablecoins:**
    *   **Mechanism:** For every stablecoin issued, a dollar's worth of assets is held in a bank account by a centralized custodian <a class="yt-timestamp" data-t="10:48:00">10:48:00</a>. Examples include USDT (Tether) and USDC (Circle) <a class="yt-timestamp" data-t="10:41:00">10:41:00</a>. If the stablecoin's price falls, the issuer buys back tokens to maintain the peg <a class="yt-timestamp" data-t="10:58:00">10:58:00</a>.
    *   **Advantages:** This model works well initially when market caps are small <a class="yt-timestamp" data-t="16:04:00">16:04:00</a>. Major backers like Coinbase (for Circle) and Bitfinex (for Tether) provide balance sheet support in early stages <a class="yt-timestamp" data-t="16:16:00">16:16:00</a>.
    *   **Disadvantages:** This model carries significant centralization risk, as users must trust the issuer to maintain deposits and engage in open market operations <a class="yt-timestamp" data-t="11:17:00">11:17:00</a>. It also poses severe regulatory risk, as regulators can exert control over the issuer, potentially impacting decentralized finance (DeFi) applications built on top of these stablecoins <a class="yt-timestamp" data-t="11:52:00">11:52:00</a>. These risks scale poorly as the market cap grows <a class="yt-timestamp" data-t="16:43:00">16:43:00</a>.

2.  **Crypto-collateralized Stablecoins:**
    *   **Mechanism:** To issue a stablecoin, more than a dollar's worth of volatile crypto assets (e.g., Ether, ERC-20 tokens) must be locked up as collateral <a class="yt-timestamp" data-t="12:28:00">12:28:00</a>. MakerDAO's DAI is a leading example <a class="yt-timestamp" data-t="12:24:00">12:24:00</a>. [[liquidation_issues_in_the_terra_ecosystem | Liquidations]] and arbitrages are used to maintain the peg if collateral value falls <a class="yt-timestamp" data-t="12:48:00">12:48:00</a>.
    *   **Advantages:** This model offers a degree of decentralization <a class="yt-timestamp" data-t="13:00:00">13:00:00</a>.
    *   **Disadvantages:** It struggles with scalability because the motivation to mint stablecoins is driven by demand for leverage on the underlying crypto asset, not by demand for the stablecoin itself <a class="yt-timestamp" data-t="13:05:00">13:05:00</a>. This can lead to the stablecoin trading above its peg during periods of high demand <a class="yt-timestamp" data-t="13:30:00">13:30:00</a>. To address this, DAI has had to add USDC as a collateral type, which unfortunately compromises its decentralization, with over 50% of DAI now backed by USDC <a class="yt-timestamp" data-t="13:41:00">13:41:00</a>.

3.  **[[algorithmic_stablecoins_and_their_importance | Algorithmic Stablecoins]]**:
    *   **Mechanism:** This class of stablecoins, which includes Terra, holds no collateral <a class="yt-timestamp" data-t="14:20:00">14:20:00</a>. Instead, it relies on game-theoretic incentives to maintain its peg <a class="yt-timestamp" data-t="14:24:00">14:24:00</a>.
    *   **Terra's Stability Mechanism:** Users can always swap 1 TerraUSD (UST) for $1 worth of Luna (Terra's native token), and vice versa <a class="yt-timestamp" data-t="18:17:00">18:17:00</a>.
        *   **When UST is below peg (e.g., $0.90):** Users are incentivized to buy UST at $0.90, redeem it for $1 worth of Luna, and sell the Luna for a profit <a class="yt-timestamp" data-t="18:30:00">18:30:00</a>. This increases demand for UST and reduces its supply, pushing the price back to $1 <a class="yt-timestamp" data-t="19:01:00">19:01:00</a>.
        *   **When UST is above peg (e.g., $1.10):** Users are incentivized to burn $1 worth of Luna to mint 1 UST, sell the UST for $1.10, and capture the arbitrage profit <a class="yt-timestamp" data-t="18:46:00">18:46:00</a>. This increases UST supply and reduces Luna supply, pushing the price back to $1 <a class="yt-timestamp" data-t="19:01:00">19:01:00</a>.
    *   **Advantages:** The strength of the algorithmic stability mechanism scales well with market cap and over time <a class="yt-timestamp" data-t="17:34:00">17:34:00</a>.

## Overcoming the "Death Spiral" and Building a Robust Economy

Many [[algorithmic_stablecoins_and_their_importance | algorithmic stablecoins]] have failed because their go-to-market strategies relied on unsustainable "Ponzi economic" incentives, such as offering extremely high APRs for depositing stablecoins into liquidity pools <a class="yt-timestamp" data-t="19:43:00">19:43:00</a>. When capital flowed out, the stablecoin's price would collapse to zero <a class="yt-timestamp" data-t="20:28:00">20:28:00</a>.

Terra's success lies in building a non-recursive, robust economy that generates real usership and economic growth on top of its stablecoins <a class="yt-timestamp" data-t="21:02:00">21:02:00</a>. Terra approaches money as a product with two main features: saving and spending <a class="yt-timestamp" data-t="21:42:00">21:42:00</a>.

*   **Spending:** Terra focused on making UST easy to spend. It developed payment services and e-wallets like Chai in Korea, integrated with major e-commerce merchants and prominent offline venues (convenience stores, movie theaters, online grocery delivery, ride-hailing) <a class="yt-timestamp" data-t="22:04:00">22:04:00</a>. This closed the retail loop, allowing users to buy almost anything with Terra stablecoins <a class="yt-timestamp" data-t="22:45:00">22:45:00</a>.
*   **Saving:** Terra built applications like [[anchor_protocol_as_a_backbone_of_terra_network | Anchor Protocol]] and Mirror Protocol.
    *   **[[anchor_protocol_as_a_backbone_of_terra_network | Anchor Protocol]]**: Allows users to deposit Terra stablecoins into a smart contract and earn a stable 20% yield <a class="yt-timestamp" data-t="22:59:00">22:59:00</a>. This yield is powered by staking yields from proof-of-stake assets across multiple blockchains like Solana, Polkadot, and Ethereum <a class="yt-timestamp" data-t="23:10:00">23:10:00</a>.
    *   **Mirror Protocol**: Enables users to invest in any asset class globally through synthetic price exposure, using UST as the gateway <a class="yt-timestamp" data-t="23:41:00">23:41:00</a>. This means users in countries like Thailand or Vietnam can buy synthetic Apple stock or ETFs using UST <a class="yt-timestamp" data-t="23:52:00">23:52:00</a>.

This approach creates an "organic demand" for UST, as people use these applications regularly, regardless of market conditions <a class="yt-timestamp" data-t="24:18:00">24:18:00</a>. This leads to a notion of "counter-cyclicality," where demand for UST remains strong even during crypto bear markets, as users still need to pay for daily goods or seek stable yields on their savings <a class="yt-timestamp" data-t="24:56:00">24:56:00</a>.

During the crypto crash in May 2021, Terra's UST market cap was around $2 billion, and about $400 million of UST was sold off <a class="yt-timestamp" data-t="26:33:00">26:33:00</a>. Despite this, the peg held extremely well, trading precisely at its theoretical swap spread with Luna <a class="yt-timestamp" data-t="26:57:00">26:57:00</a>. As more apps are built and trust in UST grows, the macro correlation with other crypto assets is expected to decrease <a class="yt-timestamp" data-t="27:19:00">27:19:00</a>.

## The Power of the Terra Community

The Terra community, often referred to as "Lunatics," is one of the most passionate in crypto <a class="yt-timestamp" data-t="29:25:00">29:25:00</a>. While Do Kwon attributes part of the growth to unknown factors, he believes the core reason for the community's deep engagement is Terra's inspiring vision: a decentralized economy needs decentralized money <a class="yt-timestamp" data-t="31:06:00">31:06:00</a>.

Many feel an existential threat to crypto and DeFi from centralized players and tightening regulations <a class="yt-timestamp" data-t="31:30:00">31:30:00</a>. If the underlying monetary layer remains centralized (e.g., using USDC or Tether), regulators could easily control DeFi protocols by freezing assets <a class="yt-timestamp" data-t="32:02:00">32:02:00</a>. TerraUSD, as a decentralized money, represents the best promise to maintain the integrity of the decentralized finance stack <a class="yt-timestamp" data-t="32:27:00">32:27:00</a>. This mission galvanizes the community.

The community's excitement notably increased with the launch of Mirror Protocol, followed by [[anchor_protocol_as_a_backbone_of_terra_network | Anchor Protocol]] <a class="yt-timestamp" data-t="33:10:00">33:10:00</a>. Initially, Terraform Labs built most marquee applications, but now hundreds of independent builders are creating projects, from NFTs and DEXs to educational material and new banks <a class="yt-timestamp" data-t="33:50:00">33:50:00</a>.

## Decentralization and Regulatory Outlook

Regarding regulatory risk, Do Kwon believes that even if Terraform Labs ceased to exist today, the [[terra_ecosystem_and_the_future_of_decentralized_finance | Terra ecosystem]] has a strong enough community for new leaders to continue building <a class="yt-timestamp" data-t="35:46:00">35:46:00</a>. The goal is for TerraUSD to eventually not need Terraform Labs, with the community self-organizing to develop core code, tooling, and new projects <a class="yt-timestamp" data-t="36:16:00">36:16:00</a>. The biggest risk would be a complete, unforeseen event impacting the core team <a class="yt-timestamp" data-t="36:44:00">36:44:00</a>. The increasing demand for UST and the growing number of projects suggest the ecosystem's tipping point towards full decentralization may be near or already passed <a class="yt-timestamp" data-t="37:03:00">37:03:00</a>.

### Future Growth and Market Position

Do Kwon envisions TerraUSD reaching or nearing $10 billion in market cap by the end of 2021 <a class="yt-timestamp" data-t="38:18:00">38:18:00</a>. By 2022, the goal is for UST to be the dominant decentralized stablecoin, surpassing DAI <a class="yt-timestamp" data-t="38:35:00">38:35:00</a>. Ultimately, Terra aims to become the de facto decentralized money across the entire crypto ecosystem, constituting liquidity and a medium of exchange for most crypto use cases <a class="yt-timestamp" data-t="39:08:00">39:08:00</a>.

Terra does not view other Layer 1 blockchains (like Ethereum, Solana, or Avalanche) as competitors <a class="yt-timestamp" data-t="41:04:00">41:04:00</a>. The underlying economics for Luna are the same regardless of where UST is used. A dollar of UST minted burns a dollar's worth of Luna, whether it's on the Terra blockchain or another chain <a class="yt-timestamp" data-t="40:47:00">40:47:00</a>. Terra's strategic goal is to become the standard for decentralized stablecoins across *all* blockchain ecosystems, making its success complementary and synergistic with other blockchain ecosystems <a class="yt-timestamp" data-t="41:30:00">41:30:00</a>. This allows Terra to leverage the growth of other ecosystems to increase UST demand and, consequently, Luna's price <a class="yt-timestamp" data-t="42:01:00">42:01:00</a>.

### [[terra_ecosystem_and_the_future_of_decentralized_finance | Columbus 5 Upgrade]]
The [[terra_ecosystem_and_the_future_of_decentralized_finance | Columbus 5 upgrade]], a significant milestone for Terra, brought three main changes:

1.  **Scalability:** Increased the number of transactions processable by Terra blocks by 33x <a class="yt-timestamp" data-t="42:37:00">42:37:00</a>.
2.  **Interchain Connectivity:**
    *   Natively connects Terra to the Cosmos ecosystem via IBC (Inter-Blockchain Communication) <a class="yt-timestamp" data-t="43:11:00">43:11:00</a>.
    *   Connects to Axelar for native Bitcoin integration into Terra and better connections to Binance Smart Chain and Avalanche <a class="yt-timestamp" data-t="43:40:00">43:40:00</a>.
    *   Connects to the Solana ecosystem via Wormhole <a class="yt-timestamp" data-t="43:52:00">43:52:00</a>.
3.  **Simplified Economics:** The Luna burn mechanism for minting UST is now direct and perpetual, simplifying the economic model for users <a class="yt-timestamp" data-t="44:06:00">44:06:00</a>. Every Luna burned to mint UST stays burned <a class="yt-timestamp" data-t="44:34:00">44:34:00</a>.

Following Columbus 5, Terra's Total Value Locked (TVL) surpassed $10 billion, exceeding Solana's TVL <a class="yt-timestamp" data-t="45:04:00">45:04:00</a>. Do Kwon emphasizes that UST distribution by number of wallets and its export to different chains are equally, if not more, important metrics than TVL <a class="yt-timestamp" data-t="45:46:00">45:46:00</a>.

## Unique Strengths and Future Directions

Terra's ecosystem is unique because it allows for the creation of "incredible products" that are superior to those in other ecosystems <a class="yt-timestamp" data-t="46:24:00">46:24:00</a>. While components of Anchor's yield generation mechanism are being adopted elsewhere (e.g., Compound Finance adding staking derivatives, Abracadabra's MIM stablecoin backed by yield-bearing assets), Terra's overall user experience (UX) is considered significantly better and easier than other ecosystems, contributing to greater stickiness for users <a class="yt-timestamp" data-t="48:20:00">48:20:00</a>.

For mass adoption and reaching a billion users, Do Kwon believes that metaverses and NFTs will be more effective than DeFi applications <a class="yt-timestamp" data-t="50:26:00">50:26:00</a>. While DeFi is interesting to "cyber nerds," concepts like "stable attractive yields" are "super boring" to everyday people <a class="yt-timestamp" data-t="50:39:00">50:39:00</a>. In contrast, "Snoop Dogg just bought NFTs on Ethereum" is "super interesting" <a class="yt-timestamp" data-t="50:52:00">50:52:00</a>. Metaverses will integrate existence and property rights into a digital context, fostering innovation and bringing in new users <a class="yt-timestamp" data-t="51:05:00">51:05:00</a>. This shift is crucial for bringing more women into the space, who may find digital art and music more engaging than traditional DeFi concepts <a class="yt-timestamp" data-t="52:00:00">52:00:00</a>.

Do Kwon is most excited about the community's role in constantly reshaping Terra's narrative <a class="yt-timestamp" data-t="53:43:00">53:43:00</a>. What started as a singular vision for decentralized money has been amplified and diversified by hundreds of thousands of community members building apps on Terra, leading to "unimaginable proportions" of growth <a class="yt-timestamp" data-t="53:13:00">53:13:00</a>.