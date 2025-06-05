---
title: Zoom leap year freeze bug
videoId: Iq_r7IcNmUk
---

From: [[fireship]] <br/> 

In 2008, Microsoft released a portable music device called Zune, intended as a competitor to the iPod <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. While the device generally functioned well, a significant software bug caused all Zune devices worldwide to freeze and become inoperable "bricks" on December 31st <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

The Zune's screen would display a loading bar stuck at 100% <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The only way to resolve this issue was to manually remove and reinsert the battery <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Cause of the Freeze

The bug was rooted in the Zune's failure to account for the extra day in a leap year <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Specifically, when the software reached the 366th day of a leap year, it attempted to reset <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. However, a logic error in handling the day count meant the device could not exit this reset loop, leading to its permanent freeze <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

The issue could have been prevented with a simple code adjustment, such as breaking out of the loop when the number of days reached 367 <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.