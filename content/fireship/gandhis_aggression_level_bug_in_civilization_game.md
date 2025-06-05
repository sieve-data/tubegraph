---
title: Gandhis aggression level bug in Civilization game
videoId: Iq_r7IcNmUk
---

From: [[fireship]] <br/> 

In the original *Sid Meier's Civilization* game, an unintentional programming oversight led to a memorable "bug" that later became an urban legend and unofficial feature. The issue centered around the aggression level of the leader Gandhi, who was initially designed as a peaceful character <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## The Bug Explained

Gandhi's aggression level was set as an unsigned integer with a value of one, making him a "super chill pacifist" <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. However, when another civilization adopted diplomacy, it would reduce aggression by two points <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Due to an unsigned integer underflow (1 - 2), Gandhi's aggression level would "max out" to 255 <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This transformation turned him into a "diabolical thermonuclear enthusiast" <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Impact and Legacy

This unexpected behavior was widely embraced by *Civilization* players, becoming so beloved that it effectively transformed from a bug into a celebrated feature, albeit an urban legend <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This phenomenon highlights how sometimes an accidental glitch can enhance a game's experience and become part of its lore.