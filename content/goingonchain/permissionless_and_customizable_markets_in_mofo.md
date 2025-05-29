---
title: Permissionless and customizable markets in Mofo
videoId: JSv0xYMS9_I
---

From: [[goingonchain]] <br/> 

Mofo is a lending and borrowing market known for its unique technological architecture <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Its design is so effective that platforms like Compound are considering to [[adoption_of_mofo_technology_by_other_platforms | adopt its technology]], and Berachain intends to pay a license fee to fork Mofo <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

Mofo's interface features two primary sections: "earn" and "borrow" <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Mofo Borrow (Mofo Blue)

The "borrow" section, also known as Mofo Blue, consists of various markets, each operating in isolation <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Isolated Markets

Unlike platforms such as Aave, where supplying collateral into a common pool allows borrowing from a wide range of assets within that pool, Mofo's markets are isolated <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. In Mofo, you can only borrow assets within the specific market where you have provided collateral <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

This design offers a significant [[advantages_of_isolated_lending_markets_in_mofo | advantage]]: if one market, for example, the WETH/USDC market, were to be exploited, the other isolated markets would remain unaffected <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Permissionless Market Creation

A key distinguishing feature of Mofo is its permissionless nature <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Anyone can create a Mofo market by providing five essential parameters <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>:
1.  Collateral asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
2.  Loan asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
3.  Loan-to-Value (LLTV) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
4.  Interest rate model <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
5.  Oracle <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>

### Customizable and Immutable Parameters

These parameters are customizable when a market is created <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. However, once they are set and embedded in the smart contract, they cannot be changed <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This provides users with certainty that market parameters will not be altered unexpectedly <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. In contrast, platforms like Aave require a governance model for updates to tokens or interest rates <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Mofo's approach makes it both permissionless and modular <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Mofo Earn

The "earn" section features "votes" where users can provide liquidity and earn yield <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. These votes are created and managed by [[role_of_curators_in_mofos_earn_feature | curators]], who actively manage the deposited capital and charge a fee for their services <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The liquidity supplied to these votes is then deployed into the various isolated markets created in the "borrow" section <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Adoption of Mofo's Technology

Mofo's modular and permissionless design has gained significant traction, especially as older DeFi applications like Compound have seen their Total Value Locked (TVL) decrease <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Berachain, for instance, is willing to pay for Mofo's technology because it offers a clean, modular money market that can easily integrate with its native tokenomics <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.