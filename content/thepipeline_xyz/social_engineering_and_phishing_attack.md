---
title: Social engineering and phishing attack
videoId: pWRC6kNvlY0
---

From: [[thepipeline_xyz]] <br/> 

A significant incident demonstrating the dangers of [[spear_phishing_and_social_engineering | social engineering]] and phishing attacks involved a blockchain company called Ronin, which was affiliated with Sky Mavis, the parent company behind the popular game Axie <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## The Ronin/Sky Mavis Hack

The hack, which could be the largest in history, originated from a seemingly innocuous phishing attempt <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Attack Vector

*   **Initial Compromise**: One of Sky Mavis's DevOps Engineers was targeted with a fake job offer, a common tactic in [[Phishing scams in the crypto industry | phishing scams in the crypto industry]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   **Malware Delivery**: The engineer reportedly clicked on an executable file contained within the job offer email <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This single action created a critical point of failure, allowing the attacker to gain access to the employee's device <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### Exploiting the Multi-Sig Wallet

The Ronin system utilized a multi-signature (multi-sig) wallet, which acts like a "door with many keys" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. To unlock it, five out of nine total keys were required <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

*   **Gaining Initial Keys**: Through the compromised device and further [[spear_phishing_and_social_engineering | social engineering]], the attackers managed to obtain four of the necessary keys <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Lateral Movement**: The attackers then performed "lateral movement," migrating from the initially compromised device to another to acquire an additional key <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   **Full Access**: With all five required keys in hand, the attackers were able to compromise the system <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Impact

The hack resulted in approximately half a billion dollars in damages <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, making it potentially the largest hack in history, all stemming from a single phishing email <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This incident highlights the significant [[Impact of the 650 million hack | impact of the 650 million hack]] and how a simple act of clicking on a malicious link can lead to catastrophic financial losses.