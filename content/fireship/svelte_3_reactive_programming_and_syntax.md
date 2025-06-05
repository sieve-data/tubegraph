---
title: Svelte 3 reactive programming and syntax
videoId: 043h4ugAj4c
---

From: [[fireship]] <br/> 

[[overview_of_svelte_3_features | Svelte 3]], released in the week prior to this content's creation, distinguishes itself by empowering developers to solve problems with less code compared to other JavaScript frameworks <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It is a compiler-based framework that handles reactivity and component logic in a unique way <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Getting Started with Svelte 3

To begin a new [[using_svelt_for_front_end_development | Svelte]] project, you can use the command `npx degit sveltejs/template` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This is analogous to `create react app` or `ng new` in other frameworks <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. After initialization, run `npm install` to install dependencies and `npm dev` to serve the application locally, typically at `localhost:5000` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Compiler Advantages

[[understanding_the_unique_features_of_frameworks_like_svelte_lit_and_alpine_js | Svelte]] primarily uses Rollup for bundling, an alternative to Webpack, though Webpack can also be used <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. A key difference with [[understanding_the_unique_features_of_frameworks_like_svelte_lit_and_alpine_js | Svelte]] is its compiler nature <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. It generates all code at build time, eliminating the need to include the framework itself as a hard dependency in the JavaScript bundle <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This approach, similar to Stencil.js, results in smaller bundle sizes as only the necessary framework JavaScript is compiled, avoiding extra bloat <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Svelte also supports server-side rendering and native web components (custom elements) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Svelte Component Structure and Reactivity

[[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] components are defined in `.svelte` files, which contain three main sections:
*   **Script (`<script>` tag)**: Houses the main JavaScript logic <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Style (`<style>` tag)**: Contains CSS styles that are automatically scoped to the component <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The compiler also eliminates unused CSS from the bundle <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Markup**: Uses [[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte's]] own templating syntax to add logic to HTML, differing from React's JSX by embedding logic directly in the HTML <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Variables and Props

Variables declared within a component's script section are private unless the `export` keyword is used <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Variables prefixed with `export let` can be passed down as props from a parent component <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Core Reactivity

[[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte's]] reactivity is based on variable assignment <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. When a variable is reassigned, the component automatically updates the DOM <a class="yt=" data-t="00:03:06">[00:03:06]</a>.

For reactive values, expressions can be written directly in the template, and [[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] will re-run the logic when the reactive value changes <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Computed Values

[[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] provides a special syntax for computed values using `$:` (dollar sign colon) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This valid vanilla JavaScript syntax tells Svelte to recalculate the value when the app reacts to changes in its dependencies <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. This allows for reusable computed properties <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

```svelte
<script>
  let random = 0;
  function randomize() {
    random = Math.random();
  }

  $: result = random > 0.5 ? 'Winner' : 'Loser';
</script>

<button on:click={randomize}>Randomize</button>
<p>Result: {result}</p>
```
<a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a> <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>

### Two-Way Data Binding

[[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] simplifies two-way data binding using the `bind:` directive. For example, to bind an input's value:

```svelte
<input type="number" bind:value={random} />
```
<a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

### Conditional Rendering

Templates can be rendered conditionally using `{#if}` blocks, similar to Angular and Vue:

```svelte
{#if computedValue > 50}
  <p>Greater than 50!</p>
{:else if computedValue > 20}
  <p>Greater than 20 but not 50!</p>
{:else}
  <p>20 or less.</p>
{/if}
```
<a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>

### Handling Arrays and Objects

When working with arrays or objects, direct mutation (e.g., `array.push()`) will not trigger reactivity because it doesn't reassign the variable <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. To ensure reactivity, the variable must be reassigned, often using the [[spread_syntax_in_javascript | spread syntax]]:

```svelte
<script>
  let items = ['item 1'];
  function addItem() {
    items = [...items, 'new item']; // Reassigns the array to trigger reactivity
  }
</script>
<button on:click={addItem}>Add Item</button>
```
<a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a> <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>

### List Rendering

To loop over arrays and display DOM elements for each item, [[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] uses the `{#each}` block, which provides access to both the value and index of each item <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This also works with asynchronous values <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

```svelte
<ul>
  {#each items as item, i}
    <li>{i}: {item}</li>
  {/each}
</ul>
```
<a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>

### Asynchronous Operations (Promises)

[[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] provides a readable and intuitive way to handle promises directly in the template using the `{#await}` block. It automatically manages loading states, success, and error handling, including race conditions <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

```svelte
<script>
  async function fetchRandom() {
    await new Promise(resolve => setTimeout(resolve, 1000));
    if (Math.random() > 0.5) {
      throw new Error('Failed to fetch!');
    }
    return Math.floor(Math.random() * 100);
  }

  let randomNumberPromise = fetchRandom();
</script>

{#await randomNumberPromise}
  <p>Loading...</p>
{:then value}
  <p>Value: {value}</p>
{:catch error}
  <p style="color: red;">Error: {error.message}</p>
{/await}
```
<a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>

### Svelte Stores

[[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] stores behave similarly to [[functional_programming_with_typescript | RxJS]] observables, allowing for easy data sharing anywhere in the component tree <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

A writable store can be created, similar to a Behavior Subject in [[functional_programming_with_typescript | RxJS]], with methods like `set` and `update` to modify its value <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

```javascript
// store.js
import { writable } from 'svelte/store';
export const randomStore = writable(0);
```

To consume a store value in a component, a special `$` (dollar sign) prefix can be used, which tells the compiler to automatically subscribe and manage the subscription, preventing memory leaks:

```svelte
<script>
  import { randomStore } from './store.js';
</script>

<p>Store value: {$randomStore}</p>
<button on:click={() => randomStore.update(n => n + 1)}>Increment Store</button>
```
<a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>

This syntactic sugar also works for [[functional_programming_with_typescript | RxJS]] observables, allowing them to be unwrapped directly in the template <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Passing All Props

When passing multiple properties from a data object to a child component, [[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] allows the use of the [[spread_syntax_in_javascript | spread syntax]] for a more concise syntax:

```svelte
<script>
  import Child from './Child.svelte';
  let data = { propA: 'Hello', propB: 123, propC: true };
</script>

<Child {...data} />
```
<a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>

### Custom Events

Child components can emit custom events up to their parent using an event dispatcher. This is useful for communicating actions or data back to the parent <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

```svelte
<!-- Child.svelte -->
<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  function removeItem(id) {
    dispatch('remove', { id });
  }
</script>

<button on:click={() => removeItem(itemId)}>Remove</button>
```

```svelte
<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
  function handleRemove(event) {
    console.log('Remove item with ID:', event.detail.id);
  }
</script>

<Child on:remove={handleRemove} />
```
<a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>

### CSS Classes

Classes can be conditionally applied using the `class:` directive. If the CSS class name is the same as the boolean property toggling it, a concise shorthand can be used:

```svelte
<li class:complete={isComplete}> <!-- isComplete is a boolean property -->
<li class:complete> <!-- Shorthand if property is named 'complete' -->
```
<a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a> <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>

## Conclusion

[[overview_of_svelte_3_features | Svelte 3]] is praised for its well-thought-out abstractions that remain close to vanilla JavaScript and native DOM APIs <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. The primary missing feature identified at the time of recording was TypeScript support, which was expected in the near future <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.