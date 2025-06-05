---
title: Introduction to TypeScript
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

TypeScript is a powerful tool that significantly impacts web developer productivity <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The speaker initially resisted learning it due to discomfort with [[type_annotations_and_strong_typing_in_typescript | strong typed languages]] and a desire to avoid writing more code <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. However, writing a little more code upfront with TypeScript pays big dividends as a project grows <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Benefits of TypeScript

The biggest benefit of TypeScript is the enhanced tooling it provides in Integrated Development Environments (IDEs) like VS Code <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Automatic Documentation** <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>: When using [[type_annotations_and_strong_typing_in_typescript | type annotations]] or working with [[type_annotations_and_strong_typing_in_typescript | strong typed]] libraries, code is automatically documented in the IDE, reducing the need to refer to online documentation <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This includes integrated documentation, error messages, and explicit views of interfaces with properties and methods <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Early Bug Detection** <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>: The TypeScript compiler can catch bugs in advance, which is a more efficient way to refactor code <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    > "Would you rather have silly errors during development or insanity inducing errors in production?" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   **Low Learning Curve** <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>: There is virtually no learning curve if you already know JavaScript because TypeScript is a superset of JavaScript, meaning any valid JavaScript code is also valid TypeScript <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This allows for incremental learning <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Future JavaScript Features** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>: TypeScript allows developers to write code with future JavaScript features without worrying about environment support, as it can be transpiled to multiple JavaScript flavors <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Getting Started with TypeScript

### Installation and Setup
1.  **[[installing_and_setting_up_typescript_with_npm | Install TypeScript globally with NPM]]** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>: This provides access to the `tsc` command, which runs the TypeScript compiler <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   `npm install -g typescript` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
    *   (At the time of the video, version 3.1 was being used) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>
2.  **Create a `.ts` file** <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>: TypeScript code cannot run directly in environments like browsers or [[introduction_to_nodejs | Node.js]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Compile with `tsc`** <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>: Use the TypeScript compiler (`tsc`) to convert `.ts` files into vanilla JavaScript (`.js`) files <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   Example: `tsc index.ts` will create `index.js` <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   By default, TypeScript compiles to ES3 <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### [[using_typescript_compiler_and_setting_ts_config | Using the TypeScript Compiler and Setting TSConfig]]
The compiler is highly sophisticated and offers many options to customize its behavior <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. While options can be passed via the command line, the standard approach is to use a `tsconfig.json` file <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **`tsconfig.json`** <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>: This file is automatically picked up when `tsc` is run <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. While it can seem overwhelming, only a few options are typically needed <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   **`target`** <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>: Defines the JavaScript flavor the code will be compiled to (e.g., `esnext` for latest features like `async/await`) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   **`watch: true`** <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>: Automatically recompiles the code every time a file is saved, eliminating the need to manually rerun `tsc` <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   **`lib`** <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>: Allows for automatic inclusion of typings for specific environments (e.g., `DOM` for web applications, `ES2017`) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This enables TypeScript to compile code with native classes and provide autocomplete/IntelliSense <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### [[integrating_thirdparty_libraries_with_typescript | Integrating Third-Party Libraries]]
*   Many mainstream libraries (e.g., Firebase) ship with type declarations automatically <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   For libraries that don't (e.g., Lodash), a warning about missing declarations will appear <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   A large community-maintained mono-repo exists (`@types/`) where development-only type packages can be installed via NPM to provide autocomplete and IntelliSense for external libraries <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Core TypeScript Concepts

### [[type_annotations_and_strong_typing_in_typescript | Type Annotations and Strong Typing]]
TypeScript allows for strong typing of code, either implicitly or explicitly <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Implicit Typing (Type Inference)** <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>: If a variable is assigned a value when declared, its type is automatically inferred (e.g., `let x = 5;` infers `x` as a `number`) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    *   If you have an implicit type, it's generally redundant to explicitly strong type it <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Explicit Typing** <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>: When a variable is declared without an initial value, it's inferred as an `any` type by default <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. To explicitly define its type, use `variable: Type` (e.g., `let myVar: number;`) <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **`any` Type** <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>: Annotating a variable with `any` opts out of the type system for that variable, allowing it to be assigned any value without type checking <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. While flexibility is gained, it's ideally avoided when possible <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Custom Types
Beyond built-in primitive types, you can create your own types <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Type Aliases**: Define a type with a name (typically Pascal Case) <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   Example: `type Style = string;` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>
*   **Union Types**: Combine multiple types using a pipe (`|`) to allow a variable to be one of several types (e.g., `type Style = "bold" | "italic" | number;`) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Interfaces
Interfaces enforce the shape of objects, preventing bugs from incorrectly shaped objects or class instances <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   Define properties and their types within an interface (e.g., `interface Person { firstName: string; lastName: string; }`) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   Interfaces can be used to [[type_annotations_and_strong_typing_in_typescript | strong type]] objects, function arguments, or return values <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Index Signatures**: To make an interface less restrictive while maintaining required properties, an index signature can be added (e.g., `[key: string]: any;` allows any additional string-keyed properties) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### Functions
[[type_annotations_and_strong_typing_in_typescript | Strong typing]] functions involves defining types for arguments and return values <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Argument Types**: Annotate arguments using `argument: Type` (e.g., `function power(x: number, y: number)`) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Return Value Types**: Annotate after the parentheses and before the curly brackets (e.g., `function power(x: number, y: number): number { ... }`) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **`void` Type**: Used for functions that do not return a value or create side effects (e.g., event listeners) <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Arrays
Arrays can be [[type_annotations_and_strong_typing_in_typescript | strong typed]] to only contain specific types <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   Syntax: `type[]` (e.g., `let numbers: number[];`) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   This is particularly useful for arrays of objects, providing IntelliSense when iterating over them (e.g., `Person[]` for an array of `Person` objects) <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Tuples
Tuples are a data structure unique to TypeScript (also found in other languages like Python) <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   They are fixed-length arrays where each item has its own specific type <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   Example: `type MyList = [string, number, boolean];` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Optional Values**: Items in a tuple can be made optional using a question mark after the type (e.g., `[string, number?, boolean?]`) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. This syntax can also make function arguments optional <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Generics
Generics allow you to use a type internally within a class or function, deferring the specific type definition until later <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   Example: An RxJS `Observable<T>` <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>, where `T` represents a variable type that can be passed in to [[type_annotations_and_strong_typing_in_typescript | strong type]] the observable's internal value <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   This enables specifying the internal type at a later point in the code (e.g., `Observable<number>` or `Observable<Person>`) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   Generics can also be inferred implicitly (e.g., `new Observable(123)` will infer an internal `number` type) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   While primarily used for consuming generics, understanding their creation is important <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

For more advanced concepts like object-oriented vs. functional programming in TypeScript or decorators, further exploration is needed <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.