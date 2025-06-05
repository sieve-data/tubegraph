---
title: Overview of Svelte 3 features
videoId: 043h4ugAj4c
---

From: [[fireship]] <br/> 

Svelte 3, released in the week prior to the video's creation, has gained positive reception due to its ability to empower developers to solve problems with less code <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Getting Started

To initialize a Svelte project, one can use `npx degit sveltejs/template`, which is comparable to `create-react-app` or `ng new` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. After creation, navigate into the project directory, run `npm install`, and then `npm run dev` to serve the application locally <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The project uses `rollup.config.js` for bundling, an alternative to Webpack, though Webpack can also be used <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Fundamental Differences

Svelte stands apart from other JavaScript frameworks like React, Angular, and Vue due to its unique approach as a compiler <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

*   **Compiler-based**: Svelte generates all code at build time, eliminating the need to include the framework itself as a hard dependency in the final JavaScript bundle <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This means no extra "bloat" in the bundle, as only the necessary framework JavaScript is compiled <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Smaller Bundle Sizes**: This approach typically results in smaller bundle sizes optimized for the code actually used, especially with tree-shakable libraries <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **Server-Side Rendering (SSR)**: Svelte supports server-side rendering <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Native Web Components**: It also supports native web components, also known as custom elements <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Component Structure

A Svelte component typically consists of three main parts:

*   **Script Tag**: Contains the main JavaScript logic <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Style Tag**: All styles defined within this tag are scoped to the specific component <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The compiler automatically eliminates unused CSS styles from the CSS bundle <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Markup**: The HTML structure of the component <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## [[svelte_3_reactive_programming_and_syntax | Svelte 3 Reactive Programming and Syntax]]

Svelte handles reactivity based on the assignment of a variable <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

*   **Props**: Variables defined with the `export let` keyword can be passed down from a parent component <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Variables without `export` are private to the component <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Event Binding**: Events in the DOM can be bound using the `on:` directive, e.g., `on:click` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Computed Values**: Svelte provides a unique `$:` syntax for defining computed values <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This tells Svelte to recalculate the value when any reactive dependency changes <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Two-Way Data Binding**: The `bind:` directive allows for two-way data binding to attributes on DOM elements, such as the `value` attribute on a form input <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Array and Object Reactivity**: For arrays or objects, direct mutation (e.g., `array.push()`) does not trigger reactivity <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. To ensure reactivity, reassign the variable, often using the spread syntax (e.g., `myArray = [...myArray, newItem]`) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Templating and Control Flow

Svelte employs its own templating syntax for adding logic to HTML, similar to Angular and Vue, differing from React's JSX <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

*   **Conditional Logic**: Templates can be displayed conditionally using `{#if}` blocks, along with `{:else if}` and `{:else}` for multiple conditions or default values <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Loops**: The `{#each}` block is used to loop over arrays, providing access to both the value and index of each item <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. `{#each}` loops also work with asynchronous values <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Asynchronous Handling**: Promises can be awaited directly in the template using the `{#await}` block, which handles loading states, successful resolution, and errors automatically <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. It also manages race conditions <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

## Advanced Features

*   **[[implementing_transitions_and_animations_in_svelte_3 | Transitions and Animations]]**: Svelte provides directives like `transition:fade` and `transition:fly` that automatically compute CSS animations when elements are added or removed from the DOM <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. These directives can be customized with properties <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. There are also specific directives for SVG graphics to draw paths along shapes <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **[[svelte_3_reactive_programming_and_syntax | Svelte Stores]]**: Stores behave similarly to RxJS observables and can be shared across the component tree for easy data sharing <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Writable Stores**: Can be created and their values set directly or updated via a callback function <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   **Automatic Subscriptions**: By prefixing a store variable with a `$` (e.g., `$storeValue`), the Svelte compiler automatically subscribes to the store and manages the subscription, preventing memory leaks <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This `$` syntax also works with RxJS observables <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   **[[creating_components_and_implementing_reactivity_in_svelte_3 | Event Dispatcher]]**: A mechanism to create and dispatch custom events from a child component to its parent, allowing data to be passed upwards <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
*   **Prop Passing Syntax**: Besides passing props one by one, Svelte allows sending all props from a data object down to a child component using the spread syntax (`{...data}`) <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Class Directive**: A built-in `class:` directive simplifies conditional CSS class application, especially when the CSS class name and the property name are the same <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **`svelte:head`**: Allows adding elements to the document's `<head>` tag directly within a Svelte component <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   **Accessibility Warnings**: Svelte automatically warns developers about accessibility issues, such as missing `alt` attributes on images <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

## Overall Impression

Svelte is highly regarded for its well-thought-out abstractions, which remain close to vanilla JavaScript and native DOM APIs, reducing boilerplate <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. At the time of the video, [[new_javascript_features_in_2020 | TypeScript]] support was identified as a missing feature, with expectations for it to be added in the near future <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.