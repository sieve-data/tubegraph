---
title: Social media and Telegram scams
videoId: WiGlovQEi3I
---

From: [[goingonchain]] <br/> 

A specific type of [[common_cryptocurrency_scam_tactics | cryptocurrency scam]] involving USDT is currently circulating, primarily initiated through social media platforms like Telegram and Instagram <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This scam targets individuals by exploiting their willingness to help, leading to the siphoning of gas fees.

## How the Scam Works

This scam operates using a clever deception that preys on a user's attempt to assist.

### Initial Contact

Scammers typically initiate contact via direct messages (DMs) on platforms such as Telegram or Instagram <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. They provide a wallet address and seed phrase, claiming they are unable to withdraw assets themselves and need assistance <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. An example given is a scammer feigning illness to elicit help <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### The Lure

Upon loading the provided wallet, victims will observe a significant amount of USDT, for instance, $1135, within it <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. However, the wallet will conspicuously lack the necessary gas fees (TRX) required for any transactions <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This creates a psychological trigger for the victim to "help" by depositing the missing gas fees <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This is a common [[psychological_tricks_in_scams | psychological trick in scams]] to entice victims.

### The Trap: [[gas_fees_siphoning_in_crypto_scams | Gas Fees Siphoning]]

The moment a victim deposits gas fees into the scammer's wallet, the funds are immediately transferred to another wallet controlled by the scammer <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This means the gas fees disappear instantly, making it impossible for the victim to withdraw the USDT.

## Technical Explanation: How to [[how_to_recognize_scam_wallets | Recognize Scam Wallets]]

The key to understanding this [[usdt_tron_scam_explanation | USDT Tron scam]] lies in examining wallet permissions on TronScan.

### Examining Wallet Permissions on TronScan

When inspecting the scammer's provided wallet address (e.g., an address ending in GT9H) on TronScan, users might notice a critical discrepancy <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Although the displayed address is GT9H, the "owner permission" for that account is actually held by a different wallet, such as one ending in W19C <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This is also true for the "active permission" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This hidden permission structure is what allows the scammer to instantly siphon funds.

### Attempting to Edit Permissions

If a victim attempts to "help" by editing the access permissions to add their own address, clicking "save" incurs a fee of 100 TRX <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The moment this TRX is sent, it too is immediately redirected to another scammer-controlled wallet <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Normal Wallet Comparison

In contrast, a normal, legitimate Tron wallet (e.g., an address ending in KNIFIAU) will show that its "owner permission" and "active permission" keys are the same as the wallet's address itself <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This consistency is a key indicator of a legitimate wallet <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Impact and Warning

Despite the technical nature of the scam, many individuals are falling victim to it <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Gas fees sent to these scam wallets are consistently diverted to the actual scammer's wallet (e.g., 2QPE), which accumulates these siphoned funds <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. For example, a scammer's wallet was seen to have accumulated approximately $2,000 in just 16 minutes through these transactions <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. While some speculate this method might be used to scam other scammers, it undeniably traps unsuspecting individuals as well <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Prevention

It is crucial for individuals involved in crypto to be aware of such [[crypto_scam_awareness | crypto scam awareness]] and [[protecting_against_scams | protecting against scams]] <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Always exercise extreme caution with unfamiliar wallets and never send funds to an address if you suspect any deceptive practices.