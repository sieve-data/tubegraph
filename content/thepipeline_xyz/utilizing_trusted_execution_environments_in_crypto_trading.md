---
title: Utilizing trusted execution environments in crypto trading
videoId: 39xuOQnIqYQ
---

From: [[thepipeline_xyz]] <br/> 

Trusted Execution Environments (TEEs) are being integrated into the cryptocurrency market to enhance security, privacy, and efficiency for various applications, particularly in trading and data verification. TEEs provide a private, confidential computing environment that protects sensitive data and operations. <a class="yt-timestamp" data-t="00:41:22">[00:41:22]</a>

## Benefits and Applications

The primary benefits of integrating TEEs into crypto operations include:

*   **Enhanced Security:** TEEs encrypt data and execute code in an isolated environment, preventing unauthorized access and manipulation.
*   **Privacy Preservation:** Sensitive information can be processed without being fully exposed to all parties, addressing concerns like market makers' reluctance to share API keys.
*   **Automation with Trust:** Complex trading strategies and data verifications can be automated with guarantees that the computations are performed as intended.
*   **Increased Efficiency:** By handling certain processes off-chain within a trusted environment, TEEs can reduce the computational load and associated costs on the blockchain.

### Data Verification and Credit Assessment

Accountable, a platform focused on verifiable credit, utilizes TEEs to establish a trust layer for assessing [[market_making_in_crypto_vs_traditional_finance | market makers]] and other entities. After experiencing significant losses due to falsified financial statements in 2022, Accountable developed a system to ensure data integrity. <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>

*   **Technology Stack:** Accountable runs its own API connectors, which can be deployed in SGX (Software Guard Extensions) for hardware guarantees. <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a> They also employ ZK-TLS (Zero-Knowledge Transport Layer Security) to further increase trust. <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   **Sensitive Data Sharing:** The platform features a "Signed API" solution, aiming to be an industry standard for secure sensitive data sharing. <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a> This allows borrowers to prove their financial health in their own local infrastructure and send it peer-to-peer to a lender without exposing raw data. <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>
*   **Addressing Hidden Liabilities:** To mitigate the risk of unreported positions, Accountable uses a summation Merkle tree on top of assets and liabilities. A zero-knowledge proof checks that known liabilities are properly reflected in reports when a borrower seeks a new loan. <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
*   **Privacy-Preserving:** The solution prioritizes preserving sensitive information like API keys, which market makers typically cannot share due to proprietary "sauce." <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a> This enables them to share only essential data points in real-time. <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a> Most proofs in lender-borrower relations are validated off-chain, as there is no need for high on-chain visibility for these specific use cases. <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>

### Advanced Trading Features

Sauce, a platform building a "sex-like experience" on-chain for advanced traders, leverages TEEs for transaction automation and to offer features not typically found in decentralized environments. <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>

*   **One-Click Transactions:** The goal is to enable one-click cross-chain transactions to any asset on any chain, from meme coins to exotic derivatives. <a class="yt-timestamp" data-t="00:39:54">[00:39:54]</a>
*   **Private Orders:** Traders often prefer not to put their trades publicly on-chain, as it reveals their intentions. TEEs allow for "private DCAs (Dollar-Cost Averaging)" and "off-chain limit orders." <a class="yt-timestamp" data-t="00:40:46">[00:40:46]</a> This means users can set orders to "buy the dip" without constant monitoring. <a class="yt-timestamp" data-t="00:47:11">[00:47:11]</a>
*   **Automated Yield Generation:** Idle funds can automatically be directed into yield-earning protocols like lending markets or yield-bearing stablecoins. <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>
*   **Copy Trading:** TEEs can facilitate [[crypto_trading_strategies_and_personal_experiences | copy trading]], allowing users to execute transactions based on another trader's actions by running code inside the TEE. <a class="yt-timestamp" data-t="00:47:24">[00:47:24]</a>
*   **Security Model:** Sauce uses AWS Nitro as their TEE implementation. <a class="yt-timestamp" data-t="00:44:30">[00:44:30]</a> The system is designed so that only the user has access to the private key that enables these automations within the TEE. <a class="yt-timestamp" data-t="00:41:25">[00:41:25]</a> API keys used for delegation are encrypted by a key within the TEE and stored in a database. <a class="yt-timestamp" data-t="00:48:23">[00:48:23]</a> The system allows for pre-specifying what code can access the keys, ensuring the keys are only used for their intended purpose. <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>, <a class="yt-timestamp" data-t="00:48:54">[00:48:54]</a>

## Future Outlook

The integration of TEEs represents a significant step towards enabling more sophisticated and user-friendly on-chain activities. By addressing critical concerns like privacy for [[crypto_trading_strategies_and_personal_experiences | advanced trading strategies]] and the security of automated financial operations, TEEs aim to bridge the gap between the efficiency of centralized exchanges and the benefits of decentralization. <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>