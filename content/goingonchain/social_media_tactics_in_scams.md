---
title: Social media tactics in scams
videoId: WiGlovQEi3I
---

From: [[goingonchain]] <br/> 

Scammers frequently utilize social media platforms to initiate cryptocurrency scams, particularly those involving USDT (Tether) <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. These tactics often rely on deception and manipulation to trick individuals into sending cryptocurrency to malicious actors.

## How the Scam Works

The scam typically begins with an unsolicited direct message (DM) on social media platforms like Telegram or Instagram <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Initial Contact and Ploy

The scammer will provide a wallet address and seed phrase, claiming they are unable to withdraw assets themselves and are asking for help <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. An example of this ploy is a scammer asking for help due to being sick, providing a seed phrase and wallet address, and requesting assistance to withdraw assets <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### The Lure: "Stuck" Funds

Upon loading the provided wallet, the victim will see a substantial amount of USDT, for instance, about 1,135 USDT <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. However, the wallet will have no "gas" (transaction fees) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This creates the illusion that the funds are genuinely "stuck" and merely require a small amount of gas to be released <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### The Trap: Gas Fee Theft

The moment a victim attempts to "help" by loading gas into the wallet, that gas fee is immediately sent to another wallet controlled by the scammer <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## How [[How cryptocurrency wallets are manipulated in scams | Cryptocurrency Wallets Are Manipulated]]

The core of this scam lies in the manipulation of wallet permissions, which can be identified by examining the wallet on a blockchain explorer like TronScan <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Discrepant Permissions

In a compromised wallet (e.g., address "gt9h"), the "owner permission" and "active permission" will not match the displayed wallet address <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Instead, these permissions will belong to a different wallet (e.g., "w19c") <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. In contrast, a normal wallet's owner and active permissions will be the same as the wallet's main address <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Attempting to "Help" Costs More

If a victim tries to edit the access permissions or put their own address, clicking "save" will incur a fee (e.g., 100 TRX) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This fee, like the gas fee, is also immediately siphoned to another wallet <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Scammer's Accumulation Wallet

Any transaction fees (like TRX) sent into the scammer's provided wallet (e.g., "gt9h") are instantly forwarded to the actual scammer's wallet (e.g., "2qpe") <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This accumulating wallet can rapidly gather significant sums; for example, one such wallet accumulated about two thousand dollars in 16 minutes <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Impact and Prevention

Despite the seemingly obvious nature of the trick, people continue to fall victim to this scam, sending TRX as gas fees or attempts to help, which are then diverted to the scammer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

It is important for users to exercise [[Protection against scams | protection against scams]] and practice [[Cybersecurity tips | cybersecurity tips]]. There are many scams circulating, and caution is advised <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

> [!TIP] Share this information with others involved in [[crypto scam awareness | cryptocurrency]] to help them [[Preventing cryptocurrency scams | avoid]] falling for such tricks <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Recognize [[recognizing_red_flags_in_online_scams | red flags in online scams]], especially when dealing with unsolicited requests for help involving cryptocurrency wallets.