---
title: real world problems being solved by crypto
videoId: wMa6GXjDyH4
---

From: [[thepipeline_xyz]] <br/> 

The crypto ecosystem aims to decentralize services and help the decentralized world supersede the centralized world <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This requires seamless interoperability between different ecosystems <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>, and a single interoperability layer is crucial for delivering the best user experience and powerful applications <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Core Philosophical Disruption

Early on, the appeal of crypto stemmed from a strong libertarian perspective, addressing perceived irresponsibility of banks and promoting self-sovereignty <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The fundamental thesis was that crypto would allow for permissionless access and full control over one's money <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

With the advent of programmable smart contracts (like Ethereum), the focus evolved to creating more interesting financial primitives and structures broadly useful to the world <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. The primary disruption remains in finance and money, which in turn unlocks numerous other empowering possibilities <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Addressing Financial Inefficiencies

### [[crypto_as_a_solution_for_high_credit_card_fees | Payments and High Credit Card Fees]]
In the Western world, credit card companies levy substantial fees (around 3%) on every transaction, which poses a significant cost to businesses, including small and large enterprises <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Crypto offers a solution where anyone with a phone can pay for a service directly, bypassing these middlemen <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

In the undeveloped world, where credit cards are less common, crypto (particularly Tether) is already widely used for payments <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. To effectively disrupt existing payment systems, crypto networks like Monad must be able to process transactions at a comparable scale, aiming for 10,000 transactions per second throughput <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The combined market capitalization of Visa and Mastercard, a trillion-dollar business, highlights the massive value extracted from businesses through these fees <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Personal Finance and DeFi
Crypto has significant potential in personal finance, aiming to make decentralized finance (DeFi) the standard for banking, trading, borrowing, and lending <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

Key improvements needed include:
*   **Reducing Slippage**: Bringing slippage costs from frequently seen 1-5% in DeFi down to single-digit basis points <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This requires performant environments where market makers can quote tightly and reduce spreads, offering better execution for users <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Lowering Transaction Costs**: Current crypto transaction fees (e.g., $20 gas fees) are often considered normal but are a significant barrier for new users, especially those without large crypto holdings <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>. Networks like Solana demonstrate that actions can be almost free, allowing users to transact without worrying about a daily "action budget" <a class="yt-timestamp" data-t="00:49:21">[00:49:21]</a>. This high cost also affects developer habits, leading them to prioritize gas optimization over adding defensive assertions, which can lead to security issues and hacks <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.
*   **Eliminating Unnecessary Friction**: Traditional financial systems impose significant friction, such as high currency exchange fees at airports or ATM fees <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. With a crypto wallet on a phone, users could easily perform FX swaps for a fraction of the cost, leveraging a shared global state with high transaction execution <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This decentralized approach also protects against single entity failures or corruption <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

### [[cryptos_potential_in_identity_and_transaction_settlement | Identity, Community, and Transaction Settlement]]
Beyond payments and personal finance, crypto holds significant potential in:
*   **Identity**: Managing and verifying digital identities <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Community**: Facilitating new forms of decentralized communities and interactions <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **General Settlement**: Enabling more efficient settlement for all kinds of transactions, from stock trading to the transfer of real-world assets like houses or cars <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

## Technical Solutions Enabling Progress

### Omni Chain Fungible Tokens (OFTs)
Wrapped assets, commonly used in bridging, create a fundamental problem where the end-user holds an IOU that carries perpetual risk; their asset could become worthless at any time if the bridge is compromised <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This shifts risk from liquidity providers (LPs) to the end-user, a "really bad trade-off" <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

Omni Chain Fungible Tokens (OFTs), such as those facilitated by LayerZero, aim to solve this by enabling native asset transfer with instant guaranteed finality <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. This means if an issuer has assets natively on multiple chains, OFTs allow direct movement of those assets between chains through the contract itself, eliminating the need for external bridging providers <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. This reduces the cost of moving assets (e.g., $100 million in Tether for the cost of gas, or a fraction of a penny) <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. This reduction in friction for inventory management increases capital efficiency, allowing for arbitrage across chains at sub-cent spreads and making markets more efficient <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.

### Parallel EVM
A significant bottleneck in existing Ethereum clients and other blockchains is state access <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>. The state database used by Ethereum clients (e.g., LevelDB for Go Ethereum) is inefficient, requiring many lookups to retrieve a single piece of state <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.

Monad addresses this by building a new custom database that:
1.  Natively stores Merkel tree data in a structure optimized for that data <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.
2.  Supports asynchronous reads and writes <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>. This enables parallel access to different regions of the Merkel tree, allowing multiple virtual machines to execute transactions and progress efficiently without blocking each other <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.

This [[startup_innovation_in_crypto | innovation]], rooted in benchmarking bottlenecks and engineering targeted solutions, enables super high throughput that can support new kinds of applications not possible elsewhere, such as fully on-chain order books for gaming or highly interactive social applications <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.# Real-World Problems Being Solved by Crypto

