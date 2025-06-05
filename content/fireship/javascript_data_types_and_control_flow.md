---
title: JavaScript data types and control flow
videoId: 9emXNzqCKyg
---

From: [[fireship]] <br/> 

Understanding the [[javascript_fundamentals_and_practical_concepts | practical fundamental concepts]] of the JavaScript programming language is essential for developers <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

## Running JavaScript Code <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>

JavaScript code can be run in various environments:
*   **Command Line (Node.js)**: By installing Node.js, a JavaScript script (e.g., `index.js`) can be executed directly from the command line using `node index.js` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This is considered a backend server-side application <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Browser Developer Console**: Code can be executed directly in the browser's developer console, which uses a JIT compiler (interpreter) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This is primarily a debugging tool <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **HTML Document (`<script>` tag)**: For web applications, JavaScript code is declared within a `<script>` tag in an HTML document <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   An `index.html` file can contain a `<script>` tag with a `src` attribute pointing to a JavaScript file (e.g., `index.js`) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   The `defer` attribute on a script tag ensures the JavaScript executes only after the HTML document is fully loaded <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This is useful because JavaScript often references HTML elements that need to be available <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   While frameworks often set up script tags automatically, understanding their function is important for web development <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Primitives and Objects (Data Types) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>

[[JavaScript objects and their properties | JavaScript]] categorizes data into two fundamental building blocks: primitives and objects <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Primitive Types <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
There are seven primitive types in modern JavaScript <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. The most common ones include:
*   `string` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
*   `number` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
*   `boolean` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
*   `null` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>
*   `undefined` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>

A key characteristic of primitives is their **immutability**: their value cannot be directly changed once assigned to a variable <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. They can be *reassigned* to a different value, but the original primitive value itself remains unchanged <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

JavaScript is a dynamic, weakly typed language, meaning explicit type annotations are not used in the code <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. The `typeof` operator can be used to check a variable's type at runtime <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

#### `undefined` vs. `null` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
*   `undefined`: The default value for a variable that has not been assigned a value, or for a function that returns nothing <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   `null`: Represents an empty value, but it is explicitly assigned by the developer <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Object Type <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
The object type represents more complex data structures like arrays, objects, and [[javascript_function_basics_and_anatomy | functions]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   [[JavaScript objects and their properties | Objects]] are collections of keys and values (or properties) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   Unlike primitives, objects can be **mutated** (changed) after being assigned to a variable <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Anything that is not a primitive type will inherit from the object type, including [[functions_and_closures_in_javascript | functions]], arrays, or any class instances <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Primitive Wrapper Objects**: While existing, these allow wrapping a primitive type in a class instance, but they are generally not recommended for use <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Control Flow and Truthiness vs. Falsiness <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>

### Conditional Statements (`if`/`else if`/`else`) <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>
Conditional logic is implemented with `if`, `else if`, and `else` statements <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Truthiness and Falsiness <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>
JavaScript attempts to coerce any value into a boolean when encountered in a conditional statement <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Truthy values**:
    *   `true` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
    *   Any object (even empty arrays or objects) <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>
    *   Strings that have length <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>
    *   All numbers except `0` <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>
*   **Falsy values**:
    *   An empty string <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
    *   The number `0` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>

To explicitly coerce a value to a boolean, use the double bang (`!!`) operator <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. The single exclamation mark (`!`) is a logical NOT operator, returning `false` if a value can be converted to `true` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Logical Operators <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>
*   **Logical AND (`&&`)**: Ensures all expressions in the condition are true <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Logical OR (`||`)**: Returns true if at least one of the expressions is true <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Equality Operators <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
JavaScript provides two distinct equality operators:
*   **Abstract Comparison (`==`)**: This operator attempts to perform type conversion before comparing values <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Most linters advise against its use due to its unpredictable behavior <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Strict Equality (`===`)**: This operator checks for equality on both the type and the value, providing more predictable behavior <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Ternary Operator <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>
The ternary operator provides a shorthand syntax for defining a variable based on an `if-else` statement <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It follows the structure: `condition ? valueIfTrue : valueIfFalse` <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### Switch Statement <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
A `switch` statement allows comparing an expression to multiple cases <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. It can be a good alternative to `if-else` statements when there are many conditions to check <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Error Handling (`try-catch-finally`) <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>
Code can be wrapped in a `try-catch` statement <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>:
*   The `try` block contains the code to attempt <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   If an error is `throw`n, execution moves to the `catch` block, which receives the error <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   A `finally` block can be added to execute code after both `try` and `catch` blocks have finished, regardless of whether an error was thrown <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Variables <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>

Understanding variables requires grasping the concept of **execution context** <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. This refers to how code is interpreted, defining the relationship between how code is written and how the JavaScript engine executes it <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### `var` <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>
*   Variables declared with `var` can be initialized, assigned a value, and then reassigned later <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Scope**: `var` variables are either global or function-scoped <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   A global variable, declared anywhere in the script, is available in the global execution context <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   Variables defined inside a [[javascript_function_basics_and_anatomy | function]] are local to that function's execution context and not available globally <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Weirdness**:
    *   Assigning a value to an undeclared variable (which should be avoided) automatically makes it a global variable, even if done inside a function <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   **Hoisting**: When JavaScript processes an execution context, it "hoists" all variable declarations to the top of that context <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This means a variable declared with `var` can be referenced before its declaration in the code, but its assignment will still happen at the point where it's defined <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   **Problems**: `var` makes it difficult to track variable scope and can lead to name collisions in complex applications <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### `let` and `const` (Modern JavaScript) <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>
Modern JavaScript introduced `let` and `const` to address the issues with `var` <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

*   **`let`**:
    *   Similar to `var` in that variables can be reassigned <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
    *   **Block-scoped**: `let` variables are limited to the scope of a block statement (e.g., inside an `if` statement or a loop) <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. They do not "leak" into the parent scope like `var` <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

*   **`const`**:
    *   Also block-scoped <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    *   Variables declared with `const` cannot be reassigned after their initial assignment <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This helps prevent accidental value overrides <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
    *   *Note*: For objects declared with `const`, the *binding* itself cannot be reassigned, but the properties of the object *can* still be mutated <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

**Best Practice**: Always use `const` unless a variable truly needs to be reassigned later, in which case use `let`. Avoid `var` entirely <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.