---
title: Cost associated with using Argent wallet
videoId: HnWCHbrUHf8
---

From: [[goingonchain]] <br/> 

The [[argent_smart_wallet_features | Argent smart wallet]] is a smart contract wallet, which means it is written on a smart contract [00:02:52]. This design leads to certain costs associated with its use.

## Activation Fees

When activating an Argent wallet, users must pay a surcharge or gas fee [00:02:59]. This initial activation is referred to as activating the "vault," which is essentially setting up the smart contract [00:04:37]. As of the transcript, this fee was approximately 0.0145 ETH, costing about $44 [00:04:42].

## Upgrade Fees

Should users wish to upgrade their Argent wallet with additional functionalities, such as support for ERC-1155 tokens, a network fee is required [00:06:06]. This is because upgrades also involve interactions with the underlying smart contract [00:06:09].

## Wallet Recovery Fees

In the event of losing access to the wallet and needing to perform a wallet recovery, users are required to pay a fee [00:08:11]. This recovery process, like other operations, interacts with the smart contract [00:08:15]. While Argent previously covered these recovery costs, users are now responsible for them [00:08:18].

## Funding Fees

Funding the Argent wallet also incurs a network fee [00:08:26]. This fee is incurred because adding funds to the wallet typically involves moving assets from Layer 1 (L1) to Layer 2 (L2), specifically from the Ethereum mainnet to zkSync in the demonstrated example [00:08:33]. The gas cost for such a transaction was around $9.45 [00:08:57]. If Ethereum gas fees are high, funding the Argent wallet can become expensive [00:09:03].

## Reason for Fees

The recurring fees for activation, upgrades, and recovery are due to Argent being a smart contract wallet [00:07:54]. Each of these actions requires an on-chain transaction to interact with or modify the underlying smart contract, thus incurring network fees [00:08:07].