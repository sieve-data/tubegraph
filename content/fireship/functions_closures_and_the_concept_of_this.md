---
title: Functions closures and the concept of this
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

## Functions

Functions are fundamental building blocks in [[javascript_fundamentals_and_practical_concepts | JavaScript]] <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. They operate by accepting an input, known as an argument, and can optionally return a value to be used elsewhere <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Function Definitions vs. Expressions
When the `function` keyword is used on its own, it's referred to as a function definition or statement <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. However, functions are also considered objects in [[javascript_fundamentals_and_practical_concepts | JavaScript]] <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This allows them to be used as [[function_declarations_vs_expressions_in_javascript | expressions]], meaning they can be assigned to [[variables_and_scope_in_javascript | variables]] <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This capability is key to constructing [[concept_of_pure_functions_and_higherorder_functions | higher-order functions]], where a function serves as an argument or a return value <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Passing Arguments
When passing arguments to a function:
*   **Primitives:** A primitive value, such as a number, is passed by value <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This creates a copy of the original variable <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Objects:** If the argument is an object, it's stored in the Heap memory and passed by reference <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This means multiple parts of the code might be mutating the same object <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Closures

Functions can be nested, which allows for the creation of a [[closures_and_recursion_in_javascript | closure]] <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. A closure encapsulates data and logic from the rest of the program <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

Normally, when a function is called, variables with primitive values are stored on the call stack, which acts as the browser's short-term memory <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. However, with a closure, the inner function can still access variables in the outer function, even after the initial outer function call has completed <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This persistence occurs because [[javascript_fundamentals_and_practical_concepts | JavaScript]] automatically stores the data from the outer function in Heap memory, allowing it to persist across function calls <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## The `this` Keyword

The `this` keyword in [[javascript_fundamentals_and_practical_concepts | JavaScript]] references an object, and which object it references depends on how the function is called <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

*   **Global Scope:** When a function is called from the global scope, `this` references the `window` object in the browser <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Object Methods:** If a function is attached to an object and called by that object, `this` will be a reference to that specific object <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Manual Binding:** A function can be manually bound to a different object using the `bind` method <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Arrow Functions and `this`
Modern [[javascript_fundamentals_and_practical_concepts | JavaScript]] provides [[arrow_functions_and_their_benefits | arrow functions]] as an alternative way to define functions <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. A key characteristic of [[arrow_functions_and_their_benefits | arrow functions]] is that they do not have their own `this` value <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. They are also always anonymous, making them well-suited for [[function_declarations_vs_expressions_in_javascript | function expressions]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.