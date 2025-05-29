---
title: Use of deposit and withdrawal wallets
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

When engaging with crypto platforms like Finblox, understanding how they manage user funds through deposit and withdrawal wallets is crucial for assessing risk and transparency. On-chain analysis allows users to trace the flow of funds and gain insights into a platform's operations and potential exposures <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## How Deposit Wallets Work

Crypto platforms utilize a specific system for handling incoming user funds:
*   **Unique User Addresses** Each user receives a unique deposit address when they [[using_and_storing_in_noncustodial_wallets | deposit]] funds into a platform <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a> <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This unique address allows the platform to recognize that the incoming funds belong to a specific user <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
*   **Consolidation to a Main Hot Wallet** It is impractical for a platform to manage millions of individual user wallets <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Therefore, funds deposited to unique user addresses are typically forwarded, often within minutes, to a central "main hot wallet" belonging to the platform <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a> <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a> <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

### Identifying a Deposit Wallet
Users can identify a platform's main deposit wallet by:
1.  **Tracking Personal Transactions** Go to your own transaction history on the blockchain explorer (e.g., from your [[using_and_storing_in_noncustodial_wallets | MetaMask wallet]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>) and look at the outflow from your unique deposit address on the platform <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
2.  **Identifying the Receiver** The address that consistently receives funds from multiple unique user deposit addresses is likely the platform's main hot wallet <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a> <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. For Finblox, the address ending in `a9e` was identified as the main deposit wallet <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
3.  **Observing Inflow/Outflow** A main deposit wallet will show significant inflows from numerous addresses and substantial outflows as funds are moved elsewhere <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## How Withdrawal Wallets Work

Platforms generally separate withdrawal wallets from deposit wallets for better management and [[security_features_of_crypto_wallets | security]] <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Identifying a Withdrawal Wallet
To find a platform's withdrawal wallet:
1.  **Track Your Withdrawal** Initiate a withdrawal from the platform to your personal crypto wallet (e.g., [[using_and_storing_in_noncustodial_wallets | MetaMask wallet]]) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
2.  **Check Inflow** Go to your personal wallet's inflow history on a blockchain explorer <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. The address from which your withdrawal originated is likely the platform's withdrawal wallet <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. For Finblox, the address ending in `d20` was identified as the withdrawal wallet for Ethereum-based tokens <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
3.  **Verify Consistent Outflows** A withdrawal wallet will show consistent, often capped, outflow transactions (e.g., Finblox's daily limit of $500 USD value) <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a> <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

*Note:* Some platforms might use the same wallet for both deposits and withdrawals for certain cryptocurrencies, like Finblox did for Bitcoin (BTC) <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a> <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>.

## Analyzing Wallet Activity

On-chain analysis tools allow users to track the movement of funds from these main wallets to other destinations.

### Tools for Analysis
Useful tools for analyzing wallet activity include:
*   Bitquery.io <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>
*   Dbank.com <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a> <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>
*   Zapper.fi <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a> <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>
*   Abord.finance <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>

These platforms provide quick overviews of funding in a wallet, including current balances and historical inflows/outflows <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Ensure to adjust the date range to see the full history <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Visualizing Money Flow with Sankey Diagram
Bitquery.io's "money flow" feature and Sankey diagram visualization are particularly useful for understanding where funds are sent from a main wallet <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a> <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. This helps identify the largest recipients of funds <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### Identifying Wallet Ownership and Purpose
By tracking where funds go, one can identify other platforms or entities involved:
*   **Exchange Hot Wallets** Funds often move to hot wallets of major exchanges like Binance or FTX, indicating that the platform uses these exchanges <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a> <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. These are often labeled or easily identifiable by large, straightforward flows <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   **Competitor Platforms** Discovering funds being sent to competitors like Nexo or BlockFi suggests that the platform might be leveraging other services for yield generation <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a> <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a> <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
*   **Treasury Funds** Inflows from entities like the Circle Treasury (which creates new USDC from fresh fiat deposits) indicate that the receiving wallet belongs to a large, enterprise-level organization, not an end-user <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a> <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
*   **DeFi Applications** Funds found in Decentralized Finance (DeFi) applications like Banker Joe or M Stable suggest engagement with various DeFi strategies <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.
*   **Known Counterparties** Funds sent to wallets publicly known to belong to specific entities, like Three Arrows Capital (3AC), reveal direct financial exposure <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

### Detecting Suspicious Activity
Irregular or random transfers to a known counterparty, especially during times of market stress (e.g., during UST de-pegging), can indicate that a platform is attempting to shore up a struggling entity or is suffering from liquidity issues <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a> <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>. Stopping such transfers when rumors of insolvency emerge further supports this <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a> <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.

## Case Study: Finblox's Wallet Analysis

Finblox's recent withdrawal limitations due to exposure to Three Arrows Capital (3AC) prompted an in-depth on-chain analysis of its wallets <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Finblox's Wallet Structure
*   **Main Deposit Wallet (Ethereum/ERC-20)**: Identified as `a9e` <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Held mostly USDC and other ERC-20 tokens, with significant inflow/outflow <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Main Withdrawal Wallet (Ethereum/ERC-20)**: Identified as `d20` <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. Showed consistent, capped withdrawals of $500 USD value <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Bitcoin Wallet**: A single wallet was used for both Bitcoin deposits and withdrawals <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a> <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>. This wallet appeared largely idle, with small inflows and outflows, despite Finblox offering interest on BTC <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a> <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>.

### Where Finblox Sent Funds
Analysis revealed Finblox's funds were primarily sent to:
*   **Binance** <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a> <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>
*   **FTX** (two main deposit accounts) <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a> <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>
*   **Nexo** <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a> <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>
*   **BlockFi** <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a> <a class="yt-timestamp" data-t="00:34:44">[00:34:44]</a>
*   **Vault** (their personal vault address) <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>

This suggests Finblox was primarily acting as an "intermediary," sending user funds to other platforms and competitors rather than employing sophisticated, in-house yield strategies <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a> <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a> <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.

### Exposure to Three Arrows Capital (3AC)
*   **Estimated Exposure** Finblox transferred an estimated 3.2 million USD in value (USDC, Singapore dollars, Ethereum) to a specific 3AC wallet (ending in `914`) <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a> <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a> <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.
*   **Timing of Transfers** While there were small, fixed transfers to 3AC last year <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a> <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>, a significant shift occurred starting May 13th, 2022, the week UST began de-pegging <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a> <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. Finblox began sending considerable and random amounts, including Singapore dollars, to 3AC <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a> <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a> <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.
*   **Cessation of Transfers** Transfers ceased around June 1st, 2022, when rumors of 3AC's insolvency began circulating <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a> <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a> <a class="yt-timestamp" data-t="00:40:27">[00:40:27]</a>.

This pattern suggests Finblox was pressured to send funds to 3AC during their crisis <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a> <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>, leading to an estimated 10-30% loss of user deposits if these funds are not recovered <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a> <a class="yt-timestamp" data-t="00:38:11">[00:38:11]</a>.

## Key Takeaways for Users

*   **Due Diligence is Crucial** Before depositing money into a new platform, especially smaller ones, conduct your own on-chain analysis to understand where your funds are going <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a> <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>.
*   **Intermediary vs. Yield Strategy** Determine if a platform has its own sophisticated yield-earning strategies or if it merely acts as an intermediary, moving funds to other platforms <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a> <a class="yt-timestamp" data-t="00:40:44">[00:40:44]</a>. If it's the latter, consider depositing directly with the underlying platforms to potentially mitigate risk <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a> <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>.
*   **Diversify Funds** As always, diversify your investments across multiple platforms to minimize risk exposure <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.