---
title: Building a todo app with different JavaScript frameworks
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 
Which JavaScript framework is the best? This is a common question without a single answer, as the ideal choice depends on various factors. This article explores different JavaScript frameworks by demonstrating how to build a basic to-do application with each, highlighting their unique features and [[tradeoffs_of_javascript_frameworks | tradeoffs]].

### [[choosing_the_best_javascript_framework | Choosing the Best JavaScript Framework]]

The "best" JavaScript framework is subjective. While [[comparison_of_popular_javascript_frameworks_in_2021 | downloads]] might suggest React, GitHub stars point to Vue, and Svelte was the most loved framework in the 2021 Stack Overflow survey <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Deciding which framework to commit to can be challenging for developers at any experience level <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. There is no absolute best framework; the only way to find what works for you is to experiment by building applications with different ones <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

This article will demonstrate building the same to-do app using ten different [[javascript_frameworks_and_their_updates | JavaScript frameworks]]: Angular, React, Vue, Svelte, Lit, Alpine, Solid, Stencil, Mithril, and vanilla JavaScript <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Vanilla JavaScript

A common "hot take" suggests that a [[emergence_of_frameworks_and_tools_in_modern_javascript | JavaScript framework]] isn't needed <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. While any expert web developer needs a solid understanding of vanilla JavaScript <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, attempting to build a non-trivial application with it can lead to creating your own, potentially problematic, framework <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

Building a to-do app with vanilla JavaScript involves:
*   **HTML Structure**: Creating an HTML file with an unordered list for to-dos and a form with an input and submit button <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Functionality**: Allowing users to input text, submit the form, display items in a list, and save items to local storage for persistence <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Core Challenges**: This simple concept involves complex considerations like state management, data binding, events, and the application lifecycle <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

One major difference between frameworks and vanilla JS is how they handle binding HTML to JavaScript <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. In vanilla JS, you must imperatively select HTML elements from the DOM using `document.querySelector` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

#### Implementation Details
*   **DOM Manipulation**: Manually creating new list item elements (`document.createElement`), updating their `innerHTML`, and appending them to the unordered list <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **State Management**: The application data (state) is completely decoupled from the UI, making it difficult to keep them in sync <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Event Handling**: Registering an event listener for the form's `submit` event, calling `preventDefault` to stop page refresh, and then adding the to-do <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The HTML itself doesn't indicate attached event listeners, requiring manual search through JavaScript code in complex applications <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Application Lifecycle**: On initialization, existing to-do items must be manually retrieved from local storage and rendered <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

While a to-do app can be built with vanilla JS, the code does not scale well for complexity, and features like routing or animation would require custom implementation <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This is why most developers opt for a framework <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### React

React is widely considered the most popular JavaScript framework, though some refer to it as a library <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Design**: Minimal by design, it relies on the open-source community for features like routing, animation, and state management <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. It's not opinionated about code organization, requiring developers to make many decisions <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Popularity**: It boasts over 10 million weekly downloads on npm and over 170,000 GitHub stars <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Its popularity makes it a valuable skill for employment and collaboration <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Development**: Created by smart people at Facebook to build complex UIs <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Tooling**: Features an official CLI, `create-react-app`, for project creation <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Alternatives like Next.js or Gatsby are also popular <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. It uses Webpack to bundle code <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

#### Implementation Details
*   **Components**: Applications are organized as a tree of components, which encapsulate UI parts and communicate with each other <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Components are represented as functions returning JSX <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **JSX**: Looks like HTML but is extended to allow embedding JavaScript <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Reactive State**: Defined using the `useState` hook, which provides the state value and a function to update it, triggering UI re-renders <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Event Binding**: Events can be bound directly in JSX (e.g., `onSubmit`), referencing a function to handle the event <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Form Input**: The `useRef` hook is used to access the current value of a form input <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Application Lifecycle**: The `useEffect` hook handles lifecycle events, such as loading items from local storage on component initialization <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This hook can be confusing for beginners, especially needing an empty array as a second argument to run only once <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

React is considered the gold standard for declarative UI frameworks <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### Angular

Angular, maintained by Google, is React's "arch nemesis" <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Design**: Very opinionated about project organization and structure <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It includes officially supported libraries for routing, animation, and server-side rendering <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Popularity**: Has 75,000 GitHub stars and is the second most downloaded framework on npm <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Structure**: Follows predictable conventions, resulting in similar project structures across applications <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. It requires the use of TypeScript <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Use Case**: Google uses it internally for hundreds of web apps <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, making it a great option for large teams, though it can be overwhelming for beginners <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Tooling**: Its CLI (`ng new`) is considered the most powerful among frameworks <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

