---
title: Role of GNS Tokens in Gains Network
videoId: UlzBJQoPlfY
---

From: [[goingonchain]] <br/> 

The GNS token is central to the operation of [[gains_network_overview|Gains Network]]'s synthetic exchange, Gains Trade, which is built for leveraged traders on the Polygon chain <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It plays a critical role in providing liquidity and maintaining the platform's stability.

## GNS as Liquidity for Synthetic Trades

The GNS token is utilized to build up the platform's liquidity <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Since trades on Gains Network are synthetic—meaning there's no real spot asset being bought or sold—two vaults support the platform: the GNS DAI pool (referred to as "GNS Daipu") and the trading vault <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

When a user enters a trade, they deposit DAI into the trading vault, and profits or losses are settled from this same vault <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The GNS DAI pool acts as a backing mechanism for the trading vault <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Deflationary Mechanism

The DAI trading vault is designed to be maintained at 110% over-collateralized <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This mechanism directly influences the GNS token supply:
*   **Token Burning**: If the trading vault exceeds 110%, the excess DAI is used to buy GNS from the GNS DAI pool, and that GNS is then burned <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Token Minting**: If the trading vault falls below 100%, GNS is minted and sold for DAI to top up the trading vault <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

This system creates buying pressure on the GNS token, particularly when traders lose, contributing to its deflationary design <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Statistics indicate that historically, more traders lose than win, leading to more GNS tokens being burned <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, reinforcing its deflationary nature <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The current inflation rate for GNS is -25%, indicating it is deflationary <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

## [[gains_network_tokenomics_and_statistics|Gains Network Tokenomics and Statistics]]

Gains Network launched in January 2021 on the Ethereum mainnet but transitioned to the Polygon chain due to high gas fees <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. During this transition, a 1:1000 split occurred, meaning one GPhantom token became 1,000 GNS tokens <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

Key GNS token statistics:
*   **Current Total Supply**: 38.5 million GNS <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>
*   **Maximum Supply**: 100 million GNS <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>

The design of GNS aims for it to be deflationary, with more tokens being burned as traders lose <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Staking GNS Tokens

Users can contribute liquidity by staking GNS into the GNS DAI pool, which offers an Annual Percentage Yield (APY) <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. As of the transcript, the trading vault offered a 10% APY, and the liquidity pool offered 47% APY <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Future plans include adding GNS single staking <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Integration with [[Utility and Use Cases of NFT Tokens|NFT Tokens]]

Gains Network NFTs offer additional features and benefits, including the ability to boost liquidity pool rewards <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. This provides further incentive for GNS holders to engage with the platform's liquidity provision.