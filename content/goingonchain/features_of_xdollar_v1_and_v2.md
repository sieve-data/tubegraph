---
title: Features of xDollar V1 and V2
videoId: tIjZzwCB-vo
---

From: [[goingonchain]] <br/> 

[[Introduction to xDollar protocol | xDollar]] is a lending protocol that enables users to borrow stablecoins with a low collateral ratio and zero percent interest <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Types of Stablecoins

To understand [[Introduction to xDollar protocol | xDollar]], it's helpful to know the different types of stablecoins <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>:
1.  **Fiat-backed:** Examples include USDC, where for every USDC, one USD is controlled by a company like Circle <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
2.  **Algorithmic:** Terra UST is a famous example, where the supply of UST is backed by the supply of Luna <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
3.  **Crypto-backed:** Dai is a well-known crypto-backed stablecoin. To borrow $500 worth of Dai, one might need $1,000 worth of ETH, resulting in a 200% collateral ratio <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

[[Introduction to xDollar protocol | xDollar]] belongs to the crypto-backed category <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Core Features of xDollar

[[Introduction to xDollar protocol | xDollar]] aims to be multi-chain and multi-collateral, allowing users to use assets like MATIC, Avalanche, or Ethereum to borrow stablecoins <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

Key features include:
*   **Low Collateral Ratio:** A low 110% collateral ratio <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Zero Percent Interest:** No interest charged on borrowed stablecoins <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **One-Time Fixed Fee:** While there's no interest, a one-time fixed fee applies <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This makes it more suitable for long-term loans <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Multi-Collateral:** Allows using different assets to borrow stablecoins <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Cross-Chain Focus:** Aims to be cross-chain, not just on Ethereum, potentially leading to lower fees on chains like Polygon <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

The team behind [[Introduction to xDollar protocol | xDollar]] is anonymous but has strong backing, including "vfec" who created "vfad2" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## xDollar V1 vs. V2 Comparison

After the V2 launch, there were naming and chain changes <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>:

| Feature          | xDollar V1                                   | xDollar V2                                                 |
| :--------------- | :------------------------------------------- | :--------------------------------------------------------- |
| Stablecoin Name  | xUSD <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>        | XIM (xDollar Intervals Money) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> |
| Protocol Token   | XTO <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>           | Space Gain <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>               |
| Supported Chains | Polygon, Avalanche, Arbitrum <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a> | Ethereum (as of now) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>           |
| Current Status   | Going through a migration <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> | Working to onboard more Layer 2 solutions and protocols <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>; working to get V2 onto Autochain <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a> |

## [[New features in Spiritswap V2 | New Features]] in xDollar V2 (Demo)

The xDollar V2 interface provides several sections:
*   **X Home:** Displays the platform's dashboard, showing protocol earnings and collateral ratio (CR ratio) <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **X Bank:** Where users borrow the stablecoin XIM, currently with ETH. Future plans include borrowing with MATIC when connected to Polygon <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **X Pool:** Allows users to supply XIM into a stability pool to earn more ETH and Space tokens <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The protocol uses the XIM in this pool to buy liquidated assets, allowing users to acquire assets like MATIC at a discount if they are bullish on them <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **X Stake:** Used for staking Space tokens to receive XSpace, a governance token <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Staking XSpace allows participation in governance voting and earning a share of the protocol's revenue <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. The longer the lock-up period, the more XSpace is earned <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **X Farm:** Enables farming Space by staking XIM 3-Curve LP tokens via Curve <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Advanced Features (Demonstrated with V1)

Two additional features demonstrated using xDollar V1 are liquidation and redemption <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>:
*   **Liquidation (Risky Troll):** Allows a user to liquidate someone else's position if their collateral ratio is low (e.g., close to 110%) <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. The liquidator pays xUSD and receives the collateral at a discount <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Redemption:** Designed for users to participate in arbitrage events <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. For example, if xUSD de-pegs to $0.90, a user can come to the platform with xUSD, which will be valued at $1 <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This is typically carried out by bots but can also be done by users <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Redemption is distinct from paying back a loan <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Future Outlook

Currently, xDollar V2 is only on Ethereum, with anticipation for deployment on other chains <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. More information about [[Introduction to xDollar protocol | xDollar]] can be found on its Twitter (@xdollar_fi) or Discord <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.