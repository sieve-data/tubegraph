---
title: FaceTime bug allowing eavesdropping
videoId: Iq_r7IcNmUk
---

From: [[fireship]] <br/> 

## Discovery <a class="yt-timestamp" data-t="02:23:09">[02:23:09]</a>
In 2019, a bug was discovered within Apple's FaceTime application on the iPhone <a class="yt-timestamp" data-t="02:23:09">[02:23:09]</a>.

## How the Bug Worked <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>
The vulnerability allowed a user to eavesdrop on the audio of a recipient's phone without them answering the call <a class="yt-timestamp" data-t="02:37:07">[02:37:07]</a>. This was achieved by:
1.  Initiating a FaceTime call <a class="yt-timestamp" data-t="02:27:07">[02:27:07]</a>.
2.  While the call was ringing, swiping up to add another person to create a group call <a class="yt-timestamp" data-t="02:29:07">[02:29:07]</a>.
3.  Adding one's own phone number as the additional person <a class="yt-timestamp" data-t="02:32:07">[02:32:07]</a>.
This sequence would cause FaceTime to glitch, incorrectly believing the group call was active, thereby enabling audio eavesdropping <a class="yt-timestamp" data-t="02:35:07">[02:35:07]</a>.

Additionally, if the original recipient pressed the power button to dismiss the incoming call, it would inadvertently activate their camera, allowing the caller to view their surroundings <a class="yt-timestamp" data-t="02:40:07">[02:40:07]</a>.

## Discovery and Apple's Reaction <a class="yt-timestamp" data-t="02:45:07">[02:45:07]</a>
The bug was initially discovered by a 14-year-old attempting to set up a group chat for playing Fortnite <a class="yt-timestamp" data-t="02:45:07">[02:45:07]</a>. His mother attempted to report the issue to Apple, but the company initially disregarded the report, seemingly confident in their code's perfection <a class="yt-timestamp" data-t="02:51:07">[02:51:07]</a>.

However, approximately a week later, the bug gained widespread attention, going viral on social media with many users demonstrating it on live streams <a class="yt-timestamp" data-t="02:56:07">[02:56:07]</a>. In response, Apple completely disabled the group FaceTime feature <a class="yt-timestamp" data-t="03:01:07">[03:01:07]</a> and released a patch within about a week <a class="yt-timestamp" data-t="03:03:07">[03:03:07]</a>. Apple later compensated the 14-year-old discoverer with a bug bounty and education funding <a class="yt-timestamp" data-t="03:05:07">[03:05:07]</a>.

## Root Cause <a class="yt-timestamp" data-t="03:10:07">[03:10:07]</a>
The root cause of the problem appeared to be FaceTime's failure to properly check the state of the call before activating the audio stream <a class="yt-timestamp" data-t="03:10:07">[03:10:07]</a>.