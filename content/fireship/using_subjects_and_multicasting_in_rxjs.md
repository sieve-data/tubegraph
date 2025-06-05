---
title: Using Subjects and Multicasting in RxJS
videoId: 2LCo926NFLI
---

From: [[fireship]] <br/> 

[[introduction_to_rxjs_and_observables | ReactiveX]] has transformed how modern developers approach app building by enabling them to treat all data as a stream unfolding over time <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This article explores two advanced RxJS concepts: Subjects and Multicasting.

## RxJS Subjects

An RxJS Subject is an [[introduction_to_rxjs_and_observables | observable]] with additional features <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. It has the capability to emit new data to its subscribers by acting as a proxy to another data source <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

### Key Benefit of Subjects

While a plain [[introduction_to_rxjs_and_observables | observable]] emits values when subscribed to <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>, the significant advantage of a Subject is its ability to directly emit new values using the `next()` method <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This means you can broadcast new values to subscribers without relying on an external source data stream to build them <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

#### Example: Emitting Values with `subject.next()`

```javascript
// Create a new Subject
const mySubject = new rxjs.Subject(); <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>

// Create multiple subscriptions to the subject
mySubject.subscribe(value => print('Subscriber 1: ' + value)); <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>
mySubject.subscribe(value => print('Subscriber 2: ' + value)); <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>

// Emit values using subject.next()
mySubject.next('Hello'); <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>
mySubject.next('World'); <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>

// Emit another value after a timeout
setTimeout(() => mySubject.next('Delayed Message'), 1000); <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>
```

## Multicasting

Multicasting is used to send values to multiple subscribers while ensuring that related side effects from the source [[introduction_to_rxjs_and_observables | observable]] run only once <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

### The Problem Multicasting Solves (Side Effects)

Consider an [[introduction_to_rxjs_and_observables | observable]] created from DOM click events that also uses the `do` [[rxjs_operators_and_their_usage | operator]] to log a side effect (e.g., "Do one time") for each click <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. If you have multiple subscribers to this [[introduction_to_rxjs_and_observables | observable]], the `do` operator's code will run for *every single subscriber* with *every single emitted value* <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. For example, 100 clicks with 100 subscribers could lead to the side effect running 10,000 times <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. The desired behavior is for the side effect to run only once per emission from the source [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

### Implementing Multicasting with `multicast()`

To achieve this, you can use the `multicast()` operator:

1.  Call `multicast()` on the original [[introduction_to_rxjs_and_observables | observable]], instructing it to return a new Subject <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
2.  Add subscribers to this new Subject <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
3.  Call `connect()` on the Subject to start the observable's execution <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

This setup ensures that when you click in the DOM, the values are sent to all subscribers, but the side effect runs only once, regardless of how many subscribers there are <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This can be highly beneficial when multiple subscribers depend on a single data source that includes side effects <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

```javascript
// Data source: Click events in the DOM
const clicks = rxjs.fromEvent(document, 'click'); <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>

// Add a 'do' operator to illustrate a side effect
const sourceWithSideEffect = clicks.pipe(
    rxjs.operators.do(() => print('Do one time')) <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>
);

// Apply multicast to the source, using a Subject as the multicast subject
const multicasted = sourceWithSideEffect.pipe(
    rxjs.operators.multicast(new rxjs.Subject()) <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>
);

// Subscribe multiple times to the multicasted observable
multicasted.subscribe(value => print('Subscriber 1: ' + value.type)); <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>
multicasted.subscribe(value => print('Subscriber 2: ' + value.type)); <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>

// Call connect to start the observable
multicasted.connect(); <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>
```