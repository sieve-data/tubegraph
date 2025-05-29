---
title: Maximal extractable value MEV on Ethereum
videoId: w9SHvQNKqEM
---

From: [[goingonchain]] <br/> 

Maximal Extractable Value (MEV), also known as Maximum Extractive Value, refers to the maximum value that can be extracted from a block production in excess of the standard block reward and gas fees <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This extraction is achieved by including, excluding, or changing the order of transactions within a block <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Initially, MEV was known as Minor Extractable Value. However, with the transition to [[the_merge_on_ethereum | Proof-of-Stake (PoS)]] on [[ethereum_merge_and_its_implications | Ethereum]], the term shifted to Maximal Extractor Value as there are no longer "miners" but "validators" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. MEV is considered both a blessing and a problem for [[ethereum_merge_and_its_implications | Ethereum]] and other networks, though it is more prominent and profitable on [[ethereum_merge_and_its_implications | Ethereum]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## How MEV Works

Block producers, whether miners or validators, are rewarded for their role in block production and validation <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. These block producers possess the power to choose which pending transactions to process, allowing them to prioritize transactions that yield greater rewards and de-prioritize others, thereby increasing their profit <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The total extracted MEV has been substantial, reaching approximately $675 million <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

All transactions (e.g., Uniswap swaps, OpenSea purchases, token transfers) first enter a public holding area known as the mempool <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This mempool is transparent, meaning anyone can view its contents <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Validators then select transactions from the mempool to validate and append them to the blockchain <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

While validators technically have the power to select transactions based on economic incentives <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, in practice, independent "searchers" actively monitor the mempool for profitable transactions <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. These searchers, often using bots, push these profitable transactions to validators <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. The profits generated from MEV are then shared with the block producers <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. For a transaction to be profitable for a searcher, the MEV profit must exceed the miner's (or validator's) payment <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## [[mev_extraction_strategies_like_gas_sniffing_and_front_running | MEV Extraction Strategies]]

Several strategies are employed to extract MEV:

*   **Gas Sniffing (or Gas Coughing)**: The goal is to have transactions use the least amount of gas <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This can be achieved by:
    *   Using long strings of zeros in addresses <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   Leaving small token balances in contracts <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    Both methods help transactions take up less space, thus consuming less gas. Searchers can then increase the gas price to get their transaction processed first while maintaining low gas consumption <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

*   **Generalized Front-Running**: When a bot detects a profitable transaction in the mempool, it copies the original transaction, increases its bid (SV), and submits its own transaction to be processed first, effectively "front-running" the original user <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

*   **Back-Running**: This strategy involves scooping up tokens at a very low price immediately after a new token listing on a [[utility_of_dex_tokens | DEX]] like Uniswap <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. As the price subsequently rises, the bot sells the tokens, acting as one of the first traders in the new pool <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

*   **[[use_of_flashbots_in_privacypreserving_mev_extraction | Flashbots]]**: [[use_of_flashbots_in_privacypreserving_mev_extraction | Flashbots]] connect searchers and block producers in a private transaction pool, preventing the public mempool from being affected by MEV activities that could otherwise drive up gas prices for retail users <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Searchers identify opportunities, bundle them, and send them to a [[use_of_flashbots_in_privacypreserving_mev_extraction | Flashbots]] platform. Block builders then construct the most profitable blocks and send them to a relay, which forwards them to validators <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## [[examples_and_use_cases_of_mev_in_decentralized_exchanges_and_liquidations | Common MEV Use Cases]]

MEV is commonly observed in the following scenarios:

*   **[[examples_and_use_cases_of_mev_in_decentralized_exchanges_and_liquidations | DEX Arbitrage]]**: This involves profiting from price differences of the same asset across different decentralized exchanges (DEXs) like SushiSwap and Uniswap <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. An arbitrageur buys a token on the DEX with the lower price and sells it on the DEX with the higher price, often within a single transaction <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

*   **[[examples_and_use_cases_of_mev_in_decentralized_exchanges_and_liquidations | Liquidations]]**: Bots constantly search for opportunities to liquidate undercollateralized positions in DeFi lending protocols, earning liquidation fees in the process <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

*   **Sandwich Trading**: This strategy involves "sandwiching" a user's transaction. For example, if user A intends to buy a large amount of a token (e.g., 10,000 Uniswap tokens), a bot monitoring the mempool can "front-run" user A's transaction by buying the token first, then allowing user A's transaction to execute (which drives up the price), and immediately "back-running" by selling the token back to user A at a higher price <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. This results in user A experiencing price impact and high slippage <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.