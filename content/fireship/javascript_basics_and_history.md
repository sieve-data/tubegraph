---
title: JavaScript basics and history
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

[[JavaScript language quirks | JavaScript]] is a versatile programming language that allows developers to build a wide range of applications, from websites to mobile and desktop apps, servers, and even AI, though some uses are not ideal for it <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. It is both praised for its capabilities and criticized for its "weird" aspects and "dystopian Wasteland of Frameworks and libraries" <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## [[history_of_javascript | History of JavaScript]]

[[JavaScript language quirks | JavaScript]] was created in 1993 by Brendan Eich at Netscape <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. At the time, web browsers were new technology, and websites were entirely static, built with pure HTML <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. JavaScript was designed as an easy-to-use, high-level language to help developers make these websites interactive <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Today, JavaScript is arguably the most popular language in the world <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Its standard implementation is called ECMAScript, and it is the default and only code that natively runs in all web browsers, aside from WebAssembly <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Runtimes and Execution

While primarily known for its use in browsers, JavaScript can also run on a server thanks to tools like Node.js and Deno <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

JavaScript is a scripting language, meaning code can be executed on the fly, for instance, by opening the browser's console in DevTools <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It is interpreted line by line, unlike compiled languages like C <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. However, the term "interpreted" isn't fully accurate, as browser engines like V8 optimize JavaScript by converting it to machine code using Just-in-Time (JIT) compilation, making it run extremely fast <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

To use JavaScript on a web page, you need an HTML document with a `<script>` tag, where code can be written directly or linked from an external file via the `src` attribute <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. `console.log` is a built-in tool for printing values to the standard output, visible in the browser's DevTools <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## [[Variables and data types in JavaScript | Variables and Data Types]]

[[Variables and data types in JavaScript | Variables]] are fundamental to JavaScript.

### Variable Declaration

The most common way to define a variable today is using `let` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Variables are typically named in camelCase <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. JavaScript is a dynamically typed language, meaning data type annotations are not necessary <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Another common option is `const`, used for variables that cannot be reassigned after their initial declaration <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The original way to declare a variable was `var`, but it is generally recommended to ignore its existence due to its quirky behavior <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

### Primitive Data Types

JavaScript has seven primitive data types <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:
*   **Numbers** <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Undefined**: The default value for a variable declared without an initial assignment <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Null**: Explicitly represents an empty value <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Strings** <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   Any value that is not a primitive inherits from the `Object` class <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Semicolons

Semicolons are technically optional in JavaScript, as the parser will automatically add them if omitted. However, their usage often sparks debate among developers <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Scope

The reason for different variable declaration methods is related to the lexical environment, which determines where variables are accessible <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>:
*   **Global scope**: Variables are available everywhere <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Function local scope**: Variables defined inside a function are local to that function and cannot be used outside it <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Block scope**: Variables declared with `let` or `const` inside a statement block (like an `if` condition) are scoped within those braces <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **`var` hoisting**: Variables declared with `var` are not block-scoped; they are hoisted up to the local function scope, which can lead to unexpected behavior <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## [[Functions and closures in JavaScript | Functions]]

[[Functions and closures in JavaScript | Functions]] are core building blocks in JavaScript <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Function Definitions and Expressions

When the `function` keyword is used alone, it's a function definition or statement <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Functions take input (arguments) and can optionally return a value <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Functions are also objects, allowing them to be used as expressions, assigned to variables, or passed as arguments to construct higher-order functions <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Closures

[[Functions and closures in JavaScript | Functions]] can be nested to create a closure, which encapsulates data and logic from the rest of the program <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. When a closure is created, the inner function can access variables from the outer function even after the outer function call, because JavaScript stores this data in the Heap memory, allowing it to persist <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### The `this` Keyword

The `this` keyword references an object based on how a function is called <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   Called from the global scope, `this` refers to the `window` object in browsers <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   If attached to an object and called by that object, `this` references that object <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   Functions can also be manually bound to an object using the `bind` method <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Arrow Functions

Modern JavaScript introduced arrow functions as another way to define functions <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Arrow functions do not have their own `this` value and are always anonymous, making them suitable for function expressions <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Pass by Value vs. Pass by Reference

*   When passing primitive arguments (like numbers) to a function, they are passed by value, meaning a copy of the original variable is created <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   If an argument is an object, it is stored in the Heap and passed by reference, meaning multiple parts of the code might be mutating the same object <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Objects and Data Structures

### Objects

Objects are fundamental for organizing data. The easiest way to define an object is with the object literal syntax using braces `{}` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. An `Object` type can also be created with a constructor using the `new` keyword <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

