---
title: Type annotations and strong typing in TypeScript
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

[[introduction_to_typescript | TypeScript]] is considered a significant tool for web developer productivity due to its impact on code quality and maintainability <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Initially, some developers, including the speaker, were resistant to learning it, especially if they were not comfortable with strong-typed languages <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. However, writing a little more code upfront with [[introduction_to_typescript | TypeScript]] can yield significant benefits as a project grows <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Benefits of Type Annotations

The primary benefit of using type annotations is enhanced tooling within an Integrated Development Environment (IDE) like VS Code <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
When working with type annotations or strong-typed [[integrating_thirdparty_libraries with_typescript | libraries]], code is automatically documented within the IDE, reducing the need to constantly refer to online documentation <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

Furthermore, the [[using_typescript_compiler_and_setting_ts_config | TypeScript compiler]] can catch bugs in advance, making code refactoring much more efficient <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This proactive bug detection prevents "insanity-inducing errors in production" by resolving "silly errors during development" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

[[introduction_to_typescript | TypeScript]] also boasts a minimal learning curve for those already familiar with [[variables_and_data_types_in_javascript | JavaScript]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This is because [[introduction_to_typescript | TypeScript]] is a superset of [[variables_and_data_types_in_javascript | JavaScript]], meaning any valid [[variables_and_data_types_in_javascript | JavaScript]] code is also valid in [[introduction_to_typescript | TypeScript]], allowing for incremental learning <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. It also enables developers to write code using [[future_of_javascript_with_potential_native_type_annotations | future JavaScript features]], which can then be transpiled to various [[variables_and_data_types_in_javascript | JavaScript]] flavors to ensure environment compatibility <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Basic Concepts: Variables and Data Types

Type annotations are fundamental to writing strongly typed code in [[introduction_to_typescript | TypeScript]] <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. There are two primary ways to apply strong typing: implicitly or explicitly <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Implicit vs. Explicit Typing

*   **Implicit Typing**: When a variable is declared and immediately assigned a value, [[introduction_to_typescript | TypeScript]] can automatically infer its type <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, assigning `10` to a variable will infer it as a `number` type <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. If a different type, like a string, is later assigned, the [[using_typescript_compiler_and_setting_ts_config | compiler]] will flag an error <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This contrasts with vanilla [[variables_and_data_types_in_javascript | JavaScript]], where such a bug would only be caught at runtime <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Explicit Typing**: If a variable is declared without an immediate assignment, or if you want to explicitly define its type, you can use a colon followed by the type (e.g., `: number`) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Without an explicit annotation, such a variable would be inferred as `any` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. A general tip is to avoid explicitly strong typing if the type is already implicitly inferred <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### The `any` Type

[[introduction_to_typescript | TypeScript]] allows developers to opt out of the type system by annotating a variable with `any` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. An `any` type means the variable can be assigned any value without the [[using_typescript_compiler_and_setting_ts_config | compiler]] performing type checking <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. While this provides flexibility, it's generally best to avoid using `any` when possible <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Custom Types

Beyond built-in [[variables_and_data_types_in_javascript | JavaScript]] types, [[introduction_to_typescript | TypeScript]] allows the creation of custom types.

### Type Aliases and Union Types

The `type` keyword allows you to define a custom type name, typically using PascalCase <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
Custom types can be simple aliases for primitive types <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. More powerfully, you can create **union types** using a pipe (`|`) to specify that a variable can be one of several types (e.g., `'bold' | 'italic'` for strings or extending with a `number` for mixed types) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Interfaces for Object Shapes

Interfaces are used to enforce the shape of an object <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. They define the types for each property within an object <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
```typescript
interface Person {
  firstName: string;
  lastName: string;
}
```
This interface can then be used to strong type objects directly, as return values from functions, or as function arguments <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
Interfaces can be made less restrictive by allowing additional properties beyond the required ones. This is achieved by adding a key with a `string` type and an `any` value type (e.g., `[key: string]: any;`) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Functions

Strong typing functions involves specifying types for both their arguments and their return values <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

*   **Typing Arguments**: Arguments are annotated similarly to variables, by adding a colon and the type after the argument name (e.g., `(x: number, y: number)`) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This ensures only specified types can be passed to the function <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Typing Return Values**: The return value type is annotated after the parentheses and before the function body (e.g., `(): number` or `(): string`) <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. The [[using_typescript_compiler_and_setting_ts_config | compiler]] will flag an error if the function's actual return type does not match the annotated type <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **`void` Return Type**: For functions that do not return a value or primarily produce side effects (like event listeners), the return type can be annotated as `void` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Arrays and Tuples

### Typing Arrays

To strong type an array, specify the element type followed by square brackets (e.g., `number[]` for an array of numbers) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. The [[using_typescript_compiler_and_setting_ts_config | compiler]] will then produce an error if an attempt is made to push a value of a different type into the array <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This is particularly useful for arrays of objects, providing intellisense when iterating over them <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### Tuples

A tuple is a [[introduction_to_typescript | TypeScript]] data structure, similar to those found in other programming languages like Python <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. Tuples are fixed-length arrays where each item has its own distinct type <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
```typescript
type MyList = [string, number, boolean?]; // Example of a tuple type
```
In the example above, `MyList` specifies that the first element must be a `string`, the second a `number`, and the third element (a `boolean`) is optional <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. Elements in tuples can be made optional by placing a question mark (`?`) after their type <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. This optional syntax can also be applied to function arguments <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## Generics

[[introduction_to_typescript | TypeScript]] generics allow you to use a type internally within a class or function without specifying it upfront <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
An example is an RxJS Observable, which is a class with an internal value that can be observed <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. The type of this internal value can be represented by a "variable type" (often denoted as `T`) that is passed in when the Observable is used <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
```typescript
class Observable<T> { /* ... */ }
// Later, specify the internal type:
const numObs: Observable<number> = new Observable<number>(/* ... */);
const personObs: Observable<Person> = new Observable<Person>(/* ... */);
```
Generics allow the internal type to be specified later in the code <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. They can also be implicitly inferred; for example, creating a new `Observable<number>` implicitly sets its internal type to `number` <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. While developers more commonly use generics rather than create them, understanding their concept is important <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.