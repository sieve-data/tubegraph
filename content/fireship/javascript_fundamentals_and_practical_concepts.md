---
title: JavaScript fundamentals and practical concepts
videoId: 9emXNzqCKyg
---

From: [[fireship]] <br/> 

To thrive as a developer in today's landscape, it's essential to understand the practical fundamental concepts of the JavaScript programming language <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This article covers key features of the language as they relate to practical programming and some of its unique aspects that can be encountered in interviews <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

## Running JavaScript Code

JavaScript code can be executed in different environments:

### Node.js (Server-Side)
You can run JavaScript directly on your machine via the command line using [[emergence_of_frameworks_and_tools_in_modern_JavaScript | Node.js]] <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. For example, typing `node index.js` in the command line will execute the code in your script <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This means you can write a backend server-side JavaScript application <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

### Browsers (Client-Side)
Most people associate [[javascript_and_frontend_development | JavaScript]] with browsers and web applications <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

#### Developer Console
Code can be run in the browser's developer console, which uses a JIT compiler (interpreter) to execute code as you type <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. However, the browser console is primarily a [[JavaScript debugging techniques | debugging tool]] <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

#### HTML `<script>` Tag
Web applications typically declare a `<script>` tag in an HTML document <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. By setting the `src` attribute to a JavaScript file, the browser will parse the HTML, see the script tag, and load and execute the script <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

Using the `defer` attribute ensures the JavaScript executes only after the HTML document is fully loaded <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. This is useful because JavaScript often references HTML elements in the body that may not be available until the document is ready <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. While [[JavaScript trends and frameworks | frameworks]] often set up script tags automatically, understanding their fundamental operation is crucial for web development <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

## Primitives and Objects

These are two of the lowest-level building blocks in the language <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

### Primitive Types
Modern JavaScript has seven primitive types <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. The most common ones include:
*   `string` <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>
*   `number` <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>
*   `boolean` <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>
*   `null` <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>
*   `undefined` <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>

A special characteristic of primitives is that they are **immutable**; their value cannot be directly changed once assigned to a variable <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. They can be reassigned to a *different* value, but not directly mutated <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

JavaScript is a dynamic, weakly typed language, so type annotations are not used in the code itself <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. However, the `typeof` operator can be used to check a type at runtime <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

#### Undefined vs. Null
*   `undefined` is the default value for a variable that hasn't had a value assigned or for a function that returns nothing <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
*   `null` represents an empty value, but it is explicitly assigned by the developer <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

### Object Type
In contrast to primitives, the `object` type represents more complex data structures like arrays, objects, and [[javascript_function_basics_and_anatomy | functions]] <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. Objects are collections of keys and values (or properties) and can be **mutated** after being assigned to a variable <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. Anything that is not a primitive type will inherit from `object` <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>, including [[javascript_function_basics_and_anatomy | functions]], arrays, and class instances <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

#### Primitive Wrapper Objects
These allow wrapping a primitive type in a class instance but should generally not be used unless there's a specific reason <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

## [[JavaScript data types and control flow | Control Flow]] and Truthy vs. Falsy

[[JavaScript data types and control flow | Conditional logic]] in JavaScript is implemented using `if` statements <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>, which can be extended with `else` and `else-if` clauses <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

### Truthy and Falsy Values
JavaScript will always try to coerce a value into a boolean when it's encountered inside a conditional statement <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
*   `true` is obviously truthy <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   Any `object` is truthy, even an empty array or an empty object <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.
*   A `string` with length is truthy <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>, but an empty string is falsy <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.
*   The `number 0` is falsy <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>, but all other numbers are truthy <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

To explicitly coerce a value to a boolean, you can use the double bang (`!!`) operator <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>. This works because a single exclamation mark (`!`) is a logical NOT operator, returning `false` if a value can be converted to `true`. Two of them effectively give you the actual boolean representation <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

### Logical Operators
*   `&&` (Logical AND): Ensures all expressions in the condition convert to `true` <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   `||` (Logical OR): Returns `true` if at least one expression is truthy <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

### Equality Operators
JavaScript provides two different equality operators:
*   **Double Equal Sign (`==`) - Abstract Comparison**: This operator attempts to make a type conversion before running the comparison <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. This can lead to unexpected behavior, and most linters recommend never using it <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.
*   **Triple Equal Sign (`===`) - Strict Equality**: This operator checks for equality on both the type and the value, providing much more predictable behavior <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

### Ternary Operator
For concise conditional variable assignment, the ternary operator (`condition ? valueIfTrue : valueIfFalse`) provides a shorthand syntax <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.

### Switch Statement
The `switch` statement is an alternative to long `if-else` chains, allowing you to compare an expression to multiple cases <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

### Try-Catch Statements
To handle errors gracefully, `try-catch` statements are used <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>. Code within the `try` block is attempted, and if an error is thrown, execution moves to the `catch` block <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. A `finally` block can be added to run code after both `try` and `catch` have executed, regardless of whether an error occurred <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.

## Variables

### Var, Let, and Const

#### `var`
The `var` keyword allows initialization, assignment, and reassignment of a variable <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. Understanding the execution context is crucial for `var` <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>.

