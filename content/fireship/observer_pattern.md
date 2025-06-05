---
title: Observer pattern
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

The [[software_design_patterns|Observer pattern]] is a behavioral [[software_design_patterns|design pattern]] that enables a push-based system, unlike the pull-based nature of the [[software_design_patterns|iterator pattern]] <a class="yt-timestamp" data-t="07:57:57">[07:57:57]</a>. It allows many objects to subscribe to events broadcast by a single other object, establishing a one-to-many relationship <a class="yt-timestamp" data-t="08:02:02">[08:02:02]</a>.

## How it Works
In the [[Observer pattern]], a "subject" object broadcasts events, and multiple "observer" objects can "listen in" or subscribe to these events <a class="yt-timestamp" data-t="08:02:02">[08:02:02]</a>.
A real-world analogy is a radio tower (subject) sending out a signal, and multiple radio receivers (observers) listening in at the same time <a class="yt-timestamp" data-t="08:08:08">[08:08:08]</a>.

## Use Cases
The [[Observer pattern]] is widely used in app development <a class="yt-timestamp" data-t="08:14:15">[08:14:15]</a>. For example, in Firebase, when data changes on the server, all client applications subscribed to that data are automatically updated with the latest information <a class="yt-timestamp" data-t="08:17:17">[08:17:17]</a>.

## Implementation Example (RxJS)
Libraries like RxJS can simplify the demonstration of this pattern <a class="yt-timestamp" data-t="08:24:24">[08:24:24]</a>.

*   **Subject Class:** RxJS provides a `Subject` class, which represents the data that observers want to listen to <a class="yt-timestamp" data-t="08:28:28">[08:28:28]</a>.
*   **Subscriptions:** Multiple subscriptions can be added to a subject <a class="yt-timestamp" data-t="08:32:32">[08:32:32]</a>. The subject keeps track of all these subscriptions <a class="yt-timestamp" data-t="08:36:36">[08:36:36]</a>.
*   **Notifications:** When the data changes, the subject calls the callback functions of all its registered subscriptions <a class="yt-timestamp" data-t="08:37:37">[08:37:37]</a>.
*   **Pushing Values:** To push a new value to the subject and notify all subscriptions, its `next` method is called <a class="yt-timestamp" data-t="08:46:46">[08:46:46]</a>.

The process can be thought of as a loop that unfolds over time <a class="yt-timestamp" data-t="08:52:52">[08:52:52]</a>.