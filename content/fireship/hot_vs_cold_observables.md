---
title: Hot vs Cold Observables
videoId: ewcoEYS85Co
---

From: [[fireship]] <br/> 

In RxJS, understanding the distinction between hot and cold observables is crucial for managing data streams. The terminology can sometimes be confusing, but the core idea revolves around whether an observable starts producing values upon subscription or whether it's already "active" and broadcasting values regardless of subscriptions <a class="yt-timestamp" data-t="04:56:06"></a>.

> [!NOTE]
> The speaker notes that they don't particularly like the "hot" and "cold" terminology and suggests thinking of it as hot observables having multiple subscriptions, while cold observables typically have only one <a class="yt-timestamp" data-t="04:56:06"></a>.

## Cold Observables

A cold observable does not create its underlying value until it is subscribed to <a class="yt-timestamp" data-t="05:04:02"></a>. This means that each new subscriber will trigger the observable to start producing values from the beginning, resulting in potentially different values for each subscriber.

### Example: Random Number Generation
If an observable is created to generate a random number, and two separate subscriptions are made to it, each subscriber will receive a *different* random number <a class="yt-timestamp" data-t="05:09:05"></a>. This occurs because the creation callback function for the observable is invoked every time a subscription is created <a class="yt-timestamp" data-t="05:16:07"></a>.

## Hot Observables

A hot observable, in contrast, can have multiple subscriptions <a class="yt-timestamp" data-t="04:58:04"></a>. It is already producing or broadcasting values, and subscribers simply tap into that existing stream. This is often desirable when you want to share a single value or stream across multiple subscribers <a class="yt-timestamp" data-t="05:25:00"></a>.

### Converting Cold to Hot
If you have an existing cold observable, there are ways to make it hot, allowing it to broadcast to multiple subscribers <a class="yt-timestamp" data-t="05:29:05"></a>. The `shareReplay` operator is particularly useful for this, as it caches the last emitted value and ensures all subscribers receive the same value <a class="yt-timestamp" data-t="05:40:08"></a>.

```javascript
// Example: Converting a cold observable to hot using shareReplay
// (Simulated random number observable)
const randomNumberObservable = new Observable(observer => {
  const num = Math.random();
  observer.next(num);
  observer.complete();
});

// Using shareReplay to make it hot and share the same value
const hotObservable = randomNumberObservable.pipe(
  shareReplay(1) // Caches the last 1 value
);

hotObservable.subscribe(val => print(val)); // First subscriber gets the value
hotObservable.subscribe(val => print(val)); // Second subscriber gets the *same cached* value
```
After applying `shareReplay(1)`, both subscribers will receive the exact same random number, demonstrating that the observable is now hot <a class="yt-timestamp" data-t="05:44:06"></a>.

### [[using_subjects_and_multicasting_in_rxjs | Subjects]] as Hot Observables
Often, developers don't convert cold observables to hot; instead, they create [[using_subjects_and_multicasting_in_rxjs | Subjects]] or BehaviorSubjects <a class="yt-timestamp" data-t="05:50:00"></a>. A [[using_subjects_and_multicasting_in_rxjs | Subject]] is considered a hot observable because it can have new values pushed to it after it's been created, functioning more like a "pump" in plumbing terms <a class="yt-timestamp" data-t="05:56:06"></a>.

[[using_subjects_and_multicasting_in_rxjs | Subjects]] have a `next` method that allows new values to be added to the stream <a class="yt-timestamp" data-t="06:14:02"></a>. A key distinction is that a regular [[using_subjects_and_multicasting_in_rxjs | Subject]] requires subscriptions to be set up *before* values are added to the stream for them to be received <a class="yt-timestamp" data-t="06:18:04"></a>. For example, if a second subscriber joins late, it will not receive values that were emitted before its subscription <a class="yt-timestamp" data-t="06:29:04"></a>.

In contrast, a [[using_subjects_and_multicasting_in_rxjs | BehaviorSubject]] is similar to a [[using_subjects_and_multicasting_in_rxjs | Subject]] but maintains the concept of a "current value" <a class="yt-timestamp" data-t="06:41:05"></a>. This means the last emitted value is cached, ensuring that every new subscription always receives a value, even if it subscribes late <a class="yt-timestamp" data-t="06:47:04"></a>. This feature is very powerful for state management in front-end applications <a class="yt-timestamp" data-t="07:01:00"></a>.