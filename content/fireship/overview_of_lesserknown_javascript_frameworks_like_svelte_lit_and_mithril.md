---
title: Overview of lesserknown JavaScript frameworks like Svelte Lit and Mithril
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 

Choosing a [[choosing_the_right_javascript_framework_for_your_project | JavaScript framework]] can be challenging, especially with the continuous emergence of new options <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While popular frameworks like React and Angular dominate the landscape, several lesser-known, yet powerful, options offer unique approaches to web development. This article explores Svelte, Lit, Stencil, SolidJS, Alpine.js, and Mithril.

## Svelte

Svelte is an independently developed [[javascript_for_interactivity_and_frameworks | JavaScript framework]] that gained significant affection, being named the most loved framework in the 2021 Stack Overflow survey <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. It has approximately 50,000 GitHub stars <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Key Characteristics
*   **Compiler, Not a Runtime**: Unlike many frameworks that ship a runtime (like a virtual DOM) to the browser, Svelte functions as a compiler <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. It translates your code into plain [[javascript_for_interactivity_and_frameworks | JavaScript]] at build time, resulting in smaller bundle sizes and faster performance <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Minimal Library**: Svelte is designed to be minimal, relying on the open-source community for additional features like routing <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **Project Structure**: Components are defined in `.svelte` files, which are typically organized into three parts: the script (for [[javascript_for_interactivity_and_frameworks | JavaScript]] logic), the template (for HTML), and the styles (for CSS) <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. When creating a new project, you might encounter Rollup or Webpack configurations, requiring some understanding of [[javascript_package_management_and_libraries | module bundlers]] <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Development Paradigm
*   **Reactive State**: To create reactive state, you simply declare a variable using the `let` keyword <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. State modifications occur within plain [[javascript_for_interactivity_and_frameworks | JavaScript]] functions <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. This approach aims for a natural feel with minimal abstractions <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
*   **Lifecycle Hooks**: Svelte provides lifecycle hooks like `onMount`, which can be imported and used to register a callback function that runs when the component is first initialized <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Templating and Event Handling**: Svelte templates feature a special syntax for looping over data, such as the `each` block <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Event handling uses `on:submit`, and modifiers like `.preventdefault` can be directly appended to prevent default browser behavior <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   **Two-Way Data Binding**: Implemented easily using the `bind:value` directive <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

### Advantages and Disadvantages
Svelte offers a very clean implementation with fewer lines of code and is relatively easy for [[javascript_for_interactivity_and_frameworks | JavaScript]] developers to pick up <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. However, its community is smaller than that of React or Angular, which can lead to challenges in finding supporting libraries or job opportunities <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Lit

Lit is a Google-sponsored project primarily focused on building web components <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Web components are a browser standard allowing the creation of custom elements that can function across multiple [[frontend_ui_libraries_and_frameworks | frameworks]] <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. Lit simplifies the process of working with the web components API, which can be difficult to use directly <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

### Key Characteristics
*   **Web Component Focus**: When you define a component in Lit, it creates a standard custom element under the hood <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **No Official CLI**: Lit does not have its own CLI; instead, developers typically use a starter project <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   **Project Structure**: The main application file (`lit-app.ts`) often shows calls to `window.customElements`, which is part of the browser's web components API <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. Components are defined as classes that extend `LitElement` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

