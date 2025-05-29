---
title: Network fees associated with smart contract wallets
videoId: HnWCHbrUHf8
---

From: [[goingonchain]] <br/> 

[[smart_contract_wallets_and_their_features | Smart contract wallets]], such as the Arjun wallet, operate differently from traditional cryptocurrency wallets due to their underlying architecture being built on smart contracts [00:02:52]. This design enables advanced features like multisig, transfer limits, and approved addresses, but it also means that certain operations incur network fees [00:03:07].

## Types of Fees

Unlike standard wallets like Metamask or Trust Wallet, which are hot wallets [00:01:26], [[smart_contract_wallets_and_their_features | smart contract wallets]] require specific actions that interact with the blockchain's smart contract layer, leading to various [[transaction_fees_and_minimum_transfers_in_crypto | transaction fees]] [00:03:02].

### Activation Fee
To begin using a [[smart_contract_wallets_and_their_features | smart contract wallet]], users must first activate it [00:02:59]. This activation process is essentially deploying or interacting with a smart contract on the blockchain [00:03:51], which incurs a "surcharge" or "guest fee" [00:03:02]. For instance, activating the Arjun wallet on Ethereum can cost approximately 0.0145 ETH, which was around $44 at the time of observation [00:04:42].

### Upgrade Fees
[[smart_contract_wallets_and_their_features | Smart contract wallets]] may offer upgrades to their features or underlying contract versions (e.g., ERC-1155 compatibility) [00:08:01]. Similar to activation, these upgrades necessitate interaction with the smart contract and thus require users to pay an additional [[understanding_transaction_fees_and_withdrawals_on_binance | network fee]] [00:06:06].

### Wallet Recovery Fees
If a user loses access to their [[smart_contract_wallets_and_their_features | smart contract wallet]] and needs to initiate a recovery process, this action also involves interacting with the smart contract [00:08:11]. Consequently, a [[transaction_fees_and_minimum_transfers_in_crypto | network fee]] must be paid for the wallet recovery [00:08:13]. In the past, Arjun used to cover these costs, but currently, users are responsible for them [00:08:18].

### Funding Fees
Funding a [[smart_contract_wallets_and_their_features | smart contract wallet]] often involves moving funds from a Layer 1 (L1) blockchain (like Ethereum mainnet) to a Layer 2 (L2) solution (like ZkSync, which Arjun supports) [00:08:31]. This bridge transaction is not free and incurs a [[transaction_fees_and_cryptocurrency_availability | gas fee]] [00:08:57]. For example, transferring 0.02 ETH from Ethereum mainnet to ZkSync on Arjun could cost around $9.45 in gas fees [00:08:59].

### Impact of Gas Fees
The cost of these operations is directly dependent on the prevailing [[transaction_fees_and_cryptocurrency_availability | Ethereum gas fees]] [00:09:01]. If [[transaction_fees_and_cryptocurrency_availability | gas is high]], funding or performing other operations on the [[smart_contract_wallets_and_their_features | smart contract wallet]] becomes more expensive [00:09:03].

> <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a> "This is because this is a [[smart_contract_wallets_and_their_features | smart contract wallet]]."

Despite these fees, the enhanced security features, such as the Guardian system for multisig approvals, instant wallet locking, and controlled transaction approvals for untrusted addresses, provide significant benefits over traditional hot wallets [00:04:53].