#### Implementation Details
*   **Components**: Defined as TypeScript classes with a `@Component` decorator <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Components are typically broken into three files: TypeScript, HTML, and CSS <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Reactive State**: Defined as properties on the component class <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Methods on the class update the state <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Application Lifecycle**: Handled by implementing special methods like `ngOnInit`, which is called when the component is first initialized <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Templating**: HTML templates are extended with a special templating language, allowing directives like `ngFor` to loop over arrays <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Unlike React, which brings HTML into JavaScript, Angular brings JavaScript into HTML <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Event Binding**: Binding to events like `submit` is done directly in the template <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Two-way Data Binding**: The `ngModel` directive enables two-way data binding for form inputs, but it requires importing the Angular Forms module <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

Angular has a higher learning curve due to its opinionated structure and requirements <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. This strong opinionated approach makes it popular for enterprise applications that need to scale <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Vue.js

Vue.js, independently developed by Evan You, offers a similar feel to Angular but in a more approachable package for independent developers <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Design**: Provides official packages for routing and state management, along with a large ecosystem of third-party packages <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Popularity**: Boasts the most GitHub stars at 187,000 and is nearly tied with Angular for second place in npm downloads <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Tooling**: Features a powerful CLI, including a `vue ui` command that launches a browser window for interactive project generation <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. While powerful, it doesn't generate components like Angular's CLI <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. It generates a simplified project structure where additional plugins can be added in `main.js` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

#### Implementation Details
*   **Components**: Defined in `.vue` files, organized into three parts: `template`, `script`, and `style` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Components are represented as plain JavaScript objects <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Reactive State**: Defined using the `data` property on the component object <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **State Modification**: Handled by methods defined in the `methods` property <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Application Lifecycle**: Tapped into using methods like `mounted`, which is called when the component is first initialized <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Templating**: Similar to Angular, Vue uses directives in its template, such as `v-for` for looping over items <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Event Handling**: `v-on:submit` handles form submissions <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. A convenient feature is the ability to add `.prevent` to the directive (e.g., `v-on:submit.prevent`) to automatically prevent default behavior <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Two-way Data Binding**: The `v-model` directive binds the form input value to a data property <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

Vue is known for its developer-friendly features and large community <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Svelte

Svelte is another independent option, recognized as the most loved framework in the 2021 Stack Overflow survey, with about 50,000 GitHub stars <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   **Design**: Minimal library that relies on the open-source community for features like routing <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **Unique Aspect**: Unlike other frameworks, Svelte doesn't ship a runtime (like a virtual DOM) to the browser <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. Instead, it acts as a compiler, transforming your code into plain JavaScript during the build process <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Development**: When starting a new project, you may need to understand module bundlers like Rollup or Webpack <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

#### Implementation Details
*   **Components**: Defined in `.svelte` files, structured with a script, template, and styles section <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Reactive State**: Achieved by simply declaring a variable with the `let` keyword <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. State modification is done via plain JavaScript functions, which feels very natural with minimal abstractions <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   **Application Lifecycle**: The `onMount` function (imported from Svelte) allows registering a callback for when the component is first initialized <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Templating**: Uses a special syntax, such as `{#each}` to loop over arrays <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Event Handling**: `on:submit` handles form submissions <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Similar to Vue, it supports event modifiers like `|preventDefault` directly in the template <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   **Two-way Data Binding**: Uses the `bind:value` directive <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

Svelte is praised for its clean implementation and readability, often requiring fewer lines of code <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. However, its community is much smaller than React's, which can lead to more challenges when seeking support or specific libraries <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

### Lit

Lit is a Google-sponsored project focused on building web components <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   **Web Components**: Web components are a browser standard for creating reusable custom elements that can work across multiple frameworks <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. The native Web Components API is known for being difficult to work with <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Design**: Lit simplifies the process, creating standard custom elements under the hood <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. While other frameworks can produce web components, it's often an afterthought with a less ideal developer experience <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Tooling**: Lit doesn't have its own CLI, but starter projects are available (with optional TypeScript) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. It directly interacts with the browser's `window.customElements` API <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

#### Implementation Details
*   **Components**: Defined as classes that extend `LitElement` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Reactive Data**: Defined as properties on the class using the `@property` decorator <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Methods are defined on the class to update state <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Application Lifecycle**: Hooks are based on the Web Components API, such as `connectedCallback` for when the component is first initialized <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   **Templating**: Lit uses existing JavaScript template literals (strings with backticks) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This allows JavaScript interpolation into HTML strings using `$` and braces, similar to JSX <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   **Event Binding**: HTML can have directives like `submit` or `.value` for event binding or input values <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Data Binding**: Does not appear to support two-way data binding, requiring a separate event listener on the input's `change` event to update state <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

