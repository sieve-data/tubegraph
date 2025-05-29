---
title: Online voting technologies and solutions
videoId: LrHaXyv8eO0
---

From: [[⁨cleoabram⁩]] <br/> 

The current era, dubbed the "ultimate election year," will likely see more people vote globally than ever before, with countries representing half the world's population holding elections for their leaders <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Despite this, traditional voting methods often present challenges, such as long travel distances, extended wait times, or the need to take time off work <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This has led to widespread interest in online voting as a potentially easier and more convenient alternative that could boost voter turnout <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

However, the implementation of online voting is far more controversial, complicated, and high-stakes than commonly imagined <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Experts caution that it is "simply not secure enough" and highly "vulnerable to cyber attacks" from "adversaries [who] have unbounded amounts of hackers, computers, and cash" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Historical Context and Current Limited Use

The concept of online voting has surprising origins, with one of the earliest instances occurring in 1997 when the US state of Texas enabled an astronaut to vote from the Mir Space Station <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This tradition continues, with American astronauts on the International Space Station (ISS) still planning to vote this way <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

Currently, several US states offer online voting options for military and overseas citizens <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. In 2020, approximately 300,000 Americans voted online <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Globally, numerous countries provide online voting to varying degrees, though it is predominantly available only to people with special circumstances, not the general populace <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Most of the world still relies on traditional in-person voting. For example:
*   In India, voters use electronic machines at polling stations and have their fingers marked with ink to prevent fraud <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   In Gambia, people cast votes by placing marbles into colored drums <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   In the United States, paper ballots are commonly used, counted by optical scan ballot counters, with physical ballots retained for audit or recount purposes <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Only about two-thirds of eligible US citizens typically vote, which is lower compared to other countries <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The primary goal of online voting is to increase voter participation and make it easier for people to engage in their democracies, provided it can be done safely <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## [[Challenges of online voting | Challenges of Online Voting]]

The stakes for online voting are exceptionally high, involving nations influencing their own and other countries' elections, making it a matter of [[cybersecurity_concerns_in_online_voting | cybersecurity on a whole other level]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Current online voting methods, such as emailing or faxing ballots, are considered highly insecure by cybersecurity experts <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Cybersecurity experts Dr. Joe Kiniry and Dr. Josh Benaloh highlight four fundamental challenges in online voting:

### 1. Credentials
Online voting necessitates digital credentials for identity verification <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Estonia's Solution:** Estonia provides every citizen with an electronic ID card used for healthcare, taxes, and online voting since the early 2000s <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This allows Estonians to validate their identity and cast their vote securely <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **US Resistance:** In the United States, there has been strong political resistance to implementing a national ID system, despite technical possibilities, making a universal digital credential system politically infeasible <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### 2. Coercion
Maintaining the secrecy of the ballot is crucial to prevent coercion, vote buying, or manipulation of voters <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>, <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Unlike in-person voting, where handing over a phone with facial ID could allow someone else to vote, online systems struggle to ensure a secret vote without a receipt that could be used for proof of vote <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>, <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Estonia's Solution:** Estonia addresses this by allowing voters to recast their vote multiple times online, with only the last recorded vote being counted. This feature allows individuals coerced into voting a certain way to revote later in secret <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Distinction from Online Banking:** Online voting differs fundamentally from online banking, where transactions are publicly logged and verifiable, and secrecy is not a requirement <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### 3. Client Malware
When voting online, every voter's device becomes part of the election's infrastructure, vastly expanding the "attack surface" for hackers <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>, <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The primary concern is "vote flipping," where malware on a device changes a voter's selection without their knowledge <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

The challenge lies in confirming that votes have been recorded properly, which is complicated by the need for a secret ballot <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>, <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. If a problem is detected, it could lead to an election being called into question, potentially encouraging malicious actors to intentionally introduce malware <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>, <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

*   **The Benaloh Challenge:** Invented by Dr. Josh Benaloh, this system allows voters to mathematically verify that their encrypted vote (a sequence of numbers) is correctly registered, without revealing how they voted <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>, <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. In a large election, if even 1% of voters perform a check, a statistically significant number of flipped votes would likely be caught <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>, <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### 4. Denial of Service (DoS) Attacks
A [[cybersecurity_concerns_in_online_voting | Denial of Service (DoS) attack]] aims to overload a system with fake traffic, causing websites to crash, load improperly, or create internet outages in specific areas <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>, <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. Even a slowdown for a few hours could be catastrophic, as factors like weather are known to influence voter turnout. A DoS attack could effectively create "online weather" to disproportionately affect specific groups, thereby altering election outcomes <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>, <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>, <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

## Future Outlook

While significant progress is being made in [[emerging_technologies_impacting_the_future | emerging technologies impacting the future]] and cybersecurity, there are still many unsolved problems in online voting <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Beyond technical hurdles, the public trust in voting systems presents a substantial, non-technological challenge <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>, <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Despite the difficulties, a future where online voting could work remains a significant possibility <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.