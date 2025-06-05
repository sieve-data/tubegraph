---
title: Creating and Subscribing to Observables
videoId: 2LCo926NFLI
---

From: [[fireship]] <br/> 

[[introduction_to_rxjs_and_observables | ReactiveX]] (or [[introduction_to_rxjs_and_observables | RxJS]]) has revolutionized modern application development by allowing data to be treated as a stream unfolding over time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article provides a foundational understanding of how to create and subscribe to [[introduction_to_rxjs_and_observables | observables]] in [[introduction_to_rxjs_and_observables | RxJS]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Environment Setup

For demonstration purposes, a basic HTML page is used with the `rxjs` script imported from a CDN in the `<head>` section <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. All custom code resides in a `lesson.js` file, imported in the `<body>` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. A helper function `print` is created in `lesson.js` to append results from an [[introduction_to_rxjs_and_observables | observable]] to the browser display <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## What are Observables?

An [[introduction_to_rxjs_and_observables | observable]] can be conceptually thought of as an array that builds up over time <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. You can "loop" over this "array" in the dimension of time by subscribing to it <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Creating Observables

### Manually with `Observable.create`

You can create an [[introduction_to_rxjs_and_observables | observable]] from scratch using `Rx.Observable.create` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This method takes an `observer` function where you define what values the [[introduction_to_rxjs_and_observables | observable]] sends to its subscribers <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. To send a value, call `observer.next()` with the desired data, which can be any type like a string or object <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

```javascript
// Example: Manually emitting "hello world"
Rx.Observable.create(observer => {
    observer.next("hello world");
}).subscribe(value => print(value)); // Prints "hello world"
```

### From DOM Events with `Observable.fromEvent`

[[introduction_to_rxjs_and_observables | Observables]] can be created from DOM events using `Observable.fromEvent` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Pass it the target element (e.g., `document`) and the event name (e.g., `'click'`) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Each click event will then be emitted by the [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

```javascript
// Example: Observing click events
Observable.fromEvent(document, 'click').subscribe(event => {
    console.log(event); // Logs the full MouseEvent object
});
```

### From Promises with `Observable.fromPromise`

Existing JavaScript promises can be converted directly into [[introduction_to_rxjs_and_observables | observables]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This is useful when integrating with libraries built on promises <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

```javascript
// Example: Converting a promise
const myPromise = new Promise(resolve => {
    setTimeout(() => resolve("resolved"), 1000); // Simulates API call
});
Observable.fromPromise(myPromise).subscribe(value => print(value)); // Prints "resolved" after 1 second
```

An [[introduction_to_rxjs_and_observables | observable]] can also be converted back to a promise by calling `toPromise()` on it <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Timers with `Observable.timer` and `Observable.interval`

*   **`Observable.timer`**: Creates an [[introduction_to_rxjs_and_observables | observable]] that emits a single value after a specified duration (in milliseconds) <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **`Observable.interval`**: Creates an [[introduction_to_rxjs_and_observables | observable]] that repeatedly emits values after a specified time frame <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

```javascript
// Example: Timer
Observable.timer(1000).subscribe(() => print("Timer ran out")); // Prints "Timer ran out" after 1 second

// Example: Interval
Observable.interval(1000).subscribe(() => print(new Date().getSeconds())); // Prints current second every second
```

### From Static Values with `Observable.of`

`Observable.of` allows you to pass any static value or sequence of values to be emitted by the [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This demonstrates that any type of data can be treated as a stream <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

```javascript
// Example: Emitting various static types
Observable.of("hello", ["world"], 123, true, { type: "object" })
    .subscribe(value => print(value));
```

## Subscribing to Observables

To make an [[introduction_to_rxjs_and_observables | observable]] start emitting values, you must call the `subscribe()` method on it <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The `subscribe()` method takes a function that will be executed for each value emitted by the [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Hot vs. Cold Observables

Understanding the distinction between [[hot_vs_cold_observables | hot and cold observables]] is crucial:

*   **Cold [[hot_vs_cold_observables | Observable]]**: The data source is created *inside* the [[introduction_to_rxjs_and_observables | observable]]. This means the underlying data won't be created until something subscribes to it <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Each new subscriber triggers a new execution of the [[introduction_to_rxjs_and_observables | observable]], potentially resulting in different values for each subscriber <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

    ```javascript
    // Example: Cold Observable
    const coldObs = Rx.Observable.create(observer => {
        observer.next(Math.random()); // Random number generated inside
    });
    coldObs.subscribe(val => print(`Subscriber 1 (cold): ${val}`)); // Gets one random number
    coldObs.subscribe(val => print(`Subscriber 2 (cold): ${val}`)); // Gets a different random number
    ```

*   **Hot [[hot_vs_cold_observables | Observable]]**: The value is built *outside* the [[introduction_to_rxjs_and_observables | observable]], or the [[introduction_to_rxjs_and_observables | observable]] is explicitly made hot <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This ensures that all subscribers receive the *same* value <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

    ```javascript
    // Example: Hot Observable (value created outside)
    const hotValue = Math.random();
    const hotObsExternal = Rx.Observable.create(observer => {
        observer.next(hotValue); // Uses the same random number
    });
    hotObsExternal.subscribe(val => print(`Subscriber 1 (hot/external): ${val}`));
    hotObsExternal.subscribe(val => print(`Subscriber 2 (hot/external): ${val}`));
    ```

    You can also make a cold [[introduction_to_rxjs_and_observables | observable]] hot by calling `publish()` on it and then `connect()` <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. `publish()` tells the [[introduction_to_rxjs_and_observables | observable]] to only emit data once `connect()` is called, sharing the emissions among subscribers <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

    ```javascript
    // Example: Making a cold Observable hot with publish/connect
    const coldObsToHot = Rx.Observable.create(observer => {
        observer.next(Math.random());
    }).publish(); // Becomes a ConnectableObservable

    coldObsToHot.subscribe(val => print(`Subscriber 1 (hot/published): ${val}`));
    coldObsToHot.subscribe(val => print(`Subscriber 2 (hot/published): ${val}`));

    coldObsToHot.connect(); // Triggers emission for all subscribers
    ```

## Completing and Unsubscribing from Observables

An [[introduction_to_rxjs_and_observables | observable]] sends a `completed` signal when it reaches the end of its lifecycle <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For example, a `timer` [[introduction_to_rxjs_and_observables | observable]] completes automatically <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. The `finally` operator can be used to execute code once the [[introduction_to_rxjs_and_observables | observable]] is completed <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

```javascript
// Example: Observable completing naturally
Observable.timer(1000)
    .finally(() => print("All done!"))
    .subscribe(() => print("Timer emitted")); // Prints "Timer emitted", then "All done!"
```

However, some [[introduction_to_rxjs_and_observables | observables]], like `interval`, do not complete on their own <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. In such cases, if not handled, this can lead to [[handling_errors_and_preventing_memory_leaks_in_rxjs | memory leaks]], especially with data-intensive streams <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

To manually stop an [[introduction_to_rxjs_and_observables | observable]] from emitting values and send the `complete` signal, you can store the subscription and call `unsubscribe()` on it <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

```javascript
// Example: Manual unsubscribe
const intervalSubscription = Observable.interval(1000).subscribe(val => print(val));
setTimeout(() => {
    intervalSubscription.unsubscribe(); // Stops the interval after 3 seconds
    print("Interval unsubscribed!");
}, 3000);
```

More sophisticated ways to complete [[introduction_to_rxjs_and_observables | observables]] include using operators like `takeUntil` and `takeWhile` <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.