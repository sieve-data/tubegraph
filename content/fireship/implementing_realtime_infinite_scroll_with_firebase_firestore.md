---
title: Implementing realtime infinite scroll with Firebase Firestore
videoId: Ppl64MY6FFc
---

From: [[fireship]] <br/> 

Implementing a real-time infinite scroll with [[building_social_media_style_feeds_with_firestore | Firebase Firestore]] using Angular's virtual scroll capabilities allows for high-performance display of large datasets while providing immediate updates as data changes in the backend <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This approach ensures a smooth user experience by only rendering visible items and fetching data in efficient batches <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Virtual Scroll Basics

Virtual scrolling is a technique beneficial for displaying large lists of items by only rendering the subset visible within the user's viewport <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a> <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This significantly improves performance compared to rendering the entire list at once <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Setup and Prerequisites

To get started, ensure you have:
*   **Angular Version 7** or higher <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a> <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Angular Material's Component Development Kit (CDK)**: Add it to your app by running `ng add @angular/material` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. When prompted, you can select the default options <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **AngularFire**: Install it if you plan to integrate with [[using_firebase_databases_and_data_modeling_techniques | Firebase]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Import `ScrollingModule`**: In your `app.module.ts`, import `ScrollingModule` from `@angular/cdk/scrolling` and add it to your `imports` array <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Generating Data

For demonstration, a large list of fake data is useful <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a> <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. You can use libraries like `faker.js` to generate fake names and email addresses <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
For example, you can create an array of 100 elements, mapping each to an object with a name, bio, and emoji <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a> <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Implementing Virtual Scroll with `cdkVirtualFor`

The `cdk-virtual-scroll-viewport` component provides the context for virtual scrolling <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **`cdkVirtualScrollViewport`**: This component requires an `itemSize` argument, representing the fixed height of each item in pixels <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Items in a virtual scroll should ideally have a fixed height <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **CSS Styling**:
    *   Ensure your `cdk-virtual-scroll-viewport` has a defined height (e.g., `100vh` to fill the viewport) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a> <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Each item inside the viewport should have a fixed height matching the `itemSize` (e.g., 100 pixels) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
    *   You can customize the scrollbar appearance using pseudo-selectors like `::-webkit-scrollbar` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **`cdkVirtualFor`**: This structural directive replaces `ngFor` and works similarly, but it's optimized for virtualized lists <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a> <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The CDK tracks which items fit into the viewport and re-renders them as needed <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This re-rendering can be observed if you apply CSS animations, as they will re-apply each time an item becomes visible <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Virtual Scroll Public API

The `cdk-virtual-scroll-viewport` component provides a public API for programmatic interaction:
*   **`scrolledIndexChange` event**: Emits the index of the item the user has scrolled to <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This is crucial for implementing infinite scroll <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Methods**: It includes methods to `measureViewport`, `getDataLength` (get total items in the list), or `scrollToOffset` (dynamically scroll to a specific element) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a> <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Accessing with `ViewChild`**: To use these methods, access the component from the DOM using `@ViewChild` and strongly type it as `CdkVirtualScrollViewport` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This allows you to interact with the component dynamically in your TypeScript code, for example, to scroll to the bottom of a chat or update scroll position for new messages <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a> <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Real-time Infinite Scroll with Firebase Firestore

This solution builds upon previous infinite scroll methods by adding real-time updates and leveraging virtual scroll for superior performance <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a> <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Component Logic

1.  **Imports**: Import `AngularFirestore` and various RxJS operators <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
2.  **Properties**:
    *   `batchSize`: Defines the number of items fetched per batch (e.g., 20) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   `viewport`: A `ViewChild` reference to `CdkVirtualScrollViewport` <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
    *   `finished`: A boolean to track if the end of the list has been reached <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   `offset`: A `BehaviorSubject` (initialized with `null`) that stores the last item's value from the previous batch, used for [[working_with_firebase_firestore_and_realtime_updates | Firestore]] queries <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a> <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
3.  **`nextBatch(event, lastItem)` Method**:
    *   Listens to the `scrolledIndexChange` event <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    *   If `finished` is true, it returns, preventing further data fetches <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
    *   Compares `viewport.getRenderedRange().end` with `viewport.getDataLength()` to determine if the user has scrolled to the end of the currently rendered list <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   If at the end, it emits the `lastItem`'s identifier (e.g., name) to the `offset` BehaviorSubject, triggering a new batch query <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a> <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
4.  **`trackBy` Function**: A `trackBy` function (e.g., tracking item index) is essential for [[optimizing_performance_with_virtual_scroll_and_firebase | optimizing performance]] with real-time data, preventing the entire list from re-rendering when a single item changes <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a> <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

### Firestore Query Logic (`getBatch` Method)

This method fetches a single batch of data from [[data_modeling_in_firestore_chat_applications | Firestore]]:
1.  **Paginated Query**:
    *   Orders the collection by a specific field (e.g., user name) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   Uses `startAfter(offsetValue)` to paginate results; `offsetValue` is `null` for the first batch or the last item's value from the previous batch <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a> <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   Limits the query to `batchSize` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
2.  **Snapshot Changes**: Calls `snapshotChanges()` to get document snapshots as an observable, which will update in real-time <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a> <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
3.  **End of Collection**: If the observable emits an empty array, it indicates the end of the collection, and the `finished` property is set to `true` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a> <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
4.  **Mapping to Document ID**: To handle real-time updates across multiple batches reliably and prevent duplicate documents, map the array of documents to an object where the key is their `document ID` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a> <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This allows updating data by its unique key regardless of its index position <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### Combining Batches and Real-time Updates

1.  **`source` Observable**: In the constructor, define a `source` observable that listens to the `offset` value <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
2.  **`mergeMap` and Throttling**:
    *   Use `mergeMap` (crucially, *not* `switchMap`, which would cancel previous subscriptions) to merge new batches into the stream whenever the `offset` changes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a> <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. `mergeMap` ensures all previous batches remain real-time <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
    *   Throttle the requests (e.g., by 500 milliseconds) to prevent redundant backend calls when scrolling <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a> <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
3.  **`scan` Operator**: Pipe the stream through the `scan` operator, which merges the current batch with existing batches into the `batchMap` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. This `batchMap` (keyed by document ID) becomes the main source of truth <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
4.  **`infinite` Observable**: Finally, create an `infinite` observable by mapping the `batchMap` to its `Object.values()`, yielding an array of objects suitable for looping in the front-end <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a> <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### HTML Modifications

1.  **`cdkVirtualFor`**: Use `cdkVirtualFor` with `let i = index` to display the index and include the `trackBy` function <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a> <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
2.  **`scrolledIndexChange` Event**: Bind to the `(scrolledIndexChange)` event and call `nextBatch`, passing the event (`$event`) and the `name` of the last item in the current array as the offset value <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a> <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
3.  **Unwrapping Observable with `async` pipe**: Unwrap the `infinite` observable using `ng-container` and the `async` pipe. Assign the resulting array to a template variable (e.g., `as people`) for use in the HTML <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a> <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

### Key Considerations

*   **Real-time Updates**: Changes made directly in the [[using_firebase_databases_and_data_modeling_techniques | Firebase]] console will be reflected in the UI in real-time <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a> <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Item Position and Deletion**: The actual position of an item will not change, and if an item is deleted from the backend, it will not automatically be removed from the list with this implementation <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a> <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Additional code would be required for such functionality <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Performance**: From the user's perspective, the list appears to exist all along, despite data being fetched in batches (e.g., 20, then 40, then 60 items) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a> <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **End of List Indication**: Implement a visual cue for the user when the end of the data collection is reached <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a> <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.