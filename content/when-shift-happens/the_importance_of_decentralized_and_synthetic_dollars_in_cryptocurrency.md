---
title: The importance of decentralized and synthetic dollars in cryptocurrency
videoId: z7sGoUXw4NE
---

From: [[when-shift-happens]] <br/> 

The cryptocurrency space was initially built to challenge existing traditional systems, yet its most crucial instrument, the stablecoin, remains heavily reliant on the banking system <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This paradox has led to the development of alternative forms of money, such as synthetic dollars, aiming to provide a crypto-native solution that operates independently of traditional banking infrastructure <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Athena: A Synthetic Dollar Protocol

Guy Young, the founder of Athena Labs, describes Athena as a synthetic dollar protocol built on Ethereum <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Its core philosophy is to create a form of money that is as safe and secure as possible, without relying on leverage <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a> <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## The Problem with Traditional Stablecoins

Traditional fiat-backed stablecoins like USDT and USDC are created by taking a T-bill, bond, or repo, sitting in a bank or a Special Purpose Vehicle (SPV), and issuing a receipt token against it <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. While generally considered low risk in their current setup, events like the USDC de-peg during the banking crisis revealed a crucial vulnerability: custodial risk <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a> <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a> <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. During that event, other stablecoins like MakerDAO and Frax also de-pegged in lockstep with USDC, demonstrating that many stable assets had the same underlying risk profile, with assets sitting in traditional banks like Silicon Valley Bank (SVB) <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a> <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a> <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

This highlighted the need for a truly uncorrelated stable asset, which is where the concept of a synthetic dollar comes into play <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a> <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.

## How Synthetic Dollars are Created (Athena's Model)

A synthetic dollar is created by putting down collateral, such as Ethereum or Bitcoin, and immediately taking out a short position of the same size on the other side <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a> <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>. The core idea is that if the price of the underlying asset moves, the two positions (long collateral and short derivative) perfectly offset each other, allowing a stable asset to be issued against this netted position <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a> <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.

Athena's model involves taking crypto assets (currently BTC and ETH) and immediately hedging them on the other side to issue its synthetic dollar, USDe <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a> <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. This process captures an interest rate, often referred to as a "funding rate," which represents the cost of capital within crypto for obtaining dollars <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a> <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. Essentially, Athena sits on the other side of those who want to long crypto, collecting an interest rate from them <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.

This strategy is known as a "cash and carry trade," which involves holding a spot asset and shorting its future or perpetual contract <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a> <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. While common in traditional finance for decades across commodities and bonds, it's now being tokenized at scale in crypto <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a> <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. Unlike traditional markets, crypto cash and carry trades can yield significantly higher interest rates, due to a large imbalance between capital supplied to crypto and market demand <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a> <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

### Risks in Cash and Carry Trade

The primary risk in a cash and carry trade, particularly in traditional finance, is excessive leverage <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a> <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>. However, Athena explicitly avoids leverage, operating on a 1x spot and 1x short basis to prioritize safety and security <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a> <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a> <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.

The biggest risk for Athena and USDe is the loss of underlying assets held with custodians, similar to the custodial risk faced by USDC with SVB <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a> <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>. This could occur due to fraud or loss of assets. While other risks exist, such as de-pegs to 98 or 99 cents, a complete wipeout of collateral backing would stem from issues with the underlying assets themselves <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a> <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>. Another less understood risk is the counterparty risk on short contracts, where the counterparty might not be able to pay out, as seen in ADL (Auto-Deleveraging) events from 2018 <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a> <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a> <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.

### Distinguishing from Luna/UST

Unlike Luna, Athena's governance token plays no role in backing USDe, ensuring the two are functionally separate <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a> <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a> <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>. The maximum market size of USDe is not limited by demand, which is estimated to be hundreds of billions of dollars for a dollar with yield above treasuries <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a> <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. Instead, the constraint is the capacity of the crypto derivatives market to support short interest <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>. The market self-regulates: as USDe grows, it pushes down funding rates, making the product less attractive and naturally limiting its size <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a> <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a> <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

## Why Synthetic Dollars Are Important for [[decentralized_finance_defi_and_its_potential | DeFi]]

[[importance_of_stablecoins_in_cryptocurrency | Stable-like assets]] have achieved genuine product-market fit in crypto beyond speculation <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a> <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. They are the "lifeblood" of nearly all [[decentralized_finance_defi_and_its_potential | DeFi]] applications:
*   Decentralized exchanges (DEXs) see dollars as the highest traded asset <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
*   Perpetual DEXs use dollars for collateral <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.
*   Money markets involve borrowing dollars <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   Over 90% of transactions on-chain and non-centralized venues involve a dollar on the other side <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

The core problem is that despite crypto's aim to disrupt traditional systems, its most vital instrument remains dependent on the banking system <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. Creating a truly crypto-native form of money is seen as the "Holy Grail" <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.

## Decentralization vs. Practicality

A key debate in crypto revolves around [[decentralization_vs_centralization_in_crypto_platforms | decentralization vs. centralization]]. While decentralization is crucial at the base layer (like Bitcoin and Ethereum), it can be unhelpful to prioritize it too early at the application layer <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a> <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a> <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Applications often function more like fintech companies than open networks <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Athena made an explicit trade-off: prioritizing scale by engaging with centralized venues over the "theatrics" of [[decentralized_finance_defi_and_its_potential | decentralized exchanges]] <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a> <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This pragmatic approach acknowledges that users often care less about pure decentralization than about scalability, efficiency, and cost <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a> <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Many builders, including early [[decentralized_finance_defi_and_its_potential | DeFi]] pioneers like Kain from Synthetix, are shifting towards building products that people actually want to use, rather than strictly adhering to purist decentralized ideals that appeal only to a small segment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a> <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a> <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Vision for the Future

Athena's initial focus was on [[decentralized_finance_defi_and_its_potential | DeFi]] applications, integrating with money markets and other stablecoin projects <a class="yt-timestamp" data-t="00:36:39">[00:36:39]</a> <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>. The next phase involves leveraging centralized exchanges (CEXs) as a significant distribution channel <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>. Unlike previous projects like MakerDAO that didn't materially push into CEXs, Athena aims to provide neutral infrastructure and align incentives so that centralized exchanges are motivated to distribute the product to their users <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a> <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>.

A key opportunity is using USDe as perpetual margin collateral, allowing trading firms to earn yield on their collateral, a significant benefit for large trading operations <a class="yt-timestamp" data-t="00:37:56">[00:37:56]</a> <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a> <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a> <a class="yt-timestamp" data-t="00:38:17">[00:38:17]</a>.

Looking ahead, Athena aims to be maximally flexible to respond to market conditions, potentially incorporating alternate sources of return, such as holding T-bills (RWAs), if market conditions in a bear market necessitate it <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a> <a class="yt-timestamp" data-t="01:00:48">[01:00:48]</a> <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>. This pragmatic approach ensures adaptability and sustainability in varied market cycles <a class="yt-timestamp" data-t="01:01:54">[01:01:54]</a>.

---
**See Also:**
*   [[importance_of_stablecoins_in_cryptocurrency | Importance of Stablecoins in Cryptocurrency]]
*   [[algorithmic_stablecoins_and_their_importance | Algorithmic Stablecoins and Their Importance]]
*   [[impact_of_centralized_and_decentralized_exchanges_on_the_crypto_market | Impact of centralized and decentralized exchanges on the crypto market]]
*   [[decentralization_vs_centralization_in_crypto_platforms | Decentralization vs centralization in crypto platforms]]
*   [[the_concept_of_decentralized_finance_and_its_evolution | The concept of decentralized finance and its evolution]]