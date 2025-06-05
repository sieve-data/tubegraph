---
title: Basics of Angular Components
videoId: 23o0evRtrFI
---

From: [[fireship]] <br/> 

Angular components are fundamental building blocks of an Angular application, acting like "LEGO pieces" that need to be properly assembled to build functionality <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This guide covers the basics of Angular components, suitable for beginners with some JavaScript and web development knowledge <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## What is a Component?

At its core, an Angular component is a controller for the user interface (UI) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Developers write components to dictate how an application is experienced by its end-users <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Component Structure

A component is primarily a TypeScript class <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It utilizes the `@Component` decorator to integrate "Angular magic," which allows for binding data from the TypeScript file to the HTML template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Creating a Component

A new component can be generated using the [[Introduction to Angular CommandLine Interface CLI | Angular CLI]] (e.g., `ng generate component home`), which creates four files <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The majority of the component's logic resides in the TypeScript file (e.g., `home.component.ts`) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Data Binding

Angular provides several ways to bind data between the component's TypeScript logic and its HTML template.

### Attribute Binding

Attribute binding allows you to bind TypeScript data to HTML attributes <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This is achieved by wrapping the HTML attribute in square brackets `[]` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. For example, `[disabled]="clicked"` binds the HTML `disabled` attribute to a `clicked` property in the TypeScript, allowing its boolean value to control the button's state <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Event Binding

Event binding enables you to react to events happening in the HTML, such as a button click <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This is done by wrapping the HTML event in parentheses `()` and passing a function defined in the TypeScript component to handle the event <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. For instance, `(click)="handleClick()"` would call the `handleClick` method when the button is clicked <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Interpolation

Interpolation involves taking a raw value from the TypeScript component and rendering it directly into the HTML <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This is done using "handlebar" syntax `{{ }}` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. For example, `{{ title }}` would display the string value of the `title` property <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Using Components

Once a component is created, it can be used within the Angular application in several ways.

### Declaring in HTML

The most basic way to use a component is by declaring its selector as an HTML element in another component's template <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For example, if a component has the selector `app-home`, it can be used as `<app-home></app-home>` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### [[Angular Router Basics | Loading with the Router]]

Components can be loaded by the [[Angular Router Basics | Angular Router]] based on a specific URL path <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This is typically configured in the router module by setting up a path and pointing it to the component <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Dynamically Loading Components

Components can also be loaded dynamically without changing the route, which is useful for pop-ups or modal windows <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Frameworks like Ionic use this for alerts and other dynamic UI elements <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### [[Using Angular components and component architecture | Angular Elements]]

A modern approach allows converting an Angular component into a regular web component using [[Using Angular components and component architecture | Angular Elements]] <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This enables the component to be used completely outside of an Angular application, even in a regular HTML page <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

## [[Angular Directives and Usage | Directives]]

A [[Angular Directives and Usage | directive]] is similar to a component but without its own HTML or CSS <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Instead, it attaches to a host HTML element and modifies its behavior <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Built-in Directives

*   **`ngIf`**: A structural [[Angular Directives and Usage | directive]] (prefixed with `*`) that controls whether elements are rendered in the DOM <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The element is only rendered if the expression assigned to `ngIf` resolves to `true` <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   **`ngFor`**: Another structural [[Angular Directives and Usage | directive]] used to loop over an array of data and render an element for each item <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. For example, `*ngFor="let item of items"` iterates through an `items` array <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **`ngClass`**: Used to conditionally apply CSS classes to an element based on logic in the TypeScript <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. It takes an object where keys are CSS class names and values are expressions that resolve to `true` or `false` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Custom Directives

Developers can also build their own custom [[Angular Directives and Usage | directives]] using the [[Introduction to Angular CommandLine Interface CLI | Angular CLI]] (`ng generate directive <name>`) <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **`@HostBinding`**: Binds a host element's property to a property in the [[Angular Directives and Usage | directive]]'s class <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **`@HostListener`**: Listens for events on the host element and executes a method in the [[Angular Directives and Usage | directive]]'s class when the event occurs <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Pipes

Pipes are mechanisms in Angular that help write reusable code by transforming data <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. A pipe is always used in an interpolated value in the HTML <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. A pipe is a function that takes an input value and returns a transformed output value <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Built-in Pipes

Angular provides several useful built-in pipes, such as the `number` pipe for formatting numbers <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### Custom Pipes

The true power of pipes comes from building custom pipes to address specific data transformation needs <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. A custom pipe implements a `transform` method <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Async Pipe

A special and highly useful pipe is the `async` pipe <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It automatically subscribes to observables or promises (commonly used for asynchronous data fetching) directly in the HTML and unwraps their values <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. Crucially, it also automatically unsubscribes when the component is destroyed, preventing memory leaks <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## Never Touch the DOM Directly

In Angular, direct manipulation of the Document Object Model (DOM) using methods like `document.querySelector` or libraries like jQuery is generally discouraged <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. While such code might work in a web app, it will fail in environments where the DOM does not exist, such as server-side rendering or native mobile apps <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Angular's data binding and [[Angular Directives and Usage | directives]] provide the necessary abstraction to handle UI updates.

## [[Lifecycle of Angular Components | Component Lifecycle]]

A component, being a class, follows a [[Lifecycle of Angular Components | lifecycle]] with specific hooks that Angular triggers at different stages.

*   **Constructor**: The very first thing that happens in a component's [[Lifecycle of Angular Components | lifecycle]] <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. It should typically only be used for injecting dependencies <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **`ngOnInit`**: The most common [[Lifecycle of Angular Components | lifecycle]] hook <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This is where initial setup logic should reside, such as fetching data from an API or setting up reactive forms <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Property bindings are guaranteed to be available when `ngOnInit` runs <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **`ngOnDestroy`**: Triggered when a component is destroyed <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This hook is used for teardown operations, like unsubscribing from observables to prevent memory leaks and performance issues <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **`ngAfterViewInit`**: Useful when a component has child views, ensuring that those child views are loaded <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   **`ngDoCheck`**: This hook is triggered constantly as part of Angular's change detection mechanism, which uses Zone.js to listen for events and asynchronous activity to re-render components <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. While not typically used for significant logic, it can be helpful for debugging <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

## [[Smart Components vs Dumb Components in Angular | Smart vs. Dumb Components]]

This concept, also known as Stateful vs. Stateless or Container vs. Presentational components, promotes separation of concerns for more predictable code <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

*   **[[Smart Components vs Dumb Components in Angular | Smart Components]] (Container)**: Generally represent pages or containers <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. They control application logic, synchronize state, and are responsible for fetching data from databases or APIs <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **[[Smart Components vs Dumb Components in Angular | Dumb Components]] (Presentational)**: Primarily concerned with presentation logic <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. They receive data (often via inputs from a smart component) and focus solely on displaying it in the UI <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. This separation makes complex applications easier to understand and manage <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.