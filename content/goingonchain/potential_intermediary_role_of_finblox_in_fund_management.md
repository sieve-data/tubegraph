---
title: Potential intermediary role of Finblox in fund management
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

Finblox recently reduced its withdrawal limits to a maximum of $500 per day and $1,500 per month, citing [[finblox_withdrawal_limitations_and_3ac_exposure | exposure to 3AC]] as the reason <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This situation prompted an in-depth [[onchain_analysis_of_finblox_wallets | on-chain analysis]] of Finblox's wallets, initially published as a Reddit post, to understand the platform's fund management practices and potential exposure <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## On-Chain Analysis Methodology

The analysis was performed by tracing transactions from personal deposit and withdrawal actions, a process made easier for those who funded Finblox from their own wallets (like Metamask) <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

### Identifying Wallets
*   **Deposit Wallet**: By checking the outflow of a user's unique Finblox deposit address, the primary "hot wallet" (ending in `fa-9e`) where all user deposits are aggregated was identified <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This wallet consolidates funds from individual unique user deposit addresses <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.
*   **Withdrawal Wallet**: Similarly, by tracing the inflow to a user's personal wallet after a withdrawal from Finblox, a distinct withdrawal wallet (ending in `d20`) was identified <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. This wallet primarily processes $500 daily withdrawals, confirming its role as the main withdrawal hub <a class="yt-timestamp" data-t="08:58:00">[08:58:58]</a>.
*   **Bitcoin (BTC) and Solana (SOL) Wallets**: For Bitcoin, Finblox appears to use a single wallet for both deposits and withdrawals <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. The same pattern was observed for Solana <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.

### Tools Used
The analysis utilized various blockchain explorers and tools to trace fund flows:
*   Bitquery.io <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>
*   DeBank.com <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>
*   Zapper.fi <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>
*   Aboard.finance <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>

## Finblox Fund Flow and Connections

The analysis revealed that Finblox primarily sends funds to other platforms rather than engaging in complex, proprietary yield-generating activities as it claimed ("eight sophisticated different yielding strategies") <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.

### Major Fund Destinations
Using a Senkey diagram, the largest outflows from Finblox's main deposit wallet (a9e) were identified <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **[[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]]**: A significant portion of funds, approximately $5.2 million USD value, was sent to a dedicated [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] deposit wallet used by the Finblox team <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **[[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]]**: Around $4.6 million USD value was transferred to two distinct [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] deposit wallets belonging to the Finblox team <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
    *   Intriguingly, these [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] wallets also received funding from other platforms like BlockFi and Nexo <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
    *   Transactions from Circle's treasury fund to these [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] accounts suggest they belong to an institutional entity, not an end-user <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

### Exposure to 3AC (Three Arrows Capital)
*   A specific wallet (ending in `914`) received approximately $3.2 million USD value from Finblox's deposit wallet <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   This `914` wallet was identified as a main wallet for [[finblox_withdrawal_limitations_and_3ac_exposure | Three Arrows Capital]] (3AC) <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
*   While this 3AC wallet received funds from various sources, including [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] and Compound, the timing of Finblox's transfers to 3AC is noteworthy <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
*   From November to January, transfers to 3AC were small, fixed amounts (e.g., $330k) <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>. However, starting May 13, 2022—the week UST began de-pegging—Finblox began sending "considerable" and "random" amounts (including Singapore dollars) to 3AC <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>.
*   These irregular transfers ceased around June 1, when rumors of 3AC's insolvency began circulating <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>. This suggests Finblox provided liquidity to 3AC during its crisis <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.

## Finblox's Intermediary Role

The analysis strongly suggests that Finblox acts primarily as an intermediary, relying on other platforms for yield generation <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>.
*   **Lack of Own Yield Strategy**: Unlike platforms like Nexo and Vault, which have their own products for borrowing, lending, and collateral, Finblox currently operates largely as a simple deposit application <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>. This contrasts with its claim of having "sophisticated different yielding strategies" <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.
*   **Stagnant BTC and SOL Funds**: The Bitcoin and Solana wallets show very little activity, with funds appearing to remain largely "idle" despite interest being offered on these assets <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.
*   **Funds to Competitors**: A significant portion of Finblox user funds was moved to competitor platforms like Nexo and BlockFi, as well as major exchanges like [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | Binance]] and [[connections_between_finblox_and_other_platforms_like_binance_and_ftx | FTX]] <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>. This raises questions about the value Finblox provides as a middleman, especially since users could deposit directly with Nexo or Vault to potentially avoid intermediary risks <a class="yt-timestamp" data-t="00:36:30">[00:36:30]</a>.

## Conclusion and Implications

The on-chain analysis indicates that Finblox's primary function might be as a gateway to other platforms for earning yield, rather than employing its own complex strategies <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.

Ultimately, of an estimated total of $25 million in end-user deposits, about $10 million was withdrawn, leaving $15-20 million to be provided to users <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. The estimated $3.2 million USD in exposure to [[finblox_withdrawal_limitations_and_3ac_exposure | Three Arrows Capital]] suggests that if no funds are recovered from 3AC, 10-30% of user deposits could be lost <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. The high [[finblox_stablecoin_interest_rates | stablecoin interest rates]] offered by Finblox were likely the primary draw for users <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>.

This type of [[onchain_analysis_of_finblox_wallets | on-chain analysis]] can be a valuable tool for users to independently verify the fund management practices of lending protocols before depositing their funds <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.