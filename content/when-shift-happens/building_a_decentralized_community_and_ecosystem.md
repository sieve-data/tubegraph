---
title: Building a Decentralized Community and Ecosystem
videoId: 144qHAKjZ24
---

From: [[when-shift-happens]] <br/> 

This article explores the strategies and philosophy behind building a robust decentralized community and ecosystem, focusing on Terra, a blockchain platform founded by Do Kwon. The discussion covers the critical role of stablecoins, the challenges of decentralized finance (DeFi), and the unique approach Terra took to foster user adoption and community engagement.

## Do Kwon's Journey into Crypto and the Genesis of Terra

Do Kwon's journey into crypto began with tinkering on side projects after college, specifically developing a Wi-Fi mesh technology that allowed devices to connect via Wi-Fi Direct or Bluetooth, enabling free internet access even without direct internet connectivity [00:01:52]. This project evolved into a B2B networking solution for venues like amusement parks and shopping malls [00:02:21]. His search for "distributed mesh network" or "decentralized network" led him to discover Bitcoin and Ethereum [00:02:46]. By 2017, he made the full-time jump into crypto by founding Terra [00:03:11].

Terra was built around the concept of a stablecoin [00:03:25].

## The Power of Stablecoins

A stablecoin is an asset designed to retain stable value against another asset, typically the US dollar, though it could also be pegged to gold or other fiat currencies [00:03:36].

Stablecoins are considered a "killer app" in crypto because they address the volatility inherent in cryptocurrencies like Bitcoin, making them impractical for everyday financial applications [00:04:40]. For instance, using Bitcoin to pay for a cab ride or for an employment contract denominated in Bitcoin would lead to significant fluctuations in cost or salary due to price changes [00:04:46]. Stablecoins mitigate this by providing a stable unit of account, allowing familiar financial transactions to be brought into a crypto context while retaining the permissionless and censorship-resistant qualities of blockchain assets [00:06:09].

While skeptics question the need for US dollar-pegged stablecoins in the crypto world, arguing that it implies a failure of native crypto assets, Do Kwon argues that even as Bitcoin becomes more stable, it won't be stable enough to quote everything [00:07:54]. The ability of fiat currency to have flexible monetary policy that responds to demand changes makes it more useful in everyday life, retaining short-term price stability against consumer spending baskets [00:08:31]. As the overall crypto market has grown, stablecoins have proven to be the most useful product, with various markets like centralized exchanges, DEXes, DeFi apps, and NFT sales being quoted in and constituting around stablecoin liquidity [00:09:05]. Furthermore, stablecoins act as "super useful dollars" that can earn yield and be transacted 24/7 globally [00:09:47].

### Types of Stablecoins

There are three main types of stablecoins [00:10:32]:

1.  **Fiat-Backed Stablecoins**: These are dominant (e.g., USDT, USDC) [00:10:39]. For every stablecoin issued, a dollar's worth of assets is held in a bank account by a centralized custodian [00:10:48].
    *   **Pros**: Simple premise, effective when the issuer can maintain purchasing demand [00:11:11].
    *   **Cons**: Severe centralization risk, requiring trust in the issuer for deposit backing and market operations [00:11:17]. They also face significant regulatory risk, as regulators can control the issuer, potentially holding DeFi apps built on them hostage [00:11:52]. This defeats the purpose of the DeFi stack's decentralization [00:12:15]. These risks scale poorly as market cap grows [00:16:43]. Despite these risks, centralized stablecoins gained initial traction due to first-mover advantage and the backing of large entities like Coinbase and Bitfinex, which could underwrite early risks [00:16:11].
