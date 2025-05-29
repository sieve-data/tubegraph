---
title: Multisig key security vulnerabilities
videoId: pWRC6kNvlY0
---

From: [[thepipeline_xyz]] <br/> 

Multisignature (multisig) systems, while designed to enhance security by requiring multiple keys to authorize a transaction, can still be vulnerable to sophisticated attacks, particularly through social engineering and [[access_vulnerabilities | access vulnerabilities]]. This was starkly demonstrated in the Ronin Network hack.

## The Ronin Network Hack: A Case Study

The Ronin Network, a blockchain company, developed a popular game called Axie <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Its parent company was Sky Mavis <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. In what might still be the largest hack in history, approximately half a billion dollars was exploited <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### How the Multisig Was Compromised

The hack originated from a phishing incident targeting a DevOps Engineer at Sky Mavis <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
1.  **Phishing Attack**: The engineer received a job offer via email <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
2.  **Malware Execution**: The engineer clicked on an executable file within the offer <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
3.  **Initial Compromise**: This action created a critical single point of failure: the engineer's device gained access to four of the necessary keys for the multisig system <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
4.  **Multisig Structure**: The multisig setup for Ronin required five out of nine keys to unlock it <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. A multisig is essentially like a door that requires multiple keys to open, rather than just one <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
5.  **Key Acquisition**:
    *   Through social engineering, the attackers obtained four keys via the compromised engineer <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   To get the crucial fifth key, the attackers performed "lateral movement," shifting from the initially compromised device to another device on the network <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
6.  **Full Compromise**: Once all five keys were acquired, the attackers were able to compromise the system fully <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

> [!CAUTION]
> This incident highlights that even advanced security measures like multisig can be undermined if fundamental [[importance_of_user_security_in_crypto | user security]] practices, such as vigilance against phishing and robust internal network segmentation, are not rigorously maintained. The attack demonstrates how a simple office email <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> can lead to massive financial damage <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.