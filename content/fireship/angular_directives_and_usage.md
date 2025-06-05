---
title: Angular Directives and Usage
videoId: 23o0evRtrFI
---

From: [[fireship]] <br/> 

In Angular, components are like the LEGO pieces of an application, but directives are another fundamental building block that allow for reusable code and manipulation of the DOM <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article covers the [[basics_of_angular_components|basics of Angular components]], including directives and pipes, for beginners with some JavaScript and web development knowledge <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## What is a Directive?

A directive is similar to an [[basics_of_angular_components|Angular component]] but does not have its own HTML or CSS template <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Instead, a directive attaches to a host element and modifies its behavior <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Built-in Directives

Angular provides several useful built-in directives for controlling how elements are rendered and styled in the DOM. Any directive that starts with a star (`*`) is a structural directive, meaning it controls how elements are rendered in the DOM <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### `*ngIf`

The `*ngIf` directive is a structural directive that conditionally renders an element based on whether its expression resolves to `true` or `false` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

*   **Usage**: Attach `*ngIf` to a `div` or any HTML element. The element will only render if the condition on the right-hand side is true <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   **Example**: Displaying boat data only after a button has been clicked, where the `clicked` property controls the visibility <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### `*ngFor`

The `*ngFor` directive is used to loop over an array of data and render an HTML element for each item in the array <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

*   **Usage**: Iterate over an array using the syntax `*ngFor="let item of items"` <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The element to which `*ngFor` is attached will be rendered for each item <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Example**: Displaying multiple "boat" items from an array using the same presentation logic <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### `[ngClass]`

The `[ngClass]` directive is used to conditionally apply CSS classes to an element based on logic in the component's TypeScript <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

*   **Usage**: Pass `[ngClass]` an object where the keys are the CSS class names and the values are expressions that resolve to `true` or `false` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Example**: Applying a `green` or `red` CSS class to an `h1` title based on the `boat name` property <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Custom Directives

You can also build your own custom directives in Angular <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Generating a Custom Directive

Use the [[introduction_to_angular_commandline_interface_cli|Angular CLI]] command `ng generate directive <name>` to create a new directive <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

*   A custom directive file (`.directive.ts`) will be generated. It will look similar to a component file but without an HTML template or CSS styles <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   Directives are used as attributes on HTML elements <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### Modifying Host Elements and Listening to Events

Custom directives can interact with their host HTML elements using decorators:

*   **`@HostBinding`**: This decorator allows you to bind a property of the directive to a property of the host element <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   **Example**: Binding to the `width` property of an image element to set its initial width <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **`@HostListener`**: This decorator allows you to listen for events on the host element and define functions to handle them <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   **Example**: Listening for the `mouseenter` event to increase the width of an image when a user hovers over it <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

Custom directives, along with components, help in writing dry and reusable code <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

## Pipes

Pipes are another mechanism in Angular for writing reusable code, primarily for transforming data for display in the HTML <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. A pipe is used in an interpolated value within the HTML template <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Built-in Pipes

Angular includes several useful built-in pipes.
*   **Example**: The `number` pipe can be used to format numbers, such as rounding to a specific number of decimal places <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### Custom Pipes

The real power of pipes comes from building custom ones <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Definition**: A pipe is essentially a function that takes an input value and "spits out" another transformed value <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Implementation**: Custom pipes implement a `transform` method. The `value` parameter represents the input, and the returned value is what will be displayed in the HTML <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Example**: Creating a custom pipe to display only the last two digits of a four-digit year <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

### Async Pipe

The `async` pipe is a special pipe commonly used in web applications to automatically handle asynchronous data fetching, such as promises or observables <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

*   **Functionality**: It automatically subscribes to an observable and converts it to an array, and importantly, it also unsubscribes when the [[lifecycle_of_angular_components|component is destroyed]] to prevent memory leaks <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Benefit**: Simplifies Angular code by allowing asynchronous data to be treated more like a synchronous JavaScript array directly in the HTML <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Example**: Using the `async` pipe with `*ngFor` to loop over an observable of boats <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.