---
title: Gas fees siphoning in crypto scams
videoId: WiGlovQEi3I
---

From: [[goingonchain]] <br/> 

This article details a specific type of cryptocurrency scam where fraudsters exploit [[understanding_cryptocurrency_transaction_fees | gas fees]] to siphon funds from unsuspecting users <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This scam, particularly prevalent with USDT on networks requiring TRX for gas, preys on an individual's willingness to help or their desire to acquire seemingly available assets <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## How the Scam Works

### Initial Contact and Deception
The scam typically begins with a direct message on social media platforms like Telegram or Instagram <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. The scammer provides a wallet address and its seed phrase, claiming they are unable to withdraw assets due to some difficulty, such as illness, and ask for assistance <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### The Lure: Apparent Funds
Upon loading the provided wallet, the victim observes a substantial amount of USDT (e.g., $1135) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. However, the wallet conspicuously lacks the necessary gas (e.g., TRX for a Tron wallet) to perform any transactions <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### The Trap: Gas Fee Siphoning
The moment the victim sends gas to this wallet, the funds are immediately siphoned off <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The gas fee is automatically forwarded to another wallet controlled by the scammer <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Technical Mechanism: Permission Control
The core of this scam lies in the manipulation of wallet permissions:
*   **Controlled Permissions:** Unlike a normal wallet where the owner permission matches the wallet address, the scam wallet's owner permission (e.g., for `gt9h`) is set to a different address (e.g., `w19c`) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. The active permission also belongs to this separate, controlling address <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Automatic Forwarding:** Any incoming gas (like TRX) is instantly redirected from the public-facing wallet address to the scammer's wallet <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. For example, gas sent to `gt9h` is immediately sent to `2qpe` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Attempted Permission Changes:** Even if a victim attempts to "edit access" and add their own address, this action itself requires a [[understanding_cryptocurrency_transaction_fees | gas fee]] (e.g., 100 TRX), which is also immediately sent to the scammer's wallet <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### The Scammer's Accumulation Wallet
The collected [[understanding_cryptocurrency_transaction_fees | gas fees]] are accumulated in a single wallet controlled by the scammer (e.g., `2qpe`) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This wallet can quickly accumulate significant amounts, such as $2,000 in a short period <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## Preventing Such Scams
While some speculate this scam might target other scammers, many unsuspecting individuals also fall victim <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Due to the prevalence of [[common_cryptocurrency_scam_tactics | crypto scams]], [[crypto_scam_awareness | awareness]] and caution are paramount <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. It is crucial to be careful and share information about these tactics to help others avoid them <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.