---
title: NFT liquidation process
videoId: lCV3tm8QY-k
---

From: [[goingonchain]] <br/> 

The [[nft_lending_and_borrowing | NFT lending and borrowing]] market has evolving mechanisms for managing loan defaults, particularly through NFT liquidation processes <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. Platforms like BenDAO enable users to bid on NFTs that are in a state of liquidation <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

## Overview of BenDAO's Liquidation Mechanism

BenDAO is a platform that facilitates [[nft_lending_and_borrowing | NFT lending and borrowing]] <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. When an NFT owner borrows ETH against their NFT, they are subject to liquidation if the value of the NFT drops relative to the borrowed amount <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

For instance, if an owner borrowed 10.82 ETH against a Bored Ape Yacht Club (MAYC) NFT that had a floor price of 12.32 ETH, and the loan becomes undercollateralized, the NFT enters a "liquidating state" <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

## The Bidding Process

Once an NFT is in a liquidating state, the original owner is given a 48-hour window to redeem their NFT <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. If the owner fails to redeem the NFT within this period, it will be awarded to the highest bidder <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

Key rules for bidding:
*   The bid price must always exceed the current highest bid by at least one percent <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

## Risks for Bidders

While bidding on liquidating NFTs can potentially offer a discount, it comes with specific risks for bidders:
*   **Locked Capital** When a bid is placed, the bidder's ETH is locked up for 48 hours <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Bidder Risk** This locking of funds creates a risk for the bidder, as their capital is inaccessible during this period <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. This risk is cited as a reason why not many people actively bid on these liquidations <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

BenDAO aims to provide liquidity for NFT holders but must address these underlying problems within its system <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.