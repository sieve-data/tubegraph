---
title: Exposure of Finblox to 3AC
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

Finblox, a cryptocurrency platform, reduced its withdrawal limits to $500 per day and a maximum of $1,500 per month due to cited exposure to Three Arrows Capital (3AC) <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Following this announcement, a Reddit user conducted a thorough on-chain analysis of Finblox's wallets to determine the extent of this exposure <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Wallet Analysis Methodology

The analysis began by tracing individual user deposits and withdrawals to identify Finblox's main operational wallets <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. The tools used for this research included Bitquery.io <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, Zapper.fi <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>, Abord.finance <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>, and DeBank.com <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

### Identifying the Deposit Wallet
Platforms like Finblox create a unique deposit address for each user <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Funds deposited into these unique addresses are then almost immediately forwarded to a central "hot wallet" belonging to the platform <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>, <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. By examining the outflow of personal deposit transactions, the main Finblox deposit wallet (ending in "a9e") was identified <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>, <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. This wallet showed significant inflow and outflow of funds, indicating it was a primary holding wallet for Finblox's Ethereum Layer 2 chain tokens, particularly USDC <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### Identifying the Withdrawal Wallet
Similarly, by initiating a withdrawal from Finblox to a personal wallet (e.g., MetaMask) and then checking the inflow of that personal wallet, the source of the withdrawal was traced back to Finblox's main withdrawal wallet (ending in "d20") <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This wallet consistently showed outflows matching the daily withdrawal limit of $500, confirming its function <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### Analyzing Money Flow with Sankey Diagrams
To understand where Finblox's funds were being sent, the "money flow" feature and Sankey diagrams on Bitquery.io were utilized <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. This allowed the analyst to visualize the largest outflows from the main deposit wallet <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

## Tracing Funds to 3AC

Through the Sankey diagram analysis, several major outflow addresses were identified from Finblox's deposit wallet <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. One significant recipient, receiving 3.2 million USDC value from Finblox's deposit wallet, was an address ending in "914" <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.

Upon further investigation of the "914" wallet's outflows, a primary recipient wallet was discovered <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. Googling this recipient wallet immediately revealed it to be a main wallet of Three Arrows Capital (3AC) <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.

### Estimated Exposure
The analysis showed that approximately 3.2 million USDC value, including stablecoins and some Ethereum, was sent from the Finblox deposit wallet to the 914 address, which then transferred funds to 3AC <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>, <a class="yt-timestamp" data-t="00:25:59">[00:25:59]</a>. While the 914 wallet also received funds from other sources like FTX Exchange and Compound, the direct Finblox contribution to this 3AC-linked wallet was 3.2 million <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>, <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.

### Timeline of Transfers
The transfer patterns from Finblox to the 3AC-linked wallet revealed a critical timeline:
*   **Late 2021**: Initial transfers from Finblox to 3AC were small, fixed amounts, not appearing suspicious <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>.
*   **May 13, 2022 onwards**: Starting around May 13, 2022, when UST began de-pegging, the Finblox team started sending "considerable" and "random" amounts of funds to the 3AC-linked wallet <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>, <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. This included not only USDC but also Singapore Dollars, indicating a desperate need for funds from 3AC <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.
*   **June 1, 2022**: The last transaction to this 3AC-linked wallet occurred around June 1, 2022, which coincided with the first rumors of 3AC's potential insolvency <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>, <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>. This suggests Finblox ceased lending to 3AC once the financial troubles became public <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.

## Finblox as an Intermediary
The analysis indicated that Finblox did not primarily use its own sophisticated yield-generating strategies <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>, <a class="yt-timestamp" data-t="00:40:17">[00:40:17]</a>. Instead, a significant portion of user funds was transferred to other large platforms and exchanges, including:
*   Binance: Approximately 5.2 million USD value went to Binance's hot wallet <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>, <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   FTX: Two Finblox deposit accounts on FTX received funds, and these accounts also received funds from BlockFi and Nexo <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>, <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. The analyst concluded that Finblox likely provided user funds to BlockFi and Nexo <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.
*   Vault and Nexo: These platforms were identified as the main receivers of Finblox user funds <a class="yt-timestamp" data-t="00:35:28">[00:35:28]</a>.

This suggests that Finblox may have acted as an intermediary, sending user funds to other platforms that actually generated yield <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>, <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>. Users might have been safer directly depositing their funds with Nexo or Vault, as these platforms did not have the same [[finblox_funds_withdrawal_limitations | withdrawal limitations]] at the time of the analysis <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>. The Bitcoin (BTC) and Solana (SOL) wallets of Finblox appeared mostly stagnant, showing little activity beyond user deposits and withdrawals, suggesting they were not actively used for yielding strategies <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>, <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>.

## Estimated Impact and Recovery
The total end-user deposits on Finblox were estimated to be around 25 million USD <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>. Approximately 10 million USD had been withdrawn from the withdrawal wallet <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>, leaving 15-20 million USD that Finblox needed to provide to users <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.

Assuming the entire 3.2 million USD exposed to 3AC is unrecoverable, this would represent a loss of between 10% and 30% of user deposits <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>, <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. The majority of deposits were in stablecoins, particularly USDC on the Ethereum chain, due to attractive interest rates offered by [[finblox_platform_features | Finblox platform features]] <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>, <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>.

This on-chain analysis technique can be useful for users to investigate landing protocols before depositing funds, to understand where their money is actually going and if the platform is truly implementing sophisticated yielding techniques <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>, <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>.