---
title: Tron USDT scam overview
videoId: WiGlovQEi3I
---

From: [[goingonchain]] <br/> 

A prevalent scam targeting Tron (TRX) users involves a deceptive scheme designed to steal cryptocurrency by exploiting wallet permissions and gas fees <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This scam, often spread through social media, manipulates users into sending TRX to what appears to be a legitimate wallet with frozen USDT assets <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## How the Scam Works

The scam typically begins with a direct message (DM) on social media platforms like Telegram or Instagram <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
1.  **Initial Contact**: A scammer DMs a user, providing a wallet address and seed phrase <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
2.  **Plea for Help**: The scammer claims to be unable to withdraw assets due to some difficulty (e.g., sickness) and asks the user for help <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
3.  **Wallet Contents**: If the user loads the provided wallet, they will see a significant amount of USDT (e.g., 1135 USDT) <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. However, the wallet will have no "gas" (TRX) to cover transaction fees <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
4.  **The Trap**: The user, attempting to help, will then load TRX (gas) into the wallet to enable the withdrawal <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
5.  **Gas Theft**: The moment TRX is deposited, it is immediately and automatically sent to another wallet controlled by the scammer <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Technical Details: Wallet Permissions

The core of this scam relies on manipulated wallet permissions on the Tron network <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Deceptive Address**: The scammer provides a wallet address (e.g., GT9H) that appears to be the primary address for the USDT <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Tron Scan Check**: When a user inspects this wallet on Tron Scan, they can check the "Account" section <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Permission Mismatch**: A crucial detail is revealed: the "Owner Permission" for the wallet (e.g., GT9H) is actually controlled by a *different* address (e.g., W19C) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The "Active Permission" also belongs to this separate, hidden address <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Failed Attempts to Change**: If a user attempts to "edit access" and change the permission to their own address, this action itself costs 100 TRX <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This TRX, like the gas fees, is immediately sent to the scammer's wallet upon saving <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Normal Wallet Comparison**: In contrast, a normal Tron wallet's owner permission and active permission keys will match its main address <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Scammer's Accumulation Wallet

All the stolen gas fees are aggregated into a single scammer's wallet (e.g., 2QPE) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This wallet continuously accumulates TRX from victims <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. As of a recent recording, this scam wallet had accumulated approximately $2,000 within a short period, demonstrating its active nature and success in deceiving users <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Awareness and Prevention

Despite the technical nature of the scam, many people continue to fall victim to it, sending TRX in an attempt to help <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While some speculate that this trick might also be used to scam other scammers, unsuspecting individuals are also at risk <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

To prevent falling victim to this and other [[crypto_scam_awareness | cryptocurrency scams]], users should:
*   Be wary of unsolicited DMs on social media asking for help with cryptocurrency wallets <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   Never load funds into a wallet provided by an unknown party, especially if a seed phrase is shared <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   Always verify wallet permissions on Tron Scan or similar blockchain explorers to ensure the owner and active permissions match the provided address <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   Share information about such scams to help others avoid them <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   Exercise extreme caution with any cryptocurrency transactions <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.