---
title: How to recognize scam wallets
videoId: WiGlovQEi3I
---

From: [[goingonchain]] <br/> 

A common scam involves enticing users to deposit gas fees into a fraudulent wallet, only for the funds to be immediately siphoned away. This specific scam targets USDT (Tether) and operates on the Tron network, requiring TRX as a gas fee <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## How the Scam Works

1.  **Initial Contact**
    Scammers typically initiate contact via social media platforms like Telegram or Instagram <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. They claim to be experiencing difficulty withdrawing assets from their wallet and ask for assistance <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They provide their wallet address and what they describe as a "seed phrase" (though the scam relies on wallet permissions, not a true seed phrase giveaway) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

2.  **The Bait**
    Upon loading the provided wallet, users will see a significant amount of USDT (e.g., $1135) but no gas fee (TRX) <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>, <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The scam's objective is to trick the user into depositing TRX to facilitate the "withdrawal" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

3.  **The Trap**
    The moment any gas fee (TRX) is loaded into the scam wallet, it is immediately transferred to another wallet controlled by the scammer <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## How to Identify a Scam Wallet

The key to recognizing this specific [[common_cryptocurrency_scam_tactics | scam tactic]] lies in examining the wallet's permissions on the blockchain explorer (like Tron Scan for Tron wallets) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

*   **Normal Wallet Permissions:**
    In a legitimate wallet, the "owner permission" and "active permission" will both match the wallet's main address <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For example, if the wallet address is `knifi au`, both the owner and active permissions would also be `knifi au` <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

*   **Scam Wallet Permissions:**
    A scam wallet will display a discrepancy:
    *   The provided wallet address (e.g., `gt9h`) will *not* be the owner permission <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   The "owner permission" will belong to a different wallet address (e.g., `w19c`) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   Similarly, the "active permission" will also belong to this different wallet (e.g., `w19c`) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   Attempting to modify the access permissions (e.g., to put your own address) will require a transaction fee (e.g., 100 TRX), which will also be immediately redirected to another wallet upon saving <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## How Funds are Stolen

Any TRX sent to the compromised wallet (e.g., `gt9h`) is automatically and immediately forwarded to the scammer's main wallet (e.g., `2qpe`) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>, <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This scammer's wallet aggregates all the stolen gas fees <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. In one instance, the scammer's wallet accumulated approximately $2,000 in gas fees within 16 minutes <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

It is crucial to be careful as people continue to fall victim to these scams <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>, <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Always exercise caution and verify wallet permissions to [[protecting_against_scams | protect against scams]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.