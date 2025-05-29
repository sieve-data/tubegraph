---
title: Analysis of Finbloxs deposit and withdrawal wallets
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

Finblox reduced its daily withdrawal limit to $500 and a maximum of $1,500 per month, citing exposure to [[Finblox_withdrawal_limitations_and_3AC_exposure | Three Arrows Capital (3AC)]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This has led to concerns among users, prompting an [[onchain_analysis_of_finblox_wallets | on-chain analysis]] of Finblox's wallets <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This analysis aimed to break down Finblox's deposit and withdrawal wallets and identify potential [[Finblox_withdrawal_limitations_and_3AC_exposure | 3AC exposure]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Identifying Finblox Wallets

To conduct this [[onchain_analysis_of_finblox_wallets | on-chain analysis]], a user initiated a deposit into Finblox from their MetaMask wallet <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### Deposit Wallet Discovery
Like other platforms such as [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] and [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]], Finblox creates a unique deposit address for each user <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. All funds deposited into this unique address are considered a user's deposit <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. However, Finblox consolidates these funds from individual unique addresses into a main hot wallet <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

The main deposit wallet (address ending in `fa9e`) was identified by:
1.  Accessing the outflow transactions from the user's unique Finblox deposit address <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
2.  Observing that all funds were consistently sent to this one particular address (the `fa9e` address) on the receiver side <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  Confirming with other Finblox users that their deposits also followed this path <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

This `fa9e` wallet showed significant inflows (e.g., over 27 million USDC) and outflows (e.g., 21 million USDC) over a two-year period, indicating it functions as a central hub <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. At one point, it held around 6 million USDC <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Withdrawal Wallet Discovery
While some platforms use the same wallet for deposits and withdrawals, Finblox appears to separate them for easier and safer management <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The withdrawal wallet (address ending in `d20`) was identified by:
1.  Initiating a withdrawal from Finblox to a personal wallet (e.g., MetaMask) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
2.  Checking the inflow transactions of the personal wallet <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
3.  Noting the specific address from which the withdrawal originated (the `d20` address) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
4.  Confirming this by observing continuous $500 value withdrawals from this wallet, consistent with Finblox's daily withdrawal limit <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

For Bitcoin (BTC), Finblox appears to use a single wallet for both deposits and withdrawals <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.

## Tools Used for Analysis
The following tools were used for the [[onchain_analysis_of_finblox_wallets | on-chain analysis]]:
*   **Bitquery.io**: A useful website for checking transaction IDs, inflow/outflow, and money flow (Sankey diagrams) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **DeBank.com**: Preferred for quick overviews of funding in a wallet <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Zapper.fi**: Another option for checking wallet contents <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Aboard.finance**: Also used for wallet analysis <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Firewallet.com**: Specifically mentioned for showing the net change of a wallet's value for Bitcoin <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.
*   **Etherscan.io**: Used to investigate individual transactions and trace origins <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

## Wallet Contents and Fund Flows

### Ethereum-based Tokens (USDC, USDT, ETH, AVAX)
The main deposit wallet (an Ethereum-based wallet) primarily holds tokens related to Ethereum Layer 2 chains, such as Avalanche (AVAX), USD Coin (USDC), and Tether (USDT) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. The analysis focused on USDC as it appeared to be the most common deposit <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

As of the analysis, the main deposit wallet held about $9.4 million USD value <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

### Bitcoin Wallet
Finblox's Bitcoin wallet had approximately 1.19 BTC, equivalent to about $25,000, which is considered a small amount <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>. The maximum amount ever held in this wallet was 4.8 BTC <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. Inflows and outflows for Bitcoin were consistently small amounts, suggesting the Bitcoin was largely idle <a class="yt-timestamp" data-t="00:32:43">[00:32:43]</a>, <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>. There was no indication of connection to a large platform for Bitcoin yielding, despite Finblox offering 5.5% to 5.75% APY on BTC <a class="yt-timestamp" data-t="00:33:28">[00:33:28]</a>, <a class="yt-timestamp" data-t="00:35:14">[00:35:14]</a>.

### Solana Wallet
A brief analysis of Finblox's Solana wallet showed similar behavior, indicating a separation of funds by token type <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>, <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>.

## Outflow Analysis and Connections

By tracing the outflow from Finblox's main deposit wallet using Sankey diagrams, the analysis revealed where user funds were being sent:

### Binance Connection
A significant portion of funds (around 5.2 million USD value) from Finblox's deposit wallet went to a specific wallet ending in `fe6` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>, <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. Further tracing revealed that this `fe6` wallet consistently sent funds to a well-known [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] hot wallet (labeled "Binance Hot Wallet Number 14") <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. This suggests that the `fe6` wallet acts as Finblox's internal deposit wallet for [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

### FTX Connection and Beyond
Two other significant addresses (ending in `a6` and `dd`) received funds from Finblox's deposit wallet <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. These addresses, although empty, showed typical behavior of deposit wallets <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Their outflow consistently went to a well-known [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] wallet <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. These are believed to be Finblox's deposit wallets with [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

Interestingly, these [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] deposit wallets for Finblox also received funds from other platforms:
*   **[[potential_intermediary_role_of_finblox_in_fund_management | BlockFi]]**: Funds were observed coming into Finblox's [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] deposit wallets from a main wallet believed to belong to [[potential_intermediary_role_of_finblox_in_fund_management | BlockFi]] <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
*   **[[potential_intermediary_role_of_finblox_in_fund_management | Nexo]]**: Similarly, a large wallet associated with the [[potential_intermediary_role_of_finblox_in_fund_management | Nexo]] platform was seen providing funds to Finblox's [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] deposit wallets <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.
*   **Circle Treasury**: One of Finblox's [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] deposit wallets received 100,000 USDC directly from the Circle Treasury Fund, which is typically only accessible to enterprise-level organizations <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>, <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. This reinforces that these are not merely end-user accounts <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

It is most probable that Finblox provided user funds to [[potential_intermediary_role_of_finblox_in_fund_management | BlockFi]] and [[potential_intermediary_role_of_finblox_in_fund_management | Nexo]] via their [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] accounts <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

### Three Arrows Capital (3AC) Exposure
An address ending in `914` received approximately 3.2 million USDC value (including Singapore dollars and Ethereum) from Finblox's deposit wallet <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>, <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. This `914` wallet did not behave like a typical deposit wallet (it held residual funds and engaged in DeFi transactions), suggesting it was not an exchange's deposit wallet <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

Upon searching, the `914` wallet was found to send significant funding to a publicly known main wallet of [[Finblox_withdrawal_limitations_and_3AC_exposure | Three Arrows Capital]] <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>. This specific wallet received about 8 million USDC from `914` <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>. However, not all of this 8 million came from Finblox; it also received funding from [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] Exchange and a Compound USD pool <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.

Historically, Finblox made small, fixed transfers (e.g., 330k and 200k) to [[Finblox_withdrawal_limitations_and_3AC_exposure | 3AC]] in late 2021 <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>. However, starting around May 13th, the week when UST stablecoin began to de-peg heavily, Finblox began sending significant and random amounts of various tokens (including USDC and Singapore dollars) to the [[Finblox_withdrawal_limitations_and_3AC_exposure | 3AC]] wallet <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>, <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>, <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>. The last transaction occurred on June 1st, coinciding with early rumors of [[Finblox_withdrawal_limitations_and_3AC_exposure | 3AC]]'s insolvency <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>, <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.

This pattern suggests that [[Finblox_withdrawal_limitations_and_3AC_exposure | 3AC]] may have urgently requested funds from Finblox during their financial distress <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>. Finblox's direct loss to [[Finblox_withdrawal_limitations_and_3AC_exposure | 3AC]] is estimated at 3.1 to 3.2 million USD <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>, <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>. This amount could be higher if [[Finblox_withdrawal_limitations_and_3AC_exposure | 3AC]] also received funds from Finblox's [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] or [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] accounts <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>.

## Conclusions and Implications

### Finblox as an Intermediary
Finblox claimed to separate funds with "eight sophisticated different yielding strategies" <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>, but the [[onchain_analysis_of_finblox_wallets | on-chain analysis]] suggests otherwise <a class="yt-timestamp" data-t="00:34:11">[00:34:11]</a>. Most funds were sent to Finblox's own "vault" address (approx. 10 million USD), [[potential_intermediary_role_of_finblox_in_fund_management | Nexo]], [[potential_intermediary_role_of_finblox_in_fund_management | BlockFi]], [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] Exchange, and [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. Placing funds on exchanges like [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] and [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] to earn interest is not considered a "sophisticated" strategy, as users can do this themselves <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.

The analysis strongly suggests that Finblox acted more as an [[potential_intermediary_role_of_finblox_in_fund_management | intermediary]], leveraging other platforms like [[potential_intermediary_role_of_finblox_in_fund_management | Nexo]] and "vault" to generate yield <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>, <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>. These platforms have their own money-making strategies (borrowing, lending, collateral), while Finblox's app is primarily for deposits <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.

If users had directly deposited their funds with [[potential_intermediary_role_of_finblox_in_fund_management | Nexo]] or "vault," they might have avoided current liquidity issues with Finblox, as those platforms did not have limited withdrawals at the time of the analysis <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.

### Estimated Losses and User Deposits
Total end-user deposits into Finblox were estimated around $25 million <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>. Around $10 million has been withdrawn <a class="yt-timestamp" data-t="00:37:36">[00:37:36]</a>, leaving $15-20 million to be provided to users <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>. If the estimated 3.2 million USD lost to [[Finblox_withdrawal_limitations_and_3AC_exposure | Three Arrows Capital]] is unrecoverable, then between 10% and 30% of user deposits could be lost <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>. Stablecoins, particularly USDC on the Ethereum chain, accounted for most of the deposits due to attractive [[Finblox_stablecoin_interest_rates | interest rates]] <a class="yt-timestamp" data-t="00:38:20">[00:38:20]</a>, <a class="yt-timestamp" data-t="00:38:37">[00:38:37]</a>.

### Lessons for [[platform_risk_and_security_concerns_with_finblox | Platform Risk]]
This [[onchain_analysis_of_finblox_wallets | on-chain analysis]] technique can be useful for future users considering depositing funds into yield-bearing protocols <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>. By examining deposit and withdrawal wallets, one can determine if a platform genuinely employs unique strategies or merely acts as an intermediary, moving funds to competitors <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>, <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>.