Objects contain collections of key-value pairs (properties and values) <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. They can inherit properties from each other through the Prototype chain, which differs from class-based inheritance found in other languages <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### Classes

JavaScript supports object-oriented programming with the `class` keyword <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Classes are syntactic sugar for prototypal inheritance and objects <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   A class can define a `constructor` function called when the object is first created <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   It can have properties and optionally create Getters and Setters <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   It helps encapsulate functions as methods on an object instance or make them global to the class name with the `static` keyword <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Built-in Data Structures

JavaScript includes several built-in data structures <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>:
*   **Array**: Holds a dynamic collection of indexed items <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Set**: Holds a collection of unique items <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Map**: Holds key-value pairs like an object but can be more easily looped over <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **WeakMap** and **WeakSet**: Contain properties that can be garbage collected to reduce memory usage, unlike regular Maps where all properties are always referenced <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Garbage Collection

JavaScript is garbage collected, meaning it automatically deallocates objects from memory when they are no longer referenced in the code <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

## Asynchronous JavaScript and the Event Loop

Normally, JavaScript code executes synchronously, line by line <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. However, JavaScript features a non-blocking event loop that allows for asynchronous code <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Asynchronous code runs in a separate thread pool while the main application continues to execute <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This is crucial for modern websites that have multiple things going on simultaneously but only access a single main thread for computing <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Callbacks

A common way to demonstrate asynchronous behavior is with `setTimeout`, which takes a function (a callback function) as an argument and calls it after a specified number of milliseconds <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Callbacks are cued in the event loop and executed on the main thread when ready <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Overuse and deep nesting of callbacks can lead to "callback hell" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Promises

Promises offer a better way to write async code <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. A promise is a wrapper for a value that will resolve to a value in the future (e.g., data from a third-party API) <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. It can `reject` to raise an error if something goes wrong <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Consumers of promises use `.then()` and `.catch()` methods to handle these outcomes <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Async/Await

Even better, an `async` function automatically returns a promise <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Inside an `async` function, the `await` keyword can pause execution to wait for other promises to resolve, resulting in more readable code <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Error handling with `async/await` is done by wrapping the code in a `try...catch` block <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Modularity and Ecosystem

### Modules

As code complexity grows, JavaScript files can be organized using modules to share code between files <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. By default, code in a module is private <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   A `default export` makes code (like a function) available for use in other files <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   An `import` statement is used to bring that exported code into another file <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   Multiple values can be exported from a single file and imported by name <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Package Management

Developers often use code written by others, managed through package managers <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. `npm` is the largest JavaScript package manager <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. When a package is installed from `npm`, its code is downloaded into the `node_modules` folder, and a `package.json` file lists all project dependencies <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## [[State of JavaScript in modern development | JavaScript in Modern Development]]

### Web Development with the DOM

On the web, JavaScript runs in the browser, which is based on the Document Object Model (DOM) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The UI is represented as a tree of HTML elements (nodes) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. The browser provides APIs to interact with these nodes, with the `document` object being central <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   `querySelector` finds an individual HTML element using a CSS selector (class name, ID, tag name) <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. It returns an instance of the `Element` class with properties and methods to get information or change behavior <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   `querySelectorAll` grabs multiple elements <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   `addEventListener` allows listening to events (like a button click) and assigns a function to be called when that event takes place <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

Much of web development involves listening to events and updating the UI accordingly <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### Front-End Frameworks

While [[building_applications_with_vanilla_javascript | vanilla JavaScript]] often results in imperative code (where the UI is mutated directly), many developers now use front-end frameworks (e.g., [[reactjs_overview_and_history | React]], [[react_introduction_and_history | React]]) <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. These frameworks produce declarative code, where the UI is a function of its input data <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. They encapsulate JavaScript, HTML, and CSS into components, which form a component tree representing the UI <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. Data inside a component is reactive, meaning any changes to the data automatically update the UI <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### Build Tools

After building a JavaScript application, all JavaScript files often need to be combined into a single bundle for the browser <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Module bundlers like Vite or Webpack handle this process <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Large JavaScript bundles can affect page load performance <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This can be mitigated by splitting the bundle into multiple files and using dynamic imports to load JavaScript only when needed <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## Beyond the Browser

JavaScript also runs on the server, with Node.js being the most popular runtime, allowing execution of JavaScript code via the `node` command <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. This expands JavaScript's reach to:
*   **Desktop applications**: Frameworks like Electron combine Node.js with a browser to create full-stack desktop apps <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
*   **Mobile applications**: Frameworks like React Native enable building iOS and Android apps with JavaScript <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

### Code Quality Tools

To improve code quality and make development easier, tools like TypeScript and ESLint perform static analysis <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.