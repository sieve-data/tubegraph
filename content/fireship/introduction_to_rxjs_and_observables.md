---
title: Introduction to RxJS and Observables
videoId: ewcoEYS85Co
---

From: [[fireship]] <br/> 

[[rxjs_operators_and_their_usage | RxJS]] is a powerful JavaScript library designed to help control data as it flows through the dimension of time <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It addresses limitations in JavaScript for handling asynchronous streams of data, where promises only work with single asynchronous values and callbacks can lead to "callback hell" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. [[rxjs_operators_and_their_usage | RxJS]] provides a powerful functional library for dealing with data streams, which refers to any data source that unfolds over time, such as data from Firebase, DOM events, WebSockets, or file uploads <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. It is gaining significant popularity, with more daily npm downloads than Angular and Reactive View <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Installation and Setup
To begin using [[rxjs_operators_and_their_usage | RxJS]], you need to install it <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The version 6.4 was mentioned <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### [[effective_importing_in_rxjs | Effective Importing in RxJS]]
It's crucial to import [[rxjs_operators_and_their_usage | RxJS]] correctly to avoid bundling the entire library into your code <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Incorrectly using `import * as RX` can lead to a large bundle size (e.g., 47 kilobytes) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. [[rxjs_operators_and_their_usage | RxJS]] is a tree-shakable library, meaning you should only import the specific classes and [[rxjs_operators_and_their_usage | operators]] you need <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This practice can significantly reduce your bundle size (e.g., to less than 2 kilobytes) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Understanding Observables
The most fundamental class in [[rxjs_operators_and_their_usage | RxJS]] is the `Observable` <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

> [!definition] Observable
> An `Observable` can be thought of as a wrapper for some data that can be subscribed to. When a subscriber is active, they will be notified anytime the data changes <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
>
> You can also think of an `Observable` as essentially a pipe for data, and [[rxjs_operators_and_their_usage | RxJS]] provides tools to modify these pipes <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### [[creating_and_subscribing_to_observables | Creating and Subscribing to Observables]]
When you create an `Observable`, it provides a callback function that you can use to notify a subscriber with new data <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Calling `next()` on the observer is like emitting an event to the subscriber <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

```javascript
// Example of creating an Observable from scratch
const observable = new Observable(observer => {
  observer.next('A');
  observer.next('B');
  observer.next('C');
});
```
<a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>

To consume data from an `Observable`, you create a subscription by calling `subscribe()` on it <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The `subscribe()` method takes a function that will be called every time the `Observable` emits a new value, demonstrating reactive programming <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

```javascript
observable.subscribe(value => print(value)); // Assuming 'print' is a helper to display values
```
<a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>

### Completing Observables
`Observables` can be completed, meaning they will shut off and no longer emit values <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This is done by calling `observer.complete()` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

```javascript
const observable = new Observable(observer => {
  observer.next('A');
  observer.next('B');
  observer.complete(); // The stream is closed here
  observer.next('C'); // This value will not be emitted
});
```
<a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>

> [!analogy] Plumber Analogy
> Creating an `Observable` is like connecting a pipe to a water source, and subscribing is like opening the valve that lets the water out <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Helper Functions for Creating Observables
[[rxjs_operators_and_their_usage | RxJS]] provides several helper functions to simplify `Observable` creation:

*   **`of()`**: Creates an `Observable` from a raw value, emitting the entire value as a single event <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    ```javascript
    import { of } from 'rxjs';
    of('Hello').subscribe(value => print(value)); // Emits "Hello"
    ```
    <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>
*   **`from()`**: Takes an array, promise, or iterable and emits each individual item from it <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. For example, passing a string to `from()` will emit each character individually <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    ```javascript
    import { from } from 'rxjs';
    from('Hello').subscribe(char => print(char)); // Emits H, e, l, l, o
    ```
    <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>
