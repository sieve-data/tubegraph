---
title: Discussion on blockchain scalability and data throughput
videoId: MqrlFj_5LtY
---

From: [[bankless]] <br/> 

## Ethereum's Pectra Upgrade and Scaling

The Ethereum Pectra upgrade, which went live on May 7th, introduces several new EIPs aimed at improving the network [01:00:43].

Key EIPs in the Pectra upgrade include:
*   **EIP 7702**: This EIP enables all 0x wallets (EOAs) to have smart contract functionality, allowing them to run one-off contract code, execute it, and then revert to being a vanilla EOA [01:01:06]. This is considered a significant UX upgrade, enabling features like batch transactions (removing the need for multiple "approve" popups) and sponsor-paid token-denominated gas fees [01:01:52].
*   **EIP 7691**: This EIP expands the blob capacity, doubling it from 3 to 6 as a target [01:01:17].
*   **EIP 7251**: This EIP introduces a max effective balance, allowing validators to stake a range of ETH between 32 ETH and 48 ETH, rather than a rigid 32 ETH [01:01:23]. This change is linked to a reduction in bandwidth overhead from consolidating validators, which in turn allows for the increase in blob capacity [01:08:34].

Despite the advancements, the Pectra upgrade faced challenges, taking a "really really really long time to ship" and being "pretty messy" with delays [01:02:57]. Some features, like blob scaling, are seen as meaningful in percentage terms (doubling capacity) but are still "peanuts" in raw terms compared to other chains [01:05:02].

There is an ongoing discussion about [[ethereum_scaling_and_gas_limits | Ethereum's scaling approach]], specifically the trade-off between scaling execution (L1 gas limit, faster block times) and scaling data availability (blobs) [01:10:37]. One perspective is that while blobs scale data meaningfully, the raw numbers are still many orders of magnitude apart from dedicated data availability layers like Celestia or Avail [01:05:14]. Ethereum's bandwidth requirements are currently minimal (kilobytes) compared to megabytes being pushed by Celestia today [01:06:08].

Some argue that increasing the execution budget by reducing block times and increasing the L1 gas limit offers "a lot more bang for your buck" as premium execution is a more valuable and stickier market for Ethereum [01:11:43]. The focus should be on building a "decentralized NASDAQ" capable of handling high-frequency trading with minimal MEV extraction, which is crucial for attracting Wall Street institutions [01:12:35].

## Comparison with Other Blockchains

When comparing Ethereum's scaling to other chains:
*   **Celestia and Avail**: These chains are pushing significantly more data (megabytes) today compared to Ethereum's kilobytes, and are expected to scale further, potentially being "orders of magnitude higher" in throughput in three years [01:05:40].
*   **Solana**: Solana's appeal as a "decentralized NASDAQ" comes from its faster transaction speeds, which is attractive to institutions that care about "bips of extraction" and execution efficiency [01:12:30]. While Ethereum prioritizes properties like MEV mitigation and decentralization, which are valuable for high-value, infrequent transactions (e.g., treasuries on-chain), the concern remains that activity might naturally gravitate to faster places even if not strictly needed [01:15:14].

## [[bitcoin_layer_2_developments_and_potential_challenges | Bitcoin Layer 2s and Unique Challenges]]

As Bitcoin begins its journey into L2 architectures, lessons from Ethereum's multi-chain roadmap are being considered [01:16:33]. However, direct analogies between Ethereum and Bitcoin L2s might be limited due to fundamental differences:
*   **User Base**: Bitcoin L2s cater to a different user desire, focusing on enabling basic DeFi functionalities that are currently not possible on Bitcoin's L1 (e.g., trustless swaps, lending, vault deposits) [01:17:31]. The argument that "there are no users of Bitcoin" but rather "holders of the Bitcoin asset" suggests a different market dynamic [01:18:37].
*   **Technical Constraints**: Bitcoin's L1 has "way smaller block sizes," is "way slower," and uses proof-of-work, lacking features like ZK verification currently present on Ethereum [01:18:15]. This means Bitcoin L2s will need to provide fundamentally different functionalities than Ethereum L2s, which often aim to make existing L1 activities faster and cheaper [01:19:41].