2.  **Crypto-Collateralized Stablecoins**: (e.g., MakerDAO's DAI) [00:12:23]. To issue $1 worth of stablecoin, more than $1 worth of volatile crypto assets (like Ether) must be locked up as collateral [00:12:28]. Liquidations and arbitrages maintain the peg if collateral value falls [00:12:48].
    *   **Pros**: Can be decentralized to some extent [00:13:00].
    *   **Cons**: Doesn't scale effectively because minting is driven by demand for leverage on the underlying crypto asset, not necessarily increased demand for the stablecoin itself [00:13:05]. This can lead to the stablecoin consistently trading above its peg during periods of high demand [00:13:30]. MakerDAO's solution of adding USDC as collateral, while resolving the scaling issue, compromised its decentralization, as over 50% of DAI became backed by USDC [00:13:41].
3.  **Algorithmic Stablecoins**: (e.g., Terra's UST) [00:14:13]. These stablecoins hold no direct collateral but use game-theoretic incentives to maintain their peg [00:14:20].

### Terra's Algorithmic Stablecoin (UST)

Terra's stability mechanism allows users to mint 1 UST by burning $1 worth of Luna, and vice versa, redeem 1 UST for $1 worth of Luna at any time [00:18:14].
*   If UST trades below peg (e.g., $0.90), users buy UST cheaply, swap it for $1 worth of Luna, and sell the Luna for a profit, shrinking UST supply and pushing its price back up [00:18:30].
*   If UST trades above peg (e.g., $1.10), users burn $1 worth of Luna to mint 1 UST, sell UST for $1.10, capturing arbitrage profit, expanding UST supply and pushing its price back down [00:18:46].

### Why Algorithmic Stablecoins Fail (and Terra's Success)

Many algorithmic stablecoins have failed due to their "go-to-market" strategy, often relying on unsustainable "ponzi economic" models [00:19:43]. For example, projects like Iron Finance offered excessively high APRs (e.g., 2000% daily) for depositing stablecoins into liquidity pools [00:19:54]. This led to massive capital inflows, but when yields dropped or the coin price fell, capital rapidly exited, causing the stablecoin's price to collapse to zero [00:20:19]. The challenge is not designing the stability mechanism, but building a non-recursive, robust economy that generates real usership and economic growth [00:20:51].

Terra achieved this by viewing "money as a product" and building applications that make Terra USD (UST) attractive for saving and spending [00:21:29].

#### Building Organic Demand: "Save It or Spend It"

Terra focused on two core functions of money: saving and spending [00:21:46].

1.  **Spending**:
    *   Initially, Terra built payment services and e-wallets in Korea, Mongolia, and Vietnam [00:22:04].
    *   In Korea, they developed "Chai," an e-wallet integrated with major e-commerce merchants and prominent offline venues like convenience stores and movie theaters [00:22:20]. Chai allows users to buy almost anything in the country with Terra stablecoins [00:22:45].
2.  **Saving**:
    *   **Anchor Protocol**: Users can deposit Terra stablecoins (UST) into a smart contract to earn a stable yield of around 20% [00:22:59]. This yield is powered by staking rewards from proof-of-stake assets across multiple blockchains like Solana, Terra, and Ethereum [00:23:06]. This provides an attractive savings yield on stablecoins [00:23:35].
    *   **Mirror Protocol**: Allows users to invest in any asset class globally through synthetic price exposure, using UST as the gateway [00:23:41]. This enables users in countries like Thailand or Vietnam to buy synthetic Apple stock or ETFs using UST without leaving the ecosystem [00:23:52].

This approach generates organic demand for UST through real-world utility and consistent savings opportunities, a stark contrast to other algorithmic stablecoins that relied solely on high, unsustainable APRs [00:24:16].

#### Counter-Cyclicality in Practice

The design of Terra's applications, particularly Mirror (for investments) and Anchor (for savings), aims to create "counter-cyclicality," meaning UST demand should remain robust even during market downturns [00:24:56]. While there was some distrust in UST's stability during the May 2021 crypto crash, leading to some sell-offs, the peg held remarkably well [00:26:24]. Do Kwon believes that as more apps are built and trust grows, users will have less reason to exit the stablecoin, even during macro crypto downturns [00:27:19]. For instance, people still need to pay for daily essentials like baby diapers or lunch, and during a bear market, the 20% yield on Anchor provides a strong incentive to hold UST while waiting for markets to recover [00:27:36]. Over time, this macro correlation is expected to diminish [00:28:32].

## [[building_a_successful_crypto_community_and_marketing_strategy | Fostering a Passionate Community]]

Terra boasts one of the most passionate communities in crypto, affectionately known as "Lunatics" [00:29:25]. Do Kwon admits that building communities was initially a challenge, but something shifted [00:29:36]. He attributes the community's deep investment to the inspiring and grand vision that underpins Terra: "a decentralized economy needs decentralized money" [00:31:06].

Terra is unique in its focus on building better decentralized money that can be used across the entire DeFi stack [00:31:23]. The community recognizes an "existential threat" to crypto and DeFi from centralized players and tightening regulations [00:31:30]. If the underlying monetary layer remains centralized (e.g., using USDC or Tether), regulators can easily control or freeze assets in DeFi protocols, forcing them to comply [00:32:07]. Therefore, decentralizing the underlying money, as Terra USD promises, is crucial for the success and independence of the broader DeFi ecosystem [00:32:27]. This vision galvanizes the community to achieve "really amazing things" [00:32:34].

The community's excitement grew significantly with the launch of Mirror Protocol due to its novel concept and alignment with movements like WallStreetBets [00:33:10]. This interest matured with Anchor Protocol's launch, offering a simple and attractive 20% fixed yield on stablecoins [00:33:28]. Initially, most marquee applications on Terra were built by Terraform Labs (TFL), the company Do Kwon founded [00:33:53]. However, the ecosystem has since exploded with hundreds of independent builders creating a diverse range of projects, from NFT projects (over 60 known) to DEXes, educational materials, and fiat gateways [00:34:03]. This community-driven development is continuously reshaping Terra's narrative, driven by hundreds of thousands of participants [00:35:00].

## Decentralization and Regulation

Regarding regulation, Do Kwon believes that even if Terraform Labs ceased to exist, the community is strong enough for new leaders to continue building a robust ecosystem [00:35:46]. While TFL currently helps accelerate growth, the long-term goal is for Terra USD to not need TFL, with the community self-organizing to drive updates, code, tooling, and new projects [00:36:15].

The biggest risk to Terra, in terms of regulation, is difficult to pinpoint, but its increasing decentralization makes it more resilient [00:36:38]. The growing demand for UST and the multitude of projects being built suggest that the "tipping point" for decentralization and unstoppable growth is either passed or very near [00:37:03].

## Future Outlook and Ecosystem Growth

Do Kwon projects that UST's market cap will reach or approach $10 billion by the end of the year [00:38:18]. By 2022, the goal is for Terra USD to be the dominant decentralized stablecoin, surpassing DAI [00:38:37]. Eventually, the aim is for UST to become the de facto decentralized money across the entire crypto ecosystem, constituting liquidity and medium of exchange for most crypto use cases [00:39:08].

Terra does not view other Layer 1 blockchains like Solana or Avalanche as competitors [00:39:39]. From a fundamental value capture perspective, it doesn't matter where Terra USD is used because minting $1 of UST always burns $1 worth of Luna, regardless of the blockchain (Ethereum, Avalanche, Binance Smart Chain, Solana, or Terra itself) [00:40:44]. Strategically, to become the standard for decentralized stablecoins across all blockchain ecosystems, UST needs to be present everywhere, making Terra's success complementary and synergistic with other blockchain ecosystems [00:41:30]. This multi-chain approach leverages the growth of other ecosystems to drive UST demand and, consequently, Luna's price [00:41:54].

A more important metric than Total Value Locked (TVL) for Terra's future is how UST is distributed by number of wallets and how much UST gets exported to different chains [00:45:46].

## Columbus 5 Upgrade

The Columbus 5 upgrade brought three main changes [00:42:29]:

1.  **Scalability**: Increased transaction processing capacity by 33x, providing more block space for various applications, including NFTs [00:42:37].
2.  **Interchain Connectivity**: Enabled by turning on the switch for IBC (Inter-Blockchain Communication), connecting Terra natively to the Cosmos ecosystem (Osmosis, Cosmos Hub, Crypto.com chain) [00:43:11]. It will also connect to Axelar for native Bitcoin integration and better connections to Binance Smart Chain and Avalanche [00:43:40]. Wormhole support will further connect Terra to the Solana ecosystem [00:43:52].
3.  **Simplified Economics**: Streamlined the Luna burn mechanism [00:44:06]. Now, when Luna is swapped for UST, it is permanently burned, leading to simpler, easier-to-understand economics [00:44:20].

## Unique Aspects and User Experience

Terra has built superior applications like Anchor, offering high and sustainable yield [00:46:11]. While components of Anchor's yield generation (e.g., using staking derivatives as collateral) are being adapted by other protocols like Compound Finance and Abracadabra [00:46:45], Terra also excels in user experience (UX) [00:48:23]. The Terra ecosystem offers a much easier and more intuitive UX compared to other ecosystems, contributing significantly to user stickiness [00:48:33]. Do Kwon suggests that this ease of use sets a higher bar compared to Ethereum, where smaller teams might have set a lower bar [00:49:17].

## Future Growth Drivers and The Power of Decentralized Building

Beyond Anchor, future growth in user adoption for Terra's ecosystem and UST is expected to come from metaverses and NFTs [00:50:26]. While DeFi is interesting for "cyber nerds," concepts like stable yields are "super boring" for everyday people [00:50:39]. In contrast, the excitement around NFTs and metaverses, exemplified by Snoop Dogg buying NFTs, is far more engaging and will bring in many more users [00:50:52]. These emerging areas will blend digital existence and property rights into a digital context, fostering innovation and user growth [00:51:05].

The most exciting aspect for Do Kwon is the unexpected growth of the Terra community [00:52:46]. He initially had a singular vision for building out Terra's monetary features, but the idea of decentralized money has resonated deeply, mobilizing entire crypto communities and attracting hundreds of different apps [00:53:05]. This community-driven development is constantly reshaping Terra's narrative, making it far more multi-dimensional than he could have imagined [00:53:30]. This open-source philosophy, where intellectual property is given away, encourages collective value creation and fosters unimaginable growth proportions [00:54:17].