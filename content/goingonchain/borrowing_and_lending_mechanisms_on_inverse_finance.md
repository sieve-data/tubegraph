---
title: Borrowing and Lending Mechanisms on Inverse Finance
videoId: jf8RaMMOTx0
---

From: [[goingonchain]] <br/> 

Inverse Finance is a platform that has upgraded its governance token to Inverse Plus, aiming to add value to the token by making it a "positive sum rewards token" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The platform operates with three core products: the IMV token, DOLA stablecoin, and Anchor, which serves as its primary [[borrowing_and_lending_strategies | lending and borrowing]] setup <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## DOLA Stablecoin

DOLA is Inverse Finance's stablecoin, offering farming opportunities on both Ethereum (ETH) and Phantom networks <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Users can swap DOLA via Curve or Stabilizer <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Stabilizer is Inverse Finance's proprietary liquidity pool, pairing DYE and DOLA <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. It charges a swap fee of 0.4% and guarantees a fixed rate of 0.996 <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The Stabilizer pool has approximately $4 million in liquidity <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Anchor: The Lending and Borrowing Hub

Anchor is the central hub for [[borrowing_and_lending_strategies | lending and borrowing]] on Inverse Finance <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. As of the recording, its Total Value Locked (TVL) was around $65 million <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Lending Process

Users can deposit assets into Anchor to earn a base reward and additional rewards in the form of APR <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. For instance, depositing ETH yields a base reward of 0.08% APY plus 5.34% APR in IMV tokens <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

A standout asset for lending is the IMV token itself, offering an APY of 122% <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This high return is due to users simultaneously supplying and staking their IMV tokens <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

#### Benefits of Supplying IMV

When users deposit IMV into Inverse Finance, they receive xIMV, which comes with several benefits:

1.  **IMV Emission**: xIMV holders receive IMV emissions per ETH block, occurring approximately 6400 times a day <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The cap for this emission is 500% APY, which can only be altered through a new governance vote <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. It's important to note that the IMV token has no maximum supply <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. The DAO can introduce a cap to cease minting if emissions become too high <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
2.  **Protocol Revenue Share**: IMV stakers also receive a portion of the protocol's revenue, which is generated from borrowing interest <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  **Voting Rights**: xIMV grants holders voting rights on the platform's governance proposals <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The governance page is active, with 35 proposals made and 32 passed, including the recent Inverse Plus upgrade <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. All voting is conducted on-chain <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Collateral for Borrowing DOLA**: One of the most significant features is the ability to use xIMV as collateral to borrow DOLA stablecoin <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This allows users to buy IMV, supply it to earn IMV emissions (e.g., 122% APY), receive a cut of the protocol revenue, vote in governance, and simultaneously use their supplied IMV as collateral to borrow stablecoin <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

For example, if a user supplies $100 worth of IMV and stakes it, they can borrow $30 of DOLA, while the initial $100 of IMV continues to earn the 122% APY (assuming it has not been degraded) <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This mechanism provides significant capital efficiency as funds are not locked <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Borrowing Process

When borrowing an asset, the smart contract utilizes the price from a Euro code <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Transparency

Inverse Finance also provides a transparency tab, which is a unique feature <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This tab displays smart contract links and details how these contracts interact with each other, similar to reading a company's balance sheet <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Further information about Inverse Plus can be found on their Twitter account <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.