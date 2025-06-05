---
title: Choosing the right JavaScript framework for your project
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 

Deciding which [[frontend_ui_libraries_and_frameworks | JavaScript framework]] is "the best" is a complex question with no single answer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While React leads in downloads <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> and Vue has the most GitHub stars <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, Svelte was identified as the most loved framework in the 2021 Stack Overflow survey <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. For both new and experienced developers, [[choosing_the_right_programming_language | selecting a framework]] can be challenging <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. There is no universally "best" framework; the ideal choice is the one that aligns with your project and team needs <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

To truly understand the [[comparison_of_web_development_frameworks | trade-offs between frameworks]], one must build something with them <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This article explores several [[comparison_of_javascript_frameworks | JavaScript frameworks]]—including Angular, React, Vue, Svelte, Lit, Alpine, Solid, Stencil, Mithril, and Vanilla JS—by examining how each handles a basic to-do application <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Vanilla JavaScript

Every expert web developer should have a solid understanding of [[javascript_for_interactivity_and_frameworks | vanilla JavaScript]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. However, attempting to build a non-trivial application with it alone can be problematic, often leading to developers creating their own rudimentary framework <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Challenges of Vanilla JS
*   **No Automatic Data Binding**: Vanilla JS does not automatically connect HTML to JavaScript <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Developers must imperatively grab HTML elements from the DOM <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Manual UI Updates**: Updating the UI requires manually creating and appending elements, which can be cumbersome in complex applications <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Decoupled State and UI**: The application data (state) is entirely separate from the UI, making it difficult to keep them in sync <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Lack of Readability**: HTML markup provides no immediate indication of attached event listeners, requiring developers to search through JavaScript code <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Missing Features**: Features like routing or animation must be implemented from scratch <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

For these reasons, most developers opt for a framework to build their applications <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Popular JavaScript Frameworks

### React
Often considered the most popular [[state_of_javascript_in_modern_development | JavaScript framework]], React is a tool that drives a project, requiring development in "the React way" <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. It was developed by Facebook to build complex UIs <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Minimal by Design**: React relies on the open-source community for features like routing, animation, and state management <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Not Opinionated**: It doesn't dictate code organization, requiring developers to choose libraries and ensure maintainability <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Popularity**: Over 10 million weekly npm downloads and 170,000+ GitHub stars <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Its popularity makes it a valuable skill for employment and collaboration <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Development**: Uses `create-react-app` CLI (though alternatives like Next.js exist) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a> and Webpack for bundling <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Component-Based**: Applications are organized as a tree of components that encapsulate UI parts and communicate declaratively <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **JSX**: Components return JSX, which combines HTML-like syntax with JavaScript <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Hooks**: `useState` defines reactive state <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, `useRef` accesses DOM elements <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>, and `useEffect` handles lifecycle events, though it can be confusing for beginners <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Pros**: Highly popular, strong job market, large community, declarative UI.
*   **Cons**: Relies heavily on community packages, `useEffect` can be complex.

### Angular
Developed and maintained by Google, Angular is a highly opinionated framework that dictates project organization and structure <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Popularity**: 75,000 GitHub stars and second most downloaded framework on npm <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Comprehensive**: Comes with official libraries for routing, animation, and server-side rendering <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Predictable Conventions**: Angular projects are structured similarly, offering excellent tooling <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **TypeScript**: Requires TypeScript for development <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **CLI**: Features the most powerful CLI among frameworks, capable of generating new components <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Component Structure**: Components are TypeScript classes with decorators, often broken into separate files for TypeScript, HTML, and CSS <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Templating**: HTML templates are extended with a special templating language, bringing JavaScript into HTML <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Directives like `ngFor` (looping) and `ngModel` (two-way data binding) are used <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Lifecycle Hooks**: Uses methods like `ngOnInit` for component initialization <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Pros**: Highly structured, excellent for large teams and enterprise applications, strong tooling.
*   **Cons**: Steep learning curve, can be overwhelming for beginners <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Vue.js
Independently developed by Evan You, Vue.js feels similar to Angular but is more approachable for independent developers <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Ecosystem**: Offers official packages for routing and state management, plus a large third-party ecosystem <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Popularity**: Has the most GitHub stars (187,000) and is tied with Angular for second place in npm downloads <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **CLI**: Features a powerful CLI with a UI (`vue ui`) that helps generate and configure applications <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Component Structure**: Components are defined in `.vue` files, organized into three parts: template, script, and styles <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Reactive Data**: Reactive state is defined using the `data` property on a plain JavaScript object <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Methods & Lifecycle**: Methods are defined to change state, and lifecycle hooks like `mounted` are used for initialization <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Directives**: Uses directives similar to Angular, such as `v-for` for looping and `v-on:submit` for event handling (with `.prevent` modifier for convenience) <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. `v-model` provides two-way data binding <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
*   **Pros**: Excellent developer experience, large community, flexible, approachable.

### Svelte
Svelte was recognized as the "most loved framework" in the 2021 Stack Overflow survey <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a> and has around 50,000 GitHub stars <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **Unique Approach**: Unlike other frameworks, Svelte acts as a compiler that turns your code into plain JavaScript during development, without shipping a runtime like a virtual DOM to the browser <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Build Tools**: May require learning about module bundlers like Rollup or Webpack <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   **Component Structure**: Components are defined in `.svelte` files with script, template, and style sections <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Reactive State**: Reactive state is created by simply declaring a variable with `let` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Plain JS Functions**: State modification uses plain JavaScript functions, making it feel very natural and less abstract <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Lifecycle Hooks**: Uses the `onMount` function for initialization <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Templating**: Special syntax for looping (`each`) and event handling (`on:submit` with `.prevent` modifier) <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. `bind:value` is used for two-way data binding <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   **Pros**: Cleanest implementation with fewer lines of code, easy to read, no runtime.
*   **Cons**: Smaller community and job market compared to more popular frameworks <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Lesser-Known and Specialized Frameworks

### Lit
Lit is a Google-sponsored project focused on building [[overview_of_lesserknown_javascript_frameworks_like_svelte_lit_and_mithril | web components]] <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. It simplifies the often-difficult Web Components API <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Web Components Focus**: Defines standard custom elements under the hood <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **Development**: No dedicated CLI, but starter projects are available <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Components are classes extending `LitElement` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Reactive Data**: Defined as properties on the class using property decorators <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   **Lifecycle Hooks**: Based on the Web Components API, such as `connectedCallback` <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Templating**: Uses JavaScript template literals (backticks) to interpolate JavaScript into HTML strings, similar to JSX <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **Event Handling**: Supports directives like `@submit` and `.value`, but explicit event listeners might be needed for two-way data binding <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Pros**: Provides a cleaner way to build standard web components.

### Stencil
From the team behind Ionic Framework, Stencil also focuses on building [[overview_of_lesserknown_javascript_frameworks_like_svelte_lit_and_mithril | web components]] to make Ionic compatible with other frameworks like React, Angular, and Vue <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Development**: Created via `npm init stencil`, providing a TypeScript project <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>. Compiles components to standard web components <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
*   **Component Structure**: Components are classes with a `@Component` decorator, similar to Angular <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **Reactive Data**: Defined as properties with the `@State` decorator <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
*   **Lifecycle Hooks**: Methods like `componentWillLoad` for initialization <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Templating**: Uses JSX, similar to React <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   **Event Handling**: Similar to React, but two-way data binding may require extra event listeners <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **Pros**: Great for building web components, ensures compatibility across frameworks.

### SolidJS
SolidJS is a [[overview_of_lesserknown_javascript_frameworks_like_svelte_lit_and_mithril | UI component framework]] inspired by React but distinct in its approach: it doesn't use a virtual DOM. Instead, it compiles code down to native DOM nodes, like Svelte <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Performance**: Achieves high performance marks across benchmarks <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.
*   **Development**: Uses Veet as its build tool <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. Components are defined in JSX files as functions <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Reactive State**: Uses "signals," similar to React hooks, returning a reactive value and an update function <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Lifecycle Hooks**: Employs the readable `onMount` hook for component initialization <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Templating**: Uses JSX, which is nearly identical to React code <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
*   **Ref Binding**: Simplifies form value binding with `ref` without needing an explicit hook import <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Pros**: Faster, more developer-friendly than React, high performance.
*   **Cons**: Smaller community <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Alpine.js
Alpine.js is a tiny (around 4KB) library that extends existing HTML with reactive data and features found in larger frameworks <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. It's often likened to [[integrating_tailwind_with_componentbased_javascript_frameworks | Tailwind]] for CSS but for JavaScript <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **HTML-Centric**: Developers primarily focus on HTML, using `x-data` attributes for reactive data <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
*   **Directives**: Uses directives like `x-for` for looping and `x-on:submit.prevent` for event handling <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   **Alpine Store**: Offers `Alpine.store` for sharing data between multiple components <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Lifecycle**: Uses `document.addEventListener` for custom Alpine events like `alpine:init` for initialization <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Pros**: Lightweight, ideal for adding small bits of interactivity to existing HTML pages, popular jQuery replacement <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.
*   **Cons**: Not suitable for complex single-page applications <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

### Mithril
Mithril is another lightweight framework that tends to perform better than larger frameworks <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. It uses a virtual DOM, similar to React and Vue, but offers a distinct development experience <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.
*   **Development**: Components can be created from functions, classes, or plain JavaScript objects <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.
*   **Data & Methods**: Data and methods are added as properties on the component object <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   **Lifecycle Hooks**: Uses special properties like `oninit` for component initialization <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   **Pure JavaScript UI**: The `m` function is used to define DOM nodes, making the UI truly defined in pure JavaScript <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. This is similar to JSX but more explicitly JavaScript-driven <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
*   **Pros**: Lightweight, good performance, pure JavaScript UI.
*   **Cons**: Can feel awkward, potentially longer development time for some <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

## Conclusion: Understanding and Choosing a Tech Stack

Ultimately, all these [[understanding_and_choosing_a_tech_stack | JavaScript frameworks]] can achieve the same basic functionality <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. The choice largely boils down to personal preference and what makes you and your team most productive and satisfied <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. As new frameworks emerge frequently, staying updated on the [[state_of_javascript_in_modern_development | evolving landscape of JavaScript development]] is key <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.