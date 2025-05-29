---
title: political and technical barriers to online voting
videoId: LrHaXyv8eO0
---

From: [[⁨cleoabram⁩]] <br/> 

The year 2024 is considered the "ultimate election year," with countries representing half the world's population holding elections for their leaders <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This presents a significant test for democracy, requiring millions of polling places and billions of ballots <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While voting is often difficult due to factors like long travel distances, long lines, or the need to take time off work <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, the idea of voting online seems appealing <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, the answer to "Why can't I vote online?" is far more controversial, complicated, and high-stakes than commonly imagined <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Current State of Online Voting

Online voting has surprising origins, including space. In 1997, Texas added an online voting option for an astronaut to vote from the Mir Space Station <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This tradition continues, with astronauts on the ISS planning to vote this way <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Many US states and other countries globally offer options for online voting, primarily for military and overseas citizens, or those with other special circumstances <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. In 2020, about 300,000 Americans voted online <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

In contrast, most of the world still relies on traditional voting methods:
*   **India**: Voters go to polling stations and use electronic machines, with indelible ink applied to prevent fraud <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Gambia**: People place marbles into colored drums <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **United States**: Many voters mark paper ballots, which are counted by optical scan ballot counters, with the physical paper ballot kept as a backup for audits or recounts <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

The ultimate goal of online voting is to increase voter turnout and make participation easier <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, but this is only desirable if it can be done safely <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## High Stakes of Online Voting

The stakes for online voting are extremely high, involving decisions for "the most important well-armed countries in the world" and attempts by adversaries to influence elections <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This elevates [[the_role_of_cybersecurity_in_voting | cybersecurity]] to a different level <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Current methods for selected online voters in the US, like emailing or faxing ballots, are deemed unsafe for widespread use by [[security_concerns_in_online_voting | cybersecurity experts]] <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Political and Technical Barriers

Cybersecurity experts Dr. Joe Kiniry and Dr. Josh Benaloh highlight four basic [[challenges_of_online_voting | challenges of online voting]] <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:

### 1. Credentials
*   **Technical Need**: Online voting requires digital credentials <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Estonian Example**: Estonia addresses this by providing every citizen an electronic ID card for healthcare, taxes, and online voting since the early 2000s <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **US Political Barrier**: In America, there has been "extreme resistance" to implementing a national ID system <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. While Social Security numbers exist, the political will for them to evolve into a national ID card is "simply a no go" <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

### 2. Coercion
*   **Technical Challenge**: Unlike a polling place, a digital voting device (e.g., phone) can be handed to someone else after logging in, enabling coercion <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. It's crucial that votes remain secret, meaning voters cannot have a receipt that could be used to prove how they voted (e.g., for vote buying) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Historically, without secret ballots, vote selling and manipulation were prevalent <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Estonian Solution**: Estonia allows voters to recast their vote multiple times online, with only the last recorded vote being counted, enabling a coerced voter to correct their vote later <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Contrast with Banking**: Online banking, by its nature, is not secret; every transaction is part of a public ledger shared with the bank <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Online voting, however, must prioritize secrecy.

### 3. Client Malware
*   **Expanded Attack Surface**: With internet voting, every voter's device becomes part of the election's infrastructure, vastly expanding the "attack surface" for hackers <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Vote Flipping**: A significant concern is malware on a voter's device secretly flipping their vote without their knowledge <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Confirmation Difficulty**: Unlike online banking or encrypted messaging, the principal difference with voting is the ability to confirm that things have been done properly <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The secret ballot, while protecting against coercion, makes confirming individual votes difficult <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **The Benaloh Challenge**: Invented by Josh Benaloh, this method allows voters to "check" their encrypted vote as many times as they want, mathematically proving the system is working <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. If even 1% of 100 million voters perform a check, a statistically significant number of flipped votes would likely be caught <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Unresolved Problem**: Even if a problem is found, the implication is that it might call an election into question. This could lead to individuals intentionally placing malware on their phones to disrupt results <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### 4. Denial of Service (DoS) Attacks
*   **Goal**: The aim of a DoS attack is to overwhelm a system with fake traffic, causing websites to crash, load improperly, or create internet outages in specific areas <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Catastrophic Potential**: Even a slowdown for a few hours could be catastrophic, as voter turnout is known to be influenced by factors like weather; DoS attacks could create "online weather" in specific places to affect voting <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   **Sophisticated Adversaries**: The adversaries involved are "extremely talented" nations with "unbounded amounts of hackers, computers, networks, and cash," making it a matter of national influence rather than simple scams <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Public Trust
Beyond the technical hurdles, a significant [[security_concerns_in_online_voting | barrier to online voting]] is the issue of public trust in the voting process, which extends "well beyond technology" <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

While progress is being made and a future where online voting works is conceivable <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, it is a much harder problem than it initially appears <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.