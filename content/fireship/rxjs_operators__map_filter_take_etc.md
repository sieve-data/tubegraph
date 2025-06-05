---
title: RxJS Operators  Map Filter Take etc
videoId: 2LCo926NFLI
---

From: [[fireship]] <br/> 

[[introduction_to_rxjs_and_observables | ReactiveX]] has transformed how modern developers approach building applications by enabling them to treat all data as a stream unfolding over time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores various ways to utilize RxJS, providing a solid foundation for its use in projects <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

The setup involves a basic HTML page importing the RxJS script from a CDN and a `lesson.js` file for custom code <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. A helper function, `print`, is used to append observable results to the browser <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## [[introduction_to_rxjs_and_observables | Observables]]

An [[introduction_to_rxjs_and_observables | observable]] can be conceptualized as an array that builds over time, which can be looped over by subscribing to it <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Creating Observables

*   **`Rx.Observable.create`**: Allows for creating an [[introduction_to_rxjs_and_observables | observable]] from scratch by defining what it sends to a subscriber via an observer function, typically by calling `observer.next()` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **`Observable.fromEvent`**: Converts DOM events, such as clicks, into an [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **`Observable.fromPromise`**: Transforms a JavaScript Promise directly into an [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **`observable.toPromise`**: Conversely, an [[introduction_to_rxjs_and_observables | observable]] can be converted back to a Promise by calling `toPromise()` on it <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **`Observable.timer`**: Creates a timer that emits a value once a specified duration (in milliseconds) has passed <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **`Observable.interval`**: Creates a repeating timer that emits a new value after a specified time frame <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **`Observable.of`**: Allows any static value (e.g., string, array, number, boolean, object) to be passed and treated as an [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Hot vs. Cold Observables

*   **Cold [[introduction_to_rxjs_and_observables | Observable]]**: Data is created inside the [[introduction_to_rxjs_and_observables | observable]]. It only generates the underlying data when something subscribes to it, meaning each subscriber gets a different instance of the data <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Hot [[introduction_to_rxjs_and_observables | Observable]]**: The value is built outside the [[introduction_to_rxjs_and_observables | observable]], allowing all subscribers to receive the same data <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   An [[introduction_to_rxjs_and_observables | observable]] can be made hot by calling `publish()` on the cold [[introduction_to_rxjs_and_observables | observable]], which tells it to emit data only when `connect()` is called <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Completing Observables

An [[introduction_to_rxjs_and_observables | observable]] sends a "completed" signal when its lifecycle ends <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

*   **`finally`**: An [[rxjs_operators_and_their_usage | RxJS operator]] that executes code once the [[introduction_to_rxjs_and_observables | observable]] is completed <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **`unsubscribe`**: Manually forces the [[introduction_to_rxjs_and_observables | observable]] to send the complete signal, which is crucial for [[handling_errors_and_preventing_memory_leaks_in_rxjs | preventing memory leaks]] with observables that don't complete automatically (e.g., `interval`) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## [[rxjs_operators_and_their_usage | RxJS Operators]]

[[rxjs_operators_and_their_usage | RxJS operators]] are functions that allow for transforming, filtering, or combining [[introduction_to_rxjs_and_observables | observables]].

*   **`map`**: Transforms emitted values based on custom logic <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. For example, it can convert numbers to their logarithms or parse JSON strings from an API response into JavaScript objects <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **`do`**: Executes code without altering the underlying [[introduction_to_rxjs_and_observables | observable]] data, providing a glimpse into the data at any point in time <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **`filter`**: Filters values, only allowing those that meet a specified condition to pass through <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   **`first`**: Takes only the very first element emitted by the [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **`last`**: Takes only the very last element emitted by the [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **`throttle` / `throttleTime`**: Useful for events emitting frequently (e.g., `mousemove`). It emits the first event and then delays before allowing any additional events to be emitted <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **`debounce` / `debounceTime`**: Similar to `throttle`, but it emits the *last* event after a specified delay, useful for ensuring a user has stopped an action like typing in an autocomplete form <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **`scan`**: Keeps a running total or aggregation of each emitted value, similar to the [[modern_javascript_array_methods | JavaScript array's `reduce` function]] <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **`switchMap`**: Allows an [[introduction_to_rxjs_and_observables | observable]] to switch to a new inner [[introduction_to_rxjs_and_observables | observable]] based on a value from the outer [[introduction_to_rxjs_and_observables | observable]]. If the outer [[introduction_to_rxjs_and_observables | observable]] emits a new value, the previous inner [[introduction_to_rxjs_and_observables | observable]] is reset <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. This is common for scenarios like querying user data after receiving a user ID <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a>.
*   **`takeUntil`**: Completes an [[introduction_to_rxjs_and_observables | observable]] based on the emission of a value from another [[introduction_to_rxjs_and_observables | observable]], providing a clever way to unsubscribe <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **`takeWhile`**: Tells an [[introduction_to_rxjs_and_observables | observable]] to emit values until a certain condition becomes true <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Combining Observables

*   **`zip`**: Combines multiple observables into arrays based on their index position, useful for observables of the same length that are related <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **`forkJoin`**: Waits for all input observables to complete, then combines their *last* emitted values together into an array <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. This is useful when waiting for multiple related API calls to resolve before updating a UI <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

### Error Handling

*   **`catch`**: Allows for catching errors within an [[introduction_to_rxjs_and_observables | observable]] stream and performing error handling, similar to how promises work in [[working_with_functions_and_arrays_in_typescript | JavaScript]] <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **`retry`**: Reruns the [[introduction_to_rxjs_and_observables | observable]] a specified number of times when an error occurs <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

## [[using_subjects_and_multicasting_in_rxjs | RxJS Subject]]

A [[using_subjects_and_multicasting_in_rxjs | Subject]] is an [[introduction_to_rxjs_and_observables | observable]] with additional features, primarily the ability to emit new data to its subscribers by acting as a proxy to another data source <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Unlike a normal [[introduction_to_rxjs_and_observables | observable]], you can directly call `subject.next()` to broadcast new values to subscribers without relying on an external source <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

### [[using_subjects_and_multicasting_in_rxjs | Multicasting]]

[[using_subjects_and_multicasting_in_rxjs | Multicast]] is used to send values to multiple subscribers without repeating related side effects <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. By calling `multicast()` on the original [[introduction_to_rxjs_and_observables | observable]] and having it return a new [[using_subjects_and_multicasting_in_rxjs | Subject]], you can add multiple subscriptions to the [[using_subjects_and_multicasting_in_rxjs | Subject]] and then call `connect()` on it. This ensures that side effects (e.g., console logs from a `do` operator) only run once, regardless of the number of subscribers <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. This is highly beneficial for data sources with multiple subscribers that perform side effects <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.