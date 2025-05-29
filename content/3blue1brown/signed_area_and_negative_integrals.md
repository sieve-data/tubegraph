---
title: Signed area and negative integrals
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 

When considering [[Integrals and derivatives | integrals]], the concept of "area under a curve" is often introduced as a measure of total accumulation <a class="yt-timestamp" data-t="01:18:46">[01:18:46]</a>. However, it's important to understand that [[Integrals and derivatives | integrals]] measure what is known as "signed area" <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>. This means that areas below the horizontal axis are counted as negative.

## Negative Velocity and Distance

Consider a scenario where a car's velocity function includes periods of negative velocity <a class="yt-timestamp" data-t="01:17:53">[01:17:53]</a>. Negative velocity implies the car is moving backwards <a class="yt-timestamp" data-t="01:17:53">[01:17:53]</a>.

If velocity is negative, a tiny distance traveled (`ds`) over a small time interval (`dt`) will also be negative, as `ds` is approximately equal to velocity multiplied by the tiny change in time (`v(t) * dt`) <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>. This means the car is reducing its displacement from its starting point.

## Visualizing Negative Area

In the context of a velocity-time graph, if the velocity function dips below the horizontal axis, the corresponding "thin rectangles" used in [[Visualizing integration and approximations | approximations]] will also extend below this axis <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>. The area of such a rectangle represents a bit of distance traveled backwards <a class="yt-timestamp" data-t="01:18:25">[01:18:25]</a>. When calculating the total distance between the car's start and end points, these "negative areas" are subtracted from the total <a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a>.

Therefore, [[Integrals and derivatives | integrals]] should not be thought of as measuring literal geometric area, but rather the net change or "signed area" between the graph and the horizontal axis <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.