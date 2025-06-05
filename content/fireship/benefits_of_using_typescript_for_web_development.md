---
title: Benefits of using TypeScript for web development
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

TypeScript is highlighted as a tool that significantly impacts web developer productivity <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While the initial thought might be to avoid writing more code, the upfront effort with TypeScript pays dividends as a project grows <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Core Advantages

### Enhanced Tooling and Documentation
The biggest benefit of TypeScript comes from the tooling capabilities it provides within an Integrated Development Environment (IDE) like VS Code <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. When using type annotations or working with strong-typed libraries, your code is automatically documented in the IDE <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This reduces the need to constantly refer to online documentation for the libraries you use <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

For example, when using the `URL` class in TypeScript, you get autocomplete and Intellisense <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Hovering over the class provides integrated documentation and specific error messages <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. You can also view the full interface, showing every property and method, though this is often unnecessary due to autocomplete <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Proactive Bug Detection
The TypeScript compiler can catch bugs in advance, making refactoring code far more efficient <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This prevents errors from occurring in production:

> [00:01:16] "Would you rather have silly errors during development or insanity inducing errors in production?"

For instance, if a variable is implicitly typed as a number, attempting to assign a string value to it will immediately result in an error <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. In plain JavaScript, such a bug would only be caught during runtime <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Minimal Learning Curve
For developers already familiar with JavaScript, there is virtually no learning curve for TypeScript <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This is because TypeScript is a superset of JavaScript, meaning any valid JavaScript code is also valid TypeScript code <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This allows developers to [[getting_started_with_typescript_and_its_installation | learn TypeScript incrementally]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Future-Proofing with Transpilation
TypeScript enables developers to write code using future JavaScript features without concern for current environment support <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The TypeScript compiler (TSC) can transpile (convert) TypeScript code into various JavaScript flavors, including older versions like ES3 or modern versions like ESNext <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This capability allows the use of features like `async/await` which can then be transpiled into compatible JavaScript for older environments <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## How TypeScript Works
TypeScript code cannot run directly in browsers or Node.js environments <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Instead, the TypeScript compiler converts it into vanilla JavaScript <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### TypeScript Compiler (TSC)
To begin, TypeScript needs to be installed globally using NPM, which provides access to the `tsc` command <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The `tsc` command runs the TypeScript compiler <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. For example, running `tsc index.ts` will create an `index.js` file, which is the executable JavaScript code <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

The compiler's behavior can be customized using a `tsconfig.json` file, which automatically gets picked up when `tsc` is run <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Key options include:
*   **`target`**: Specifies the JavaScript flavor to compile to (e.g., `esnext` for the latest JavaScript version) <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **`watch: true`**: Recompiles the code automatically every time a file is saved <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **`lib`**: Allows automatic inclusion of typings for specific environments like the DOM or ES2017, enabling TypeScript to compile code with native classes without errors <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Handling Third-Party Libraries
Many mainstream libraries, like Firebase, ship with type declarations automatically <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. For libraries that don't (e.g., Lodash), TypeScript will issue a warning about missing declarations, meaning no autocomplete or Intellisense <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. However, a large community-maintained mono-repo provides type declarations (e.g., `@types/lodash`) that can be installed to enable full tooling support <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## [[type_annotations_and_error_checking_in_typescript | Type Annotations and Type Inference]]
TypeScript offers two primary ways to strong type your code: implicitly and explicitly <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

*   **Implicit Typing (Type Inference)**: If a variable is assigned a value during declaration, TypeScript automatically infers its type <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, `let x = 10;` will implicitly type `x` as a `number` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. If a variable is declared without an initial value and no explicit type, it defaults to an `any` type, which allows assignment of any value without compiler checks <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. While flexible, using `any` should generally be avoided <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

*   **Explicit Typing**: You can explicitly annotate a variable with a type using a colon followed by the type name (e.g., `let x: number;`) <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This is necessary when a variable doesn't have an initial value <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## [[typescript_interfaces_and_custom_types | Custom Types and Interfaces]]
Beyond built-in types, TypeScript allows you to [[typescript_interfaces_and_custom_types | create your own types]] <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Custom Types**: Defined using the `type` keyword, typically in Pascal case <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. They can be simple (e.g., `type Style = string;`) or more complex, such as [[typescript_interfaces_and_custom_types | union types]] (e.g., `type Style = "bold" | "italic";`) which restrict values to a predefined set <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **[[typescript_interfaces_and_custom_types | Interfaces]]**: Used to enforce the shape of objects <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This is crucial for preventing bugs when composing objects or class instances that don't have the correct structure <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. An interface defines the types for each property of an object (e.g., `interface Person { firstName: string; lastName: string; }`) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Interfaces can also be made less restrictive by allowing additional properties beyond the required ones <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

## [[working_with_functions_and_arrays_in_typescript | Functions and Arrays]]
TypeScript provides strong typing for functions and arrays, ensuring data consistency.

### Functions
When strong typing a function, you define types for both its arguments and its return value <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Argument Typing**: Arguments are annotated with a colon and their type (e.g., `function power(x: number, y: number)`) <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This prevents invalid types (like strings) from being passed to numerical operations <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Return Value Typing**: The return type is specified after the parentheses and before the function body (e.g., `function power(x: number, y: number): number`) <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. If a function doesn't return a value (e.g., a side effect), its return type can be set to `void` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Optional Arguments**: Function arguments can be made optional using a question mark after the parameter name <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Arrays and Tuples
*   **Arrays**: An array can be forced to contain only specific types (e.g., `number[]` for an array of numbers) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This is particularly useful for arrays of objects, providing Intellisense when iterating over them based on defined [[typescript_interfaces_and_custom_types | interfaces]] <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Tuples**: TypeScript introduces tuples, which are fixed-length arrays where each item has its own specific type <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. For example, `type MyList = [string, number, boolean]` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. Tuple elements can also be made optional with a question mark <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

## Generics
TypeScript generics allow a type to be used internally within a class or function, providing flexibility <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. A common example is an RxJS observable, where a variable type (often denoted by `T`) can be passed in to strong type the observable's internal value <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This means the internal type can be specified later, such as `Observable<number>` or `Observable<Person>` (using the `Person` interface) <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Generics can also be implicitly inferred based on the value provided <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. While often used, understanding how to create them is also important <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.