*   **`fromEvent()`**: Creates an `Observable` from DOM events. It takes a DOM element and the event to listen to <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
    ```javascript
    import { fromEvent } from 'rxjs';
    fromEvent(document, 'click').subscribe(event => print(event)); // Emits click events
    ```
    <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   **`interval()`**: Sets up an `Observable` based on a time interval, emitting a number each time the interval passes <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
    ```javascript
    import { interval } from 'rxjs';
    interval(1000).subscribe(num => print(num)); // Emits 0, 1, 2... every second
    ```
    <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

### Schedulers
[[rxjs_operators_and_their_usage | RxJS]] can be synchronous or asynchronous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This behavior can be controlled by modifying schedulers <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. By default, an `Observable` created with `of()` will be treated as an asynchronous value, with its subscription happening on the main thread <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. However, passing in the `asyncScheduler` will cause the `Observable` value to be emitted on the next iteration of the event loop <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

```javascript
import { of, asyncScheduler } from 'rxjs';

of('Hello').subscribe(val => print(val)); // Synchronous by default, prints 'Hello' then 'World' if 'World' is printed immediately after
print('World'); // Result: Hello, World (if run synchronously)
```
<a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>
```javascript
import { of, asyncScheduler } from 'rxjs';

of('Hello', asyncScheduler).subscribe(val => print(val));
print('World'); // Result: World, Hello (due to async scheduler)
```
<a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>

### [[hot_vs_cold_observables | Hot vs Cold Observables]]
The distinction between [[hot_vs_cold_observables | hot and cold observables]] is important <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

*   **Cold Observables**: Can only have one subscription <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. They don't actually create the underlying value until they are subscribed to <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. If subscribed to multiple times, a cold `Observable` will execute its creation logic for each subscription, potentially yielding different values (e.g., a new random number each time) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Hot Observables**: Can have multiple subscriptions <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. They allow a value to be shared or broadcast across multiple subscribers <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. The `shareReplay(1)` [[rxjs_operators_and_their_usage | operator]] is a common way to make a cold `Observable` hot by caching the last value and sharing it with new subscribers <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### [[using_subjects_and_multicasting_in_rxjs | Using Subjects and Multicasting in RxJS]]
Instead of making cold `Observables` hot, it's often more common to create subjects or behavior subjects <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

*   **Subject**: A `Subject` is a type of hot `Observable` that has the added benefit of being able to have new values pushed to it using its `next()` method <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. A potential "gotcha" with a regular `Subject` is that subscriptions need to be set up *before* values are added to it; late subscribers will not receive past values <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

    ```javascript
    import { Subject } from 'rxjs';
    const subject = new Subject();
    subject.subscribe(value => print('Subscriber 1: ' + value));
    subject.next('A');
    subject.next('B');
    subject.subscribe(value => print('Subscriber 2: ' + value)); // Subscriber 2 will get nothing if A, B already emitted
    subject.next('C'); // Both subscribers will get C
    ```
    <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>
*   **BehaviorSubject**: Similar to a `Subject`, but it has the concept of a "current value" <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This means the last emitted value will be cached, ensuring that every new subscription always receives an immediate value, even if they subscribe late <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This is a powerful feature for state management in front-end applications <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

    ```javascript
    import { BehaviorSubject } from 'rxjs';
    const behaviorSubject = new BehaviorSubject('Initial'); // Initial value
    behaviorSubject.subscribe(value => print('Subscriber 1: ' + value)); // Gets "Initial"
    behaviorSubject.next('A');
    behaviorSubject.next('B');
    behaviorSubject.subscribe(value => print('Subscriber 2: ' + value)); // Gets "B" immediately
    behaviorSubject.next('C'); // Both subscribers get C
    ```
    <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>

## [[rxjs_operators_and_their_usage | RxJS Operators and Their Usage]]
[[rxjs_operators_and_their_usage | Operators]] are functions that help you control and transform the flow of data going through your `Observables` <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. You can compose multiple [[rxjs_operators_and_their_usage | operators]] together using the `pipe()` method, where data flows through and is modified by each function <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

```javascript
import { from } from 'rxjs';
import { map, filter, scan, tap, take } from 'rxjs/operators';

const sourceObservable = from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
```
<a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>

