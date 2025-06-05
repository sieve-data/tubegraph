---
title: Getting started with TypeScript and its installation
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

[[benefits_of_using_typescript_for_web_development | TypeScript]] has had a significant impact on web developer productivity, even for those initially resistant to learning it <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This article covers the basic concepts needed to work successfully with [[benefits_of_using_typescript_for_web_development | TypeScript]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

> [!NOTE] Resource
> A recommended resource for advanced [[benefits_of_using_typescript_for_web_development | TypeScript]] concepts is the "TypeScript Deep Dive" book by Basarat Syed, which is free and open source <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Why Use TypeScript?
Initially, some developers may be resistant to learning [[benefits_of_using_typescript_for_web_development | TypeScript]] due to discomfort with strongly typed languages <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. However, writing a little more code upfront with [[benefits_of_using_typescript_for_web_development | TypeScript]] pays significant dividends as a project grows <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The biggest benefit of [[benefits_of_using_typescript_for_web_development | TypeScript]] is its tooling within Integrated Development Environments (IDEs) like VS Code <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. When using type annotations or working with strongly typed libraries, code is automatically documented in the IDE, reducing the need to refer to online documentation <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Additionally, the [[type_annotations_and_error_checking_in_typescript | TypeScript]] compiler can catch bugs in advance, making code refactoring more efficient <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. A Reddit post encapsulates this benefit: "Would you rather have silly errors during development or insanity inducing errors in production?" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>

## TypeScript vs. JavaScript
There's virtually no learning curve for developers who already know JavaScript, as [[benefits_of_using_typescript_for_web_development | TypeScript]] is a superset of JavaScript <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This means any valid JavaScript code is also valid [[benefits_of_using_typescript_for_web_development | TypeScript]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Developers can learn it incrementally <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. [[benefits_of_using_typescript_for_web_development | TypeScript]] also allows writing code using future JavaScript features without worrying about environmental support, as it can be transpiled to multiple JavaScript flavors <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Installation and Basic Compilation
To get started, [[installing_and_setting_up_nodejs | install]] [[benefits_of_using_typescript_for_web_development | TypeScript]] globally using NPM <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>:
```bash
npm install -g typescript
```
This command provides access to the `tsc` command, which runs the [[benefits_of_using_typescript_for_web_development | TypeScript]] compiler <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. As of the video, version 3.1 was being used <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

[[benefits_of_using_typescript_for_web_development | TypeScript]] code cannot run directly in browsers or Node.js; it must be converted to vanilla JavaScript using the compiler <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

1.  **Create a `.ts` file**: For example, `index.ts` <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
2.  **Write JavaScript code**: `console.log("hello world")` <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  **Compile**: Run `tsc index.ts` in the command line <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
4.  **Output**: This creates an `index.js` file, which is the executable JavaScript code <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

By default, [[benefits_of_using_typescript_for_web_development | TypeScript]] compiles to ES3 <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. When an `async` function is written in a `.ts` file and compiled, the output JavaScript may appear "crazy-looking" due to transpilation to support `async/await` in older ES versions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Configuring the TypeScript Compiler with `tsconfig.json`
The [[benefits_of_using_typescript_for_web_development | TypeScript]] compiler is highly sophisticated and offers many customization options <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. While options can be passed via the command line, the standard approach is to create a `tsconfig.json` file, which the `tsc` command automatically picks up <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Key options in `tsconfig.json`:
*   `target`: Specifies the JavaScript flavor your code will be compiled to <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Setting `target` to `esnext` allows `async/await` to compile natively, as it targets the latest JavaScript version <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   `watch: true`: Automatically recompiles code every time a file is saved, eliminating the need to manually rerun `tsc` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   `lib`: Allows automatic inclusion of typings for specific environments, such as the DOM or ES2017 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Including the `Dom` library enables [[benefits_of_using_typescript_for_web_development | TypeScript]] to compile code with native DOM classes without errors <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This provides autocomplete and Intellisense for DOM classes like `URL`, integrated documentation on hover, and error messages <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Developers can also right-click and go to "Taipings" for an explicit view of the interface, including all properties and methods <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Working with Third-Party Libraries
When using third-party libraries (e.g., Lodash), you might need to [[type_annotations_and_error_checking_in_typescript | install]] type declarations separately if the library doesn't ship with them automatically <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For example, if you import Lodash without its type declarations, [[benefits_of_using_typescript_for_web_development | TypeScript]] will warn that no declarations are found, meaning no autocomplete or Intellisense <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

However, a large mono-repository exists with community-maintained types. [[installing_and_setting_up_nodejs | Installing]] these types (e.g., `@types/lodash`) in your development environment provides autocomplete and Intellisense for all library functions <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## Type Annotations
[[type_annotations_and_error_checking_in_typescript | Type annotations]] allow for strong typing of code, either implicitly or explicitly <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

*   **Implicit Typing**: If a variable is assigned a value when declared, its type is automatically inferred <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. For instance, `let x = 10;` will implicitly type `x` as a `number`. If a string is later assigned to `x`, [[benefits_of_using_typescript_for_web_development | TypeScript]] will flag an error, catching a bug that vanilla JavaScript would only reveal at runtime <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. If no value is assigned upfront, the type will be inferred as `any` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Explicit Typing**: To explicitly annotate a variable with a type, use a colon followed by the type (e.g., `let x: number;`) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This ensures only values of that specific type can be assigned.
*   **The `any` Type**: [[benefits_of_using_typescript_for_web_development | TypeScript]] allows opting out of the type system by annotating a variable with `any` (e.g., `let x: any;`). This means the variable can be assigned any value, and the compiler will not type check it <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. While it offers flexibility, it's generally best to avoid `any` when possible <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Redundancy**: If a variable has an implicit type (e.g., `let x = 10;`), explicitly adding the type annotation (`let x: number = 10;`) is redundant <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Custom Types and Interfaces
Beyond built-in types, you can create your own types from scratch <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Custom Types**: Define a type with a name (typically PascalCase) and assign it to a primitive type or a union of types <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. For example, `type Style = "bold" | "italic";` creates a union type allowing only "bold" or "italic" as values <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. These can even include different primitive types, like strings and numbers <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **[[typescript_interfaces_and_custom_types | Interfaces]]**: For strongly typing objects with multiple properties, [[typescript_interfaces_and_custom_types | interfaces]] enforce the shape of an object <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. For example, a `Person` [[typescript_interfaces_and_custom_types | interface]] could define `firstName` and `lastName` as `string` types <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This [[typescript_interfaces_and_custom_types | interface]] can be used to strong type objects directly, or as return values or arguments for functions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Optional Properties in [[typescript_interfaces_and_custom_types | Interfaces]]**: To allow additional properties beyond the required ones, you can add a key with a `string` type and an `any` value type (e.g., `[key: string]: any;`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This requires the specified properties while allowing any other property to be added <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## [[working_with_functions_and_arrays_in_typescript | Working with Functions and Arrays]]
### Functions
[[working_with_functions_and_arrays_in_typescript | Strong typing a function]] involves typing both its arguments and its return value <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Argument Annotation**: Arguments are annotated similarly to variables, using a colon followed by the type (e.g., `function power(x: number, y: number)`). This ensures only specified types (like numbers) can be passed as arguments <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Return Value Annotation**: A specific return value type can be annotated after the parentheses and before the function body's curly braces (e.g., `function power(x: number, y: number): number`). If the function returns a different type, [[benefits_of_using_typescript_for_web_development | TypeScript]] will flag an error <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **`void` Type**: For functions that do not return a value or primarily create side effects (e.g., event listeners), the return value can be typed as `void` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Arrays and Tuples
*   **Strong Typing Arrays**: To force an array to contain only specific types (e.g., numbers), annotate it with the type followed by brackets (e.g., `number[]`). This will produce an error if a non-matching type is pushed into the array <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This is particularly useful for arrays of objects, providing Intellisense when iterating over them <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Tuples**: Tuples are a [[benefits_of_using_typescript_for_web_development | TypeScript]] data structure (found in other languages like Python) that represent a fixed-length array where each item has its own specific type <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. For example, `type MyList = [string, number, boolean];` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Optional Tuple Values**: Values within a tuple can be made optional by placing a question mark after their type (e.g., `type MyList = [string, number?, boolean?];`) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This question mark syntax can also be used to make function arguments optional <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## Generics
[[benefits_of_using_typescript_for_web_development | TypeScript]] generics allow you to use a type internally within a class or function without specifying it upfront <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. A common example is an RxJS `Observable`, which is a class with an internal observable value <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. The `T` in `Observable<T>` represents a variable type that can be passed in to strong type the observable's internal value <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This means the internal type can be specified later, such as `Observable<number>` or `Observable<Person>` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. Generics can also be inferred implicitly when creating a new instance <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. While developers more often use generics than create them, understanding them is important <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## Conclusion
This overview provides a foundational understanding of [[benefits_of_using_typescript_for_web_development | TypeScript]]'s power <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. Further topics could include [[object_oriented_programming_with_typescript | Object Oriented Programming with TypeScript]], [[functional_programming_with_typescript | Functional Programming with TypeScript]], or decorators <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.