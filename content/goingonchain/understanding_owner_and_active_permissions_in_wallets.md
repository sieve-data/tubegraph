---
title: Understanding owner and active permissions in wallets
videoId: WiGlovQEi3I
---

From: [[goingonchain]] <br/> 

## The USDT "No Gas" Scam

A common scam circulating on social media, particularly Telegram and Instagram, involves fraudsters direct-messaging individuals with a wallet address and seed phrase <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The scammer claims to be unable to withdraw assets due to a supposed difficulty, often feigning illness or other issues, and asks for help <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

When the victim loads the provided wallet, they will see USDT (e.g., 1135 USDT) present <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. However, there is no "gas" (transaction fee currency like TRX for Tron wallets) in the wallet <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The moment the victim deposits gas into the wallet, that gas is immediately siphoned off to another wallet <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### How the Scam Works

The core of this scam lies in manipulating wallet permissions. When examining the scammer's wallet address (e.g., `gt9h`) on a blockchain explorer like Tronscan <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>:

*   **Owner Permission**: The "owner permission" for the `gt9h` wallet is not `gt9h` itself, but rather a different wallet address, `w19c` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Active Permission**: Similarly, the "active permission" (which controls the key for access) also belongs to `w19c` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

This setup means that while the victim can see the USDT balance, they do not have the necessary permissions to control the wallet or its funds. The actual control lies with the `w19c` wallet, which instantly sweeps any incoming gas fees.

### Understanding Wallet Permissions

To highlight the deceptive nature of the scam wallet, it's crucial to understand how permissions work in a normal, legitimate wallet.

#### Normal Wallet Permissions

In a standard wallet (e.g., address `knifi au`), the owner and active permissions are directly tied to the wallet's address <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:

*   **Owner Permission**: The owner permission is the same as the wallet address itself (e.g., `knifi au`) <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Active Permission**: The key for the active permission is also the wallet address (e.g., `knifi au`) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This symmetrical setup ensures that the person holding the wallet's private key or seed phrase has full control over its assets and permissions.

#### Scam Wallet Permissions

In contrast, the scam wallet (e.g., `gt9h`) is configured to divert any incoming gas fees <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>:

*   Any transaction (like adding TRX for gas) sent to `gt9h` is immediately forwarded to another wallet, such as `2qpe` <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   The wallet `2qpe` acts as the actual scammer's wallet, accumulating all the gas fees sent by unsuspecting victims <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### The "Edit Access" Trap

Another layer to this scam is the "edit access" option often found on blockchain explorers. If a victim attempts to change the wallet's permissions or add their own address to the access list, clicking "save" can cost approximately 100 TRX <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The moment this TRX is sent, it is also instantly transferred to the scammer's receiving wallet <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Scam Profitability and Prevention

Despite the seemingly obvious nature of the trick, people continue to fall victim to this scam, sending TRX for gas fees which are then siphoned off <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. As of the video's recording, the scammer's wallet `2qpe` had accumulated about $2,000 in just 16 minutes <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

It is advised to be extremely cautious when dealing with wallet addresses and seed phrases provided by others, especially those requesting help with withdrawals <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Always verify wallet permissions on a blockchain explorer if you suspect foul play.