### Common Operators
*   **`map()`**: Transforms each emitted item from the input to a new output <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
    ```javascript
    sourceObservable.pipe(
      map(num => num * num) // Squares each number
    ).subscribe(value => print(value)); // Emits 1, 4, 9...
    ```
    <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>
*   **`scan()`**: Accumulates values as they flow through the `Observable`, similar to `Array.prototype.reduce()` <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    ```javascript
    sourceObservable.pipe(
      scan((acc, curr) => acc + curr, 0) // Keeps a running total
    ).subscribe(value => print(value)); // Emits 1, 3, 6, 10...
    ```
    <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
    The order of [[rxjs_operators_and_their_usage | operators]] in the `pipe()` matters, as it affects the transformation logic <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **`filter()`**: Prevents certain items from being emitted in the stream based on a condition <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    ```javascript
    sourceObservable.pipe(
      filter(num => num > 5) // Only allows numbers greater than 5
    ).subscribe(value => print(value)); // Emits 6, 7, 8, 9, 10
    ```
    <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
*   **`take()`**: Tells the `Observable` to complete after emitting a specified number of values <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
    ```javascript
    sourceObservable.pipe(
      take(3) // Emits only the first 3 values then completes
    ).subscribe(value => print(value)); // Emits 1, 2, 3
    ```
    <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>
*   **`tap()`**: Allows you to trigger side effects from inside the `Observable` pipe without modifying the stream <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Useful for logging, debugging, or saving values to a backend database <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    ```javascript
    sourceObservable.pipe(
      tap(val => console.log('Initial value:', val)),
      map(num => num * 2),
      tap(val => console.log('Mapped value:', val))
    ).subscribe(value => print(value));
    ```
    <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>

### Backpressure Operators
Backpressure occurs when an `Observable` emits values faster than a subscriber can process them <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

*   **`debounceTime()`**: Filters out all events until they have stopped happening for a certain period of time <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Useful for type-ahead suggestions where you don't want to make an API call until the user is done typing <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
    ```javascript
    import { fromEvent } from 'rxjs';
    import { debounceTime } from 'rxjs/operators';
    fromEvent(document, 'mousemove').pipe(
      debounceTime(1000) // Emits only after 1 second of no mouse movement
    ).subscribe(event => print(event.clientX));
    ```
    <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   **`throttleTime()`**: Emits the first value and then ensures no additional values can be emitted until a certain time period has passed <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
    ```javascript
    import { fromEvent } from 'rxjs';
    import { throttleTime } from 'rxjs/operators';
    fromEvent(document, 'mousemove').pipe(
      throttleTime(1000) // Emits at most one event per second
    ).subscribe(event => print(event.clientX));
    ```
    <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>
*   **`buffer()`**: Collects events into an array and only emits them when the buffer reaches a specified length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This keeps all data but processes it in chunks.
    ```javascript
    import { fromEvent } from 'rxjs';
    import { buffer, take } from 'rxjs/operators';
    fromEvent(document, 'mousemove').pipe(
      buffer(fromEvent(document, 'click')), // collects mouse moves until a click happens
      take(1) // for demo purposes, take one buffer
    ).subscribe(events => print(`Buffered ${events.length} mouse events`));
    ```
    (The transcript mentioned `buffer` when a length of 20 is reached, this example is slightly modified to reflect the `buffer` operator which takes an `ObservableInput` as argument, `bufferCount` takes a number.) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>

### Combination Operators
These [[rxjs_operators_and_their_usage | operators]] combine multiple `Observables` or switch between them.

*   **`switchMap()`**: Allows you to start with one `Observable` and then switch to another, which is critical for handling relational data (e.g., fetching user data then user orders) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. It cancels previous inner `Observables` if a new source value arrives. This avoids nested subscriptions, leading to cleaner code <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
    ```javascript
    import { of } from 'rxjs';
    import { switchMap } from 'rxjs/operators';

    const userObservable = of({ id: 1, name: 'John Doe' });
    const getUserOrders = (userId) => of(['Order A', 'Order B']); // Simulate fetching orders

    userObservable.pipe(
      switchMap(user => getUserOrders(user.id)) // Switches to an observable of orders
    ).subscribe(orders => print(orders)); // Emits ['Order A', 'Order B']
    ```
    <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>
