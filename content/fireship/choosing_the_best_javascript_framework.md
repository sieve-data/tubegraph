---
title: Choosing the best JavaScript framework
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 

Determining the "best" JavaScript framework is a complex decision, as there is no single answer. While some metrics like downloads or GitHub stars might suggest a winner, the most suitable framework ultimately depends on individual preferences and project needs <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Factors like "most loved" surveys also play a role <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. For developers, whether new or experienced, choosing a framework is a significant decision related to frontend code <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The only way to find out which one truly satisfies requirements is to [[building_a_todo_app_with_different_javascript_frameworks|build something]] with multiple options <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

This article explores a [[comparison_of_10_web_frameworks|comparison of 10 web frameworks]] by demonstrating how the same basic to-do application can be built using each one, highlighting their [[tradeoffs_of_javascript_frameworks|trade-offs]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Vanilla JavaScript

While some argue that a [[comparison_of_popular_javascript_frameworks_in_2021|JavaScript framework]] isn't always necessary, any expert web developer needs a solid understanding of vanilla JavaScript <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. However, building a non-trivial application with vanilla JavaScript can lead to significant challenges, often resulting in developers inadvertently creating their own rudimentary framework <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

Building a to-do app in vanilla JavaScript involves:
*   Creating an HTML file with a script tag <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   Implementing functionality for users to input text, submit forms, and display items in a list <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   Saving items to local storage for persistence across page refreshes <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

This seemingly simple concept involves complex considerations such as state management, data binding, event handling, and the application lifecycle <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Challenges with Vanilla JS
The primary difference between frameworks and vanilla JavaScript is that frameworks provide automatic ways to bind HTML to JavaScript <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. In vanilla JS, developers must imperatively select HTML elements from the DOM using methods like `document.querySelector` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Manually creating new elements (e.g., `document.createElement`), updating their `innerHTML`, and appending them to the DOM is required for UI changes <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This process of manually managing DOM updates makes building complex applications annoying <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

A significant issue is the decoupling of application data (state) from the UI, making it difficult to keep them synchronized <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Event listeners must be registered explicitly, and understanding which HTML elements have attached listeners often requires searching through JavaScript code, which is challenging in complex applications <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Managing the application lifecycle, such as loading existing data from local storage upon initialization, also requires manual implementation <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

Vanilla JavaScript does not scale well with complexity, and features like routing or animation would need to be implemented from scratch <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This is why the vast majority of developers choose to build applications with a framework <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Popular JavaScript Frameworks

### React
React is widely considered the most popular [[comparison_of_popular_javascript_frameworks_in_2021|JavaScript framework]], often referred to as a library, but it dictates the main approach to a project <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Developed by Facebook, it excels at building complex UIs <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

*   **Philosophy**: React is minimal by design, relying on the open-source community for features like routing, animation, and state management <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. It's not opinionated about code organization, requiring developers to make decisions on libraries and maintainability <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Popularity**: It's the most popular framework, with over 10 million weekly npm downloads and over 170,000 GitHub stars <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Its popularity makes it a valuable skill for employment and collaboration <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Tools**: React has an official CLI called Create React App <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Alternative tools like Next.js or Gatsby are also popular <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Projects generated with Create React App use Webpack for code bundling <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Components**: Applications are organized as a tree of components that encapsulate UI parts and communicate with each other <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This enables a declarative approach where UI is consistent for given data <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Syntax**: Components are typically functions that return JSX, an HTML-like syntax extended with JavaScript insertion <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **State Management**: Reactive state is defined using hooks like `useState`, which returns the state value and a function to update it, triggering UI re-renders <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Event Handling**: Events can be bound directly to JSX elements using attributes like `onSubmit` <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. The `useRef` hook can be used to access form input values <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Lifecycle Hooks**: The `useEffect` hook handles component lifecycle, such as loading data on initialization <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. However, `useEffect` can be confusing for beginners, especially when ensuring it runs only once by adding an empty array as a second argument <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Angular
Angular, developed and maintained by Google, is React's "arch nemesis" <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Unlike React, it is highly opinionated about project organization and structure <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

*   **Popularity**: It has 75,000 GitHub stars and is the second most downloaded framework on npm <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Features**: Angular provides officially supported libraries for routing, animation, and server-side rendering <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Conventions**: Its predictable conventions ensure that Angular projects are structured similarly, offering excellent tooling <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **TypeScript**: It requires the use of TypeScript <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Use Cases**: Google uses Angular internally for hundreds of web applications <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. It's a strong option for large teams but can be overwhelming for beginners <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Tools**: Projects are initialized with `ng-new` from the command line, providing a large, pre-configured TypeScript project <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Angular has the most powerful CLI among frameworks, allowing for automatic component generation <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Components**: Components are represented as TypeScript classes with a `@Component` decorator <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Most Angular apps separate components into three files: TypeScript, HTML, and CSS <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **State Management**: Reactive state is defined as properties on the class <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Methods are defined on the class to update state <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Lifecycle Hooks**: Special methods like `ngOnInit` manage the component's lifecycle, called upon initialization <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Templating**: Templates resemble HTML but are extended with a special templating language using directives like `ngFor` to loop over items <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Unlike React, which brings HTML into JavaScript, Angular brings JavaScript into HTML <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Event Handling & Data Binding**: The `submit` event can be bound to methods <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Two-way data binding is achieved using the `ngModel` directive <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>, which requires importing the `Angular Forms` module <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Learning Curve**: Angular tends to have a higher learning curve due to its opinionated structure and requirements <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Its structured approach makes it popular for enterprise applications <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Vue.js
Vue.js is an independently developed and maintained framework by Evan You, offering a similar feel to Angular but in a more approachable package for independent developers <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

*   **Ecosystem**: It provides official packages for routing and state management, alongside a large ecosystem of third-party packages <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Popularity**: Vue has the most GitHub stars (187,000) and is nearly tied with Angular for second place in npm downloads <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Tools**: Vue has a powerful CLI, including a `view ui` command that provides a browser-based interface to manage dependencies and features <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. While good, it's not as powerful as Angular's CLI for generating components <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Project Structure**: It generates a more simplified project structure, allowing for additional plugins (e.g., routing) to be added in `main.js` as needed <a class="yt-timestamp" data-t="00:10:57">[00:11:05]</a>.
*   **Components**: Components are defined in `.vue` files, organized into three parts: template, script, and styles <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **State Management**: Components are represented as plain JavaScript objects <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>, with reactive data defined using the `data` property <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. State changes are handled by methods defined in the `methods` property <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Lifecycle Hooks**: Lifecycle methods like `mounted` are called when the component is initialized <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Templating**: Similar to Angular, Vue templates use directives like `v-for` to loop over items and `v-on:submit` for event handling <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. A useful feature is the `.prevent` modifier on `v-on` directives to automatically prevent default event behavior <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Data Binding**: The `v-model` directive provides two-way data binding for form inputs <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. Vue offers many small conveniences that improve developer experience <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

### Svelte
Svelte is another independent framework known for being the "most loved" framework in the 2021 Stack Overflow survey <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. It has approximately 50,000 GitHub stars and is less common than React, Angular, or Vue, but highly appreciated by its users <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

*   **Philosophy**: Like React, Svelte is designed as a minimal library, relying on the open-source community for features like routing <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **Unique Compilation**: Its key distinction is that it doesn't ship a runtime (like a virtual DOM) to the browser <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. Instead, it acts as a compiler, transforming code into plain JavaScript <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Build Tools**: When creating a new project, developers may need to understand module bundlers like Rollup or Webpack, as the CLI tools don't fully abstract this away <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Components**: Components are defined in `.svelte` files, structured with three parts: script, template, and styles <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **State Management**: Reactive state is created by simply declaring a variable with `let` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. State modification is handled by plain JavaScript functions <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. This approach feels natural due to minimal abstractions <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Lifecycle Hooks**: The `onMount` function (imported from Svelte) allows registering a callback for component initialization <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Templating**: Svelte uses a special syntax with directives like `{#each}` for looping through arrays <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Event Handling & Data Binding**: Event handling uses `on:submit`, with a modifier like `|preventDefault` to avoid manual implementation in the function <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Two-way data binding is done with the `bind:value` directive <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   **Pros & Cons**: Svelte offers a clean implementation with fewer lines of code and good readability <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. However, its community is significantly smaller than React's, which can lead to challenges when seeking supporting libraries or job opportunities <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

### Lit
Lit is a Google-sponsored project focused on building web components <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Web components are a browser standard for creating custom elements that can work across different frameworks <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>, although their native API can be challenging <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

*   **Focus**: Lit simplifies the creation of standard custom elements, making the web components API more approachable <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **Tools**: Lit doesn't have its own CLI but provides a starter project (with optional TypeScript) <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. It directly uses `window.customElements`, part of the browser's web components API <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Components**: Components are defined as classes that extend `LitElement` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   **State Management**: Reactive data is defined as properties on the class using the `@property` decorator <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Methods are defined on the class to update state <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Lifecycle Hooks**: Lifecycle hooks are based on the web components API, such as `connectedCallback`, which runs when the component is initialized <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Templating**: Lit uses JavaScript template literals (strings with backticks) for templates, allowing interpolation of JavaScript into HTML strings using `${}` <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This feels similar to React's JSX <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Event Handling & Data Binding**: HTML can include directives like `@submit` or `.value` for binding <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. It doesn't appear to support two-way data binding, requiring explicit event listeners (e.g., `input change`) to update state <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Use Cases**: Lit provides a much nicer way to build standard web components without needing deep expertise in the underlying APIs <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Stencil
Stencil is another framework focused on web components, developed by the team behind the Ionic Framework (a component library for mobile development built with Stencil) <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Ionic uses web components to ensure compatibility with React, Angular, and Vue <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

*   **Tools**: A new app is created using `npm init stencil`, providing a TypeScript project <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.
*   **Compilation**: Like Lit, Stencil compiles each component down to a standard web component <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
*   **Components**: A component is a class with the `@Component` decorator, similar to Angular <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **State Management**: Reactive data is defined as properties using the `@State` decorator <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Custom methods update the state <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
*   **Lifecycle Hooks**: Lifecycle hooks include `componentWillLoad`, which runs when the component is initialized <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **Templating**: For templating, Stencil uses JSX, similar to React, offering a blend of Angular-like component structure with React-like UI definition <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.
*   **Data Binding**: It does not appear to support two-way data binding, requiring an additional `onInput` event listener to update text when a user types <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

### SolidJS
SolidJS is a UI component building tool heavily inspired by React <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. Its key difference is that it does not use a virtual DOM; instead, it compiles code directly to native DOM nodes, similar to Svelte <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.

*   **Performance**: This compilation approach leads to very high performance across benchmarks <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **Developer Experience**: It's considered a faster, more developer-friendly version of React <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Community**: The drawback is a smaller community <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Tools**: New projects are generated using Vite as the build tool <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
*   **Components**: Components are defined in JSX files, just like React <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>, and are represented as functions <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **State Management**: Reactive state uses "signals," similar to React hooks, returning a reactive value and an update function <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. Functions can be defined to update the state <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Lifecycle Hooks**: Instead of `useEffect`, Solid offers the more readable `onMount` hook, which runs upon component initialization <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Templating**: The UI is defined using JSX, almost identical to React code <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Developer Conveniences**: Solid streamlines certain aspects; for instance, the `ref` attribute for binding form values doesn't require importing a `useRef` hook, unlike React <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. Overall, SolidJS feels like a more refined and faster version of React <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### Alpine.js
Alpine.js is a tiny (around 4KB) library that extends existing HTML with reactive data and features found in larger frameworks <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. Unlike other frameworks that prioritize JavaScript, Alpine primarily focuses on manipulating HTML <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. It's often compared to Tailwind CSS but for JavaScript interactivity <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

*   **Popularity**: It has over 17,000 GitHub stars and is a popular replacement for jQuery <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   **Setup**: To start, include the Alpine script tag in an HTML file <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
*   **State Management**: Reactive data can be stored directly within a DOM node using the `x-data` attribute <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. This data can then be used in child elements with directives like `x-for` for looping <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.
*   **Event Handling**: `x-on:submit` handles form submissions, and `prevent` can be added to the directive to prevent default behavior <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
*   **JavaScript Integration**: Plain JavaScript can be written in a script tag <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. Alpine offers `Alpine.store` for sharing data between multiple components <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Lifecycle Hooks**: The `alpine:init` custom event can be listened to using `document.addEventListener` to load data when the component is initialized <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Use Cases**: Alpine is excellent for adding minor JavaScript interactivity to existing HTML pages <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. However, it may not be suitable as a replacement for frameworks like React, Vue, or Angular when building complex single-page applications <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.

### Mithril
Mithril is a lightweight framework that often outperforms larger frameworks <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. It uses a virtual DOM, similar to React and Vue, but offers a distinct developer experience <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

*   **Setup**: Start by including the Mithril script tag in an `index.html` file <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Components**: Components can be created from functions, classes, or plain JavaScript objects <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.
*   **State & Methods**: Data and methods are added as properties on the component object <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   **Lifecycle Hooks**: Special properties like `oninit` serve as lifecycle hooks for component initialization <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   **Templating**: The UI is defined using a `view` property <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. DOM nodes are created with the `m` function, passing the node name as the first argument and options (like class name) or children as subsequent arguments <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.
*   **Event Handling**: Event handlers, like `onsubmit` for forms, are defined within the `m` function's options <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.
*   **Syntax**: The syntax is similar to JSX but defines the UI entirely in pure JavaScript <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. This approach might appeal to developers who prefer to avoid HTML <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

## Conclusion

All [[comparison_of_popular_javascript_frameworks_in_2021|JavaScript frameworks]] can achieve the same basic results <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. The choice ultimately comes down to which one makes the developer and their team happy <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. The [[javascript_trends_and_frameworks|emergence of frameworks and tools in modern JavaScript]] is continuous, meaning such [[javascript_frameworks_and_their_updates|comparisons]] can quickly become outdated <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>. For a [[pros_and_cons_of_different_full_stack_frameworks|comparison with other JavaScript frameworks]] in action, further resources are available <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.