---
title: Bitcoin mining and block creation
videoId: bBC-nXj3Ng4
---

From: [[3blue1brown]] <br/> 

[[understanding_the_basics_of_bitcoin_and_cryptocurrency | Bitcoin]], like any [[understanding the basics of Bitcoin and cryptocurrency | cryptocurrency]], is fundamentally a ledger, where the history of transactions serves as the currency itself <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>. This ledger is distributed, meaning everyone keeps their own copy <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. When a transaction occurs, it is broadcast to the network for individuals to record on their personal ledgers <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.

The core challenge in a decentralized system is achieving consensus on what constitutes the correct and agreed-upon ledger <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. [[blockchain_and_proof_of_work_in_the_bitcoin_protocol | Bitcoin]] addresses this by trusting whichever ledger has demonstrated the most computational work <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>.

## Proof of Work and Cryptographic Hash Functions

The foundation of this system relies on a concept called a [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash function]], such as SHA256 <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. These functions take any input (message or file) and produce a fixed-length string of bits, like [[256_bit_security_and_its_implications | 256 bits]], as an output or "hash" <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>. Even a slight change in the input drastically alters the resulting hash, making it unpredictable <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>. Crucially, it is infeasible to compute these functions in reverse; finding an input that produces a specific hash requires brute-force guessing <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>.

This property enables a "proof of work" <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>. To prove a significant amount of computational effort has been expended, one must find a "special number" (often called a nonce) which, when appended to a list of transactions, results in a hash that starts with a predetermined number of zeros <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>. For example, if the requirement is 30 leading zeros, it would, on average, take a billion guesses to find such a number <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>. Once found, this proof of work is quick and easy to verify <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>.

## Blocks and the Blockchain

The ledger is organized into "blocks," each containing a list of transactions along with its [[blockchain_and_proof_of_work_in_the_bitcoin_protocol | proof of work]] <a class="yt-timestamp" data-t="16:19:00">[16:19:00]</a>. A block is only considered valid if it possesses a valid [[blockchain_and_proof_of_work_in_the_bitcoin_protocol | proof of work]] <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>. To maintain a standard order and integrity, each block must include the hash of the preceding block in its header <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>. This chaining mechanism ensures that altering any past block would invalidate all subsequent blocks, requiring immense computational effort to re-calculate all proofs of work <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>. Due to this chaining, the ledger is commonly referred to as a [[blockchain_and_proof_of_work_in_the_bitcoin_protocol | blockchain]] <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>.

## Bitcoin Mining

Anyone can become a "block creator" or [[bitcoin_mining_and_applicationspecific_integrated_circuits | miner]] <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>. This process involves:
1.  Listening for broadcasted transactions <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>.
2.  Collecting these transactions into a block <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>.
3.  Performing intensive computational work to find the special number (nonce) that makes the block's hash meet the required criteria (e.g., starting with many zeros) <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.
4.  Broadcasting the newly found block to the network <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>.

This activity is called [[bitcoin_mining_and_applicationspecific_integrated_circuits | mining]] because it requires significant computational effort and introduces new currency into the economy <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>. From a miner's perspective, each block represents a "miniature lottery" where they are guessing numbers rapidly until a winner is found <a class="yt-timestamp" data-t="18:41:00">[18:41:00]</a>.

### Block Reward and New Currency

To incentivize [[bitcoin_mining_and_applicationspecific_integrated_circuits | block creators]], a "block reward" is included in each new block <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>. This special transaction, typically placed at the top of the block, mints new currency (e.g., 10 ledger dollars or [[understanding the basics of Bitcoin and cryptocurrency | Bitcoin]]) out of thin air, an exception to normal transaction rules as it doesn't come from any sender <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>. This means the total amount of currency in the economy increases with each new block <a class="yt-timestamp" data-t="18:13:00">[18:13:00]</a>.

