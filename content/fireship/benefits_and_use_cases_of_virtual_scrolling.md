---
title: Benefits and use cases of virtual scrolling
videoId: Ppl64MY6FFc
---

From: [[fireship]] <br/> 

[[angular_7_virtual_scroll_feature_in_the_component_development_kit | Angular 7]] introduced virtual scroll as a key feature in its Component Development Kit (CDK), enabling the creation of high-performance lists that only render items visible to the user <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This behavior is crucial for [[optimizing_performance_with_virtual_scroll_and_firebase | optimizing performance]] when dealing with large datasets <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## What is Virtual Scrolling?
Virtual scrolling is a technique where only the items currently visible within the user's viewport are rendered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This differs from traditional lists where all items, regardless of visibility, are rendered on the page, potentially leading to performance issues <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Benefits of Virtual Scrolling
*   **Smoother Performance** <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>: By only rendering a small subset of data, the browser's workload is significantly reduced, resulting in a much smoother user experience, especially with large lists <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Reduced DOM Elements**: Fewer elements are present in the Document Object Model (DOM), leading to faster page loads and less memory consumption.
*   **Simplified Code**: The CDK provides components and directives that make [[setting_up_virtual_scroll_in_an_angular_app | implementing virtual scrolling]] straightforward and reliable <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## Core Concepts and Implementation (Angular CDK)

To start with virtual scroll in Angular, ensure you are updated to Angular version 7 or later <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Setup
1.  **Add Angular Material/CDK**: Run `ng add @angular/material` to quickly add the CDK to your Angular application <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  **Import `ScrollingModule`**: Import `ScrollingModule` from `@angular/cdk/scrolling` into your `AppModule` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Creating a Large Data List
For demonstration, a large array of fake data (e.g., 100 elements with names, bios, and emojis) can be generated using libraries like `faker.js` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### `cdk-virtual-scroll-viewport` Component
This component defines the context for virtual scrolling in your HTML <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. It has one required argument: `itemSize` (or height) in pixels <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

```html
<cdk-virtual-scroll-viewport itemSize="100">
  <!-- Content goes here -->
</cdk-virtual-scroll-viewport>
```

### Styling for Fixed Height Items
For optimal performance, items within a virtual scroll list should ideally have a fixed height <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   The `cdk-virtual-scroll-viewport` needs a defined height (e.g., `height: 100vh;`) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   Each item inside the viewport should have a fixed height (e.g., `height: 100px;`) matching the `itemSize` <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### `cdkVirtualFor` Directive
This structural directive replaces `ngFor` within the `cdk-virtual-scroll-viewport` context <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. It works identically to `ngFor` but leverages the virtual scrolling mechanism <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

```html
<cdk-virtual-scroll-viewport itemSize="100">
  <div *cdkVirtualFor="let person of people">
    {{ person.name }}
  </div>
</cdk-virtual-scroll-viewport>
```

### Visualizing Virtual Scroll
When the app is served, the CDK tracks which items fit into the viewport, rendering only those <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. A plain CSS animation applied to list items can demonstrate this: the animation will be re-applied every time an item is re-rendered in the DOM as the user scrolls <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This is a side effect unique to virtual scrolling, as a regular list would only apply the animation on initial page load <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Advanced Features and Public API

### `scrolledIndexChange` Event
The `cdk-virtual-scroll-viewport` component emits a custom event called `scrolledIndexChange` <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This event provides the index of the item the user has scrolled to, which is useful for implementing features like infinite scroll by determining when to fetch the next batch of items from a database <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### `cdk-virtual-scroll-viewport` Public API
The component exposes a public API that allows dynamic interaction in TypeScript code <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This includes methods to:
*   Measure the viewport <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   Get the total item list size <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Dynamically scroll to a specific element <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

To access these methods, you can use `@ViewChild` to grab the component from the DOM and strongly type it as `CdkVirtualScrollViewport` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. For example, this could be used to automatically scroll to the bottom of a chat messages list or update scroll position upon new message arrival <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## [[implementing_realtime_infinite_scroll_with_firebase_firestore | Implementing Real-time Infinite Scroll with Firestore]]

Combining virtual scroll with a backend like Firestore allows for a powerful and performant [[implementing_realtime_infinite_scroll_with_firebase_firestore | real-time infinite scroll]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Improvements over Previous Solutions
This approach improves upon traditional infinite scroll implementations in two significant ways:
1.  **Real-time Data**: Even when items are pulled in batches, they remain real-time, updating instantly if the data changes on the backend <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
2.  **Virtual Scroll Performance**: By using virtual scroll, much better performance is achieved as the user scrolls through many items <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Fetching Data in Batches
Data is pulled from the database in defined batch sizes (e.g., 20 items) <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This involves:
*   **Offset Tracking**: A `BehaviorSubject` tracks the offset, which is the last seen item from the previous batch, used to paginate the Firestore query <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. It starts with `null` for the initial query <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Listening to `scrolledIndexChange`**: When the user scrolls to the bottom of the current list, the `scrolledIndexChange` event triggers a method to fetch the next batch <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Querying Firestore**: Queries order data (e.g., by name), start after the current offset, and limit to the batch size <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. If an empty array is emitted, it indicates the end of the collection <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### Handling Real-time Updates
To keep everything real-time across multiple batches:
*   **Map Documents to Objects by ID**: Documents are mapped to an object where the key is their document ID. This allows for updating specific document data anywhere in the list based on its unique key, preventing duplicate documents if data changes between queries <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **RxJS Operators**:
    *   `mergeMap`: Used to merge new batches into the stream when the offset changes. `mergeMap` is crucial here (instead of `switchMap`) to ensure previous subscriptions are not canceled, maintaining real-time updates for all loaded batches <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
    *   `throttleTime`: Throttles the `scrolledIndexChange` event to prevent redundant backend requests <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   `scan`: Merges the current batch with existing batches, maintaining a single source of truth for all item keys and data <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **`trackBy` Function**: Using a `trackBy` function with `cdkVirtualFor` helps optimize real-time data by tracking item indices, ensuring only changed items are re-rendered <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### HTML Modifications
The `cdkVirtualFor` directive is updated to listen to `scrolledIndexChange` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The `async` pipe with an `ng-container` is used to unwrap the infinite observable into a template variable for easy looping <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

```html
<cdk-virtual-scroll-viewport itemSize="100" (scrolledIndexChange)="nextBatch($event, people[people.length - 1].name)">
  <ng-container *ngIf="(infinite | async) as people">
    <div *cdkVirtualFor="let person of people; let i = index; trackBy: trackByIndex">
      {{ i }}. {{ person.name }} - {{ person.bio }} {{ person.emoji }}
    </div>
  </ng-container>
  <div class="end-message" *ngIf="end">No items left to retrieve.</div>
</cdk-virtual-scroll-viewport>
```

### Demo and Observations
In a live demonstration, data queried from Firestore appears in alphabetical order <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Changes made to the data on the backend are reflected in the UI in real-time <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. The array size incrementally grows (e.g., 20, 40, 60 items) as the user scrolls, creating a seamless "infinite" experience where the list appears to exist all along <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Upon reaching the end of the collection, an indication is displayed to the user <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.