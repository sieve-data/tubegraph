---
title: Onchain analysis of Finblox wallets
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

Recent events have brought Finblox's operations under scrutiny, particularly after the platform reduced its daily withdrawal limits to $500 and a maximum of $1,500 per month <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This measure was attributed to [[finblox_withdrawal_limitations_and_3ac_exposure | Finblox's exposure to Three Arrows Capital (3AC)]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. A comprehensive [[analysis_of_finbloxs_deposit_and_withdrawal_wallets | on-chain analysis of Finblox's wallets]], detailed in a Reddit post by a user (referred to as Ian), sheds light on the platform's fund movements and connections <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Methodology of On-Chain Analysis

The analysis began by examining personal transactions, specifically withdrawals made before Finblox imposed its limits <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. By observing transaction IDs from personal wallets (e.g., MetaMask) or exchanges like Binance, it's possible to trace where funds are sent <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

Key steps in the analysis include:
*   **Identifying Unique Deposit Addresses:** Finblox, like other platforms such as [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] and [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]], creates a unique deposit address for each user <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Funds deposited to these unique addresses are then forwarded to a main "hot wallet" <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Tracing Funds to Main Wallets:** By analyzing the outflow from personal deposit addresses on block explorers like bitquery.io, the primary Finblox hot wallet (ending in 'a9e') was identified as the recipient of most user deposits <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Identifying Withdrawal Wallets:** Similarly, by checking the inflow to a personal wallet after a withdrawal from Finblox, the source address was identified as Finblox's main withdrawal wallet (ending in 'd20') <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This wallet consistently shows outflows of 500 USDC, aligning with the daily withdrawal limit <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Assessing Wallet Balances:** Tools like debank.com, zapper.fi, and a board.finance were used to get a quick overview of the funds held in these identified wallets <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Using Sankey Diagrams:** Bitquery.io's money flow (Sankey) diagram feature was crucial for visualizing where the largest amounts of funds were being sent from the main Finblox deposit wallet <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

## Key Findings and Fund Flows

### Main Wallets
*   **Deposit Wallet (a9e):** Identified as the primary hot wallet for incoming funds. It has seen significant inflow (over 27 million USDC) and outflow (21 million USDC) over two years <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a> <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Withdrawal Wallet (d20):** Dedicated to processing user withdrawals, evidenced by continuous 500 USD value outflows <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a> <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Bitcoin Wallet:** Unlike Ethereum-based tokens, Finblox appears to use a single wallet for both Bitcoin deposits and withdrawals <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. This wallet holds a relatively small amount of Bitcoin (1.19 BTC, equivalent to ~25K USD), and movements suggest it's primarily used for end-user transactions rather than sophisticated yield strategies <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a> <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

### Destinations of Finblox Funds
The analysis revealed that Finblox primarily moves its users' funds to a few key destinations, mostly on the Ethereum Layer 2 chain, with USDC being the predominant stablecoin <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a> <a class="yt-timestamp" data-t="00:38:37">[00:38:37]</a>.

*   **Binance:** A significant portion of Finblox's funds, estimated around 5.2 million USD value, was sent to Binance hot wallets <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a> <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. This suggests Finblox uses [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] as a deposit exchange for its own team.
*   **FTX:** Approximately 4.6 million USD value was transferred to two distinct [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] deposit wallets <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a> <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. Intriguingly, these [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] wallets also received funds from other platforms like BlockFi and Nexo <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a> <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>. One of these FTX wallets received a 100,000 USDC transfer directly from a Circle Treasury fund, implying an institutional connection rather than an end-user <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a> <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. This leads to the assumption that Finblox might be providing user funds to BlockFi and Nexo <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.
*   **Three Arrows Capital (3AC):**
    *   A specific wallet (ending in '914') received 3.2 million USD value in USDC from Finblox's deposit wallet <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a> <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.
    *   This '914' wallet then sent 8 million USDC to a known 3AC main wallet <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
    *   Historically, Finblox made small, fixed transfers to 3AC in late 2021 <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>.
    *   However, starting May 13th, 2022, around the time UST began de-pegging, Finblox began sending significant and often random amounts (including odd cents and Singapore dollars) to 3AC <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a> <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>.
    *   These transfers ceased around June 1st, 2022, when rumors of 3AC's insolvency began to circulate <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a> <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.
    *   The total direct exposure to 3AC is estimated at 3.2 million USD, though indirect exposure through other exchanges might increase this figure <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a> <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>. If this amount is completely lost, it could represent 10-30% of Finblox's total user deposits <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a> <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

## Implications for Finblox's Operations

The [[potential_intermediary_role_of_finblox_in_fund_management | analysis suggests Finblox may act primarily as an intermediary platform]] <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>. While Finblox offers attractive [[finblox_stablecoin_interest_rates | stablecoin interest rates]] (previously 15% and 12%) <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>, it appears they leverage other platforms like Nexo and Vault (not explicitly identified in the transcript but mentioned as a main receiver of funds from Finblox) to generate yield <a class="yt-timestamp" data-t="00:35:28">[00:35:28]</a> <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.

This implies that Finblox may not have its own sophisticated yielding strategies <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a> <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>. If users had directly invested in platforms like Nexo or Vault, they might have avoided the current [[platform_risk_and_security_concerns_with_finblox | Finblox platform risk and security concerns]] and withdrawal limitations, as these platforms did not have similar restrictions at the time of the analysis <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a> <a class="yt-timestamp" data-t="00:36:57">[00:36:57]</a>.

### Total Funds and Withdrawals
Approximately 25 million USD in end-user deposits were identified across Finblox's wallets <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>. Around 10 million USD had already been withdrawn from the withdrawal wallet prior to the analysis <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a> <a class="yt-timestamp" data-t="00:37:36">[00:37:36]</a>.

## Conclusion

This on-chain analysis provides valuable insights into Finblox's operational strategies, revealing its reliance on other platforms for yield generation and its significant exposure to 3AC. Such techniques can be crucial for users to assess [[platform_risk_and_security_concerns_with_finblox | platform risk and security concerns]] before depositing funds into yield-bearing protocols <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a> <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>.