---
title: Strategies of value extraction including front running back running and gas coughing
videoId: w9SHvQNKqEM
---

From: [[goingonchain]] <br/> 

Maximum Extracted Value (MEV), also known as "Nav," is a complex and deep subject that represents both a blessing and a problem, particularly prominent on the Ethereum network due to its profitability <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. MEV refers to the maximum value that can be extracted from block production in excess of the standard block reward and gas fees <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This extraction can be achieved by including, excluding, or changing the order of transactions within a block <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Historically, it was called "Minor Extractable Value," but with the transition to Proof of Stake (POS), it is now "Maximum Extractor Value" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

As a block producer (miner or validator), you receive block rewards for validating and producing blocks <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Block producers have the power to select which transactions to process, prioritizing those that yield more reward, thus maximizing profit <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The total extracted MEV has reached approximately $675 million, highlighting the significant interest in this area <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Transaction Flow and MEV Extraction

When a transaction occurs, such as swapping USDC to ETH on Uniswap, making a purchase on OpenSea, or sending tokens, it enters a public waiting area called the mempool <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Validators then select these transactions, validate them, and append them to the blockchain <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

While validators technically have the power to select pending transactions based on economic incentives <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, in practice, independent actors known as "searchers" actively monitor the mempool for profitable opportunities <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Most searchers use bots to identify and push these profitable transactions to validators <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. The MEV profits generated are typically shared with the block producers <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Value Extraction Strategies

Several strategies are employed to extract MEV:

### Gas Coughing
This strategy aims to process transactions using the least amount of gas <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Gas fees are calculated as gas price multiplied by gas used <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Searchers can reduce gas usage by:
1.  Having long strings of zeros in their addresses <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Leaving small token balances in contracts <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

These methods take up less space, reducing gas consumption <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Searchers can then increase the gas price to get their transaction processed first, while still keeping their gas concerns low <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Generalized Front Running
When a bot identifies a profitable transaction in the mempool, it can copy the original transaction, increase the gas price, and submit its own transaction to be processed *before* the original one <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This allows the bot to "front-run" the original transaction, often at the expense of retail users <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Back Running
This strategy occurs when a new token is about to be listed on a decentralized exchange (DEX), such as Uniswap, by adding liquidity (e.g., 50% token A and 50% stable B into a pool) <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Searcher bots monitoring the mempool spot this liquidity addition transaction <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. The bot will then immediately scoop up the token at a very low price (being the first to trade in the new pool) and sell it later as the price rises <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### Flashbots
Flashbots is a system designed to connect searchers and block producers in a private pool <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. This private channel helps prevent MEV activities from significantly impacting public gas prices, which otherwise affect retail users <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Searchers find opportunities in the mempool, bundle them, and send them to Flashbots. Block builders then create and send the most profitable blocks to a relay, which are then transmitted to validators <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Common Use Cases for MEV Strategies

MEV strategies are commonly applied in several scenarios:

*   **Dex Arbitrage**: This involves exploiting price differences for the same asset across two different DEXs (e.g., SushiSwap and Uniswap) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. A searcher can buy a token on the DEX offering the lower price and immediately sell it on the DEX with the higher price, often within a single transaction <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   **Liquidation**: Bots constantly search for collateralized debt positions that fall below a certain threshold, triggering liquidation <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. By being the first to liquidate, bots can earn liquidation fees <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **[[use_cases_for_mev_such_as_dex_arbitrage_liquidation_and_sandwich_trading | Sandwich Trading]]**: This occurs when a bot detects a large incoming buy order (e.g., User A wants to buy 10,000 UNI) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The bot will "front-run" the user by placing its own buy order just before User A's transaction, then immediately "back-run" User A's transaction by selling the token it just bought <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This action drives up the price for User A, leading to price impact and high slippage <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## Resources and References

For further learning about MEV, the following resources are available:
*   The Ethereum Block: Provides examples and explanations of MEV <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   Flashbots Documentation and GitHub: Offers details on Flashbots and its use cases <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   MEV Explorer: Allows users to observe bot transactions <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   MEV Wiki: Explains terms and provides examples not understood from Flashbots documentation <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   Paradigm Research Blog Post: Breaks down MEV, its current state, and future outlook <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   Ethereum Post by Hitch Cycle Guide: Discusses MEV and innovations like proposer-builder separation, aiming for centralized block production with decentralized and trustless block validation <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.