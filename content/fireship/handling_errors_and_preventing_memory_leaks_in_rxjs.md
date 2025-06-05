---
title: Handling Errors and Preventing Memory Leaks in RxJS
videoId: ewcoEYS85Co
---

From: [[fireship]] <br/> 

RxJS is a powerful [[javascript_memory_management_and_garbage_collection | JavaScript]] library for controlling data flow over time <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. When working with [[introduction_to_rxjs_and_observables | RxJS Observables]], it's crucial to understand how to handle errors and prevent memory leaks to ensure robust and efficient applications <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>, <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

## Handling Errors

In the context of an RxJS stream, there is significant flexibility in how errors can be handled <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. A common strategy is to catch an error and then replace it with an alternative value <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### `catchError` Operator
The `catchError` [[rxjs_operators_and_their_usage | operator]] can intercept an error and allow a different default value to be emitted from the stream <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This enables the application to handle errors gracefully in the background and provide useful information to the user <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

### `retry` Operator
RxJS also allows for easy retrying of operations using the `retry` [[rxjs_operators_and_their_usage | operator]] <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. This is particularly useful when dealing with [[rxjs_operators_and_their_usage | HTTP]] calls, where temporary network issues might cause failures <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

#### Example
Without error handling, an error pushed to a [[using_subjects_and_multicasting_in_rxjs | Subject]] would result in an uncaught error in the console <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. By using `catchError`, the error can be handled, and a substitute value or action can be performed <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

## Preventing Memory Leaks

Preventing "leaks" in your RxJS "pipes" refers to avoiding memory leaks, which can degrade application performance <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. There are two primary methods to prevent memory leaks in RxJS subscriptions <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

### 1. Unsubscribing Manually

The most direct way to prevent a memory leak is to manually `unsubscribe` from your subscriptions <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. For example, an `interval` observable will run indefinitely unless its subscription is closed <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. By storing the subscription in a variable and calling `subscription.unsubscribe()` at a later point, the leak can be stopped <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

### 2. Using Completion Operators

A more robust approach is to use RxJS [[rxjs_operators_and_their_usage | operators]] that automatically complete the observable, thereby preventing the need for manual unsubscription <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

#### `takeWhile` Operator
The `takeWhile` [[rxjs_operators_and_their_usage | operator]] allows an [[introduction_to_rxjs_and_observables | observable]] to emit values only while a specified condition remains true <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. Once the condition becomes false, the observable will complete, effectively stopping the emission of values and preventing a memory leak <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

#### `takeUntil` Operator
The `takeUntil` [[rxjs_operators_and_their_usage | operator]] takes another [[introduction_to_rxjs_and_observables | observable]] as its argument <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. When this argument [[introduction_to_rxjs_and_observables | observable]] emits a value, it triggers the completion of the source [[introduction_to_rxjs_and_observables | observable]], cancelling its subscription <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. For instance, setting a timer with `takeUntil` can complete an `interval` [[introduction_to_rxjs_and_observables | observable]] after a specified duration <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.