---
title: Comparison with other JavaScript frameworks
videoId: 043h4ugAj4c
---

From: [[fireship]] <br/> 

JavaScript's ever-evolving landscape means the "status quo" rarely lasts long <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While [[comparison_of_popular_javascript_frameworks_in_2021 | React]], Angular, and Vue have dominated developer mindshare, Svelte has recently gained traction with its distinct approach <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Svelte aims to empower developers to solve problems with less code <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Fundamental Differences: Compiler vs. Runtime Frameworks

Unlike many traditional frameworks, Svelte is a compiler <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This means it generates all of your application's code at *build time*, eliminating the need to include the framework itself as a hard dependency in your JavaScript bundle <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This approach is shared by [[tradeoffs_of_javascript_frameworks | Stencil.js]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

This compilation process has several advantages:
*   **Reduced Bundle Size:** Only the JavaScript from the framework that is actually needed is compiled, preventing "extra bloat" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This can lead to smaller bundle sizes or bundles optimized for the specific code used, especially with tree-shakable libraries <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **No Runtime Overhead:** Because the framework compiles away, there's no runtime interpretation of framework code, which can contribute to faster performance.

Svelte also supports server-side rendering and native web components (custom elements) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Development Experience

### Reactivity
Svelte handles reactivity based on the assignment of a variable <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. For example, to make an array or object reactive, the variable must be reassigned, often using the spread syntax, rather than just mutating the existing object <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

For computed values, Svelte uses a unique `$: ` syntax, which is valid vanilla JavaScript, to tell the compiler to recalculate a value when its dependencies change <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Templating Syntax
Svelte employs its own templating syntax for adding logic to HTML <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This approach is similar to Angular and Vue, where logic is primarily placed within the HTML <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This differs from [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | React]], which uses JSX, where HTML is written inside JavaScript <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Styling
Styles in Svelte components are automatically scoped to that component <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. A notable feature of the Svelte compiler is its ability to automatically eliminate unused CSS styles from the final CSS bundle <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Component Communication
*   **Props:** Variables can be exported from a component using the `export let` syntax to be passed down as props from a parent component <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. All props can be passed down concisely using the spread syntax <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Custom Events:** Child components can emit custom events up to their parent components using an event dispatcher, allowing data to be passed back from child to parent <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

## Unique Features

### Built-in Animations
Svelte offers directives like `fade` and `fly` from `svelte/transition` that automatically compute CSS animations based on changes in the template <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This allows animation logic to be directly tied to the DOM element being animated, with customizable properties <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. There's even a directive specifically for SVG graphics that draws paths along shapes <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Handling Asynchronous Operations (Promises)
Svelte provides a `{#await}` block syntax to handle promises directly within the template <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This allows for clear definition of loading, resolved, and error states, and automatically handles race conditions <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This approach is similar to a "future builder" in Flutter <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Stores (State Management)
Svelte stores behave similarly to [[javascript_trends_and_frameworks | RxJS]] observables and can be shared across the entire component tree <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. A key feature is the `$` prefix syntax for store values, which tells the Svelte compiler to automatically subscribe to and manage the subscription, preventing memory leaks and reducing boilerplate <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

## Similarities to Other Frameworks

While unique, Svelte shares concepts with other frameworks:
*   **Project Initialization:** `npx degit sveltejs/template` is equivalent to `create-react-app` or `ng new` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Bundling:** Svelte uses Rollup.js by default, but Webpack can also be used, similar to other frameworks <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Event Binding:** Binding to DOM events like `on:click` is common across frameworks <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Conditional Rendering:** Svelte's `{#if}` and `{:else if}` syntax is a standard pattern for conditional display <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Looping:** The `{#each}` loop syntax is used to iterate over arrays and display elements for each item <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, and also works with asynchronous values similarly to Angular's `async` pipe <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Conclusion

Svelte's abstractions are designed to be well-thought-out without taking developers too far away from vanilla JavaScript or native DOM APIs <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. As of the video's recording, the main missing feature was TypeScript support, though it was expected in the near future <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. Svelte presents a compelling alternative for developers looking to build web applications with less boilerplate and optimized performance.