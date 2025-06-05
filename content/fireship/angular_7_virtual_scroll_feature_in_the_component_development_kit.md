---
title: Angular 7 virtual scroll feature in the component development kit
videoId: Ppl64MY6FFc
---

From: [[fireship]] <br/> 

Angular 7 officially introduces the [[setting_up_virtual_scroll_in_an_angular_app | virtual scroll]] behavior within the Component Development Kit (CDK) <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This feature enables the creation of high-performance lists that only render items currently visible to the user <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Benefits of Virtual Scrolling
[[benefits_and_use_cases_of_virtual_scrolling | Virtual scrolling]] is particularly useful when dealing with a large number of items in a list <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Instead of rendering all items, it only renders those visible in the viewport <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This approach significantly improves performance by reducing the browser's rendering workload to a small subset of the total data <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The CDK provides components and directives to simplify the implementation of [[benefits_and_use_cases_of_virtual_scrolling | virtual scrolling]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, and tools to measure scrolled elements for dynamic data fetching from a backend database in batches <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Setting up Virtual Scroll
To use [[setting_up_virtual_scroll_in_an_angular_app | virtual scroll]]:
1.  Ensure your Angular project is updated to version 7 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  Add the CDK to your application by running `ng add @angular/material` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Accept the default prompts <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
3.  For backend integration, install `angularfire` (e.g., for [[optimizing_performance_with_virtual_scroll_and_firebase | Firebase]] interaction) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  In your `app.module.ts`, import `ScrollingModule` from the CDK and add it to your `imports` array <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Optionally, include `AngularFireModule` for backend functionalities <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Generating Data and Basic Implementation
To demonstrate [[setting_up_virtual_scroll_in_an_angular_app | virtual scroll]], you'll need a large list of items <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. You can use libraries like `faker.js` to generate fake data such as names and email addresses <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

In your component's HTML, the `cdk-virtual-scroll-viewport` [[using_angular_components_and_component_architecture | component]] creates the context for [[setting_up_virtual_scroll_in_an_angular_app | virtual scroll]] <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. It requires an `itemSize` argument, representing the height of each item in pixels <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. For optimal performance, items in a [[setting_up_virtual_scroll_in_an_angular_app | virtual scroll]] list should ideally have a fixed height <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

```html
<cdk-virtual-scroll-viewport itemSize="100">
  <!-- Content goes here -->
</cdk-virtual-scroll-viewport>
```
In your CSS, ensure the viewport has a defined height, and each item inside has a fixed height that matches the `itemSize` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

Inside the `cdk-virtual-scroll-viewport`, use the `cdkVirtualFor` structural directive <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. It functions similarly to `ngFor` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

```html
<cdk-virtual-scroll-viewport itemSize="100">
  <div *cdkVirtualFor="let item of people">
    <!-- Item content -->
  </div>
</cdk-virtual-scroll-viewport>
```
The CDK tracks which items fit into the viewport <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. When an item is scrolled into view, it is rerendered in the DOM <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This behavior means CSS animations applied to list items will re-trigger each time the item is rerendered, unlike in a regular list where animations only apply on initial page load <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Virtual Scroll API and Events
The [[setting_up_virtual_scroll_in_an_angular_app | virtual scroll]] [[using_angular_components_and_component_architecture | component]] emits a custom event called `scrolledIndexChange` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This event provides the index of the item the user has scrolled to, which is crucial for implementing infinite scroll by determining when to fetch the next batch of items <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

The component also has a public API to perform actions such as:
*   Measuring the viewport <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   Getting the total item list size <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Dynamically scrolling to a specific element <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

To access these methods, you'll need to retrieve the [[using_angular_components_and_component_architecture | component]] from the DOM using `ViewChild` and strongly type it as `CdkVirtualScrollViewport` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

