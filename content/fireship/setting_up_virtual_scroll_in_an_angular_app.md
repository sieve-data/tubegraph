---
title: Setting up virtual scroll in an Angular app
videoId: Ppl64MY6FFc
---

From: [[fireship]] <br/> 

[[angular_7_virtual_scroll_feature_in_the_component_development_kit | Angular 7]] introduced a significant feature: the [[angular_7_virtual_scroll_feature_in_the_component_development_kit | virtual scroll behavior]] in the Component Development Kit (CDK) <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This functionality allows developers to create high-performance lists by only rendering the items currently visible to the user <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## What is Virtual Scrolling?
[[benefits_and_use_cases_of_virtual_scrolling | Virtual scrolling]] is highly beneficial when dealing with large lists of items <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Instead of rendering all items in the list, it intelligently renders only those within the user's viewport <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This approach leads to much smoother performance, as the browser only needs to process a small subset of the data <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The CDK provides components and directives that simplify the implementation of virtual scrolling <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, including tools for measuring scrolled elements, which can be used to pull data in batches from a backend database, enabling an [[optimizing_performance_with_virtual_scroll_and_firebase | infinite, real-time virtual scroll]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Setup and Installation

To begin, ensure your Angular application is updated to version 7 or newer <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

1.  **Add the Angular CDK**:
    Run the following command in your terminal:
    ```bash
    ng add @angular/material
    ```
    During the installation process, Angular 7 will present a series of questions; you can typically select the default options <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

2.  **Install AngularFire (Optional for Backend Integration)**:
    If you plan to integrate with Firebase for an infinite scroll, install AngularFire:
    ```bash
    npm install @angular/fire
    ```
    This is necessary for the backend data handling part of an [[optimizing_performance_with_virtual_scroll_and_firebase | infinite scroll implementation]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

3.  **Import `ScrollingModule`**:
    In your `app.module.ts` file, import `ScrollingModule` from `@angular/cdk/scrolling` and add it to your `imports` array <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    ```typescript
    import { ScrollingModule } from '@angular/cdk/scrolling';

    @NgModule({
      imports: [
        // ...other modules
        ScrollingModule,
        // optionally AngularFireModule for backend stuff
      ],
      // ...
    })
    export class AppModule { }
    ```

## Generating Fake Data (for demonstration)

For demonstration purposes, you'll need a large list of items. You can generate fake data using a library like `faker.js` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

In your component's TypeScript file:
1.  Install `faker.js`: `npm install faker`
2.  Import `faker` (or `faker-js/faker` if using ES modules).
3.  Create a helper function for random emojis (optional) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
4.  Generate an array of 100 elements and map each to an object with fake data (e.g., name, bio, emoji) <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

```typescript
import { Component, OnInit } from '@angular/core';
import { faker } from '@faker-js/faker'; // Or 'faker' for older versions

@Component({
  selector: 'app-my-list',
  templateUrl: './my-list.component.html',
  styleUrls: ['./my-list.component.scss']
})
export class MyListComponent implements OnInit {
  people: any[] = [];

  ngOnInit() {
    this.people = Array(100).fill(0).map(() => ({
      name: faker.person.fullName(),
      bio: faker.lorem.sentence(),
      emoji: this.getRandomEmoji()
    }));
  }

  getRandomEmoji(): string {
    const emojis = ['😀', '🤩', '🚀', '🔥', '👍'];
    return emojis[Math.floor(Math.random() * emojis.length)];
  }
}
```

## Basic Virtual Scroll Implementation

### HTML Structure
In your HTML template, wrap your list items within the `<cdk-virtual-scroll-viewport>` component <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This component requires an `itemSize` input, which represents the height of each item in pixels <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. For optimal performance with virtual scroll, items should ideally have a fixed height <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Inside the `cdk-virtual-scroll-viewport`, use the `cdkVirtualFor` structural directive (which replaces `ngFor`) to loop over your data <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

```html
<cdk-virtual-scroll-viewport itemSize="100">
  <div *cdkVirtualFor="let person of people; let i = index; trackBy: trackByIndex" class="item">
    <div class="emoji">{{ person.emoji }}</div>
    <div class="details">
      <h3>{{ i }} - {{ person.name }}</h3>
      <p>{{ person.bio }}</p>
    </div>
  </div>
</cdk-virtual-scroll-viewport>
```

### CSS Styling
Ensure your `cdk-virtual-scroll-viewport` has a defined height, and each item within it matches the `itemSize` specified in the component <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

```css
cdk-virtual-scroll-viewport {
  height: 100vh; /* Fill the entire viewport height */
  border: 1px solid #ccc;
}

.item {
  height: 100px; /* Matches the itemSize in HTML */
  display: flex;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

/* Optional: Customize the scrollbar */
cdk-virtual-scroll-viewport::-webkit-scrollbar {
  width: 10px;
  background-color: #f5f5f5;
}
cdk-virtual-scroll-viewport::-webkit-scrollbar-thumb {
  background-color: #000000;
  border-radius: 5px;
}
```

When the application is served, the CDK tracks which items are visible in the list and only renders those that fit into the viewport <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Dynamic Interaction and Events

The virtual scroll component offers useful events and a public API:

*   **`scrolledIndexChange` Event**: This custom event is emitted when the user scrolls, providing the index of the item that has been scrolled to <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This is crucial for implementing [[optimizing_performance_with_virtual_scroll_and_firebase | infinite scroll]] functionality, as it helps determine when to fetch the next batch of items from a database <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

*   **Public API Methods**: The `cdk-virtual-scroll-viewport` component provides methods to interact dynamically with the scroll functionality. These include `measureViewport` (to measure the viewport), `getDataLength` (to get the total item list size), and methods to dynamically scroll to a specific element <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

To access these methods, you'll need to get a reference to the component in your TypeScript code using `@ViewChild` and strongly type it <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

```typescript
import { Component, OnInit, ViewChild } from '@angular/core';
import { CdkVirtualScrollViewport } from '@angular/cdk/scrolling';

@Component({
  selector: 'app-my-list',
  templateUrl: './my-list.component.html',
  styleUrls: ['./my-list.component.scss']
})
export class MyListComponent implements OnInit {
  @ViewChild(CdkVirtualScrollViewport) viewport!: CdkVirtualScrollViewport;

  // ... (data generation logic)

  ngAfterViewInit() {
    // You can now access viewport methods, e.g.:
    // console.log('Viewport total item size:', this.viewport.getDataLength());
    // this.viewport.scrollToIndex(50); // Scroll to item at index 50
  }

  onScroll(event: number) {
    // Logic to handle scroll index change, e.g., for infinite scroll
    console.log('Scrolled to index:', event);
  }

  // Good practice for real-time data to track item changes
  trackByIndex(index: number, item: any): number {
    return index;
  }
}
```

The `trackByIndex` function helps Angular efficiently re-render only the items that have changed, which is especially useful for real-time data to prevent the entire list from re-rendering <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

By combining the virtual scroll features with backend data fetching, you can create a highly efficient [[optimizing_performance_with_virtual_scroll_and_firebase | infinite and real-time scrolling experience]] for users <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.