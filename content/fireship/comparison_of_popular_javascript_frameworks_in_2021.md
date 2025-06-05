---
title: Comparison of popular JavaScript frameworks in 2021
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 

Choosing a JavaScript framework can be a difficult decision for developers of any experience level, as there is no single "best" option <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The ideal choice often depends on individual preference and project requirements <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. This article provides a [[comparison_with_other_javascript_frameworks | comparison]] of 10 different JavaScript frameworks by examining how each approaches the task of [[building_a_todo_app_with_different_javascript_frameworks | building a basic to-do application]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This approach helps highlight the [[tradeoffs_of_javascript_frameworks | tradeoffs]] between them, aiding in [[choosing_the_best_javascript_framework | choosing the best JavaScript framework]] for a given project <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Why JavaScript Frameworks?

While some argue that a JavaScript framework isn't always necessary <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, building a non-trivial application with vanilla JavaScript often leads to creating one's own, less optimized framework <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Frameworks simplify complex tasks like state management, data binding, event handling, and managing the application lifecycle <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Vanilla JavaScript Implementation Challenges
The core advantage of frameworks over vanilla JavaScript is automatic HTML-to-JavaScript binding <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. In vanilla JavaScript, developers must imperatively select DOM elements <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For a to-do app, this involves:
*   Manually creating and appending list item elements to update the UI <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   Storing data in local storage and manually updating the UI when data changes <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   Explicitly registering event listeners for user interactions, making it hard to see the connection between HTML and JavaScript <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Managing the application lifecycle manually, such as loading existing items from local storage on initialization <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

This manual approach doesn't scale well for complex applications that might require features like routing or animation <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Popular Frameworks in Detail

### React
*   **Overview**: Often considered the most popular framework, with over 10 million weekly npm downloads and 170,000+ GitHub stars <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Developed by Facebook, it excels at building complex UIs <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. It's minimal by design and relies on its open-source community for features like routing and state management <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Development**: Uses a component-based architecture where applications are organized as a tree of encapsulated UI parts <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Key Features**:
    *   **JSX**: An extension of HTML syntax that allows embedding JavaScript directly into HTML <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   **`useState` Hook**: Manages reactive state on components, triggering UI re-renders when data changes <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
    *   **`useEffect` Hook**: Handles component lifecycle events, though its behavior can be confusing for beginners <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **CLI**: `create-react-app` is the official CLI, though alternatives like Next.js or Gatsby are often used <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Pros**: High popularity leads to many job opportunities and a large community for support <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. HTML is more descriptive, showing data and event bindings <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Cons**: Requires many decisions about third-party libraries due to its minimal nature <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Angular
*   **Overview**: Developed and maintained by Google, Angular is a highly opinionated framework for structuring projects <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. It has over 75,000 GitHub stars and is the second most downloaded framework on npm <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Development**: Components are represented as TypeScript classes with decorators <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Projects typically break components into separate TypeScript, HTML, and CSS files <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Key Features**:
    *   **TypeScript**: Required for Angular projects <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   **Powerful CLI**: Considered the most powerful among frameworks, used for project generation and component creation <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   **Templating Language**: Extends HTML with special directives like `*ngFor` for looping over arrays <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   **Two-Way Data Binding**: Achieved using the `[(ngModel)]` directive for form inputs <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   **Lifecycle Hooks**: Methods like `ngOnInit` are used to run code when components are initialized <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Pros**: Highly structured and predictable conventions make it great for large teams and enterprise applications <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Comes with official libraries for routing, animation, and server-side rendering <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Cons**: Higher learning curve compared to other frameworks <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Vue.js
*   **Overview**: Independently developed by Evan You, Vue.js offers a similar feel to Angular but is more approachable for independent developers <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. It boasts the most GitHub stars (187,000+) and is tied with Angular for second place in npm downloads <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Development**: Components are defined in `.vue` files, organized into three parts: template, script, and styles <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Reactive data is defined on a plain JavaScript object via the `data` property <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Key Features**:
    *   **CLI**: A powerful CLI includes a UI command that provides a browser-based interface for project generation and dependency management <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
    *   **Directives**: Uses directives like `v-for` for looping and `v-on:submit` for event handling <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. It allows adding `.prevent` to directives to automatically prevent default event behavior <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
    *   **`v-model`**: Provides two-way data binding for form inputs <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
    *   **Lifecycle Methods**: Methods like `mounted` are called when the component is first initialized <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Pros**: Large community and ecosystem of third-party packages <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Offers many conveniences that simplify development <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Cons**: CLI component generation is not as powerful as Angular's <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

### Svelte
*   **Overview**: Svelte was recognized as the "most loved" framework in the 2021 Stack Overflow survey, with around 50,000 GitHub stars <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. Unlike most other frameworks, Svelte operates as a compiler, transforming code into plain JavaScript at build time instead of shipping a runtime (like a virtual DOM) to the browser <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Development**: Components are defined in `.svelte` files, similar to Vue, with script, template, and style sections <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Key Features**:
    *   **Reactive State**: Achieved by simply declaring variables with `let` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
    *   **Minimal Abstractions**: Feels like regular JavaScript, making it very natural for developers <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   **`onMount` Function**: Handles lifecycle hooks, registered as a callback <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
    *   **Templating Syntax**: Uses special syntax like `{#each}` for looping <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
    *   **`bind:value` Directive**: Provides two-way data binding <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   **Pros**: Cleanest implementation with fewer lines of code and high readability <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Cons**: Smaller community compared to React or Angular, which can lead to roadblocks when seeking supporting libraries or job opportunities <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. May require learning about module bundlers <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

## Specialized and Alternative Frameworks

### Lit
*   **Overview**: A Google-sponsored project focused on building web components, which are a browser standard for creating custom, reusable elements <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Lit simplifies the notoriously difficult Web Components API <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   **Development**: Components are defined as classes extending `LitElement` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Key Features**:
    *   **Reactive Data**: Defined as properties on the class using the `@property` decorator <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
    *   **Lifecycle Hooks**: Based on Web Components API, such as `connectedCallback` <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
    *   **Templates**: Utilizes JavaScript template literals (backticks) to interpolate JavaScript into HTML strings, similar to React's JSX <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
    *   **No Two-Way Data Binding**: Requires manual event listeners for input changes <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Pros**: Provides a much nicer developer experience for building standard web components without deep API expertise <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.
*   **Cons**: No built-in CLI, relies on starter projects <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

### Stencil
*   **Overview**: Developed by the team behind Ionic Framework, Stencil is also focused on creating web components <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Ionic uses Stencil to build components compatible with React, Angular, and Vue <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
*   **Development**: Components are TypeScript classes with a `@Component` decorator, resembling Angular components <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **Key Features**:
    *   **Compilation**: Compiles each component down to a standard web component <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
    *   **Reactive Data**: Defined as properties with the `@State` decorator <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
    *   **Lifecycle Hooks**: Includes methods like `componentWillLoad` <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
    *   **Templating**: Uses JSX, similar to React <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
    *   **No Two-Way Data Binding**: Requires separate event listeners for input changes <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **Pros**: Excellent for building reusable web components that are framework-agnostic <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.
*   **Cons**: Similar to Lit, the lack of built-in two-way data binding for forms.

### SolidJS
*   **Overview**: SolidJS is a UI component building tool heavily inspired by React, but it does not use a virtual DOM <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. Instead, it compiles code down to native DOM nodes, similar to Svelte, resulting in high performance <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.
*   **Development**: Components are defined as functions within JSX files, similar to React <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
*   **Key Features**:
    *   **Signals**: A reactive state mechanism similar to React hooks, returning a reactive value and an update function <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
    *   **`onMount` Hook**: A more readable lifecycle hook compared to React's `useEffect`, running when the component is initialized <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
    *   **JSX**: Uses JSX for UI definition, which looks almost identical to React's JSX <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
    *   **Developer Friendly**: Simplifies certain aspects, like binding form values with `ref` without needing explicit hook imports <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   **Pros**: Offers a faster and more developer-friendly experience than React <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
*   **Cons**: Smaller community compared to larger frameworks <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Alpine.js
*   **Overview**: A tiny (around 4 KB) library that extends existing HTML with reactive data and framework-like features <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. Alpine.js is often considered the JavaScript equivalent of Tailwind CSS for its utility-first approach to HTML <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. It has over 17,000 GitHub stars and is a popular jQuery replacement <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   **Development**: Primarily focuses on HTML, with JavaScript interactions handled directly in DOM nodes via special attributes <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
*   **Key Features**:
    *   **`x-data`**: Stores reactive data directly in a DOM node <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
    *   **`x-for`**: Used for looping over arrays <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   **`x-on:submit`**: Handles form submissions, with `.prevent` modifier for default behavior <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
    *   **Alpine Store**: A mechanism for storing and sharing data across multiple components <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
    *   **`alpine:init` Event**: A custom event that fires when Alpine is initialized, useful for loading data <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Pros**: Adds interactivity to existing HTML with minimal code <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
*   **Cons**: Not suitable for very complicated single-page applications where frameworks like React, Vue, or Angular would be better <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

### Mithril
*   **Overview**: A lightweight JavaScript framework that uses a virtual DOM, similar to React and Vue, but offers a distinct developer experience <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. It generally performs better than larger frameworks <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
*   **Development**: Components can be created from functions, classes, or plain JavaScript objects <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.
*   **Key Features**:
    *   **Pure JavaScript UI**: The UI is defined entirely in JavaScript using the `m` function to create DOM nodes <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.
    *   **`oninit` Property**: A lifecycle hook for component initialization <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.
    *   **Reactive Data**: Defined as properties on the component object <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   **Pros**: Lightweight and high-performing <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. Appeals to developers who prefer to define UI purely in JavaScript <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.
*   **Cons**: The UI definition can feel awkward and might take longer to learn for some <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

## Conclusion

The [[comparison_of_10_web_frameworks | comparison of these 10 web frameworks]] demonstrates that while new [[javascript_frameworks_and_their_updates | JavaScript frameworks]] continue to emerge <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>, they all aim to achieve the same fundamental tasks <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. The ultimate decision on which framework to use boils down to personal preference and what works best for a development team <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. Each framework offers distinct [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | differences and similarities]] in its approach, providing various [[tradeoffs_of_javascript_frameworks | tradeoffs]] that cater to different project needs and team dynamics.