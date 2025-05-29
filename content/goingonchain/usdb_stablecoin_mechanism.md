---
title: USDB Stablecoin Mechanism
videoId: Iulawbmbv6s
---

From: [[goingonchain]] <br/> 

USDB is a [[types_of_stablecoins_and_their_distinctions | stablecoin]] that serves as the base asset of the liquidity pool within the Vader protocol's Automated Market Maker (AMM) <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. Its mechanism is designed to maintain a peg to the US dollar and to drive demand for the native Vader token <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## Pegging Mechanism

The supply of Vader is directly linked to the supply of USDB, functioning similarly to how Luna and UST operated <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. The target peg for USDB is one USDB equals one USD <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

*   **When USDB is above $1**: If USDB trades for more than one USD, Vader supply is burned to mint more USDB <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. This increases the supply of USDB, which helps bring its value back to the one USD peg <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. A consequence of this mechanism is that the reduced supply of Vader causes the price of Vader to increase <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **When USDB is below $1**: If USDB trades for less than one USD, USDB supply is burned to mint Vader <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. This action reduces the supply of USDB, helping to restore its peg <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. However, this process also increases the supply of Vader, which can lead to a drop in the Vader token's price <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

In summary, increased demand for USDB generally correlates with a better price for the Vader token <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## Demand for USDB

The primary source of demand for USDB comes from its role within the Vader AMM <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. To become a liquidity provider (LP) on Vader, users must provide an asset alongside USDB <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. This requirement establishes USDB as the essential base asset, thereby consistently driving its demand <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. This makes USDB a [[types_of_stablecoins_and_their_distinctions | stablecoin]] with pre-populated demand <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.