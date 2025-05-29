---
title: How cryptocurrency wallets are manipulated in scams
videoId: WiGlovQEi3I
---

From: [[goingonchain]] <br/> 

A specific type of USDT scam is actively circulating, designed to exploit individuals by manipulating cryptocurrency wallet permissions <a class="yt-timestamp" data-t="00:00:05">00:00:05</a>. This scam targets users through social media and leverages technical vulnerabilities in how wallet permissions are managed on blockchain explorers like TronScan <a class="yt-timestamp" data-t="00:01:19">00:01:19</a>.

## How the Scam Works

The scam typically begins with an unsolicited direct message on social media platforms like Telegram or Instagram <a class="yt-timestamp" data-t="00:00:12">00:00:12</a>.

1.  **Initial Contact and Deception**: The scammer contacts a potential victim, providing their wallet address and seed phrase <a class="yt-timestamp" data-t="00:00:15">00:00:15</a>. They claim to be experiencing difficulty withdrawing assets from the wallet and ask for help, often fabricating a story such as being sick <a class="yt-timestamp" data-t="00:00:25">00:00:25</a>, <a class="yt-timestamp" data-t="00:00:32">00:00:32</a>.
2.  **The Wallet Trap**: When the victim loads the provided wallet, they will see a significant amount of USDT (e.g., $1135) present, but no "gas" (TRX for transaction fees) <a class="yt-timestamp" data-t="00:00:42">00:00:42</a>, <a class="yt-timestamp" data-t="00:01:06">00:01:06</a>.
3.  **The Siphoning Mechanism**: The moment the victim sends "gas" (TRX) to the wallet to facilitate the withdrawal, that TRX is immediately transferred to another wallet controlled by the scammer <a class="yt-timestamp" data-t="00:00:54">00:00:54</a>, <a class="yt-timestamp" data-t="00:00:56">00:00:56</a>.

## Technical Manipulation of Wallet Permissions

The core of this scam lies in the manipulation of wallet permissions, which can be observed by inspecting the wallet on a blockchain explorer like TronScan <a class="yt-timestamp" data-t="00:01:02">00:01:02</a>, <a class="yt-timestamp" data-t="00:01:19">00:01:19</a>.

*   **Owner and Active Permissions**: For a legitimate, normal wallet, the "owner permission" and "active permission" addresses are identical to the wallet's public address <a class="yt-timestamp" data-t="00:02:08">00:02:08</a>, <a class="yt-timestamp" data-t="00:02:14">00:02:14</a>.
*   **Scam Wallet Discrepancy**: In the scam wallet, while the displayed wallet address (e.g., GT9H) holds the USDT, the actual "owner permission" and "active permission" are set to a different address (e.g., W19C) <a class="yt-timestamp" data-t="00:01:28">00:01:28</a>, <a class="yt-timestamp" data-t="00:01:38">00:01:38</a>, <a class="yt-timestamp" data-t="00:01:41">00:01:41</a>.
*   **Attempting to "Fix" the Wallet**: If a victim attempts to "edit access" or change the permissions to their own address, this action itself requires a TRX fee (e.g., 100 TRX) <a class="yt-timestamp" data-t="00:01:48">00:01:48</a>, <a class="yt-timestamp" data-t="00:01:52">00:01:52</a>. The moment this fee is sent, it is also siphoned off to the scammer's wallet <a class="yt-timestamp" data-t="00:01:56">00:01:56</a>.

## Scammer's Accumulation Wallet

The "gas" fees sent by victims are immediately redirected from the provided wallet (e.g., GT9H) to a centralized scammer's wallet (e.g., 2QPE) <a class="yt-timestamp" data-t="00:02:43">00:02:43</a>, <a class="yt-timestamp" data-t="00:03:04">00:03:04</a>. This accumulation wallet continuously collects these small transaction fees, which can quickly add up to significant amounts (e.g., $2000 in 16 minutes) <a class="yt-timestamp" data-t="00:03:09">00:03:09</a>, <a class="yt-timestamp" data-t="00:03:14">00:03:14</a>.

## [[crypto_scam_awareness | Protection against Scams]]

Despite the sophisticated nature of this scam, people continue to fall victim, sometimes out of a desire to help <a class="yt-timestamp" data-t="00:02:27">00:02:27</a>, <a class="yt-timestamp" data-t="00:02:35">00:02:35</a>. It is crucial to exercise extreme caution and share information about such scams within the cryptocurrency community <a class="yt-timestamp" data-t="00:03:30">00:03:30</a>. [[Importance of cryptocurrency security | Being vigilant]] can help [[Preventing cryptocurrency scams | prevent financial loss]] <a class="yt-timestamp" data-t="00:03:36">00:03:36</a>.