The crypto ecosystem aims to decentralize services and help the decentralized world supersede the centralized world <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This requires seamless interoperability between different ecosystems <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>, and a single interoperability layer is crucial for delivering the best user experience and powerful applications <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Core Philosophical Disruption

Early on, the appeal of crypto stemmed from a strong libertarian perspective, addressing perceived irresponsibility of banks and promoting self-sovereignty <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The fundamental thesis was that crypto would allow for permissionless access and full control over one's money <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

With the advent of programmable smart contracts (like Ethereum), the focus evolved to creating more interesting financial primitives and structures broadly useful to the world <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. The primary disruption remains in finance and money, which in turn unlocks numerous other empowering possibilities <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Addressing Financial Inefficiencies

### [[crypto_as_a_solution_for_high_credit_card_fees | Payments and High Credit Card Fees]]
In the Western world, credit card companies levy substantial fees (around 3%) on every transaction, which poses a significant cost to businesses, including small and large enterprises <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Crypto offers a solution where anyone with a phone can pay for a service directly, bypassing these middlemen <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

In the undeveloped world, where credit cards are less common, crypto (particularly Tether) is already widely used for payments <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. To effectively disrupt existing payment systems, crypto networks like Monad must be able to process transactions at a comparable scale, aiming for 10,000 transactions per second throughput <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The combined market capitalization of Visa and Mastercard, a trillion-dollar business, highlights the massive value extracted from businesses through these fees <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Personal Finance and DeFi
Crypto has significant [[potential_for_crypto_in_payments_and_gaming | potential in personal finance]], aiming to make decentralized finance (DeFi) the standard for banking, trading, borrowing, and lending <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

Key improvements needed include:
*   **Reducing Slippage**: Bringing slippage costs from frequently seen 1-5% in DeFi down to single-digit basis points <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This requires performant environments where market makers can quote tightly and reduce spreads, offering better execution for users <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Lowering Transaction Costs**: Current crypto transaction fees (e.g., $20 gas fees) are often considered normal but are a significant barrier for new users, especially those without large crypto holdings <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>. Networks like Solana demonstrate that actions can be almost free, allowing users to transact without worrying about a daily "action budget" <a class="yt-timestamp" data-t="00:49:21">[00:49:21]</a>. This high cost also affects developer habits, leading them to prioritize gas optimization over adding defensive assertions, which can lead to security issues and hacks <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.
*   **Eliminating Unnecessary Friction**: Traditional financial systems impose significant friction, such as high currency exchange fees at airports or ATM fees <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. With a crypto wallet on a phone, users could easily perform FX swaps for a fraction of the cost, leveraging a shared global state with high transaction execution <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This decentralized approach also protects against single entity failures or corruption <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

### [[cryptos_potential_in_identity_and_transaction_settlement | Identity, Community, and Transaction Settlement]]
Beyond payments and personal finance, crypto holds significant potential in:
*   **Identity**: Managing and verifying digital identities <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Community**: Facilitating new forms of decentralized communities and interactions <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **General Settlement**: Enabling more efficient settlement for all kinds of transactions, from stock trading to the transfer of real-world assets like houses or cars <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

## Technical Solutions Enabling Progress

### Omni Chain Fungible Tokens (OFTs)
Wrapped assets, commonly used in bridging, create a fundamental problem where the end-user holds an IOU that carries perpetual risk; their asset could become worthless at any time if the bridge is compromised <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This shifts risk from liquidity providers (LPs) to the end-user, a "really bad trade-off" <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

Omni Chain Fungible Tokens (OFTs), such as those facilitated by LayerZero, aim to solve this by enabling native asset transfer with instant guaranteed finality <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. This means if an issuer has assets natively on multiple chains, OFTs allow direct movement of those assets between chains through the contract itself, eliminating the need for external bridging providers <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. This reduces the cost of moving assets (e.g., $100 million in Tether for the cost of gas, or a fraction of a penny) <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. This reduction in friction for inventory management increases capital efficiency, allowing for arbitrage across chains at sub-cent spreads and making markets more efficient <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.

### Parallel EVM
A significant bottleneck in existing Ethereum clients and other blockchains is state access <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>. The state database used by Ethereum clients (e.g., LevelDB for Go Ethereum) is inefficient, requiring many lookups to retrieve a single piece of state <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.

Monad addresses this by building a new custom database that:
1.  Natively stores Merkel tree data in a structure optimized for that data <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.
2.  Supports asynchronous reads and writes <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>. This enables parallel access to different regions of the Merkel tree, allowing multiple virtual machines to execute transactions and progress efficiently without blocking each other <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.

This [[startup_innovation_in_crypto | innovation]], rooted in benchmarking bottlenecks and engineering targeted solutions, enables super high throughput that can support new kinds of applications not possible elsewhere, such as fully on-chain order books for gaming or highly interactive social applications <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.