---
title: MEV extraction strategies like gas sniffing and front running
videoId: w9SHvQNKqEM
---

From: [[goingonchain]] <br/> 

[[maximal_extractable_value_mev_on_ethereum | Maximal Extractable Value (MEV)]] is a complex and deep subject that represents the maximum value that can be extracted from block production beyond the standard block reward and gas fees <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. It can be achieved by including, excluding, or reordering transactions within a block <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Originally known as "miner extractable value," it's now termed "maximum extractable value" due to the shift to Proof-of-Stake (PoS) where there are no longer miners <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

[[maximal_extractable_value_mev_on_ethereum | MEV]] is prominent on Ethereum, but occurs on any network, as block producers (miners or validators) have the power to choose which transactions to process to maximize their profit <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The total extracted [[maximal_extractable_value_mev_on_ethereum | MEV]] has been estimated at approximately $675 million <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

Transactions, such as swapping tokens on Uniswap, making purchases on OpenSea, or sending tokens, first enter a public holding area called the mempool <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Validators then pick up and process these transactions to append them to the blockchain <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. While validators technically have the power to select pending transactions based on economic incentives, independent searchers actively monitor the mempool for profitable opportunities and push them to validators, often using bots <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. These [[maximal_extractable_value_mev_on_ethereum | MEV]] profits are shared with the block producers <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## MEV Extraction Strategies

### Gas Coughing (Gas Sniffing)

Gas coughing is a strategy aimed at using the least amount of gas for transactions <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Gas fees are calculated as gas price multiplied by gas used <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Searchers employ two main methods to reduce gas usage:
1.  Including long strings of zeros in their addresses <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
2.  Leaving small token balances in contracts <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Both methods help transactions take up less space, thereby using less gas <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. These searchers can then increase the gas price for their transaction to ensure it's processed first, while still keeping their overall gas cost lower due to reduced gas usage <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Generalized Front Running

[[front_running_scams | Generalized front running]] occurs when a bot identifies a profitable transaction in the mempool <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The bot can then copy the original transaction, increase its own transaction's value (SV), and ensure its transaction is processed before the original one, effectively [[front_running_scams | front running]] the retail user <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Back Running

Back running is another strategy, often observed when a new token is about to be listed, for example, on Uniswap with 50% of token A and 50% of stable B in a pool <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Searchers monitoring the mempool can spot this initial listing transaction <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. The bot will then immediately scoop up the token at a very low price, and subsequently sell it when the price rises <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. This is akin to being the very first person to trade in the new liquidity pool <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Sandwich Trading

[[examples_and_use_cases_of_mev_in_decentralized_exchanges_and_liquidations | Sandwich trading]] involves a bot monitoring a user's transaction, such as a large purchase of 10,000 Uniswap tokens <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The bot will [[front_running_scams | front run]] the user's transaction by buying the token first, and then immediately "back run" by selling the token back to the user <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This results in the user experiencing price impact and high slippage <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Use of Flashbots

[[use_of_flashbots_in_privacypreserving_mev_extraction | Flashbots]] are a solution designed to connect searchers and block producers in a private pool <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. This private arrangement aims to prevent [[maximal_extractable_value_mev_on_ethereum | MEV]] extraction in the public mempool from affecting public gas prices, which impacts retail users <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Searchers identify opportunities in the mempool, bundle them, and send them to a [[use_of_flashbots_in_privacypreserving_mev_extraction | flashbots]] form <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. From there, block builders construct blocks and send them to a relay, and the most profitable block is then sent to the validators <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## Resources

*   **Ethereum Blog:** Features a topic about [[maximal_extractable_value_mev_on_ethereum | MEV]] with examples and explanations <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **[[use_of_flashbots_in_privacypreserving_mev_extraction | Flashbots]] Documentation and GitHub:** Provides more details on [[use_of_flashbots_in_privacypreserving_mev_extraction | flashbots]] and interesting use cases <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **MEV Explorer:** Allows users to view transactions executed by bots, often linking to Etherscan for detailed analysis <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **MEV Wiki:** Offers translations and examples for terms found in [[use_of_flashbots_in_privacypreserving_mev_extraction | flashbots]] documentation <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Paradigm Research Blog Post:** Breaks down what [[maximal_extractable_value_mev_on_ethereum | MEV]] is, its current state, and future outlook <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Hsiao-Wei Wang's Cycle Guide to Ethereum Post:** Discusses [[maximal_extractable_value_mev_on_ethereum | MEV]] and innovations like proposer-builder separation, aiming for centralized block production with decentralized, trustless block validation <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.