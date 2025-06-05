---
title: Intel Pentium FDIV bug
videoId: Iq_r7IcNmUk
---

From: [[fireship]] <br/> 

The Intel Pentium FDIV bug, an infamous software flaw from 1994, occasionally caused programs performing floating-point division on a Pentium chip to return an incorrect value <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>, <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

## Discovery and Initial Reaction

This bug was rare, occurring in approximately 1 in 9 billion division operations <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. It was discovered by a professor at Lynchberg College while he was performing computational number theory <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Initially, the professor believed it was an error in his own code <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. However, after extensive testing, he reported the issue to Intel <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

Intel initially attempted to downplay the significance of the bug <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. The situation escalated into a massive public relations crisis when IBM suspended the use of Intel chips in their personal computers <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

## Technical Details

The core of the issue lay within the SRT division algorithm, which is designed to accelerate division operations by utilizing lookup tables to estimate the next digit of a quotient <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>, <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. The lookup table, which contained 1,066 entries, was found to have five missing entries <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>, <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. This omission resulted in certain combinations of numbers yielding incorrect results at the hardware level <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.