Lit provides a more pleasant way to build standard web components without needing deep expertise in the underlying APIs <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Stencil

Stencil is another framework focused on web components, developed by the team behind the Ionic framework <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Purpose**: Ionic, a component library for mobile development, is built with Stencil to ensure compatibility with React, Angular, and Vue out of the box <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Tooling**: New apps are created using `npm init stencil`, which sets up a TypeScript project <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   **Compiler**: Like Lit, Stencil compiles each component down to a standard web component <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

#### Implementation Details
*   **Components**: A class with a `@Component` decorator, similar to Angular <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **Reactive Data**: Defined as properties using the `@State` decorator <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Custom methods update the state <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
*   **Application Lifecycle**: Uses hooks like `componentWillLoad` to run code when the component is first initialized <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Templating**: Uses JSX, like React <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.
*   **Data Binding**: Does not appear to support two-way data binding, necessitating an `onInput` event listener to update the text when the user types <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

Stencil is another strong choice for building web components <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

### SolidJS

SolidJS is a UI component building tool that is inspired by React but does not use the virtual DOM <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Design**: Compiles code down to native DOM nodes, similar to Svelte <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This approach leads to very high performance scores across benchmarks <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.
*   **Comparison**: Often described as a faster, more developer-friendly version of React <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
*   **Drawback**: Has a smaller community compared to more established frameworks <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Tooling**: Uses Vite as its build tool for new projects <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

#### Implementation Details
*   **Components**: Defined in JSX files, just like React, and are represented as functions <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
*   **Reactive State**: Uses "signals," which are similar to React hooks, returning a reactive value and an update function <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **State Modification**: A plain function can be defined to update the state <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Application Lifecycle**: Uses the `onMount` hook, which is more readable than React's `useEffect`, to run code when the component is first initialized <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   **Templating**: Uses JSX, which looks almost identical to React code <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
*   **Form Input**: Simplifies form binding with a `ref` attribute to link a form value to a variable, without needing a dedicated hook like `useRef` in React <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

SolidJS aims to provide a more streamlined and performant experience than React <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### Alpine.js

Alpine.js is a tiny library (around 4 kilobytes) designed to extend existing HTML with reactive data and features found in larger frameworks <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.
*   **Design Philosophy**: Primarily focuses on augmenting HTML, similar to how [[integrating_tailwind_css_with_javascript_frameworks | Tailwind CSS]] functions for CSS <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. It's a popular replacement for jQuery <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.
*   **Popularity**: Has over 17,000 GitHub stars <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   **Setup**: Requires including the Alpine script tag in an HTML file <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

#### Implementation Details
*   **Reactive Data**: Stored directly in a DOM node using the `x-data` attribute <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   **Templating**: Data can be used in child elements with attributes like `x-for` to loop over arrays <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   **Event Handling**: `x-on:submit` handles form submissions and can include `.prevent` to avoid default behavior <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. Concepts are similar to other frameworks but applied directly within raw HTML <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
*   **State Sharing**: Alpine Store allows storing and sharing data between multiple components, useful for loading data from local storage <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Application Lifecycle**: The `document.addEventListener` for the custom `alpine:init` event handles initialization code <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

Alpine is an excellent choice for adding light JavaScript interactivity to existing HTML pages <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. However, it's generally not suitable for building complex single-page applications where frameworks like React, Vue, or Angular would be more appropriate <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

### Mithril

Mithril is a lightweight framework that often outperforms larger frameworks <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   **Design**: Uses a virtual DOM like React and Vue, but with a distinct developer experience <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.
*   **Setup**: Requires including the Mithril script tag in an HTML file <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

#### Implementation Details
*   **Components**: Can be created from functions, classes, or plain JavaScript objects <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. Data and methods are added as properties on the object <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   **Application Lifecycle**: Uses special properties like `oninit` as a lifecycle hook for component initialization <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   **UI Definition**: The `view` property defines the UI <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. DOM nodes are defined using the `m` function, passing the node name as the first argument and options (like class name) or children as the second <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   **Templating**: Results in UI that is truly defined in pure JavaScript, which might appeal to developers who prefer to avoid HTML <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
*   **Event Handling**: Handlers for events like `onsubmit` are defined on the form element <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.

Mithril's approach to UI definition can feel awkward to some, but its pure JavaScript approach may appeal to others <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

### Conclusion

This [[comparison_with_other_javascript_frameworks | comparison of popular JavaScript frameworks in 2021]] demonstrates that while new frameworks constantly emerge <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>, they all perform the same basic functions <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. The choice ultimately comes down to personal preference and what works best for you and your team <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.