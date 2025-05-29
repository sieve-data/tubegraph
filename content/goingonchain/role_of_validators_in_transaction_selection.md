---
title: Role of validators in transaction selection
videoId: w9SHvQNKqEM
---

From: [[goingonchain]] <br/> 

Maximum Extractable Value (MEV), also known as "Nav," is a significant aspect of blockchain networks, particularly Ethereum, due to its profitability <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. It refers to the maximum value that can be extracted from block production beyond the standard block reward and gas fee <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This extraction is achieved by including, excluding, or reordering transactions within a block <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Initially known as "Minor Extractable Value," the terminology shifted to "Maximum Extractable Value" with the transition to [[Proof of work vs proof of stake | Proof of Stake (POS)]], as miners are no longer present in the system <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Validator's Power in Transaction Selection

As block producers, whether miners in the past or validators in the present, they receive block rewards for block production and validation <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Beyond these standard rewards, validators possess the authority to choose which transactions to process and in what order <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This power allows them to prioritize transactions that offer more rewards, thereby increasing their profit <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The total extracted MEV has been substantial, reaching around $675 million <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Transaction Flow and the Mempool

When users perform actions like swapping tokens on [[Understanding decentralized exchanges | Uniswap]], making purchases on OpenC, or sending tokens, they create transactions <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. These transactions enter a public mempool, which functions as a holding area viewable by anyone <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Validators then select transactions from this mempool, validate them, and append them to the public ledger (blockchain) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

Technically, validators have complete discretion in selecting pending transactions based on economic incentives <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Role of Searchers and Bots

In practice, independent actors known as "searchers" actively monitor the mempool for profitable transactions <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Most searchers utilize bots to identify these opportunities <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. These searchers then push the identified transactions to validators, and the MEV profits are shared with the block producers <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## MEV Extraction Strategies

Several strategies are employed for MEV extraction, relying on the validator's ability to order transactions:

*   **Gas Golfing** <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>: Aims to create transactions that use the least amount of gas by including long strings of zeros in addresses or leaving small token balances in contracts. Searchers then increase the gas price to get their transaction processed first while keeping their overall gas consumption low <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Generalized Front-Running** <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>: A bot identifies a profitable transaction in the mempool, copies it, and submits its own transaction with a higher fee to be processed before the original, thereby front-running the user <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Back-Running** <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>: When a token is about to be listed on a platform like [[Understanding decentralized exchanges | Uniswap]], bots monitor the transaction that pools the new token. They immediately scoop up the token at a very low price when it lists and later sell it when the price increases <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Flashbots** <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>: Connects searchers and block producers (validators) in a private pool. This prevents the public mempool from being affected by increased gas prices due to MEV extraction. Searchers bundle profitable opportunities and send them to a Flashbots relayer. Block builders then construct and send the most profitable block to the validators <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Common MEV Use Cases

MEV strategies are commonly applied in various scenarios:

*   **[[Role of traders and protocols in DEX | DEX]] Arbitrage** <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>: Bots identify price discrepancies for the same token across different Decentralized Exchanges (DEXs), like Sushi Swap and Uniswap. They buy the token on the lower-priced DEX and sell it on the higher-priced one, often within a single transaction <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Liquidation** <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>: Bots search for liquidation opportunities in lending protocols to earn liquidation fees <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Sandwich Trading** <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>: When a bot detects a large incoming buy order for a token (e.g., 10,000 Uniswap tokens), it can front-run the user by buying the token before the user's transaction, then back-run by selling it back to the user at a higher price after the user's transaction increases the price. This results in price impact and high slippage for the original user <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## Future Developments

Innovations such as the "proposal builder separation" are being explored, which would involve centralized block production but maintain decentralized and trustless block validation <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.