*   **Execution Context**: This refers to how your code is interpreted, defining the relationship between how code is written and how the JavaScript engine interprets it <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
*   **Global Variables**: Variables defined anywhere in the script are considered global and available in the global execution context, meaning they can be referenced by functions elsewhere <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.
*   **Local Variables**: Variables defined inside a [[javascript_function_basics_and_anatomy | function]] are local to that function's execution context and not available in the global context <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.
*   **Undeclared Variables**: Assigning a value to an undeclared variable (which should be avoided) automatically makes it a global variable, even if done inside an enclosing function <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
*   **Hoisting**: When JavaScript processes an execution context, it effectively moves all variable declarations (and [[javascript_function_basics_and_anatomy | function]] declarations) to the top of the context <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. This means a variable referenced higher up in the code will still be considered declared, though its value assignment happens where it's defined <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>. To maintain sanity, it's best practice to declare variables at the top of their context <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

The main problem with `var` is that it makes variable scope difficult to track and can lead to name collisions in complex applications <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.

#### `let`
Introduced in [[basics_of_javascript_and_its_history | modern JavaScript]], `let` is similar to `var` but is limited to the scope of a **block statement** (e.g., inside an `if` statement or a loop) <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. Unlike `var`, `let` does not "leak" out into the parent scope <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. Variables defined with `let` can be reassigned to different values later <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>.

#### `const`
`const` is used for values that should never be reassigned, making it harder to accidentally override values in your code <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

**Recommendation**: Always use `const` unless you are certain the value will be overridden later, in which case use `let`. Avoid using `var` <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

## [[functions_and_closures_in_javascript | Functions]]

A [[javascript_function_basics_and_anatomy | function]] is a piece of code that takes an input and produces an output when called <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.

### Defining Functions
*   **`function` keyword**: Traditional way to define a function <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
*   **Arrow syntax**: A more concise way in [[basics_of_javascript_and_its_history | modern JavaScript]] <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>. If braces are omitted, the code following the arrow implicitly returns a value <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

### Important Concepts

#### Anonymous vs. Named Functions
[[javascript_function_basics_and_anatomy | Functions]] can be anonymous (without a name) or have a name that immediately follows the `function` keyword <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>. Anonymous [[javascript_function_basics_and_anatomy | functions]] are commonly assigned to variables <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.

#### Higher-Order Functions
[[JavaScript]] supports higher-order functions, meaning [[javascript_function_basics_and_anatomy | functions]] can be provided as arguments (inputs) to other [[javascript_function_basics_and_anatomy | functions]] or returned as values from them <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>. This is critical for concepts like callbacks in the [[JavaScript and Frontend Development | JavaScript event loop]], where anonymous functions are often passed as arguments to be called back later after asynchronous code finishes <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

#### Nested Functions and [[functions_and_closures_in_javascript | Closures]]
You can define new [[javascript_function_basics_and_anatomy | functions]] within a [[javascript_function_basics_and_anatomy | function]] (an inner function within an outer function) <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.

A **[[functions_and_closures_in_javascript | closure]]** is a [[javascript_function_basics_and_anatomy | function]] within a [[javascript_function_basics_and_anatomy | function]] where the inner [[javascript_function_basics_and_anatomy | function]] references a variable declared in the scope of the outer [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. The special aspect of [[functions_and_closures_in_javascript | closures]] is that the variable in the outer [[javascript_function_basics_and_anatomy | function]] is maintained in memory even after that [[javascript_function_basics_and_anatomy | function]] returns and is popped off the call stack <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>. This allows the inner [[javascript_function_basics_and_anatomy | function]] to always access the state from the outer [[javascript_function_basics_and_anatomy | function]] at the time it was created <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

A [[functions_and_closures_in_javascript | closure]] is conceptually similar to a class instance in object-oriented programming: a [[javascript_function_basics_and_anatomy | function]] contains some state, and an inner [[javascript_function_basics_and_anatomy | function]] can operate on and change that state <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>. The `class` keyword in [[JavaScript]] is essentially syntactic sugar for [[javascript_function_basics_and_anatomy | functions]] and [[functions_and_closures_in_javascript | closures]] <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>.

## Objects

An object is a data structure that allows you to associate a collection of key-value pairs, similar to a map or hash map in other languages <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.

### Defining and Accessing Objects
While it's possible to instantiate an object and add properties one by one, the **object literal syntax** is most common <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>. This involves defining an object by enclosing key-value pairs inside braces <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.

You can access the value of a key using **dot notation** (e.g., `object.key`) or **bracket notation with a string** (e.g., `object['key']`) <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>. Properties on an object can be mutated even if the object itself is defined as a `const` variable <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>.

### Functions as Object Values
[[javascript_function_basics_and_anatomy | Functions]] can be used as values on an object <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.

### The `this` Keyword
`this` is a keyword that refers to the current object the code is operating in <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
*   In the browser, if `this` is referenced by itself or in a normally called [[javascript_function_basics_and_anatomy | function]], it refers to the **`window` object** (the global scope) <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.
*   When `this` is used inside a [[javascript_function_basics_and_anatomy | function]] defined with the `function` keyword as a property of a custom object, `this` refers to that **custom object** <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
*   In contrast, **arrow [[javascript_function_basics_and_anatomy | functions]] do not have their own `this` bindings** <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>. This means `this` inside an arrow [[javascript_function_basics_and_anatomy | function]] will reference the `this` from its enclosing lexical context, which might be the global object if not nested <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>.

#### `.call()` Method
[[javascript_function_basics_and_anatomy | Functions]] have a `.call()` method that allows you to explicitly pass in the `this` context you want to bind to the [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>. Any references to `this` inside the [[javascript_function_basics_and_anatomy | function]] will then point to the object passed to `.call()` <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>.

Understanding `this` is crucial for becoming a better [[JavaScript]] developer, even if it's not used daily <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>.