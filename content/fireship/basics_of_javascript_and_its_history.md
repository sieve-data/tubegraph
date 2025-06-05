---
title: Basics of JavaScript and its history
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

[[javascript_fundamentals_and_practical_concepts | JavaScript]] is a versatile programming language that can be both challenging and rewarding for beginners <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it allows developers to build a wide array of applications and secure jobs, it's also noted for its quirks and the complex ecosystem of [[emergence_of_frameworks_and_tools_in_modern_javascript | frameworks and libraries]] surrounding it <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## [[history_and_evolution_of_javascript | History]]

[[history_and_evolution_of_javascript | JavaScript]] was created in 1993 by [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Brendan Eich]] at [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Netscape]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Its initial purpose was to make websites, which were purely static HTML at the time, interactive <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. It was designed as an easy-to-use, high-level language <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Today, it is arguably the most popular programming language globally <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Its standardized implementation is known as [[standardization_of_javascript_and_the_ecmascript_specification | ECMAScript]], and it is the default language in all web browsers <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. In fact, it is the only code that natively runs in a browser, aside from Web Assembly <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## [[using_javascript_on_web_and_server_environments | Where JavaScript Runs]]

While primarily known for its role in web browsers, [[javascript_fundamentals_and_practical_concepts | JavaScript]] is not limited to that environment <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. It can also be run on a server, thanks to tools like Node.js and Deno <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This capability extends to building:

*   Websites <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>
*   Mobile applications (e.g., with React Native) <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a> <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>
*   Desktop applications (e.g., with Electron, which combines Node.js with a browser runtime) <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>
*   Server-side applications <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>

## [[javascript_fundamentals_and_practical_concepts | Core Concepts]]

### Scripting Language and Execution

[[javascript_fundamentals_and_practical_concepts | JavaScript]] is a scripting language, meaning code can be executed on the fly <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This can be demonstrated by opening the console in browser developer tools and running code that modifies a website's appearance <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

While often described as interpreted (line-by-line execution), a more accurate term is that it undergoes Just In Time (JIT) compilation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Under the hood of browsers, an engine like V8 converts [[javascript_fundamentals_and_practical_concepts | JavaScript]] code to machine code, enabling extremely fast execution <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Basic Web Integration

To use [[javascript_fundamentals_and_practical_concepts | JavaScript]] on a webpage, you typically include it within an HTML document using a `<script>` tag <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Code can be written directly inside this tag or linked from an external file using the `source` attribute <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

The `console.log()` function is a built-in tool for printing output to the standard output, visible in the browser's developer tools console <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Variables

[[javascript_fundamentals_and_practical_concepts | JavaScript]] offers several ways to define variables:

*   `let`: The most common method today <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Variables declared with `let` can be reassigned later <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   `const`: Used for variables whose values should not be reassigned after their initial declaration <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   `var`: The original way to declare variables. It's generally recommended to avoid `var` due to its less predictable scoping behavior <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

[[javascript_fundamentals_and_practical_concepts | JavaScript]] is a dynamically typed language, meaning data type annotations are not necessary <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. It includes seven primitive data types, such as numbers and strings <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Variables can be explicitly assigned `null` for an empty value or default to `undefined` if not initialized <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Any value that is not a primitive will inherit from the `Object` class <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

Semicolons at the end of statements are technically optional in [[javascript_fundamentals_and_practical_concepts | JavaScript]], as the parser automatically adds them <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Scope

The "lexical environment" determines where variables are accessible:

