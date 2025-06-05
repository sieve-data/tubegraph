---
title: RxJS Operators and Their Usage
videoId: ewcoEYS85Co
---

From: [[fireship]] <br/> 

RxJS is a powerful JavaScript library designed to help control data flow over time <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It addresses the challenges of working with asynchronous streams of data, providing a functional library to manage data sources like Firebase, DOM events, WebSockets, or file uploads <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

While [[introduction_to_rxjs_and_observables | promises]] handle single asynchronous values, and callbacks can lead to "callback hell" for real-time streams, RxJS offers a robust solution for dealing with streams that unfold over time <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It's becoming increasingly popular, with more daily npm downloads than [[Angular Directives and Usage | Angular]] or Vue <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## What are Operators?

[[RxJS Operators | Operators]] are functions that allow you to control and modify the flow of data through [[introduction_to_rxjs_and_observables | observables]] <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. They enable the transformation, filtering, and combination of data streams <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Multiple [[RxJS Operators | operators]] can be chained together using the `pipe()` method, where data flows through and is modified by each function in order from top to bottom <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>, <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Key RxJS Operators and Their Usage

### Transformation Operators

*   **`map`**
    *   **Purpose**: Transforms each item emitted by an [[introduction_to_rxjs_and_observables | observable]] into a new output <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   **Usage**: Takes an input value and returns a new transformed value <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
    *   **Example**: `map(number => number ** 2)` will square each number <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

*   **`scan`**
    *   **Purpose**: Accumulates values over time, similar to the `reduce` method in [[modern_javascript_array_methods | JavaScript array methods]] <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
    *   **Usage**: Takes an accumulator function that adds the current value to an accumulated value <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   **Example**: `scan((acc, curr) => acc + curr)` can keep a running total of all emitted values <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   **Important**: The order of [[RxJS Operators | operators]] in the `pipe()` matters, as it changes the underlying math and results <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>, <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Filtering Operators

*   **`filter`**
    *   **Purpose**: Prevents certain items from being emitted in the stream based on a condition <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   **Usage**: Takes a predicate function, and only values that meet the condition are emitted <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   **Example**: `filter(value => value > 10)` will only emit numbers greater than 10 <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

*   **`take`**
    *   **Purpose**: Tells the [[introduction_to_rxjs_and_observables | observable]] to complete after emitting a specified number of values <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   **Usage**: `take(n)` emits only `n` values from the [[introduction_to_rxjs_and_observables | observable]] and then completes it <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>, <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### Side Effect Operator

*   **`tap`**
    *   **Purpose**: Allows you to trigger side effects from inside the [[introduction_to_rxjs_and_observables | observable]] pipe without modifying the stream <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>, <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   **Usage**: Can be used for console logging at different points to inspect values, or for more complex side effects like saving data to a backend database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   **Benefit**: Gives context to "tap into" the [[introduction_to_rxjs_and_observables | observable]] stream and perform actions <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### Backpressure Control Operators

Backpressure occurs when an [[introduction_to_rxjs_and_observables | observable]] emits more values than you actually need or can process <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. These [[RxJS Operators | operators]] help manage this.### Backpressure Control Operators

Backpressure occurs when an [[introduction_to_rxjs_and_observables | observable]] emits more values than you actually need or can process <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. These [[RxJS Operators | operators]] help manage this.

*   **`debounceTime`**
    *   **Purpose**: Filters out events until they have stopped happening for a certain period of time <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>, <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
    *   **Usage**: Useful for "type-ahead" scenarios, preventing API calls until the user finishes typing <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>, <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
    *   **Example**: `debounceTime(1000)` will wait one second after the last event before emitting the value <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

*   **`throttleTime`**
    *   **Purpose**: Emits the first value but ensures no additional values are emitted until a specified time period has passed <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>, <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    *   **Usage**: Guarantees a maximum rate of emissions.
    *   **Example**: `throttleTime(1000)` will emit at most one event per second <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

