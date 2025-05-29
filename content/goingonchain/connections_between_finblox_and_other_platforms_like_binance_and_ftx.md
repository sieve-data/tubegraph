---
title: Connections between Finblox and other platforms like Binance and FTX
videoId: AaPN203qCXU
---

From: [[goingonchain]] <br/> 

Finblox recently [[finblox_withdrawal_limitations_and_3ac_exposure | reduced their withdrawal]] limits to $500 per day and a maximum of $1500 per month, citing [[finblox_withdrawal_limitations_and_3ac_exposure | exposure to 3AC]] (Three Arrows Capital) [00:00:02]. This situation led to a [[onchain_analysis_of_finblox_wallets | thorough analysis on the Finblox wallet]] by a Reddit user, detailing the platform's deposit and withdrawal wallets and estimating its exposure to 3AC [00:00:16].

## On-Chain Analysis Methodology

The analysis began by identifying Finblox's main deposit and withdrawal wallets on the blockchain [00:01:11]. The analyst had prior experience in risk management and diversified funds across multiple platforms, including Finblox [00:01:21]. Concerns arose when rumors circulated about Three Arrows Capital (3AC) becoming insolvent, given its close relationship with Finblox [00:01:42].

### Identifying Deposit Wallets
Finblox, like other platforms such as FTX, Binance, and Celsius, creates a unique deposit address for each user [00:02:23]. Funds sent to these unique addresses are then automatically forwarded to a main hot wallet [00:03:49]. The analyst identified Finblox's main deposit wallet (ending in `a9e`) by tracking their own transaction outflow from their MetaMask wallet to Finblox, then checking the receiver address of that transaction [00:02:48]. This `a9e` wallet was confirmed as the main deposit wallet because all user deposits were forwarded to it [00:06:53].

Tools like bitquery.io were used to trace transaction flows [00:04:48], while debank.com, zapper.fi, and a.board.finance were preferred for quickly viewing the current value and holdings of a wallet [00:09:32].

### Identifying Withdrawal Wallets
The withdrawal wallet was identified by initiating a withdrawal from Finblox to a MetaMask wallet [00:07:54]. By checking the inflow to the MetaMask wallet, the sender's address (Finblox's withdrawal wallet, ending in `d20`) was revealed [00:08:09]. This `d20` address showed consistent outflows of $500, aligning with Finblox's daily withdrawal limit, confirming its role as the primary withdrawal wallet for Ethereum-based tokens [00:08:58].

For Bitcoin (BTC), Finblox appears to use a single wallet for both deposits and withdrawals. This was discovered by tracking a user's Bitcoin deposit and noting that subsequent withdrawals originated from the same address [00:31:17].

## Connections with Binance and FTX

By analyzing the outflows from Finblox's main deposit wallet (`a9e`) using a Sankey diagram, large transaction values were identified, leading to further investigation of receiving addresses [00:11:14].

### Binance Connection
One significant recipient address (ending in `fe6`) from Finblox's deposit wallet was identified as a Binance hot wallet [00:12:44]. This was determined by observing that virtually all funds flowing into this `fe6` wallet were immediately sent to a well-known Binance cold wallet [00:13:40]. This indicates that Finblox has a dedicated deposit wallet with Binance, used to transfer user funds [00:14:41].

### FTX Connection
Similarly, two other addresses (ending in `a6` and `dd`) receiving substantial funds from Finblox's main deposit wallet were identified as Finblox's deposit wallets with FTX [00:15:15]. These wallets also exhibited typical deposit wallet behavior, promptly forwarding incoming funds to a well-known FTX wallet [00:16:01].

Intriguingly, when analyzing the inflow to these FTX wallets, it was discovered that funds were also arriving from other platforms like BlockFi and Nexo [00:18:14]. This suggests that Finblox was receiving funds from or sending funds to these competitor platforms via FTX [00:18:51]. The analyst concluded that these FTX wallets were not just end-user accounts because they received funds directly from the Circle Treasury Fund, which is typically only accessible to enterprise-level organizations [00:19:36].

The analyst proposed three possibilities for these shared FTX accounts:
1.  **Counterparty Ownership**: The FTX wallets are owned by a counterparty (e.g., 3AC) that receives funds from Finblox, BlockFi, and Nexo [00:20:22].
2.  **Shared Exchange Account**: The platforms (Finblox, BlockFi, Nexo) share an FTX exchange account to benefit from lower transaction fees through higher volume tiers [00:20:58].
3.  **Finblox Lending to Competitors**: Finblox provides its users' funds to BlockFi and Nexo [00:22:11]. This is considered the most probable scenario given the relatively smaller transaction volumes and the fact that 3AC had its own identified wallet [00:21:50].

## Finblox's Yield Strategy and Intermediary Role

Finblox stated it uses "eight sophisticated different yielding strategies" [00:34:03]. However, the on-chain analysis suggests that most funds were primarily moved to Vault and Nexo [00:35:27], in addition to Binance and FTX.

It appears Finblox is acting as an [[potential_intermediary_role_of_finblox_in_fund_management | intermediary]] [00:36:01]. Instead of generating yields through its own strategies, Finblox seems to be leveraging other platforms like Nexo and Vault, which have established lending and borrowing products [00:36:11]. This raises [[platform_risk_and_security_concerns_with_finblox | platform risk]] questions, as users might consider directly depositing funds with Nexo or Vault, especially since these platforms did not have withdrawal limitations at the time of the analysis, unlike Finblox [00:36:30].

The total end-user deposits on Finblox were estimated to be around $25 million [00:37:26]. With about $10 million already withdrawn, approximately $15-20 million remains to be provided back to users [00:37:38]. Given the estimated loss of $3.2 million to 3AC, the analyst's personal belief is that between 10% and 30% of user deposits may be lost [00:38:08]. Most of the deposits appear to be in USDC on the Ethereum chain, likely due to attractive stablecoin interest rates [00:38:37].

This type of [[onchain_analysis_of_finblox_wallets | on-chain analysis]] can be a useful technique for users to investigate yield-bearing protocols before depositing funds, to understand where their money is truly being moved [00:39:35].