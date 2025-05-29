---
title: USDB stablecoin and its mechanics
videoId: Iulawbmbv6s
---

From: [[goingonchain]] <br/> 

USDB is a [[Types of Stablecoins | stablecoin]] and the base asset of the liquidity pool within the Vader protocol's Automated Market Maker (AMM) <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. Its mechanics are similar to how Luna and UST operate <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Pegging Mechanism

The supply of Vader tokens is directly linked to the supply of USDB <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. The goal is for one USDB to always equal one USD <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

*   **When USDB goes above $1:** If the price of USDB rises above one dollar, the supply of Vader is burned to mint more USDB <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. This increases the supply of USDB, which helps bring its value back down to the $1 peg <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. Concurrently, the reduced supply of Vader causes its price to increase <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **When USDB goes below $1:** If the price of USDB falls below one dollar, the supply of USDB is burned to mint Vader <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. This action reduces the supply of USDB, helping to restore its peg <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. As a result, the increased supply of Vader causes its price to drop <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

In summary, a higher demand for USDB generally benefits the price of Vader <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## Demand Generation

Demand for USDB is primarily driven by its role as the base asset in liquidity pools on the Vader AMM <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. To become a liquidity provider on Vader, users must contribute an asset paired with USDB <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. This requirement ensures a pre-populated demand for the [[Types of Stablecoins | stablecoin]] <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>, making USDB integral to the platform's liquidity provision <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.