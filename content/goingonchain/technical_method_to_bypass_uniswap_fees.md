---
title: Technical method to bypass Uniswap fees
videoId: 4PmgYsP2HnY
---

From: [[goingonchain]] <br/> 

Uniswap recently implemented a 0.15% swap fee for using their user interface (UI) [00:00:07]. This means an extra charge is applied when conducting a swap directly on the Uniswap site [00:00:16]. While this fee may seem small, it can accumulate significantly when multiple transactions are performed [00:00:20]. These collected [[understanding_uniswap_swap_fees | fees]] are directed to Uniswap Labs, not to UNI token holders [00:00:28].

To avoid this additional charge, various [[methods to avoid Uniswap fees | methods to avoid Uniswap fees]] exist, including a direct technical approach.

## Using the Backend Directly

A more technical method to avoid the Uniswap UI fee involves interacting directly with the backend smart contract [00:01:55]. This approach is ideal for users with a technical understanding of blockchain interactions [00:02:12].

### Steps to Bypass Fees via Backend

1.  **Navigate to Etherscan**: Access the Uniswap V2 router on Etherscan [00:02:01].
2.  **Access Contract Write Function**: Go to the "Contract" tab and then select "Write Contract" [00:02:03].
3.  **Connect Wallet**: Connect your web3 wallet to Etherscan [00:02:05].
4.  **Call Desired Function**: Locate and select the specific function you wish to execute, such as "sort if for exact tokens" [00:02:07].
5.  **Input Parameters**: Provide the necessary inputs for the chosen function [00:02:11].

This direct interaction with the smart contract allows users to execute trades without incurring the 0.15% UI fee imposed by Uniswap [00:01:57].