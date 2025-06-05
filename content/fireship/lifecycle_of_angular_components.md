---
title: Lifecycle of Angular Components
videoId: 23o0evRtrFI
---

From: [[fireship]] <br/> 

The lifecycle of an Angular component refers to the various stages it goes through from its creation to its destruction <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Understanding these stages is crucial for managing component behavior and optimizing application performance.

## Key Lifecycle Hooks

Angular components are essentially TypeScript classes <a class="yt-timestamp" data-t="01:03:13">[01:03:13]</a>. Several lifecycle hooks allow developers to tap into specific moments in a component's existence.

### Constructor

The `constructor` is the very first thing to happen in a component's lifecycle <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. In Angular, it is typically used only for dependency injection <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. Property bindings are not guaranteed to be available at this stage <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

### `ngOnInit`

`ngOnInit` is the most common lifecycle hook used by Angular developers <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. It is triggered when `change detection` first runs in the component <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This hook is where you should perform most of your component's setup, such as:
*   Fetching data from an API <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   Setting up reactive forms <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

### `ngOnDestroy`

`ngOnDestroy` is triggered when a component is about to be destroyed <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This hook is essential for performing any teardown operations, such as unsubscribing from observables to prevent memory leaks and performance issues <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

### `ngAfterViewInit`

If a component contains child views, `ngAfterViewInit` can be used to ensure that these child views are fully loaded <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### `ngDoCheck`

The `ngDoCheck` lifecycle hook allows you to determine when `change detection` is occurring <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. While not typically used for significant logic, it can be useful for debugging interactive applications, as it triggers constantly with events and asynchronous activity <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

## Change Detection

`Change detection` is a core concept in Angular <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Behind the scenes, Angular uses Zone.js to listen for events or asynchronous activity within your application <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. When such activity occurs, Angular re-renders components as needed <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

## Do Not Directly Manipulate the DOM

A crucial principle for Angular developers is to avoid direct manipulation of the Document Object Model (DOM) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. For example, using `document.querySelector` to change `innerHTML` is discouraged <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. This is because:
*   While it works in web apps where the DOM exists, it will not work for server-side rendering or native mobile apps where the DOM is absent <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   This is why libraries like jQuery are generally discouraged in Angular <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

Instead of direct DOM manipulation, Angular's `change detection` and data binding mechanisms should be leveraged. For more information on Angular components, see [[basics_of_angular_components | Basics of Angular Components]] and [[using_angular_components_and_component_architecture | Using Angular components and component architecture]].