Initially, [[understanding the basics of Bitcoin and cryptocurrency | Bitcoin]] block rewards were 50 [[understanding the basics of Bitcoin and cryptocurrency | Bitcoin]] per block <a class="yt-timestamp" data-t="22:32:00">[22:32:00]</a>. This reward is cut in half approximately every four years (or every 210,000 blocks) <a class="yt-timestamp" data-t="22:49:00">[22:49:00]</a>. Currently, the reward is 12.5 [[understanding the basics of Bitcoin and cryptocurrency | Bitcoin]] per block <a class="yt-timestamp" data-t="22:56:00">[22:56:00]</a>. Due to this geometrically decreasing reward, the total supply of [[understanding the basics of Bitcoin and cryptocurrency | Bitcoin]] is capped at 21 million <a class="yt-timestamp" data-t="23:00:00">[23:00:00]</a>.

### Transaction Fees

In addition to the block reward, [[bitcoin_mining_and_applicationspecific_integrated_circuits | miners]] can also earn [[transaction_fees_and_scalability_issues_in_bitcoin | transaction fees]] <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>. Users can optionally include a fee with their payment, which is collected by the [[bitcoin_mining_and_applicationspecific_integrated_circuits | miner]] who includes that transaction in their block <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>. This incentivizes [[bitcoin_mining_and_applicationspecific_integrated_circuits | miners]] to include a user's transaction in the next block <a class="yt-timestamp" data-t="23:29:00">[23:29:00]</a>.

### Difficulty Adjustment and Block Time

The [[blockchain_and_proof_of_work_in_the_bitcoin_protocol | Bitcoin protocol]] periodically adjusts the difficulty of the [[blockchain_and_proof_of_work_in_the_bitcoin_protocol | proof of work]] (the number of leading zeros required) to ensure that a new block is found, on average, every 10 minutes <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>. As more [[bitcoin_mining_and_applicationspecific_integrated_circuits | miners]] join the network and computational power increases, the challenge becomes harder to maintain this consistent block time <a class="yt-timestamp" data-t="22:12:00">[22:12:00]</a>.

## Decentralized Consensus and Trust

The key to decentralized consensus is that everyone agrees to prioritize the longest [[blockchain_and_proof_of_work_in_the_bitcoin_protocol | blockchain]], which by definition represents the one with the most computational work invested <a class="yt-timestamp" data-t="19:10:00">[19:10:00]</a>. If two conflicting chains appear, the network waits for one to become longer before committing <a class="yt-timestamp" data-t="19:22:00">[19:22:00]</a>.

For a transaction to be considered trustworthy, it's not enough to simply hear a new block <a class="yt-timestamp" data-t="21:23:00">[21:23:00]</a>. One should wait for several additional blocks to be added on top of it <a class="yt-timestamp" data-t="21:29:00">[21:29:00]</a>. This confidence arises because a fraudulent chain would require an attacker to possess over 50% of the network's total computing power to consistently outpace the legitimate chain <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>. Without such dominance, the honest chain will almost certainly grow faster, eventually causing any fraudulent chain to be rejected by the network <a class="yt-timestamp" data-t="21:03:00">[21:03:00]</a>.

## Scalability Concerns

In [[understanding the basics of Bitcoin and cryptocurrency | Bitcoin]], each block is limited to approximately 2400 transactions <a class="yt-timestamp" data-t="23:36:00">[23:36:00]</a>. This relatively small block size leads to slower transaction processing compared to traditional payment systems like Visa, which can handle thousands of transactions per second <a class="yt-timestamp" data-t="23:41:00">[23:41:00]</a>. This limitation contributes to higher [[transaction_fees_and_scalability_issues_in_bitcoin | transaction fees]], as [[bitcoin_mining_and_applicationspecific_integrated_circuits | miners]] prioritize transactions with higher fees when constructing new blocks <a class="yt-timestamp" data-t="23:56:00">[23:56:00]</a>.

***

> "If you understand it, you understand the heart of [[understanding the basics of Bitcoin and cryptocurrency | Bitcoin]] and other [[understanding the basics of Bitcoin and cryptocurrency | cryptocurrencies]]." <a class="yt-timestamp" data-t="22:20:00">[22:20:00]</a>