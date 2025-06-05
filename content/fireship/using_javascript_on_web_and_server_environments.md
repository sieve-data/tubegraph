---
title: Using JavaScript on web and server environments
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

[[Basics of JavaScript and its history | JavaScript]] is a versatile programming language suitable for beginners, despite some perceived complexities and its ecosystem of frameworks and libraries <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Mastering it can enable developers to build almost anything and secure jobs in various fields <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Historical Context and Design Philosophy
[[History and evolution of JavaScript | JavaScript]] was created in 1993 by Brendan Eich at Netscape <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. At the time, web browsers were cutting-edge technology connecting people globally via the World Wide Web <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Websites were primarily static HTML documents <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. [[Basics of JavaScript and its history | JavaScript]] was designed as an easy-to-use, high-level language to make these websites interactive <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Today, it is arguably the most popular language globally <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Its standard implementation is known as [[Standardization of JavaScript and the ECMAScript specification | ECMAScript]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## [[Running JavaScript in various environments | Running JavaScript on the Web (Browser)]]
[[Influence of browsers and companies on JavaScripts development | JavaScript]] is the default language in all web browsers and is the only code that natively runs in a browser, aside from WebAssembly <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Core Concepts in the Browser
*   **Scripting Language**: [[Basics of JavaScript and its history | JavaScript]] is a scripting language, meaning code can be executed on the fly, for example, by opening the console in browser DevTools to change a website's appearance <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Execution**: While often described as interpreted, [[Basics of JavaScript and its history | JavaScript]] runs extremely fast in the browser thanks to engines like V8, which convert code to machine code using Just-in-Time (JIT) compilation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Embedding in HTML**: To use [[Basics of JavaScript and its history | JavaScript]] on a webpage, code can be written directly within a `<script>` tag in an HTML document or linked via an external file using the `source` attribute <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. `console.log` is a built-in tool for printing to standard output, visible in browser DevTools <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Document Object Model (DOM)**: On the web, [[Basics of JavaScript and its history | JavaScript]] interacts with the browser's Document Object Model (DOM), which represents the UI as a tree of HTML elements or nodes <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   **APIs**: The browser provides APIs to interact with these nodes, with the `document` object being central <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
    *   **Element Selection**: Methods like `querySelector` (using CSS selectors) and `querySelectorAll` can retrieve HTML elements <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   **Event Handling**: `addEventListener` allows listening for events (e.g., button clicks) on elements and assigning functions to be called when these events occur <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **[[JavaScript and Frontend Development | Frontend Development]]**: Much of web development involves listening to events and updating the UI <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
    *   **Imperative vs. Declarative**: While vanilla [[Basics of JavaScript and its history | JavaScript]] often leads to imperative code (directly mutating the UI), many developers now use [[JavaScript trends and frameworks | front-end frameworks]] that produce declarative code, where the UI is a function of its input data <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   **Components**: These libraries encapsulate [[Basics of JavaScript and its history | JavaScript]], HTML, and CSS into components that form a component tree for the UI <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   **Reactivity**: Data within a component is reactive, meaning the UI automatically updates when data changes <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **Module Bundling**: After building a [[JavaScript and Frontend Development | JavaScript]] application, files are often combined into a single bundle for browser use <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Module bundlers like Vite or Webpack handle this process <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
    *   **Performance**: Large [[Basics of JavaScript and its history | JavaScript]] bundles can affect page load performance <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. Dynamic Imports can split bundles into multiple files, importing [[Basics of JavaScript and its history | JavaScript]] only when needed to improve performance <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## [[Running JavaScript in various environments | Running JavaScript on the Server]]
[[Running JavaScript in various environments | JavaScript]] also runs on the server <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   **Node.js**: Node.js is the most popular runtime for server-side [[Running JavaScript in various environments | JavaScript]], allowing execution of [[Basics of JavaScript and its history | JavaScript]] code using the `node` command <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Deno**: Deno is another tool that allows [[Running JavaScript in various environments | JavaScript]] code to run on a server <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Cross-Platform Applications**: Server-side [[Running JavaScript in various environments | JavaScript]] enables building:
    *   Full-stack desktop applications with [[JavaScript trends and frameworks | frameworks]] like Electron (combining Node.js with a browser) <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
    *   iOS and Android mobile applications with [[JavaScript trends and frameworks | frameworks]] like React Native <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

## Fundamental [[Basics of JavaScript and its history | JavaScript]] Concepts (Applicable to Both Environments)

### Variables
*   **Declaration**: Variables can be defined using `let`, `const`, or `var` <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. `let` is common for reassignable variables, while `const` is for variables that cannot be reassigned <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. `var` is an older method that should generally be ignored <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Dynamic Typing**: [[Basics of JavaScript and its history | JavaScript]] is a dynamically typed language, meaning data type annotations are not necessary <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. A variable can be reassigned to a different data type <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Primitive Data Types**: [[Basics of JavaScript and its history | JavaScript]] has seven built-in primitive data types (e.g., number, string) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. `undefined` is the default value for unassigned variables <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, while `null` explicitly represents an empty value <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Semicolons**: Semicolons are technically optional in [[Basics of JavaScript and its history | JavaScript]] as the parser automatically adds them, though their usage is a debated topic among developers <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Scope
The lexical environment determines where variables are accessible <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Global Scope**: Variables defined globally are available everywhere <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Local (Function) Scope**: Variables defined inside a function are local to that function and cannot be used outside it <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Block Scope**: Variables can be scoped within block statements (e.g., `if` conditions) if declared with `let` or `const` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. `var` is not block-scoped and will be "hoisted" to the local function scope <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Functions
Functions are fundamental building blocks that take inputs (arguments) and optionally return values <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Definitions vs. Expressions**: When used by itself, it's a function definition or statement <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. As objects, functions can also be used as expressions (e.g., assigned to variables) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Higher-Order Functions**: Functions can be arguments or return values of other functions <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Closures**: Nested functions can create closures, encapsulating data and logic <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. An inner function in a closure can access variables from its outer function even after the outer function has completed execution, as the data is stored in Heap memory <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **`this` Keyword**: The `this` keyword references an object based on how a function is called <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   In global scope, `this` references the `window` object in browsers <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   If a function is attached to and called by an object, `this` refers to that object <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   Functions can be manually bound to objects using the `bind` method <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Arrow Functions**: Modern [[Basics of JavaScript and its history | JavaScript]] offers arrow syntax for functions, which do not have their own `this` value and are always anonymous, making them ideal for function expressions <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Argument Passing**: Primitives (like numbers) are passed by value (a copy is created), while objects are passed by reference (multiple parts of the code can mutate the same object) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Objects and Data Structures
*   **Objects**: The easiest way to define an object is with the object literal syntax using braces <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Objects contain key-value pairs (properties and values) <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   **Prototype Chain**: Objects can inherit properties from each other via the prototype chain <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This differs from class-based inheritance in other languages as it deals with real objects in memory <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   **Classes**: [[Basics of JavaScript and its history | JavaScript]] supports object-oriented programming with the `class` keyword, which is syntactic sugar for prototypal inheritance and objects <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Classes can define constructors, properties, getters, setters, and organize functions as methods <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. `static` methods are global to the class name <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Built-in Data Structures**: [[Basics of JavaScript and its history | JavaScript]] includes:
    *   `Array`: For dynamic collections of indexed items <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
    *   `Set`: To hold unique items <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
    *   `Map`: Holds key-value pairs like objects but is more easily iterable <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Garbage Collection**: [[Basics of JavaScript and its history | JavaScript]] is garbage collected, meaning objects are automatically deallocated from memory when no longer referenced <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. `WeakMap` and `WeakSet` exist for properties that can be garbage collected to reduce memory usage <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Asynchronous JavaScript
[[Basics of JavaScript and its history | JavaScript]] features a non-blocking event loop <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Synchronous vs. Asynchronous**: Code is typically executed synchronously line by line <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The event loop allows asynchronous code to run in a separate threadpool while the main application continues, crucial for modern websites that multitask with only a single main thread <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Callbacks**: `setTimeout` demonstrates callbacks, where a function is queued in the event loop to be called later on the main thread <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Overuse can lead to "callback hell" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Promises**: A better way to write asynchronous code <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. A promise is a wrapper for a value that will resolve in the future (e.g., from an API call) or reject if an error occurs <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Consumers use `.then()` and `.catch()` methods to handle outcomes <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Async/Await**: An `async` function automatically returns a promise <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. The `await` keyword can pause execution within an `async` function until other promises resolve, resulting in more readable code <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Error handling is typically done with a `try...catch` block <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

### Modules and Package Management
*   **Modules**: Modules allow sharing code between files <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. By default, code in a module is private, but functions or values can be made available using `export` (e.g., `default export` or named exports) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Other files can then use `import` statements to utilize this code <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **NPM**: The largest [[Basics of JavaScript and its history | JavaScript]] package manager is npm <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Installing a package from npm downloads its code into the `node_modules` folder, and a `package.json` file lists project dependencies <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## Quality Control and Future Trends
Tools like [[Alternatives and complements to JavaScript | TypeScript]] or ESLint perform static analysis to improve [[Basics of JavaScript and its history | JavaScript]] code quality <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.