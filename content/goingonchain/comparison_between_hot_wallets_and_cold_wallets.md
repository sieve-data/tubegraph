---
title: Comparison between hot wallets and cold wallets
videoId: HnWCHbrUHf8
---

From: [[goingonchain]] <br/> 

Wallet hacking incidents are a significant concern in the crypto space <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. A notable example is the founder of Defiance Capital losing $1.6 million in a hot wallet hack, including NFTs <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. He suspected the exploit was due to phishing <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Other common hacking incidents include laptop compromises, scams, and users signing malicious transactions <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Specific cases mentioned include a MetaMask Chrome extension hack leading to a loss of $400 worth of ETH <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> and a $1.7 million NFT theft via a phishing attack <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

The crypto community often debates the security of [[using_cold_wallets_versus_hot_wallets | hot wallets versus cold wallets]] <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Hot Wallets

Hot wallets are defined as wallets that are connected to the internet <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Examples include MetaMask and Trust Wallet <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

A key security concern is that hot wallets on mobile phones are "not safe enough" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, particularly when conducting many transactions <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Cold Wallets

Cold wallets are not connected to the internet <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

Examples of cold storage methods include:
*   **Hardware Devices**: Using a hardware wallet like Ledger <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. If MetaMask is used with a Ledger device, it effectively becomes a cold wallet because transactions must be signed on the Ledger hardware device to be approved <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Ledger devices cost around $200, often with promotional discounts <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Paper Seed Phrases**: Writing down your seed phrase on paper and storing it physically is considered a "super hardcore" [[noncustodial_wallets_and_key_management | key management]] method for security <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

While hardware wallets enhance [[security_measures_for_cryptocurrency_wallets | security]], they cannot protect against user error, such as signing a malicious contract <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Other Security Strategies

Beyond the hot vs. cold wallet debate, other [[security_measures_for_cryptocurrency_wallets | security practices]] include:
*   **Multiple Wallet Addresses**: Users can own multiple wallet addresses for different purposes, such as one for trading, one for DeFi, one for NFTs, one for storage, and one for testing <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## [[smart_contract_wallets_and_their_features | Smart Contract Wallets]]: Argent

Argent is highlighted as a [[smart_contract_wallets_and_their_features | smart contract wallet]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, meaning its functionality is written on a smart contract <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Its contracts are open-source <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Key Features of Argent

Argent offers features not typically found in traditional wallets like MetaMask:
*   **Multisig (Guardians)**: Users can set up "guardians" who act as third-party signers <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Guardians can approve transactions (especially those over a set limit), help recover a lost wallet, or instantly lock a compromised wallet <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Transfer Limits**: The ability to set maximum transfer limits <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Approved Addresses**: Users can define specific addresses to which funds can be sent, preventing transfers to untrusted addresses <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Token Allowance Limits**: Control how much of a specific token can be spent <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Wallet Connect Compatibility**: Works with Wallet Connect <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Built-in DeFi Functionality**:
    *   **Token Swaps**: Allows trading tokens directly within the wallet <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Staking**: Supports staking ETH via Lido <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   **Stablecoin Yields**: Offers stablecoin yield opportunities from protocols like Yearn, Aave, or Zero Protocol <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   **Index Funds**: Integration with index funds powered by Index Coop <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **User Experience**: Described as having a good user experience, simpler than the MetaMask app, possibly due to fewer chain options <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### Limitations of Argent

Despite its advanced [[security_measures_for_cryptocurrency_wallets | security]] features, Argent has some downsides:
*   **Network Fees**:
    *   **Activation Fee**: A surcharge (gas fee) is required to activate the wallet (the smart contract vault) <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. This fee can be substantial (e.g., $44 for 0.0145 ETH) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
    *   **Upgrade Fees**: Upgrading the wallet (e.g., for ERC-1155 support) also incurs a network fee <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    *   **Wallet Recovery Fees**: Recovering a lost wallet requires paying another network fee <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   **Funding Fees**: Funding the wallet involves moving funds from L1 (Ethereum mainnet) to L2 (zkSync), which incurs network fees that vary with Ethereum gas prices <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Limited Blockchain Support**: Currently only supports Ethereum and zkSync <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, meaning it does not work with chains like Fantom, Avalanche, or Polygon <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This makes it less suitable for "advanced users" who engage in activities on multiple chains <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

Historically, Argent covered these network costs, but users are now responsible for them <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.