*   **`combineLatest()`**: Takes an array of `Observables` and waits for each to emit a value. It then emits all values together as an array <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. If any `Observable` emits after that, it will emit everything again, providing the current state of every `Observable` in the array <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    ```javascript
    import { combineLatest, of } from 'rxjs';
    import { delay } from 'rxjs/operators';

    const obs1 = of(Math.random());
    const obs2 = of(Math.random()).pipe(delay(1000));

    combineLatest([obs1, obs2]).subscribe(values => print(values)); // Waits for obs2, then emits [val1, val2]
    ```
    <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>
*   **`merge()`**: Emits each value one by one as it comes in from any of the merged `Observables`, without waiting for all `Observables` to emit <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. It cares about when values are emitted in the context of time <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
    ```javascript
    import { merge, of } from 'rxjs';
    import { delay } from 'rxjs/operators';

    const obs1 = of('A');
    const obs2 = of('B').pipe(delay(500));
    const obs3 = of('C');

    merge(obs1, obs2, obs3).subscribe(value => print(value)); // Emits A, C, then B (after 500ms)
    ```
    <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>

## [[handling_errors_and_preventing_memory_leaks_in_rxjs | Handling Errors and Preventing Memory Leaks in RxJS]]

### Error Handling
A common strategy for error handling is to catch the error and replace it with some other value <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

*   **`catchError()`**: Intercepts an error in the stream and allows you to emit some other default value, preventing an uncaught error in the console <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **`retry()`**: Easily retries an `Observable` chain, super useful when working with HTTP calls <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

```javascript
import { Subject, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

const errorSubject = new Subject();
errorSubject.pipe(
  catchError(error => {
    print('Caught error: ' + error);
    return of('Default Value'); // Replace error with a default value
  }),
  // retry(3) // Optional: retry the observable 3 times on error
).subscribe(
  value => print('Received: ' + value),
  err => print('Final Error (should not happen with catchError): ' + err) // This callback is for uncaught errors
);

errorSubject.next('Good Value');
errorSubject.error('Something went wrong!'); // Will trigger catchError
errorSubject.next('Another Value'); // Will not be emitted if catchError completes the stream or replaces it
```
<a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>

### Preventing Memory Leaks
Memory leaks in [[rxjs_operators_and_their_usage | RxJS]] often occur when subscriptions are not properly closed <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

*   **`unsubscribe()`**: Manually call `unsubscribe()` on a `Subscription` object to stop an `Observable` from emitting values <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
    ```javascript
    import { interval } from 'rxjs';
    const myInterval = interval(1000);
    const subscription = myInterval.subscribe(num => print(num));
    setTimeout(() => {
      subscription.unsubscribe(); // Stops the interval after 5 seconds
      print('Unsubscribed!');
    }, 5000);
    ```
    <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>
*   **`takeWhile()`**: Pipes into an `Observable` to tell it to emit values only while a certain condition is true <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. When the condition becomes false, the `Observable` completes, preventing memory leaks without manual unsubscription <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
    ```javascript
    import { interval } from 'rxjs';
    import { takeWhile } from 'rxjs/operators';
    interval(1000).pipe(
      takeWhile(num => num < 5) // Emits until the number is 5, then completes
    ).subscribe(num => print(num));
    ```
    <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>
*   **`takeUntil()`**: Takes another `Observable` as its argument <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. When that argument `Observable` emits something, it will cancel the subscription on the source `Observable` <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Useful when an `Observable` needs to stop based on an event from another `Observable` (e.g., a timer or a UI event).
    ```javascript
    import { interval, timer } from 'rxjs';
    import { takeUntil } from 'rxjs/operators';
    interval(1000).pipe(
      takeUntil(timer(5000)) // Emits until 5 seconds have passed, then completes
    ).subscribe(num => print(num));
    ```
    <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>