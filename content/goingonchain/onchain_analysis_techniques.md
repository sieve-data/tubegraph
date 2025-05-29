---
title: Onchain analysis techniques
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

On-chain analysis involves examining blockchain transactions to gain insights into the movement of funds and the financial health of crypto platforms. This article details the techniques used by a Reddit user to conduct a thorough analysis of Finblox's wallets following their decision to reduce withdrawals due to exposure to Three Arrow Capital (3AC) <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Motivation for On-Chain Analysis

The analysis began out of personal concern, as the individual had funds with Finblox and practices diversification across numerous platforms, similar to [[Blockchain fundamentals | traditional risk management]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Rumors regarding the insolvency of [[Coordinated attack on stablecoins | Three Arrow Capital]] (3AC), closely related to Finblox, prompted an attempted withdrawal before the platform limited daily withdrawals to $500 <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This situation highlighted the need to understand where funds were being moved on-chain.

## Identifying Wallets

The first step in an [[Onchain analysis techniques | on-chain analysis]] is to identify the relevant wallet addresses of the platform being investigated.

### Deposit Wallets
Platforms like Finblox, FTX, Binance, and Celsius create a unique deposit address for each user <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Funds deposited to these unique addresses are then typically consolidated into a main "hot wallet" or internal address <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

To find the main deposit wallet:
1.  **Initiate a deposit:** Deposit funds to the platform <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
2.  **Obtain Transaction ID:** Retrieve the transaction ID from your exchange or personal wallet (e.g., MetaMask) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
3.  **Trace the transaction:** Use a blockchain explorer (like Bitquery.io) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> to follow the transaction's outflow from your unique deposit address. The receiver of these funds, especially if it's a consistent address for many users, is likely the platform's main deposit wallet (e.g., Finblox's `fa-9e` wallet) <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Withdrawal Wallets
While a deposit wallet might also be used for withdrawals, many platforms separate them for better management and security <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

To find the withdrawal wallet:
1.  **Initiate a withdrawal:** Withdraw funds from the platform (e.g., $500 daily cap from Finblox) <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
2.  **Trace the inflow:** Go to your receiving wallet (e.g., MetaMask) <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a> and check the inflow. The address from which the funds originate is likely the platform's main withdrawal wallet (e.g., Finblox's `d20` address) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
3.  **Confirm consistency:** Observe if all withdrawal transactions, especially those at the daily limit, consistently come from this address <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

> [!NOTE] Bitcoin and Solana wallets for Finblox appeared to use a single wallet for both deposits and withdrawals, which remained largely idle, indicating no active yielding strategy for these assets <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.

## On-Chain Analysis Tools

Several tools are essential for tracing and visualizing fund movements:

*   **Bitquery.io**: Considered "beautiful" and easier than others for this kind of research <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Useful for viewing inflow and outflow for specific addresses and creating "Sankey diagrams" for visualizing money flow <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Dbank.com, Zapper.fi, Zerion.xyz**: These are top tools for quickly assessing the total value of funds within a wallet across various chains (e.g., Ethereum, Avalanche) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Firewaller.com**: Specifically useful for Bitcoin wallets to see the net change and maximum historical balance of a wallet <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.

> [!NOTE] When using these explorers, remember to adjust the date range to "all time" or a sufficiently long period (e.g., two years) to capture all historical transactions <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

## Tracing Fund Movements and Identifying Counterparties

Once the main wallets are identified, the next step is to analyze their outflows to determine where the funds are being sent.

1.  **Analyze Large Transactions:** Look for large transaction values in the outflow of the main deposit wallet <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
2.  **Use Sankey Diagrams:** Bitquery.io's money flow feature and Sankey diagrams help visualize where the largest amounts of funds are moving from a given wallet <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. This helps prioritize which recipient addresses to investigate first (e.g., identifying Binance's hot wallet as a major recipient) <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
3.  **Identify Exchange Wallets:** By tracing funds to well-known hot wallets of major exchanges (e.g., Binance, FTX), one can identify the platform's deposit wallets with those exchanges <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
4.  **Investigate Unusual Inflows:** Check the inflow of these identified exchange deposit wallets. If funds are coming from unexpected sources (e.g., BlockFi, Nexo, or Circle treasury fund), it suggests deeper connections <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. For instance, funds from Circle Treasury indicate an institutional, not an end-user, transaction <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
5.  **Google Wallet Addresses:** A simple but effective method is to Google suspicious or unknown wallet addresses. This can directly link an address to a known entity, such as [[Coordinated attack on stablecoins | Three Arrow Capital]]'s main wallet <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.

## Key Findings from Finblox Analysis

Using these [[Onchain analysis techniques | on-chain analysis techniques]], several critical observations were made regarding Finblox:

*   **Fund Allocation:** Most Finblox funds (especially USDC) were on Ethereum layer-2 chains <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Intermediary Role:** Finblox appears to act primarily as an intermediary, moving funds to other platforms like Binance, FTX, Nexo, and BlockFi, as well as holding some in their own "vault" <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>. This suggests they may not have their own sophisticated yield generation strategies <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.
*   **Exposure to 3AC:**
    *   A significant amount (3.2 million USDC value) was sent from Finblox's deposit wallet to a particular address that, upon investigation, was found to be directly linked to [[Coordinated attack on stablecoins | Three Arrow Capital]] <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.
    *   Initially, transfers to 3AC were small and fixed <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>.
    *   However, starting May 13th, the week UST (TerraUSD) began to depeg, Finblox started sending "random" and "considerable amounts" to 3AC, including various tokens like Singapore Dollars <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. This suggests 3AC was urgently calling for funds during the crisis <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.
    *   These transfers stopped around June 1st, when rumors about 3AC's insolvency began to circulate <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>.
*   **Estimated Losses:** If the 3.2 million from 3AC is completely lost, it could account for 10-30% of Finblox user deposits <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.
*   **No Yielding Strategy for BTC/SOL:** For Bitcoin and Solana, the analysis indicated the funds remained largely idle in a single wallet, not being moved to other platforms for yielding strategies <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>.

## Benefits of On-Chain Analysis

This analysis demonstrates the power of [[Onchain analysis techniques | on-chain analysis]] in understanding the operations and risks of cryptocurrency platforms:

*   **Transparency:** Allows users to independently verify how platforms manage their funds <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.
*   **Risk Assessment:** Reveals potential exposure to distressed entities (e.g., 3AC) or risky practices (e.g., acting as a mere intermediary without proprietary yield strategies) <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.
*   **Due Diligence:** Enables users to perform their own due diligence before investing in new lending protocols <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>. It can help assess if a platform truly offers "sophisticated different yielding strategies" or just moves funds to other, more established entities <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.
*   **Informed Decisions:** Helps users decide if it's better to directly use established platforms (like Nexo or Vault) rather than relying on intermediaries that may introduce additional layers of risk <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>.

> [!WARNING] This kind of analysis could have been done before investing, as Finblox's wallet behavior remained consistent for over six months <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.