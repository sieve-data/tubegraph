---
title: Functions and closures in JavaScript
videoId: 9emXNzqCKyg
---

From: [[fireship]] <br/> 

[[javascript_fundamentals_and_practical_concepts | JavaScript]] functions are fundamental building blocks that take an input and produce an output when called <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Understanding their behavior, especially in relation to [[variables_and_scope_in_javascript | scope]] and execution context, is crucial for any developer <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## Defining Functions <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>

Functions can be defined in a couple of ways in modern [[javascript_fundamentals_and_practical_concepts | JavaScript]]:

*   **`function` keyword**: Functions can be declared using the `function` keyword <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. These can be named <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a> or anonymous <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Arrow Syntax**: A more concise way to define functions is using the arrow (`=>`) syntax <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. If braces are omitted, the code following the arrow will implicitly return a value, allowing for single-line function definitions <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

Anonymous functions are often assigned to the value of a variable <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## Higher-Order Functions and Callbacks

[[functional_programming_with_typescript | JavaScript]] supports [[functional_programming_with_typescript | higher-order functions]] <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This means:
*   Functions can be provided as inputs or arguments to another function <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   Functions can be returned as the value from another function <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

Anonymous functions are commonly used as arguments to other functions, especially for asynchronous code, where they will be called back later after the asynchronous operation finishes executing <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Nested Functions and Closures

It's possible to define new functions within an existing function <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The outer function wraps the inner function <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### What is a Closure? <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
In its simplest sense, a [[closures_and_recursion_in_javascript | closure]] is a function defined within another function <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. The key characteristic is that the inner function references a variable that was declared in the [[variables_and_scope_in_javascript | scope]] of the outer function <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

What makes [[closures_and_recursion_in_javascript | closures]] special in [[javascript_fundamentals_and_practical_concepts | JavaScript]] is that the variable in the outer function is maintained in memory even after that outer function returns and is popped off the call stack <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. This means the inner function always has access to the [[variables_and_scope_in_javascript | state]] from the outer function at the time it was created <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

For example, if you define variables in an outer function, operate on them, and then return an inner function that references these variables, the inner function will retain access to that [[variables_and_scope_in_javascript | state]] even after the outer function has completed its execution <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

*   **Conceptual Similarity to Classes**: If you have experience with object-oriented programming, a [[closures_and_recursion_in_javascript | closure]] is conceptually very similar to a class instance <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. A function can contain some [[variables_and_scope_in_javascript | state]], and an inner function can operate on and change that [[variables_and_scope_in_javascript | state]] <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. In fact, the `class` keyword in [[javascript_fundamentals_and_practical_concepts | JavaScript]] is just syntactic sugar for functions and [[closures_and_recursion_in_javascript | closures]] <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

## The `this` Keyword in Functions

The `this` keyword refers to the current object that the code is operating in <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. Anything that is not a primitive value in [[javascript_fundamentals_and_practical_concepts | JavaScript]] is an object <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

*   **Global Context**: In a browser console, `this` by itself, or when used in a function called normally, refers to the `window` object, which is the global [[variables_and_scope_in_javascript | scope]] <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   **Object Methods**: When a function is defined as a value (method) on an object, `this` inside that function will refer to the object it's defined on <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Arrow Functions and `this`**: Arrow functions behave differently regarding `this` compared to functions defined with the `function` keyword <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. Arrow functions do not have their own `this` bindings; instead, they inherit `this` from their enclosing lexical context <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. This means `this` in an arrow function might refer to the global object if not explicitly bound <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

### Explicitly Setting `this` Context

Functions have methods like `call()` that allow you to explicitly pass in the `this` context you want to bind to the function <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. Any references to `this` inside the function will then refer to the object passed to `call()` <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.