```typescript
import { CdkVirtualScrollViewport } from '@angular/cdk/scrolling';
import { ViewChild } from '@angular/core';

export class MyComponent {
  @ViewChild(CdkVirtualScrollViewport) viewport: CdkVirtualScrollViewport;

  // Use viewport.measureViewportRect() or viewport.getDataLength()
}
```
This allows dynamic interaction with the [[using_angular_components_and_component_architecture | component]], for example, to scroll to the bottom of a chat messages list or update scroll position when new messages arrive <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Infinite Real-time Scroll with Firestore
To build an [[optimizing_performance_with_virtual_scroll_and_firebase | infinite real-time scroll]] using [[optimizing_performance_with_virtual_scroll_and_firebase | Firestore]], several improvements are made:
*   The list is [[optimizing_performance_with_virtual_scroll_and_firebase | real-time]], meaning items are updated even when pulled in batches <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   The use of [[setting_up_virtual_scroll_in_an_angular_app | virtual scroll]] provides better performance for large lists <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   The CDK simplifies and makes the code more reliable <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Component Logic
In the [[using_angular_components_and_component_architecture | component]]'s TypeScript, import `AngularFirestore` and various operators from `rxjs` <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   Define a `BATCH_SIZE` (e.g., 20 items per batch) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   Use a `BehaviorSubject` to track the `offset` for [[optimizing_performance_with_virtual_scroll_and_firebase | Firestore]] queries, initializing it with `null` <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Listen to the `scrolledIndexChange` event on the `cdk-virtual-scroll-viewport` to trigger the `nextBatch` method when the user scrolls near the end of the current list <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

The `nextBatch` method checks if the `viewport.renderedRange.end` equals `viewport.getDataLength()` <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. If so, it means the end of the list has been reached, and a new `offset` value (e.g., the last item's name) is sent to the `BehaviorSubject` to fetch the next batch <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

It's also beneficial to set up a `trackBy` function for `cdkVirtualFor` to track items by their index <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This ensures that only changed items are rerendered, which is important for [[optimizing_performance_with_virtual_scroll_and_firebase | real-time]] data to prevent the entire list from rerendering on every change <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Fetching Batches from Firestore
To get a batch from [[optimizing_performance_with_virtual_scroll_and_firebase | Firestore]]:
1.  Order the query by a specific field (e.g., user's name) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
2.  Use `startAfter` with the `offset` value (which is `null` for the first batch, or the last item's name for subsequent batches) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
3.  `limit` the query to the `BATCH_SIZE` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  Call `snapshotChanges()` to get document snapshots as an observable <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. If an empty array is emitted, it signifies the end of the collection <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

For [[optimizing_performance_with_virtual_scroll_and_firebase | real-time]] updates across multiple batches, map the array of documents to an object where the key is the document ID <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. This allows updating documents based on their unique key rather than their index position, preventing duplicate documents if data changes between queries <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

In the constructor, set up a source observable that listens to the `offset` value <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Use `mergeMap` (not `switchMap`) to merge new batches into the stream <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. `mergeMap` is crucial because `switchMap` would cancel previous subscriptions, making only the last batch [[optimizing_performance_with_virtual_scroll_and_firebase | real-time]] <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Throttle the stream (e.g., by 500ms) to avoid redundant backend requests <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Pipe in the `scan` operator to merge the current batch with existing batches <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This `batchMap` observable becomes the main source of truth, containing all mappings for individual item keys and their data <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Finally, transform this map into an array of objects (e.g., using `Object.values()`) for rendering in the frontend <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

### HTML Modifications
In the HTML template:
*   Optionally show the item index by declaring `let i = index` in `*cdkVirtualFor` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   Add the `trackBy` function defined in the component <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   Listen to the `(scrolledIndexChange)` event, passing the event itself and the offset value (e.g., `people[event]?.name` for the last person's name in the array) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   Unwrap the infinite observable using an `ng-container` and the `async` pipe, aliasing the array of objects to a template variable (e.g., `as people`) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

```html
<cdk-virtual-scroll-viewport itemSize="100" (scrolledIndexChange)="nextBatch($event, people[people.length - 1]?.name)">
  <ng-container *ngIf="infiniteObservable | async as people">
    <div *cdkVirtualFor="let person of people; let i = index; trackBy: trackByIndex">
      {{ i }}: {{ person.name }} - {{ person.bio }} {{ person.emoji }}
    </div>
  </ng-container>
</cdk-virtual-scroll-viewport>
```

When observed, the data is queried in alphabetical order, mirroring the [[optimizing_performance_with_virtual_scroll_and_firebase | Firebase]] console <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Changes made to the data on the backend are reflected in the UI in [[optimizing_performance_with_virtual_scroll_and_firebase | real time]] <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. While item position might not change if data is updated or deleted (requiring additional logic for that functionality), the data itself remains current <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

The list size grows in batches (e.g., 20, 40, 60, etc.) as the user scrolls, creating a seamless "infinite" experience <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. When the end of the list is reached, a user indication can be displayed <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.