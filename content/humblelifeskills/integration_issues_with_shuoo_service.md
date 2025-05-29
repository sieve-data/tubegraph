---
title: Integration issues with Shuoo service
videoId: 5SYwKoTWolo
---

From: [[humblelifeskills]] <br/> 

A significant bug has been identified regarding video recording and destination sending functionality on the Nokia N95 camera, particularly when attempting [[integrating_wirecast_with_other_platforms_like_skype | integration]] with services like Shuoo <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Description of the Bug
The bug manifests when a user records video clips in succession on the N95.

### Steps to Reproduce
1.  Record a video clip <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
2.  Stop the recording <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The device then prompts the user to send the clip to one of their configured destinations <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, such as Shuoo <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
3.  Record a second clip <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
4.  Record a third clip <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Observed Behavior
After recording two clips in succession, the device prompts the user to save them to the web <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. If the camera is positioned so the screen is not visible (e.g., pointing towards the user) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, and a third recording attempt is made, the device remains stuck awaiting a "yes" or "no" response to the previous prompt <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

Attempting to exit this state by pressing the four cursors button causes the device to navigate to the main menu <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. However, once at the main menu, the device becomes unresponsive, preventing access to the gallery or any other functions <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Resolution
The only way to resolve this issue is to power the device off and then power it back on again <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Impact
This bug makes the video side of the N95 "not very user friendly" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a> due to the need for a full device restart to regain functionality <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.