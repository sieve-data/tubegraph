---
title: Multisig key compromise
videoId: pWRC6kNvlY0
---

From: [[thepipeline_xyz]] <br/> 

The Ronin blockchain company, known for its popular game Axie, experienced a significant security breach involving a multisig key compromise <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This incident is considered one of the largest hacks in history <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## How the Compromise Occurred

The hack originated at Sky Mavis, Ronin's parent company <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The attack began with a phishing incident:
*   A devops engineer was phished with a fake job offer <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   The engineer clicked an executable file, which became a single point of failure <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   Through social engineering, the attackers gained access to four out of the nine multisig keys <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Multisig requires five keys out of nine keyholes to unlock <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The attackers then performed lateral movement, moving from the initially [[compromised_trading_accounts | compromised]] device to another to acquire a fifth key <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Multisig Mechanism

A multisig (multi-signature) setup acts like a "door with many keys" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. In this case, the Ronin Bridge multisig required five keys out of a total of nine to authorize a transaction <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Impact

Once the attackers obtained all five necessary keys, they were able to compromise the system, leading to a loss of approximately half a billion dollars <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This incident highlights the significant [[impact_of_the_650_million_hack | impact of large-scale hacks]] originating from seemingly simple social engineering tactics like phishing emails <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.