*   **`buffer`**
    *   **Purpose**: Collects events into an array and only emits them when a certain condition (e.g., array length) is met <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
    *   **Usage**: Allows keeping all data but listening to it in batches <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
    *   **Example**: `buffer(20)` will emit an array of 20 events <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>, <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Combination and Flat-Mapping Operators

*   **`switchMap`**
    *   **Purpose**: Starts with one [[introduction_to_rxjs_and_observables | observable]] and then "switches" to another, canceling previous inner [[introduction_to_rxjs_and_observables | observables]] if a new value arrives from the source <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>, <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   **Usage**: Critical for relational data scenarios, such as fetching user orders after a user ID becomes available <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. It avoids nested subscriptions, which can lead to "callback hell" <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>, <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   **Flexibility**: You can return an [[introduction_to_rxjs_and_observables | observable]], a [[introduction_to_rxjs_and_observables | promise]], or an [[modern_javascript_array_methods | array]] from `switchMap` <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

### Combining Observable Functions (not technically operators)

*   **`combineLatest`**
    *   **Purpose**: Combines the latest values from multiple [[introduction_to_rxjs_and_observables | observables]] into a single array <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>, <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
    *   **Behavior**: It waits for each source [[introduction_to_rxjs_and_observables | observable]] to emit at least one value before emitting anything <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>, <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. After that, it emits a new array whenever *any* of the source [[introduction_to_rxjs_and_observables | observables]] emit a new value <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
    *   **Result**: Provides the current state of every [[introduction_to_rxjs_and_observables | observable]] in the input array <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

*   **`merge`**
    *   **Purpose**: Combines multiple [[introduction_to_rxjs_and_observables | observables]] into a single output [[introduction_to_rxjs_and_observables | observable]], emitting values as they arrive from any of the sources <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>, <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
    *   **Behavior**: Unlike `combineLatest`, it does not wait for all sources to emit; it simply emits each value one by one as it comes in, regardless of its source's position <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>, <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>, <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Error Handling Operators

[[handling_errors_and_preventing_memory_leaks_in_rxjs | Error handling]] in RxJS streams offers significant flexibility <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>, <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

*   **`catchError`**
    *   **Purpose**: Intercepts an error and allows you to emit some other default value or a new [[introduction_to_rxjs_and_observables | observable]] in its place <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>, <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
    *   **Benefit**: Prevents uncaught errors from crashing the application and allows for graceful degradation or user feedback <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>, <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

*   **`retry`**
    *   **Purpose**: Retries the source [[introduction_to_rxjs_and_observables | observable]] a specified number of times if an error occurs <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>, <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
    *   **Usage**: Extremely useful when dealing with HTTP calls that might fail due to network issues <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

### Memory Leak Prevention and Completion Operators

[[handling_errors_and_preventing_memory_leaks_in_rxjs | Preventing memory leaks]] is crucial in RxJS <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

*   **`unsubscribe()`**
    *   **Purpose**: Manually stops a subscription, preventing it from running indefinitely and causing a memory leak <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>, <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
    *   **Usage**: Call `subscription.unsubscribe()` at an appropriate point in your code <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>, <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

*   **`takeWhile`**
    *   **Purpose**: Emits values from the source [[introduction_to_rxjs_and_observables | observable]] only while a specified condition is true <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>, <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
    *   **Behavior**: When the condition becomes false, the [[introduction_to_rxjs_and_observables | observable]] completes, automatically preventing memory leaks without manual unsubscription <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>, <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>, <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

*   **`takeUntil`**
    *   **Purpose**: Completes the source [[introduction_to_rxjs_and_observables | observable]] when another specified "notifier" [[introduction_to_rxjs_and_observables | observable]] emits its first value <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>, <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>, <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>, <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
    *   **Usage**: Useful when an [[introduction_to_rxjs_and_observables | observable]]'s lifespan should be tied to another event, such as a timer finishing <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>, <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>, <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.

These [[RxJS Operators | operators]] provide a robust toolkit for managing asynchronous data flows, making RxJS a powerful choice for modern JavaScript applications.