*   **Global scope**: Variables are available everywhere in the program <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Function scope**: Variables defined inside a [[javascript_function_basics_and_anatomy | function]] are local to that [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Block scope**: Variables declared with `let` or `const` inside a block (e.g., `if` statement braces) are scoped to that block <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. `var` declarations, however, are not block-scoped and are "hoisted" to the nearest [[javascript_function_basics_and_anatomy | function]] scope <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### [[javascript_function_basics_and_anatomy | Functions]]

[[javascript_function_basics_and_anatomy | Functions]] are fundamental building blocks in [[javascript_fundamentals_and_practical_concepts | JavaScript]] <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. They take input (arguments) and can optionally return a value <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

*   **Function Definitions/Statements**: Declared using the `function` keyword by itself <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Function Expressions**: [[javascript_function_basics_and_anatomy | Functions]] can be treated as objects and assigned to variables or used to construct higher-order functions (where a [[javascript_function_basics_and_anatomy | function]] is passed as an argument or returned) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Closures**: [[javascript_function_basics_and_anatomy | Functions]] can be nested to create closures, which encapsulate data and logic from the rest of the program <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. This allows inner functions to access variables from their outer [[javascript_function_basics_and_anatomy | function]] even after the outer [[javascript_function_basics_and_anatomy | function]] has finished executing, as the data is stored in Heap memory <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **`this` Keyword**: A keyword that references an object based on how a [[javascript_function_basics_and_anatomy | function]] is called <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Its value can change depending on the context (global scope, attached to an object, or manually bound) <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Arrow Functions**: A modern syntax for defining [[javascript_function_basics_and_anatomy | functions]] that do not have their own `this` value and are always anonymous, making them ideal for [[javascript_function_basics_and_anatomy | function]] expressions <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Passing Arguments**: Primitive values (like numbers) are passed by value (a copy is created), while objects are passed by reference (multiple parts of the code can mutate the same object) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Objects

Objects are a core concept in [[javascript_fundamentals_and_practical_concepts | JavaScript]].

*   **Definition**: The easiest way to define an object is with the object literal syntax using braces `{}` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Objects can also be created with a constructor using the `new` keyword <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Properties**: An object contains a collection of key-value pairs <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Prototypal Inheritance**: Objects can inherit properties from each other through the "Prototype chain" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Every object has a private property linking to exactly one prototype, differing from class-based inheritance in other languages <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Classes**: [[javascript_fundamentals_and_practical_concepts | JavaScript]] supports object-oriented programming with the `class` keyword <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Classes are syntactic sugar for prototypal inheritance and objects, providing a more structured way to define constructors, properties, getters, setters, and methods (instance or static) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### Data Structures

In addition to objects, [[javascript_fundamentals_and_practical_concepts | JavaScript]] includes built-in data structures:

*   **Array**: Holds a dynamic collection of indexed items <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Set**: Holds a collection of unique items <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Map**: Holds key-value pairs, similar to objects, but can be more easily iterated over <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **WeakMap** and **WeakSet**: Contain properties that can be garbage collected, optimizing memory usage <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Memory Management

[[javascript_fundamentals_and_practical_concepts | JavaScript]] uses garbage collection, meaning it automatically deallocates objects from memory when they are no longer referenced in the code <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Asynchronous [[javascript_fundamentals_and_practical_concepts | JavaScript]] (Non-blocking Event Loop)

Normally, [[javascript_fundamentals_and_practical_concepts | JavaScript]] code executes synchronously, line by line <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. However, [[javascript_fundamentals_and_practical_concepts | JavaScript]]'s non-blocking event loop allows for asynchronous code execution in a separate thread pool, enabling the rest of the application to continue running <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This is crucial for modern websites that perform multiple tasks simultaneously on a single "main thread" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

*   **Callbacks**: A common way to handle asynchronous operations. For example, `setTimeout` takes a [[javascript_function_basics_and_anatomy | function]] that is called after a specified delay <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Deeply nested callbacks can lead to "callback hell" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Promises**: A better way to write asynchronous code <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. A promise is a wrapper for a value that will resolve (succeed) or reject (fail) in the future <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Consumers use `.then()` for resolution and `.catch()` for rejection <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **`async/await`**: A modern syntax built on Promises, allowing asynchronous code to be written in a more readable, synchronous-like style <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. An `async` [[javascript_function_basics_and_anatomy | function]] automatically returns a promise, and `await` pauses execution until another promise resolves <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Error handling is managed with `try/catch` blocks <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

### Modules

As code complexity grows, [[javascript_fundamentals_and_practical_concepts | JavaScript]] allows sharing code between files using modules <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. By default, code within a file is private to that module <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Code intended for external use can be made a `default export` or multiple values can be exported by name, then imported into other files using `import` statements <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Package Management

The largest [[javascript_fundamentals_and_practical_concepts | JavaScript]] package manager is npm (Node Package Manager) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. When a package is installed via npm, its code is downloaded into the `node_modules` folder <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. A `package.json` file lists all project dependencies <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

### Document Object Model (DOM) Interaction

On the web, [[javascript_fundamentals_and_practical_concepts | JavaScript]] interacts with the Document Object Model (DOM), which represents the UI as a tree of HTML elements <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The browser provides APIs to interact with these "nodes," with the `document` object being the most important <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

*   `querySelector()`: Used to grab an individual HTML element by a CSS selector (class name, ID, or tag name) <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. It returns an instance of the element class, which has properties and methods to get information or change behavior <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   `querySelectorAll()`: Used to grab multiple elements at once <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   `addEventListener()`: Allows listening to events (like a button click) on an element and assigning a [[javascript_function_basics_and_anatomy | function]] to be called when that event occurs <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### [[emergence_of_frameworks_and_tools_in_modern_javascript | UI Development Trends]]

Vanilla [[javascript_fundamentals_and_practical_concepts | JavaScript]] for UI often results in imperative code, where the UI is directly mutated <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. Many developers now use front-end [[emergence_of_frameworks_and_tools_in_modern_javascript | frameworks]] that produce declarative code, where the UI is a [[javascript_function_basics_and_anatomy | function]] of its input data <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. These libraries encapsulate [[javascript_fundamentals_and_practical_concepts | JavaScript]], HTML, and CSS into components, which form a component tree <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. Data within components is reactive, automatically updating the UI when changes occur <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

### Build Tools

After building a [[javascript_fundamentals_and_practical_concepts | JavaScript]] application, files often need to be combined into a single bundle for browser use <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Tools like module bundlers (e.g., Vite or Webpack) handle this process <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. To improve page load performance for large bundles, it's possible to split the bundle into multiple files and use dynamic imports to load [[javascript_fundamentals_and_practical_concepts | JavaScript]] only when needed <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

### Code Quality Tools

To improve code quality and make development easier, tools like TypeScript (for static analysis and type checking) or ESLint (for linting and code style enforcement) can be used <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.