---
title: Use cases for MEV such as dex arbitrage liquidation and sandwich trading
videoId: w9SHvQNKqEM
---

From: [[goingonchain]] <br/> 

[[maximal_extractable_value_mev_on_ethereum | Maximal Extractable Value (MEV)]] refers to the maximum value that can be extracted from a block production, exceeding the standard block reward and gas fee [00:00:41]. This is achieved by including, excluding, or changing the order of transactions within a block [00:00:53]. While formerly known as Miner Extractable Value, it is now termed Maximum Extractable Value due to the shift to Proof-of-Stake (PoS) and the absence of miners [00:01:01].

[[role_of_block_producers_in_mev | Block producers]], whether miners or validators, have the power to select which transactions to process, allowing them to prioritize transactions that offer more rewards [00:01:25]. This leads to increased profit for the block producer, as MEV can be very profitable, with total extracted MEV reaching around $675 million [00:01:36].

Bots and "searchers" actively monitor the mempool for profitable transactions, which they then push to validators [00:02:37]. These MEV profits are typically shared with block producers [00:02:51]. While searchers aim to maximize their gas payment to the miner, it only makes sense if the profit from the MEV trade exceeds the miner's payment [00:02:59].

## Common MEV Use Cases

MEV is most commonly used in arbitrage conditions [00:02:54].

### Dex Arbitrage

Decentralized Exchange (DEX) arbitrage involves exploiting price differences for the same asset across different DEXs [00:05:08]. For example, if SushiSwap and Uniswap are offering ETH/DAI at different prices, a bot can simultaneously buy the token at the lower price on one DEX and sell it at the higher price on another in a single transaction [00:05:17]. This is a form of [[arbitrage_opportunities_in_cryptocurrency | arbitrage opportunity]] [00:05:23].

### Liquidation

Liquidation refers to bots searching for opportunities to liquidate collateralized positions to earn liquidation fees [00:05:32].

### Sandwich Trading

Sandwich trading involves a bot detecting a large incoming trade (e.g., a user wanting to buy 10,000 UNI tokens) and executing two trades around it [00:05:39]. The bot will:
1.  **Front-run** the user's transaction by buying the token first, ahead of the user's purchase [00:05:51].
2.  **Back-run** the user's transaction by selling the token back after the user's large purchase has driven the price up [00:05:56].

This strategy causes the original user to experience price impact and high slippage [00:05:59].