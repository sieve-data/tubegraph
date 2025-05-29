---
title: Finblox funds withdrawal limitations
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

Finblox implemented withdrawal reductions, citing exposure to Three Arrows Capital (3AC) <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Withdrawals were reduced to a daily maximum of $500 USD and a monthly maximum of $1,500 USD <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This decision was made on June 16, following rumors about 3AC becoming insolvent <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

An in-depth analysis of Finblox's wallets was conducted by a Reddit user, detailing the platform's [[use_of_deposit_and_withdrawal_wallets | deposit and withdrawal wallets]] and potential exposure to 3AC <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The analysis, while based on estimates, was considered impressive given the analyst's stated lack of prior experience <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Analysis Methodology

The analysis began by examining personal transactions, as most exchanges provide a transaction ID that can reveal the origin and destination of funds <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. For instance, if funds came from Binance, it would show as originating from a Binance hold wallet going to a specific Finblox address <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. MetaMask wallet users could directly check their transaction history <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### Identifying Deposit Wallets

Finblox, like other platforms (FTX, Binance, Celsius), creates a unique deposit address for each user <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. However, to manage funds efficiently, they consolidate deposits from these unique addresses into a main "hot wallet" <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

To identify Finblox's main deposit wallet (an address ending in `fa-9e`), the analyst traced the outflow from their personal Finblox deposit address <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. Using blockchain explorers like Bitquery.io, the receiver address of these outflows was identified <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This central address receives funds from numerous user addresses, indicating it as the main deposit wallet <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

At one point, the deposit wallet held approximately 9.4 million USD, primarily in ERC-20 tokens like USDC, which seemed to be the most popular asset due to attractive interest rates (initially 15%, then 12%) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

### Identifying Withdrawal Wallets

While some platforms use the same wallet for deposits and withdrawals, Finblox appears to separate them for better management and safety <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The withdrawal wallet (an address ending in `d20`) was identified by tracing incoming transactions to a personal MetaMask wallet after initiating a withdrawal <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

The inflow to the personal wallet would show the sender as Finblox's withdrawal wallet <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Checking this wallet on Bitquery revealed consistent outflows of $500 USD transactions, matching Finblox's daily withdrawal limit, thus confirming its identity as the official withdrawal wallet <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Tools for Wallet Analysis

Key tools used for analyzing wallet contents and transactions include:
*   **Bitquery.io**: Useful for general transaction tracing and identifying inflow/outflow <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Debank.com, Zapper.fi, Aboard.finance**: Provide quick overviews of funding in a wallet <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Senky Diagram (Bitquery.io Money Flow)**: Visualizes the flow of funds from a wallet, indicating where the largest amounts are being sent <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

### Fund Flow to Other Exchanges

By analyzing the outflow from Finblox's main deposit wallet using the Senky diagram, several destination wallets were identified:

*   **Binance**: A significant portion of funds (4.4 million USDC) from Finblox's main deposit wallet was sent to an address (ending in `fe6`) that, upon further investigation, was identified as a Binance hot wallet <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This suggests Finblox uses Binance as a holding or operational exchange.
*   **FTX**: Two specific addresses (ending in `a6` and `dd`) received funds from Finblox's main deposit wallet and forwarded them to well-known FTX hot wallets <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. Interestingly, these FTX deposit wallets also received funds from other platforms like BlockFi and Nexo <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
    *   This raised three possibilities:
        1.  These FTX wallets were owned by a counterparty, like 3AC, which was known to use FTX heavily <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
        2.  Finblox, BlockFi, and Nexo shared FTX accounts to benefit from lower transaction fees through higher tiers <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
        3.  Finblox was providing user funds to BlockFi and Nexo <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.
    *   The analyst concluded the third option was most probable, suggesting Finblox was leveraging competitors' platforms for yield <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

### Exposure to Three Arrows Capital (3AC)

A direct transfer wallet (ending in `914`) was identified receiving 3.2 million USD in USDC and other assets from Finblox's deposit wallet <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. This `914` wallet was not a typical exchange deposit wallet as it held funds and showed signs of DeFi transactions <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.

By tracing the outflow from the `914` wallet, a significant amount of funding was found going to a main 3AC wallet <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>. While the `914` wallet also received funds from other sources (like FTX exchange and a Compound USD pool), the focus was on the Finblox connection <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

Crucially, Finblox's transfers to 3AC became frequent and erratic starting around May 13, 2022, which coincided with the heavy de-pegging of the UST stablecoin and the start of 3AC's financial difficulties <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. Before this period, transfers to 3AC were rare and in fixed amounts <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. The random amounts (e.g., 85 pennies, 61 pennies) and inclusion of Singapore Dollars suggest a desperate need for funds by 3AC <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>. Finblox ceased these transfers around June 1, when rumors of 3AC's insolvency intensified <a class="yt-timestamp" data-t="00:28:39">[00:28:39]</a>.

The direct exposure of Finblox to 3AC through this specific wallet is estimated at 3.1-3.2 million USD <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. There could be additional indirect exposure through funds sent to FTX or Binance accounts that might have subsequently been moved to 3AC <a class="yt-timestamp" data-t="00:30:20">[00:30:20]</a>.

### Bitcoin and Solana Wallets

For Bitcoin, Finblox uses a single wallet for both deposits and withdrawals <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. The Bitcoin wallet showed a maximum of 4.8 BTC ever held, with only 1.19 BTC remaining at the time of analysis <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. The inflow and outflow amounts were consistently small, suggesting these funds were largely idle and being withdrawn by end-users, rather than being used for active yield generation on other major platforms <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>. Despite Finblox offering interest (e.g., 5.75% APY) on BTC, it appeared to be stagnant <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>. A similar pattern was observed for Solana <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

## Finblox's Role as an Intermediary

The analysis indicates that Finblox's claim of using "eight sophisticated different yielding strategies" is questionable <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>. Instead, it appears Finblox largely acts as an [[finblox_platform_features | intermediary]], sending substantial user funds to platforms like Vault and Nexo <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>. These larger platforms have their own money-making strategies, such as [[borrowing_against_crypto_assets | borrowing against crypto assets]] and lending <a class="yt-timestamp" data-t="00:35:49">[00:35:49]</a>. This suggests Finblox does not have its own yield generation strategy but rather leverages others' products <a class="yt-timestamp" data-t="00:36:11">[00:36:11]</a>.

If users were to deposit directly with Nexo or Vault, they might avoid the [[withdrawal_processes_before_binance_ban | liquidity problems]] that Finblox experienced, as these platforms did not have limited withdrawals at the time of the analysis <a class="yt-timestamp" data-t="00:36:49">[00:36:49]</a>.

## Financial Impact and Outlook

The analysis estimated total end-user deposits on Finblox to be around 25 million USD <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>. Approximately 10 million USD had been withdrawn from the withdrawal wallet <a class="yt-timestamp" data-t="00:37:36">[00:37:36]</a>, leaving 15-20 million USD that Finblox needs to provide to users <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.

Assuming the 3.2 million USD lost to 3AC is not recoverable, the overall estimated loss for Finblox users could be between 10% and 30% of their deposits <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. The majority of deposits were in stablecoins, particularly USDC on the Ethereum chain, due to the attractive interest rates offered <a class="yt-timestamp" data-t="00:38:37">[00:38:37]</a>.

## Conclusion and Recommendations

This on-chain analysis technique is highly valuable for prospective users considering depositing funds into lending protocols <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>. By examining where funds are actually sent, users can determine if a platform has proprietary yield strategies or merely acts as an intermediary for other competitors <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>. This due diligence can help users make more informed decisions about where to place their funds.