---
title: Creating components and implementing reactivity in Svelte 3
videoId: 043h4ugAj4c
---

From: [[fireship]] <br/> 

Svelte 3, released in the week prior to this content, offers a positive development experience by enabling solutions with less code compared to other JavaScript frameworks like [[component_composition_and_hooks_in_react | React]], Angular, and Vue [00:00:08]. This article will cover the basic concepts of Svelte, focusing on its component creation and unique approach to reactivity.

## Getting Started with Svelte 3

To initialize a Svelte 3 project, you can run `npx degit sveltejs/template` [00:00:44]. This command is equivalent to `create-react-app` or `ng new` for other frameworks [00:00:47]. After setup, navigate into the project directory, run `npm install`, and then `npm run dev` to serve the application locally, typically on `localhost:5000` [00:00:51].

Svelte uses Rollup.js for bundling code, though Webpack can also be used [00:01:02]. Svelte supports server-side rendering (SSR) and native [[using_web_components_in_modern_web_development | web components]] (custom elements) [00:01:11].

### The Svelte Compiler

A fundamental difference in [[overview_of_svelte_3_features | Svelte 3 features]] is that it operates as a compiler [00:01:25]. Unlike frameworks that require themselves to be included as a runtime dependency in the JavaScript bundle, Svelte generates all necessary code at build time [00:01:27]. This approach, also seen in Stencil.js, means the framework itself isn't shipped to the browser, resulting in smaller, optimized bundle sizes by only compiling the JavaScript that is actually needed, akin to tree-shaking [00:01:36].

## Svelte Component Structure

A typical Svelte component file (`.svelte`) consists of three main sections:
*   **Script Tag:** Contains the main JavaScript logic for the component [00:02:08].
*   **Style Tag:** All CSS styles defined here are automatically scoped to that specific component [00:02:13]. The Svelte compiler also automatically eliminates unused CSS styles from the final bundle [00:02:16].
*   **Markup (HTML):** Svelte uses its own templating syntax to add logic directly within the HTML, similar to Angular and Vue [00:02:23]. This differs from [[component_composition_and_hooks_in_react | React]]'s JSX, which embeds HTML-like syntax within JavaScript [00:02:30].

### Component Props

To define a variable that can be passed down from a parent component as a prop, use the `export` keyword in front of the variable declaration (e.g., `export let name`) [00:02:47]. Variables without the `export` keyword are private to the component [00:02:54].

For passing multiple props from a data object to a child component, Svelte allows the use of the spread syntax (`{...data}`) directly in the component declaration, making the code more concise [00:08:54].

## [[svelte_3_reactive_programming_and_syntax | Svelte 3 Reactive Programming and Syntax]]

Svelte's reactivity is based on variable assignment [00:03:00]. When a variable's value is reassigned, Svelte automatically updates the DOM where that variable is used [00:03:06].

### Computed Values

For values computed from other reactive variables, Svelte provides a unique `$: ` syntax (e.g., `$: result = ...`) [00:03:56]. This tells Svelte to recalculate the `result` variable whenever its dependencies change, ensuring the computed value is always up-to-date and reusable across the template [00:04:07].

### Two-Way Data Binding

Svelte simplifies two-way data binding on DOM elements using the `bind:` directive (e.g., `bind:value={randomVariable}`) [00:04:17]. This automatically keeps the input's value synchronized with the bound variable [00:04:26].

### Reactivity with Arrays and Objects

When working with arrays or objects, direct mutation (e.g., `array.push()`) will not trigger reactivity because the variable itself isn't reassigned [00:05:54]. To ensure reactivity, reassign the variable, often by creating a new array/object using the spread syntax (e.g., `array = [...array, newItem]`) [00:06:06].

### Conditional Rendering

Svelte uses an `{#if}` `{:else if}` `{:else}` `{/if}` block syntax directly in the template for conditional rendering [00:04:44]. This allows different parts of the template to be displayed based on logical conditions [00:04:52].

### Iterating Over Lists (`each` blocks)

To loop over arrays and display DOM elements for each item, Svelte uses an `{#each}` `{:else}` `{/each}` block syntax [00:06:17]. This provides access to both the value and index of each item [00:06:23]. These loops also work with asynchronous values, similar to Angular's async pipe [00:06:30].

### Handling Promises (`await` blocks)

Svelte offers a clean way to handle promises directly in the template using an `{#await}` `{:then}` `{:catch}` `{/await}` block [00:06:45]. This structure naturally supports loading states, successful resolution, and error handling, including automatic management of race conditions [00:06:55]. This approach is similar to Flutter's FutureBuilder [00:07:12].

## Svelte Stores for State Management

Svelte stores behave similarly to [[building_react_hooks_from_scratch | RxJS observables]] and provide an easy mechanism for sharing data across any component in the application's tree [00:07:17].

*   **Writable Stores:** You can create a writable store (e.g., `writable(defaultValue)`) [00:07:28].
    *   `set(newValue)`: Directly sets the store's value [00:07:36].
    *   `update(callback)`: Provides the current value to a callback function, which then returns the new value [00:07:38].
    *   `subscribe(callback)`: Allows listening to the store's value [00:07:48].

### Automatic Store Subscription (`$`)

A powerful feature of Svelte is the automatic subscription management for stores. By prefixing a store variable with a dollar sign (`$`), the Svelte compiler automatically subscribes to the store and manages its subscription lifecycle, preventing memory leaks [00:08:11]. This syntactic sugar also works for RxJS observables, allowing them to be unwrapped directly in the template [00:10:37].

## Component Communication: Custom Events

To pass data from a child component back up to a parent component, Svelte uses custom events [00:11:41]. An `EventDispatcher` can be used within a child component to create and dispatch custom DOM events [00:11:54]. The parent component can then listen for these custom events using an `on:` directive (e.g., `on:remove`, `on:toggle`) [00:13:54].

## [[implementing_transitions_and_animations_in_svelte_3 | Implementing Transitions and Animations in Svelte 3]]

Svelte simplifies [[creating_css_animations_based_on_react_state | CSS animations]] by providing built-in transition directives. You can import `fade` and `fly` (or other transitions) from `svelte/transition` [00:05:03]. By adding `transition:fade` or `transition:fly={{x: 200}}` to a DOM element, Svelte automatically computes and applies CSS animations when the element is added or removed from the DOM [00:05:16]. These directives allow animation logic to be directly tied to the DOM element and customized with properties [00:05:30]. There's even a specific directive for animating SVG graphics by drawing paths along shapes [00:05:43].

## Other Noteworthy Features

*   **Accessibility Warnings:** Svelte automatically warns developers about accessibility issues, such as missing `alt` attributes on images [00:10:15].
*   **Head Tag Access:** Svelte allows adding content to the document's `<head>` section using a `svelte:head` tag within components [00:09:54].
*   **CSS Class Directive:** Svelte has a `class:` directive to conditionally apply CSS classes. If the CSS class name and the boolean property toggling it share the same name, it can be made even more concise (e.g., `class:complete`) [00:12:37].

Overall, Svelte's abstractions are well-thought-out, maintaining a close relationship to vanilla JavaScript and native DOM APIs, making it a very impressive framework [00:14:24].