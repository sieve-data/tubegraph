---
title: Social engineering and phishing attacks
videoId: pWRC6kNvlY0
---

From: [[thepipeline_xyz]] <br/> 

Social engineering and phishing attacks are significant [[common_attack_vectors_in_the_crypto_space | attack vectors]] used to compromise digital assets. A notable example of such an attack is the hack of Ronin, a blockchain company associated with the popular game Axie, operated by its parent company Sky Mavis <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Case Study: The Ronin Bridge Hack

In this incident, a devops engineer at Sky Mavis was compromised through a phishing attempt <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The attack unfolded as follows:

*   **Phishing Vector** The engineer received a fraudulent job offer via email <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It is believed they clicked on an executable file contained within this deceptive offer <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Initial Compromise and [[access_vulnerabilities | Access Vulnerabilities]]** A critical [[access_vulnerabilities | access vulnerability]] was exploited: the engineer's device, once compromised, provided access to four keys for a multi-signature (multi-sig) wallet <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. A multi-sig acts like a door requiring multiple keys to unlock; in this case, five out of nine keys were needed <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **[[social_engineering_tactics | Social Engineering]] and Lateral Movement** Through the initial compromise, the attackers leveraged [[social_engineering_tactics | social engineering]] to obtain four of the necessary keys <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. They then performed lateral movement, shifting from the initially compromised device to another to acquire a fifth key <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. With all five keys in hand, they gained full control <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Impact** This successful attack, stemming from a seemingly innocuous official email, resulted in significant damage, reportedly costing about half a billion dollars <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. It is considered one of the largest hacks in history <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.