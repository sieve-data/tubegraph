---
title: Binding Properties and Events in Angular
videoId: 23o0evRtrFI
---

From: [[fireship]] <br/> 

[[basics_of_angular_components | Angular components]] are the fundamental building blocks of an Angular application, acting as "LEGO pieces" that need to be correctly assembled to build an application <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. At its core, an Angular component is a controller for the user interface <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Developers write components to control the end-user experience of an application <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

An Angular component is essentially a TypeScript class that utilizes the `@Component` decorator to incorporate Angular functionality <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This decorator is crucial as it enables the binding of data from the TypeScript file to the HTML template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. When a new component is generated using the Angular CLI, it typically creates four files, with most of the logic residing in the TypeScript file (e.g., `home.component.ts`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Data Binding

Angular offers several ways to bind data between the component's TypeScript logic and its HTML template.

### Property Binding
Property binding allows you to bind data from your TypeScript code to HTML attributes <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This is achieved by wrapping the HTML attribute in square brackets `[]` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

For example, to disable a button based on a TypeScript property:
1.  Define a property in your component's TypeScript class, e.g., `clicked: boolean = false;` <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  Bind this property to the `disabled` attribute in your HTML: `<button [disabled]="clicked">Click Me</button>` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

If `clicked` is `false`, the button is clickable <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. If `clicked` is `true`, the button becomes disabled and unclickable <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Event Binding
Event binding allows you to respond to events that occur in the HTML, such as a button click <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This is done by wrapping the HTML event in parentheses `()` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

For instance, to change a property when a button is clicked:
1.  Define an event handler method in your component's TypeScript class, e.g., `handleClick() { this.clicked = true; }` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Bind this method to the `click` event on the button: `<button (click)="handleClick()">Click Me</button>` <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

When the button is clicked, the `handleClick` method fires, setting the `clicked` property to `true`, which then disables the button via property binding <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Interpolation
Interpolation is used to display raw values from your TypeScript code directly into the HTML <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This is achieved using the double curly brace or "handlebar" syntax `{{}}` <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

Example:
1.  Define a string property in TypeScript, e.g., `title = 'Angular 6 Project';` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
2.  Display it in HTML: `<h1>{{ title }}</h1>` <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

This will render `<h1>Angular 6 Project</h1>` in the browser <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Using Components

Once a component is created, it can be used within an Angular application in several ways:
*   **Declaring with its selector**: The most basic method is to declare the component using its selector (e.g., `<app-home>`) directly in another component's HTML template <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Router Outlet**: Components can be loaded dynamically based on a specific URL path using the Angular router, appearing where a `<router-outlet>` is defined <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Dynamic Loading**: Components can be loaded dynamically without changing the route, often used for pop-up or modal windows, a technique frequently seen in frameworks like Ionic <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Angular Elements**: Components can be converted into standard web components using Angular Elements, allowing them to be used outside of Angular, even dropped into a regular HTML page <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## [[angular_directives_and_usage | Angular Directives]]

A [[angular_directives_and_usage | directive]] is similar to a component but without its own HTML or CSS <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Instead, it attaches to a host element and modifies its behavior <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Built-in Directives
Angular provides several useful built-in [[angular_directives_and_usage | directives]]:
*   **`*ngIf`**: A structural directive that controls how elements are rendered in the DOM, only rendering an element if its condition resolves to `true` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **`*ngFor`**: Used to loop over an array of data and render an element for each item in the array <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **`[ngClass]`**: Used to conditionally apply CSS classes to an element based on TypeScript logic <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. It takes an object where keys are CSS class names and values are expressions resolving to `true` or `false` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

### Custom Directives
You can also build your own custom [[angular_directives_and_usage | directives]] <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. A custom [[angular_directives_and_usage | directive]] is generated via the CLI (e.g., `ng generate directive magnifier`) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Key differences from a component include the absence of an HTML template or CSS styles; instead, it's used as an attribute on an HTML element <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

*   **`@HostBinding`**: Used to bind to properties of the host element <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **`@HostListener`**: Used to listen to DOM events on the host element and define a function to handle them <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

This allows for writing reusable code by combining components and [[angular_directives_and_usage | directives]] <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

## Pipes

Pipes are mechanisms in Angular that help write reusable code by transforming displayed values in the HTML <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. A pipe is always used in an interpolated value within the HTML <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

*   **Built-in Pipes**: Angular has useful built-in pipes, such as the `number` pipe for rounding numbers <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Custom Pipes**: The real power of pipes comes from building custom pipes <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. A pipe is a simple function that takes an input value and returns a transformed output value <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Custom pipes implement a `transform` method where the transformation logic resides <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Async Pipe**: A special and very useful pipe is the `async` pipe <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It automatically handles asynchronous data streams like Promises or Observables directly in the HTML <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. It subscribes to the observable and automatically unsubscribes when the component is destroyed, preventing memory leaks <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. This simplifies handling asynchronous data, allowing it to be treated more like a synchronous [[javascript_objects_and_their_properties | JavaScript array]] <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Avoiding Direct DOM Manipulation

In Angular, it's generally discouraged to directly manipulate the DOM using methods like `document.querySelector()` to change `innerHTML` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. While this might work in a web app, such code will not function if you aim for server-side rendering or building a native mobile app, because the DOM does not exist on those platforms <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. This is why libraries like jQuery are generally discouraged in Angular <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## [[lifecycle_of_angular_components | Component Lifecycle]]

A component's [[lifecycle_of_angular_components | lifecycle]] refers to the sequence of events that occur from its creation to its destruction <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

*   **Constructor**: The very first thing to happen is the constructor firing <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. In Angular, it's typically used only for injecting dependencies <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **`ngOnInit`**: This is the most common [[lifecycle_of_angular_components | lifecycle hook]] you'll use <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. It's guaranteed that property bindings are available when `ngOnInit` runs, as it's the first time change detection runs in the component <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. It's the primary place for setup logic, such as fetching data from an API or setting up an [[introduction_to_reactive_forms_in_angular | Angular reactive form]] <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **`ngOnDestroy`**: Triggered when a component is destroyed <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This hook is used for teardown operations, commonly unsubscribing from observables to prevent memory leaks and performance issues <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **`ngAfterViewInit`**: Ensures that child views inside your component are loaded <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   **`ngDoCheck`**: This [[lifecycle_of_angular_components | hook]] is triggered constantly in an interactive app and can be useful for debugging to observe when change detection is happening <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. Angular uses Zone.js to listen for events or asynchronous activity and re-render components as needed, triggering change detection <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

## [[smart_components_vs_dumb_components_in_angular | Smart Components vs. Dumb Components]]

A common concept in Angular and other [[javascript_objects_and_their_properties | JavaScript]] frameworks is the distinction between [[smart_components_vs_dumb_components_in_angular | smart components and dumb components]] (also known as stateful vs. stateless, or container vs. presentational components) <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This promotes a separation of concerns, making code more predictable <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

*   **[[smart_components_vs_dumb_components_in_angular | Smart Component]] (Container)**: Typically a page or container component that controls how things work throughout the application, handling low-level concerns like synchronizing app state and fetching data <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **[[smart_components_vs_dumb_components_in_angular | Dumb Component]] (Presentational)**: Primarily concerned with presentation logic, focusing solely on how to display data in the UI <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

This architectural pattern makes it easier to understand and manage complexity as an application grows <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.