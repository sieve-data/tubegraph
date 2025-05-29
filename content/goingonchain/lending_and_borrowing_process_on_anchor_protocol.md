---
title: Lending and borrowing process on Anchor Protocol
videoId: jt74C4Es5Ns
---

From: [[goingonchain]] <br/> 

[[Interest rates on Anchor Protocol | Anchor Protocol]] is a decentralized finance (DeFi) platform designed for peer-to-peer lending and borrowing [00:00:15](<a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>). It allows users to deposit funds to earn a stable yield or borrow money using cryptocurrency as [[role_of_collateral_in_anchor_protocol | collateral]] [00:00:23](<a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>).

## Key Participants

*   **Lenders (e.g., Alice)**: Individuals who deposit money into the protocol. They can earn a high annual percentage rate (APR), typically ranging from 19% to 20% [00:00:19](<a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>).
*   **Borrowers (e.g., Bob)**: Individuals who borrow money from the protocol. They must provide crypto as [[role_of_collateral_in_anchor_protocol | collateral]] and pay a floating interest rate [00:00:23](<a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>). Borrowers also receive ANC tokens as a reward for borrowing [00:00:29](<a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>).

## How Anchor Maintains High Yield

The protocol sustains its high yield for lenders through a combination of borrower-paid interest and staking rewards from the borrower's [[role_of_collateral_in_anchor_protocol | collateral]] [00:00:33](<a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>).

### Components Contributing to Yield

1.  **Borrow APR**: The interest rate borrowers pay on their loans [00:00:38](<a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>). For instance, a borrower might pay 21.55% APR on a borrowed amount [00:00:42](<a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>).
2.  **Staking Reward**: When borrowers provide their crypto as [[role_of_collateral_in_anchor_protocol | collateral]], it is staked, generating a staking reward [00:00:50](<a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>). This reward, such as 5.83%, contributes to the overall yield [00:00:53](<a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>).

### Example of Funds Flow

Consider an example where Alice lends $1,000, expecting to earn 20% APR, and Bob borrows $1,000 using $3,000 of bLuna as [[role_of_collateral_in_anchor_protocol | collateral]]:

1.  **Bob's Borrowing Cost**: Bob pays 22% interest on the $1,000 borrowed, amounting to $220 [00:01:06](<a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>).
2.  **Staking Reward from Bob's Collateral**: From his $3,000 [[role_of_collateral_in_anchor_protocol | collateral]], Bob's staked assets generate a 5% reward, which is $150 [00:01:10](<a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>).
3.  **Total Collected**: The total amount collected from Bob's borrowing activities (interest + staking reward) is $370 ($220 + $150) [00:01:13](<a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>).
4.  **Distribution of Collected Funds**:
    *   **To Alice (Lender)**: $200 is paid to Alice to fulfill her 20% APR expectation on her $1,000 deposit [00:01:15](<a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>).
    *   **To Anchor Yield Reserve**: The remaining $170 ($370 - $200) goes into the Anchor yield reserve [00:01:17](<a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>). This reserve helps stabilize the yield paid to lenders, particularly during periods of low borrowing demand or fluctuating staking rewards.

This mechanism demonstrates the power of decentralized finance in generating yield for participants [00:01:20](<a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>).