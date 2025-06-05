---
title: Using Svelt for front end development
videoId: J5x3OMXjgMc
---

From: [[fireship]] <br/> 

Svelte is a [[javascript_and_frontend_development | JavaScript]] library utilized for building the [[front_end_and_back_end_development | front end]] user interface (UI) of web applications <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. A notable characteristic of Svelte is that it is not sponsored by large technology companies <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

In the context of a decentralized chat application, Svelte is used to manage both user authentication and a group chat room <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Core Concepts and Features

### Stores for Reactivity
Svelte provides "stores" (importable from `svelte/store`) which function as observable values <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. These stores enable the UI to re-render automatically whenever their values change <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. They can also be shared across multiple components, facilitating [[creating_components_and_implementing_reactivity_in_svelte_3 | reactivity]] and state management <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For instance, a `username` store can be created to reactively update the UI when the current user's alias changes or when the authentication state changes (e.g., sign in/out) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Svelte Syntax for Stores
Svelte offers a unique syntax for interacting with stores:
*   **Dollar Sign Syntax (`$`)**: By prepending a store's name with a dollar sign (e.g., `$username`), Svelte components can subscribe to the store and automatically react to any changes <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This allows for conditional rendering based on store values (e.g., `{#if $username}` to show content only when a user is logged in) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>, and direct display of store values (e.g., `{$username}`) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This is a key part of [[svelte_3_reactive_programming_and_syntax | Svelte 3 reactive programming and syntax]].

### Two-Way Data Binding
Svelte simplifies two-way data binding using the `bind:value` directive on form inputs <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. When a user types into an input field bound with `bind:value`, the associated variable's value automatically updates <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Lifecycle Hooks
The `onMount` lifecycle hook in Svelte allows code to be executed when a component is first initialized <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This is useful for tasks like querying data from a database when a component loads <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### Looping Over Arrays
Svelte uses an `{#each}` block to iterate over arrays and render components or HTML elements for each item <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. Providing a unique key (e.g., `(message.when)`) within the parentheses helps Svelte efficiently sort and update messages <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.