### Development Paradigm
*   **Reactive Data**: Reactive data is defined as properties on the class, often using the `@property` decorator <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Methods are defined on the class to update this state <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Lifecycle Hooks**: Lifecycle hooks in Lit are based on the web components API, such as `connectedCallback`, which runs code when the component is first initialized <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Templating**: Lit leverages [[javascript_for_interactivity_and_frameworks | JavaScript's]] existing template literals (strings with backticks) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This allows for interpolation of [[javascript_for_interactivity_and_frameworks | JavaScript]] expressions into HTML strings using `${}` <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>, resulting in a feel similar to JSX in React <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Event Handling and Data Binding**: HTML elements can have directives like `@submit` or `.value` to bind to form events or input values <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. Lit does not natively support two-way data binding, so event listeners (e.g., `oninput`) must be manually set up to update state <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

### Advantages
Lit provides a significantly improved way to build standard web components without requiring deep expertise in the underlying browser APIs <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

## Stencil

Stencil, developed by the team behind the Ionic [[frontend_ui_libraries_and_frameworks | framework]], is another [[frontend_ui_libraries_and_frameworks | framework]] focused on web components <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Ionic itself is a component library for mobile development built with Stencil, utilizing web components for compatibility with frameworks like React, Angular, and Vue <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

### Key Characteristics
*   **Web Component Compilation**: Similar to Lit, Stencil compiles each component down to a standard web component <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
*   **Project Creation**: A new app can be created by running `npm init stencil`, which provides a TypeScript project <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

### Development Paradigm
*   **Component Definition**: Components are defined as TypeScript classes with a `@Component` decorator, resembling Angular components <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **Reactive Data**: Reactive data is defined as properties using the `@State` decorator <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Custom methods are defined to update this state <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   **Lifecycle Hooks**: Stencil offers lifecycle hooks like `componentWillLoad`, which runs code when the component is first initialized <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Templating**: For templating, Stencil uses JSX, similar to React <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.
*   **Data Binding**: It does not appear to support two-way data binding, requiring manual event listeners (e.g., `onInput`) to update the text when the user types <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

## SolidJS

SolidJS is a [[frontend_ui_libraries_and_frameworks | framework]] for building UI components that takes inspiration from React but with a crucial distinction: it does not use a virtual DOM <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. Instead, it compiles code directly down to native DOM nodes, similar to Svelte <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

### Key Characteristics
*   **Performance**: Due to its compilation to native DOM nodes, SolidJS achieves very high performance marks across various benchmarks <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **Developer Experience**: It's often described as a faster, more developer-friendly version of React <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
*   **Community**: The main drawback is its smaller community compared to more established frameworks <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Build Tool**: New projects generated with SolidJS utilize Vite as the build tool <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

### Development Paradigm
*   **Component Definition**: Components are defined as functions within JSX files, much like React <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
*   **Reactive State**: Reactive state is managed using "signals," which are similar to React hooks <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. A signal returns a reactive value and a function to update it <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
*   **Lifecycle Hooks**: SolidJS provides a more readable `onMount` hook, which runs when the component is first initialized, serving the same purpose as React's `useEffect` <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   **Templating and Data Binding**: The UI is built using JSX, which looks almost identical to React code <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. SolidJS simplifies certain aspects, such as binding form values to a variable using `ref` without needing to import a `useRef` hook <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

## Alpine.js

Alpine.js is a lightweight library, around 4 kilobytes in size, designed to add [[javascript_for_interactivity_and_frameworks | JavaScript interactivity]] to existing HTML <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. It allows developers to extend HTML with reactive data and features commonly found in larger frameworks <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.

### Key Characteristics
*   **HTML-Centric**: Alpine.js emphasizes working primarily with HTML, rather than focusing on separate [[javascript_for_interactivity_and_frameworks | JavaScript]] files <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. It's often compared to [[integrating_tailwind_with_componentbased_javascript_frameworks | Tailwind CSS]] for [[javascript_for_interactivity_and_frameworks | JavaScript]] <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
*   **Popularity**: It has over 17,000 GitHub stars and is a popular replacement for jQuery <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Simple Setup**: To get started, you simply include the Alpine script tag in your HTML file's head <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

### Development Paradigm
*   **Reactive Data**: Reactive data can be directly stored within a DOM node using the `x-data` attribute <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
*   **Templating and Event Handling**: Data can be used in child elements with directives like `x-for` for looping <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. Event handling is done via `x-on:submit`, with `.prevent` available to prevent default behavior <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. The concepts are similar to other frameworks but applied directly to raw HTML <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Plain [[javascript_for_interactivity_and_frameworks | JavaScript]] and State Management**: Plain [[javascript_for_interactivity_and_frameworks | JavaScript]] can be written in a script tag. Alpine also offers `Alpine.store` for storing and sharing data across multiple components <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Lifecycle**: To handle component initialization, `document.addEventListener` can be used for the custom `alpine:init` event <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### Use Case
Alpine.js is an excellent choice when you need to add a small amount of [[javascript_for_interactivity_and_frameworks | JavaScript interactivity]] to an existing HTML page <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. However, it may not be suitable as a replacement for more comprehensive single-page application frameworks like React, Vue, or Angular <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

## Mithril

Mithril is another lightweight [[frontend_ui_libraries_and_frameworks | framework]] that often outperforms larger frameworks <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. It uses a virtual DOM, similar to React and Vue, but offers a distinct developer experience <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

### Key Characteristics
*   **Lightweight and Performant**: Mithril is known for its small size and efficient performance <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   **Setup**: To begin, you create an `index.html` file and include the Mithril script tag <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

### Development Paradigm
*   **Component Definition**: Components can be created from functions, classes, or plain [[javascript_for_interactivity_and_frameworks | JavaScript]] objects <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. Data and methods are added as properties on the object <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   **Lifecycle Hooks**: Special properties like `oninit` serve as lifecycle hooks, executing when the component is first initialized <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   **Templating**: The UI is defined using the `view` property. DOM nodes are created with the `m` function, which takes the node name as the first argument, and options (like class names) or children as subsequent arguments <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. This approach defines the UI purely in [[javascript_for_interactivity_and_frameworks | JavaScript]], offering a JSX-like feel <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.
*   **Event Handling**: Handlers for events like `onsubmit` are defined directly on the form element <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.

### Considerations
Mithril's system might appeal to developers who prefer to define UI entirely in [[javascript_for_interactivity_and_frameworks | JavaScript]] and avoid HTML <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. However, some developers might find its paradigm awkward or challenging to learn <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

Ultimately, the "best" [[comparison_of_javascript_frameworks | JavaScript framework]] is subjective and depends on individual preference and project needs <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. All these frameworks are capable of building the same basic applications <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>; the choice comes down to what makes you and your team most productive and satisfied <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.