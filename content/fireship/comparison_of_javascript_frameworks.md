---
title: Comparison of JavaScript frameworks
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 

When choosing a [[choosing_the_right_javascript_framework_for_your_project | JavaScript framework]] for a project, developers face a difficult decision due to the variety of options available and their varying strengths <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. There is no single "best" framework; the ideal choice depends on individual preference and project needs <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The most effective way to determine suitability is to build applications with different frameworks <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

This article explores various [[frontend_ui_libraries_and_frameworks | frontend UI libraries and frameworks]] by comparing how a basic to-do application is built with each, highlighting their unique features and trade-offs <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Vanilla JavaScript

While some argue against the necessity of a [[javascript_for_interactivity_and_frameworks | JavaScript framework]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, attempting to build a non-trivial application solely with vanilla JavaScript can lead to significant challenges <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Developers often end up creating their own makeshift framework, which can be inefficient <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

A fundamental difference between frameworks and vanilla JavaScript is the automatic binding of HTML to JavaScript <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. In vanilla JavaScript, developers must imperatively select and manipulate HTML elements from the DOM <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### To-Do App Implementation in Vanilla JS

A to-do application requires managing state, data binding, events, and the application lifecycle <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

*   **HTML Structure**: An unordered list for to-dos and a form with an input and submit button are used <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **DOM Manipulation**: HTML elements are manually selected using `document.querySelector` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **State Management**: An empty array tracks to-do items <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **UI Updates**: Manually create new list item elements, update their `innerHTML`, and append them to the unordered list <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Data and UI are completely decoupled, making synchronization difficult <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Event Handling**: An event listener is registered on the form's `submit` event, calling `preventDefault` to stop page refresh <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. It's difficult to tell from HTML alone that an event listener is attached without examining the JavaScript <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Lifecycle**: On initialization, existing to-do items are retrieved from local storage and rendered <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

Vanilla JavaScript code does not scale well for complexity, requiring manual implementation of features like routing or animation <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This is why most developers opt for frameworks <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Key JavaScript Frameworks

### React

React is often considered the most popular framework <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, though sometimes referred to as a library <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. It drives project development, requiring adherence to the "React way" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Developed by Facebook for complex UIs, React is minimal by design <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. It relies on its open-source community for features like routing and state management <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. React is unopinionated about code organization, giving developers freedom but requiring many decisions <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

*   **Popularity**: Over 10 million weekly npm downloads and over 170,000 GitHub stars <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Its popularity makes it a valuable skill for employment and collaboration <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **CLI/Build Tools**: Uses `create-react-app` for new projects <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, though alternatives like Next.js or Gatsby are common <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Webpack bundles code <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Components**: Applications are organized as a tree of components that encapsulate UI parts and communicate <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This enables declarative UI where data dictates the rendered output <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Components are often simple JavaScript functions <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **JSX**: The return value of a component function is JSX, an HTML-like syntax extended to insert JavaScript directly into HTML <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **State Management**: `useState` hook defines reactive state, re-rendering the UI when updated <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Event Handling**: Events can be bound directly to forms using `onSubmit` <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. `useRef` is used to get form input values <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. HTML is more descriptive, showing data and event bindings <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Lifecycle Hooks**: `useEffect` handles component lifecycle, such as loading data from local storage on initialization <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. However, `useEffect` can be confusing for beginners due to its dependency array <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Angular

Angular, maintained by Google, is highly opinionated about project organization and structure <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. It includes official libraries for routing, animation, and server-side rendering <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Its convention-driven structure ensures consistency across projects and provides robust tooling <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Angular mandates the use of TypeScript <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

*   **Popularity**: 75,000 GitHub stars and is the second most downloaded framework on npm <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Google uses it internally for hundreds of web apps <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **CLI/Build Tools**: The `ng new` command creates a large, pre-configured TypeScript project <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Angular's CLI is considered the most powerful among frameworks <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, allowing component generation <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Components**: Components are TypeScript classes with a `@Component` decorator <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Most Angular apps separate components into three files: TypeScript, HTML, and CSS <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **State Management**: Reactive state is defined as properties on the component class <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, with methods on the class to update it <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Templating**: Angular extends HTML with a special templating language, using directives like `*ngFor` to loop over arrays <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Unlike React, which integrates HTML into JavaScript, Angular integrates JavaScript into HTML <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Event Handling**: Binds to events like `submit` to run component methods <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Two-way data binding uses the `ngModel` directive <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>, requiring the `FormsModule` import <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Lifecycle Hooks**: Manages component lifecycle using methods like `ngOnInit`, called on initialization <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Learning Curve**: Angular has a higher learning curve due to its strong opinions and module requirements <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Its structured approach makes it popular for enterprise applications <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Vue.js

Vue.js, independently developed by Evan You, offers a similar feel to Angular but is more approachable for independent developers <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. It provides official packages for routing and state management and has a large ecosystem of third-party packages <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

*   **Popularity**: Has the most GitHub stars (187,000) and is nearly tied with Angular for second place in npm downloads <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **CLI/Build Tools**: Features a powerful CLI, including a GUI (`vue ui`) that walks developers through dependency and feature selection during app generation <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. While powerful, it doesn't generate components like Angular's CLI <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Projects have a simplified structure, allowing plugins for functionality to be added as needed <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Components**: Components are defined in `.vue` files and organized into three parts: `<template>`, `<script>`, and `<style>` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Components are represented as plain JavaScript objects <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **State Management**: Reactive data is defined using the `data` property on the component object <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. State changes are handled by methods defined in the `methods` property <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Templating**: Similar to Angular, Vue uses directives in its template, such as `v-for` for looping and `v-on:submit` for form submissions <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. A useful feature is `.prevent` modifier on `v-on` to automatically prevent default behavior <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Two-Way Data Binding**: Uses the `v-model` directive to bind form input values to component data <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Lifecycle Hooks**: Taps into the component lifecycle with methods like `mounted`, called on initialization <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## [[overview_of_lesserknown_javascript_frameworks_like_svelte_lit_and_mithril | Lesser-Known JavaScript Frameworks]]

### Svelte

Svelte was the "most loved" framework in the 2021 Stack Overflow survey <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a> and has about 50,000 GitHub stars <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. It is a minimal library, relying on the open-source community for features like routing <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. Svelte is unique because it doesn't ship a runtime like a virtual DOM to the browser; instead, it compiles code into plain JavaScript <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

*   **Build Tools**: Projects often use Rollup or Webpack for bundling <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>, meaning developers might need some knowledge of module bundlers <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   **Components**: Defined in `.svelte` files, with three parts: `<script>`, `<template>`, and `<style>` <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **State Management**: Reactive state is declared simply with the `let` keyword <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. State modification uses plain JavaScript functions, offering a natural feel with minimal abstractions <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   **Lifecycle Hooks**: The `onMount` function (imported from `svelte`) registers a callback for component initialization <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Templating**: Uses a special syntax like `{#each}` for looping over arrays <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Event handling uses `on:submit` with a `|preventDefault` modifier to prevent default behavior <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Two-Way Data Binding**: Achieved with the `bind:value` directive <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

Svelte's implementation is noted for its cleanliness, few lines of code, and readability for JavaScript developers <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. Its drawback is a smaller community compared to more popular frameworks, which can lead to roadblocks when seeking support or jobs <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

### Lit

Lit is a Google-sponsored project focused on building web components, a browser standard for creating custom, reusable elements <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. While other frameworks can create web components, Lit prioritizes this goal, offering a better developer experience for it <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. The standard Web Components API is known for being difficult to work with <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

*   **Project Setup**: Lit does not have its own CLI but provides a starter project (available in TypeScript) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. It uses `window.customElements`, part of the browser's Web Components API <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Components**: Defined as classes extending `LitElement` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **State Management**: Reactive data is defined as properties on the class using the `@property` decorator <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Methods are defined on the class to update state <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Lifecycle Hooks**: Based on Web Components API hooks, such as `connectedCallback` for component initialization <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Templating**: Uses existing JavaScript template literals (strings with backticks) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>, allowing JavaScript interpolation within HTML strings <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. The result is similar to JSX <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Event Handling**: HTML can include directives like `@submit` or `.value` for binding events or input values <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Two-Way Data Binding**: Does not natively support two-way data binding, requiring manual event listeners (e.g., `input change`) to update state <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

Lit provides a more pleasant way to build standard web components without requiring deep expertise in the underlying browser APIs <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Stencil

Stencil, from the team behind the Ionic framework, also focuses on web components <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Ionic itself uses web components built with Stencil to ensure compatibility across React, Angular, and Vue <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

*   **Project Setup**: New apps are created with `npm init stencil`, providing a TypeScript project <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>. It compiles components down to standard web components <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
*   **Components**: Defined as classes with a `@Component` decorator, similar to Angular <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **State Management**: Reactive data is defined as properties with the `@State` decorator <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. Custom methods update the state <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
*   **Lifecycle Hooks**: Includes hooks like `componentWillLoad` for initialization <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **Templating**: Uses JSX for templating, like React <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.
*   **Two-Way Data Binding**: Does not appear to support two-way data binding, requiring an `onInput` event listener to update text <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

### SolidJS

SolidJS is a UI component building tool heavily inspired by React <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. Its key difference is that it does not use a virtual DOM; instead, it compiles code down to native DOM nodes, similar to Svelte <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>. This results in very high performance across benchmarks <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. It's often described as a faster, more developer-friendly version of React <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

*   **Build Tools**: New projects use Vite as the build tool <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
*   **Components**: Defined in JSX files as functions <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
*   **State Management**: Uses "signals," similar to React hooks, which return a reactive value and an update function <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Lifecycle Hooks**: Offers a more readable `onMount` hook instead of `useEffect` for component initialization <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Templating**: Uses JSX, which looks almost identical to React's <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Data Binding**: Allows binding form values to variables using `ref` without needing to import a special hook like React's `useRef` <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

The main drawback of SolidJS is its smaller community <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Alpine.js

Alpine.js is a tiny library (around 4 KB) designed to extend existing HTML with reactive data and features found in larger frameworks <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. While frameworks primarily focus on JavaScript, Alpine emphasizes extending HTML <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. It's compared to [[integrating_tailwind_with_componentbased_javascript_frameworks | Tailwind CSS]] for JavaScript interactivity <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a> and is a popular replacement for jQuery <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. It has over 17,000 GitHub stars <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.

*   **Project Setup**: Requires adding the Alpine script to an HTML file <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
*   **State Management**: Reactive data is stored directly in a DOM node using the `x-data` attribute <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   **Templating/Directives**: Data can be used in child elements with directives like `x-for` for looping <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Event Handling**: Uses `x-on:submit` with `.prevent` to handle form submissions and bind to JavaScript functions <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. Concepts are similar to other frameworks but applied directly to raw HTML <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
*   **Global State**: `Alpine.store` allows storing and sharing data between multiple components <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Lifecycle**: The `document.addEventListener` for `alpine:init` event handles initialization, loading data from local storage into the store <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

Alpine.js is an excellent option for adding minor [[javascript_for_interactivity_and_frameworks | JavaScript interactivity]] to existing HTML pages <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. However, it's not a direct replacement for frameworks like React, Vue, or Angular for building complex single-page applications <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

### Mithril

Mithril is a lightweight framework that generally outperforms larger frameworks <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. It uses a virtual DOM, similar to React and Vue, but offers a distinct developer experience <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

*   **Project Setup**: Requires adding a Mithril script tag to an `index.html` file <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.
*   **Components**: Can be created from functions, classes, or plain JavaScript objects <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. Data and methods are added as properties to the component object <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   **Lifecycle Hooks**: Uses special properties like `oninit` for component initialization <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   **Templating**: The UI is defined using a `view` property <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. DOM nodes are created with the `m` function, passing the node name as the first argument and options or children as subsequent arguments <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. This system defines the UI entirely in pure JavaScript, which might appeal to those who prefer avoiding HTML <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.
*   **Event Handling**: Handlers for events like `onsubmit` are defined on the form element <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.

Mithril can feel awkward due to its pure JavaScript UI definition <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

## Conclusion

The [[state_of_javascript_in_modern_development | JavaScript framework landscape]] is constantly evolving, with new options emerging regularly <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>. Ultimately, all these frameworks are capable of achieving the same basic functionality <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. The choice comes down to personal preference and what works best for the development team <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.