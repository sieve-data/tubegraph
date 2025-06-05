---
title: Handling Asynchronous Programming in Flutter
videoId: 7sJZi0grFR4
---

From: [[fireship]] <br/> 

[[asynchronous_programming_in_javascript | Asynchronous programming]] is a crucial concept in both JavaScript and Flutter <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. While JavaScript uses promises, Dart (and by extension Flutter) utilizes futures <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

## Futures vs. Promises
In Dart, futures function exactly like JavaScript promises <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.
*   An `async` function in Dart will automatically return a future <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>.
*   You can use `await` to pause the execution of a function until a future returns a value <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>. This is similar to how `await` works with promises in JavaScript <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
*   Just like with promises, you can call `.then()` to capture the resolved value or `.catchError()` (equivalent to `.catch()`) if the future results in an error <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.

## Streams
Dart includes a "stream" data structure for handling multiple asynchronous values <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
*   Unlike vanilla JavaScript, which doesn't have built-in stream support (though libraries like RxJS and MobX offer observables for this functionality) <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>, Dart's streams are native.
*   You can use `async`/`await` with streams via an `await for` loop <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. This approach can lead to more readable code compared to chaining multiple callback functions <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.
*   Alternatively, you can "subscribe" to a stream using its `.listen()` method, similar to how `.subscribe()` works with observables <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.

## UI Rendering with Asynchronous Data
Flutter offers "builders" that enable you to work with asynchronous data sources and automatically render the UI <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.
*   These builders are conceptually similar to Angular's `async` pipe <a class="yt-timestamp" data-t="13:11:00">[13:11:00]</a>.
*   You configure your UI to listen to a stream, and it will re-render different templates or widgets based on the stream's current value <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.