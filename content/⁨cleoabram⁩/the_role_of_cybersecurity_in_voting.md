---
title: the role of cybersecurity in voting
videoId: LrHaXyv8eO0
---

From: [[⁨cleoabram⁩]] <br/> 

The modern era, particularly the "ultimate election year" when countries representing half the world's population hold elections, presents a significant test for democracy <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. While traditional voting methods can involve long distances, queues, or taking time off work <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, the idea of online voting arises as a potential solution for convenience <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, the question of "Why can't I vote online?" reveals a highly controversial, complicated, and high-stakes answer primarily rooted in cybersecurity <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Early Adoptions and Context

Despite the widespread challenges, some forms of online voting have existed. The US state of Texas initiated online voting in 1997 to allow an astronaut to vote from the Mir Space Station <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This tradition continues, with astronauts on the ISS planning to vote this way <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Additionally, many US states and various countries worldwide offer online voting options for military and overseas citizens, totaling about 300,000 American online votes in 2020 <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. These are generally for people with special circumstances, not the general public <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

The primary aspiration for online voting is to increase voter turnout and simplify participation in democracies <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, but this is only feasible if it can be done safely <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## The Core Challenge: Cybersecurity

The stakes for online voting are exceptionally high, involving the most powerful nations choosing their leaders and potentially influencing adversaries' elections <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This elevates cybersecurity to an entirely different level <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

Current methods used for some online voters in the US, such as emailing or faxing ballots, are explicitly deemed unsafe for a national system by cybersecurity experts <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Dr. Joe Kiniry and Dr. Josh Benaloh, cybersecurity experts with over two decades of experience in online voting, highlight that the problem is "difficult" and not yet fully solved <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Key Cybersecurity Challenges in Online Voting

Four basic [[challenges_of_online_voting | challenges to voting online]] are identified:

1.  **Credentials and Identity Verification**: Online voting requires digital credentials <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   Estonia provides an electronic ID card to every citizen, used for various services including online voting since the early 2000s <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   In the US, there has been "extreme resistance" to a national ID system <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. While Social Security numbers exist, adopting them as a foundation for a national ID is a "no go" from a [[political_and_technical_barriers_to_online_voting | political standpoint]], demonstrating that the barriers are not solely technical <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

2.  **Coercion and Secret Ballot Integrity**: This is both a technical and [[political_and_technical_barriers_to_online_voting | political challenge]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
    *   Unlike polling places, a phone logged in via facial ID could be handed to someone else to cast a vote <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
    *   The crucial aspect of voting is the secret ballot, not just voting in secret, but also ensuring no receipt can be shown to prove a vote was cast a certain way (e.g., for vote buying or selling) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Estonia addresses this by allowing voters to recast their vote multiple times online, with only the last vote counted, providing a safeguard against coercion <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   Online banking, by contrast, is not secret; all transactions are part of a public ledger shared with the bank <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Online voting cannot operate under this principle.

3.  **Client Malware and Vote Flipping**:
    *   Adopting internet voting means every voter's device becomes part of the election's infrastructure, significantly increasing the "attack surface" for hackers <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   The primary concern is "vote flipping," where malware on a voter's device changes their intended vote without their knowledge <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
    *   Unlike online banking or encrypted messaging, the principal difference in voting is the difficulty of confirming that actions have been done properly due to the secret ballot <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. The very mechanism protecting voters (secrecy) makes confirmation difficult <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

    *   **The Benaloh Challenge**: Invented by Dr. Josh Benaloh, this cryptographic method allows voters to "check" their encrypted vote to ensure it's recorded correctly without revealing their choice <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This process can be repeated, mathematically proving the system's integrity <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
        *   In a large election, if even 1% of 100 million voters performed a check, approximately 100 flipped votes across the election would likely be caught <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
        *   At the end of an election, the voter's specific encrypted number would be recorded, allowing them to verify their vote was submitted, but not how they voted <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   **Limitations of Confirmation**: A significant problem arises if finding malware on a phone could call an election into question; this creates an incentive for malicious actors to intentionally introduce malware onto devices to disrupt or overturn results <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

4.  **Denial of Service (DoS) Attacks**: This is potentially the highest-stakes challenge <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
    *   The goal is to overload a system with fake traffic, causing websites to crash, load improperly, or even create localized internet outages <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   Even a slowdown of a few hours could be catastrophic, as voter turnout can be influenced by factors like rain <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. DoS attacks could be used to create "online weather" in specific areas to impact voting patterns <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   Adversaries, described as "extremely talented" with "unbounded amounts of hackers, computers, networks, and cash," pose a significant threat to election integrity through such attacks <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Broader Implications and Public Trust

Beyond technical challenges like [[security_concerns_in_online_voting | cybersecurity]], online voting also intersects with the complex issue of public trust in elections <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This is not purely a technological problem <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

While progress is being made on [[challenges_of_online_voting | unsolved problems]] in online voting, it remains a significantly harder problem than it might appear <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. A future where online voting works safely is possible, but it requires overcoming substantial hurdles <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.