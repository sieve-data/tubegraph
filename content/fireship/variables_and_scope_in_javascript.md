---
title: Variables and scope in JavaScript
videoId: 9emXNzqCKyg
---

From: [[fireship]] <br/> 

Understanding variables and their scope is a fundamental concept for [[javascript_fundamentals_and_practical_concepts | JavaScript]] developers, especially to navigate some of the language's more "weirder parts" and common interview questions, such as [[functions_and_closures_in_javascript | closures]] and hoisting <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Execution Context

The execution context defines how [[javascript_fundamentals_and_practical_concepts | JavaScript]] code is interpreted <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. It establishes the relationship between how code is written and how the [[basics_of_javascript_and_its_history | JavaScript]] engine will interpret it <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   **Global Execution Context**
    Variables defined anywhere in a script are considered global variables, meaning they are available throughout the global execution context <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This means a variable defined globally can be referenced by a [[javascript_function_basics_and_anatomy | function]] elsewhere in the code <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Conceptually, the global scope can be thought of as an imaginary [[javascript_function_basics_and_anatomy | function]] that wraps the entire script <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **[[javascript_function_basics_and_anatomy | Function]] Execution Context**
    When additional [[javascript_function_basics_and_anatomy | functions]] are defined, they create a different execution context for defining variables <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. A variable defined inside a [[javascript_function_basics_and_anatomy | function]] is a local variable and is not available in the global context, which would result in a reference error if attempted <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Undeclared Variables**
    Assigning a value to an undeclared variable (which is generally discouraged) will automatically assign it as a global variable, even if the assignment occurs within an enclosing [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Hoisting

Hoisting is a behavior where [[variable_declaration_and_scope_in_javascript | JavaScript]] effectively moves all variable declarations to the top of their current execution context during the processing phase <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This means a variable can be referenced "higher up" in the code before its explicit declaration, and it will still be considered declared within that scope <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. However, the actual assignment of a value to the variable will still occur at the line where it is defined <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. To maintain code clarity and sanity, it is advisable to declare variables at the top of their context <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Variable Declaration Keywords

In [[variable_declaration_and_scope_in_javascript | JavaScript]], variables can be declared using `var`, `let`, or `const`.

### `var`

The `var` keyword allows a variable to be initialized, assigned a value, and then reassigned a different value later in the code <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

*   **Problems with `var`:**
    *   It can be difficult to track the scope of `var` variables <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   `var` declarations can "leak" out into the parent scope from block statements like `if` statements or loops <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   It can lead to name collisions as applications grow in complexity <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Recommendation:** In modern [[variable_declaration_and_scope_in_javascript | JavaScript]], it is recommended to never use `var` due to these issues <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### `let`

The `let` keyword was introduced in modern [[variable_declaration_and_scope_in_javascript | JavaScript]] as an alternative to `var` <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

*   **Scope:** `let` is block-scoped, meaning variables declared with `let` are limited to the scope of the block statement (e.g., `if` statement, loop) where they are defined <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. This prevents them from leaking into the parent scope like `var` <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Reassignment:** Similar to `var`, variables defined with `let` can be reassigned to different values later in the code <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### `const`

The `const` keyword is used for declaring constants, values that should not be reassigned after their initial assignment <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. This helps prevent accidental overwriting of values <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

*   **Immutability:** While `const` prevents reassignment of the variable itself, it's important to note that if a `const` variable holds an object, the properties of that object can still be mutated <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This aligns with the concept that objects are mutable, unlike primitive data types <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Recommendation:** A good general rule is to always use `const` unless there is a known reason that the value will need to be reassigned later, in which case `let` should be used <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.