---
title: Largest hack in crypto history  Bybit
videoId: Ggatja5uOT0
---

From: [[bankless]] <br/> 

On a recent Friday, Bybit, a significant Asian cryptocurrency exchange, suffered a massive security breach, losing approximately $1.5 billion in ETH, staked ETH (stETH), Wrapped ETH (wETH), and other ERC-20 tokens <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>, <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. This event marked the largest hack in crypto's history, accounting for 13% of all exploited funds ever <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>, and was twice the size of the previous second-largest hack, the $600 million Ronin bridge exploit in March 2022 <a class="yt-timestamp" data-t="00:22:39">[00:22:39]</a>.

## The Perpetrator: Lazarus Group (North Korea)

Both the Bybit and Ronin bridge exploits were attributed to the Lazarus Group, a cybercrime organization linked to North Korea <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Bybit's Crisis Response

Despite the immense loss, Bybit's leadership garnered significant praise for their crisis response <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. Ben, a representative from Bybit, immediately initiated a calm and collected live stream, taking ownership of the situation and detailing the response efforts, which helped to calm widespread fears <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. This approach was heralded as one of the best in the industry's history <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.

Bybit, known for having one of the most robust Proofs of Reserve, proves daily that they hold excess funds for nearly every asset offered on their exchange to cover client liabilities <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>. Even with the $1.5 billion loss, they had ample reserves, including $8-19 billion in other assets in their treasury <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>, <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>. The crypto industry also stepped in to support Bybit, lending them ETH to honor client withdrawals <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>, <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>. This cooperative effort was notably different from the circumstances surrounding Sam Bankman-Fried and FTX <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

The MNT token, associated with Bybit, saw a significant drop of 27% among the top 100 crypto assets following the news <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

## How the Hack Happened

The attack specifically targeted Bybit's cold wallet signers through a sophisticated phishing campaign utilizing the Gnosis Safe front-end <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>, <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.

*   **Compromised Front-End:** Hackers gained access to Bybit's front-end interface, specifically their Gnosis Safe integration <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>. Other Gnosis Safe users were unaffected <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   **Malicious JavaScript Injection:** The attackers injected malicious JavaScript into Safe's AWS infrastructure, deceiving signers into unknowingly approving malicious transactions <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>, <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.
*   **Proxy Contract Reassignment:** A forensic review by Galaxy's GK8 revealed that the initial malicious transaction was extremely subtle, appearing to move no funds but actually reassigning the proxy contract of Bybit's safe to one controlled by the Lazarus Group <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>, <a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a>.
*   **Fund Sweeping:** Two minutes after the proxy contract was reassigned, the hackers swept all funds from the cold storage address <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.
*   **Failure to Detect:** Bybit's core infrastructure was not compromised, but its security controls failed to detect the attack <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>.

This incident specifically targeted Bybit's cold wallet, which typically holds the vast majority of an exchange's funds offline and is considered highly secure <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>. This is in contrast to typical hot wallet hacks which are connected to the internet for processing withdrawals and deposits <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>.

## Key Takeaways for the Industry

The Bybit hack highlighted several critical security and user experience (UX) vulnerabilities in the crypto industry:

*   **Message Verification:** The importance of robust message verification and secure signing processes was underscored <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>.
*   **Blind Signing:** The practice of "blind signing" transactions, where users approve transactions without fully understanding the underlying complex code, was identified as a major risk <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>, <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>. Even experienced users often "blind sign" on popular platforms like OpenSea <a class="yt-timestamp" data-t="00:29:23">[00:29:23]</a>.
*   **Untrusted Front-Ends:** Assuming that front-ends are inherently secure is a critical mistake in crypto security <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. Users must verify the integrity of the message being signed, even when using trusted platforms <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.
*   **Cold Storage Best Practices:** The incident reinforces the advice to keep life savings and significant assets in cold storage, separate from wallets used for frequent transactions or signing <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>.
*   **UX Improvements:** Addressing the complexity of transaction data and providing human-readable interpretations for signing is crucial <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>. Innovations like hardware devices with larger screens (e.g., GridPlus) could help users clearly understand what they are signing <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.
*   **Bitcoin vs. Ethereum Multisig:** The differing nature of multisignature capabilities was noted. Bitcoin's simpler script allows for native multisig, while Ethereum requires standalone applications like Gnosis Safe, introducing more complexity <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

The hack represents a "bad look" for the industry, especially concerning institutional adoption and national security implications, as it was perpetrated by a state actor <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>.

## Related Discussions

The Bybit hack also ignited a wave of online trolling from certain Bitcoin maximalists who fabricated tweets and spread false information about Ethereum supposedly planning a chain rollback to revert the stolen funds <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>, <a class="yt-timestamp" data-t="00:34:30">[00:34:30]</a>. This trolling referenced the historical DAO hack in 2016, where Ethereum did intervene in the blockchain's state <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>, <a class="yt-timestamp" data-t="00:36:18">[00:36:18]</a>. The intent was to undermine Ethereum's perceived "credible neutrality" – a property shared with Bitcoin where the blockchain is neutral to its assets and transactions <a class="yt-timestamp" data-t="00:40:16">[00:40:16]</a>. This type of tribalism, while sometimes seen as humorous by "online" crypto participants, can be damaging and misleading to those less familiar with the industry's history <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>, <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>.