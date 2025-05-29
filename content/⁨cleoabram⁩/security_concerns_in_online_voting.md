---
title: security concerns in online voting
videoId: LrHaXyv8eO0
---

From: [[⁨cleoabram⁩]] <br/> 

The prospect of online voting, while offering the potential to increase voter turnout and convenience, presents a complex and high-stakes set of [[challenges_of_online_voting | challenges]] and security risks that have made its widespread implementation highly controversial <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Experts describe it as "simply not secure enough" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a> and "vulnerable to cyber attacks" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> due to "unbounded amounts of hackers, computers, and cash" wielded by adversaries <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

While some limited forms of online voting exist for special circumstances, such as astronauts voting from space <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a> and options for military and overseas citizens in certain countries <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, these systems often involve less secure methods like emailing or faxing ballots, which [[the_role_of_cybersecurity_in_voting | cybersecurity]] experts deem unsuitable for an entire country <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Dr. Joe Kiniry and Dr. Josh Benaloh, [[the_role_of_cybersecurity_in_voting | cybersecurity]] experts with over 20 years of experience in online voting, identify four basic [[challenges_of_online_voting | challenges]] to voting online <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Key Security Challenges

### 1. Credentials
For online voting, digital credentials are required to validate a voter's identity <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. While countries like Estonia have electronic ID cards for citizens, used for various services including online voting <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>, the United States has historically shown "extreme resistance" to a national ID system <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</sup> <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This highlights significant [[political_and_technical_barriers_to_online_voting | political and technical barriers]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### 2. Coercion
Maintaining the secrecy of the ballot is paramount to prevent coercion, vote selling, or vote buying <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. If a voter can hand their device to someone else after logging in (e.g., with facial ID), or provide a receipt of their vote, it undermines the secret ballot <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Unlike online banking, where transactions are part of a public ledger visible to the user and the bank, online voting must ensure secrecy, meaning no public receipt of an individual's vote <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

Estonia addresses this by allowing voters to recast their vote multiple times online, with only the last vote counted, providing a safeguard against forced voting <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### 3. Client Malware
When voters use their personal devices (phones, computers) for online voting, "every voter's device in the entire election is part of the election's infrastructure" <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This drastically expands the "attack surface" for hackers, making the system vulnerable to manipulation <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

A primary concern is "vote flipping," where malware on a device could change a voter's selection without their knowledge <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Unlike online banking, where users can confirm transactions, the secret ballot makes it difficult for voters to confirm their vote was correctly recorded without revealing their choice <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a> <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

#### The Benaloh Challenge
One proposed solution to allow confirmation while preserving secrecy is the "Benaloh challenge," invented by Josh Benaloh <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This system allows a voter to either submit their encrypted vote or "check" it, demonstrating that the system correctly processes their intended choice without revealing it <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. By allowing voters to test the system repeatedly, it provides statistical proof of its integrity <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. If even 1% of 100 million voters perform a check, a small number of flipped votes would likely be caught <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

However, a critical issue remains: if finding a problem on a voter's phone could call an election into question, it creates an incentive for individuals to intentionally install malware on their devices to disrupt the process <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### 4. Denial of Service (DoS) Attacks
Beyond vote flipping, a major [[the_role_of_cybersecurity_in_voting | cybersecurity]] risk is a denial of service (DoS) attack <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. The goal is to overwhelm the voting system with fake traffic, causing websites to crash, load improperly, or even creating internet outages in specific areas <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. Even a slowdown for a few hours could catastrophically impact voter turnout <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This allows adversaries, who possess "unbounded amounts of hackers, computers, networks and cash," to strategically "create online weather" to influence election outcomes <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a> <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. This is about nations attempting to influence each other's elections <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Conclusion
The [[challenges_of_online_voting | challenges of online voting]] are multifaceted, encompassing not only technical hurdles but also significant [[political_and_technical_barriers_to_online_voting | political and technical barriers]] and issues of public trust <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. While progress is being made and a future where online voting works safely is envisioned, "unsolved problems" persist <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.