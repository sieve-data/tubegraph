---
title: Transaction flow and mempool in blockchain
videoId: w9SHvQNKqEM
---

From: [[goingonchain]] <br/> 

To understand how blockchain networks function, it's crucial to grasp the process of transaction flow and the role of the mempool <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## What is a Transaction?

A transaction in a blockchain network refers to any action that changes the state of the ledger <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Examples include:
*   Swapping tokens (e.g., $10 of USDC to ETH on Uniswap) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
*   Making a purchase on an NFT marketplace like OpenSea <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Sending a token to another wallet <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

## The Mempool: A Holding Area

All these transactions enter a "mempool" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The mempool is publicly viewable and acts as a holding area for all pending transactions <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Validator's Role

Validators are responsible for picking up transactions from the mempool <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Their role involves:
1.  **Validating Transactions**: Ensuring the legitimacy of the transactions <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
2.  **Appending to the Blockchain**: Once validated, transactions are appended to the public ledger, which is the blockchain <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
3.  **Transaction Success**: After this process, the transaction is successful <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

Validators possess the power to select pending transactions based on economic incentives <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Searchers and Bots

In practice, independent actors known as "searchers" actively monitor the mempool for profitable transactions <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Most searchers utilize bots to perform this task <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. These searchers then push the identified profitable transactions to the validators <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. The profits generated from these activities are often shared with the block producers <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.